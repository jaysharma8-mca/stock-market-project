import unittest
from stock import Stock, StockMarket

class TestStockMarket(unittest.TestCase):
    
    def setUp(self):
        # Setup some stock data for testing
        self.tea = Stock("TEA")
        self.pop = Stock("POP")
        self.ale = Stock("ALE")
        self.gin = Stock("GIN")
        self.joe = Stock("JOE")
        
        self.market = StockMarket([self.tea, self.pop, self.ale, self.gin, self.joe])
    
    def test_dividend_yield_common(self):
        # Test dividend yield for common stocks
        self.pop.data["last_dividend"] = 8
        self.assertEqual(self.pop.calculate_dividend_yield(100), 0.08)
    
    def test_dividend_yield_preferred(self):
        # Test dividend yield for preferred stocks
        self.gin.data["fixed_dividend"] = 0.02
        self.gin.data["par_value"] = 100
        self.assertEqual(self.gin.calculate_dividend_yield(100), 0.02)

    def test_pe_ratio(self):
        # Test P/E ratio calculation
        self.ale.data["last_dividend"] = 23
        self.assertAlmostEqual(self.ale.calculate_pe_ratio(100), 4.35, places=2)

    def test_vwsp(self):
        # Test Volume Weighted Stock Price calculation
        self.ale.record_trade(100, "BUY", 120)
        self.ale.record_trade(150, "BUY", 110)
        self.assertAlmostEqual(self.ale.calculate_volume_weighted_stock_price(), 114.00)

    def test_gbce_index(self):
        # Test GBCE All Share Index calculation
        self.tea.record_trade(100, "BUY", 120)
        self.pop.record_trade(150, "BUY", 130)
        self.ale.record_trade(200, "BUY", 140)
        self.assertAlmostEqual(self.market.calculate_gbce_all_share_index(), 129.74, places=2)

if __name__ == '__main__':
    unittest.main()
