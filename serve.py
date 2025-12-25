#!/usr/bin/env python3
"""
启动本地 HTTP 服务器，用于运行圣诞树效果
使用方法: python serve.py
然后浏览器打开 http://localhost:8080/1_tree.html
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import subprocess

PORT = 8080
HOST = "0.0.0.0"

# 切换到脚本所在目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

# 添加 MIME 类型支持
Handler.extensions_map.update({
    '.js': 'application/javascript',
    '.mjs': 'application/javascript',
    '.json': 'application/json',
    '.wasm': 'application/wasm',
})

def kill_port(port):
    """杀死占用指定端口的进程"""
    try:
        # 查找占用端口的进程
        result = subprocess.run(
            ['lsof', '-ti', f':{port}'],
            capture_output=True, text=True
        )
        pids = result.stdout.strip().split('\n')

        for pid in pids:
            if pid:
                print(f"🔪 正在关闭占用端口 {port} 的进程 (PID: {pid})")
                subprocess.run(['kill', '-9', pid], capture_output=True)

        return True
    except Exception as e:
        print(f"⚠️ 无法自动清理端口: {e}")
        return False

def main():
    try:
        # 允许端口复用
        socketserver.TCPServer.allow_reuse_address = True

        with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
            url = f"http://localhost:{PORT}/1_tree.html"
            print(f"🎄 圣诞树服务器已启动!")
            print(f"📍 访问地址: {url}")
            print(f"📁 图片目录: images/")
            print(f"⌨️  按 Ctrl+C 停止服务器")
            print("-" * 40)

            # 自动打开浏览器
            webbrowser.open(url)

            httpd.serve_forever()
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"⚠️ 端口 {PORT} 已被占用，正在尝试清理...")
            if kill_port(PORT):
                print("✅ 端口已清理，正在重新启动...")
                import time
                time.sleep(0.5)
                main()  # 递归重试
            else:
                print(f"❌ 无法清理端口 {PORT}")
                sys.exit(1)
        else:
            raise
    except KeyboardInterrupt:
        print("\n👋 服务器已停止")

if __name__ == "__main__":
    main()
