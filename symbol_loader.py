import json

STOCKS_FILE_PATH = "data/Stocks.json"


def load_unique_symbols(file_path: str = STOCKS_FILE_PATH) -> list[str]:
    """Load portfolio holdings and return the deduplicated, sorted list of
    valid ticker symbols (drops placeholder entries like '?')."""
    with open(file_path) as f:
        holdings = json.load(f)

    symbols = {
        holding["Stock"]
        for holding in holdings
        if holding.get("Stock") and holding["Stock"] != "?"
    }
    return sorted(symbols)
