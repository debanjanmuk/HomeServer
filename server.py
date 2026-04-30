from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "127.0.0.1"
PORT = 8080

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        if self.path == "/home":
            self.wfile.write(b"<html><body><h1>Ahi and Ved are the coolest kids ever!</h1><p>They love adventures, coding, and making everyone smile.</p></body></html>")
        elif self.path == "/office":
            self.wfile.write(b"<html><body><h1>Hello, world!</h1></body></html>")

    def log_message(self, format, *args):
        return  # Disable console logging for cleaner output


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), HelloHandler)
    print(f"Serving on http://{HOST}:{PORT}")
    server.serve_forever()
