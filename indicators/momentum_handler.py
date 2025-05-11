# region imports
from AlgorithmImports import *
# endregion

class MomentumHandler:


    def __init__(self, algorithm:QCAlgorithm, symbols:Symbol,):
        
        self.algorithm = algorithm
        self.symbols = symbols

        self.indicators = {
            "stoch": self.algorithm.sto(symbols, 8,3,3, Resolution.DAILY),
            "rsi": self.algorithm.rsi(symbols, 2, MovingAverageType.SIMPLE, Resolution.DAILY),
            "ema21": self.algorithm.ema(symbols, 21, Resolution.DAILY)
        }

    def identify_pull_back(self, trend: str):
        if not self._indicators_ready():
            return False
        
        i = self.indicators
        #checking if price is near the ema21
        price = self.algorithm.securities[self.symbols].price
        ema21 = i["ema21"].current.value

        # set ema check
        price_near_ema = abs(price - ema21) / price < 0.01

        # check for pull back 
        if trend == "bullish" and price <= ema21 and price_near_ema:
            return True
        elif trend == "bearish" and price >= ema21 and price_near_ema:
            return True
        return False

    
    def _indicators_ready(self):
        return all(ind.IsReady for ind in self.indicators.values())
        
