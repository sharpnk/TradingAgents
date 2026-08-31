I have all the data needed. All indicator tool outputs are consistent with the verified snapshot (10 EMA 21.96, 50 SMA 29.39, 200 SMA 26.01, RSI 43.55, MACD -2.01, MACDH +0.56, ATR 1.93; VWMA 21.40 from the indicator feed, which the snapshot does not publish — no conflicts otherwise). Here is the full analysis.

---

# PL (Planet Labs PBC) — Technical Analysis Report
**Analysis date: 2026-08-06 | Exchange: NYQ | Sector: Industrials / Aerospace & Defense**

## 1. Market Context (What the tape is telling us)

PL has completed a massive 18-month cycle: from a **$3.38 close on 2025-03-31** it rallied to a **blow-off top close of $51.40 on 2026-05-28**, then suffered a violent distribution and waterfall decline. The single most damaging session was **2026-06-05**, when the stock gapped from a $43.23 open to close at **$32.22 on 40.8M shares** — the heaviest volume in the entire dataset — marking the transition from uptrend to downtrend. The decline continued into a **lower base in late July**, bottoming at a **$19.47 close on 2026-07-29** (intraday low $19.16 on 07-28).

As of today (2026-08-06), PL closed at **$22.72** (O 22.00 / H 23.75 / L 22.00 / V 4.62M), up **+16.7% from the $19.47 July 29 low** — a tentative, low-volume recovery attempt inside what remains a confirmed medium- and long-term downtrend.

## 2. Indicator Selection (8 indicators, non-redundant)

Given the regime — extreme volatility, a waterfall decline, and an early-stage bounce — I selected indicators that cover **four complementary dimensions** without duplication:

| Dimension | Indicator | Why it fits this market |
|---|---|---|
| Short-term trend/momentum | `close_10_ema` | Captures the current bounce's turn quickly; the first average price reclaimed on the way up |
| Medium-term trend | `close_50_sma` | Defines the dominant downtrend slope; acts as the overhead resistance to watch |
| Long-term trend | `close_200_sma` | Strategic benchmark: price sits below it, so the structural regime is still bearish |
| Momentum crossover | `macd` | Below-zero but converging lines flag whether the bounce has follow-through |
| Momentum strength | `macdh` | Histogram expansion/contraction shows whether the bounce is accelerating or fading |
| Overbought/oversold | `rsi` | Was >74 at the May top and <28 at the July low; now recovering — clean mean-reversion read |
| Volatility/risk | `atr` | ATR is the sizing tool here; PL's daily range is ~$1.93, so stops/position sizes must adapt |
| Volume confirmation | `vwma` | Confirms whether the bounce is backed by volume (price has just reclaimed VWMA) |

*(Bollinger values from the verified snapshot — mid 22.44, upper 26.29, lower 18.58 — are referenced as supplementary levels.)*

## 3. Detailed Trend Observations

**Moving averages — bearish medium/long-term, bullish short-term.**
- Close **$22.72 > 10 EMA $21.96**: price reclaimed the 10-day EMA on 08-04 and has held it for three sessions. The 10 EMA has inflected upward (21.41 → 21.96 over 08-03 → 08-06).
- Close **< 50 SMA $29.39**: the 50-day is still falling sharply (from ~$38.7 on 06-05 to $29.39 now), confirming the medium-term downtrend. Every rally toward it has been rejected since June.
- Close **< 200 SMA $26.01**: the long-term average is *rising* (22.78 on 06-05 → 26.01 now) purely because the 200-day window is rolling in the higher prices of Nov-2025–Feb-2026 — but price is still **below it**, meaning the structural regime remains bearish until reclaimed.

**MACD family — bearish regime, bullish acceleration.**
- MACD line **-2.01** vs signal **-2.56**: both deeply below zero (bearish regime), but the MACD line has risen from -3.09 (07-29) to -2.01, and the lines crossed bullishly around 08-03/08-04.
- Histogram **+0.56** and rising for five straight sessions (0.18 → 0.38 → 0.47 → 0.56): momentum is accelerating on the bounce. Note the histogram already whipsawed around zero several times in July (positive 07-01/02, negative mid-July, positive again 07-31) — a warning that below-zero MACD crossovers in this stock can be short-lived.

**RSI — recovering from oversold, not yet bullish.**
- RSI **43.55**, up from **27.39 on 07-29** (oversold) and from **74.42 on 05-28** (overbought top). The recovery off oversold supports the bounce, but RSI < 50 still says the primary momentum is down. A sustained break above 50 would be the first confirmation of a genuine momentum shift.

**ATR — volatility compressing but still high.**
- ATR **$1.93**, down from **$4.77 on 06-05** and from ~$3.5–4.2 through June. Volatility is normalizing (panic phase over), but ±1.93 (~8.5% of price) is still elevated for a single-day move. A 2-ATR stop ≈ $3.86 — position sizes must be small relative to typical setups.

**VWMA — bounce is volume-justified so far.**
- Price $22.72 **> VWMA $21.40**, reclaimed on 08-04 and held. However, the recovery from $19.47 has run on modest volume (~5–6M shares/day) versus the **40.8M-share capitulation day on 06-05** — a low-volume recovery is fragile until volume expands on an approach to resistance.

**Key price structure (from verified snapshot + tape):**
- **Immediate support:** 10 EMA $21.96 → VWMA $21.40 → $21.00 (07-27 close) → $20.4–20.5 (07-28/07-31 closes) → **$19.47** (07-29 swing-low close) → Bollinger lower $18.58.
- **Immediate resistance:** $23.75 (today's high) → $24.9–25.96 (07-15/16 zone) → **$26.01 200 SMA + $26.29 Bollinger upper (confluence)** → **$29.39 50 SMA**.
- Today's close $22.72 sits just above the Bollinger middle ($22.44), with the band still very wide (18.58–26.29), reflecting lingering volatility.

## 4. Actionable Insights

1. **Short-term (1–4 weeks): constructive but countertrend.** The setup — price above 10 EMA and VWMA, rising MACD histogram, RSI recovering off 27, falling ATR — supports a continued bounce *toward* the $26 confluence zone (200 SMA 26.01 + Bollinger upper 26.29). Preferred entries are pullbacks to $21.5–22.2 (10 EMA/VWMA cluster) rather than chasing strength, given ~$1.93 daily ATR.
2. **The pivotal test is $26.00–26.30.** A high-volume close above this would flip the structure from "downtrend with bear-market rally" to "potential basing/reversal," opening a path toward the 50 SMA ($29.39). Until then, treat rallies as countertrend.
3. **Risk discipline is critical.** Stop-loss logic: below $21.00 invalidates the near-term bounce; a close back under $19.47 re-opens the June–July downtrend toward $18.58 (Bollinger lower). With ATR ~1.93, size positions so a 1.5–2 ATR adverse move is an acceptable loss.
4. **Medium-term (1–6 months): downtrend intact.** Price is below both the 50 SMA ($29.39) and 200 SMA ($26.01). The May top ($51.40 close on 05-28) and the 06-05 breakdown (40.8M-share selloff) mark a distribution top; the burden of proof is on the bulls to reclaim the 200 SMA with volume before any trend-reversal thesis.
5. **Watch for volume confirmation.** The bounce's weakness is its light volume. A push toward $26 on expanding volume (>10M shares) would add credibility; a stall at $25–26 on rising volume would signal supply re-entry.

## 5. Summary Table

| Indicator | Value (08-06-2026) | Signal | Interpretation |
|---|---|---|---|
| Close | $22.72 | — | +16.7% off 07-29 low ($19.47); recovery in progress |
| close_10_ema | $21.96 | Bullish | Price reclaimed short-term average; bounce confirmed short-term |
| close_50_sma | $29.39 | Bearish | Falling; overhead resistance — medium-term downtrend intact |
| close_200_sma | $26.01 | Bearish | Price below long-term benchmark; structure remains bearish |
| macd / macds | -2.01 / -2.56 | Improving | Bullish crossover below zero; bearish regime, rising momentum |
| macdh | +0.56 | Bullish | Five-session histogram expansion — bounce accelerating |
| rsi | 43.55 | Neutral | Recovered from 27.39 (oversold); <50 keeps primary momentum down |
| atr | $1.93 | High | Volatility compressing from $4.77 (06-05) but still ~8.5% of price |
| vwma | $21.40 | Bullish | Price above volume-weighted average since 08-04 |
| Bollinger (mid/up/low) | 22.44 / 26.29 / 18.58 | Mixed | Price at middle band; wide band = elevated volatility; $26.29 = key resistance confluence with 200 SMA |

**Bottom line:** The tape shows a violent May–July distribution/downtrend now in a low-volume early bounce. Short-term indicators (10 EMA, VWMA, MACD histogram, RSI) have turned up, but the medium/long-term structure (50/200 SMA) remains firmly bearish. The decisive zone is **$26.00–26.30** (200 SMA + Bollinger upper); above it the thesis improves materially, below $21.00 the bounce is invalidated.

FINAL TRANSACTION PROPOSAL: **HOLD** — do not add fresh long exposure until PL reclaims the $26.00–26.30 confluence (200 SMA/Bollinger upper) on expanding volume, and exit or hedge any longs on a close below $21.00 / re-test of $19.47; existing holders can use strength toward $26–29 (50 SMA) to reduce risk in this still-downtrending, high-ATR tape.