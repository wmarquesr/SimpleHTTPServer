#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer

# Create custom HTTPRequestHandler class
class KodeFunHTTPRequestHandler(BaseHTTPRequestHandler):
    rootdir = 'C:/Users/wesle/PycharmProjects/SimpleHTTPServer/rsc.txt'  # file location

    f = open(rootdir, 'r')  # open requested file
    file_content = f.read()

    def set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    # handle GET command
    def do_GET(self):
        try:
            if self.path.endswith('.txt'):
                self.set_response()

                message = self.file_content

                # send file content to client
                self.wfile.write(bytes(message, "utf8"))
                return

        except IOError:
            self.send_error(404, 'file not found')

    # Handle POST command
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])  # Gets the size of data
            post_data = self.rfile.read(content_length)  # Gets the data itself

            self.file_content += post_data.decode('utf-8')

            self.set_response()
            self.wfile.write(bytes(self.file_content, "utf8"))
            return

        except IOError:
            self.send_error(404, 'file not found')

    # Handle PUT command
    def do_PUT(self):
        self.do_POST()
        return

    # Handle DELETE command
    def do_DELETE(self):
        try:
            content_length = int(self.headers['Content-Length'])  # Gets the size of data
            post_data = self.rfile.read(content_length)  # Gets the data itself

            rm = post_data.decode('utf-8')

            self.file_content = str(self.file_content).replace(rm, "")

            self.set_response()
            self.wfile.write(bytes(self.file_content, "utf8"))
            return

        except IOError:
            self.send_error(404, 'file not found')


def run():
    print('http server is starting...')

    # ip and port of server
    server_address = ('127.0.0.1', 80)
    httpd = HTTPServer(server_address, KodeFunHTTPRequestHandler)
    print('http server is running...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()