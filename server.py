from http.server import HTTPServer, BaseHTTPRequestHandler
import os

def check_and_create_status_file():
    if not os.path.exists("status.txt"):
        with open("status.txt", "w") as f:
            f.write("OFF")

def update_status(new_status):
    with open("status.txt", "w") as data_base:
        data_base.write(new_status)

def read_current_status():
    with open("status.txt", "r") as data_base:
        return data_base.read()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        if self.path == '/status-on':
            update_status('ON')
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Status changed')
        
        elif self.path == '/status-off':
            update_status('OFF')
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Status changed')
        
        else:
            self.send_response(200)
            self.end_headers()
            current_status = read_current_status()
            self.wfile.write(f'STATUS: {current_status}'.encode())

def start_server():
    print('Сервер запущен: http://localhost:5000')
    HTTPServer(('localhost', 5000), Handler).serve_forever()

check_and_create_status_file()
start_server()
