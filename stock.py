import logging
from datetime import datetime, timedelta
import threading
from exceptions import InvalidPriceError, InvalidStockSymbolError

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

STOCK_DATA = {
    "TEA": {"symbol": "TEA", "type": "Common", "last_dividend": 0, "fixed_dividend": 0, "par_value": 100},
    "POP": {"symbol": "POP", "type": "Common", "last_dividend": 8, "fixed_dividend": 0, "par_value": 100},
    "ALE": {"symbol": "ALE", "type": "Common", "last_dividend": 23, "fixed_dividend": 0, "par_value": 60},
    "GIN": {"symbol": "GIN", "type": "Preferred", "last_dividend": 8, "fixed_dividend": 0.02, "par_value": 100},
    "JOE": {"symbol": "JOE", "type": "Common", "last_dividend": 13, "fixed_dividend": 0, "par_value": 250}
}

class Stock:
    def __init__(self, symbol):
        if symbol not in STOCK_DATA:
            raise InvalidStockSymbolError(f"Invalid stock symbol: {symbol}")
        self.data = STOCK_DATA[symbol]
        self.trades = []
        self.lock = threading.Lock()

    def calculate_dividend_yield(self, price):
        if price <= 0:
            logging.error("Invalid price entered")
            raise InvalidPriceError("Price must be greater than 0")

        if self.data["type"] == "Common":
            result = self.data["last_dividend"] / price
            logging.info(f"Calculated Dividend Yield for {self.data['symbol']}: {result}")
            return result
        elif self.data["type"] == "Preferred":
            result = (self.data["fixed_dividend"] * self.data["par_value"]) / price
            logging.info(f"Calculated Dividend Yield for {self.data['symbol']}: {result}")
            return result
        else:
            logging.error("Unknown stock type")
            raise ValueError("Unknown stock type")

    def calculate_pe_ratio(self, price):
        dividend_yield = self.calculate_dividend_yield(price)
        if dividend_yield == 0:
            return float('inf')
        return price / self.data["last_dividend"]

    def record_trade(self, quantity, indicator, price):
        if quantity <= 0 or price <= 0:
            raise ValueError("Quantity and price must be greater than 0")

        with self.lock:
            logging.info(f"Recording trade for {self.data['symbol']}")
            self.trades.append({
                "timestamp": datetime.now(),
                "quantity": quantity,
                "indicator": indicator,
                "price": price
            })
            logging.info(f"Trade recorded successfully for {self.data['symbol']}")

    def calculate_volume_weighted_stock_price(self):
        trade_time_cutoff = datetime.now() - timedelta(minutes=5)
        recent_trades = [trade for trade in self.trades if trade["timestamp"] >= trade_time_cutoff]

        if not recent_trades:
            return 0

        total_quantity = sum(trade["quantity"] for trade in recent_trades)
        total_trade_value = sum(trade["price"] * trade["quantity"] for trade in recent_trades)

        if total_quantity == 0:
            return 0

        return total_trade_value / total_quantity


class StockMarket:
    def __init__(self, stocks):
        self.stocks = stocks

    def calculate_gbce_all_share_index(self):
        vwsp_list = [stock.calculate_volume_weighted_stock_price() for stock in self.stocks]
        vwsp_list = [price for price in vwsp_list if price > 0]

        if not vwsp_list:
            return 0

        product = 1
        for price in vwsp_list:
            product *= price
        return product ** (1 / len(vwsp_list))
