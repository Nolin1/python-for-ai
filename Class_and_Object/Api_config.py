class APIConfig:
    def __init__(self, api_key, model = "gpt-3.5-turbo",max_tokens = 100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"

dev_config = APIConfig(api_key= "sk-dev-key", max_tokens=50)

prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)

print(dev_config.model)
print(prod_config.model)
print(prod_config.max_tokens) 