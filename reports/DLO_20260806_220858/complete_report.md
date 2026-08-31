# TradingAgents Investment Report

**Ticker:** DLO
**Date:** 2026-08-06
**Depth:** Deep (5 rounds)

## I. Analyst Team Reports

### Market
All data retrieved. The verified snapshot and indicator outputs are consistent (10 EMA 14.94, 50 SMA 13.53, 200 SMA 13.23, RSI 54.14, MACD 0.38, ATR 0.54, Bollinger mid 14.81 — all match). Here is my detailed analysis.

---

# DLO (DLocal Limited) — Technical Indicator Analysis
**Analysis date: 2026-08-06 | Exchange: NMS | Sector: Technology / Software – Infrastructure**

## Market Context

DLO has completed a dramatic recovery arc in 2026. After a sharp breakdown on **2026-05-15** (close fell to $10.83 on 8.4M shares — the heaviest volume of the entire dataset), the stock spent June basing between roughly $11–13. On **2026-07-01** it gapped up on a massive 11.76M-share volume spike, closing at $14.67 (+12.9% from the prior $12.99 close), and pushed to a post-rally peak close of $15.25 on 2026-07-06. Since then, price has been consolidating in a $14.1–$15.5 range. The latest session (2026-08-06) closed at **$14.77** (−2.8% from $15.20), on light volume of 972.6K — a pullback, not a rout.

## Indicator Selection Rationale (8 indicators, non-redundant)

| # | Indicator | Category | Why selected for this market |
|---|-----------|----------|------------------------------|
| 1 | `close_10_ema` | Trend (short) | Captures the current pullback — price just slipped below it; first gauge of short-term momentum loss |
| 2 | `close_50_sma` | Trend (medium) | Rising dynamic support; defines the medium-term uptrend that is being tested |
| 3 | `close_200_sma` | Trend (long) | Strategic trend benchmark; needed to confirm the fresh golden cross and overall bull structure |
| 4 | `macd` | Momentum | Unbounded trend-momentum measure; detects momentum fade vs. trend intact (still > 0) |
| 5 | `rsi` | Momentum | Bounded oscillator; shows overbought has been relieved (71 → 54), leaving room in both directions |
| 6 | `boll` | Volatility | Band context around the 20 SMA — price sits at the middle band, with upper band marking the resistance zone |
| 7 | `atr` | Volatility | Absolute volatility for stop placement and position sizing; ATR is compressing, signaling consolidation |
| 8 | `vwma` | Volume | Volume-weighted confirmation; price is just below VWMA, confirming the pullback is volume-neutral |

This set deliberately avoids redundancy: three trend lengths (short/medium/long), two *structurally different* momentum tools (bounded RSI + unbounded MACD, not a second stochastic oscillator), two volatility views (absolute ATR + relative Bollinger), and one volume-weighted filter.

## Trend Analysis

**Long-term (200 SMA):** Uptrend intact. The 200 SMA bottomed around $13.17 in late June and has been grinding higher to **$13.23** (2026-08-06). Price at $14.77 is **+11.6%** above it. The 200 SMA's turn back up after dipping through May–June is consistent with the post-May recovery.

**Medium-term (50 SMA):** Clearly bullish. The 50 SMA has risen steadily from $12.47 (2026-06-30) to **$13.53** (2026-08-06), and price is **+9.2%** above it. Critically, the **50 SMA crossed above the 200 SMA on ~2026-07-31** (50 SMA $13.26 vs. 200 SMA $13.24; the prior day the 50 SMA at $13.19 was still below the 200 SMA at $13.23). This is a **fresh golden cross** that has since widened to a $0.30 gap — a bullish structural development, though it occurred during the current consolidation, so its durability is not yet proven.

**Short-term (10 EMA):** Pullback in progress. The 10 EMA rose with the July rally to ~$14.94, and price closed below it on 2026-08-06 ($14.77 vs. $14.94, −1.1%). The 10 EMA itself has flattened (14.98 → 14.94 over the last three sessions), indicating short-term momentum has stalled rather than reversed.

**Key levels:**
- **Resistance:** $15.44–$15.65 (recent intraday highs: 7/31 $15.44, 8/4 $15.51, 8/5 $15.65); Bollinger upper band $15.48 — a stacked resistance zone.
- **Immediate pivot:** $14.81–$14.83 (Bollinger middle / VWMA).
- **Support:** $14.1–$14.5 (July consolidation lows — 7/22 low $14.12, 7/23 low $13.90, 7/17 close $14.48); then the rising 50 SMA at $13.53; then the 200 SMA at $13.23.

## Momentum Analysis

**RSI:** Cooled from overbought to neutral. RSI printed 71.4 on 2026-07-07 and 70.6 on 07-10, then faded to **54.14** (2026-08-06). This is a textbook overbought relief within an uptrend — the oscillator has reset without breaking down, giving room for further upside without the prior overextension.

**MACD:** Positive but weakening. MACD peaked at +0.74 on 2026-07-13 and has decayed to **+0.38**. The MACD line ($0.38) is now **below its signal line** ($0.43), with histogram at **−0.05** — a short-term bearish crossover. Importantly, MACD remains comfortably above the zero line, so this reads as momentum consolidation **inside** a bull trend, not a trend reversal.

## Volatility Analysis

**Bollinger Bands:** Middle band $14.81, upper $15.48, lower $14.15. Price ($14.77) sits just below the middle band — the dead center of the band envelope (band width ≈ 9%). The upper band coincides almost exactly with the recent highs ($15.44–$15.65), reinforcing that zone as resistance. The lower band ($14.15) aligns with the July consolidation lows.

**ATR:** Compressing. ATR has declined from $0.68 (2026-07-08) to **$0.54** (2026-08-06) — roughly a 20% reduction — confirming the post-rally consolidation. As a percentage of price, ATR is ~3.7%, which is moderate. For risk management: a 2×ATR stop ≈ $1.08; a 3×ATR swing stop ≈ $1.62 below entry. Note the recent low on 8/6 was $14.64, so a close below the $14.1–$14.2 band-low zone (≈ 2×ATR below the 8/6 close) would signal a failed consolidation.

## Volume Analysis

**VWMA:** $14.83 — price ($14.77) is marginally below the volume-weighted average, consistent with the light-volume pullback. The rally was volume-verified: the 7/1 breakout printed 11.76M shares and 7/2 5.9M, versus the 6/26 anomaly of 13.8M (likely index-related). The current decline is occurring on **declining volume** (8/6: 973K vs. multi-million-share sessions earlier in the week), which is a constructive feature — sellers are not aggressively distributing into this dip. The lack of heavy down-volume argues for treating this as a consolidation rather than distribution.

## Synthesis & Actionable Insights

**Overall posture: medium-term bullish structure, short-term pullback/consolidation.** The fresh 50/200 golden cross, price holding +9–12% above both key SMAs, RSI reset to neutral (54), and MACD still above zero all describe a healthy uptrend pausing after a +35% run from the May low.

**Bullish scenario (confirmation):** A daily close back above ~$14.94–$15.00 (10 EMA / VWMA zone) would signal the pullback is over, opening a retest of the $15.44–$15.65 resistance stack. A decisive break above $15.65 on expanding volume would complete the July consolidation pattern and extend the uptrend.

**Bearish scenario (invalidation):** A close below the $14.1–$14.2 band (Bollinger lower ~$14.15 + July lows) would break the consolidation and open a test of the rising 50 SMA at $13.53; losing that would put the golden cross at risk and target the $13.2 area (200 SMA).

**Tactical guidance:**
- Momentum traders: wait for the 10 EMA / VWMA reclaim before adding longs; the MACD histogram must flip positive again to confirm.
- Swing traders: the $14.1–$14.5 zone is the risk-defined buy area; place stops below $13.90–$14.00 (≈ 2–3×ATR) and target $15.4–$15.6.
- Risk managers: use ATR (0.54) for sizing — current volatility supports ~3.7% stop distances; avoid chasing entries while price is below the 10 EMA.

**Discrepancy note:** No conflicts were found between the verified snapshot and the indicator feeds — all exact values cited above match the verified snapshot (the source of truth for exact claims).

## Key Points Summary

| Metric | Value (2026-08-06) | Signal |
|---|---|---|
| Close | $14.77 (O 14.97 / H 15.16 / L 14.64) | Pullback day, light volume (972.6K) |
| 10 EMA | $14.94 | Price below → short-term momentum stalled |
| 50 SMA | $13.53 (rising) | Price +9.2% above → uptrend intact |
| 200 SMA | $13.23 (rising) | Price +11.6% above → long-term bull structure |
| Golden cross | 50 SMA crossed 200 SMA ~07-31 | Fresh bullish structural signal, gap widening |
| RSI | 54.14 | Neutral; overbought (71) relieved — room both ways |
| MACD / Signal / Hist | 0.38 / 0.43 / −0.05 | Short-term bearish crossover, still above zero (consolidation, not reversal) |
| Bollinger | Mid 14.81 / Upper 15.48 / Lower 14.15 | Price at mid-band; upper band = resistance $15.44–15.65 |
| ATR | 0.54 (~3.7% of price) | Volatility compressing; use for stops/sizing |
| VWMA | $14.83 | Price just below → volume-neutral pullback |
| Resistance | $15.44–$15.65 | Stacked: recent highs + upper Bollinger |
| Support | $14.1–$14.5 → $13.53 (50 SMA) → $13.23 (200 SMA) | Layered, rising floor |
| Key confirmation | Close > $14.94–15.00 | Resumes uptrend toward $15.4–15.6 |
| Key invalidation | Close < $14.1–14.2 | Opens test of 50 SMA / golden-cross zone |

**Bottom line:** DLO is in a confirmed medium-term uptrend (fresh golden cross, price above both key SMAs) undergoing a healthy, low-volume consolidation after a strong July rally. The short-term bias is neutral-to-positive pending a reclaim of the 10 EMA/VWMA (~$14.8–15.0); the risk-defined long zone is $14.1–$14.5 with invalidation below $13.90, and the upside target is the $15.44–$15.65 resistance stack.

### Sentiment
**Overall Sentiment:** **Mildly Bullish** (Score: 5.8/10)
**Confidence:** Low

## DLO Sentiment Report — 2026-07-30 to 2026-08-06

### 1. Source-by-source breakdown

**News headlines (Yahoo Finance, past 7 days) — Mildly Bullish.**
Two articles were captured, both from Zacks, and both frame DLO (DLocal Limited) favorably relative to payment-sector peers:
- *"PRTH or DLO: Which Payments Stock Is the Better Buy for Investors Now?"* — positions DLO ahead of Priority (PRTH) on faster payment growth, a broader emerging-market network, and stronger cash resources, while explicitly flagging **margin risks** as the counterweight.
- *"Flywire vs. dLocal: Which Payments Stock Is the Better Investment Now?"* — positions DLO ahead of Flywire (FLYW) on faster payment growth, strong customer expansion, broad emerging-market reach, and a lower forward sales multiple.

Both are peer-comparison / relative-value pieces rather than event-driven news (no earnings, no product launch, no M&A). The tone is consistently constructive on growth and valuation, with a recurring caveat about margin pressure. Note that both items share a single source (Zacks), so this is a narrow, moderately bullish signal — institutional framing that is favorable but not exuberant.

**StockTwits — Unavailable.**
The StockTwits feed returned an `HTTPError` placeholder for the DLO cashtag window. **No retail bullish/bearish ratio is available.** This removes the single fastest-moving sentiment signal from the read, and I will not infer a retail stance from absence.

**Reddit (r/wallstreetbets, r/stocks, r/investing) — Silent.**
No posts mentioning DLO were found across the three tracked subreddits in the past 7 days. Zero engagement data (no upvotes, no comments) is therefore available. DLO is a ~mid-cap emerging-markets fintech and clearly below the meme-stock attention threshold of r/wallstreetbets and the typical radar of r/stocks/r/investing over this window.

### 2. Cross-source divergences and alignments

There is **no detectable divergence** — and no alignment signal either — because two of the three sources are silent/unavailable. The only observable pattern is a **one-source alignment**: the two Zacks articles are mutually consistent (both bullish on DLO vs. its comparables). The retail-side void means I cannot test whether retail sentiment is chasing or contradicting the institutional framing. This materially limits the robustness of the read.

### 3. Dominant narrative themes

- **Emerging-market payments growth as the core thesis.** Both articles anchor on DLO's faster payment growth and broad EM network reach — the market sees DLO's cross-border/EM payments footprint as its principal value driver.
- **Relative value vs. payment peers.** The consistent comparison frame (PRTH, FLYW) tells us the current narrative is "DLO is the cheaper, faster-growing pick in the group" — a valuation-and-growth argument rather than a pure momentum story.
- **Margin risk as the standing counter-narrative.** The recurring caveat that growth and cash strength come with margin pressure is the one bearish thread visible in the data; it appears in the PRTH comparison article and is the kind of theme that would intensify around earnings.

### 4. Catalysts and risks surfaced by the data

- **Catalyst: peer-relative valuation** — a lower forward sales multiple than Flywire combined with faster growth is an arguable setup for multiple re-rating if the growth narrative holds.
- **Catalyst: continued customer expansion** — "strong customer expansion" is cited as a live driver of sentiment.
- **Risk: margin compression** — the explicit caveat in the coverage; any earnings print showing margin deterioration would likely flip the favorable narrative.
- **Risk: no event catalysts in the window** — the coverage is analytical, not event-driven; there is no fresh company-specific news (earnings, guidance, deals) to anchor a directional move.
- **Data risk: silent retail channel** — no StockTwits or Reddit read means sentiment could swing quickly on news flow with no prior community positioning visible to us.

### 5. Key sentiment signals summary

| Signal | Direction | Source | Supporting evidence |
|---|---|---|---|
| Peer comparison vs. PRTH | Bullish | Yahoo News / Zacks | DLO favored on faster payment growth, wider EM network, stronger cash; margin risk flagged |
| Peer comparison vs. FLYW | Bullish | Yahoo News / Zacks | DLO favored on growth, customer expansion, EM reach, lower forward sales multiple |
| Margin pressure caveat | Mildly Bearish | Yahoo News / Zacks | Explicit counterweight cited in PRTH comparison |
| Retail sentiment (StockTwits) | N/A — unavailable | StockTwits | HTTPError; no bullish/bearish ratio collected |
| Community discussion (Reddit) | N/A — silent | Reddit (wsb/stocks/investing) | No posts mentioning DLO in past 7 days |

### Bottom line

The available data skews mildly bullish: both news items frame DLO as the better-value, faster-growing pick versus its payment peers, with margin risk as the only noted negative. However, this rests on just two articles from a single source, with the entire retail channel (StockTwits, Reddit) dark for the period. Treat this as a **Mildly Bullish, low-confidence** read — a soft constructive tilt to weigh alongside fundamentals and technicals, not a conviction call.

### News
I now have comprehensive data across all sources. Let me compile the full research report.

---

# NEWS & MACRO RESEARCH REPORT — DLO (DLocal Limited)
**Ticker:** DLO | **Exchange:** NMS | **Sector:** Technology / Software – Infrastructure (Cross-Border Payments / Fintech) | **Analysis Date:** 2026-08-06

## 1. Executive Summary

DLocal (DLO) enters the week of 2026-08-06 with a **constructive but momentum-driven news backdrop**. Sell-side commentary (Zacks) has twice in the past week framed DLO as the superior pick among cross-border payments peers (vs. Priority Technology (PRTH) and Flywire (FLYW)) on growth, emerging-market network breadth, cash position, and valuation. A notable +12.9% single-session share-price surge on above-average volume signals rotation into beaten-down fintech names amid the AI sell-off. The only company-specific negative item was a small, pre-arranged insider sale by co-founder/director Sebastian Kanovich (25,700 Class A shares, ~$398K), which is immaterial relative to his retained ~11.6M Class B stake.

The macro backdrop is **mixed-to-firm for DLO's business model**: US growth is steady (Q2 real GDP +0.37% QoQ), unemployment fell to 4.2%, inflation is decelerating (June CPI down 0.42% MoM; core PCE +0.13% in window), and recession odds are low (Polymarket 8%, down 4.5pp). However, **10Y Treasury yields have risen to 4.63% (peaked 4.75% on 7/31)**, the Fed is fully priced on hold (88% probability of zero cuts in 2026), and **oil/Strait of Hormuz geopolitics is injecting volatility into emerging-market currencies and trade** — DLO's core operating theater. Prediction markets imply a 60% chance Hormuz traffic normalizes by year-end but only 12% by Aug 31, leaving a lingering EM currency/trade risk over the near term.

---

## 2. Company-Specific News (DLO, trailing window 2026-07-01 → 08-06)

| Date | Headline | Source | Key Signal |
|---|---|---|---|
| ~08-05/06 | "PRTH or DLO: Which Payments Stock Is the Better Buy?" | Zacks | **Bullish** — DLO favored over Priority on faster payment growth, broader EM network, stronger cash resources; flag: margin risk |
| ~08-05/06 | "Flywire vs. dLocal: Which Payments Stock Is the Better Investment Now?" | Zacks | **Bullish** — DLO favored over Flywire on growth, customer expansion, EM reach, and lower forward sales multiple |
| 07-14 | "DLocal Director Sebastian Kanovich Sells 25,700 Shares ($398,350)" | Motley Fool | **Neutral/minor** — Pre-arranged 10b5-1 plan; retains 11.6M convertible Class B shares; not a control-change signal |
| ~07-30 | "AI Is Selling Off, But These 5 Stocks Could Benefit Next" (includes DLO) | MarketBeat | **Tactically bullish** — DLO cited as beaten-down with strong fundamentals and analyst upside as capital rotates out of crowded AI trades |
| ~07-31 | "DLocal (DLO) Moves 12.9% Higher: Will This Strength Last?" | Zacks | **Mixed momentum** — +12.9% surge on above-average volume; however, earnings-estimate revisions do NOT suggest further strength |
| ~07-29 | "UBS Says It's Time to Diversify — These Are Its 2 Stock Picks" | TipRanks | **Supportive** — DLO appears in diversification-focused stock-picking context (pairs with broader EM/fintech rotation theme) |

**Key takeaways (company-specific):**
- **Fundamental narrative remains intact:** faster payment volume growth, expanding EM merchant network, strong net cash, and a cheaper forward sales multiple than peers.
- **Momentum catalyst exists:** the +12.9% single-day move shows buyer interest, but Zacks' caution on estimate revisions tempers the bullishness — the move may be technical/rotation-driven rather than fundamental-revision-driven.
- **Insider activity is a non-event** from a governance standpoint (10b5-1 plan, small size, founder retains control via Class B).
- **Watch item:** DLO typically reports Q2 earnings in mid-August (historically ~Aug 13-15 window). No Q2 report yet in this window — upcoming earnings are the next major catalyst.

---

## 3. Macroeconomic Environment (FRED data)

| Indicator | Latest | Trend / Window Change | Interpretation |
|---|---|---|---|
| Fed Funds Effective Rate | **3.63%** (Jul) | Flat over 30 days | Policy on hold; market prices ~88% probability of **zero** cuts in 2026 |
| 10Y Treasury Yield | **4.63%** (Aug 5) | +8bp in a month; peaked **4.75%** on 7/31 | Rising long-end yields = valuation headwind for growth/multiples |
| Yield Curve (10Y-2Y) | **+0.44%** (Aug 6) | +8bp (+22%) over window; steepening | Curve firmly positive — recession signal receding |
| CPI (headline) | **332.57** (Jun) | −0.42% in window (MoM decline) | Disinflationary impulse |
| Core PCE | **130.27** (Jun) | +0.13% in window | Core inflation contained, near target |
| Unemployment Rate | **4.2%** (Jun) | −0.1pp from 4.3% (May) | Labor market resilient |
| Real GDP | **$24,270.6B** (Q2 '26 SAAR) | +0.37% QoQ | Modest but positive growth |
| VIX | **15.81** (Aug 5) | Down from 20.66 spike (7/29) | Volatility normalized after Fed-day/tech-selloff spike |

**Macro narrative for a cross-border EM payments name:**
- **Rates/USD:** With the Fed on hold at 3.63% and no cuts priced, the USD should remain relatively firm. A firm USD is a **mild headwind** for EM currencies, compressing DLO's FX take-rate economics at the margin, though DLO's model historically benefits from FX volatility itself (spreads widen).
- **Growth:** Positive US growth + low recession odds (8%) support global e-commerce and cross-border volumes, DLO's revenue drivers.
- **Inflation:** Disinflation helps EM central banks and consumer purchasing power in DLO's markets (LatAm, Africa, Asia).
- **Rates/yields:** Rising 10Y yields (4.63–4.75%) pressure high-multiple software/fintech valuations — a real near-term headwind for DLO's multiple despite improving fundamentals.

---

## 4. Geopolitics & Energy Backdrop (critical for EM exposure)

- **Strait of Hormuz disruption is the dominant macro story of the week.** Headlines: "Oil rises on concerns over Strait of Hormuz reopening plans" (Reuters), "Oil extends gains and stocks fall on fresh Hormuz worries" (AFP), "Asian Government Bonds Fall Amid Rising Oil Prices" (WSJ).
- **Prediction-market reads:** Normal Hormuz traffic by **Dec 31: 60%** (+8pp WoW); by **Aug 31: 12%**; by **Aug 15: 1%**. Iran charging Hormuz fees by Aug 31: **10%** (−16pp WoW — easing). Bab el-Mandeb effectively closed by Aug 31: **5%**.
- **Oil price expectations:** Market assigns only **4%** probability to WTI hitting $110 in August and **12%** to crude hitting an all-time high by Dec 31 — i.e., markets see the oil spike as **contained/pain-trade** rather than a structural repricing.
- **Implications for DLO:** DLO operates in the Middle East (a fast-growing region for the company), Africa, and Asia, plus LatAm. A prolonged Hormuz disruption would (a) raise energy import costs for EM nations, pressuring EM currencies and consumer demand, and (b) create FX volatility that DLO monetizes via spreads. The base case (60% normalization by year-end) is manageable; the tail case (prolonged closure) is a genuine EM-currency risk factor to monitor into DLO's Q2 print.

---

## 5. Prediction Markets — Forward-Looking Consensus

| Market | Probability | Move (1W) | Read |
|---|---|---|---|
| No Fed rate cuts in 2026 | **88%** | −1.8pp | Rates locked at ~3.6%; USD-supportive |
| Any of 6/9/10/11/12 cuts in 2026 | 0% | ~flat | Cut cycle definitively off the table for 2026 |
| US recession by end-2026 | **8%** | −4.5pp | Recession risk de-escalating fast |
| UK recession in 2026 | 14% | +7.5pp | Modest UK wobble (secondary for DLO) |
| Japan recession in 2026 | 32% | −14.0pp | Easing |
| Hormuz normal traffic by Dec 31 | **60%** | +8.0pp | Geopolitical risk fading on longer horizon |
| Crude all-time high by Dec 31 | 12% | −2.0pp | Oil spike seen as contained |

**Net consensus:** Steady Fed, no recession, contained oil disruption. This is broadly a **risk-on, USD-stable macro regime** — supportive for EM payments volume, with the caveat of elevated US yields.

---

## 6. Synthesis & Actionable Insights for DLO

**Bull case (supported by evidence):**
1. Sell-side positioning favors DLO vs. PRTH and FLYW on growth + EM network + cash + lower forward multiple (Zacks, 2 articles this week).
2. Momentum signal: +12.9% one-day surge on above-average volume; rotation into beaten-down non-AI fintech (MarketBeat) is a live market theme.
3. Macro regime is benign for EM commerce: no US recession (8%), disinflation, 4.2% unemployment, positive growth.
4. Insider sale is immaterial (10b5-1, founder retains control) — not a red flag.
5. No direct negative catalysts in the news flow.

**Bear case / risks:**
1. Rising 10Y yields (4.63–4.75%) pressure DLO's multiple; Zacks notes estimate revisions are not improving despite the price spike.
2. Margin/take-rate risk flagged in peer comparisons.
3. Hormuz/oil tail risk: EM currencies (DLO's operating arena) could face stress if disruption persists past September; only 12% chance of normalization by end-August.
4. Strong USD regime (no Fed cuts priced) is a mild structural headwind for EM FX take-rates.
5. Insider sale, while small, adds noise for sentiment-sensitive traders.

**Trading/actionable angles:**
- **Catalyst calendar:** Q2 2026 earnings expected mid-August — the single biggest upcoming catalyst. News flow suggests positioning into the print is improving (analyst coverage positive, momentum up), but Zacks' estimate-revision caution implies expectations management risk.
- **Hedging/monitoring:** Track Hormuz resolution markets (60% by Dec) and WTI volatility; an escalation leg (oil >$110, 4% now) would be a clear negative trigger for EM FX and DLO's near-term economics.
- **Relative value:** The recurring "DLO vs. peer" commentary positions DLO as the cheapest/fastest-growing cross-border payments name — supportive of long/short relative-value flows into DLO versus FLYW/PRTH.
- **Macro overlay:** A yield-driven growth-stock pullback (10Y >4.75%) would be the primary entry opportunity; the fundamental news mix argues against chasing the +12.9% move at highs without earnings confirmation.

**Overall stance for the team:** **HOLD-to-constructive (leaning BUY on weakness before earnings, not at post-spike highs).** Fundamentals and news flow are positive; the valuation/yield backdrop and the Zacks estimate-revision caution argue for patience and a disciplined entry. Final BUY/HOLD/SELL determination to be made by the portfolio decision layer.

---

## 7. Key Points Summary Table

| Category | Event / Data Point | Date | Signal | Actionable Implication |
|---|---|---|---|---|
| Company | Zacks: DLO favored over PRTH and FLYW (growth, EM network, cash, valuation) | 08-05/06 | Bullish | Supports relative-value longs DLO vs. payments peers |
| Company | DLO +12.9% single-session move on high volume | ~07-31 | Mixed | Momentum up, but Zacks flags flat estimate revisions — don't chase |
| Company | Director Kanovich sells 25.7K Class A shares ($398K, 10b5-1); retains 11.6M Class B | 07-14 | Neutral | Non-event; founder control intact |
| Company | Q2 2026 earnings expected mid-August | Upcoming | Catalyst | Primary decision point; position ahead with caution |
| Macro | Fed funds 3.63%, 88% probability of zero 2026 cuts | 08-06 | USD-firm | Mild headwind for EM FX take-rate |
| Macro | 10Y Treasury 4.63% (peak 4.75%) | 08-05 | Bearish for multiple | Growth-stock valuation pressure |
| Macro | CPI June −0.42% MoM; core PCE +0.13%; UNRATE 4.2% | Jun data | Bullish | Disinflation + resilient labor supports EM consumer |
| Macro | Real GDP +0.37% QoQ (Q2 '26); yield curve +0.44% | 08-06 | Bullish | No recession; positive trade/commerce backdrop |
| Macro | VIX 15.81 (spiked to 20.66 on 7/29) | 08-05 | Neutral | Volatility normalized post-Fed-day |
| Geopolitics | Hormuz disruption; oil headlines dominant | 08-05/06 | Risk | 60% normalization by Dec; 12% by Aug 31 — monitor EM FX |
| Geopolitics | Iran Hormuz-fee probability −16pp WoW to 10% | 08-06 | Easing | Tail risk moderating |
| Prediction Mkts | US recession 2026: 8% (−4.5pp); crude ATH by Dec: 12% | 08-06 | Bullish | Risk-on consensus supports EM payments volume |
| Sector | AI sell-off rotation into beaten-down fintech (DLO listed) | ~07-30 | Tactically bullish | Potential inflow theme into DLO |

*Sources: Zacks/Yahoo Finance, Motley Fool, MarketBeat, TipRanks, Reuters, AFP, WSJ, Barrons, FRED (FEDFUNDS, DGS10, T10Y2Y, CPIAUCSL, PCEPILFE, UNRATE, GDPC1, VIXCLS), Polymarket.*

### Fundamentals
I now have comprehensive data across fundamentals, balance sheet, cash flow, and income statements (quarterly and annual). Let me compile the full research report.

---

FINAL TRANSACTION PROPOSAL: **BUY**

---

# DLocal Limited (DLO) — Fundamental Research Report
**Analysis Date: 2026-08-06 | Exchange: NMS (Nasdaq) | Sector: Technology | Industry: Software - Infrastructure (Cross-Border Payments Platform)**

---

## 1. Executive Summary

DLocal Limited is a rapidly scaling emerging-markets payments infrastructure company that just reported a blockbuster first quarter (Q1 2026) with revenue of **$335.9M (+54.9% YoY)**. Full-year 2025 revenue hit **$1.09B (+46.6% YoY)**, a sharp re-acceleration from the +14.7% growth posted in 2024. The company sits on a **fortress balance sheet with ~$913.6M in cash + short-term investments against only $2.8M in total debt** (net cash ≈ 21% of market cap), generates strong free cash flow (~$83M in Q1 2026 alone), and is returning capital to shareholders via buybacks and a $150M special dividend paid in 2025.

The stock trades at **~$14.77** (implied from market cap/shares), a **23.8x TTM P/E but only 13.0x forward P/E**, with ROE near 35% and FCF yield ~9%. Despite margin compression (gross margin declined from 48% in 2022 to 37% in 2025) and emerging-market FX/regulatory risks, the combination of accelerating growth, net cash, and a modest forward multiple supports a **BUY** thesis.

---

## 2. Company Profile & Valuation Snapshot (get_fundamentals)

| Metric | Value |
|---|---|
| Company | DLocal Limited |
| Sector / Industry | Technology / Software - Infrastructure |
| Market Cap | $4,346,355,200 (~$4.35B) |
| Price (implied) | ~$14.77 |
| P/E (TTM) | 23.82x |
| Forward P/E | 13.03x |
| Forward EPS | $1.13 |
| EPS (TTM) | $0.62 |
| Price/Book | 7.84x |
| Book Value / Share | $1.885 |
| Dividend Yield | 1.28% |
| Beta | 0.874 |
| 52-Week High / Low | $16.78 / $10.38 |
| 50-Day / 200-Day Avg | $13.47 / $13.40 |
| Revenue (TTM) | $1,212.7M |
| Gross Profit (TTM) | $436.6M |
| EBITDA (TTM) | $232.4M |
| Net Income (TTM) | $192.1M |
| Profit Margin | 15.8% |
| Operating Margin | 15.7% |
| Return on Equity | 35.0% |
| Return on Assets | 9.2% |
| Current Ratio | 1.33 |
| Free Cash Flow (TTM) | $396.4M |

**Note:** The reported "Debt to Equity: 19.83" appears to be a data artifact; actual total debt on the balance sheet is just **$2.8M** (capital leases only) against $553.3M of equity — true leverage is minimal.

---

## 3. Income Statement Analysis

### 3.1 Annual Trends (FY2022–FY2025)

| ($M) | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| Total Revenue | 418.9 | 650.4 | 746.0 | 1,093.6 |
| Revenue Growth YoY | — | +55.2% | +14.7% | **+46.6%** |
| Gross Profit | 202.2 | 276.9 | 294.7 | 402.8 |
| Gross Margin | 48.3% | 42.6% | 39.5% | 36.8% |
| Operating Income | 133.4 | 176.5 | 140.9 | 222.1 |
| Operating Margin | 31.9% | 27.1% | 18.9% | 20.3% |
| EBITDA | 128.6 | 191.3 | 168.9 | 255.2 |
| Net Income | 108.7 | 149.0 | 120.4 | 196.8 |
| Diluted EPS | $0.35 | $0.49 | $0.39 | $0.65 |
| Effective Tax Rate | 9.6% | 16.5% | 20.2% | 13.9% |

**Key observations:**
- **2024 was a reset year** — revenue growth slowed to 14.7% and EPS fell ~20% on margin compression (gross margin −310bps, operating margin −820bps) and a high tax rate. 
- **2025 marked a strong re-acceleration**: revenue +46.6%, operating income +57.6%, net income +63.4%, EPS +67%.
- Gross margin has secularly declined (48.3% → 36.8%) as the mix shifts toward lower-take-rate, higher-volume markets — a common pattern in scaling payment processors, but worth monitoring.
- Net income in 2025 included a **$14.5M gain on sale of security** (2024: $38.6M) — core profitability is still strong, with normalized EBITDA of $247.0M in 2025 (vs. $137.4M in 2024, +80%).

### 3.2 Quarterly Momentum (Q1'25 → Q1'26)

| ($M) | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 | Q1'26 YoY |
|---|---|---|---|---|---|---|
| Revenue | 216.8 | 256.5 | 282.5 | 337.9 | 335.9 | **+54.9%** |
| Gross Profit | 84.9 | 98.9 | 103.2 | 115.8 | 118.7 | +39.8% |
| Operating Income | 46.2 | 57.2 | 55.6 | 63.1 | 53.6 | +16.0% |
| Net Income | 46.6 | 42.8 | 51.8 | 55.5 | 42.0 | −10.0% |
| Diluted EPS | $0.15 | $0.14 | $0.17 | $0.18 | $0.14 | −6.7% |
| Gross Margin | 39.2% | 38.6% | 36.5% | 34.3% | 35.3% | — |
| Effective Tax Rate | 10.1% | 16.1% | 15.4% | 13.8% | 25.8% | — |

**Critical read-through:**
- Revenue has roughly quadrupled off the Q1'25 base run-rate of $867M → **$1.34B annualized at Q1'26**.
- **Q1'26 net income dipped YoY (−10%)** despite +55% revenue growth — driven by a **tax rate spike to 25.8%** (vs. 10.1% in Q1'25) and a modest sequential revenue dip (−0.6% vs Q4'25). This is a tax-timing/FX effect, not an operational deterioration: pretax income actually rose to $56.5M (Q1'25: $51.9M).
- TTM net income of $192.1M and TTM EPS of $0.62 underpin the 23.8x TTM multiple.

---

## 4. Balance Sheet Analysis (get_balance_sheet)

### 4.1 Liquidity & Capital Position (Quarterly)

| ($M) | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 |
|---|---|---|---|---|---|
| Cash & Equivalents | 511.5 | 476.9 | 604.5 | 424.5 | **815.6** |
| Short-Term Investments | 125.5 | 125.5 | 95.0 | 123.6 | 98.0 |
| Total Cash + ST Inv. | 637.0 | 602.5 | 699.5 | 548.1 | **913.6** |
| Total Debt | 3.9 | 3.9 | 3.7 | 90.3 | **2.8** |
| Net Cash | +633.1 | +598.6 | +695.8 | +457.8 | **+910.8** |
| Receivables | 477.3 | 487.3 | 576.4 | 520.9 | **740.4** |
| Payables & Accrued | 634.8 | 705.4 | 831.5 | 875.9 | **1,156.3** |
| Total Assets | 1,241.6 | 1,221.3 | 1,408.8 | 1,541.0 | **1,825.8** |
| Total Equity | 545.1 | 448.2 | 504.5 | 569.3 | **553.3** |
| Working Capital | 451.0 | 353.8 | 409.3 | 454.8 | **412.0** |
| Current Ratio | 1.65 | 1.46 | 1.46 | 1.47 | **1.33** |

**Key observations:**
- **Q1'26 cash ballooned to $815.6M** (+$391M QoQ) as the ~$86.9M line of credit was repaid (total debt fell from $90.3M to $2.8M) and settlement payables surged with record volumes.
- The large payables/receivables are **merchant settlement float** — normal for payments infrastructure and a sign of growing TPV.
- Goodwill & intangibles rose to $99.1M (from $74.0M at FY25) — modest M&A/tech investment; $9.2M spent on intangibles in Q1'26.
- Equity dipped to $553.3M in Q1'26 after the buyback and retained earnings flow; share count fell to 294.3M ordinary shares (buybacks: $10.1M in Q1'26).

### 4.2 Annual Balance Sheet (FY2021–FY2025)

| ($M) | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Total Assets | — | 826.3 | 1,084.5 | 1,171.3 | 1,541.0 |
| Cash + ST Inv. | — | 249.1 | 325.5 | 330.0 | 548.1 |
| Receivables | — | 218.6 | 319.5 | 457.2 | 520.9 |
| Total Equity | — | 399.6 | 455.0 | 488.9 | 569.3 |
| Retained Earnings | — | 220.0 | 369.6 | 490.0 | 534.8 |
| Total Debt | — | 4.1 | 4.0 | 54.5 | 90.3 |
| Tangible Book Value | — | 348.2 | 397.1 | 425.6 | 495.3 |

The balance sheet has compounded steadily: equity +42% over two years, tangible book value +24% in 2025 alone. Even with the FY25 line-of-credit draw of $86.9M (repaid by Q1'26), leverage was never a concern.

---

## 5. Cash Flow Analysis (get_cashflow)

### 5.1 Quarterly Cash Flows

| ($M) | Q1'25 | Q2'25 | Q3'25 | Q4'25 | Q1'26 |
|---|---|---|---|---|---|
| Operating Cash Flow | 95.4 | 124.5 | 95.2 | 100.4 | 92.8 |
| CapEx | −7.5 | −8.4 | −9.3 | −11.5 | −9.7 |
| **Free Cash Flow** | **87.9** | **116.0** | **85.8** | **88.9** | **83.0** |
| Dividends Paid | 0 | −150.0 | 0 | 0 | 0 |
| Buybacks (Common Stock Payments) | 0 | 0 | 0 | 0 | −10.1 |
| Interest Received | 5.1 | 6.0 | 8.4 | 6.7 | 10.6 |

**FCF has been consistently strong: ~$83–116M per quarter for five straight quarters** — TTM FCF of ~$374–396M. Note Q2'25 included the **$150.0M special dividend** and Q1'26 initiated a $10.1M buyback tranche.

### 5.2 Annual Cash Flows (FY2022–FY2025)

| ($M) | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| Operating Cash Flow | 154.5 | 293.5 | **−32.8** | 415.5 |
| CapEx | −12.4 | −18.2 | −22.6 | −36.8 |
| **Free Cash Flow** | **142.1** | **275.2** | **−55.4** | **378.7** |
| Buybacks | −2.0 | −97.9 | −101.1 | 0 |
| Dividends | 0 | 0 | 0 | −150.0 |
| Net Debt Issuance | −5.6 | −1.1 | +49.9 | +51.2 |

- **FY2024 operating cash flow went negative (−$32.8M)** due to a massive working-capital swing (receivables +$162.6M, payables −$10.1M). This normalized dramatically in FY2025 (OCF $415.5M, payables +$251.1M).
- FY2025 FCF of **$378.7M** converts at ~190% of net income — high-quality cash generation.
- Shareholder returns totaled ~$251M across FY23–FY25 (buybacks + special dividend), with buybacks resuming in Q1'26.

---

## 6. Key Ratios & Quality Metrics

| Metric | Value | Assessment |
|---|---|---|
| ROE (TTM) | 35.0% | Excellent — best-in-class returns on equity |
| ROA (TTM) | 9.2% | Solid for an asset-light platform |
| Gross Margin | 36.8% FY25 (declining from 48.3% FY22) | Watch item — mix-driven compression |
| Operating Margin | 20.3% FY25 | Improving YoY (+140bps) |
| Net Margin | 18.0% FY25 | Strong |
| Net Cash | ~$910.8M (Q1'26) | Fortress balance sheet |
| FCF Yield (TTM) | ~9.1% | Attractive |
| P/E TTM / Fwd | 23.8x / 13.0x | Undemanding vs. 40–55% growth |
| PEG (approx, fwd) | ~0.3–0.5 | Deep value relative to growth |
| Beta | 0.874 | Below-market volatility |
| Dividend Yield | 1.28% | Newly initiated capital returns |

---

## 7. Catalysts, Risks & Actionable Insights

### Positive Catalysts
1. **Revenue re-acceleration**: 55% YoY growth in Q1'26; annualized run-rate now ~$1.34B vs. $1.09B FY25. If 40%+ growth persists, the 13x forward multiple compresses quickly.
2. **Forward EPS of $1.13** implies ~82% EPS growth in 2026 vs. 2025 — analysts expect margin leverage + tax normalization to convert top-line momentum into bottom-line acceleration.
3. **~$911M net cash (~21% of market cap)** provides buyback capacity, M&A optionality, and downside protection.
4. **High ROE (35%) + ~9% FCF yield** — the stock compounds cheaply relative to its earnings power.
5. **Resumption of buybacks** ($10.1M in Q1'26) and 1.28% dividend yield broaden the shareholder-return story.

### Key Risks
1. **Emerging-market exposure**: FX volatility, capital controls, and regulatory changes in LatAm/Africa/Asia can hit revenue, margins, and cash conversion (FY24's negative OCF is the template for what working-capital swings can do).
2. **Structural gross-margin erosion**: 48.3% → 36.8% over four years; if mix shift accelerates, operating leverage may disappoint.
3. **Q1'26 tax-rate spike** (25.8% vs. 10.1% a year ago) and sequential revenue dip (−0.6% QoQ) show near-term earnings can be lumpy; TTM EPS growth lagged revenue growth.
4. **Customer concentration** in large merchants and history of short-seller scrutiny in this name warrant monitoring of disclosures.
5. **One-off gains** ($14.5M security sale in FY25, $38.6M in FY24) partly inflated past net income — use normalized earnings for valuation.

### Trader-Actionable Insights
- **Entry zone**: Stock (~$14.77) sits ~9.6% above its 50-day average ($13.47) and ~10% above the 200-day ($13.40), within the $10.38–$16.78 52-week band. Support cluster: $13.40–$13.47 (moving averages); resistance: $16.78 (52-week high).
- **Valuation gap**: 13.0x forward P/E vs. 35%+ ROE and ~50% revenue growth is a historically cheap setup; any re-rating toward 18–20x forward would imply $20–23.
- **Watch items next quarter**: (1) gross-margin trajectory (needs stabilization above ~35%), (2) tax-rate normalization, (3) sustained OCF > $90M/quarter, (4) buyback cadence, and (5) FX headwinds in Q2.

---

## 8. Summary Table of Key Points

| Category | Key Finding | Implication |
|---|---|---|
| **Identity** | DLocal Limited; Tech / Software-Infrastructure; NMS | Emerging-markets cross-border payments platform |
| **Revenue** | FY25 $1.09B (+46.6%); Q1'26 $335.9M (+54.9% YoY) | Strong re-acceleration; ~$1.34B annualized run-rate |
| **Profitability** | FY25 Net Income $196.8M; TTM $192.1M; EPS TTM $0.62 | Solid 18% net margin; Q1'26 tax spike dampened YoY EPS |
| **Margins** | GM 36.8% (down from 48.3% FY22); OM 20.3% | Watch mix-driven GM erosion; OM improving on scale |
| **Balance Sheet** | $913.6M cash+ST inv vs $2.8M debt; net cash ~$911M | Fortress; ~21% of market cap in net cash |
| **Cash Flow** | FY25 FCF $378.7M; Q1'26 FCF $83.0M; TTM FCF ~$396M | High-quality conversion (~190% of NI in FY25) |
| **Capital Returns** | $150M special dividend (2025); buybacks resumed Q1'26 ($10.1M); yield 1.28% | Shareholder-friendly; optionality for more |
| **Valuation** | P/E 23.8x TTM / 13.0x fwd; P/B 7.8x; FCF yield ~9% | Cheap vs. growth; PEG ~0.3–0.5 |
| **Efficiency** | ROE 35.0%; ROA 9.2%; Current ratio 1.33 | Best-in-class returns; adequate liquidity |
| **Momentum** | Price ~$14.77 vs 50d $13.47 / 200d $13.40; beta 0.87 | Above both moving averages; low volatility |
| **Risks** | EM FX/regulatory; GM compression; Q1'26 tax rate 25.8%; customer concentration; FY24 OCF was negative | Monitor FX, margins, and working capital |
| **Recommendation** | **BUY** | Accelerating growth + net cash + 13x fwd P/E offers favorable risk/reward |

---

*Data sources: get_fundamentals, get_balance_sheet (quarterly & annual), get_cashflow (quarterly & annual), get_income_statement (quarterly & annual) for DLO, retrieved 2026-08-06. All figures in USD unless noted. This report is for informational purposes and does not constitute individualized investment advice.*

## II. Research Team Decision

### Bull

Bull Analyst: **DLO (DLocal Limited) — The Bull Case: This Is What a Compounder Looks Like**

Let’s cut through the noise. I know the bear argument sounds sophisticated: “margin compression,” “EM risk,” “tax-rate spike,” “rising yields,” “momentum without fundamental support.” But when you actually stack the data, the bear case collapses under the weight of the numbers. DLO at **$14.77** is a re-accelerating, cash-rich, dominant emerging-markets payments infrastructure business trading at **13x forward earnings** with a fortress balance sheet. Let me show you exactly why the bull case wins.

---

## 1. Growth Potential: The Re-Acceleration Is Real

The most important number in this entire debate is **Q1 2026 revenue growth of +54.9% YoY**. Not 15%, not 20% — 55%. And this isn’t a one-quarter fluke.

- FY2024 revenue growth: **+14.7%**
- FY2025 revenue growth: **+46.6%**
- Q1 2026 revenue growth: **+54.9%**
- Q1 2026 annualized run-rate: **~$1.34B**, up from $1.09B in all of FY2025

That is not a slowing company. That is a company that hit a rough patch in 2024, re-engineered its growth engine, and is now compounding faster than almost any payments peer.

Where is the growth coming from? Cross-border, emerging-market e-commerce. DLO is not trying to win merchant acquirer share in saturated US/EU markets. It is the infrastructure layer for global merchants who need to collect payments in Latin America, Africa, Asia, and the Middle East. That is a massive, still-underpenetrated TAM. As global e-commerce penetration rises in these regions, DLO is the toll booth.

And the bear says “scalability problem”? DLO generated **$396.4M in TTM free cash flow** while growing revenue 55%. That’s not a business that requires endless capital to grow. That’s an asset-light, high-margin, scalable payments network.

---

## 2. Competitive Advantages: The Moat Is the Emerging-Market Rail Itself

Here’s where I think the bear fundamentally misunderstands DLO’s business model.

This week, Zacks ran *two* peer-comparison pieces — one vs. Priority (PRTH) and one vs. Flywire (FLYW). Both times, **DLO came out ahead on faster payment growth, broader emerging-market network, stronger cash position, and lower forward sales multiple.**

That’s the moat:

- **Local payment methods and local currency settlement** — this is brutally hard to replicate. It takes years of licensing, bank relationships, and local operational expertise.
- **Scale in high-growth markets** — merchants don’t want to integrate five different payment providers across 20 EM countries. They want one platform. DLO is that platform.
- **35.0% ROE** — if the moat were weakening, ROE would be collapsing. Instead, it’s best-in-class.
- **$913.6M cash + short-term investments** — capital strength lets DLO invest through cycles, acquire bolt-on capabilities, and survive regulatory shocks that would cripple smaller competitors.

The bear calls EM exposure a risk. I call it a barrier to entry. Capital controls, currency complexity, regulatory fragmentation — those are exactly why DLO earns high returns. If it were easy, everyone would do it.

---

## 3. Positive Indicators: Financial Health Is the Story

Let’s look at the balance sheet, because it’s genuinely extraordinary.

| Metric | Value |
|---|---|
| Market cap | ~$4.35B |
| Cash + ST investments | **$913.6M** |
| Total debt | **$2.8M** |
| Net cash | **~$910.8M** |
| Net cash per share | **~$3.10** |
| TTM FCF | **$396.4M** |
| FCF yield | **~9%** |
| Forward P/E | **13.0x** |

So when you buy DLO at $14.77, approximately **21% of the market cap is just net cash**. Strip that out, and you’re paying roughly **$11.67 per share for the operating business** — a business doing **$1.13 in forward EPS**. That’s roughly **10x forward earnings on an EV basis** for a company growing revenue 55%.

Add the **+1.28% dividend yield** and resumed buybacks ($10.1M in Q1 2026), and the shareholder-return story is just beginning.

---

## 4. Addressing the Bear Directly: Let’s Take the Objections One by One

### Bear: “Gross margin is compressing — 48.3% in 2022 to 36.8% in 2025.”

I hear this one a lot, and it sounds scary until you look at the bottom line.

- FY2025 operating income: **$222.1M, up 57.6% YoY**
- FY2025 net income: **$196.8M, up 63.4% YoY**
- FY2025 operating margin: **20.3%, up 140bps YoY**

What’s happening? DLO is shifting mix toward higher-volume, lower-take-rate markets — a classic, healthy pattern in payments. Gross margin is not profit margin. The company is converting revenue growth into even faster earnings growth. That’s operating leverage.

And Q1 2026 net income dipped? Yes — but that was **a tax-rate spike to 25.8% vs. 10.1% a year ago**, not an operational collapse. Pretax income actually rose from $51.9M to $56.5M. Tax rates normalize. The growth engine didn't break.

### Bear: “13x forward P/E doesn’t matter because margins are deteriorating.”

Let’s be honest: 13x forward earnings for a company growing revenue 50%+ is cheap by any standard. That’s a PEG ratio around **0.3–0.5**. If DLO simply re-rates to 18x forward earnings — still not demanding for a 35% ROE compounder — the stock goes to **$20+**. You don’t need a speculative multiple expansion; you just need the market to stop pricing DLO like a shrinking business when it’s actually accelerating.

### Bear: “Rising Treasury yields pressure high-multiple fintech names.”

DLO is not a high-multiple fintech on forward earnings. It’s 13x. And with **$911M net cash**, DLO is actually *earning* interest income while competitors are borrowing. Rising yields are a headwind for the bear’s favorite short candidates; they’re a manageable macro backdrop for a net-cash grower.

Also note: **the market is pricing an 88% chance of zero Fed cuts in 2026**, and it hasn’t broken DLO. The stock is holding above its 50-day and 200-day moving averages. That tells me the growth story is absorbing macro pressure.

### Bear: “The +12.9% pop was momentum without fundamental support.”

The Zacks article did caution that earnings estimate revisions weren’t confirming the price surge. Fair point. But what does the price action actually show?

- The move came on **11.76 million shares** — the heaviest real volume event in the dataset.
- The stock is now consolidating between **$14.10 and $15.50** on **declining volume** (the 8/6 pullback was just 972K shares).
- The **50-day SMA crossed above the 200-day SMA** — a fresh **golden cross**.
- RSI reset from overbought ~71 to a neutral **54.14**, which is exactly what a healthy uptrend does before the next leg higher.

The bear sees a failed breakout. I see a **low-volume pullback in an established uptrend**, with layered support at $14.10–$14.50, then the rising 50-day at $13.53, then the 200-day at $13.23. That’s not a fragile chart. That’s a coil.

### Bear: “Emerging-market FX and regulatory risk could blow up the model.”

This is the evergreen bear case for DLO. But here’s the counter: **DLO’s entire value proposition is navigating EM complexity.** FX volatility is not a one-way risk — it creates spread opportunities. Regulatory barriers keep competitors out. DLO has already navigated multiple EM cycles, and it’s sitting on $911M net cash precisely to weather dislocations.

And the macro environment right now is actually supportive:

- **US recession odds are just 8%** — down 4.5 points over the week.
- **June CPI fell 0.42% MoM** — disinflation helps EM consumer purchasing power.
- **Unemployment is 4.2%** and GDP is still growing.
- **The Strait of Hormuz risk is real**, but prediction markets put **60% probability of normalization by year-end**, and crude hitting an all-time high is only at 12%.

A contained oil spike, a resilient US consumer, and disinflation is a *constructive* backdrop for cross-border payments volume.

### Bear: “The insider sale by director Sebastian Kanovich is a red flag.”

Come on. It was **25,700 Class A shares worth ~$398K**, executed under a **pre-arranged 10b5-1 plan**. Kanovich still retains **~11.6 million Class B shares**, which carry control rights. That’s not a founder exiting; that’s a minor portfolio diversification trade. It’s noise.

---

## 5. The Sentiment and News Set-Up Are Improving, Not Deteriorating

The social sentiment read was **mildly bullish (5.8/10)** — and that was based almost entirely on institutional news framing. StockTwits was unavailable and Reddit was silent. That’s actually an *opportunity*, not a negative: **the retail crowd hasn’t piled into DLO yet.** When a stock has this much fundamental momentum and the retail channel is still quiet, the next wave of inflows can drive meaningful upside.

The news flow is constructive:

- Zacks: DLO favored over PRTH on growth, EM network, and cash.
- Zacks: DLO favored over FLYW on growth, customer expansion, and valuation.
- MarketBeat: DLO specifically named as a beaten-down non-AI fintech that could benefit from AI-selloff rotation.

The only missing catalyst is **Q2 2026 earnings, expected mid-August**. That’s a binary event, yes — but the setup is skewed positive because the market is already bracing for margin pressure while DLO is actually re-accelerating revenue. If DLO posts another 40%+ growth quarter with stabilizing margins, this stock re-rates quickly.

---

## 6. The Risk/Reward Is Asymmetrical to the Upside

Let’s put the trade in concrete terms:

- **Current price:** $14.77
- **Immediate resistance:** $15.44–$15.65
- **Breakout target:** $20+ on an 18x forward multiple
- **Support zone:** $14.10–$14.50
- **Invalidation:** a close below $13.90 would break the consolidation and target the 50-day at $13.53

So the bull case offers **$0.70 to $1.00 upside to the immediate resistance, then $5+ upside on the re-rating**, while the risk is defined at roughly **$0.90 to the invalidation level**. That’s a favorable risk/reward even before you factor in the fundamental margin of safety.

And the technicals support the fundamental view:

- Price is **+9.2% above the rising 50-day SMA** and **+11.6% above the rising 200-day SMA**.
- MACD remains **above zero** at +0.38, despite the short-term bearish crossover.
- Bollinger midline at $14.81 is acting as the immediate pivot; the upper band at $15.48 aligns with resistance.
- ATR compression to $0.54 signals the post-rally consolidation is maturing.

---

## Bottom Line: The Bear Is Fighting the Fundamentals

I respect the bear’s caution. Risk management matters. But the bear case relies on cherry-picking a single gross-margin trend, a tax-rate anomaly, and a macro tail risk, while ignoring the fact that DLO is:

- Growing revenue **55%**
- Generating **~$400M in TTM free cash flow**
- Sitting on **~$911M net cash**
- Trading at **13x forward earnings**
- Displaying a **fresh golden cross** on the charts
- Favored by sell-side comparisons against peers

DLocal is a **compounder in the middle of a growth re-acceleration**, and the market is handing you that growth at a reasonable price. The bear can keep worrying about margin percentages. I’ll take the **55% revenue growth, 35% ROE, $3 per share net cash, and a 13x forward multiple** any day.

**Verdict: BUY DLO.** The growth, balance sheet, and technical structure all point higher. This is not a time to be a bear. It’s a time to be a shareholder.
Bull Analyst: **Bull Rebuttal: The Bear Is Fighting the Last Quarter, Not the Next One**

You made a strong case, Bear — I’ll give you credit. You cherry-picked the right single quarter, the right single margin line, and the right single indicator, and you built a tidy narrative. But when you step back and look at the full picture, that narrative falls apart.

Let me take your objections one by one and show you why the bull case is still standing — and why DLO at $14.77 remains a buy.

---

## 1. “Revenue grew 55% but net income fell 10%” — You’re confusing a tax line with a business problem.

Yes, Q1 2026 net income was down year over year. But look *why*:

- Q1 2025 effective tax rate: **10.1%**
- Q1 2026 effective tax rate: **25.8%**

That’s not margin deterioration. That’s tax timing.

Strip out the tax distortion and look at the underlying economics:

- Revenue grew **+54.9% YoY**
- Gross profit grew **+39.8% YoY**
- Operating income grew **+16.0% YoY**
- **Pretax income rose from $51.9M to $56.5M**

DLO earned **more pretax income** in Q1 2026 than in Q1 2025. The net income decline is a tax artifact, not an operational collapse.

And if you want to talk about “compounder” behavior, look at the full-year data, because a single quarter is exactly the kind of misleading snapshot you criticized:

- FY2025 revenue: **+46.6% YoY**
- FY2025 operating income: **+57.6% YoY**
- FY2025 net income: **+63.4% YoY**
- FY2025 operating margin: **20.3%, up 140bps YoY**

That is operating leverage. That is a compounder. The bear case is demanding you ignore the annual trend because one quarter had a tax spike.

As for the “sequential revenue decline” from Q4 to Q1 — Q4 is seasonally the strongest quarter in payments. A small dip from $337.9M to $335.9M is noise, not a trend. The annualized run-rate is still **$1.34 billion**.

---

## 2. The balance sheet is not “settlement float” — it’s a fortress with a net-cash moat.

You correctly note that DLO carries $1.156B in payables. But that’s not debt. It’s merchant settlement liabilities — the other side of the receivables ledger. In payments, that’s how the business works:

- Receivables: **$740.4M**
- Payables: **$1,156.3M**
- But total debt: **$2.8M**
- And cash + short-term investments: **$913.6M**

Even if you haircut the cash for float, DLO still has **$412M of positive working capital** and **zero real leverage**. The current ratio is 1.33 — not 0.8, not 0.5. That’s not “worsening liquidity”; that’s a healthy, scaling payments platform.

And the FY2024 negative FCF you cite? That was a working-capital swing — receivables growing faster than payables. It reversed hard in FY2025:

- FY2025 operating cash flow: **$415.5M**
- FY2025 free cash flow: **$378.7M**
- Q1 2026 free cash flow: **$83.0M**

TTM FCF: **~$396M**. That’s a ~9% FCF yield on a $4.35B market cap. If you want to call that “hostage to working capital,” fine — but every high-growth payments company has working-capital swings. The difference is DLO generates $83–116M of FCF *every single quarter* while growing 50%+.

And don’t forget: DLO is earning **interest income** on that cash. The stronger the “no-cut” Fed regime, the more net interest income DLO collects. That’s a feature, not a bug.

---

## 3. Gross margin compression is not a moat failure — it’s a mix shift into bigger, faster lanes.

The bear says: “a dominant toll booth shouldn’t collect lower tolls every year.”

But that’s not what’s happening. DLO isn’t cutting prices on the same lanes. It’s adding new lanes in emerging markets and winning larger, higher-volume merchants with lower take rates but much larger total payment volumes. That’s the classic Visa/Mastercard/Adyen playbook.

You want proof the moat is intact? Look at the return on equity: **35.0%.** Look at FY2025 operating margin: **20.3%, up 140bps.** Look at FY2025 net income: **+63.4%.**

If competition were crushing DLO’s take rates, those metrics would be collapsing, not expanding. Instead, DLO is converting gross-margin compression into **faster revenue growth and higher absolute profit**. That’s the definition of a winning network business.

And yes, Q1 2026 operating margin was down YoY — but again, that’s a single quarter with investment spend and seasonality. The full-year trajectory is what matters, and the full-year trajectory is up.

---

## 4. The 13x forward P/E is not “hope” — it’s the market underpricing a growth re-rating.

The bear says the forward P/E assumes an 82% EPS jump. But look at the numbers:

- FY2025 EPS: **$0.65**
- Q1 2026 revenue growth: **+54.9%**
- Q1 2026 pretax income: **up**
- Tax rate: **distorted upward**

Consensus forward EPS of **$1.13** doesn’t require a miracle. It requires tax normalization plus continued execution on a 50% growth trajectory. That’s not fantasy; that’s basic math.

Even more important: use the right valuation lens.

- Market cap: **$4.35B**
- Net cash: **~$910.8M**
- Forward earnings: **~$330M** (if $1.13 EPS on ~294M shares)
- EV / forward earnings: **~10.4x**

So on an enterprise-value basis, you’re paying about **10x forward earnings** for a company growing revenue 55% and earning 35% ROE. That’s a PEG of roughly **0.2–0.3**.

The bear wants to use trailing P/E of 23.8x, but that’s like judging a stock one day after a tax shock. The market is forward-looking — and the forward number says DLO is cheap.

---

## 5. Technicals: You see a stall below resistance. I see a healthy consolidation inside a golden-cross uptrend.

Let’s be precise about the chart:

- Price: **$14.77**
- 50 SMA: **$13.53, rising**
- 200 SMA: **$13.23, rising**
- Price is **+9.2% above the 50** and **+11.6% above the 200**
- 50 SMA crossed above 200 SMA on **July 31** — a fresh golden cross

Yes, price is below the 10 EMA. That’s a short-term pullback after a **+35% rally**. That’s not a reversal; that’s the market catching its breath.

And notice *how* DLO is pulling back:

- The July 1 breakout ran on **11.76M shares**
- The August 6 pullback was on **972K shares**

That is low-volume digestion, not distribution. Distribution happens on heavy volume. This is quiet profit-taking and consolidation.

RSI at **54.14** is exactly where a healthy uptrend resets after overbought. MACD is still **above zero**. The negative histogram is barely negative. ATR is compressing, which means the range is tightening for the next move.

Risk/reward? You define downside to $13.53 as 8.4% and upside to $15.65 as 6%. But that only works if you buy at $14.77 and sell at the first resistance. The bull case doesn’t end at $15.65. A breakout above $15.65 opens the path toward **$20+** — and you don’t need a speculative multiple to get there. At 18x forward earnings, DLO is $20.34.

The bear is pricing the stock like a failed rally. The data says it’s a coiled spring.

---

## 6. Macro is not the enemy — it’s neutral-to-supportive for a net-cash EM payments grower.

The bear says rising yields and a strong dollar are headwinds. Let’s look at the actual macro data:

- **US recession odds: 8%, down 4.5 points**
- **Unemployment: 4.2%**
- **Q2 GDP: +0.37% QoQ**
- **June CPI: −0.42% MoM**
- **Core PCE: +0.13%**
- **Yield curve: +0.44% — positive and steepening**

That’s not a deteriorating backdrop. That’s a **resilient, disinflationary, no-recession** environment. Global e-commerce and cross-border payments volume do well when the US consumer stays employed and EM inflation cools.

Strait of Hormuz? Yes, it’s a risk. But prediction markets put **60% odds of normalization by year-end**, and only **12% odds of crude hitting an all-time high**. The probability of Iran charging Hormuz fees fell **16 points week-over-week**. This is a monitored tail risk, not the base case.

And on the strong dollar: DLO monetizes FX volatility. It’s a feature of the business model, not just a threat. Plus, with **~$911M net cash**, DLO is earning interest income while the market waits for Fed cuts that may never come.

The bear’s macro case is a list of standard EM boogeymen. The actual data shows a constructive global backdrop.

---

## 7. Sentiment: “No retail interest” means no froth — that’s a buying opportunity, not a red flag.

The bear says StockTwits was quiet and Reddit was silent, so there’s no marginal buyer. But remember: the marginal buyer in a $4.35B mid-cap is **institutional**, not WallStreetBets.

What did the institutional-facing news say this week?

- Zacks: DLO favored over **PRTH** on growth, EM network, and cash.
- Zacks: DLO favored over **FLYW** on growth, customer expansion, and valuation.
- MarketBeat: DLO named as a beaten-down fintech that could benefit from AI-selloff rotation.

That’s not “weak sentiment.” That’s the sell-side starting to frame DLO as the **relative-value winner** in payments. And the fact that retail hasn’t piled in yet means there’s still room for flows.

The bear also loves the “estimate revisions don’t support the rally” line. But forward EPS of **$1.13** is already in the model. Analysts aren’t chasing the price; they’re waiting for Q2. That’s not bearish — that’s a setup.

---

## 8. The earnings catalyst cuts *in favor* of the bull — because expectations are already depressed.

The bear warns that Q2 2026 could “de-rate” the stock if it’s just okay. But look at what’s already priced in:

- Market is braced for margin compression
- Market is braced for FX volatility
- Market is braced for tax noise
- The stock is only 13x forward earnings

If DLO posts another quarter of 40%+ revenue growth — which is exactly what the trend suggests — and stays anywhere near current margins, the market has to re-rate. You can’t grow revenue 50% at 13x forward earnings forever. Something breaks, and it usually breaks to the upside.

If Q2 misses? The downside is cushioned by **$910M net cash**, a **35% ROE**, and a **~9% FCF yield**. That’s not a fragile momentum stock; that’s a real business with a margin of safety.

---

## Bottom Line: The Bear Is Asking You to Ignore the Trajectory

The bear case is a mosaic of single-quarter noise, settlement-liability optics, and standard EM fear-mongering. The bull case is simple and data-driven:

- **Revenue growth accelerating:** FY24 +14.7% → FY25 +46.6% → Q1'26 +54.9%
- **Profitable at scale:** FY25 net income $196.8M; TTM FCF ~$396M
- **Fortress balance sheet:** $910.8M net cash, $2.8M debt
- **Elite returns:** 35% ROE
- **Cheap on forward earnings:** 13.0x P/E, ~10x EV/forward
- **Fresh golden cross** with price above both 50 and 200 SMAs
- **Sell-side relative-value support** vs PRTH and FLYW

DLocal Limited is not a perfect company. Every EM payments name carries complexity. But at **$14.77**, the market is treating DLO like a deteriorating value trap while the business is generating **55% revenue growth and $83M of free cash flow per quarter**.

I’ll take that mismatch every time.

**Verdict: BUY DLO.** The bear is fighting the last quarter. The bull is investing in the next five years.
Bull Analyst: **Bull Analyst — Closing Argument: The Bear Is Reading the Wrong Pages of the Story**

You know, Bear, I appreciate the effort. You brought receipts, you brought conviction, and you brought the same three talking points every DLO short has leaned on for years: margins are compressing, the cash is just "float," and the forward multiple is a fantasy. But here’s the thing — you keep losing the forest for the trees. Let’s take your final rebuttal apart, line by line, and show everyone why DLO at $14.77 is one of the most asymmetric risk/reward setups in payments right now.

---

## 1. “A compounder compounds earnings.” Yes — and DLO did exactly that in FY2025.

You keep hammering Q1 2026 net income. **But you're conveniently freezing the frame on one tax-distorted quarter.**

Yes, Q1 2026 net income fell 10% YoY. But you *know* why — the effective tax rate jumped from 10.1% to 25.8%. That's not a business problem. That's a tax timing and jurisdiction mix issue. Pretax income *rose* from $51.9M to $56.5M. Operating income *rose* 16% on top of a 55% revenue comp. That's still positive operating leverage, just not the obscene kind you demand.

And if you want to talk about "compounding," look at the actual full-year record:

- FY2025 revenue: **+46.6%**
- FY2025 operating income: **+57.6%**
- FY2025 net income: **+63.4%**
- FY2025 diluted EPS: **+67%**
- FY2025 operating margin: **up 140bps to 20.3%**

That's a compounder. One quarter with a tax spike and timing effects doesn't erase the annual trajectory. You say the "incremental pretax margin" in Q1 was sub-4%. But you're measuring a quarter where DLO is making deliberate investments in new markets, new payment methods, and sales capacity — and still converting 55% revenue growth into $83M of free cash flow. The growth engine is working.

And your point about one-off gains? FY2025 net income included a $14.5M gain. Even if you strip it out, normalized net income was still ~$182M, up massively from FY2024's $120M. That's not "flattered." That's genuine improvement.

---

## 2. The "settlement float" argument doesn't make a $910M net cash position any less valuable.

I never said all $913.6M was unencumbered owner cash. But the bear treats it as *worthless*, which is just as wrong. Let's do the math properly.

DLO has:

- Cash + ST investments: **$913.6M**
- Total debt: **$2.8M**
- Receivables: **$740.4M**
- Payables & accrued: **$1,156.3M**
- Positive working capital: **$412M**

Yes, a portion of the cash is merchant settlement float. That's how payments works. But the company still has **zero net debt**, $412M of positive working capital, and a current ratio of 1.33 — which, by the way, is not "deteriorating." It's normal for a hypergrowth payments platform that is scaling volume faster than settlement cycles can clear.

And your FY2024 negative FCF scare? That was a working capital swing caused by receivables growing faster than payables during an acceleration phase. It reversed violently in FY2025: **$415.5M operating cash flow and $378.7M FCF.** The Q1 2026 FCF of $83M is still a ~9% trailing FCF yield. You call that "unstable." I call that exactly what a high-growth, capital-light network should produce.

Most companies would kill for $83M of quarterly FCF *while growing 55%*. You're treating a feature as a bug.

---

## 3. The forward P/E isn't "hope" — it's the market refusing to price 55% growth.

Your favorite attack is "trailing P/E is 23.8x, so 13x forward is a leap." But think about this from an institutional investor's perspective: they buy earnings *power*, not trailing tax-distorted EPS.

Consensus forward EPS is **$1.13**. That's not some bull fantasy; that's the sell-side's estimate, incorporating everything we know about margins, FX, and growth. At $14.77, that's **13x forward earnings**. For a company growing revenue 55%, with 35% ROE, and ~$910M net cash, that's absurdly cheap.

Use the enterprise-value lens, which correctly strips out net cash:

- Market cap: ~$4.35B
- Net cash: ~$0.91B
- Forward net income: ~$330M (at $1.13 EPS)
- EV / forward net income: **~10.4x**

So you're paying roughly **10x forward earnings** for a business with 55% revenue growth, a 35% ROE, and an asset-light EM payments network. Even if you haircut the net cash for float by 50%, you're still at ~11x forward. A PEG of ~0.2–0.3. That's not a momentum trade. That's a quality compounder priced like a struggling enterprise.

You say trailing EPS is going backwards. TTM EPS is $0.62 because of the Q1 tax hit. But forward EPS is all about the next four quarters, and analysts see tax normalization plus continued growth. Dismissing forward estimates because *you* don't like one quarter is not analysis — it's narrative-driven skepticism.

---

## 4. The technicals aren't a "stall" — they're the quiet pause before the next leg.

You've been very selective with the chart, Bear. Let's put the *full* picture on the table:

- Price: **$14.77**
- 50-day SMA: **$13.53, rising**
- 200-day SMA: **$13.23, rising**
- Golden cross on ~July 31: **50 > 200**
- Price is **+9.2% above the 50** and **+11.6% above the 200**
- RSI: **54.14** — the healthy reset zone, not broken
- MACD: **+0.38, above zero**, yes slightly below signal, but still in positive territory
- ATR: **$0.54** — declining volatility, tightening coil

You call the golden cross "lagging." That's true by definition. And yet it's also one of the most reliable medium-term trend signals in technical analysis. The rally off May's low had volume confirmation: **11.76M shares on 7/1**. The pullback has happened on **972K shares**. That's not distribution — distribution requires heavy selling volume into weakness. This is just profit-taking and base-building.

You frame risk/reward as "up 6% to $15.65, down 8% to $13.53." But that's a strawman. The bull case doesn't end at $15.65. A close above $15.65 opens a measured move toward **$20+** at 18x forward earnings. If you want to compute risk/reward, use the actual target: upside $5.50+ to $20, downside $0.85 to the 50-day SMA. That's roughly a 6:1 reward-to-risk. There aren't many setups like that in this market.

And "no buyers" on the pullback? At $14.77, the stock is holding comfortably above two rising key moving averages. If there were no buyers, it would be testing $13. It's not. That's called accumulation, not exhaustion.

---

## 5. The macro environment is actually your friend when you're a net-cash EM payments platform.

You keep listing macro fears: higher yields, firm USD, Hormuz. Let's address each honestly.

- **Rising yields hurt high-multiple, high-duration stocks.** DLO is at 13x forward earnings — low duration relative to the software/fintech complex. And with $911M net cash, DLO is sitting on *interest income* while yields are elevated. That's a modest tailwind, not a headwind.
- **USD strength.** Yes, a strong dollar can compress USD-reported EM revenue. But DLO's model monetizes cross-border FX flows. Volatility is not just a risk; it's a revenue driver through spreads and conversion economics. And the macro data right now shows disinflation (June CPI −0.42% MoM), no recession (8% odds), and a resilient US consumer (4.2% unemployment). That's a constructive backdrop for global e-commerce volumes.
- **Hormuz and oil.** This is a monitored tail risk, not the base case. Prediction markets imply 60% odds of normalization by year-end. Only a 12% chance of an all-time high in crude. Iran's "Hormuz fee" probability dropped 16 points WoW. In the meantime, oil disruptions create *more* FX volatility — which, again, is the environment DLO knows how to monetize.

The bear says "capital controls and settlement delays." DLO's *entire value proposition* is navigating those complexities. That's why competitors stay out. That's why gross margins are above 35% while volumes compound. The moat is the complexity itself.

---

## 6. Sentiment is quiet, but that's exactly the opportunity.

You say "no retail interest means no marginal buyer." Let me flip that: **when a mid-cap growth stock is still under the radar while institutional sell-side is comparing it favorably to peers, there's massive upside in positioning.**

What did the actual news flow say?

- Zacks: DLO favored over PRTH on growth, EM network, cash.
- Zacks: DLO favored over FLYW on growth, customer expansion, lower forward sales multiple.
- MarketBeat: DLO identified as a beaten-down non-AI fintech that could benefit from rotation as AI trades deflate.

That's not "weak sentiment." That's the beginning of a narrative shift. And the low-confidence sentiment score? It's based on only two sources — which means the crowd hasn't arrived *yet*. When the Q2 print hits and the revenue growth story re-validates, you'll see the inflow.

As for the insider sale — a $398K sale by a co-founder in a 10b5-1 plan while retaining 11.6M shares is not a signal of lost conviction. It's a rounding error. And DLO has already lived through short-seller scrutiny and come out stronger. Governance concerns are part of the EM landscape, and DLO has a $913M balance sheet to back its disclosures.

---

## 7. The Q2 earnings catalyst is asymmetric: even "okay" is good enough at this valuation.

The bear says Q2 could de-rate the stock. But let's look at what's already embedded in the stock price:

- Forward P/E of **13x**
- EV/forward P/E of ~**10x**
- Net cash per share of ~**$3.10**

If Q2 delivers 40%+ revenue growth — and the momentum strongly suggests it will — the stock *has* to re-rate. You cannot have a 55%-growing, 35% ROE, net-cash business permanently stuck at 13x earnings. Something breaks, and it usually breaks upward.

If Q2 is "okay" with stable margins and tax normalization, the forward EPS of $1.13 becomes credible, and the stock moves toward $16–$17 quickly. If Q2 is strong, we're talking $18–$20. If Q2 disappoints — you know what? DLO still has $911M net cash, 35% ROE, and a ~9% FCF yield. The downside is cushioned. Meanwhile, the bear's "downside to $13.23" is just 10% away, and the upside to $20 is 35%. That's an asymmetric setup by every measure.

---

## Final Verdict: Buy DLO Now. The Bear Is Fighting the Last Quarter, Not the Next Five Years.

Bear, I respect the rigor. But your entire thesis is built on:

- A tax-rate anomaly,
- One quarter of operating margin compression,
- A working-capital swing in FY24,
- And a low-volume pullback.

Meanwhile, the bull thesis rests on:

- **Revenue growth accelerating to 54.9%**
- **FY25 earnings up 63%**
- **$396M TTM free cash flow**
- **$910M net cash**
- **35% ROE**
- **13x forward earnings**
- **A fresh golden cross with rising 50 and 200 SMAs**
- **Institutional sell-side framing DLO as the best-value payment stock vs. PRTH and FLYW**

The bear asks you to *avoid* this while it trades at the most reasonable valuation it's had since the early growth days. I ask you to *buy* it while the crowd is still silent.

You don't need a miracle. You just need DLO to keep doing what it's already doing.

**BUY DLO.** The numbers are on our side.
Bull Analyst: # Bull Analyst — Closing Argument: The Bear Keeps Fighting the Last Quarter. We’re Investing in the Next One.

Bear, I’ll give you this much: you’ve got discipline. You’ve hammered the same four beats all debate — Q1 margin compression, the “float” balance sheet, the 13x forward “hope,” and the stall under $15.65. But here’s the problem: every one of those beats requires the investor to ignore the trajectory of this business, the strength of its balance sheet, and the market it operates in. So let me take your final argument head-on one more time — with the data actually in front of us.

---

## 1. “Operating margin collapsed 530bps” — You’re treating a growth investment phase like a terminal disease.

You keep citing Q1 2026 operating margin of 16.0% vs. 21.3% a year ago. Let’s put that in context without the scare tactics.

Q1 2026:

- Revenue: **+54.9% YoY**
- Gross profit: **+39.8% YoY**
- Operating income: **+16.0% YoY**
- Pretax income: **+8.9% YoY** — yes, still up
- Net income: **−10%** — driven almost entirely by an effective tax rate of **25.8% vs. 10.1%** a year ago

Now, which part of that says “broken business”? Revenue growth accelerated to nearly 55%. Gross profit grew 40%. Operating income grew 16% on top of a massive revenue comp. Pretax income grew. The net income decline is a tax-timing and jurisdiction-mix issue, not a demand problem and not a competitive collapse.

You say a real compounder compounds earnings. Fine. Look at FY2025:

- Revenue: **+46.6%**
- Operating income: **+57.6%**
- Net income: **+63.4%**
- EPS: **+67%**
- Operating margin expanded **140bps to 20.3%**

That’s compounding. One quarter with a tax spike doesn’t erase the annual trend. And you keep saying the Q1 operating margin decline is “the business itself” — but you conveniently ignore that DLO is investing in new markets, new local payment methods, and sales capacity to sustain that 55% growth. If you want 55% growth *and* 530bps margin expansion in the same quarter, you’re asking for a business that doesn’t exist outside of a fantasy spreadsheet.

---

## 2. “The cash is just merchant float” — The math still says net cash, zero debt, and a 35% ROE.

You keep pointing to $1.156B in payables as if it cancels out $913.6M in cash. That’s not how payments accounting works, and you know it.

Let’s use the numbers that actually matter:

- Cash + short-term investments: **$913.6M**
- Total debt: **$2.8M**
- Net cash: **~$910.8M**
- Positive working capital: **$412M**
- Current ratio: **1.33**

Yes, some of that cash is settlement float. But DLO still has **zero net debt**, a **$412M working capital surplus**, and a current ratio above 1.3. That’s not a company on the edge of a liquidity crisis — that’s a scaling payments platform with a fortress underneath it.

And your “FCF is hostage to working capital” point? Let’s check the actual record:

- FY2024 FCF: **−$55.4M** — one working-capital swing during an acceleration phase
- FY2025 FCF: **+$378.7M**
- Q1 2026 FCF: **+$83.0M** — on a TTM basis, roughly **$396M**
- TTM FCF yield: **~9%**

You also ask: “If DLO has $911M of free cash, why did they only buy back $10.1M?” That’s easy — they just paid a **$150M special dividend** in 2025, and they’re buying back stock *while growing the business*. The buyback is small because management is prioritizing growth investments at 55% revenue growth. That’s not a red flag. That’s rational capital allocation.

---

## 3. “13x forward is hope, not valuation” — Hope is ignoring a 55% grower at 13x forward earnings.

You keep saying forward EPS of $1.13 is an “82% jump” and therefore unbelievable. But let’s actually build that number:

- FY2025 EPS was **$0.65**
- Q1 2026 pretax income **rose YoY**
- The only reason EPS fell in Q1 was the **tax rate spike**
- If the tax rate normalizes — and it will, because 25.8% is not a structural level for a company that paid 10–16% in the prior four quarters — the earnings power is clearly there
- Consensus forward EPS of **$1.13** is not a fairy tale. It’s what sell-side analysts see when they model tax normalization on a 50%+ grower.

Now run the valuation the way an acquirer or long-term owner would:

- Market cap: **~$4.35B**
- Net cash: **~$0.91B**
- EV: **~$3.44B**
- Forward net income: **~$330M**
- **EV / forward earnings: ~10.4x**

Even if you haircut the net cash for float by 50%, you’re still at **~11x forward earnings** for a company growing revenue nearly 55% with a **35% ROE**. That’s not a momentum trade. That’s a quality compounder trading at a PEG of roughly **0.2–0.3**.

And your “EV / trailing net income is 18x” point? That’s what happens when you use a quarter distorted by a one-time tax hit. The market is forward-looking, and the forward numbers say this is cheap.

---

## 4. The technicals aren’t a “stall.” They’re a low-volume consolidation inside a golden-cross uptrend.

You keep saying price is below the 10 EMA and VWMA, and that’s true. But you’re ignoring the structural trend:

- Price: **$14.77**
- 50 SMA: **$13.53, rising**
- 200 SMA: **$13.23, rising**
- **Golden cross on ~July 31**
- Price is **+9.2% above the 50** and **+11.6% above the 200**
- RSI: **54.14** — a healthy reset, not a breakdown
- MACD: **+0.38, above zero**

Your risk/reward math conveniently stops at first resistance. Let’s do it honestly:

- Upside to $15.65: **+6%**
- But a break above $15.65 opens a measured move to **$20+** — that’s **+35%**
- Downside to 50 SMA at $13.53: **−8.4%**
- Downside to 200 SMA at $13.23: **−10.4%**

So the real setup is: **+35% potential on a confirmed breakout vs. −8–10% to rising support.** That’s a 3:1 or better reward-to-risk. And the pullback is happening on **972K shares** after a breakout on **11.76M shares**. That’s not distribution — distribution needs heavy volume into weakness. This is quiet profit-taking.

You call it “no buyers.” I call it a coiled spring.

---

## 5. The macro environment is not the enemy of a net-cash EM payments grower.

You keep listing yields, USD, and Hormuz. Let’s address all three:

- **10Y at 4.63%:** DLO is at 13x forward earnings, not 40x. It’s not a high-duration story. And with **$911M net cash**, DLO is earning interest income while rates stay high. That’s a tailwind, not a headwind.
- **Firm USD:** Yes, a strong dollar can weigh on USD-reported EM revenue. But DLO monetizes cross-border FX flows — volatility widens spreads and creates trading economics. This is the business DLO is built for.
- **Hormuz:** Real risk, but the base case is contained. Prediction markets put **60% odds of normalization by year-end**. Crude at an all-time high is only **12%**. And Iran’s “Hormuz fee” probability **dropped 16 points week-over-week**. This is a monitored tail risk, not the base case.

Meanwhile, the macro data that actually drives global e-commerce is solid:

- **US recession odds: 8%, down 4.5 points**
- **Unemployment: 4.2%**
- **June CPI: −0.42% MoM**
- **Q2 GDP: +0.37% QoQ**

That’s a disinflationary, no-recession backdrop supportive of cross-border commerce in the EM markets DLO serves.

---

## 6. Sentiment quiet? That’s the opportunity, not the problem.

You say no retail interest means no marginal buyer. I say the absence of retail froth is exactly what you want before a fundamental catalyst.

What’s the institutional-facing news flow actually saying?

- Zacks: **DLO favored over PRTH** on growth, EM network, and cash
- Zacks: **DLO favored over FLYW** on growth, customer expansion, and valuation
- MarketBeat: **DLO named as a beaten-down non-AI fintech that could benefit from rotation**

The sentiment read is “low confidence” only because the retail channel is silent. But the people who actually move a $4.35B mid-cap — institutional portfolio managers — are getting hit with a steady drumbeat of “DLO is the better-value payments pick.” That’s how positioning builds before a breakout.

And the “estimates didn’t move” line? That’s because Q2 earnings are right around the corner. Analysts aren’t chasing price; they’re waiting for the print. That’s not bearish — that’s a setup.

---

## 7. The earnings catalyst is asymmetric — and it favors the bull.

You say Q2 could “de-rate” the stock if margins stay weak. But let’s think about what’s already priced in:

- 13x forward earnings
- ~10x EV/forward earnings
- A market bracing for margin compression
- A stock that’s already corrected from $16.78 to $10.38 and recovered to $14.77

If Q2 delivers anything close to 40%+ revenue growth with stable margins and tax normalization, the **$1.13 forward EPS becomes credible**, and the multiple re-rates toward 18x — that’s **$20+**.

If Q2 is merely “okay,” the downside is cushioned by **$910M net cash**, a **35% ROE**, and a **~9% FCF yield**. This is not a fragile, concept stock. This is a real business.

You point out DLO fell from $16.78 to $10.38 despite the cash. True — because that decline was driven by fear, momentum, and a high-multiple reset. But the difference today is that DLO is no longer priced for perfection at 40x earnings. It’s at 13x forward. The risk asymmetry has flipped in the bull’s favor.

---

## Final Verdict: The Bear Is Still Fighting the Last Quarter. The Bull Is Investing in the Next Five Years.

Bear, you’ve made the most detailed bear case anyone could ask for. But at the end of the day, your entire thesis rests on:

- One tax-distorted quarter
- One operating margin line item during an investment phase
- A working-capital swing from two years ago
- A low-volume pullback under resistance

The bull case rests on:

- **Revenue growth accelerating: +14.7% → +46.6% → +54.9%**
- **FY2025 earnings up 63%**
- **$396M TTM free cash flow**
- **~$911M net cash, $2.8M debt**
- **35% ROE**
- **13x forward earnings / ~10x EV/forward**
- **A fresh golden cross with rising 50 and 200 SMAs**
- **Sell-side framing DLO as the best-value payments stock vs. PRTH and FLYW**
- **A quiet retail channel, meaning the crowd hasn’t arrived yet**

You ask investors to wait for a close above $15.65 on strong volume. Fine — but by then the risk/reward will be worse. The time to buy is when the growth is accelerating, the balance sheet is fortress-strong, the sentiment is still skeptical, and the multiple is still reasonable.

That time is now.

**BUY DLO.** The numbers are on our side — and so is the trajectory.
Bull Analyst: Bear, I’m not going to keep this polite forever — because you’ve now made the same argument three times, and every time it gets more elegant but not more accurate. I’m going to close this debate by doing what you’ve never done: I’m going to put **every** number you cited back into **full context**, and show the jury that the bull case is built on the **quarterly, annual, and five-year trajectory of an actual compounding franchise**, while the bear case is glued together by **one tax-distorted quarter, an accounting-primer misunderstanding of settlement float, and a chart read that conveniently stops at first resistance.**

Let’s settle this once and for all.

---

## 1. You say “operating margin collapsed 530 bps.” I say growth re-accelerated to 55% and operating income *still grew 16% on a 55% comp.*

Bear, look at your own table. You posted Q1 2025 vs Q1 2026:

- Revenue: **+54.9%**
- Gross margin: **39.2% → 35.3%**
- Operating margin: **21.3% → 16.0%**
- Net income: **$46.6M → $42.0M**

That sounds terrifying until you ask the question you’ve avoided in all three rounds: ** *Why* did margins compress?** Not because of a broken toll booth — because DLO is deliberately investing into **new geographies, new local payment methods, and sales capacity** to capture the **$1.34 billion annualized run-rate** it’s now operating at.

But let’s pull the lens back, because that’s what you refuse to do. **FY2025 — the full year we just completed:**

- Revenue: **+46.6%**
- Operating income: **+57.6%**
- Net income: **+63.4%**
- EPS: **+67%**
- **Operating margin expanded 140 bps to 20.3%**

That. Is. A. Compounder. One quarter of deliberate investment spend and a tax spike doesn’t erase the full-year trajectory. And to your “incremental pretax margin is sub-4%” — that’s actually backwards. In Q1 alone, DLO generated **$83M of free cash flow** — a **~9% TTM FCF yield** — while growing 55%. The "growth at any cost" story you're trying to sell is falsified by the cash flow statement. Growth this fast shouldn't throw off this much cash. But it does. Because this is the *opposite* of a low-quality growth story.

---

## 2. You call the balance sheet “merchant float.” I call it a **$910.8M net cash fortress with $2.8M of total debt.**

The bear’s favorite parlor trick is pointing to **$1.156B in payables** and implying it cancels out the cash. Let me explain how a payments *platform* works: **receivables and payables scale with total payment volume.** The same way Microsoft has deferred revenue and Visa has settlement float, DLO has merchant settlement liabilities — and *every single one of them* is matched by cash on the asset side. That’s not leverage. That’s not a red flag. That is the *operating machinery of a growing business.*

Now the facts you left out:

- **Total debt: $2.8M**
- **Net cash: ~$910.8M — roughly 21% of the market cap**
- **Positive working capital: $412M**
- **Current ratio: 1.33** — not 0.8, not 0.5. 1.33.

And your “FCF is hostage to working capital” line? You’re citing the **FY2024 negative FCF** as if it’s a recurring feature. It was a **one-time working-capital swing in an acceleration phase.** FY2025 normalized hard: **$415.5M operating cash flow, $378.7M FCF.** Q1 2026: **$83M FCF**, down only slightly from Q1 2025's $87.9M — *while revenue grew 55% and the company paid a $150M special dividend in the prior year*. That’s not a business fraying at the edges. That’s a business printing capital while it invests.

And to your cheeky question: "If DLO has $911M of free cash, why did they only buy back $10.1M?" Because they **just paid out $150M in a special dividend** and are prioritizing 55% growth investments. Rational capital allocation is not a bear case. It’s a bull case.

---

## 3. “13x forward P/E is hope.” No — it’s the market underpricing a 55% grower with 35% ROE.

You keep saying the $1.13 forward EPS is an “82% jump” and therefore fantasy. But here’s what actually gets us to $1.13:

- FY2025 EPS was **$0.65**
- Q1 2026 pretax income **grew year-over-year** — the business made more money before tax
- Q1 2026’s EPS decline was the **25.8% effective tax rate** vs. 10.1% last year
- Structural tax normalization plus continued 40–55% revenue growth gets you **$1.13 within reach**

And even if we’re *spicy* conservative — says let’s haircut the forward EPS by 20% just to be mean. That’s still **~$0.90 of forward earnings, or ~16x forward P/E for a 50% grower.** You don't need the miracle you're describing. You just need **average execution** for the next four quarters. The estimates were built by professional sell-side analysts, not by a bull analyst with a Sharpie — and your claim that “nobody raised estimates” ignores the fact that **the stock surged *before* the Q2 print.** Analysts hold their numbers until earnings; that's a quirk of the research calendar, not a referendum on the story.

And for the last time, the **EV math** is what an acquirer cares about:

- Market cap: ~$4.35B
- Net cash: ~$0.91B
- EV: ~$3.44B
- Forward income: ~$330M
- **EV / forward earnings: ~10.4x**

That is a payments infrastructure business with **35% ROE**, **$396M TTM FCF**, and **55% revenue growth** trading in **single-digit EV/earnings** when you subtract cash. You want to call that "hope"? The market called it hope at $10 in May. Now it’s $14.77 — and it’s still cheap.

---

## 4. You say “the chart is a stall.” Let’s show the full chart: Golden cross, price above two rising SMAs, low-volume pullback after a **volume-verified** breakout.

I’m glad you keep bringing up the technicals, because they’re actually a *stronger* bull case than the fundamentals. You point to the 10 EMA and VWMA and stop the tape. Let’s roll the tape forward:

- **Price: $14.77**
- **50 SMA: $13.53, rising**
- **200 SMA: $13.23, rising**
- **50 crossed above 200 on July 31 — a fresh golden cross, now widening**
- Price is **+9.2% above the 50** and **+11.6% above the 200**
- **RSI: 54.14** — a healthy reset from overbought, with runway to the upside
- **MACD: +0.38, above zero** — positive momentum territory
- ATR: **0.54 and compressing** — the coil tightening before the next leg

You say the golden cross is a lagging indicator. By definition, yes. And it's still one of the most **statistically robust** medium-term trend signals in the discipline. The breakout on July 1 printed on **11.76M shares**; the pullback on Aug 6 printed on **972K shares**. That's a 12:1 volume ratio. Distribution requires *heavy* volume into weakness. This isn't that. It's quiet profit-taking in an uptrend.

Your “risk/reward is negative” math only holds if you *refuse to use the actual target*:

- Upside to a confirmed breakout: **$20+ (18x forward) = +35%**
- Downside to rising 50 SMA: **−8.4%**
- Downside to rising 200 SMA: **−10.4%**

**That's a 3:1 to 4:1 reward-to-risk setup.** You're pricing the stock like the rally *ends* at $15.65. The bull thesis is that **$15.65 is the launchpad**, not the target.

---

## 5. “Macro is not your friend.” Actually — data says the opposite.

Let’s review the latest macro snapshot, since you keep cherry-picking around the edges:

- **US recession odds: 8% — down 4.5 points in a week**
- **Unemployment: 4.2%**
- **June CPI: −0.42% MoM** — disinflation
- **Core PCE: +0.13%**
- **Q2 GDP: +0.37% QoQ**
- **Yield curve: +0.44% — positively steepening**

That’s a **risk-on, disinflationary, no-recession environment.** It directly supports cross-border e-commerce volume in emerging markets — DLO’s **entire operating theater.**

To the 10Y at 4.63%: DLO trades at **13x forward**, not 40x. It is not a high-duration software story. And sitting on **$911M net cash**, DLO is *earning interest income* in this yield environment. That's a **tailwind**, and no amount of bear theater changes that.

To your Hormuz doomsday: prediction markets put **60% odds of normalization by year-end** and only **12% odds of oil hitting an all-time high**. The "Iran charge" probability dropped 16 points week-over-week. It's a **monitored tail risk** — not the base case. And FX volatility that you fear is *literally* the environment DLO was designed to monetize. Complexity is the barrier to entry that keeps competitors out.

---

## 6. “Quiet retail means no buyer.” It means **no froth, no crowd, and a catalyst ahead.** That’s not a warning. That’s a setup.

Bear — you’ve spent three rounds calling the sentiment weak because StockTwits was down and Reddit was silent. But a $4.35B mid-cap is **institutional territory.** Here’s what the institutional-facing tape said this week:

- **Zacks: DLO favored over PRTH** on faster payment growth, broader EM network, stronger cash
- **Zacks: DLO favored over FLYW** on growth, customer expansion, EM reach, and *lower forward sales multiple*
- **MarketBeat: DLO named as a beaten-down fintech positioned to benefit from AI-selloff rotation**

That is not “weak sentiment.” That is the **sell-side beginning to frame DLO as the relative-value winner in payments.** The “low confidence” score is low *only* because the retail channel is dark.

And the “analysts didn't revise estimates” line — you keep presenting that as a fatal flaw. The *reason* estimates haven't moved is because **the next catalyst, Q2 earnings, is sitting right there in mid-August.** Analysts don't chase a stock up 13% two weeks before a print. That's not skepticism; that's process. The moment DLO delivers the quarter — and the trend says it will — the revisions and the re-rating trigger.

---

## 7. The earnings catalyst is asymmetric **to the upside** — because DLO isn't priced for perfection anymore.

Here's the part you keep ignoring when you warn about a de-rating: **the de-rating already happened.**

DLO fell from **$16.78 to $10.38** in the May selloff. It now sits at **$14.77** — still **12% below the 52-week high**, not above it. The stock is **not** priced at 40x; it's priced at **13x forward**. The market has *already* baked in the margin concerns, the FX concerns, and the governance concerns.

If Q2 shows 40%+ revenue growth — which is exactly the trajectory — with margins anywhere stable and tax normalization, the **$1.13 estimate becomes credible**, the multiple starts moving toward 18x, and we're talking about **$20+**. If Q2 is merely "okay," the downside is cushioned by **$910M net cash, 35% ROE, and a 9% FCF yield.** This isn't a binary story with poor odds. It's a **quality growth business trading in a value multiple, with a defined invalidation at $13.90.** That's precisely the *asymmetry* we want.

---

## The Verdict Is Clear

Bear, you've delivered the best version of the bear case — and it still requires the jury to ignore:

- The **55% growth acceleration**
- The **FY25 earnings +63% print**
- The **$396M TTM FCF**
- The **$910M net cash with $2.8M of debt**
- The **35% ROE**
- The **13x forward multiple**
- The **golden cross with rising 50 and 200 SMAs**
- The **sell-side peer-comparison tailwind**
- And the **non-arrival of the retail crowd**

The bear case asks investors to *buy the story that the tax-distorted last quarter is forever, and the forward estimates are lies*. The bull case simply says: **DLO is doing exactly what it needs to do — compounding revenue, compounding cash, stacking net cash — and the market is pricing it like a wounded enterprise.** That mismatch is the entire opportunity.

The numbers aren't "hope." The growth isn't "a story." And at $14.77, this is not a momentum trade with a value costume. It's a quality compounder going through a **legitimate, low-volume consolidation before its next leg up.**

**BUY DLO now, before the Q2 print forces the crowd to pay $20 for what we're pointing out today at $14.77.**

Case closed.

### Bear

Bear Analyst: **Bear Analyst Rebuttal: DLO — You’re Buying a Story the Numbers Keep Contradicting**

Thanks, bull. I appreciate the confidence. But let’s be honest about what you’re actually doing: you’re taking one strong quarter, one big volume spike, and one Zacks headline, and extrapolating that into a “compounder” thesis. That’s not investing; that’s hoping. And the data underneath DLO’s recent bounce tells a much more fragile story.

---

## 1. The “55% Growth” Is Real. The Quality of That Growth Is the Problem.

You keep leading with **Q1 2026 revenue growth of +54.9% YoY**. Great headline. But let’s look at what actually happened to the bottom line in that same quarter:

- **Revenue:** +54.9% YoY  
- **Pretax income:** +8.9% YoY  
- **Net income:** **−10% YoY**  
- **Diluted EPS:** **−6.7% YoY**  
- **Operating margin:** 16.0% vs. 21.3% in Q1 2025  
- **Gross margin:** 35.3% vs. 39.2% in Q1 2025  

So DLO grew revenue by more than half, and **net income went backward**. That is not operating leverage. That is the opposite of operating leverage. A real compounder does not produce less profit when revenue grows 55%.

And the sequential story is just as telling: Q4 2025 revenue was $337.9M; Q1 2026 revenue was $335.9M. That’s a **sequential revenue decline**. You can wave it off as seasonality, but the market is pricing this company as a hyper-growth re-accelerator, not a “flat sequentially” payment processor.

The bull case keeps repeating “55% growth,” but the earnings power of that growth is deteriorating. That’s the single most important fact in this debate.

---

## 2. That “Fortress Balance Sheet” Is Largely Settlement Float — Not Owner Cash

You love the $913.6M cash and short-term investments. But you conveniently ignored the **$1,156.3M in payables and accrued liabilities** sitting right next to it.

In the payments business, a big chunk of that cash is not “fortress capital.” It’s merchant settlement money flowing through the company — recorded as cash on one side and payables on the other. That means DLO doesn’t get to use all of that cash to buy back stock, pay dividends, or fund M&A. It has to hold it to settle merchants.

Look at the trend:

- **Current ratio:** 1.65 in Q1 2025 → **1.33 in Q1 2026**  
- **Receivables:** $740.4M  
- **Payables:** $1,156.3M  

That’s a worsening liquidity position, not an improving one. And remember: DLO’s **FY2024 operating cash flow was −$32.8M**, and FY2024 free cash flow was **−$55.4M**. FCF in this name is hostage to working capital swings. The $378.7M FY2025 FCF number looks great, but it was flattered by a huge payables build. In Q1 2026, FCF was **$83.0M — actually below Q1 2025’s $87.9M**.

So the “9% FCF yield” and “cash-rich” narrative is not as clean as the bull makes it sound.

---

## 3. Gross Margin Compression Is Not “Healthy Mix.” It’s a Competitive Red Flag.

The bull says falling gross margin — from **48.3% in 2022 to 36.8% in 2025** — is just a mix shift toward higher-volume, lower-take-rate markets. But you need to ask yourself: why is a *dominant* toll booth collecting lower tolls every single year?

In 2022, DLO kept roughly **48 cents of every dollar** of revenue. By 2025, it kept **36.8 cents**. And in Q1 2026, it was **35.3%**.

That is not a company gaining pricing power. That is a company facing:

- intensifying competition from payments infrastructure players,
- take-rate pressure in core markets,
- mix shifts into lower-margin geographies or products.

The bull says “gross margin is not profit margin.” Fine. But look at the most recent quarter: **operating margin fell 530 basis points YoY**. Where’s the scale benefit? DLO is spending more to generate each dollar of revenue, and the margin trend says the moat is not as deep as advertised.

---

## 4. The “13x Forward P/E” Is a Hope, Not a Valuation

This is where the bull case gets dangerous. DLO’s **trailing P/E is 23.8x**. The forward P/E of 13x assumes the company will earn **$1.13 per share** over the next year — an implied **~82% earnings jump** from the current trailing EPS of $0.62.

But what did the most recent quarter actually deliver? **Earnings went down.** Margins went down. Net income went down.

Why should anyone underwrite an 82% EPS acceleration when the company just reported a 6.7% EPS decline? That forward number assumes tax rates normalize *and* margins stabilize *and* growth continues *and* no EM FX damage. That’s a lot of “ifs.”

Even if we use the bull’s own balance sheet math, the EV/earnings story is not as impressive as he claims:

- Market cap: ~$4.35B  
- Net cash (using gross cash): ~$0.91B  
- Trailing net income: ~$192M  
- EV / trailing net income: **~18x** — not 10x, and that’s if you treat all the cash as available.

So you’re paying **~18x delivered earnings** for a business whose latest quarter showed a profit decline, margin compression, and deteriorating liquidity. That is not a value trade. That is a momentum trade dressed up as value.

---

## 5. Technicals: The Bull Sees a Coil. I See a Stall Below Resistance.

Let’s talk about the chart, because the bull’s setup is not as clean as he suggests.

- Close: **$14.77**
- 10 EMA: **$14.94** — price is **below** short-term momentum
- VWMA: **$14.83** — price is **below** the volume-weighted average
- MACD: **+0.38 but below its signal line**, with a **negative histogram**
- RSI: **54.14** — neutral, not bullish thrust
- Resistance: **$15.44–$15.65**, stacked with the upper Bollinger band at $15.48
- Current price: **$14.77** — sitting right in the middle, with no breakout confirmation

The 50/200 golden cross sounds impressive, but it is a **lagging indicator**. It only appeared after DLO had already rallied roughly 35% off the May low. And what has happened since the golden cross? The stock has gone sideways and is now below the 10 EMA with a bearish MACD crossover.

Let’s talk about risk/reward honestly:

- Upside to resistance: **$15.65** — about **6%**
- Downside to the 50 SMA: **$13.53** — about **8.4%**
- Downside to the 200 SMA: **$13.23** — about **10.4%**

That is not an asymmetrical long setup. That is a **negative risk/reward** unless you blindly trust the $20 re-rating fantasy.

The bull calls the low-volume pullback constructive. But DLO has now failed twice to close decisively above $15.40–$15.65. A high-volume spike into resistance followed by stalling is how **distribution** looks, not accumulation.

---

## 6. Macro Is Not Your Friend Right Now

The bull says the macro backdrop is supportive. Let me show you why it isn’t:

- **10Y Treasury yield:** 4.63%, peaked at 4.75%
- **Fed:** 88% probability of **zero cuts in 2026**
- **USD:** Firm USD regime is a direct headwind for EM currencies and EM-reported revenue
- **Oil / Hormuz:** Only 12% probability of normalization by Aug 31; 60% by year-end means a **40% chance this tail risk persists into 2027**

DLO earns money in emerging-market currencies and converts it into USD. A strong dollar compresses the USD value of that revenue. A prolonged Hormuz disruption raises energy import costs for the same EM countries DLO depends on. That is not a “contained macro backdrop.” That is a live risk to the business model.

The bull wants to dismiss FX volatility as “spread opportunity.” But FX volatility can also mean capital controls, settlement delays, and hit-or-miss earnings. The FY2024 negative operating cash flow is already a warning sign that working capital in this model can unwind violently.

---

## 7. The Sentiment Data Is Weak, Not “Quiet Opportunity”

The bull says “no retail interest means room for inflows.” I say it means **no marginal buyer**.

The sentiment report itself was **Mildly Bullish at 5.8/10 with low confidence**. The only real inputs were **two Zacks articles** comparing DLO to PRTH and FLYW. That’s not a wave of institutional conviction; that’s a couple of relative-value write-ups. StockTwits was unavailable. Reddit was silent.

Even the positive Zacks articles **explicitly flag margin risk**. And the earlier Zacks piece on the +12.9% spike warned that **earnings estimate revisions do NOT suggest further strength**.

Let me repeat that, because it’s the bull’s Achilles heel: **the stock surged, but estimates didn’t improve.** That means the move was flow-driven, not fundamental-driven. Flow-driven moves reverse when the flow stops.

And the insider sale? Yes, it’s small, and yes, it’s a 10b5-1 plan. I’ll even concede it’s “noise.” But it’s certainly not a bullish signal. A co-founder selling near $15.50 after a big run is not a message of confidence. And DLO has a history of short-seller scrutiny around related-party transactions and governance. That overhang doesn’t disappear because the stock went up 13% in one day.

---

## 8. The Earnings Catalyst Cuts Both Ways — and Risk Is to the Downside

The bull is already looking to Q2 2026 earnings in mid-August as the “re-rating catalyst.” But think about what expectations are baked in:

- Forward EPS of $1.13 assumes an ~82% jump from trailing EPS
- The market has already bid the stock up 35% off the low
- DLO just reported a quarter where net income **fell 10%**
- Margins are still compressing
- The macro/EM FX backdrop is uncertain

If Q2 2026 is just okay, the stock doesn’t re-rate — it **de-rates**, because the forward P/E was built on a margin miracle. If Q2 misses, the downside to $13.53 or $13.23 becomes the path of least resistance.

You don’t need to be short to see the asymmetry. You just need to refuse to pay $14.77 for a story that the last quarter already weakened.

---

## Bottom Line: This Is Not a Compounder Position — It’s a Momentum Trade in a Deteriorating Fundamental Story

I’m not saying DLO is a bad company or that emerging-market payments are a bad industry. I’m saying the **current risk/reward at $14.77 is poor**, and the bull’s best arguments rely on:

- ignoring the **sequential revenue decline**,
- hand-waving the **530bps operating margin drop** in Q1 2026,
- treating **settlement float as owner cash**,
- paying **23.8x trailing earnings** while pretending the forward multiple is guaranteed,
- and trusting a **$20 re-rating** that has no estimate revision support.

A real compounder grows revenue and earnings together. DLO delivered 55% revenue growth and **lower net income**. That is not a “pause in a healthy uptrend.” That is a business whose economics are deteriorating at the operating line, and a stock that has already priced in an optimistic future.

**Bear verdict: AVOID DLO. If you own it, take profits into strength. If you must trade it, demand a close above $15.65 on strong volume with a stable margin quarter before believing the bullish story again. As of 2026-08-06, the downside to $13.53–$13.23 looks far more likely than a green candle to $20.**
Bear Analyst: **Bear Analyst — Final Rebuttal: You’re Buying the Headline, Not the Earnings Power**

Alright, bull — you made me work for it. I’ll concede one thing: you’re consistent. You keep leading with **+54.9% revenue growth**, a **golden cross**, and **$910M net cash**, and you keep hoping the market fills in the rest. But every time you try to wave away the fundamentals, you have to pull a new “trust me” assumption out of the hat. Let’s go through it one more time — because the numbers keep telling a different story.

---

## 1. “Revenue grew 55%, so it’s a compounder.” No. A compounder compounds earnings.

This is the hill your whole thesis dies on, bull.

Q1 2026:

- Revenue: **+54.9% YoY**
- Operating income: **+16.0% YoY**
- Pretax income: **+8.9% YoY**
- Net income: **−10.0% YoY**
- Diluted EPS: **−6.7% YoY**
- Operating margin: **16.0% vs. 21.3% in Q1 2025**
- Gross margin: **35.3% vs. 39.2% in Q1 2025**

Let me put that in plain English: **DLO generated roughly $119 million more revenue year-over-year and kept only about $4.6 million more pretax profit.** That’s a sub-4% incremental pretax margin. A “toll booth” should be keeping 30% or more of incremental revenue. This is not operating leverage — this is **operating deleverage**.

You call the net income decline a “tax artifact.” Fine. But the tax rate doesn’t explain why operating income grew only 16% on 55% revenue growth. It doesn’t explain the 530 basis point operating margin decline. And it doesn’t explain why gross margin has fallen from **48.3% in 2022 to 36.8% in 2025 to 35.3% in Q1 2026**.

You also love the FY2025 annual numbers. But even those are flattered. FY2025 net income included a **$14.5 million gain on sale of security**; FY2024 had a **$38.6M gain**. Strip out the one-offs, and the “compounding” is less impressive. And your own data shows TTM EPS of **$0.62** — *below* FY2025’s $0.65. A real compounder does not see trailing earnings per share go backwards.

**The growth is real. The conversion is not.** You can’t just ignore the bottom line because you like the top line.

---

## 2. The “fortress balance sheet” is partly merchant float — not a war chest you can deploy freely.

You’re obsessed with the **$913.6M cash + short-term investments**. But you conveniently skip over the **$1,156.3M in payables and accrued liabilities** sitting right next to it.

DLO runs a payments platform. A big chunk of that cash is **merchant settlement money** — cash on the asset side, matched by settlement liabilities on the liability side. It is not all discretionary capital for buybacks, dividends, or M&A.

Look at the liquidity trend:

- Current ratio: **1.65 in Q1 2025 → 1.33 in Q1 2026**
- Receivables: **$740.4M**
- Payables: **$1,156.3M**

That’s not a “fortress” improving over time. That’s a balance sheet getting **tighter as the company scales**.

And let’s talk about the “9% FCF yield” you love so much.

- FY2024 operating cash flow: **−$32.8M**
- FY2024 free cash flow: **−$55.4M**
- Q1 2026 FCF: **$83.0M**, *below* Q1 2025’s **$87.9M**

So the big FY2025 FCF number was flattered by a massive payables build. In the most recent quarter, FCF actually **declined year-over-year**. That isn’t a stable compounding machine — it’s a business whose cash conversion swings violently with working capital.

Yes, DLO has no net debt. Great. That makes it a lower-risk company. But it doesn’t make the current stock price a bargain.

---

## 3. The 13x forward P/E is not a valuation. It’s a hope.

Here’s where the bull case gets dangerous.

DLO is trading at **23.8x trailing earnings**. The **13.0x forward P/E** is based on consensus forward EPS of **$1.13** — an implied **~82% increase** from trailing EPS of $0.62.

But what is the business actually doing right now?

- Q1 EPS: **down 6.7% YoY**
- Q1 operating margin: **down 530bps YoY**
- Q1 net income: **down 10% YoY**

You’re underwriting an 82% EPS acceleration after a quarter where EPS **fell**. That’s not analysis. That’s a leap of faith.

And the EV math isn’t as clean as you pretend:

- Market cap: **~$4.35B**
- Net cash: **~$0.91B**
- Trailing net income: **~$192M**
- EV / trailing net income: **~18x**

If you use delivered earnings, you’re paying roughly **18x EV/earnings** for a business whose margins are compressing and whose latest quarter showed negative earnings growth. That’s not a value stock. That’s a momentum trade wearing a value costume.

You keep banking on “18x forward = $20.” But the stock is only going to re-rate if the $1.13 EPS estimate is credible. And the evidence from the most recent quarter says the opposite.

---

## 4. The technicals are not a “coiled spring.” They’re a stall under resistance.

Let’s look at the actual chart, bull:

- Price: **$14.77**
- 10 EMA: **$14.94** — price is **below**
- VWMA: **$14.83** — price is **below**
- MACD: **+0.38, below its signal line**, with a **negative histogram**
- RSI: **54.14** — neutral, not thrusting
- Resistance: **$15.44–$15.65**, with the Bollinger upper band at **$15.48**
- Support: **$14.10–$14.50**, then **$13.53**, then **$13.23**

The **golden cross** is a lagging signal. It appeared after DLO had already rallied ~35% off the May low. And what has happened since? The stock has gone sideways, failed twice near $15.40–$15.65, and is now below the 10 EMA with a bearish MACD crossover.

Now do the actual risk/reward math:

- Upside to resistance: **$15.65** — about **+6%**
- Downside to the 50 SMA: **$13.53** — about **−8.4%**
- Downside to the 200 SMA: **$13.23** — about **−10.4%**

That is a **negative skew**. You can call it “consolidation” all you want, but a high-volume spike into resistance followed by stalling and low-volume drift is textbook **distribution risk**, not accumulation.

And the “low volume pullback” you think is bullish? It can also mean **there are simply no buyers stepping in**. A stock that surges 13% on one day and then can’t break out on subsequent attempts is not showing strength. It’s showing exhaustion.

---

## 5. Macro is not your friend. It’s a live risk to the business model.

You keep painting a benign macro picture. Let’s look closer:

- **10Y Treasury yield:** **4.63%**, peaked at **4.75%**
- **Fed:** **88% probability of zero cuts in 2026**
- **USD:** Firm dollar — a direct headwind for EM currencies and USD-reported revenue
- **Strait of Hormuz:** Only **12% probability of normalization by Aug 31**; **60% by year-end** — meaning there’s a **40% chance this disruption lingers into 2027**

DLO converts emerging-market currencies into USD. A strong dollar shrinks the USD value of that revenue. A prolonged oil shock raises import costs for the same EM countries DLO depends on. That’s not a “contained tail risk.” That’s a direct hit to the operating theater.

You say FX volatility is a “spread opportunity.” In theory, sure. In practice, FX volatility also means **capital controls, settlement delays, and earnings volatility**. We already saw what that can do: **FY2024 operating cash flow was −$32.8M**. You can’t just hand-wave that away as a one-off when the company’s entire model is exposed to EM financial stress.

And rising yields matter, even for a “net cash” company. DLO is a growth stock trading at 23.8x trailing earnings. When the 10Y is pushing toward 4.75%, the market is going to demand more for that growth. The multiple compresses when yields rise. That’s not a bull case. That’s a headwind.

---

## 6. The sentiment data is not “room to run.” It’s a warning.

You say retail silence means “no froth, no marginal buyer yet.” I say it means **there is no marginal buyer at all.**

The sentiment report that you’re celebrating was:

- **Mildly Bullish: 5.8/10**
- **Low confidence**
- Based almost entirely on **two Zacks articles**
- StockTwits: **unavailable**
- Reddit: **silent**

Even the favorable Zacks pieces **explicitly flag margin risk**. And the earlier Zacks piece on the +12.9% spike said something you keep ignoring: **earnings estimate revisions do NOT support further strength.**

That is the killer line, bull. The stock went up 13% in one day, but the analysts who follow it did not raise their numbers. That means the move was **flow-driven, not fundamental-driven**. Flow-driven rallies can reverse just as fast when the flow rotates elsewhere.

And the insider sale? You call it noise. I call it a **co-founder selling into strength after a 35% rally**. It’s not the end of the world, but it’s certainly not a signal of conviction. Combined with DLO’s history of short-seller scrutiny around governance and related-party concerns, the overhang is still there.

---

## 7. The earnings catalyst cuts both ways — and right now, it’s a downside risk.

You’re already banking on Q2 2026 earnings in mid-August as the re-rating catalyst. But think about what’s priced in:

- Forward EPS of **$1.13** assumes an **~82% jump**
- The stock has **already rallied 35%** off the low
- The last quarter showed **net income down 10%**
- Margins are **still compressing**
- EM FX and oil are **still uncertain**
- Estimates have **not been revised upward**

If Q2 is just “okay” — revenue up 40%, operating margin down, EPS flat — the forward P/E loses its credibility and the stock **de-rates**. You don’t need a miss to hurt DLO. You just need a quarter that confirms margins are still falling.

The bull says “expectations are already depressed.” That’s not true. **Expectations are for $1.13 EPS.** That’s not depressed. That’s heroic.

---

## Bottom Line: This Is Not a Compounder Setup. It’s a Momentum Trade in Deteriorating Fundamentals.

I’m not saying DLO is a bad company. Emerging-markets payments is a real and growing market, and DLO is a legitimate player. But “real business” and “good stock at $14.77” are two completely different questions.

Here’s what the bull is asking you to ignore:

- A quarter with **55% revenue growth and lower net income**
- **530bps operating margin compression**
- **Sequential revenue decline**
- **Trailing P/E of 23.8x** dressed up as a 13x forward bargain
- A technical pattern that is **below the 10 EMA, below VWMA, with a bearish MACD crossover**
- A **negative risk/reward** to first support versus first resistance
- A macro environment of **firm USD, high yields, and unresolved Hormuz risk**
- **No upward estimate revisions** behind a 35% rally
- A sentiment read that is **low confidence** and based on a handful of Zacks articles

A real compounder grows revenue **and** earnings together. DLO grew revenue 55% and delivered **less profit**. That is not a pause. That is deterioration at the operating line.

**Bear verdict: AVOID DLO at $14.77. If you own it, take profits into strength. If you must trade it, demand a close above $15.65 on strong volume *and* a quarter that shows stable margins before you trust this rally again.**

As of 2026-08-06, the downside to **$13.53–$13.23** looks far more probable than the green candle to $20. The bull is fighting the story he wants. I’m reading the numbers in front of us.
Bear Analyst: Bear Analyst — Final Word: You’re Not Buying a Compounder. You’re Buying a Hope-Filled Chart.

Bull, I’ve got to hand it to you: you’ve turned “ignore the quarter in front of us” into an art form. But every time you pivot from the actual earnings power to a golden cross or a forward estimate, you’re admitting what this trade really is — a momentum bet dressed up as value investing. So let’s do this one last time, with the numbers that actually matter for anyone putting capital at risk in **DLO** today.

---

## 1. “A compounder compounds earnings.” DLO’s latest quarter shows the opposite.

You keep telling us to ignore Q1 2026 because of the tax rate. But here’s the problem: **taxes don’t explain operating margin collapsing by 530 basis points.** That’s not a tax artifact. That’s the business itself.

Q1 2026:

- Revenue: **+54.9% YoY**
- Operating income: **+16.0% YoY**
- Pretax income: **+8.9% YoY**
- Operating margin: **16.0% vs. 21.3%** a year ago
- Net income: **−10% YoY**
- EPS: **−6.7% YoY**

Let me translate: DLO added ~$119 million in revenue and kept only ~$4.6 million more pretax profit. That is a **sub-4% incremental margin**. A toll booth with pricing power should convert 30–40% of incremental revenue into profit. This is **operating deleverage**, not “investment for growth.” Investments eventually need to show up in the margin line. They haven’t.

And the full-year 2025 you keep celebrating? Even that was flattered by a **$14.5M gain on sale of security**. Strip it out, and FY2025 net income is still up — fine. But it’s also true that **TTM EPS is $0.62, below FY2025’s $0.65**. Trailing earnings are going *backwards* while the stock has already rallied 35% off the lows. That is not the signature of a compounder at this price.

---

## 2. Net cash? A big chunk of it is merchant float — and you know it.

You’re leaning on $913.6M in cash while ignoring the **$1.156B in payables and accrued liabilities** sitting right across the balance sheet. A payments company holds settlement money that isn’t discretionary. That’s why the **current ratio has deteriorated from 1.65 to 1.33** in one year.

And the cash flow story is not the clean machine you pretend it is:

- FY2024 operating cash flow: **−$32.8M**
- FY2024 free cash flow: **−$55.4M**
- Q1 2026 FCF: **$83.0M** — *below* Q1 2025’s $87.9M

So your “fortress” is partly a working-capital ponzi — payables build flattered FY2025 FCF, and now the latest quarter shows FCF declining YoY. If DLO truly had $911M of free cash, why did they only buy back **$10.1M** in Q1 2026? Because the cash isn’t as free as the bull case pretends.

---

## 3. 13x forward P/E? That’s an *assumption*, not a valuation.

DLO trades at **23.8x trailing earnings**. The 13x forward multiple depends entirely on consensus EPS of **$1.13** — an **~82% jump** from trailing EPS of $0.62.

Here’s the problem: **analysts have not raised estimates after the +12.9% spike.** Zacks explicitly said the move wasn’t supported by estimate revisions. You’re underwriting an 82% earnings acceleration immediately after a quarter where EPS *fell*. That’s not conservative. That’s heroic.

Let’s use actual delivered numbers:

- Market cap: **$4.35B**
- Net cash: **~$0.91B**
- TTM net income: **~$192M**
- EV / trailing net income: **~18x**

That’s not a bargain. That’s a fair-to-rich price for a business whose margins are contracting at the operating line.

---

## 4. The technicals aren’t a coil. They’re a stall under resistance.

You keep pointing to the golden cross, but it’s a **lagging signal** — it appeared after a 35% rally, and since then the stock has gone *nowhere* above $15.65.

The current chart:

- Price **$14.77** is **below the 10 EMA ($14.94)** and **below VWMA ($14.83)**
- MACD is **below its signal line** with a **negative histogram**
- RSI at **54.14** is neutral, not thrusting
- Resistance is stacked at **$15.44–$15.65** with the upper Bollinger band at **$15.48**
- The stock has **failed twice** to close decisively above that zone

Now do the honest risk/reward:

- Upside to resistance: **~+6%**
- Downside to 50 SMA ($13.53): **~−8.4%**
- Downside to 200 SMA ($13.23): **~−10.4%**

That’s a **negative skew** unless you underwrite the $20 fantasy. And “low-volume pullback” cuts both ways — it can simply mean **no one is stepping in to buy**. Distribution often happens quietly after a headline spike. You call it accumulation. I call it a lack of demand at higher prices.

---

## 5. Macro: still not your friend.

- **10Y Treasury at 4.63%, peaked 4.75%** — pressure on growth valuations.
- **88% odds of zero Fed cuts in 2026** — a firm USD regime that directly compresses USD-reported EM revenue.
- **Strait of Hormuz: only 12% odds of normalization by Aug 31, 40% chance disruption persists into 2027.** That’s a real, unresolved tail risk in DLO’s core operating theater.

You say FX volatility is a “spread opportunity.” Fine. But volatility also brings **capital controls, settlement delays, and violent working-capital swings** — we already saw FY2024 OCF go negative. DLO monetizes complexity, yes. But complexity can also blow up your near-term cash conversion.

---

## 6. Sentiment? Quiet retail isn’t an opportunity. It’s an absence of demand.

The sentiment read was **5.8/10, low confidence**, based almost entirely on **two Zacks articles**. StockTwits unavailable. Reddit silent. There is no wave of buyers building here — just a couple of relative-value write-ups.

And the one piece of high-conviction information in the news flow is the one you keep downplaying: **estimates didn’t move after the stock surged.** The rally was flow, not fundamentals. Flow can reverse just as quickly.

The insider sale? You call it rounding error. But a co-founder selling into a 35% run isn’t a vote of confidence. It’s not decisive alone — but combined with the short-seller history and governance overhang, it’s one more reason not to chase.

---

## 7. The earnings catalyst: you’re pricing in perfection.

You say “even okay is good enough at 13x forward.” But “okay” is *not* good enough when the forward number assumes an 82% EPS jump. If Q2 shows revenue up 40% but operating margin down another 200–300 basis points, the **$1.13 forward EPS loses credibility**, and the multiple compresses. You don’t need a miss to get hurt. You just need a “fine” quarter that validates margin deterioration.

You keep saying the downside is cushioned by net cash. But **net cash doesn’t stop a de-rating**. DLO fell from $16.78 to $10.38 with that same net cash on the books. The market will reprice this stock on forward earnings power, not balance-sheet optics.

---

## Bottom Line

I’ll say it clearly: **DLO may be a fine company. But at $14.77, it is not a fine risk/reward.**

The bull case asks you to:

- Ignore an operating margin down **530bps** in the latest quarter
- Ignore net income **down 10%** on revenue up 55%
- Treat settlement float as owner cash
- Pay **23.8x trailing earnings** and call it 13x forward on an estimate that is *not being revised upward*
- And underwrite a $20 re-rating that has no fundamental confirmation

That’s not a compounder setup. That’s a momentum trade with a value-stock costume.

**My recommendation stands: AVOID DLO at $14.77. If you own it, take profits into strength. If you want to be a buyer, wait for a close above $15.65 on strong volume *and* a quarter that shows stable or expanding margins. Until then, the asymmetry favors the downside — toward $13.53, then $13.23.**

The bull is betting on the story he wants. I’m reading the numbers in front of all of us.
Bear Analyst: # Bear Analyst — Final Verdict: You're Paying $14.77 for a Story the Financials Keep Contradicting

Bull, I've listened carefully through every round, and I want to acknowledge something: you build a beautiful narrative. Growth accelerating to 55%. A fortress balance sheet. A golden cross. A $20 target. It all sounds so compelling.

But here's the uncomfortable truth: **every single pillar of your thesis requires the investor to ignore what the latest quarter actually delivered.** And when you strip away the storytelling, the data point to a business whose growth is becoming increasingly expensive to generate and a stock whose risk/reward is skewed to the downside.

Let me walk through it one final time.

---

## 1. The "Compounder" Thesis Dies on the Operating Margin Line

You keep telling us to ignore Q1 2026 because of the tax rate. But here's what the tax rate **doesn't** explain:

| Metric | Q1 2025 | Q1 2026 | Change |
|---|---|---|---|
| Revenue | $216.8M | $335.9M | **+54.9%** |
| Gross margin | 39.2% | 35.3% | **−390bps** |
| Operating margin | 21.3% | 16.0% | **−530bps** |
| Net income | $46.6M | $42.0M | **−10%** |
| Diluted EPS | $0.15 | $0.14 | **−6.7%** |

Let me put that in the simplest terms: **DLO added nearly $120 million in revenue and kept only $4.6 million more in pretax profit.** That's a sub-4% incremental margin. A real "toll booth" with pricing power should convert 30-40% of incremental revenue into profit. This is **operating deleverage**, not "investment for growth."

And the full-year numbers you celebrate? Even they are flattered by a **$14.5M gain on sale of security** in FY2025 and a **$38.6M gain in FY2024**. Strip those out, and the compounding is far less impressive. TTM EPS of $0.62 is **below** FY2025's $0.65. Trailing earnings are going **backwards** while the stock has rallied 35% off the lows.

That's not the signature of a compounder at this price. It's the signature of a growth story where **every additional dollar of revenue is generating less and less profit**.

---

## 2. The "Fortress Balance Sheet" Is Partly Merchant Float

You keep leading with $913.6M in cash and short-term investments. But you keep conveniently skipping the **$1,156.3M in payables and accrued liabilities** sitting right next to it.

That's not discretionary capital. That's merchant settlement money flowing through the platform — recorded as cash on one side and as a liability on the other. It's the **float**, not owner earnings.

Look at the trend:

- Current ratio: **1.65 in Q1 2025 → 1.33 in Q1 2026** — deteriorating
- FY2024 operating cash flow: **−$32.8M** — negative during a growth phase
- Q1 2026 FCF: **$83.0M**, *below* Q1 2025's **$87.9M** — declining year-over-year

Your "9% FCF yield" is flattered by a massive payables build in FY2025. The latest quarter shows FCF going **down**. This is a business whose cash conversion swings violently with working capital — not a stable compounding machine.

And if DLO truly had $911M of free cash, why did they only buy back **$10.1M** in Q1 2026? Because a large chunk of that cash is **not free**. It's earmarked for merchant settlement.

---

## 3. 13x Forward P/E Is an Assumption, Not a Valuation

This is where your thesis gets genuinely dangerous for investors.

- Trailing P/E: **23.8x**
- Forward P/E: **13.0x** — requires EPS of **$1.13**
- Implied EPS growth: **~82%**

But what did the most recent quarter deliver? **EPS down 6.7%.** Operating margin down 530bps. Net income down 10%.

Now, the critical point you keep dancing around: **analysts have NOT raised estimates after the +12.9% spike.** Zacks explicitly said the move was **not supported by estimate revisions**. You're underwriting an 82% earnings acceleration after a quarter where earnings **fell**, with no sell-side analyst willing to back that up with revised numbers.

Let's use delivered numbers instead:

- Market cap: **$4.35B**
- Net cash (even at face value): **$0.91B**
- TTM net income: **$192M**
- **EV / trailing net income: ~18x**

That's not a bargain. That's a **fair-to-rich price** for a business whose margins are contracting at the operating line and whose latest quarter showed profit decline.

---

## 4. The Technicals Say Stall, Not Spring

Let's be honest about the chart one more time:

- Price: **$14.77** — **below the 10 EMA ($14.94)** and **below VWMA ($14.83)**
- MACD: **+0.38 but below signal line**, negative histogram
- RSI: **54.14** — neutral, not thrusting
- Resistance: **$15.44–$15.65** — tested and **rejected twice**
- The golden cross? It's a **lagging indicator** that appeared after a 35% rally — and since then, the stock has gone **sideways**

Now the honest risk/reward:

- Upside to $15.65: **+6%**
- Downside to 50 SMA at $13.53: **−8.4%**
- Downside to 200 SMA at $13.23: **−10.4%**

That is **negative skew**. And the "low-volume pullback" you call constructive? It can also mean **there are simply no buyers stepping in**. A stock that surges 13% on high volume and then fails twice at resistance is showing **exhaustion**, not accumulation.

You want to underwrite a $20 price target with zero estimate revision support? That's not asymmetry. That's hope.

---

## 5. Macro Is Not Your Friend — It's a Live Risk

You call the macro backdrop "constructive." Let's review what's actually happening:

- **10Y Treasury at 4.63%, peaked 4.75%** — real pressure on growth valuations
- **88% probability of zero Fed cuts in 2026** — a firm USD regime that directly compresses USD-reported EM revenue
- **Strait of Hormuz: only 12% odds of normalization by Aug 31, 40% chance disruption persists into 2027** — a live, unresolved tail risk in DLO's core operating theater

You say FX volatility is a "spread opportunity." In theory, sure. In practice, FX volatility means **capital controls, settlement delays, and violent working-capital swings**. We already saw FY2024 OCF go negative. This is not speculation — it's the history of this business.

And rising yields matter even for a "net cash" company. DLO is trading at 23.8x trailing earnings. When the 10Y pushes toward 4.75%, the market demands more for that growth. The multiple compresses. That's not a tailwind — it's a structural headwind for the valuation you're asking investors to accept.

---

## 6. The Sentiment Data Is a Warning, Not an Opportunity

You say "quiet retail means room for inflows." I say **quiet retail means no marginal buyer.**

The sentiment report was **Mildly Bullish at 5.8/10 with LOW confidence**, based almost entirely on **two Zacks articles**. StockTwits was unavailable. Reddit was silent.

Even the positive Zacks pieces **explicitly flag margin risk**. And the Zacks article on the +12.9% spike said something you keep ignoring: **earnings estimate revisions do NOT support further strength.**

And the insider sale? You call it noise. I call it a **co-founder selling into strength after a 35% rally**. It's not decisive alone, but combined with DLO's history of short-seller scrutiny around governance and related-party concerns, it's one more reason not to chase.

---

## 7. The Earnings Catalyst Cuts Both Ways — and the Setup Favors the Downside

You're banking on Q2 2026 earnings in mid-August as the re-rating catalyst. But think about what's already priced in:

- Forward EPS of **$1.13** — an **~82% jump** from trailing EPS
- A **35% rally** off the lows
- No upward estimate revisions
- A quarter that just showed **net income DOWN 10%** and **operating margin DOWN 530bps**

If Q2 delivers revenue growth of 40% but operating margin declines another 200-300bps, the **$1.13 forward EPS loses credibility** and the multiple compresses. You don't need a disaster — you just need a "fine" quarter that confirms margins are still falling.

You say the downside is cushioned by net cash. But **net cash doesn't stop a de-rating**. DLO fell from $16.78 to $10.38 with that same net cash on the books. The market reprices stocks on **forward earnings power**, not balance-sheet optics.

---

## The Bottom Line: This Is a Momentum Trade With a Value Costume

DLO may be a legitimate company in a real and growing market. But "real business" and "good stock at $14.77" are different questions.

Here's what you're asking investors to accept:

| Bull Claim | Reality Check |
|---|---|
| "55% revenue growth" | Net income **down 10%**; operating margin **down 530bps** |
| "$911M net cash fortress" | **$1.156B in payables**; current ratio deteriorating; FCF **declining YoY** |
| "13x forward P/E" | **23.8x trailing**; requires 82% EPS jump with **no estimate revisions** supporting it |
| "Golden cross" | **Lagging signal**; price below 10 EMA and VWMA; MACD bearish crossover; failed twice at resistance |
| "Asymmetric risk/reward" | +6% to resistance vs. −8% to −10% to support — **negative skew** |
| "Macro is supportive" | 10Y at 4.63%, firm USD, Hormuz unresolved, 40% chance of disruption into 2027 |
| "Quiet sentiment is opportunity" | Low-confidence 5.8/10 based on two Zacks articles; no retail demand; no estimate revisions |

The bull is fighting for the story he wants to be true. I'm reading the numbers in front of all of us.

**My recommendation stands: AVOID DLO at $14.77. If you own it, take profits into strength. If you must trade it, demand a close above $15.65 on strong volume AND a quarter that shows stable or expanding margins before you trust this rally again.**

Until then, the safer trade is the downside — toward **$13.53**, then **$13.23**.

The burden of proof is on the bull. And so far, the proof isn't there.
Bear Analyst: # Bear Analyst — Final Rebuttal: DLO Is a Great Business Story, but a Poor Stock at $14.77

Bull, I’ll say this: you’ve reframed the same narrative four times with real polish. But polish isn’t earnings. Every round, you ask investors to ignore the quarterly financials in front of us and instead “trust the trajectory.” I’m not going to do that, and neither should anyone putting actual capital at risk in **DLO**.

Let’s go through your final argument line by line — because the numbers keep telling a different story than the one you’re selling.

---

## 1. You keep calling DLO a compounder. A compounder compounds *earnings* — DLO’s latest quarter did the opposite.

Your favorite move is to dismiss Q1 2026 as a “tax-distorted quarter.” But taxes don’t explain the operating deterioration:

| Metric | Q1 2025 | Q1 2026 | Change |
|---|---|---|---|
| Revenue | $216.8M | $335.9M | **+54.9%** |
| Gross margin | 39.2% | 35.3% | **−390 bps** |
| Operating margin | 21.3% | 16.0% | **−530 bps** |
| Operating income | $46.2M | $53.6M | **+16.0%** |
| Pretax income | $51.9M | $56.5M | **+8.9%** |
| Net income | $46.6M | $42.0M | **−10.0%** |
| Diluted EPS | $0.15 | $0.14 | **−6.7%** |

Do the math: DLO added roughly **$119 million in revenue** and kept only **$4.6 million more pretax profit**. That’s a **sub-4% incremental pretax margin**. A toll booth with pricing power converts 30–40% of incremental revenue into profit. This is not operating leverage — it’s **operating deleverage**.

And your “it’s just investment spending” defense doesn’t hold up either. Investments eventually need to show up in margins. Instead, gross margin has gone from **48.3% in 2022 → 36.8% in 2025 → 35.3% in Q1 2026**. The trend is one-directional, and the latest quarter accelerated it.

Then there’s the full-year flattery. FY2025 net income included a **$14.5M gain on sale of security**. Strip it out, and TTM EPS of **$0.62 is below FY2025’s $0.65**. Trailing earnings are going **backwards** while the stock has already rallied 35% off the lows. That is not the signature of a compounder at this price.

---

## 2. The “$910M fortress” is partly merchant float — and the cash-flow trend is not your friend.

You keep listing cash and short-term investments as if the $1.156B in payables doesn’t exist. But in a payments business, a large chunk of that cash is **merchant settlement money** — it has to be held to settle merchants. It is not discretionary capital for buybacks, dividends, or M&A.

The evidence:

- Current ratio: **1.65 in Q1 2025 → 1.33 in Q1 2026** — deteriorating
- FY2024 operating cash flow: **−$32.8M** — negative during a growth phase
- Q1 2026 FCF: **$83.0M**, *below* Q1 2025’s **$87.9M**
- Buybacks in Q1 2026: just **$10.1M** — if the cash were truly free, why so small?

You say FY2025 FCF of $378.7M proves the model. But that was flattered by a massive payables build. The latest quarter shows FCF **declining year-over-year**. That’s not a stable compounding machine — it’s a business whose cash conversion swings violently with working capital.

And yes, DLO has zero net debt. That makes it a **less risky company**. It does **not** make the stock cheap at $14.77.

---

## 3. 13x forward P/E is not a valuation — it’s an assumption that earnings will nearly double.

Here’s the dangerous part of your thesis, Bull:

- Trailing P/E: **23.8x**
- Forward P/E: **13.0x**, based on consensus EPS of **$1.13**
- Implied EPS growth: **~82%**

What did the latest quarter deliver? **EPS down 6.7%.** Net income down 10%. Operating margin down 530 bps. And the stock surged 13% on July 1 — yet Zacks explicitly said **earnings estimate revisions do NOT support further strength**.

You want investors to underwrite an 82% earnings acceleration after a quarter where earnings *fell*, with **zero upward estimate revisions** behind the rally. That’s not “average execution.” That’s hope.

Let’s use delivered numbers instead:

- Market cap: **$4.35B**
- Net cash (even at face value): **$0.91B**
- TTM net income: **~$192M**
- **EV / trailing net income: ~18x**

That’s not a bargain. That’s a **fair-to-rich price** for a business whose margins are contracting at the operating line. The market is paying for future perfection, and the recent past says perfection isn’t coming.

---

## 4. The technicals don’t say “coiled spring.” They say “stall under resistance.”

You love the golden cross, Bull. It’s a **lagging indicator** — it appeared after a 35% rally, and since then DLO has gone sideways and failed twice at $15.40–$15.65.

Current chart reality:

- Price **$14.77** is **below the 10 EMA ($14.94)** and **below VWMA ($14.83)**
- MACD is **below its signal line** with a **negative histogram**
- RSI at **54.14** is neutral, not thrusting
- Resistance is stacked at **$15.44–$15.65** with the upper Bollinger band at **$15.48**
- The stock has failed **twice** to close decisively above that zone

Now do the honest risk/reward:

- Upside to resistance: **~+6%**
- Downside to the 50 SMA at $13.53: **~−8.4%**
- Downside to the 200 SMA at $13.23: **~−10.4%**

That is **negative skew** unless you underwrite your $20 fantasy. And a “low-volume pullback” cuts both ways — it can simply mean **there are no buyers stepping in**. Distribution often happens quietly after a headline spike. You call it accumulation. I call it a lack of demand at higher prices.

You say the breakout on 11.76M shares confirms the move. But the stock traded **12:1 volume on the way up, and then stalled for a month** — that’s exhaustion, not a launchpad.

---

## 5. Macro is not your friend. It’s a live risk to DLO’s operating theater.

You call the macro backdrop “constructive.” Let’s review what’s actually stressing DLO’s markets:

- **10Y Treasury at 4.63%, peaked 4.75%** — real pressure on growth valuations
- **88% probability of zero Fed cuts in 2026** — a firm USD regime that directly compresses USD-reported EM revenue
- **Strait of Hormuz: only 12% odds of normalization by Aug 31, and a 40% chance the disruption persists into 2027** — a live tail risk in DLO’s core operating region

You say FX volatility is a “spread opportunity.” In theory, yes. In practice, FX volatility brings **capital controls, settlement delays, and violent working-capital swings**. We already saw FY2024 operating cash flow go negative. That’s not speculation — that’s this company’s own history.

And rising yields matter even for a “net cash” company. DLO trades at 23.8x trailing earnings. When the 10Y pushes toward 4.75%, the market demands more for that growth — the multiple compresses. That’s a headwind, not a tailwind.

---

## 6. Quiet retail sentiment isn’t an opportunity — it’s an absence of marginal demand.

The sentiment report you’re celebrating was **Mildly Bullish at 5.8/10 with LOW confidence**, based almost entirely on **two Zacks articles**. StockTwits was unavailable. Reddit was silent.

Even those positive Zacks pieces **explicitly flag margin risk**. And the Zacks article on the +12.9% spike said the move was **not supported by estimate revisions**.

That is the single most important data point in this debate: **the stock went up 13%, and the analysts who cover it did not change their numbers.** That means the rally was flow-driven, not fundamental-driven. Flow-driven moves reverse when the flow rotates elsewhere.

And the insider sale? You call it noise. I call it a **co-founder selling into strength after a 35% run**. It’s not decisive alone — but combined with DLO’s history of short-seller scrutiny around governance and related-party concerns, it’s one more reason not to chase.

---

## 7. The earnings catalyst cuts both ways — and the setup favors the downside.

You say Q2 2026 could be the re-rating catalyst. But think about what’s already priced in:

- Forward EPS of **$1.13** — an ~82% jump from trailing EPS
- A **35% rally** off the lows
- **No upward estimate revisions**
- A quarter that just showed **net income down 10%** and **operating margin down 530 bps**

If Q2 delivers revenue growth of 40% but operating margin declines another 200–300 bps, the **$1.13 forward EPS loses credibility**, and the multiple compresses. You don’t need a disaster — you just need a “fine” quarter that confirms margins are still falling.

You say the downside is cushioned by net cash. But **net cash doesn’t stop a de-rating**. DLO fell from **$16.78 to $10.38** with that same net cash on the books. The market reprices stocks on **forward earnings power**, not balance-sheet optics.

---

## Bottom Line: This Is a Momentum Trade With a Value Costume

DLO may be a legitimate company in a real and growing market. But “real business” and “good stock at $14.77” are two different questions.

Here’s what the bull is asking investors to accept:

| Bull Claim | Reality Check |
|---|---|
| “55% revenue growth” | Net income **down 10%**; operating margin **down 530 bps** |
| “$911M net cash fortress” | **$1.156B in payables**; current ratio deteriorating; FCF **declining YoY** |
| “13x forward P/E” | **23.8x trailing**; requires an 82% EPS jump with **no estimate revisions** |
| “Golden cross” | **Lagging signal**; price below 10 EMA and VWMA; MACD bearish crossover; failed twice at resistance |
| “Asymmetric risk/reward” | +6% to resistance vs. −8% to −10% to support — **negative skew** |
| “Macro is supportive” | 10Y at 4.63%, firm USD, Hormuz unresolved, 40% chance of disruption into 2027 |
| “Quiet sentiment is opportunity” | Low-confidence 5.8/10 based on two Zacks articles; no retail demand; no estimate revisions |

The bull is fighting for the story he wants to be true. I’m reading the numbers in front of all of us.

**My recommendation stands: AVOID DLO at $14.77. If you own it, take profits into strength. If you must trade it, demand a close above $15.65 on strong volume AND a quarter that shows stable or expanding margins before you trust this rally again.**

Until then, the safer direction is toward **$13.53**, then **$13.23**. The burden of proof is on the bull — and so far, the proof isn’t there.

### Manager
**Recommendation**: Overweight

**Rationale**: This was a rigorous, high-quality debate. The bull analyst built the stronger case by anchoring on the multi-year trajectory rather than one tax-distorted quarter — FY2025 delivered +63% net income growth, operating margin expansion of 140bps to 20.3%, and $379M in free cash flow, all while revenue re-accelerated from +14.7% to +46.6% to +54.9% in Q1 2026. The bear's fixation on Q1 2026 operating margin compression (530bps) is partially valid but overplayed: pretax income still grew, the tax-rate spike (10.1% → 25.8%) was the primary driver of the net income decline, and investment in new geographies explains much of the margin give-back. The valuation is genuinely supportive: 13x forward earnings, ~10x EV/forward earnings after stripping net cash, and a ~9% TTM FCF yield for a business with 35% ROE. The technical picture — golden cross, price above rising 50/200 SMAs, and a 12:1 volume ratio favoring the breakout over the pullback — reinforces the fundamental setup.

However, the bear scored legitimate points that keep this from a full Buy conviction. First, the 13x forward P/E depends on $1.13 in forward EPS — an ~82% jump from trailing — and the Zacks article explicitly noted that estimate revisions did not confirm the price surge. Second, the margin compression trend (gross margin from 48.3% in 2022 to 35.3% in Q1 2026) cannot be entirely dismissed as "healthy mix"; it warrants monitoring. Third, the macro backdrop of firm USD, elevated 10Y yields, and unresolved Hormuz risk creates genuine uncertainty for EM-exposed earnings. Fourth, the stock has failed twice to clear $15.44–$15.65 resistance, and the upcoming Q2 earnings print in mid-August is a binary event that cuts both ways.

The bull wins the debate on balance — DLO is a quality compounder at a reasonable price, and the asymmetry favors the upside over a 6–12 month horizon. But the bear's margin-compression and estimate-revision concerns temper the conviction enough to recommend building exposure gradually rather than going all-in ahead of the Q2 print.

**Strategic Actions**: 1. **Initiate or add to DLO with half of the intended full position size at current levels (~$14.77).** The 13x forward multiple, $910M net cash cushion, and golden cross provide a favorable entry.

2. **Set a near-term stop at $13.90 (just below the $14.10–$14.50 support zone).** A close below this level would break the post-golden-cross consolidation and target the 50-day SMA at $13.53 — invalidating the near-term bullish thesis.

3. **Reserve the remaining half of the position for one of two triggers:**
   - A confirmed breakout above $15.65 on strong volume (≥8M shares), which opens the path to $20+ at 18x forward earnings.
   - A Q2 2026 earnings print (expected mid-August) that delivers 40%+ revenue growth with stable or improving operating margins. If margins compress another 200+ bps, hold the half-position and reassess.

4. **Position sizing guidance:** Given the Overweight rating, target ~1.5–2x the portfolio's benchmark weight for DLO, but scale in across the two tranches. The net-cash balance sheet (~$3.10/share) and 9% FCF yield provide a margin of safety that justifies above-benchmark exposure for patient capital.

5. **Monitor key risk triggers for downgrade to Hold:**
   - A second consecutive quarter of 400+ bps operating margin compression (signals the moat is weakening, not just investment spend).
   - A breakdown in EM FX or a Hormuz-driven oil spike that materially disrupts DLO's core markets.
   - Forward EPS estimate cuts below $0.95 (would push forward P/E above 15.5x and reduce the valuation case).

6. **Take partial profits (⅓ of position) if the stock reaches $18–$20 on the Q2 catalyst**, letting the remaining position ride as the compounding story plays out over the next 2–3 years.

## V. Portfolio Manager Decision

Overweight