# region imports
from AlgorithmImports import *
# endregion

class TrendHandler:

    def __init__(self, algorithm: QCAlgorithm, symbol: Symbol):
        self.algorithm = algorithm
        self.symbol = symbol

        self.indicators = {
                "ema8": self.algorithm.ema(symbol, 8, Resolution.DAILY),
                "ema21": self.algorithm.ema(symbol, 21, Resolution.DAILY),
                "ema34": self.algorithm.ema(symbol, 34, Resolution.DAILY),
                "sma50": self.algorithm.sma(symbol, 50, Resolution.DAILY),
                "sma100": self.algorithm.sma(symbol, 100, Resolution.DAILY),
                "sma200": self.algorithm.sma(symbol, 200, Resolution.DAILY),
                "rsi": self.algorithm.rsi(symbol, 2, MovingAverageType.SIMPLE, Resolution.DAILY),
                "stoch": self.algorithm.sto(symbol, 8, 3, 3, Resolution.DAILY),
            }
        self.last_trend = None

    def trend_identifier(self):
    
        # check if indicators are not ready
        if not self._indicators_ready():
            return None
        
        i = self.indicators
        
        bullish_trend = (
                i["ema8"].Current.Value > i["ema21"].Current.Value and
                i["ema21"].Current.Value > i["ema34"].Current.Value and
                i["ema34"].Current.Value > i["sma50"].Current.Value and
                i["sma50"].Current.Value > i["sma100"].Current.Value and
                i["sma100"].Current.Value > i["sma200"].Current.Value
            )
        
        bearish_trend = (
                i["ema8"].Current.Value < i["ema21"].Current.Value and
                i["ema21"].Current.Value < i["ema34"].Current.Value and
                i["ema34"].Current.Value < i["sma50"].Current.Value and
                i["sma50"].Current.Value < i["sma100"].Current.Value and
                i["sma100"].Current.Value < i["sma200"].Current.Value
            )

        if bullish_trend:
            return "bullish"
        elif bearish_trend:
            return "bearish"
        else:
            return None

    def is_retracement_stochs(self):

        i = self.indicators

        if not i["stoch"].IsReady:
                return None

        bullish_trend_stochs = (
            i["stoch"].StochK.Current.Value <= 40 and
            i["stoch"].StochD.Current.Value <= 40
        )

        bearish_trend_stochs = (
            i["stoch"].StochK.Current.Value >= 60 and
            i["stoch"].StochD.Current.Value >= 60
        )

        if bullish_trend_stochs:
            return "bullish"
        elif bearish_trend_stochs:
            return "bearish"
        else:
            return None
       
    
    def is_retracement_rsi(self):
        i = self.indicators
        
        if not i["rsi"].is_ready:
            return False
        
        if i["rsi"].Current.Value <= 10:
            return "bullish"
        elif i["rsi"].Current.Value >= 90:
            return "bearish"
        else:
            return None

    
    def _indicators_ready(self):
        return all(ind.IsReady for ind in self.indicators.values())


