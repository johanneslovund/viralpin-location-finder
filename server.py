import http.server
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
httpd = http.server.HTTPServer(("", 3456), http.server.SimpleHTTPRequestHandler)
print("Serving on http://localhost:3456")
httpd.serve_forever()
