All data retrieved and cross-checked. The indicator API values match the verified snapshot exactly (50 SMA 337.31, 200 SMA 265.55, 10 EMA 325.27, RSI 51.32, MACD 3.79, MACDH 7.18, ATR 34.38) — no discrepancies to flag. Here is the full analysis.

---

# COHR (Coherent Corp.) — Technical Analysis Report
**Analysis date:** 2026-08-16 (latest trading row: 2026-08-14) | **Exchange:** NYQ | **Sector:** Technology / Scientific & Technical Instruments

## 1. Indicator Selection Rationale (8 indicators)

COHR is an exceptionally high-volatility, momentum-driven AI/photonics name that has ranged from ~$90 to ~$427 over the past year. I selected indicators to cover four non-redundant dimensions:

| Dimension | Indicator(s) | Why suitable here |
|---|---|---|
| Trend (3 timeframes) | `close_200_sma`, `close_50_sma`, `close_10_ema` | Price is above the 200 SMA but below the 50 SMA — a classic post-correction tug-of-war. All three are needed to disambiguate long-term uptrend vs. medium-term correction vs. short-term recovery. |
| Momentum | `macd`, `macdh`, `rsi` | MACD line + histogram capture the speed of the violent July→August reversal; RSI flags whether the bounce is exhausted or extended. (Avoided stochrsi/other momentum dups.) |
| Volatility | `atr` | ATR of ~$34 (~10.5% of price) makes position sizing and stop placement the single most important risk variable. |
| Volume confirmation | `vwma` | Confirms whether the recovery is backed by real accumulation or is a low-quality short squeeze. |

I deliberately left out Bollinger bands as a *selected* indicator (ATR covers volatility) but reference the verified snapshot's band values for context.

## 2. Trend Analysis

**Long-term (200 SMA) — bullish but extended:**
- Close $325.83 vs. 200 SMA $265.55 → price sits **~22.7% above** the long-term benchmark.
- The 200 SMA has risen steadily from ~$192.74 (May 18) to $265.55 (Aug 14), confirming a powerful multi-month uptrend that began well below $100 in Aug 2025.
- No death-cross risk; the structural trend is intact.

**Medium-term (50 SMA) — bearish/corrective:**
- Close $325.83 vs. 50 SMA $337.31 → price is **~3.4% below** the 50 SMA.
- The 50 SMA has been *declining* from ~$369.0 (Jul 2) to $337.31 (Aug 14), confirming that the June→July selloff (from $426.89 on 6/2 to $222.05 on 7/29, **–48.0%**) flipped the medium-term structure to downtrend. The stock has not reclaimed this average.

**Short-term (10 EMA) — recovering but stalling:**
- Close $325.83 vs. 10 EMA $325.27 → price is essentially *at* the 10 EMA.
- The 10 EMA bottomed at ~$269.84 (Jul 31) and climbed steeply to $325.27, showing the bounce off the July low. However, the EMA has flattened over the last 3 sessions (324.68 → 325.15 → 325.27), indicating the short-term recovery is losing upward thrust.

## 3. Momentum Analysis

**MACD — bullish crossover, but fading thrust:**
- MACD line: **+3.79** vs. signal: **–3.39** → MACD is above signal; **bullish crossover** occurred around Aug 3–4 after the MACD bottomed at –28.76 (Jul 30).
- Histogram **+7.18** — positive, but down ~46% from its Aug 7 peak of +13.31. Momentum from the bounce is decaying.
- The MACD line itself recovered from –27.76 (Jul 31) to +3.79 (Aug 14) — a huge swing that reflects the violence of the move but also warns that the "easy" momentum leg may be done.

**RSI — neutral, no edge:**
- RSI **51.32** — recovered from oversold (28.3 on Jul 29) back to dead center. No overbought/oversold signal; no divergence visible in the provided window. RSI is currently uninformative for direction, which itself signals indecision.

## 4. Volatility Analysis

- **ATR: $34.38** (~10.5% of the $325.83 close). Daily ranges of $25–$40 are routine; the last five sessions alone show closes of 379.13 → 325.15 → 328.57 → 355.64 → 327.23 → 325.83.
- Verified Bollinger context: middle $303.75, upper $382.99, lower $224.50. Price sits in the upper-middle of an extraordinarily wide band (~$158 band width). The lower band (~$224.50) sits right at the July 29 low ($222.05) — a meaningful structural reference.
- **Implication:** any stop tighter than ~1.5× ATR (~$50) is likely to be whipsawed. Position sizes should be cut relative to a normal-volatility stock.

## 5. Volume Analysis (VWMA + raw volume)

- VWMA: **$316.07** (rising from $273.94 on Jul 31) — close ($325.83) is **above VWMA**, so the bounce has been volume-supported on balance.
- **However, distribution signs are visible at the top of the bounce:**
  - Aug 7 rally to $379.13 on 11.26M shares.
  - Aug 10 –14% plunge to $325.15 on 9.85M.
  - Aug 12 +8.2% pop to $355.64 on 12.45M.
  - Aug 13 **–8.0% drop to $327.23 on 13.07M (highest volume of the period)**.
  - Aug 14 drift to $325.83 on 8.74M.
- The heaviest volume of the recent window landed on a big down day (Aug 13), which is a caution flag against treating the bounce as durable accumulation.

## 6. Key Levels & Scenarios (based on observed data)

| Level | Value | Basis |
|---|---|---|
| Recent bounce high | $379.13 | Aug 7 close (near Bollinger upper $382.99) |
| 50 SMA (immediate resistance) | $337.31 | Declining medium-term average |
| Recent close | $325.83 | Aug 14 |
| VWMA / consolidation floor | ~$315–317 | Aug 10/11 lows & rising VWMA $316.07 |
| Bollinger middle | $303.75 | 20-SMA basis |
| 200 SMA (structural support) | $265.55 | Long-term trend benchmark |
| July capitulation low | $222.05 | Jul 29 close (near Bollinger lower $224.50) |

**Bullish confirmation:** A daily close back above the 50 SMA (~$337) with volume, ideally followed by a retest of $355–380, would re-open the uptrend and target the June highs (~$427).
**Bearish confirmation:** A break below the $315–317 shelf on rising volume would likely test $303 (Bollinger middle), then $265–280 (200 SMA zone), with the July low at $222 as the ultimate reference.

## 7. Risks & Caveats

- **Extreme volatility:** ATR ~10.5% of price; whipsaw risk is severe. Overnight gaps of ±8–14% have occurred repeatedly (Aug 10, Aug 12, Aug 13).
- **Momentum fade:** MACD histogram down ~46% from peak while price is below the falling 50 SMA — classic setup for a failed bounce if buyers don't defend $315.
- **High-volume down days** suggest some participants are distributing into strength.
- **Long-term trend integrity:** As long as price holds above the 200 SMA ($265.55), the structural bull case remains intact; a close below it would be a major regime change given the 22.7% cushion that would be erased.

## 8. Verdict

The evidence paints a picture of a **long-term uptrend undergoing a violent, unresolved correction**: price above the 200 SMA (bullish), below the falling 50 SMA (bearish), short-term recovery stalled at the 10 EMA, MACD positive but fading, RSI neutral, and volatility extreme. This is not a clean buy (no reclaim of the 50 SMA, fading momentum) nor a clean sell (long-term trend intact, price above VWMA and 200 SMA). The highest-probability posture is to **stand aside / hold** and let the $315–337 zone resolve.

---

## Summary Table

| Indicator | Latest Value (2026-08-14) | Signal | Interpretation |
|---|---|---|---|
| Close | $325.83 | — | Below 50 SMA, above 10 EMA, above 200 SMA |
| close_200_sma | $265.55 | 🟢 Bullish | Price ~22.7% above; long-term uptrend intact |
| close_50_sma | $337.31 | 🔴 Bearish | Price ~3.4% below; medium-term correction active |
| close_10_ema | $325.27 | 🟡 Neutral | Price at the EMA; short-term recovery flattening |
| MACD / Signal | +3.79 / –3.39 | 🟢 Bullish (fading) | Bullish crossover intact but thrust decaying |
| MACD Histogram | +7.18 | 🟡 Cooling | Down ~46% from Aug 7 peak of +13.31 |
| RSI (14) | 51.32 | 🟡 Neutral | Neither overbought nor oversold; no divergence |
| ATR (14) | $34.38 | ⚠️ High risk | ~10.5% of price; use wide stops / small size |
| VWMA | $316.07 | 🟢 Mildly bullish | Close above volume-weighted average; supports bounce |
| Bollinger mid/up/low | $303.75 / $382.99 / $224.50 | 🟡 Wide range | Extreme band width; lower band near July low |
| Volume pattern | 13.07M on Aug 13 down day | 🔴 Caution | Distribution risk near bounce top |
| **Composite** | — | **HOLD** | Wait for $337 reclaim (bull) or $315 break (bear) |

**Actionable guidance:** Do not initiate new longs until a daily close above ~$337 (50 SMA) on above-average volume. Do not short until a confirmed break below ~$315. If already long, trail stops under the $303.75 Bollinger middle / ~$300 round level; if already short, cover above $355. Given ATR of ~$34, size positions at roughly one-third of normal and expect ±10% daily swings.

FINAL TRANSACTION PROPOSAL: **HOLD**