#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer
import sys

if __name__ == "__main__":
    ipaddr = (sys.argv[1])
    port = int(sys.argv[2])
    text = sys.argv[3]

    class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def do_GET(self):
            
            if self.path == '/':
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(text)
                return
            return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    Handler = MyRequestHandler
    server = SocketServer.TCPServer((ipaddr, port), Handler)

    server.serve_forever()
