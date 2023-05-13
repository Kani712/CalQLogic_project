import json
import requests


class SentimentAnalysis:
    def __init__(self, text, providers):
        self.text = text
        self.providers = providers
        self.headers = {}
        with open("config.json") as f:
            config = json.load(f)
            self.headers["Authorization"] = f"Bearer {config['token']}"
        self.url = "https://api.edenai.run/v2/text/sentiment_analysis"

    def analyze(self):
        results = {}
        for provider in self.providers:
            payload = {
                "providers": provider,
                'language': "en",
                'text': self.text
            }

            s = requests.Session()
            response = s.post(
                self.url, json=payload, headers=self.headers)
            result = json.loads(response.text)

            if result.get(provider):
                results[provider] = dict(list(result[provider].items())[0:-1])
            else:
                print(result)
                return result

            print(f"\n{provider}")
            print("\n", dict(list(result[provider].items())[0:-1]), '\n')
        return results


# Try-except block to handle user input for the text to be analyzed
try:
    text = input("Enter the text: ")
    if not text:
        raise ValueError("Input cannot be empty")

except Exception as e:
    print("Invalid input, please enter a valid text")
    exit()

# Try-except block to handle user input for sentiment analysis providers
try:
    providers = input("Enter a provider: ")
    if not providers:
        raise ValueError("providers cannot be empty")
    if ',' in providers:
        raise ValueError("Only one provider can be specified per request.")

except Exception as e:
    print(e)

providers = [providers.strip().lower()]
# Creating an instance of the SentimentAnalysis class
sa = SentimentAnalysis(text, providers)

# Calling the analyze function
sa.analyze()
