I now have all the data needed. The verified snapshot and indicator outputs are fully consistent with each other (no discrepancies flagged). Let me compile the detailed analysis report.

---

# TMDX (TransMedics Group, Inc.) — Technical Analysis Report
**Date of Analysis:** 2026-08-06 | **Exchange:** NGM | **Sector:** Healthcare / Medical Devices

## Executive Summary

TMDX is in the early-to-mid stage of a **recovery rally inside a dominant long-term downtrend**. The stock suffered a catastrophic, high-volume crash in early May 2026 (a ~21% gap down on 2026-05-06, closing at $72.92 vs. $94.93 the prior session, on 7.7M shares — roughly 3–7× normal volume), bottomed near **$62.04** (close, 2026-05-14), and has since ground higher. As of 2026-08-06, price closed at **$80.21**, above its rising 50-day SMA ($73.19), its 10-day EMA ($77.54), and VWMA ($75.71), but still **~26% below the 200-day SMA ($108.42)**. Momentum has flipped decisively positive (MACD +1.59, histogram +0.63, RSI 58.7), yet volatility is elevated (ATR $4.54 ≈ 5.7% of price), and price is pressing against the upper Bollinger Band ($81.50) near a swing high — a setup that favors **patience over chasing**.

---

## Indicator Selection Rationale (8 indicators chosen)

| # | Indicator | Category | Why selected (market context) |
|---|-----------|----------|-------------------------------|
| 1 | `close_50_sma` | Trend (medium) | Identifies the medium-term regime; TMDX just reclaimed it and it has turned up — the key trend-inflection signal |
| 2 | `close_200_sma` | Trend (long) | Strategic benchmark; price is 26% below it, quantifying that the structural downtrend is still intact |
| 3 | `close_10_ema` | Trend (short) | Captures the fast momentum of the July–August rally and serves as the first pullback reference |
| 4 | `macd` | Momentum | Shows the shift from deeply negative (−5.28 on 2026-06-08) to positive (+1.59) — a full momentum cycle turn |
| 5 | `rsi` | Momentum | Health check; at 58.7 it confirms strength without the overbought extremes that precede sharp reversals |
| 6 | `boll_ub` | Volatility | Price is at 80.21 vs. upper band 81.50 — quantifies how stretched the short-term move has become |
| 7 | `atr` | Volatility | Elevated at 4.54 (5.7% of price) — essential for position sizing and stop placement in this post-crash tape |
| 8 | `vwma` | Volume | Confirms whether the rally is supported by volume or drifting on thin participation |

These eight cover **trend (3 horizons), momentum (2), volatility (2), and volume (1)** with minimal redundancy — MACD captures EMA-based momentum while RSI captures price-based momentum; Bollinger measures band stretch while ATR measures raw range.

---

## Detailed Trend Analysis

### 1. Multi-Timeframe Trend Structure
- **Long-term (200-day): Bearish.** The 200 SMA is still descending (116.70 on 2026-06-08 → 108.42 on 2026-08-06) and price ($80.21) remains well below it. TMDX is in a **bear market structure**; the December 2025 peak near $156 and the May 2026 crash define this.
- **Medium-term (50-day): Turning bullish.** The 50 SMA bottomed near **$70.78 (2026-07-17/07-20)** and has risen every session since to **$73.19**. Price has held above it since mid-July. The 10 EMA crossed above the 50 SMA around **2026-07-14 to 07-16**, a bullish alignment now in place.
- **Short-term (10-day): Bullish.** The 10 EMA is rising (73.0 on 07-27 → 77.54 on 08-06) and price closed above it. The sequence **10 EMA > price-holding > 50 SMA** is constructive.

### 2. Momentum
- **MACD:** Turned up from −5.28 (06-08) to cross the zero line around **2026-07-27/28** and now stands at **+1.59** vs. signal **+0.96**, with a positive and expanding histogram (**+0.63**). This is a textbook momentum cycle bottom-to-top reversal.
- **RSI:** Recovered from 38.0 (06-30) to 58.7 today, with a brief 64.4 spike on 08-03. It is in the bullish zone but **not overbought** (no 70+ reading), leaving room for further upside without immediate exhaustion.

### 3. Volatility
- **ATR:** 4.54 (up from 3.65 on 07-31), representing ~5.7% of price. The post-crash tape remains volatile; the 2026-08-05 session alone spanned $68.00–$77.41 on 2.95M shares.
- **Bollinger:** Middle band (20 SMA) at $75.47; upper band $81.50; lower band $69.45. Today's close ($80.21) sits in the upper quartile of the band envelope. On 08-03 the close ($81.55) actually pierced the upper band ($79.87 that day) — an early sign of a momentum thrust that is now being tested at the band edge.

### 4. Volume Confirmation
- **VWMA** (75.71) is rising and price is ~5.9% above it — supportive.
- **Caveat:** the 08-06 up day printed **1.10M shares**, materially lighter than the 2.95M on the 08-05 down-day shakeout and the 1.5–1.6M on 08-03/08-04. The rally is currently **not being confirmed by rising volume** at the highs — a caution flag for breakout quality.

### 5. Key Price Levels (from verified data)
- **Resistance:** $81.50 (upper Bollinger) → **$81.55 / $83.39** (08-03 close / intraday high) → $85–$88 (former early-June price zone) → **$108.42 (200 SMA)**.
- **Support:** **$77.54** (10 EMA) → **$75.71** (VWMA) / **$75.47** (Bollinger mid) → **$73.19** (50 SMA) → **$69.45** (lower Bollinger) / $68.00 (08-05 intraday low) → **$62–$64** (May base).
- The 08-05 low of **$68.00** was successfully defended (intraday) and 08-06 closed back at $80.21 — a constructive inside-day recovery after the shakeout.

---

## Actionable Insights

1. **Trend bias:** Short/medium-term bullish, long-term bearish. This is a **counter-trend rally in a downtrend** — trade it with defined risk, not as a new secular uptrend.
2. **Entry strategy (patience):** Rather than chasing at $80 near the upper band, consider entries on a **pullback to $75.5–$77.5** (VWMA/Bollinger mid/10 EMA confluence) with confirmation, or on a **high-volume break and close above $83.40** (above the 08-03 high) targeting $85–$88.
3. **Stop placement:** With ATR at 4.54, a 1× ATR stop is roughly $4.50; a 1.5× ATR stop ≈ $6.80. Stops placed **below the 50 SMA (~$73)** or below $71 would avoid noise, but risk ~10% of entry — size positions accordingly.
4. **Watch items:**
   - A close **below $75.5–$76** would invalidate the short-term thrust and likely retest the 50 SMA ($73.2).
   - The **200 SMA at ~$108** is the structural overhead magnet; the $85–$88 zone is the first meaningful resistance before that.
   - **Volume confirmation** on any breakout above $81.5 is essential given the recent light-volume up days.
5. **Risk context:** This remains a high-beta, post-implosion healthcare name; ATR of 5.7% per day means adverse single-day moves of 5%+ are routine. Keep position sizes small relative to the elevated volatility.

---

## Summary Table

| Metric / Indicator | Current Value (2026-08-06) | Signal / Interpretation |
|---|---|---|
| Close | $80.21 (+$3.72 vs. prior) | Recovered from 08-05 shakeout; near 08-03 swing high |
| close_10_ema | $77.54 | Bullish — price above; EMA rising |
| close_50_sma | $73.19 (rising) | Bullish — reclaimed; medium-term trend turning up |
| close_200_sma | $108.42 (falling) | Bearish — price ~26% below; structural downtrend intact |
| macd / macds / macdh | 1.59 / 0.96 / +0.63 | Bullish — above zero, histogram expanding |
| rsi | 58.69 | Neutral-bullish; room before overbought (70) |
| boll / boll_ub / boll_lb | 75.47 / 81.50 / 69.45 | Price near upper band — short-term stretched |
| atr | 4.54 (~5.7% of price) | High volatility — size positions and stops accordingly |
| vwma | $75.71 (rising) | Bullish but up-days on lighter volume — breakout needs confirmation |
| Key resistance | $81.50–$83.40 → $85–$88 → $108.42 | Sequential upside targets |
| Key support | $77.5 → $75.5–$75.7 → $73.2 → $68–$69.5 | Pullback reference zones |
| Volume (08-06) | 1.10M vs. 2.95M (08-05) | Rally not yet volume-confirmed |

**Bottom line:** TMDX shows a convincing short/medium-term momentum recovery (MACD cycle turn, RSI 58.7, price above a rising 50 SMA and VWMA) but remains in a long-term downtrend with elevated volatility and a stretched short-term position near resistance. The optimal play is to **wait for either a healthy pullback into the $75.5–$77.5 zone or a volume-confirmed breakout above $83.40** before adding exposure; long-term trend followers should await a decisive reclaim of the 200 SMA.

FINAL TRANSACTION PROPOSAL: **HOLD**