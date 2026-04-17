"""
Local HTTP server for Task App (Flutter web build).
Double-click serve.bat or run: python serve.py
Opens the app in your default browser at http://localhost:8080
Press Ctrl+C to stop.
"""
import http.server
import os
import sys
import webbrowser
import threading

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Suppress noisy request logs
        pass

    def end_headers(self):
        # Required CORS and caching headers for Flutter web
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()


def open_browser():
    webbrowser.open(f'http://localhost:{PORT}')


if __name__ == '__main__':
    os.chdir(DIRECTORY)
    with http.server.HTTPServer(('', PORT), Handler) as httpd:
        print(f'Task App in esecuzione su http://localhost:{PORT}')
        print('Premi Ctrl+C per chiudere.')
        print()
        # Open browser after a short delay (server needs to be ready)
        threading.Timer(0.5, open_browser).start()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nServer chiuso.')
            sys.exit(0)
