import json
import requests


def call_rpc_method(url, method, params):
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({
        'jsonrpc': '2.0',
        'id': 0,
        'method': method,
        'params': params
    })

    response = requests.post(url, headers=headers, data=data)
    return response.json()['result']


def main():
    url = 'http://localhost:5000'

    text = input("Enter the text for sentiment analysis: ")
    providers = input("Enter the provider for sentiment analysis: ")

    sentiment_result = call_rpc_method(
        url, 'edenai_sentiment', {'text': text, 'providers': providers})
    print("Sentiment analysis result:", sentiment_result)

    text = input("Enter the text for named entity extraction: ")
    providers = input("Enter the provider for named entity extraction: ")

    entity_extraction_result = call_rpc_method(
        url, 'edenai_entity_extraction', {'text': text, 'providers': providers})
    print("Named entity extraction result:", entity_extraction_result)


if __name__ == '__main__':
    main()
