
# region imports
from AlgorithmImports import *
# endregion

class StopLossHandler:
    def __init__(self, algorithm: QCAlgorithm, symbol: Symbol):
        self.algorithm = algorithm
        self.symbol = symbol
        self.entry_price = None
        self.stop_distance = 0.20  # 20% stop loss

    def update_entry_price(self, price: float):
        self.entry_price = price

    def check_stop_loss(self):
        # check if there is an entry price
        if self.entry_price is None:
            return False

        current_price = self.algorithm.securities[self.symbol].Price
        stop_price = self.entry_price * (1 - self.stop_distance)

        if current_price <= stop_price:
            quantity = self.algorithm.Portfolio[self.symbol].Quantity
            if quantity > 0:
                self.algorithm.MarketOrder(self.symbol, -quantity)
                self.algorithm.Debug(f"Stop loss hit for {self.symbol} at {current_price}")
                self.entry_price = None  # reset
            return True
        return False
