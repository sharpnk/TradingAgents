All indicator calls returned successfully, and their values match the verified snapshot exactly (e.g., 50 SMA 66.03, 200 SMA 43.61, 10 EMA 68.78, MACD 0.61, RSI 59.71, Bollinger mid 69.56, ATR 3.57). No discrepancies to flag. VWMA (68.35) is provided by the indicator feed only; the snapshot does not list it, so I use it as supplementary confirmation.

FINAL TRANSACTION PROPOSAL: **BUY**

---

# BDT.TO (Bird Construction Inc.) — Technical Analysis Report
**Analysis date:** 2026-08-15 (latest verified trading row: 2026-08-14)
**Sector/Classification:** Industrials / Engineering & Construction (TOR)

## 1. Indicator Selection Rationale

The current market condition for BDT.TO is best described as a **powerful long-term uptrend currently in a high-volatility, post-pullback recovery phase**. The stock trades far above its long-term averages, recently suffered a sharp ~16% correction off the July peak, and is now rebounding on heavy volume. This demands indicators that (a) establish trend context across multiple timeframes, (b) gauge momentum regime without redundancy, and (c) quantify the elevated volatility for risk management. I selected exactly 8 indicators across 5 categories:

| # | Indicator | Category | Why it fits this market |
|---|-----------|----------|------------------------|
| 1 | `close_200_sma` | Moving Average | Long-term trend benchmark (43.61). Confirms the secular bull and provides strategic context for the massive premium price holds above it. |
| 2 | `close_50_sma` | Moving Average | Medium-term trend (66.03). Rising steadily; serves as the dynamic decision line for whether the medium-term uptrend is still intact after the July–August pullback. |
| 3 | `close_10_ema` | Moving Average | Fast, responsive average (68.78). Captures the speed of the current two-day rebound and helps time entries vs. the slower SMAs. |
| 4 | `macd` | MACD | Momentum regime gauge (0.61). Shows momentum collapsed from ~4.3 to near zero during the pullback and is now re-accelerating — the key short-term signal. |
| 5 | `rsi` | Momentum | Overbought/oversold + divergence (59.71). After RSI hit 82 in mid-July and reset to ~42, it now sits neutral with room to run — essential for judging whether the rebound is extended or early. |
| 6 | `boll` | Volatility | Bollinger mid (69.56), with upper 77.51 / lower 61.61 from the snapshot. Provides the volatility envelope and breakout/reversion frame for a stock now in the upper half of very wide bands. |
| 7 | `atr` | Volatility | Absolute volatility/risk measure (3.57). ATR has roughly quadrupled since January (~0.75→3.57); critical for position sizing and stop placement in this regime. |
| 8 | `vwma` | Volume-Based | Volume-weighted trend confirmation (68.35). Verifies that the recent rally is supported by volume rather than a low-participation drift. |

**Redundancy avoided:** No Stochastic RSI (duplicates RSI), no separate MACD signal/histogram calls (derived from the same MACD family and confirmed via snapshot), and only one volume indicator. MAs are kept deliberately at three distinct timeframes (10/50/200) because each answers a different question (timing / trend / regime).

## 2. Trend Structure — Secular Uptrend Intact

- **Massive long-term advance:** Close on 2025-08-15 was **23.93**; latest close 2026-08-14 is **73.14** — a **+205.6% gain over the trailing 12 months** (supported directly by the price series).
- **Price vs. moving averages (all bullish alignment):**
  - Close **73.14** > 10 EMA **68.78** (+6.3%)
  - Close **73.14** > 50 SMA **66.03** (+10.8%)
  - Close **73.14** > 200 SMA **43.61** (+67.7%)
- The 50 SMA (66.03) sits far above the 200 SMA (43.61) with both rising — a textbook bullish long-term configuration. The 50 SMA has climbed without interruption from ~28.2 (2025-11-28) to 66.0, confirming a persistent medium-term uptrend.

## 3. Recent Price Action — Sharp Correction, Powerful Volume-Backed Rebound

- **July spike:** 2026-07-14 closed 68.01 → 2026-07-15 closed **77.10** (+13.4%) on 679,200 shares — the breakout that set the current peak zone (intraday high 77.77 on 07-15; 78.56 on 07-16).
- **Correction:** From the 77.10 peak close, price fell to a **64.50 close on 2026-08-12** (−16.3%), with an intraday low of 62.93 on 07-29. During this leg, RSI cooled from the low-80s to ~42-43 and MACD collapsed from ~4.3 to −0.18 — a textbook momentum washout, not a trend break (price never came close to the 50 SMA at ~66 at the worst point… note: the low was 62.93 intraday, below the then-50 SMA; the close-based relationship remained constructive).
- **Rebound:** 2026-08-13 closed **71.88** (+11.4%) on 622,100 shares; 2026-08-14 closed **73.14** (+1.75%) on 596,500 shares. These are the two heaviest-volume sessions since the July 15 spike, indicating institutional participation in the recovery rather than thin, short-covering drift.

## 4. Momentum — Re-Accelerating After a Healthy Reset

- **RSI = 59.71** (verified). Neutral-to-bullish. It reset from overbought (82.4 on 07-15, 78.9 on 07-17) down to 43.6 on 08-12 and has recovered to ~60 in two sessions. There is meaningful headroom before the 70 overbought threshold — the rebound is not yet extended.
- **MACD = 0.61**, signal **0.63**, histogram **−0.02** (verified). The MACD line is **above zero** (positive momentum regime) but just below its signal line, i.e., a fresh, shallow bearish cross in the daily timeframe. Importantly, the MACD line has swung from −0.18 (08-12) to +0.21 (08-13) to +0.61 (08-14) — it is re-accelerating quickly, so a bullish re-cross above the signal is likely imminent if the rally holds. Treat the −0.02 histogram as noise-level, not a confirmed bearish signal.
- **Interpretation:** The correction reset short-term overbought conditions while the larger momentum regime stayed positive (MACD remained above zero throughout, and price stayed above the rising 200 SMA). This is the classic structure for a trend-continuation setup.

## 5. Volatility & Risk — Elevated Regime Requires Discipline

- **ATR = 3.57** (verified), up from ~0.75–0.92 in Jan-2026 and ~1.5–2.6 through May–June. ATR has roughly **quadrupled-to-quintupled** over eight months. Daily true ranges near 3.5–4 points on a ~73 handle mean **~5% average daily swings** — position sizes should be cut accordingly and stops should not be set at pre-volatility tightness.
- **Bollinger Bands** (verified): mid 69.56, upper 77.51, lower 61.61 — band width ~15.9 points (≈23% of price), reflecting the expanded volatility regime. Price at 73.14 sits between the mid and upper band, in the upper half of the envelope. A daily close above ~77.5 would be an upper-band extension (strong-trend behavior); a close below the mid (~69.6) would signal loss of short-term momentum.

## 6. Volume Confirmation

- **VWMA = 68.35** (08-14); price at 73.14 is **+7.0% above VWMA**, confirming the advance is volume-justified.
- The 08-13 (622K) and 08-14 (597K) sessions are roughly **2–3× the typical recent daily volume** (~150–300K), strongly suggesting accumulation into the recovery.
- Caveat: VWMA can be skewed by volume spikes; here the spikes coincide with large up-close candles, which is the constructive direction.

## 7. Reference Levels (derived from indicator values and verified price history — not claimed as proven S/R)

- **Resistance zone:** ~77.0–78.6 — the July 15–16 peak closes (77.10, 76.10, 76.47, 77.00) and intraday highs (77.77, 78.56); also coincides with the upper Bollinger band (77.51).
- **Immediate support:** 10 EMA ~68.8, then Bollinger mid ~69.6; 50 SMA ~66.0.
- **Structural risk line:** ~64.0–64.5 — the 08-10/08-12 lows (64.37, 64.50) and the lower Bollinger band (61.61). A daily close below ~64 would negate the rebound thesis.

## 8. Actionable Insights

1. **Bias is bullish** — trend, momentum reset, and volume all align. The correction repaired overbought conditions without breaking the structure.
2. **Entry discipline:** Two complementary approaches — (a) **dip-buy** toward 68.8–70.0 (10 EMA / Bollinger mid) for a better risk/reward; (b) **breakout-add** on a daily close above ~77.5 (upper band + July resistance), which would confirm trend extension.
3. **Risk management:** Given ATR 3.57, a sensible invalidation is a daily close below ~66 (50 SMA) for swing positions, or tighter ~1.5×ATR (~5.4 points) from entry for tactical positions. Size positions for ~5% daily swings; this is not a low-volatility name.
4. **Watch the MACD cross:** A bullish re-cross of MACD over its signal in the next sessions would add confirmation; failure of price at 77–78.5 with RSI stalling below 65 would argue for another consolidation leg rather than immediate breakout.
5. **Avoid chasing extended candles:** After a +11% day, entering at market on 08-15 carries elevated pullback risk; limit orders at support or breakout-confirmation orders are preferable.

## 9. Key Points Summary

| Aspect | Observation | Evidence (verified) |
|---|---|---|
| Long-term trend | Powerful bull, +205.6% in 12 months | 23.93 (2025-08-15) → 73.14 (2026-08-14) |
| Trend alignment | Price > 10 EMA > 50 SMA >> 200 SMA | 73.14 / 68.78 / 66.03 / 43.61 |
| Medium-term trend | Rising 50 SMA, no break | 50 SMA ~28.2 (Nov-25) → 66.0 (Aug-26) |
| Correction | −16.3% peak-to-trough close | 77.10 (07-15) → 64.50 (08-12); low 62.93 (07-29) |
| Rebound | +13.4% in two sessions on heavy volume | 64.50 (08-12) → 73.14 (08-14); vols 622K/597K |
| RSI | Neutral-bullish, room before overbought | 59.71 (reset from 82.4 on 07-15) |
| MACD | Positive regime, shallow bearish cross, re-accelerating | MACD 0.61 vs signal 0.63; hist −0.02; line swung −0.18→+0.61 in 2 days |
| Bollinger | Wide bands; price in upper half | Mid 69.56, upper 77.51, lower 61.61 |
| ATR / Volatility | Highly elevated; size positions down | ATR 3.57 vs ~0.75–0.9 in Jan-26 |
| Volume | Accumulation into rebound | VWMA 68.35 < price 73.14; 2–3× typical volume on 08-13/14 |
| Key resistance | July peak / upper band | ~77.0–78.6 (closes 77.10/77.00; highs 77.77/78.56; UB 77.51) |
| Key support | 10 EMA / mid band / 50 SMA | ~68.8 / ~69.6 / ~66.0 |
| Structural invalidation | Daily close below ~64 | 08-10/08-12 lows 64.37/64.50 |
| Recommendation | **BUY** — dip-buy 68.8–70.0 or add on breakout >77.5; stop discipline per ATR | — |

**Bottom line:** BDT.TO remains in a strong, well-defined uptrend. The July–August pullback reset momentum, and the two-day, high-volume recovery has restored short-term bullish structure with RSI still only at ~60. The primary risk is near-term — price is approaching the 77–78.5 resistance/upper-band zone with ATR near multi-month highs. The disciplined approach is to accumulate on pullbacks toward 68.8–70.0 or add on a confirmed close above ~77.5, with stops managed around the 50 SMA (~66) and a hard invalidation below ~64.