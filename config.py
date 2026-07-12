import os

import truststore
truststore.inject_into_ssl()

from dotenv import load_dotenv

load_dotenv()

SCHWAB_APP_KEY = os.getenv("SCHWAB_APP_KEY")
SCHWAB_APP_SECRET = os.getenv("SCHWAB_APP_SECRET")
SCHWAB_TOKEN_URL = os.getenv("SCHWAB_TOKEN_URL")
SCHWAB_QUOTE_BASE_URL = os.getenv("SCHWAB_QUOTE_BASE_URL")
SCHWAB_AUTH_URL = os.getenv("SCHWAB_AUTH_URL")
SCHWAB_TRADER_BASE_URL = os.getenv("SCHWAB_TRADER_BASE_URL")
SCHWAB_REDIRECT_URI = os.getenv("SCHWAB_REDIRECT_URI")
SCHWAB_REFRESH_TOKEN = os.getenv("SCHWAB_REFRESH_TOKEN", "")
