import base64
from http.server import BaseHTTPRequestHandler, HTTPServer

# Configuration
USERNAME = 'user'
PASSWORD = 'passw'
IP_ADDRESS = '0.0.0.0'
PORT = 8090

# Helper function to encode the username and password in base64
def encode_credentials(username, password):
    credentials = f"{username}:{password}".encode('utf-8')
    return base64.b64encode(credentials).decode('utf-8')

# The encoded credentials
EXPECTED_AUTH_HEADER = f"Basic {encode_credentials(USERNAME, PASSWORD)}"

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Check for the Authorization header
        auth_header = self.headers.get('Authorization')

        if auth_header == EXPECTED_AUTH_HEADER:
            # If the authentication is correct
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Hello, you've been authenticated!")
        else:
            # If the authentication is incorrect
            self.send_response(401)
            self.send_header('WWW-Authenticate', 'Basic realm=\"Login Required\"')
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Authentication required.")

def run():
    server_address = (IP_ADDRESS, PORT)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Server running on http://{IP_ADDRESS}:{PORT}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
