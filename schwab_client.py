import requests

import config


def _headers(access_token: str) -> dict:
    return {"Authorization": f"Bearer {access_token}"}


def get_account_numbers(access_token: str) -> list[dict]:
    response = requests.get(
        f"{config.SCHWAB_TRADER_BASE_URL}accounts/accountNumbers",
        headers=_headers(access_token),
    )
    response.raise_for_status()
    return response.json()


def get_quotes(access_token: str, symbols: list[str]) -> dict:
    """Fetch quotes for up to ~100 symbols in a single call. Returns a dict
    keyed by symbol, matching the raw Schwab response shape."""
    response = requests.get(
        f"{config.SCHWAB_QUOTE_BASE_URL}quotes",
        headers=_headers(access_token),
        params={"symbols": ",".join(symbols), "fields": "quote", "indicative": "false"},
    )
    response.raise_for_status()
    body = response.json()
    body.pop("errors", None)
    return body


def get_all_positions(access_token: str) -> list[dict]:
    """Fetch every account for the authorized client, each including its positions."""
    response = requests.get(
        f"{config.SCHWAB_TRADER_BASE_URL}accounts",
        headers=_headers(access_token),
        params={"fields": "positions"},
    )
    response.raise_for_status()
    return response.json()
