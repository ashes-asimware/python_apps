# Using classes to call OpenAI API
class OpenAIAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openai.com/v1"
    
    def generate_response(self, prompt):
        response = f"{self.api_key} {self.base_url} responding to: {prompt}"
        return response
