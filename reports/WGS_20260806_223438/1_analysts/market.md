All data retrieved and cross-checked. The indicator outputs (50 SMA 61.77, 200 SMA 90.04, RSI 58.05, MACD 1.85, MACD signal 1.23, boll_ub 71.34, boll_lb 57.56, ATR 5.36) match the verified snapshot exactly — no discrepancies in the indicator layer. One data-level anomaly needs flagging (see below).

---

# WGS (GeneDx Holdings Corp., NMS) — Technical Trend Report
**Analysis date: 2026-08-06 | Sector: Healthcare / Diagnostics & Research**

## Verified Market Snapshot (source of truth, 2026-08-06)
- **OHLCV:** Open 67.94 / High 70.21 / Low 65.74 / Close **69.59** / Volume 789,100
- **Trend:** 10 EMA 67.07 | 50 SMA 61.77 | 200 SMA 90.04
- **Momentum:** MACD 1.85 | MACD signal 1.23 | MACD histogram 0.62 | RSI 58.05
- **Volatility:** Bollinger middle 64.45 | Upper 71.34 | Lower 57.56 | ATR 5.36

---

## 1. Data Integrity Flag (important)
The raw price series shows a **severe discontinuity on 2026-05-05**: close fell from 67.93 (2026-05-04) to **34.51** (2026-05-05) — approximately −49% in one session — on massive volume (11.26M vs 3.07M the prior day). The `Stock Splits` column reports 0.0 for that date, so this is either a 2-for-1 split not captured in the vendor feed or a major repricing event (e.g., dilutive offering). I am **not** treating this as organic price action, and all percentage claims below stay within either side of that boundary. The indicator vendor computed its values on this same series (verified snapshot matches indicator calls), so there is no indicator-vs-snapshot conflict — the discontinuity simply means the 200 SMA still contains pre-event price levels.

## 2. Trend Structure (Three Horizons)

**Long-term (200 SMA) — Bearish / structural downtrend.** Price at 69.59 is **~22.7% below** the 200 SMA (90.04). The 200 SMA is falling steadily: from ~102.14 (2026-06-08) to 90.04 (2026-08-06), roughly −11.8% over two months. The 50 SMA (61.77) remains below the 200 SMA (death-cross configuration). This is the dominant overhead picture: after peaking near 167 in late November 2025 (close 167.51 on 2025-11-25), WGS spent Q1–Q2 2026 in a sustained decline before the May repricing.

**Medium-term (50 SMA) — Bullish / recovery trend.** Price is **+12.7% above** the rising 50 SMA (61.77, up from 55.65 on 2026-06-08, ≈ +11% in two months). Price reclaimed and has held above the 50 SMA since mid-June (first sustained closes above it around 2026-06-11, when close 60.99 vs 50 SMA 55.46). The 50 SMA has become a dynamic floor, currently ~61.77.

**Short-term (10 EMA) — Bullish.** Close 69.59 is +3.8% above the 10 EMA (67.07), and the 10 EMA sits above the 50 SMA — a healthy short-term alignment within the medium-term recovery.

**Price action summary:** From the post-repricing low close of 34.51 (2026-05-05), price has recovered to 69.59 (+101.7%). From the June low close of 51.80 (2026-06-08), price is +34.3%. Over the last two weeks: 59.10 (07-24) → 69.59 (08-06) = +17.7%. The recovery is real, but it is occurring **beneath a falling 200 SMA** — i.e., a bear-market rally that has reclaimed the medium-term trend.

## 3. Momentum (MACD + RSI)
- **MACD:** Bullish crossover occurred ~2026-07-31 (MACD 0.737 > signal 0.727), after the line had compressed to ~0.06 on 07-28. Since then MACD has expanded to **1.85** vs signal 1.23, with histogram **0.62** and growing. Momentum is firmly positive and accelerating — the strongest MACD expansion of the past month.
- **RSI:** **58.05** — neutral with a bullish tilt. It rose from 44.8 (07-24) to 60.3 (08-04) and has since cooled slightly. No overbought condition (not near 70), so momentum has room to extend, but it is no longer at an oversold entry point either.

## 4. Volatility & Bands
- **Bollinger:** Price (69.59) sits in the **upper half of the bands** (mid 64.45, upper 71.34, lower 57.56), only ~2.5% below the upper band. Band width is ~21.4% of the middle — wide and widening (upper band has risen from ~58.3 on 2026-06-08 to 71.34). The price is pressing into the upper envelope, which typically coincides with either trend continuation (band-riding) or a pullback risk.
- **ATR:** **5.36** (~7.7% of price) and rising from ~4.1 in early June. Volatility expanded sharply with the 2026-08-04 session (open 76.00, high 79.38, low 64.28, close 70.90 — an enormous ~15-point range on 2.66M shares, the heaviest volume in weeks). Position sizing must treat ±5% daily swings as normal.

## 5. Key Price Levels (from verified OHLCV history)
- **Resistance zone ~70–72:** This zone capped multiple rallies — closes of 71.71 (07-01), 70.90 (08-04), highs of 71.80 (07-01) and 71.14 (07-09); it coincides almost exactly with the current upper Bollinger band at **71.34**. The 08-04 rally tagged 79.38 intraday but was rejected, closing back at 70.90 — clear overhead supply in the 70–72 area.
- **Above that:** 79.38 (08-04 intraday high) is the next reference; the falling 200 SMA (~90) is the ultimate overhead magnet but far away.
- **Support:** 10 EMA 67.07 → Bollinger middle 64.45 → rising 50 SMA 61.77 → 58.8–60.9 zone (observed reaction lows on 07-17 low 58.78, 07-24 close 59.10, 07-27 close 60.54) → lower band 57.56.

## 6. Indicator Selection Rationale (8 chosen, no redundancy)
| Indicator | Why it was selected |
|---|---|
| close_50_sma | Defines the medium-term recovery trend; price +12.7% above a rising 50 SMA — the core bullish regime signal |
| close_200_sma | Defines the structural bear context; falling 200 SMA at 90.04 is the key overhead reference |
| macd | Captures momentum acceleration; bullish crossover 07-31 with expanding histogram to 1.85 |
| macds | The signal line needed to identify the crossover and gauge momentum trend (histogram expansion) |
| rsi | Flags overbought/oversold; 58.05 shows neutral-bullish room, no exhaustion yet |
| boll_ub | Marks the immediate overhead/overbought boundary at 71.34 that price is pressing against |
| boll_lb | Marks the lower volatility boundary/support at 57.56 for pullback targets |
| atr | Risk-management backbone; 5.36 (~7.7% of price) quantifies stop placement and position sizing |

Dropped: `close_10_ema` (redundant with MACD's EMA engine and already visible via the 67.07 snapshot value) and `vwma` (volume dynamics were assessed directly from the raw OHLCV series, notably the 08-04 2.66M-share spike).

## 7. Actionable Insights for Traders
1. **The trend hierarchy is mixed:** short/medium-term bullish (price > 10 EMA > 50 SMA, both rising, MACD expanding) but long-term bearish (price < falling 200 SMA). Treat the current move as a **recovery within a downtrend**, not a confirmed new bull phase.
2. **Immediate decision point is 71.34–72:** price is ~2.5% below the upper Bollinger band inside the 70–72 resistance shelf. A **confirmed close above ~72 on above-average volume** (the 08-04/08-05 prints were 2.66M and 0.87M) would target 79.38 and open the path toward the 200 SMA; failure here risks a pullback to 67 (10 EMA), then 64.45 (band middle), then ~61.8 (50 SMA).
3. **Pullback buying zone:** 64–62 (Bollinger middle → 50 SMA confluence) offers a much better risk/reward entry than chasing 69.6 into the upper band, given ATR of 5.36.
4. **Risk management:** with ATR ≈ 5.36, a 1×ATR stop is ~7.7% away; keep position sizes small enough to absorb a full band-width swing (~13.8 points between bands).
5. **Watch RSI:** 58.05 leaves room to run, but a push to 70+ RSI while price stalls below 72 would signal exhaustion rather than breakout.
6. **Flag for further research:** the 2026-05-05 −49% repricing event (with 0.0 in the split column) materially affects all longer-horizon indicator readings (e.g., the 200 SMA); verify the corporate action before relying on long-horizon metrics.

**Net stance:** Momentum favors the bulls in the near/medium term, but the trade is extended into a well-defined resistance shelf under a falling long-term average. Prudent approach: **HOLD** existing longs; initiate/scale in on a confirmed breakout above ~72 with volume, or on pullbacks toward 64–62; avoid chasing strength into the 71.34 upper band.

---

## Summary Table

| Dimension | Indicator | Value (2026-08-06) | Read |
|---|---|---|---|
| Price | Close | 69.59 | +12.7% vs 50 SMA; −22.7% vs 200 SMA |
| Long-term trend | close_200_sma | 90.04 (falling) | Bearish — price below, death-cross structure |
| Medium-term trend | close_50_sma | 61.77 (rising) | Bullish — price above since ~06-11 |
| Short-term trend | close_10_ema | 67.07 | Bullish — price +3.8% above |
| Momentum | macd / macds / macdh | 1.85 / 1.23 / 0.62 | Bullish crossover 07-31; expanding |
| Momentum | rsi | 58.05 | Neutral-bullish; room before 70 |
| Volatility | boll / boll_ub / boll_lb | 64.45 / 71.34 / 57.56 | Upper-half; pressing 71.34 resistance |
| Volatility/Risk | atr | 5.36 (~7.7% of price) | High & rising; size positions accordingly |
| Key resistance | Price levels | 70–72 (multiple rejections), 79.38 (08-04 high) | Break >72 opens 79.38+ |
| Key support | Price levels | 67.07 (10 EMA) → 64.45 (mid-band) → 61.77 (50 SMA) → 57.56 (lower band) | Confluence at 64–62 |
| Volume | Raw OHLCV | 789K (08-06); 2.66M spike 08-04 | Heavy volume at 08-04 reversal day |
| Data anomaly | 2026-05-05 | −49% close vs 05-04; splits column = 0.0 | Flagged — verify corporate action |
| **Recommendation** | — | — | **HOLD**; tactical buy >72 breakout or 64–62 pullback |

FINAL TRANSACTION PROPOSAL: **HOLD**