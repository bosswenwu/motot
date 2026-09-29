---
name: canvas-moto-arcade
description: "Create or extend dependency-free, single-file HTML5 Canvas motorcycle arcade games. Use for road-racing combat prototypes with weapon selection, terrain stages, rival AI, garage upgrades, synthesized audio, exhaust effects, and portable delivery."
---

# Canvas Motorcycle Arcade Games

Build or extend a playable arcade motorcycle racer as one self-contained HTML file. Keep it easy to copy, open, and run without a package manager, build step, remote assets, or server-side setup.

## Workflow

1. **Inspect the target.** Read the requested source file and preserve its existing controls, game loop, saves, visual language, and user content. For a new game, create a dedicated output folder and one `index.html`.
2. **Turn requests into systems.** Map each requested feature to visible UI and game behavior before editing. Keep controls discoverable and support keyboard plus touch where appropriate.
3. **Implement in the single file.** Keep CSS and JavaScript inline. Use Canvas for the race scene and ordinary HTML elements for menus, HUD, shop, and dialogs. Avoid remote scripts, fonts, images, audio files, and runtime dependencies. Use original procedural shapes and names rather than copying protected game assets.
4. **Keep gameplay data-driven.** Put weapon stats, terrain profiles, upgrade costs, and rival tuning in small configuration arrays/objects. Use a bounded-delta animation loop, consistent input state, capped particle counts, and explicit cooldowns.
5. **Make rival behavior legible.** Let AI opponents choose lanes to avoid traffic and crowding, occasionally approach the player, show a brief attack tell, then attack only within range and cooldown. Provide counterplay through steering, braking, or the player's own weapon.
6. **Persist garage progress safely.** Store only compact, versioned preferences and upgrades in `localStorage`. Guard parsing and storage writes with `try/catch`; provide reasonable defaults when storage is unavailable. Award currency only on clear progression events and show prices, levels, and purchase feedback.
7. **Add audio without assets.** Use Web Audio oscillators/noise for simple music and effects when no audio files are requested. Create or resume the `AudioContext` only after a user gesture, expose a mute toggle, and tolerate unsupported or blocked audio.
8. **Add motion effects.** Emit short-lived exhaust, boost, impact, and smoke particles. Cap particle counts, tie boost color/intensity to a visible resource, and avoid unbounded allocations.
9. **Validate.** Run `python /home/ubuntu/skills/canvas-moto-arcade/scripts/validate_canvas_game.py <path-to-html>`. Fix parse errors, missing Canvas, external dependencies, or JavaScript syntax failures. If a local preview is needed, serve the folder with a lightweight static server; do not add a build system just for preview.
10. **Deliver clearly.** Provide the HTML file and, when useful, a ZIP of its containing folder. Include controls and verification notes. Write to a requested desktop only when the current Desktop connection is authorized and compatible; if unavailable, leave the verified files in the sandbox and explain how to retrieve them rather than attempting a workaround.

## Feature checklist

- [ ] Start, pause/restart, race completion, and responsive HUD
- [ ] More than one selectable weapon with distinct range, cooldown, and effect
- [ ] Stage-specific road/terrain palettes and scenery
- [ ] Garage upgrades with visible currency, costs, levels, and persistent state
- [ ] AI lane changes, traffic avoidance, attack tells, attack cooldowns, and counterplay
- [ ] Optional synthesized background loop, sound effects, and mute control
- [ ] Speed-sensitive exhaust/boost particles with a strict lifetime/count cap
- [ ] Keyboard and, where practical, touch input
- [ ] No external runtime dependency unless the user explicitly requests one
