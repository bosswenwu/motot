#!/usr/bin/env python3
"""Validate a self-contained HTML5 Canvas game and syntax-check inline scripts."""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path


class GameHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.canvas_count = 0
        self.inline_scripts: list[str] = []
        self.script_attrs: dict[str, str] | None = None
        self.script_parts: list[str] = []
        self.errors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {k.lower(): (v or "") for k, v in attrs}
        if tag.lower() == "canvas":
            self.canvas_count += 1
        if tag.lower() == "script":
            if self.script_attrs is not None:
                self.errors.append("nested <script> tag")
            self.script_attrs = values
            self.script_parts = []
            if values.get("src", "").strip():
                self.errors.append(f"external script dependency: {values['src']}")
        if tag.lower() in {"img", "audio", "video", "source", "iframe"}:
            src = values.get("src", "").strip()
            if src.startswith(("http://", "https://", "//")):
                self.errors.append(f"remote asset dependency in <{tag}>: {src}")
        if tag.lower() == "link":
            href = values.get("href", "").strip()
            if href.startswith(("http://", "https://", "//")):
                self.errors.append(f"remote stylesheet/resource dependency: {href}")

    def handle_data(self, data: str) -> None:
        if self.script_attrs is not None:
            self.script_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "script" and self.script_attrs is not None:
            script_type = self.script_attrs.get("type", "").lower()
            if "json" not in script_type and "ld+json" not in script_type:
                self.inline_scripts.append("".join(self.script_parts))
            self.script_attrs = None
            self.script_parts = []


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("html", type=Path, help="path to the standalone game HTML file")
    args = ap.parse_args()
    path = args.html.expanduser().resolve()
    if not path.is_file():
        print(f"FAIL: file not found: {path}", file=sys.stderr)
        return 2
    text = path.read_text(encoding="utf-8")
    parser = GameHTMLParser()
    try:
        parser.feed(text)
        parser.close()
    except Exception as exc:  # HTMLParser is permissive; surface unexpected parser errors.
        print(f"FAIL: HTML parse error: {exc}", file=sys.stderr)
        return 2
    if parser.canvas_count < 1:
        parser.errors.append("no <canvas> element found")
    if not parser.inline_scripts:
        parser.errors.append("no inline JavaScript found")
    if re.search(r"@import\s+url\(\s*['\"]?https?://", text, re.I) or re.search(r"url\(\s*['\"]?(?:https?:)?//", text, re.I):
        parser.errors.append("remote CSS import or asset URL found")
    if parser.errors:
        for error in parser.errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    node = shutil.which("node")
    if node:
        for index, script in enumerate(parser.inline_scripts, start=1):
            with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as f:
                f.write(script)
                temp_path = Path(f.name)
            result = subprocess.run([node, "--check", str(temp_path)], text=True, capture_output=True)
            temp_path.unlink(missing_ok=True)
            if result.returncode:
                print(f"FAIL: inline script {index} has JavaScript syntax errors:\n{result.stderr}", file=sys.stderr)
                return result.returncode
    else:
        print("WARN: Node.js not found; skipped JavaScript syntax check.")
    print(f"PASS: {path.name}: Canvas present, {len(parser.inline_scripts)} inline script(s), no remote script/media/link assets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
