from schwab_auth import get_access_token
from schwab_client import get_all_positions


def main() -> None:
    access_token = get_access_token()
    accounts = get_all_positions(access_token)

    print(f"\nFound {len(accounts)} account(s):\n")
    for entry in accounts:
        account = entry.get("securitiesAccount", entry)
        account_number = account.get("accountNumber", "unknown")
        positions = account.get("positions", [])

        print(f"Account {account_number} — {len(positions)} position(s)")
        for position in positions:
            instrument = position.get("instrument", {})
            symbol = instrument.get("symbol", "?")
            quantity = position.get("longQuantity") or position.get("shortQuantity") or 0
            market_value = position.get("marketValue", 0)
            print(f"  {symbol:<8} qty={quantity:<10} marketValue=${market_value:,.2f}")
        print()


if __name__ == "__main__":
    main()
