from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import threading


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # content_length = int(self.headers['Content-Length'])  # 获取post数据长度
        # post_data = self.rfile.read(content_length)  # 获取post数据
        # print("接收到指令请求", post_data.decode('utf-8'))

        # 使用当前的默认回复内容进行响应
        self.send_response(200)
        self.send_header('Content-type', 'application/x-www-form-urlencoded;charset=UTF-8')
        self.end_headers()
        self.wfile.write(default_reply.encode('utf-8'))  # 发送回复内容

    def log_message(self, format, *args):
        """Override to disable logging."""
        return  # 空实现，不执行任何操作，从而不打印日志


def update_default_reply():
    """持续检查并更新默认回复内容"""
    global default_reply
    while True:
        default_reply = input("请输入指令: ")
        print("指令已下放.")
        # 可以添加逻辑来判断是否停止循环，比如输入特定命令来结束程序


def run_server(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
    print(f"指令通信端口已启动： {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    default_reply = "未设定"  # 初始化默认回复内容
    port = 7888

    # 启动回复内容更新线程
    reply_thread = threading.Thread(target=update_default_reply)
    reply_thread.daemon = True  # 设置为守护线程，主程序退出时自动结束
    reply_thread.start()

    # 运行服务器
    run_server(port)