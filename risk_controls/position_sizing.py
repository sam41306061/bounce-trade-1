# region imports
from AlgorithmImports import *
# endregion

class PositionSizeHandler:

    def __init__(self, algorithm: QCAlgorithm, symbol: Symbol, atr_period: int = 13, risk_per_trade: float = 0.10):

        self.algorithm = algorithm
        self.symbol = symbol
        self.atr = algorithm.atr(symbol, atr_period, MovingAverageType.SIMPLE, Resolution.DAILY)
        self.risk_per_trade = risk_per_trade  # e.g., 0.10 = 10%
        self.entry_price = None
        


    def position_sizing(self, direction: str = "long"):
            portfolio = self.algorithm.portfolio
            symbol = self.symbol

            if not portfolio[symbol].invested:
                if not self.atr.IsReady:
                    return

                price = self.algorithm.securities[symbol].Price
                equity = portfolio.total_portfolio_value
                allocation = equity * self.risk_per_trade
                quantity = int(allocation / price)


                if quantity <= 0:
                    return

                order_direction = OrderDirection.BUY if direction == "long" else OrderDirection.SELL
                order_quantity = quantity if direction == "long" else -quantity

                # Check if you have enough margin to place this order
                buying_power = self.algorithm.portfolio.get_buying_power(symbol,order_direction)
                order_value = abs(price * quantity)

                if order_value <= buying_power:
                    self.algorithm.market_order(symbol, order_quantity)
                    self.entry_price = price
                    self.algorithm.set_stop_loss[symbol].update_entry_price(price)
                    # self.debug(f"Entered{direction} position on {symbol} at {price} with quanity{order_quantity}")
                else:
                     self.algorithm.debug(f"Skipped order for {symbol}, insufficient buying power.")
                
            else:
                # Already invested - check for profit target
                current_price = self.algorithm.securities[symbol].price
                if self.entry_price is None:
                    return

                position = portfolio[symbol]
                quantity = position.Quantity

                # Calculate gain depending on position direction
                if quantity > 0:
                    # Long position
                    gain_pct = (current_price - self.entry_price) / self.entry_price
                else:
                    # Short position
                    gain_pct = (self.entry_price - current_price) / self.entry_price

                if gain_pct >= 0.50:
                    self.algorithm.MarketOrder(symbol, -quantity)
                    self.algorithm.Debug(f"Exited {symbol} at {current_price} with {gain_pct*100:.2f}% gain")
                    self.entry_price = None

            


