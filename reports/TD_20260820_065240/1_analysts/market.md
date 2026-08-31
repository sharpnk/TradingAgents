I now have all the data needed. Let me compile the analysis. The verified snapshot (latest trading row 2026-08-19) is consistent with the raw OHLCV CSV (both show close 118.35, volume 3,871,700 on 8/19; 2026-08-20 is not a trading day in this dataset). Here is my report.

---

# TD (The Toronto-Dominion Bank) — Technical Analysis Report
**Analysis date: 2026-08-20** (latest verified trading row: 2026-08-19) | **Exchange: NYQ** | Sector: Financial Services / Diversified Banks

## Indicator Selection Rationale

For a large-cap bank trading in a mature multi-month uptrend that has just entered a sharp corrective phase, I selected 8 indicators spanning three complementary categories — avoiding redundancy (e.g., no stochRSI alongside RSI, no duplicate short-term averages):

| Category | Indicators Chosen | Why suitable here |
|---|---|---|
| **Trend** | close_50_sma, close_200_sma, close_10_ema | Distinguish long-term uptrend (200 SMA) from medium-term (50 SMA) and short-term (10 EMA) deterioration — critical for judging whether this is a pullback within an uptrend or a trend change |
| **Momentum** | macd, rsi | MACD histogram is already negative (fresh bearish crossover), RSI has dropped below 50; together they gauge whether selling momentum is accelerating or exhausting |
| **Volatility** | boll_ub, boll_lb, atr | Price has collapsed through the middle band toward the lower band while ATR is expanding — key for setting stop/entry zones and sizing |

---

## 1. Trend Analysis — Uptrend Intact Long-Term, Broken Short-Term

**Long-term (200 SMA):** The 200-day SMA is **101.35** and has risen steadily from ~72.9 in December 2025 to current levels — a textbook rising long-term trend benchmark. The last close of **118.35** sits **+16.8% above** the 200 SMA. The secular uptrend (from ~$67.6 in June 2025 to a closing peak of $124.80 on 2026-07-15, per the dataset) remains structurally intact.

**Medium-term (50 SMA):** This is the key change. The 50 SMA is **119.95**, and the 8/19 close (118.35) is the **first close below the 50 SMA since the indicator data begins in April 2026**. On 8/18 the close was 121.97, still above the 50 SMA (119.86). This fresh break below the medium-term trend line is the single most important warning signal in the data. The 50 SMA now flips from support to potential resistance near the 120 area.

**Short-term (10 EMA):** The 10 EMA is **121.66**; price broke below it on 8/18 and is now **2.7% beneath it**. The short-term structure has clearly rolled over.

**Price action:** The August rally stalled just shy of the July high — closing at 124.36 (8/14) and 124.34 (8/17) vs. the 7/15 closing peak of 124.80 (intraday 8/17 reached 125.47 but closed weak). The last two sessions produced a **-4.82% cumulative drop** (124.34 → 118.35), with 8/19 closing essentially at the day's low (close 118.35 vs. low 118.33) — a wide-range bearish candle on elevated volume. This "lower high" at ~124.3–125.5 followed by a fast break below the 50 SMA resembles a double-top / failed-resistance pattern at the zone, though confirmation of a reversal (vs. a shakeout) is not yet complete.

---

## 2. Momentum — Rolling Over, Not Yet Oversold

**MACD (0.68) vs. signal (0.88), histogram -0.19:** The MACD line is still positive (12-EMA above 26-EMA), but it has **crossed below its signal line** — a fresh bearish crossover — and the histogram has turned negative. MACD has been on a declining trajectory since peaking near 3.0 in late April 2026, making a series of lower highs while price was still climbing toward new highs. That is a classic **momentum divergence** into the August peak.

**RSI (42.34):** RSI fell from 63.16 (8/17) to 42.34 (8/19) in two sessions — a sharp loss of buying momentum. It is now below the 50 midline (bearish short-term regime) but **not yet oversold** (<30), meaning there is still room for further downside before a mean-reversion bounce would be flagged. RSI's lower highs (70.65 on 7/15 → 63.25 on 8/14) corroborate the MACD divergence.

---

## 3. Volatility — Expansion Confirms the Break

**Bollinger Bands:** Middle 20-SMA band is **120.89**, upper band **124.69**, lower band **117.09**. Price (118.35) closed below the middle band and within ~1.1 points of the lower band — the lower half of the envelope. The lower band sits almost exactly on the late-July swing low cluster (close 116.99 on 7/29, intraday low 116.84), making **~117 the pivotal near-term support to watch**.

**ATR (2.15, ~1.8% of price):** ATR has expanded from ~1.77 (late June) to 2.15, with the 8/19 daily range (~4.4 points) running ~2x ATR. This is a genuine volatility expansion accompanying the breakdown — not a quiet drift. For risk management, a 1–2 ATR buffer implies stops of roughly $2.15–$4.30 from entry; a trader entering a mean-reversion long near the lower band would need to respect the 117 level as invalidation.

---

## 4. Volume Context — Distribution on the Breakdown

The 8/19 down day printed **3,871,700 shares**, roughly **2.2x** the prior session (1,738,500 on 8/18) and well above the typical ~1–2M August turnover. Selling into the break below the 50 SMA on expanding volume gives the bearish signal more conviction than a low-volume drift would. Note that the July volatility cluster (7/8–7/10) also saw 6M+ share days, so TD's capacity for high-volume swings in this zone is established.

---

## 5. Key Levels & Scenario Map

| Level | Value | Significance |
|---|---|---|
| Resistance | **~124.3–125.5** | July 15 closing high (124.80) + Aug 17 intraday high (125.47); rejected twice |
| Resistance (now) | **119.95–121.66** | 50 SMA / 10 EMA — any bounce must reclaim this to neutralize the breakdown |
| Pivot / Support | **117.09–117.0** | Bollinger lower band + 7/29 swing low (116.99); last defense before deeper correction |
| Below 117 | ~113–115 | June/July congestion zone (no bounce can be claimed yet — level only) |
| Major trend support | **101.35** | 200 SMA — far below; defines the long-term uptrend boundary |

**Scenarios:**
- **Bullish stabilization:** Reclaim of the 10 EMA (~121.7) and then the 50 SMA (~120) on volume would invalidate the breakdown and re-establish the pullback-buy setup within the uptrend.
- **Neutral/pending:** Holding 117–120 with RSI stabilizing above ~40 suggests a digestion phase; wait for direction.
- **Bearish confirmation:** A daily close below ~117 (lower band + July low) on elevated volume would open the path toward 113–115 and shift the medium-term structure negative, even though the 200 SMA (101.35) remains the ultimate trend anchor.

---

## 6. Recommendation

**FINAL TRANSACTION PROPOSAL: HOLD**

The evidence supports **HOLD** rather than BUY or SELL:
- **Against buying now:** Price broke the 50 SMA and 10 EMA, MACD just issued a fresh bearish crossover, RSI is below 50 with room to fall, and the breakdown came on ~2.2x volume. Nothing in the short-term data yet confirms a bottom.
- **Against selling short:** The long-term uptrend is intact (price +16.8% above a rising 200 SMA), RSI is not oversold-extreme enough to force a capitulation, and the stock is sitting just above a well-defined confluence of support (~117). Shorting into a structurally strong long-term trend near a support confluence is poor risk/reward without a confirmed break of 117.
- **Actionable plan:** Existing holders should trail stops below ~117 (or use ATR-based stops ~1.5–2 ATR below entry). New longs should wait for either (a) a reclaim of the 10 EMA/50 SMA zone (121.7–120) on volume, or (b) a stabilizing bounce off 117–118 confirmed by RSI turning up from the low 40s. A close below 117 on volume invalidates the pullback thesis.

---

## Summary Table

| Indicator | Latest Value (8/19) | Signal | Interpretation |
|---|---|---|---|
| **Close** | 118.35 (low 118.33) | Bearish candle | Closed at day's low after a 2-day -4.82% slide |
| **close_10_ema** | 121.66 | Bearish | Price 2.7% below; short-term trend down |
| **close_50_sma** | 119.95 | Bearish (fresh) | First close below 50 SMA in dataset window; support → resistance |
| **close_200_sma** | 101.35 | Bullish | +16.8% above; long-term uptrend intact and rising |
| **macd / macds / macdh** | 0.68 / 0.88 / -0.19 | Bearish | Fresh MACD < signal crossover; histogram negative; momentum divergence since April |
| **rsi** | 42.34 | Bearish (not oversold) | Below 50; fell from 63.2 in 2 days; more downside room before oversold |
| **boll_ub / boll / boll_lb** | 124.69 / 120.89 / 117.09 | Bearish | Price below mid-band, near lower band; 117 is the pivotal support |
| **atr** | 2.15 | Rising | Volatility expanding (~1.8% of price); 8/19 range ~2x ATR |
| **Volume** | 3,871,700 | Bearish | ~2.2x prior day on the breakdown — distribution characteristics |
| **Overall** | — | **HOLD** | Uptrend intact long-term; short-term breakdown unresolved; wait for 117 hold or 121.7–120 reclaim |

*All exact values sourced from the verified market snapshot for TD on 2026-08-20 (latest row 2026-08-19). No discrepancies were found between the snapshot, raw OHLCV CSV, and indicator outputs.*