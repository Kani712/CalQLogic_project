import os
import http.server
import socketserver
import json
from urllib.parse import urlparse, parse_qs
from sentiment_analysis import SentimentAnalysis
from NE import NamedEntityExtraction


class APIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Get the subdirectory from the URL
        subdirectory = '/edenai-sentiment'
        if self.path.startswith('/edenai-entityextraction'):
            subdirectory = '/edenai-entityextraction'
        if not self.path.startswith(subdirectory):
            error = {'error': f'Error: Path not found: {self.path}'}
            self.send_response(404)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(error).encode())
            return

        # Remove the subdirectory from the path
        self.path = self.path[len(subdirectory):]

        query = parse_qs(urlparse(self.path).query)
        text = query.get('text', [''])[0]
        providers = query.get('providers', [''])[0]

        # Validating the input
        if not text:
            error = {'error': 'Error: Text cannot be empty.'}
            self.send_response(400)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(error).encode())
            return
        if not providers:
            error = {'error': 'Error: Providers cannot be empty.'}
            self.send_response(400)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(error).encode())
            return
        if ',' in providers:
            error = {
                'error': 'Error: Only one provider can be specified per request.'}
            self.send_response(400)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(error).encode())
            return

        providers_list = [providers.strip().lower()]

        if subdirectory == '/edenai-sentiment':
            handler = SentimentAnalysis(text, providers_list)
            results = handler.analyze()
            log_file = "results/sentiment_analysis.log"
        else:
            handler = NamedEntityExtraction(text, providers_list)
            results = handler.analyze()
            log_file = "results/named_entity_extraction.log"

        # Writing the results to a file
        with open(log_file, "a") as file:
            file.write("\n" + text)
            file.write("\n" + json.dumps(results) + "\n")

        # Sending the response
        if results.get('status') == 'error':
            self.send_error(500)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(results).encode())
        else:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(results).encode())


# Create a subdirectory for the results
if not os.path.exists('results'):
    os.makedirs('results')

PORT = 5000
Handler = APIHandler

# Use ThreadingMixIn to handle multiple requests concurrently


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


httpd = ThreadedTCPServer(("", PORT), Handler)

print(f"Serving at port {PORT}")
httpd.serve_forever()
