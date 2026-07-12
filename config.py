import os

import truststore
from dotenv import load_dotenv

truststore.inject_into_ssl()
load_dotenv()


def _require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


SCHWAB_APP_KEY = _require_env("SCHWAB_APP_KEY")
SCHWAB_APP_SECRET = _require_env("SCHWAB_APP_SECRET")
SCHWAB_TOKEN_URL = _require_env("SCHWAB_TOKEN_URL")
SCHWAB_QUOTE_BASE_URL = _require_env("SCHWAB_QUOTE_BASE_URL").rstrip("/") + "/"
SCHWAB_AUTH_URL = _require_env("SCHWAB_AUTH_URL")
SCHWAB_TRADER_BASE_URL = _require_env("SCHWAB_TRADER_BASE_URL").rstrip("/") + "/"
SCHWAB_REDIRECT_URI = _require_env("SCHWAB_REDIRECT_URI")
SCHWAB_REFRESH_TOKEN = os.getenv("SCHWAB_REFRESH_TOKEN", "")
