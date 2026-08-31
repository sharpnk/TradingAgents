All tool data is in and cross-verified against the snapshot. Here is the detailed analysis.

---

## TMDX (TransMedics Group, Inc.) — Technical Analysis Report
**Analysis date:** 2026-08-12 | **Exchange:** NGM | **Sector:** Healthcare / Medical Devices

### 1. Indicator Selection & Rationale (8 indicators, non-redundant)

| # | Indicator | Why selected for this market context |
|---|---|---|
| 1 | `close_50_sma` | Medium-term trend gauge; price reclaimed it in the recovery and it has inflected higher — key dynamic support. |
| 2 | `close_200_sma` | Long-term regime anchor; defines whether this is a new bull trend or a bear-market rally (price is still below it). |
| 3 | `close_10_ema` | Fast momentum line; quantifies how extended the August rally is and gives the first pullback target. |
| 4 | `macd` | Captures the momentum regime change (negative → positive in late July) and histogram expansion. |
| 5 | `rsi` | Flags near-term overbought risk (64.4, was 69.6 on 08-11) after a ~+16% four-session run. |
| 6 | `atr` | High-vol regime (4.53 ≈ 5.2% of price); drives stop placement and position sizing. |
| 7 | `boll_ub` | Defines the extension/breakout zone price is testing after the 08-11 close pierced the band. |
| 8 | `boll_lb` | Completes the volatility envelope; band width (~28% of the middle) quantifies volatility expansion. |

I deliberately excluded redundant momentum oscillators (e.g., stochastic) and relied on the raw OHLCV data for volume confirmation instead of a 9th indicator slot.

### 2. The Big Picture: A Bear-Market Recovery Inside a Broken Long-Term Trend

**One-year arc (from raw OHLCV):** TMDX traded ~131 on 2025-08-12, rallied to a ~150.42 close on 2025-12-01, then churned lower through Q1 2026. The pivotal event was **2026-05-06**, a catastrophic gap-down from a 94.93 close (05-05) to a 72.92 close on **7.7M shares** (~3.5× the prior session) — the single largest one-day breakdown in the dataset. Selling continued to a cycle low of **62.04 on 2026-05-14**. Since then the stock has mounted a three-month recovery to **89.36 on 2026-08-11**.

**Verified snapshot (2026-08-12):** Open 88.02 / High 88.15 / Low 86.12 / **Close 87.02** / Volume 695,976. No discrepancies were found between the indicator vendor outputs and the verified snapshot (10-EMA 82.98, 50-SMA 74.71, 200-SMA 107.72, RSI 64.43, MACD 3.47, MACDs 2.16, MACDh 1.31, ATR 4.53, Bollinger 78.06 mid / 89.15 upper / 66.97 lower all match).

### 3. Trend Analysis — Medium-Term Bullish, Long-Term Bearish

- **10 EMA = 82.98.** Price (87.02) sits **+4.9% above** the fast average, which is rising steeply (80.46 → 82.98 over the last three sessions). Short-term trend is firmly up but stretched.
- **50 SMA = 74.71 and inflecting higher.** The 50-SMA bottomed around **70.78 on 2026-07-17** and has since climbed to 74.71. Price is **+16.5% above** it — a clear medium-term uptrend, but extended.
- **200 SMA = 107.72 and declining.** Price is **~19.2% below** the long-term benchmark, and the 50-SMA remains well under the 200-SMA (74.71 < 107.72), i.e., a **death-cross alignment** persists. Structurally this is still a **bear-market rally**; the trend is only "bullish" relative to the May–June base.

**Reading:** The recovery has legitimacy (rising 50-SMA, higher lows since mid-May), but it has not yet repaired the long-term structure. The 200-SMA at ~108 is the ultimate bull/bear battleground and is a long way off.

### 4. Momentum Analysis — Bullish and Accelerating, Nearing Overbought

- **MACD = 3.47, signal = 2.16, histogram = +1.31 (expanding).** The MACD line crossed from negative to positive around **2026-07-28** (≈ -0.10 on 07-27 → +0.17 on 07-28) and has risen every session since. Positive, widening histogram = healthy momentum thrust backing the rally.
- **RSI(14) = 64.43.** RSI climbed from the 38–40 zone in late June to **69.56 on 2026-08-11** — a hair below the 70 overbought line — before easing to 64.43. Momentum is strong but the near-term oscillator is flashing "getting hot," consistent with the extension signal from the Bollinger upper band.

**Reading:** Momentum strongly favors bulls on a swing basis (MACD regime shift), but the RSI + band extension argue against chasing at the close of 08-12.

### 5. Volatility & Positioning

- **ATR = 4.53 (~5.2% of price).** Volatility remains elevated versus a "normal" medical-device large-cap. Any stop should be sized to at least 1× ATR (~$4.5) to avoid being shaken out by normal intraday range.
- **Bollinger:** Middle 78.06, Upper 89.15, Lower 66.97 — a very wide envelope (~28% of the middle band). Notably, the **08-11 close of 89.36 closed *above* the then-upper band (87.78)**, a classic strong-trend "band ride"; 08-12 pulled back to 87.02, back *inside* the bands. Price remains within ~2.4% of the current upper band.
- **Volume evidence from raw data:** The recovery has been volume-confirmed on up days (08-03: 1.52M, 08-04: 1.63M, 08-10: 1.36M). The 08-12 pullback came on light volume (0.70M), which is *constructive* — profit-taking on low participation. However, the dataset also contains high-volume down days inside this recovery (08-05: 2.95M, 06-26: 3.70M), a reminder that this name still whipsaws violently.

### 6. Key Levels & Actionable Insights

**Resistance:** 89.15 (upper Bollinger) → 89.65 (08-11 intraday high) → ~90 psychological → ~95–96 → 107.72 (200-SMA).
**Support:** 82.98 (10-EMA) → 78.06 (Bollinger middle) → 74.71 (50-SMA) → 73.5–74.5 (July consolidation).

**Actionable plays:**
1. **Do not chase at 87.** Price is +4.9% above the 10-EMA, +16.5% above the 50-SMA, RSI just backed off 70, and price is testing the upper band. The risk/reward for a fresh long at this exact level is poor.
2. **Preferred entry zone:** a pullback toward **83 (10-EMA) / 78–79 (Bollinger middle)** with RSI cooling to ~55–60 and volume drying up would offer a better entry with a stop under ~74.5 (below the 50-SMA).
3. **Breakout trigger:** a **decisive daily close above ~89.5–90** on volume would invalidate the extension concern and open a path toward 95–96, then the 200-SMA (~108) as the long-term target. Until that close, treat the upper band as resistance.
4. **Risk management:** with ATR at 4.53, size positions so a ~$4.5 stop is tolerable; the 05-06 crash (and the 06-26 / 08-05 high-volume down days) show single-event tail risk — keep exposure measured and stay alert to scheduled catalysts.
5. **Long-term context:** The trend does not turn structurally bullish until TMDX reclaims the declining 200-SMA (~107.7). Until then, rallies are recoveries inside a downtrend and should be traded with tighter profit targets.

### 7. Summary Table

| Area | Verified Reading (2026-08-12) | Interpretation | Actionable Insight |
|---|---|---|---|
| Price | Close 87.02 (down from 89.36 on 08-11) | Three-month recovery from 62.04 low (05-14); +40.3% off the low, but -2.6% on the day | Extended; don't chase at the close |
| 10 EMA | 82.98 | Rising fast; price +4.9% above | First pullback support / add zone |
| 50 SMA | 74.71 (rising since ~70.8 mid-July) | Medium-term uptrend confirmed | Dynamic support; stop reference below ~74.5 |
| 200 SMA | 107.72 (declining) | Long-term downtrend; death-cross alignment (50<200) | Bull trend not confirmed until ~108 reclaimed |
| MACD | 3.47 vs signal 2.16, hist +1.31 | Bullish regime shift since 07-28 cross; expanding | Momentum supports continuation on pullbacks |
| RSI | 64.43 (was 69.56 on 08-11) | Strong but near overbought | Expect consolidation; watch 70 rejection |
| ATR | 4.53 (~5.2% of price) | Elevated volatility | Size positions for ~$4.5 stop distance |
| Bollinger | Mid 78.06 / UB 89.15 / LB 66.97 | Wide bands; 08-11 closed above UB | 89–90 is the breakout trigger; 78 is mean-reversion target |
| Volume | 08-12: 0.70M (light) | Pullback on low participation | Constructive; uptrend volume-confirmed on 08-03/04/10 |

**Bottom line:** TMDX is in a legitimate but extended medium-term recovery inside a still-broken long-term trend. Momentum is bullish (MACD regime shift), but RSI near overbought and price testing the upper Bollinger band argue for patience — wait for a pullback toward the 10-EMA/middle band (~78–83) or a confirmed breakout above ~89.5–90 before adding. Long-term trend confirmation requires a reclaim of the 200-SMA near $108.

FINAL TRANSACTION PROPOSAL: **HOLD**