All data has been retrieved and cross-checked. The `get_indicators` outputs match the `get_verified_market_snapshot` exactly (10 EMA 23.96, 50 SMA 22.34, 200 SMA 17.73, RSI 54.06, MACD 0.38, MACD-Hist −0.05, ATR 1.20; OHLC 23.48/24.32/23.30/24.23 on 3,245,805 volume), so there are no discrepancies to flag.

---

# RELY (Remitly Global, Inc.) — Technical Analysis Report
**Analysis date:** 2026-08-12 | **Exchange:** NMS | **Sector:** Technology / Software – Infrastructure

## 1. Indicator Selection Rationale (8 complementary indicators)

| Indicator | Why selected | Role in this context |
|---|---|---|
| `close_200_sma` | Long-term regime filter | Confirms structural uptrend (price far above a rising 200 SMA); strategic context only |
| `close_50_sma` | Medium-term trend + dynamic support | Defines the "higher-low" uptrend channel and the first key support zone |
| `close_10_ema` | Short-term timing | Captures the immediate post-pullback recovery (price just reclaimed it) |
| `macd` | Trend momentum quality | Tracks whether momentum is expanding or fading within the uptrend |
| `macdh` | Early momentum-shift visibility | Flags the current small negative histogram (consolidation, not reversal) |
| `rsi` | Overbought/oversold + divergence watch | Neutral 54 → no exhaustion, room to move; avoids redundancy with stochastic |
| `atr` | Volatility regime / risk sizing | Elevated 1.20 (~5% of price) → wider stops and smaller size warranted |
| `vwma` | Volume-weighted price confirmation | Price vs. volume-weighted average validates whether buying is genuine |

*Deliberately excluded:* Bollinger bands (auto-provided in the verified snapshot), stochastic momentum (redundant with RSI), and additional SMAs (redundant with the 10/50/200 structure).

## 2. Trend Analysis — Bullish Structure Across All Timeframes

**Long-term (200 SMA = 17.73, rising):** RELY trades at **24.23, ~36.7% above** the 200-day average. The 200 SMA has climbed steadily from ~16.50 (mid-June) to 17.73 — a textbook long-term uptrend. The stock's journey is dramatic: after a November 2025 earnings-driven crash (2025-11-06: close 12.31 on 23.4M shares, down from ~16.40 the prior day), it bottomed in the low-$12s, broke out post-earnings on 2026-02-19 (close 17.14 on 22.9M volume), and has more than recovered. From the 2025-11-06 close (12.31) to today (24.23) the stock is up **~96.8%**; vs. the start of the dataset (2025-01-02 close 22.40) it is up ~8.2%, having round-tripped a deep drawdown.

**Medium-term (50 SMA = 22.34, rising):** Price is **~8.5% above** the 50 SMA, which has risen from ~20.50 (mid-June) to 22.34. The 50 SMA is well above the 200 SMA, and both are rising — a healthy, aligned bullish structure (10 EMA 23.96 > 50 SMA 22.34 > 200 SMA 17.73).

**Short-term (10 EMA = 23.96):** After the August 6 spike to an intraday high of **27.15** (close 25.93 on 8.4M shares), price pulled back to 23.14 (08-10) and 23.61 (08-11), then closed 08-12 at **24.23 — back above the 10 EMA** (+1.1%). The 10 EMA flattened (24.14 → 23.96) and is now being retested from above; the immediate question is whether this reclaim holds.

## 3. Momentum — Fading But Stabilizing, Not Reversing

- **MACD (0.38) is positive but below its signal line (0.43); MACD histogram = −0.05.** The MACD line peaked at ~1.04 (07-16) and has cooled during the consolidation, but it remains firmly in positive territory — momentum is constructive at the macro level and merely consolidating at the micro level.
- **Histogram trajectory:** Negative through late July (−0.28 on 07-27), briefly positive on 08-06/07 (+0.11/+0.08) during the spike, then negative again 08-10 → 08-12, but improving from −0.066 (08-11) to −0.052 (08-12). This is a flattening, not a fresh leg down.
- **RSI (54.06) is neutral** — down from an overbought 71.6 (07-06) and 66.3 (08-06) but never reaching oversold. There is no momentum-exhaustion signal; both bulls and bears have room, with the balance of evidence tilted bullish given the trend alignment.

## 4. Volatility — Elevated; Risk Management Is Critical

- **ATR = 1.20 (~4.9% of price)**, up from ~0.85 in late June. The August 6 spike (range 24.11–27.15) and subsequent 3-day pullback expanded realized volatility. Expect single-session moves of ~$1.20 as "normal."
- **Bollinger Bands:** middle 23.75, upper **25.49**, lower **22.01** (band width ~14.7% of the middle band). Price sits in the upper half, near the middle band — not stretched. The wide bands reflect the high-volatility regime.
- **Practical implication:** Stop-losses should be sized at ~1.5–2× ATR (≈$1.80–$2.40) to avoid being shaken out, and position sizes should be trimmed relative to lower-volatility periods.

## 5. Volume — Mildly Constructive

- **VWMA = 24.08;** the close (24.23) sits just **above** it (+0.6%), indicating recent up-moves are, on balance, volume-supported.
- The August 6 breakout printed **8.4M shares** (vs. ~2–3M typical), showing real participation. The pullback days (08-10: 4.3M, 08-11: 3.0M, 08-12: 3.2M) were progressively lighter — the selloff is not showing panic distribution.
- Prior conviction-volume events: 2025-11-06 crash (23.4M), 2026-02-19 earnings gap (22.9M), 2026-05-13 (31.1M) — the stock's trend has been defined by high-volume inflection points.

## 6. Key Levels (derived from verified data)

**Resistance:**
- **~25.5** — Bollinger upper band (25.49) and the 25.2–25.9 zone (07-16 close 25.23; 08-06 close 25.93).
- **27.15** — August 6 intraday high (the current cycle high).

**Support:**
- **~23.9–24.1** — 10 EMA (23.96) / VWMA (24.08); the immediate line in the sand.
- **~22.3–22.5** — confluence of the 50 SMA (22.34), Bollinger lower band (22.01), and recent July lows (07-24 close 22.53; 08-10 low 22.75). This is the zone where a failed consolidation would turn into a deeper correction.
- **17.73** — 200 SMA (major long-term support, ~27% below; only relevant in a severe scenario).

## 7. Actionable Insights

1. **Trend-following bias remains bullish.** Price is above every major average, all averages are rising, and MACD is positive. The current condition is a **pullback within an uptrend**, not a trend break.
2. **Tactical trigger:** The 08-12 close above the 10 EMA (23.96) and VWMA (24.08) is the first sign of short-term stabilization after the −10.8% decline from the 27.15 spike high. A sustained hold above ~24.0–24.1 opens a path back toward the 25.5 Bollinger upper band, then the 27.15 cycle high.
3. **Invalidation / risk line:** A daily close below ~22.3–22.5 (50 SMA + lower band confluence) would signal the consolidation is deepening and likely target the 21–21.5 area (late-May/June shelf). Stops for longs are best placed below this zone, sized against the elevated ATR.
4. **Momentum confirmation to watch:** A MACD histogram print back above zero and an RSI reclaim of 55–60 would confirm the momentum re-acceleration; currently the histogram's flattening (−0.066 → −0.052) is early, tentative evidence of that.
5. **Position management:** With ATR at ~5% of price, keep per-trade risk modest and avoid leverage until volatility contracts or a decisive close above 25.5 occurs.

## 8. Summary Table

| Dimension | Indicator | Value (2026-08-12) | Read |
|---|---|---|---|
| Price (verified) | Close | 24.23 | +1.1% reclaim of 10 EMA; stabilizing after Aug 6 spike |
| Long-term trend | close_200_sma | 17.73 (rising) | Strong uptrend; price +36.7% above |
| Medium-term trend | close_50_sma | 22.34 (rising) | Uptrend intact; price +8.5% above; key support ~22.3–22.5 |
| Short-term timing | close_10_ema | 23.96 (flattening) | Bullish if price holds above; bearish if lost |
| Momentum | macd / macds / macdh | 0.38 / 0.43 / −0.05 | Positive but consolidating; histogram flattening |
| Momentum oscillator | rsi | 54.06 | Neutral — no exhaustion, no panic |
| Volatility | atr | 1.20 (~5% of price) | Elevated → size positions smaller, stops wider |
| Volume confirmation | vwma | 24.08 | Price slightly above → recent buying supported |
| Volatility bands (snapshot) | boll / boll_ub / boll_lb | 23.75 / 25.49 / 22.01 | Upper-half placement; resistance 25.5, support 22.0 |
| Cycle extremes | High / Low | 27.15 (08-06) / 12.31 (2025-11-06) | +96.8% off the Nov 2025 low; −10.8% off the Aug 6 high |

**Bottom line:** RELY is in a confirmed long-term and medium-term uptrend, currently digesting a sharp early-August spike. Momentum is consolidating (not reversing), RSI is neutral, and volume supports the recovery. The constructive scenario requires holding above the ~23.9–24.1 short-term pivot; a close below ~22.3–22.5 would invalidate the near-term bullish setup. Given elevated ATR, disciplined risk sizing is the key execution variable.