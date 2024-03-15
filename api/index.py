from flask import Flask, Response
import requests

app = Flask(__name__)

# URL from which to fetch the JavaScript code
JS_URL = "https://adbpage.com/adblock?v=3&format=js"

@app.route('/')
def fetch_javascript():
    """Fetch and return JavaScript code from a predefined URL."""
    try:
        response = requests.get(JS_URL)
        response.raise_for_status()  # Raises an HTTPError if the response status code is 4xx or 5xx
        return response.text
    except requests.RequestException as e:
        return Response("Error fetching JavaScript: {}".format(e), status=500)

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for development purposes
