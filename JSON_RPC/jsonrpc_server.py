import os
import json
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from sentiment_analysis import SentimentAnalysis
from NE import NamedEntityExtraction


def analyze_sentiment(text, providers):
    if not text:
        raise ValueError("Error: Text cannot be empty.")
    if not providers:
        raise ValueError("Error: Providers cannot be empty.")
    if ',' in providers:
        raise ValueError(
            "Error: Only one provider can be specified per request.")

    providers_list = [providers.strip().lower()]

    handler = SentimentAnalysis(text, providers_list)
    results = handler.analyze()
    log_file = "results/sentiment_analysis.log"

    with open(log_file, "a") as file:
        file.write("\n" + text)
        file.write("\n" + json.dumps(results) + "\n")

    return results


def analyze_entity_extraction(text, providers):
    if not text:
        raise ValueError("Error: Text cannot be empty.")
    if not providers:
        raise ValueError("Error: Providers cannot be empty.")
    if ',' in providers:
        raise ValueError(
            "Error: Only one provider can be specified per request.")

    providers_list = [providers.strip().lower()]

    handler = NamedEntityExtraction(text, providers_list)
    results = handler.analyze()
    log_file = "results/named_entity_extraction.log"

    with open(log_file, "a") as file:
        file.write("\n" + text)
        file.write("\n" + json.dumps(results) + "\n")

    return results


if not os.path.exists('results'):
    os.makedirs('results')

PORT = 5000
server = SimpleJSONRPCServer(('localhost', PORT))

server.register_function(analyze_sentiment, 'edenai_sentiment')
server.register_function(analyze_entity_extraction, 'edenai_entity_extraction')

print(f"Serving at port {PORT}")
server.serve_forever()
