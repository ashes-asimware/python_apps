class APIConfig:
    def __init__(self, api_key, model="gpt-4o-mini", max_tokens=128, base_url="https://api.openai.com/v1"):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = base_url

dev_config = APIConfig(api_key="sk-dev-key", max_tokens=64)

prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4o", max_tokens=2048) 

print(f"Model(development): {dev_config.model}")  # Output: gpt-4o-mini
print(f"Max. number of tokens(development): {dev_config.max_tokens}")  # Output: 64
print(f"Model(production): {prod_config.model}")  # Output: gpt-4o
print(f"Max. number of tokens(production): {prod_config.max_tokens}")  # Output: 2048


