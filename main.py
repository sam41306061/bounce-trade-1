# region imports
from AlgorithmImports import *
from indicators.trend_handler import *
from indicators.momentum_handler import *
from custom_sectors.sectors import *
from risk_controls.position_sizing import * 
from risk_controls.stop_loss import *
# endregion


class BullishStrategy(QCAlgorithm):
    def initialize(self):
        self.set_start_date(2012, 1, 1)
        self.set_end_date(2024, 12, 31)
        self.set_cash(10000)

        # Create handlers properly
        self.sector_handler = SectorHandler()
        self.trend_handler = {}
        self.momentum_handler = {}
        self.position_sizing = {}
        self.set_stop_loss = {}
        self.symbols = []

        selected_sectors = ["ConsumerStaples", "Realestate", "Technology", "Industrial", "Financial", "HealthCare"]

        # Now populate symbols (just one sector for example)
        for sectors in selected_sectors:
            for ticker in self.sector_handler.sectors[sectors]:
                symbol = self.add_equity(ticker, Resolution.DAILY).Symbol
                self.symbols.append(symbol)
                self.trend_handler[symbol] = TrendHandler(self, symbol)
                self.momentum_handler[symbol] = MomentumHandler(self, symbol)
                self.position_sizing[symbol] = PositionSizeHandler(self, symbol)
                self.set_stop_loss[symbol] = StopLossHandler(self, symbol)

    def on_data(self, data: Slice):
        for symbol in self.symbols:
            if symbol not in data or not data[symbol]:
                continue
            
            trend_handler = self.trend_handler.get(symbol)
            momentum_handler = self.momentum_handler.get(symbol)
            position_sizing = self.position_sizing.get(symbol)
            set_stop_loss = self.set_stop_loss.get(symbol)

            # no trend or momentum identifed check
            if not trend_handler or not momentum_handler or not position_sizing:
                continue
            
            trend = trend_handler.trend_identifier()
            # handling the actual order
            if trend in ("bullish", "bearish") and momentum_handler.identify_pull_back(trend):
                direction = "long" if trend == "bullish" else "short"
                position_sizing.position_sizing(direction=direction)

            elif set_stop_loss and set_stop_loss.check_stop_loss():
                self.Debug(f"Stop loss was identified and triggered for {symbol}")  