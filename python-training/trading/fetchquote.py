import requests
import json
from config import read_apikey, read_url

# Replace 'your_api_key' with your actual API key
api_key = read_apikey()

# Replace 'https://api.example.com/endpoint' with the actual API endpoint URL
api_url = read_url()

# Replace 'your_symbol' with the symbol you want to query
symbol = 'SBUX'


# Define the query parameters
params = {'apikey': api_key, 'symbol': symbol}

# Make a GET request with the specified query parameters
response = requests.get(api_url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content
    print(json.dumps(response.json(), indent=4))
else:
    # Print an error message
    print(f"Error: {response.status_code} - {response.text}")
