# server.py
import http.server
import socketserver
from urllib.parse import parse_qs, urlparse

import dashboard, explore, forecast, histdata, alerts, page6

PORT = 80

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    pages = {
      "/":           dashboard,
      "/explore":    explore,
      "/forecast":   forecast,
      "/historical": histdata,
      "/alerts":     alerts,
      "/page6":      page6
    }

    def do_GET(self):
        parsed = urlparse(self.path)
        module = MyRequestHandler.pages.get(parsed.path)
        if module:
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            form = parse_qs(parsed.query)
            html = module.get_page_html(form, path=parsed.path)
            self.wfile.write(html.encode("utf-8"))
        else:
            super().do_GET()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
        print("Visit http://localhost/ in your browser")
        httpd.serve_forever()
