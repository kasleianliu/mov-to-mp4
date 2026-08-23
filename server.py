#!/usr/bin/env python3
# MOV 转 MP4 本地开发服务器
# 用法: python3 server.py
# 然后浏览器访问 http://localhost:8000
# 注意: 部署到 GitHub Pages 时无需此文件

import http.server
import socketserver
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # 根路径 -> 返回 index.html
        if self.path == '/' or self.path == '':
            self.path = '/index.html'
        super().do_GET()

    def end_headers(self):
        # 启用 cross-origin isolation (ffmpeg.wasm 需要)
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Resource-Policy', 'cross-origin')
        super().end_headers()

    def log_message(self, format, *args):
        pass

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def main():
    os.chdir(DIRECTORY)
    with ReusableTCPServer(("", PORT), Handler) as httpd:
        print("\n========================================")
        print("  MOV 转 MP4 转换器已启动")
        print("========================================")
        print(f"\n  请在浏览器打开:  http://localhost:{PORT}\n")
        print("  按 Ctrl + C 停止服务器\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n服务器已停止")
            sys.exit(0)

if __name__ == "__main__":
    main()
