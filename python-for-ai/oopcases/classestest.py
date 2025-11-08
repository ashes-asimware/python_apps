# Using code without classes to call OpenAI API
name = "OpenAI"
model = "gpt-4o-mini"
api_key = "your_api_key_here"

def setupapi(api_key):
    # Simulate API setup
    return {"key": api_key, "base_url": "https://api.openai.com/v1"}

def generate_response(api_config, prompt):
    response = f"{api_config['key']} {api_config['base_url']} responding to: {prompt}"
    return response

api = setupapi(api_key)
response = generate_response(api, "Explain the theory of relativity.")

# Using code with classes to call OpenAI API
from client import OpenAIAPIClient

client = OpenAIAPIClient(api_key)
response = client.generate_response("Explain the theory of relativity.")