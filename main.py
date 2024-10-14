from stock import Stock, StockMarket

# Initialize stock instances
stocks = {
    "TEA": Stock("TEA"),
    "POP": Stock("POP"),
    "ALE": Stock("ALE"),
    "GIN": Stock("GIN"),
    "JOE": Stock("JOE")
}

# Initialize the stock market
market = StockMarket(stocks.values())

def menu():
    while True:
        print("\n--- Stock Market Menu ---")
        print("1. Calculate Dividend Yield")
        print("2. Calculate P/E Ratio")
        print("3. Record a Trade")
        print("4. Calculate Volume Weighted Stock Price")
        print("5. Calculate GBCE All Share Index")
        print("6. Quit")

        choice = input("Select an option (1-6): ")

        if choice == '6':
            print("Exiting program.")
            break

        elif choice == '1':
            symbol = input("Enter stock symbol (TEA, POP, ALE, GIN, JOE): ").upper()
            if symbol not in stocks:
                print("Invalid stock symbol. Please enter a valid symbol.")
                continue

            try:
                price = float(input("Enter stock price: "))
                if price <= 0:
                    print("Invalid price. Price must be greater than 0.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number for price.")
                continue

            print(f"Dividend Yield: {stocks[symbol].calculate_dividend_yield(price):.2f}")

        elif choice == '2':
            symbol = input("Enter stock symbol (TEA, POP, ALE, GIN, JOE): ").upper()
            if symbol not in stocks:
                print("Invalid stock symbol. Please enter a valid symbol.")
                continue

            try:
                price = float(input("Enter stock price: "))
                if price <= 0:
                    print("Invalid price. Price must be greater than 0.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number for price.")
                continue

            print(f"P/E Ratio: {stocks[symbol].calculate_pe_ratio(price):.2f}")

        elif choice == '3':
            symbol = input("Enter stock symbol (TEA, POP, ALE, GIN, JOE): ").upper()
            if symbol not in stocks:
                print("Invalid stock symbol. Please enter a valid symbol.")
                continue

            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Invalid quantity. Must be greater than 0.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number for quantity.")
                continue

            indicator = input("Enter indicator (BUY/SELL): ").upper()
            if indicator not in ['BUY', 'SELL']:
                print("Invalid indicator. Please enter BUY or SELL.")
                continue

            try:
                trade_price = float(input("Enter trade price: "))
                if trade_price <= 0:
                    print("Invalid trade price. Must be greater than 0.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number for trade price.")
                continue

            stocks[symbol].record_trade(quantity, indicator, trade_price)
            print(f"Trade recorded for {symbol}")

        elif choice == '4':
            symbol = input("Enter stock symbol (TEA, POP, ALE, GIN, JOE): ").upper()
            if symbol not in stocks:
                print("Invalid stock symbol. Please enter a valid symbol.")
                continue

            vwsp = stocks[symbol].calculate_volume_weighted_stock_price()
            print(f"Volume Weighted Stock Price for {symbol}: {vwsp:.2f}")

        elif choice == '5':
            gbce_index = market.calculate_gbce_all_share_index()
            print(f"GBCE All Share Index: {gbce_index:.2f}")

        else:
            print("Invalid option. Please select a number between 1 and 6.")

if __name__ == "__main__":
    menu()
