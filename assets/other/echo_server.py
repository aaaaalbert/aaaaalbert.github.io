"""
This is a simple echo server for HTTP that echoes parts of the
URL it sees from the client. It is written in Python 2.
Most of the logic is adapted from Python's SimpleHTTPServer module.

To make the server listen on a port other than the default 8000,
supply that port as the command-line argument.
"""
import BaseHTTPServer
import urlparse

class EchoServerHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    server_version = "EchoServer/0.1"

    def do_GET(self):
        """Serve an HTTP GET request."""
        # Parse the URL and its query part, yielding a hostname (perhaps).
        parsed_URL = urlparse.urlparse(self.path)
        list_of_query_tuples = urlparse.parse_qsl(parsed_URL.query)
        query_dict = dict(list_of_query_tuples)
        hostname = query_dict.get("hostname", None)

        # Get the client's address (name from reverse-resolved IP)
        client_name = self.address_string()
        
        # Construct a reply, text-only for now.
        reply = "Hello, " + client_name
        if hostname:
            reply += " from host " + hostname
        reply += "."

        # Send the actual response now
        self.send_response(200)
        self.send_header("Content-Type", "text")
        self.send_header("Content-Length", str(len(reply)))
        self.end_headers()
        print >>self.wfile, reply


def test(HandlerClass = EchoServerHTTPRequestHandler,
         ServerClass = BaseHTTPServer.HTTPServer):
    BaseHTTPServer.test(HandlerClass, ServerClass)


if __name__ == '__main__':
    test()


