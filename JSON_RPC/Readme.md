**The code consists of three different files: SentimentAnalysis.py, Server.py, and client.py.**
Results are logged into **sentiment_analysis.log**

The SentimentAnalysis.py file contains a class called "SentimentAnalysis", which analyzes the sentiment of a given text using different providers such as connexun, amazon, google, microsoft, oneai, emvista, openai, lettria, and ibm. The class constructor takes two arguments, the text to analyze and the list of providers. The class has a method called "analyze" which sends a request to the API of each provider, receives the result, and stores it in a dictionary. The method then returns the dictionary containing the results for each provider.

**Requirements**

- Python 3.x
- requests
- Flask

# **Install the required packages using follwing command**

```
pip install -r requirements.txt.

```

**"sentiment_analysis.py"**

This module contains the SentimentAnalysis class which has the following attributes and methods:

**Attributes:**

- text: Input text to be analyzed.
- providers: List of sentiment analysis providers.
- headers: Dictionary of headers required to make a request to the API endpoint.
- url: URL of the API endpoint.
- Methods:
- analyze(): Sends a POST request to the API endpoint for each provider specified in the providers attribute and returns a dictionary of results for each provider.

To run this script, you need to have requests and json modules installed. You can either run this script on the command line or use it in another script.

On the command line, navigate to the directory containing the sentiment_analysis.py script and run the following command:

```Python
python sentiment_analysis.py
```

To use this script in another script, you can import the SentimentAnalysis class and create an instance of it, passing in the text and providers parameters. You can then call the analyze method on the instance to get the results.

**"server.py"**

This script defines a server using the http.server module that listens for incoming HTTP requests on a specified port. It defines a handler that will handle the incoming HTTP requests and call the SentimentAnalysis class to perform sentiment analysis on the user input text. It creates a client using the http.client module that sends an HTTP request to the server with the user input text and sentiment analysis providers. It then displays the result returned by the server in the web browser.

To run this script, you need to have http.server, http.client, and json modules installed. You can either run this script on the command line or use it in another script.

On the command line, navigate to the directory containing the server.py script and run the following command:

```Python
python server.py

```

Once the server is running, you can access it by opening a web browser and entering the following URL:

```Php
http://localhost:5000/?text=<YOUR_TEXT>&providers=<YOUR_PROVIDERS>

```

Replace <YOUR_TEXT> with the text you want to analyze and <YOUR_PROVIDERS> with the providers you want to use for analysis. If no providers are specified, it uses a default list of providers. The server returns the sentiment analysis results in JSON format.

**"client.py"**

This module is a Flask web application that sends an HTTP request to the server with the user input text and sentiment analysis providers. It then displays the result returned by the server in the web browser.

**Instructions to run the program:**

- Install the required packages using the command pip install -r requirements.txt.
- Start the server by running python server.py in the terminal.
- In a web browser, open localhost:5000.
- Enter the text to be analyzed and select the sentiment analysis providers.
- Click on the "Analyze" button.
- The sentiment analysis results will be displayed on the web page.

To run this script, you need to have Flask module installed. You can run this script on the command line or use it in another script.

On the command line, navigate to the directory containing the client.py script and run the following command:

```python

python client.py

```

Once the client is running, you can access it by opening a web browser and entering the following URL:

```php
http://localhost:5001/

```

You will be prompted to enter the text you want to analyze and the providers you want to use for analysis. If no providers are specified, it uses a default list of providers. The client sends the input to the server using an HTTP request and displays the sentiment analysis results in the web browser.
**Note: The providers parameter in the SentimentAnalysis class can be set to any combination of the following providers:**

- connexun
- amazon
- google
- microsoft
- oneai
- emvista
- openai
- lettria
- ibm

If the providers parameter is not specified, the default providers are used, which are all the providers mentioned above.
