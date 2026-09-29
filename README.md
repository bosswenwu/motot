# 公路狂飙

一个无需依赖和构建流程、可直接在现代浏览器中打开的单文件 HTML5 Canvas 街机摩托游戏。

## 运行

直接打开 `index.html` 即可游玩；也可用任意静态 HTTP 服务器托管。音乐与音效由浏览器 Web Audio 合成，首次点击“开始比赛”后启用。车库进度保存在当前浏览器的 `localStorage` 中。

## 操作

- `W` / `↑`：加速；`S` / `↓`：刹车
- `A` / `D` 或方向键：变线
- `J` / `K` / `Space`：侧击或自动攻击
- `1`–`4`：切换武器；`Shift`：氮气加速
- `Esc`：暂停；`M`：切换音乐和音效

## 内容

- 多种近战街机武器与车库解锁
- 五种连续推进的地形关卡
- 引擎、护甲、氮气升级与持久化车币
- 会避让交通、切换赛道并主动侧击的 AI 对手
- Web Audio 合成音乐/音效、氮气尾焰与粒子效果
- 本机前十排行榜，自动记录每场比赛积分

## 文件

- `index.html`：完整游戏（HTML、CSS、JavaScript 全部内嵌）
- `skills/canvas-moto-arcade/`：创建和扩展此类游戏的可复用 Manus Skill 与单文件校验脚本
- `.github/workflows/deploy-pages.yml`：推送到 `main` 或手动触发时，自动部署游戏页

## 排行榜与在线部署

排行榜仅保存在当前浏览器的本地存储中，不会上传或跨设备同步。GitHub Actions 只将 `index.html` 发布到 Pages，不会把 README、技能文件或工作流目录作为站点内容发布。GitHub Pages 页面是公开可访问的；从私有仓库发布需要符合 GitHub 计划资格。若仓库尚未启用 Pages，可在 Settings → Pages → Build and deployment 将 Source 设为 GitHub Actions。
