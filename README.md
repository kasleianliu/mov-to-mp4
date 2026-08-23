# MOV 转 MP4 批量转换器

一个纯浏览器端的 MOV 转 MP4 批量转换工具，基于 ffmpeg.wasm。**所有视频转换在本地浏览器完成，不会上传到任何服务器**，保护隐私。

## 功能特性

- 🎬 批量选择 / 拖拽上传多个 MOV 文件
- ⚡ 基于 ffmpeg.wasm，H.264 + AAC 编码
- 📊 实时进度条 + 全局转换进度
- 📥 单文件下载 / 全部下载 / 失败重试
- 📱 移动端友好（深色主题、触控优化）
- 🔒 隐私安全，文件不离开本地

## 在线使用

部署到 GitHub Pages 后直接访问即可：

> ⚠️ 首次访问需刷新一次页面以激活转换引擎环境

首次使用需加载转换引擎（约 30MB），请耐心等待。引擎加载完成后即可上传 MOV 文件进行转换。

## 本地运行

如需本地运行（开发或测试），需通过带跨域隔离头的 HTTP 服务器访问：

```bash
# 使用项目自带的 server.py（已配置 COOP/COEP 头）
python3 server.py

# 或使用 npx
npx serve -H --cors
```

然后浏览器访问 http://localhost:8000

## 部署到 GitHub Pages

1. Fork 或克隆本仓库
2. 在 GitHub 仓库设置中开启 Pages（Settings → Pages → Source: main 分支）
3. 访问 `https://<用户名>.github.io/<仓库名>/`

> 本项目通过 `coi-serviceworker.js` 在 GitHub Pages 上注入 COOP/COEP 头，使 ffmpeg.wasm 所需的 SharedArrayBuffer 可用。

## 项目结构

```
.
├── index.html              # 主页面
├── coi-serviceworker.js    # COOP/COEP polyfill（GitHub Pages 必需）
├── ffmpeg/                 # ffmpeg.wasm 引擎资源（约 32MB）
│   ├── ffmpeg.js
│   ├── util.js
│   ├── 814.ffmpeg.js       # worker chunk
│   ├── ffmpeg-core.js
│   └── ffmpeg-core.wasm    # 主引擎二进制（~31MB）
└── server.py               # 本地开发服务器（可选）
```

## 技术栈

- [ffmpeg.wasm](https://github.com/ffmpegwasm/ffmpeg.wasm) v0.12
- [coi-serviceworker](https://github.com/gzuidhof/coi-serviceworker) - 在不支持 COOP/COEP 头的静态托管上启用 cross-origin isolation
- 纯原生 HTML/CSS/JS，无构建依赖

## 浏览器要求

- 支持Service Worker 的现代浏览器（Chrome / Edge / Firefox / Safari 最新版）
- 需启用 JavaScript
- 建议内存 ≥ 4GB（ffmpeg.wasm 转换需占用较多内存）

## License

MIT
