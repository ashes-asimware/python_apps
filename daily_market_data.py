import json
from datetime import date
from dataclasses import dataclass, asdict

from schwab_auth import get_market_data_access_token
from schwab_client import get_quotes
from symbol_loader import STOCKS_FILE_PATH, load_unique_symbols

CHUNK_SIZE = 100


@dataclass
class MarketDataQuote:
    symbol: str
    market_date: str
    price: float
    open_price: float
    close_price: float
    high_price: float
    low_price: float
    volume: int
    average_volume: int
    high_volume: int
    low_volume: int


def _chunk(items: list[str], size: int) -> list[list[str]]:
    return [items[i : i + size] for i in range(0, len(items), size)]


def _to_quote(symbol: str, raw: dict) -> MarketDataQuote:
    quote = raw["quote"]
    # Schwab's quote payload only carries totalVolume, not separate high/low/average
    # volume figures, so all four volume fields share that one value (same
    # simplification the original C# SchwabQuote used).
    total_volume = quote["totalVolume"]
    return MarketDataQuote(
        symbol=symbol,
        market_date=date.today().isoformat(),
        price=quote["lastPrice"],
        open_price=quote["openPrice"],
        close_price=quote["closePrice"],
        high_price=quote["highPrice"],
        low_price=quote["lowPrice"],
        volume=total_volume,
        average_volume=total_volume,
        high_volume=total_volume,
        low_volume=total_volume,
    )


def fetch_daily_quotes(symbols: list[str]) -> tuple[list[MarketDataQuote], list[str]]:
    quotes: list[MarketDataQuote] = []
    failed_symbols: list[str] = []
    access_token = get_market_data_access_token()

    for chunk in _chunk(symbols, CHUNK_SIZE):
        raw_quotes = get_quotes(access_token, chunk)
        for symbol in chunk:
            if symbol in raw_quotes:
                quotes.append(_to_quote(symbol, raw_quotes[symbol]))
            else:
                failed_symbols.append(symbol)

    return quotes, failed_symbols


def update_stocks_file(quotes: list[MarketDataQuote], file_path: str = STOCKS_FILE_PATH) -> None:
    """Write the latest price/open/close/high/low/volume onto every holding
    in Stocks.json whose symbol matches a fetched quote."""
    with open(file_path) as f:
        holdings = json.load(f)

    quotes_by_symbol = {quote.symbol: quote for quote in quotes}
    updated_count = 0
    for holding in holdings:
        quote = quotes_by_symbol.get(holding.get("Stock"))
        if quote is None:
            continue
        holding["Price"] = quote.price
        holding["Open_Price"] = quote.open_price
        holding["Close_Price"] = quote.close_price
        holding["High_Price"] = quote.high_price
        holding["Low_Price"] = quote.low_price
        holding["Volume"] = quote.volume
        updated_count += 1

    with open(file_path, "w") as f:
        json.dump(holdings, f, indent=2)
    print(f"\nUpdated {updated_count} holding(s) in {file_path}")


def main() -> None:
    symbols = load_unique_symbols()
    print(f"Loaded {len(symbols)} unique symbols from Stocks.json")

    quotes, failed_symbols = fetch_daily_quotes(symbols)

    print(f"\nFetched {len(quotes)} quote(s):")
    for quote in quotes:
        print(
            f"  {quote.symbol:<8} price={quote.price:<10} "
            f"open={quote.open_price:<10} close={quote.close_price:<10} "
            f"high={quote.high_price:<10} low={quote.low_price:<10} volume={quote.volume}"
        )

    if failed_symbols:
        print(f"\nNo quote returned for {len(failed_symbols)} symbol(s): {failed_symbols}")

    output_path = f"data/daily_quotes_{date.today().isoformat()}.json"
    with open(output_path, "w") as f:
        json.dump([asdict(q) for q in quotes], f, indent=2)
    print(f"\nSaved quotes to {output_path}")

    update_stocks_file(quotes)


if __name__ == "__main__":
    main()
