import base64
import webbrowser
from pathlib import Path
from urllib.parse import urlencode, urlparse, parse_qs

import requests
from dotenv import set_key

import config

_ENV_PATH = str(Path(__file__).resolve().parent / ".env")

_refresh_token = config.SCHWAB_REFRESH_TOKEN


def get_authorization_url() -> str:
    query = urlencode(
        {
            "response_type": "code",
            "client_id": config.SCHWAB_APP_KEY,
            "scope": "readonly",
            "redirect_uri": config.SCHWAB_REDIRECT_URI,
        }
    )
    return f"{config.SCHWAB_AUTH_URL}?{query}"


def _basic_auth_header() -> dict:
    creds = f"{config.SCHWAB_APP_KEY}:{config.SCHWAB_APP_SECRET}"
    encoded = base64.b64encode(creds.encode()).decode()
    return {
        "Authorization": f"Basic {encoded}",
        "Content-Type": "application/x-www-form-urlencoded",
    }


def _store_tokens(tokens: dict) -> None:
    global _refresh_token
    refresh_token = tokens.get("refresh_token")
    if refresh_token:
        _refresh_token = refresh_token
        set_key(_ENV_PATH, "SCHWAB_REFRESH_TOKEN", refresh_token)


def exchange_code_for_tokens(redirect_response_or_code: str) -> str:
    """Exchange an authorization code (or the full redirect URL containing it) for tokens."""
    code = redirect_response_or_code.strip()
    if code.startswith("http"):
        code = parse_qs(urlparse(code).query).get("code", [""])[0]
    if not code:
        raise ValueError("No authorization code found in the provided input.")
    response = requests.post(
        config.SCHWAB_TOKEN_URL,
        headers=_basic_auth_header(),
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": config.SCHWAB_REDIRECT_URI,
        },
    )
    response.raise_for_status()
    tokens = response.json()
    _store_tokens(tokens)
    return tokens["access_token"]


def refresh_access_token() -> str:
    if not _refresh_token:
        raise RuntimeError("No refresh token available; complete authorization first.")

    response = requests.post(
        config.SCHWAB_TOKEN_URL,
        headers=_basic_auth_header(),
        data={
            "grant_type": "refresh_token",
            "refresh_token": _refresh_token,
        },
    )
    response.raise_for_status()
    tokens = response.json()
    _store_tokens(tokens)
    return tokens["access_token"]


def get_market_data_access_token() -> str:
    """Get an app-level token for public market data (quotes) via the
    client_credentials grant. No user login required."""
    response = requests.post(
        config.SCHWAB_TOKEN_URL,
        headers=_basic_auth_header(),
        data={"grant_type": "client_credentials"},
    )
    response.raise_for_status()
    return response.json()["access_token"]


def get_access_token() -> str:
    """Return a usable access token, refreshing the cached refresh token or
    prompting for one-time interactive authorization when needed."""
    if _refresh_token:
        try:
            return refresh_access_token()
        except requests.HTTPError:
            print("Stored refresh token is no longer valid; re-authorization required.")

    auth_url = get_authorization_url()
    print("Open this URL, log in to Schwab, and approve access:")
    print(auth_url)
    webbrowser.open(auth_url)
    redirected = input(
        "After approving, paste the full redirect URL (or just the 'code' value) here: "
    )
    return exchange_code_for_tokens(redirected)
