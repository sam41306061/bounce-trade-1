### Swing Trading Algorithm – Sector-Rotational Bounce Strategy

Over the past few months, I’ve been building and refining a **systematic swing trading algorithm** designed to identify **optimal bounce trade setups** across multiple equity sectors. The strategy targets **pullback entries in trending stocks**, applying both momentum and trend analysis to time high-probability reversals with risk-managed precision.

#### 🛠️ Tech Stack & Architecture

- **QuantConnect / Lean Engine** (Python-based)
- Custom-built modules for:

  - **Trend detection** (`TrendHandler`)
  - **Momentum confirmation** (`MomentumHandler`)
  - **Dynamic position sizing** (`PositionSizeHandler`)
  - **Sector rotation** via ETF or industry constituents
  - **Risk controls** including stop-loss triggers

#### Strategy Highlights

- **Multi-sector exposure**: Trades are filtered by trend strength across key sectors like Technology, Consumer Staples, Real Estate, Healthcare, Industrials, and Financials.
- **Bounce trade logic**: Waits for a **pullback in a bullish/bearish trend**, then confirms with momentum shifts before entry.
- **Modular risk management**: Position size and stop-loss thresholds are calculated per symbol using custom handlers.

#### 🧪 Backtest Parameters

- **Timeframe**: 2012–2024 (12 years of daily data)
- **Capital**: \$10,000
- **Resolution**: Daily bars

#### 📊 Key Performance Metrics (hypothetical example)

- **Compounded Annualized Return**: 14.897%
- **Max Drawdown**: -27.400%
- **Sharpe Ratio**: .682
- **Win Rate**: 67%
- **PSR**: 16.926%
- **Annual Variance**: .018

#### 💡 Takeaways

This project pushed my understanding of algorithmic trading, risk-adjusted performance, and modular system design. It also reinforced the importance of building **clean, reusable architecture**—each component of the algorithm (trend, momentum, risk) can evolve independently, enhancing testability and robustness.

---

If you're interested in trading automation, factor modeling, or backtesting with Python/QuantConnect, happy to chat or share insights!
