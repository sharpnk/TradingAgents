All data is in. I have the verified snapshot, the full OHLCV history since 2026-05-14, and time-series for the 8 selected indicators. Here is the detailed analysis.

---

# CBRS (Cerebras Systems Inc., NMS) — Technical Analysis Report
**Analysis date: 2026-08-07 (using latest trading row 2026-08-06)**

## 1. Indicator Selection Rationale (8 chosen)

| # | Indicator | Why it was selected (complementary role) |
|---|---|---|
| 1 | `close_10_ema` | Short-term responsiveness; CBRS is a high-beta AI/semiconductor name where fast shifts matter. Gives timely entry/exit timing. |
| 2 | `close_50_sma` | Medium-term trend gauge; price just reclaimed it (Aug 4–6) — key to judge whether the recovery is real. |
| 3 | `close_200_sma` | Long-term regime benchmark; price is still below it (~219), so it defines the bull/bear dividing line. |
| 4 | `macd` | Momentum crossover detection; the MACD line just crossed above zero on ~Aug 4 — a major regime signal. |
| 5 | `rsi` | Overbought/oversold + divergence; was ~31 at the June low, now ~52 — shows momentum repair without exhaustion. |
| 6 | `atr` | Volatility/risk sizing; ATR ≈ 11% of price — stop placement and position sizing are paramount. |
| 7 | `vwma` | Volume-weighted trend confirmation; price above VWMA supports the recovery with volume participation. |
| 8 | `boll_ub` | Volatility envelope/overbought zone; upper band ≈ 233.5 marks the breakout target / overbought threshold. |

Redundant indicators deliberately excluded: `boll`/`boll_lb` (volatility already captured by `boll_ub` + `atr`), `macds`/`macdh` (same MACD family as `macd`; referenced below from the snapshot for context).

## 2. Verified Market Snapshot (source of truth, 2026-08-06)

| Metric | Value |
|---|---:|
| Close | 211.30 |
| Open / High / Low | 206.51 / 219.50 / 205.00 |
| Volume | 2,950,600 |
| close_10_ema | 207.13 |
| close_50_sma | 208.90 |
| close_200_sma | 219.09 |
| RSI | 51.72 |
| MACD / Signal / Histogram | 1.83 / -1.62 / 3.45 |
| Bollinger Mid / Upper / Lower | 200.02 / 233.55 / 166.49 |
| ATR | 23.41 |
| VWMA (Aug 6) | 203.14 |

## 3. Trend Analysis

**Long-term picture: still corrective.** CBRS debuted on 2026-05-14 at $350.00, spiked to an intraday high of $386.34, and closed its first day at $311.07 on volume of ~33.5M shares. From that first close, the stock is down **-32.1%** to $211.30. The June slide bottomed with an intraday low of $160.81 on 2026-06-26 (close $181.59).

**Medium-term: recovery off a higher low.** After the June 26 low, the stock recovered to ~$221 (June 30–July 1), pulled back to a secondary low of $169.39 (July 29 close, intraday low $168.71 — a clear **higher low** vs. $160.81), and has since rallied to $227.15 on Aug 4 and $211.30 on Aug 6. From the July 29 close to the Aug 4 close, that is **+34.1%** in four sessions; from the June 26 close to the Aug 4 close, **+25.1%**.

**Moving-average structure (key nuance):**
- Price ($211.30) closed **above** the 10 EMA ($207.13) and above the 50 SMA ($208.90) for a third consecutive session (Aug 4–6) — first sustained reclaim of the 50-day line since the June breakdown.
- Price remains **below** the 200 SMA ($219.09), which is still sloping down (it declined from ~$254 on June 8 to ~$219 now, though part of that series is affected by data-window limitations — see Discrepancies).
- The 50 SMA is also still declining (254.56 → 208.90 over the window), so the recovery is occurring *beneath* two descending longer-term averages. This is an **early-stage, not yet confirmed, trend reversal**.

## 4. Momentum Analysis

- **MACD:** The MACD line was deeply negative in June/July (e.g., -12.57 on June 26, -10.66 on July 8) but crossed **above zero between Aug 3 (-1.75) and Aug 4 (+0.61)**, reaching +1.83 by Aug 6. It sits well above its signal line (-1.62) with a positive, expanding histogram (+3.45). This is a textbook **fresh bullish momentum crossover** — the strongest MACD reading since the data window began.
- **RSI:** Recovered from 31.2 (June 25) and the mid-July 37–41 range to **51.72** — dead center of neutral. Momentum has repaired without reaching overbought (>70), leaving headroom for further upside. There is no negative divergence at present.

## 5. Volatility Analysis

- **ATR:** $23.41 and declining (from ~$31.3 on June 8, ~$28 on June 29). Still **~11.1% of the current price** — exceptionally high. Daily ranges of $10–$20+ are the norm (e.g., Aug 4 range $214.05–$230.99). Position sizing must assume ~2× ATR daily swings.
- **Bollinger Bands:** Price ($211.30) sits in the **upper half** of an extremely wide band (mid $200.02, upper $233.55, lower $166.49). The upper band has compressed from ~$324 (June 8) to ~$233.5, i.e., volatility is normalizing lower, but the envelope is still ~33% wide relative to the mid-band.

## 6. Volume Analysis

- **VWMA** (volume-weighted MA): $203.14 on Aug 6 and **rising** (from $197.4 on July 29). Price above VWMA confirms the rally is volume-supported rather than a low-volume drift. Note the Aug 4 up-day carried 5.3M shares vs. ~3.0M on the Aug 6 pullback — the advance had heavier participation than the subsequent dip.

## 7. Key Price Levels (derived from tool output)

| Type | Level | Basis |
|---|---|---|
| Resistance | ~$227 | Aug 4 high/close ($230.99 / $227.15) |
| Resistance | ~$219–220 | 200 SMA ($219.09) + Aug 3 close ($219.97) + prior July 23 close ($220.00) |
| Resistance (stretch) | ~$233.5 | Bollinger upper band |
| Support | ~$208–209 | 50 SMA ($208.90) + Aug 3 low ($184.85 is lower, but 50 SMA is the dynamic level) |
| Support | ~$200–203 | Bollinger mid ($200.02) / VWMA ($203.14) |
| Support (deeper) | ~$169 | July 29 low ($168.71) / higher-low reference |

## 8. Discrepancy Flags (tool-vs-snapshot)

- The `close_200_sma` series from `get_indicators` returns values **identical to `close_50_sma` for most dates before ~July 31** (e.g., both show 222.0779 on July 24). This is almost certainly because only 58 trading rows of price history exist in the window — too few to compute a genuine 200-day average — so the vendor backfilled the 200 SMA with the 50 SMA. The **verified snapshot** is the only trustworthy 200 SMA reading: **$219.09 on Aug 6**. I used the snapshot value and do not treat the earlier 200-SMA series as valid.
- All other indicator values reconcile cleanly between the two sources (MACD 1.83, RSI 51.72, ATR 23.41, Bollinger upper 233.55, 10 EMA 207.13, 50 SMA 208.90).

## 9. Actionable Insights

1. **Regime is transitioning, not confirmed.** A fresh MACD zero-line crossover, three closes above the 50 SMA, price above a rising VWMA, and a higher low at ~$169 all argue the intermediate downtrend is being repaired. However, the 200 SMA (~$219) still caps price, and both long averages are declining.
2. **The pivotal test is $219–227.** A sustained daily close above $227 (Aug 4 high) with volume would confirm the reversal and open the path to the $233.5 upper Bollinger band. Failure at $219–227 keeps the tape range-bound/corrective.
3. **Risk management is non-negotiable.** At ATR ≈ $23.4 (~11% of price), a single-day adverse swing can exceed 5%. Stop placement near 1.5–2× ATR below entry (roughly $35–47) or structural stops below $200 / $169 should be sized accordingly. Position sizes should be materially smaller than for a low-volatility name.
4. **Do not chase strength without confirmation.** RSI at ~52 is not stretched, so a pullback toward the $203–209 support cluster (VWMA/Bollinger mid/50 SMA) would offer a better risk/reward than buying at $211 mid-range.
5. **Watch the 50 SMA slope.** The 50 SMA must flatten/turn up for the recovery to mature; it is still declining.

## 10. Summary Table

| Factor | Reading (verified) | Implication |
|---|---|---|
| Price vs. 10 EMA / 50 SMA | $211.30 > $207.13 / $208.90 | Short-term bullish; medium-term reclaim in progress |
| Price vs. 200 SMA | $211.30 < $219.09 (declining) | Long-term trend still bearish; ~$219 is the regime line |
| MACD | 1.83 vs signal -1.62, hist +3.45 | Fresh bullish crossover (above zero since Aug 4) |
| RSI | 51.72 | Neutral; momentum repaired, not overbought |
| ATR | 23.41 (~11% of price, falling) | Extreme volatility; use wide stops / small size |
| Bollinger | Mid 200.02, Upper 233.55, Lower 166.49 | Price in upper half; wide envelope; band compression = normalization |
| VWMA | 203.14, rising; price above | Volume-confirmed recovery |
| Support cluster | ~200–209; deeper ~169 | Pullback-buy zone / structural stop reference |
| Resistance | ~219–227; stretch 233.5 | Breakout confirmation zone |
| Trend structure | Higher low (169.39 vs 160.81) + higher closes | Early-stage reversal, not yet confirmed |

**Net assessment:** The weight of evidence (MACD crossover, 50-SMA reclaim, higher low, volume participation, RSI repairing from oversold) favors the bulls tactically, but the declining 200 SMA, still-declining 50 SMA, extreme ATR, and unbroken $219–227 resistance argue against aggressive accumulation. This is a "wait for confirmation or buy the dip" setup, not a chase-the-breakout setup.

FINAL TRANSACTION PROPOSAL: **HOLD**

*(Upgrade to BUY on a sustained daily close above ~$227 with volume; downgrade to SELL/avoid on a daily close below ~$200, which would negate the recovery structure.)*