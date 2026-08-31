# TradingAgents Investment Report

**Ticker:** RELY
**Date:** 2026-08-12
**Depth:** Deep (5 rounds)

## I. Analyst Team Reports

### Market
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

### Sentiment
**Overall Sentiment:** **Bullish** (Score: 7.5/10)
**Confidence:** Medium

# RELY (Remitly Global, Inc.) — Sentiment Report
**Period:** 2026-08-05 to 2026-08-12 · **Analysis date:** 2026-08-12 · **Ticker:** RELY (NasdaqGS)

## 1. Source-by-source breakdown

### News headlines (Yahoo Finance) — Strongly Bullish
The news tape over the past 7 days is dominated by a single catalyst: a **record Q2 2026 earnings beat** reported on Aug 5–6, and the associated product/news flow that followed. Key facts reported across multiple outlets (MarketBeat, Zacks, StockStory, Simply Wall St., Motley Fool):

- Revenue of **$495.16M, +20.2% YoY**, beating consensus (+2.19% surprise) with a **GAAP EPS of $0.93–$0.98** — a **+268.97% earnings surprise** (Zacks). StockStory notes GAAP profit came in "significantly above" analyst estimates.
- **Record adjusted EBITDA of $115M (23% margin)** — the "scaling up and expanding margins" narrative drove an 8% pop on Aug 6 ("Why Remitly Global Stock Popped 8% Today").
- **10 million active customers** milestone (10x growth since 2019) flagged repeatedly.
- **Raised FY2026 revenue guidance** to $1.978–$1.988B, with Q3 guidance (~$506M) close to analyst estimates.
- **Product catalyst: the Remitly Global Card launch** — a multi-currency card allowing hold/spend/save/borrow/send, positioned as expansion beyond core remittances into higher-value transfers, small-business flows, recipients, and an AI push (MarketBeat, Simply Wall St.).
- **Barron's published an outright bullish stock call**: "This Stock Can Rally 35% as It Disrupts Global Remittance Markets," citing the $900B+ global remittance market and RELY's ~$5B market cap.
- Two articles framed insider sales as **benign and informational**, not bearish: a director exercised fully vested pre-IPO options at $0.64/share and retains 261,094 shares + 169,818 options, plus a separate director retains a $45.96M position.
- Counterweight: Simply Wall St. published a cautionary piece ("Trading At A Premium After Record Q2?") noting the stock is up **84.7% YTD** and screens as "not an obvious bargain," i.e., much good news may be priced in.

Net news tone: clearly bullish on fundamentals and growth catalysts, with a minority valuation-caution thread and benign insider-sale coverage.

### StockTwits — Bullish (small sample, zero bears)
30 most-recent cashtag messages: **16 Bullish (53%) vs 0 Bearish (0%)**, 14 unlabeled. A 53/0 split with zero explicit bearish labels is a strongly one-sided retail read, though the sample is small and the bulk of activity clusters around the earnings print (Aug 5–7).

Supporting posts: @ENG5757 ("such low p/e lower than s&p… I see 70% in the next 3 month"), @HedgeHog_1 ("up 88% in 6 months… potential to go up another 30-40%"), @eganon69 (large cup-and-handle breakout targets >$27.35), @JFDI ("big ol base… we goin' stage 2?"), @fundamentalCo ("I want more!!!"), @Existentialtrader ("another great quarter"), @MarketPulsee (RELY hitting new 52-week highs Aug 6).

Notable nuance from unlabeled messages: @applehead93 is hesitant ("triple top break out? Not sure if I want to take the risk at these levels"), @NovaNoble is skeptical of valuation ("needs to show me, not tell me"), and @BlazarBeta sees the 10M-customer milestone as growth "that is real" but adds "now they need to prove they can monetize it." So the retail crowd is overwhelmingly constructive but with an audible fear-of-chasing streak.

### Reddit — Silent (data gap)
- r/wallstreetbets: 1 post in the window, but it is an **unrelated MSFT→META rotation thesis** that only incidentally surfaced in the RELY feed — no RELY-specific sentiment content.
- r/stocks: **no posts** mentioning RELY in the past 7 days.
- r/investing: **no posts** mentioning RELY in the past 7 days.

Community discussion is effectively absent. This is a genuine data limitation, not a bearish signal, but it means the "crowd exuberance" leg of sentiment (which is often a top signal on WSB) is unavailable for RELY this week.

## 2. Cross-source divergences and alignments

**Alignments:** All live sources point the same direction. News is bullish (earnings beat, guidance raise, product launch, Barron's 35% upside call); StockTwits is bullish (53% labeled bullish, 0% bearish, new 52-week highs). There is no major bearish institutional headline in the window, and the closest thing — insider sales — was explicitly framed by Motley Fool as discretionary/pre-IPO option exercises by a director who retains a large position.

**Divergences (mild, not directional):**
1. *Valuation caution:* Simply Wall St.'s "trading at a premium" piece and StockTwits users questioning the risk of chasing ("triple top", "needs to show me") temper the euphoria. This is a speed-bump caveat, not a bearish thesis.
2. *Reddit silence vs. StockTwits activity:* the absence of Reddit discussion while StockTwits buzzes suggests enthusiasm is concentrated in technically-oriented retail traders rather than a broad retail mania — historically a slightly more sustainable setup than a WSB-style frenzy.
3. *Monetization skepticism:* @BlazarBeta's "growth is real, now prove you can monetize it" echoes the fundamental question behind the premium-valuation headlines, but no source argues the business is deteriorating.

## 3. Dominant narrative themes

1. **"Q2 was a blowout and guidance is up"** — the single dominant narrative across every news outlet and most StockTwits posts (record revenue, EPS surprise, record EBITDA margin, raised FY26 outlook).
2. **"Scaling beyond remittances"** — the Global Card launch, higher-value transfers, small-business/recipient expansion, and AI push are framed as a TAM expansion that justifies a premium multiple.
3. **"10 million active customers"** — repeated as a milestone proving the platform's scale (10x since 2019).
4. **"The innovator's dilemma vs. Western Union"** — Motley Fool and Barron's both frame RELY as the disrupter taking share from legacy remittance players (WU's 13.5% dividend yield cited as a value trap).
5. **"Stock has run a lot — is it too late?"** — the cautionary counter-theme (84.7% YTD gain, premium valuation screens, 45% below all-time highs, retail hesitation at current levels, profit-taking after the 88% six-month run).

## 4. Catalysts and risks

**Catalysts (emerging from the data):**
- Q2 beat + **raised FY2026 revenue guidance** ($1.978–$1.988B) — the foundational positive.
- **Remitly Global Card** multi-currency product rollout to additional markets — a potential second growth leg beyond remittance.
- **10M active customers** milestone supporting a long-duration growth narrative.
- **Barron's 35% upside call** — institutional media endorsement that can draw in new buyers.
- Momentum signals: new 52-week highs, "stage 2" technical breakout commentary, cup-and-handle targets (>$27.35) from retail chartists.

**Risks (emerging from the data):**
- **Valuation/premium risk:** stock +84.7% YTD and screening expensive per Simply Wall St.; Q3 guidance is only "close to" (not above) estimates, so the next earnings bar is high.
- **Insider sales:** a director halved his direct holdings via a $0.64 pre-IPO option exercise; while framed benignly, it is a headline that can spook momentum traders.
- **Chasing/froth risk:** multiple retail posts flag a possible triple top and hesitation to add at current levels; profit-taking after an 88% six-month run was already observed on Aug 7.
- **Monetization execution risk:** the bull case rests on converting the 10M-user base into higher-value products (card, lending, small business); if adoption disappoints, the premium multiple is vulnerable.
- **Data gap:** zero Reddit engagement means no read on broader retail "hype" sentiment — the enthusiasm may be narrower than it looks.

## 5. Key sentiment signals summary

| Signal | Direction | Source | Supporting evidence |
|---|---|---|---|
| Q2 earnings beat + raised guidance | Bullish | News (MarketBeat, Zacks, StockStory, Motley Fool) | Revenue $495.16M (+20.2% YoY), GAAP EPS $0.93–$0.98, EPS surprise +268.97%, FY26 guide raised to ~$1.98B, record adj. EBITDA $115M (23% margin) |
| Product expansion (Global Card, AI, SMB) | Bullish | News (MarketBeat, Simply Wall St.) | Multi-currency card with spend/save/borrow/send; "expansion beyond traditional remittance" |
| Institutional/sell-side endorsement | Bullish | News (Barron's) | "This Stock Can Rally 35%" — $900B remittance market, $5B market cap |
| Retail sentiment breadth | Bullish | StockTwits | 16 Bullish (53%) vs 0 Bearish (0%) of 30 messages; breakout/52-week-high chatter |
| Insider selling (pre-IPO options exercise) | Mildly Bearish (contained) | News (Motley Fool) | Director halved direct holdings at $0.64 strike; retains 261,094 shares + 169,818 options; $45.96M position remains |
| Valuation premium concern | Cautionary / Neutral | News (Simply Wall St.), StockTwits (@NovaNoble, @applehead93) | +84.7% YTD; "not an obvious bargain"; "triple top… risk at these levels" |
| Community/Reddit engagement | Neutral / data gap | Reddit (r/WSB, r/stocks, r/investing) | No RELY-relevant posts; only WSB post is an unrelated MSFT→META rotation |

## Conclusion

Sentiment for RELY across the Aug 5–12 window is **Bullish**: the news flow is uniformly positive around a strong Q2 beat, raised guidance, a new product catalyst, and a high-profile bullish call from Barron's, while StockTwits shows a one-sided bullish retail skew (53% labeled bullish, 0% bearish, new 52-week highs). The main counterweights are valuation-premium commentary, benign-but-notable insider sales, and retail hesitation about chasing — plus a complete absence of Reddit discussion, which limits how broadly we can claim the enthusiasm extends. **Overall band: Bullish · Score: 7.5/10 · Confidence: medium** (news and StockTwits are substantive, but Reddit returned no RELY-specific data). This is a sentiment read for the trader to weigh alongside fundamentals and technicals — not a price call.

### News
I now have comprehensive data across company news, macro indicators, global headlines, and prediction markets. Let me compile the full research report.

---

# News & Macro Research Report — RELY (Remitly Global, Inc.)
**Analysis Date:** 2026-08-12 | **Exchange:** NMS (NASDAQ: RELY) | **Sector:** Technology / Software – Infrastructure (Digital Cross-Border Payments)

---

## 1. Executive Summary

RELY is in the middle of a powerful fundamental re-rating week. On **Aug 5–6**, the company reported **record Q2 2026 results** (revenue +20% YoY, record adjusted EBITDA, GAAP profitability, 10M+ active users), raised FY2026 guidance, and launched the **Remitly Global Card** — a strategic pivot from pure remittance toward a multi-currency global banking/neobank product. The stock reacted with an ~8% single-day pop and is up **~85% YTD**, though it still sits ~45% below its all-time highs, and valuation screens as rich ("not an obvious bargain").

The macro backdrop is broadly supportive but carries one live tail-risk: **U.S. rates are high-for-longer (86% market-implied odds of zero Fed cuts in 2026), the dollar is stable, labor markets are firm (unemployment 4.1% and falling), and inflation is cooling.** The principal macro risk is **geopolitical (Iran/Hormuz/oil)**, which is actively repricing (US-invasion odds 18%, Hormuz normalization odds collapsing), and oil-price pressure could dent remittance senders' disposable income and raise costs in receiving corridors.

**Net read:** Fundamentals and catalysts are strongly positive; the main friction points are valuation (post-runup premium), insider option-sale overhang, and macro/geopolitical volatility that could hit a high-beta growth name.

---

## 2. Company-Specific News & Catalysts (RELY)

### A. Record Q2 2026 Earnings (reported Aug 5, 2026) — Primary Catalyst
- **Revenue:** $495.16M, **+20.2% YoY**, above guidance and ~2.2% above consensus (Zacks: +2.19% revenue surprise).
- **Profitability inflection:** Net income $205.91M; **GAAP EPS $0.93** vs. consensus — a **+268.97% earnings surprise** (Zacks). Adjusted EBITDA hit a **record $115M at a 23% margin** (MarketBeat).
- **Scale milestone:** Surpassed **10 million active customers** (CEO Sebastian Gunningham).
- **Guidance:** Raised full-year 2026 revenue outlook; Q3 2026 guide of ~$506M is close to analyst estimates (StockStory).
- **Reaction:** Stock popped ~8% on Aug 6; follow-through coverage cites "scaling up and expanding margins" (Motley Fool) and +7.2% post-earnings move (Simply Wall St.).

### B. Remitly Global Card Launch — Strategic Re-rating Driver
- Launched the **Remitly Global Card**: multi-currency balances, global no-fee spending, instant cardholder-to-cardholder transfers, integrated credit, and save/borrow features — a "global banking" product beyond core remittance (Simply Wall St.).
- Executives confirmed growth strategy: **core remittance market-share gains + new revenue streams** from higher-value transfers, small businesses, recipients, and the card + AI push (MarketBeat, Aug 10).
- This expands TAM beyond the >$900B/yr global remittance market (World Bank via Barron's) into consumer banking — a potential multiple re-rating driver if execution follows.

### C. Sell-Side & Sentiment
- **Barron's bullish feature (Aug):** Stock can rally **35%**; framed as a disrupter in a >$900B market with ~$5B market cap (Barron's via Yahoo).
- **Motley Fool (Aug 12):** Argues RELY is the better buy vs. competitor Western Union (WU), whose 13.5% dividend yield signals distress ("innovator's dilemma").
- **Valuation caution:** Simply Wall St. flags RELY as **relatively expensive** after the 84.7% YTD run — "not an obvious bargain."

### D. Insider Activity — Minor Negative Sentiment Flag
- A director **cashed in pre-IPO options** (exercise price $0.64/share), reducing direct holdings by half but retaining 261,094 shares + 169,818 options; another director's discretionary sale leaves a **$45.96M position** intact (Motley Fool, Aug 12).
- These are **option-exercise-driven sales at low cost basis**, common post-earnings; not a fundamental red flag, but worth flagging for near-term sentiment/overhang.

---

## 3. Macroeconomic Environment (FRED data, as of 2026-08-12)

### Rates — High-for-Longer Regime
- **Fed Funds Effective Rate: 3.63%** — unchanged across May–July 2026. The FOMC meeting in late July caused "Fed Day turmoil" in markets (Barron's), consistent with a hawkish hold.
- **10Y Treasury: 4.70%** (Aug 11), **+23bps over 90 days** (from 4.47%). Rising long-end yields signal term-premium/sticky-growth concerns.
- **Yield curve (10Y–2Y): +0.48** and steepening (from ~0.27 in mid-June) — positive, no inversion recession signal.
- **Implication for RELY:** Elevated funding costs for payments infrastructure, but Remitly is now GAAP-profitable with record EBITDA, reducing balance-sheet sensitivity; high rates also underpin USD strength, which supports the USD-sender FX margin model.

### Inflation — Cooling/Contained
- **CPI:** 332.81 (July 2026), **-0.35% over the window** (May→July); latest reading "met expectations" (WSJ: Treasury yields slipped after inflation matched forecasts).
- **Core PCE:** +0.13% over the window — benign.
- **Implication:** Stable purchasing power for U.S.-based remittance senders (immigrant labor force); lower inflation reduces pressure on household budgets that fund remittances.

### Labor Market — Firm (Remittance Demand Driver)
- **Unemployment: 4.1%** (July), **down from 4.3% in May** — improving employment is a direct tailwind for remittance send volumes from the U.S.

### Dollar — Stable, Slightly Soft
- **Broad dollar index: ~119.06** (Aug 7), +0.3% over 90 days but drifting lower in early August (from ~120.8 late July to 119.1).
- **Implication:** A stable-to-slightly-soft USD modestly supports recipient-side purchasing power in corridors (MXN, PHP, etc.); no FX shock affecting corridor economics.

### Market Volatility — Calm
- **VIX: 15.28** (Aug 11), down ~11% over the month; global equity markets grinding higher (TSX record high; Nasdaq charging on inflation data). Low vol favors continuation of the growth-stock rally.

### Energy/Geopolitics — The Live Risk
- **Oil prices climbing again** (Reuters); global headlines centered on supply-side stress (Codelco lower copper output, Vale projects).
- **Prediction markets (Polymarket):** US invasion of Iran before 2027 at **18% (+2pp WoW)**; Strait of Hormuz traffic back to normal by Aug 31 only **3% (-11.7pp)**; by Dec 31 only **46% (-15pp)**. This implies an **active, unresolved Hormuz disruption**.
- **Implication for RELY:** Rising oil/Hormuz risk could (1) raise fuel/food prices in receiving countries, pressuring recipient-side demand; (2) increase sending-side cost of living for migrants; (3) trigger risk-off vol that would hit a high-beta, 85%-YTD growth name harder than the index.

---

## 4. Forward-Looking Signals (Prediction Markets)

| Market | Implied Probability | Read |
|---|---|---|
| **No Fed rate cuts in 2026** | **86%** (-2pp WoW) | Market firmly prices zero easing; high-for-longer is the base case |
| **US recession by end of 2026** | **8%** (-1pp) | Low recession risk → remittance demand holds up |
| **US invasion of Iran before 2027** | **18%** (+2pp) | Geopolitical risk rising; watch for risk-off spikes |
| **Hormuz traffic normal by Aug 31** | **3%** (-11.7pp) | Active disruption; oil bid → cost pressure in receiving corridors |
| **Bitcoin ≥ $67.5K in Aug** | 36% (-21pp) | Crypto weak — minor negative for crypto-adjacent remittance rails, immaterial overall |

---

## 5. Risks & Watch Items

1. **Valuation/momentum risk:** +84.7% YTD; post-earnings pop may have front-run the good news; Simply Wall St. screens it as expensive.
2. **Insider sales:** Two director sale/exercise filings in the same week (though positions remain substantial) — monitor Form 4 flow.
3. **Geopolitical escalation (Iran/Hormuz/oil):** The single largest macro threat; would pressure margins via corridor economics and trigger growth-stock de-risking.
4. **High-for-longer rates:** 4.70% 10Y and no-cut pricing raise discount rates for long-duration growth equities — a valuation headwind offset by improving fundamentals.
5. **Competitive landscape:** WU/other incumbents are struggling (13.5% dividend yield), which is an opportunity, but also signals a deflationary fee war; card rollout execution risk across new markets.
6. **Q3 guide (~$506M) is "close to estimates"** — bar is set; further upside needs beat-and-raise cadence to continue.

---

## 6. Actionable Insights for Traders

- **Event-driven posture: BULLISH on fundamentals.** Record Q2, raised guidance, 10M users, Global Card TAM expansion, improving labor market, cooling inflation, and a Barron's +35% upside call combine for a strong news tape.
- **Momentum traders:** The post-earnings move (+8% day; +7.2% follow-through) with a calm VIX (~15) and low recession odds (8%) favors continuation, but 85% YTD gains mean buying here is chasing — wait for pullbacks toward the post-earnings gap or use options to define risk.
- **Event risk to hedge:** Hormuz/Iran (18% invasion odds, rising) is the classic catalyst that could gap a high-beta fintech lower; consider downside protection or sizing down into any oil-spike headlines.
- **Watch items this week:** Further Form 4 filings, Global Card market-rollout announcements, any corridor-specific FX moves (MXN/PHP/NGN), and the Aug CPI follow-through commentary.
- **Framework:** Fundamentals = Buy-grade; Valuation = stretched; Macro = supportive-with-tail-risk. Net news flow is decisively positive, with the main bear case being "good news is priced."

---

## 7. Key Points Summary Table

| Category | Data Point | Detail | Signal for RELY |
|---|---|---|---|
| **Earnings** | Q2 2026 revenue | $495.2M, +20.2% YoY, above guidance | ✅ Positive |
| **Earnings** | GAAP EPS | $0.93 vs. consensus; +269% EPS surprise | ✅ Strong positive |
| **Earnings** | Adjusted EBITDA | Record $115M, 23% margin | ✅ Positive |
| **Guidance** | FY26 + Q3 (~$506M) | Raised FY guide; Q3 in line | ✅ Positive |
| **User growth** | Active customers | Surpassed 10M | ✅ Positive |
| **Product** | Remitly Global Card | Multi-currency banking launch; TAM expansion | ✅ Re-rating catalyst |
| **Analyst tone** | Barron's / MF | 35% upside call; RELY > WU | ✅ Positive |
| **Valuation** | YTD +84.7%; ~45% below highs | Screens "not an obvious bargain" | ⚠️ Stretched |
| **Insider** | Director sales/option exercises | $45.96M position retained; $0.64 cost-basis sales | ⚠️ Mild overhang |
| **Rates** | Fed funds 3.63%; 10Y 4.70% | No cuts priced (86% zero-cut odds); high-for-longer | ⚠️ Valuation headwind |
| **Inflation** | CPI -0.35% (3-mo); core PCE benign | Cooling, met expectations | ✅ Supportive |
| **Labor** | Unemployment 4.1% (down from 4.3%) | Firm U.S. employment = remittance senders' income | ✅ Positive |
| **Dollar** | Broad DXY ~119, flat-to-soft | Stable FX; no corridor shock | ✅ Neutral-positive |
| **Volatility** | VIX 15.28, down 11% MoM | Calm tape supports growth rally | ✅ Positive |
| **Recession odds** | 8% US recession by end-2026 (-1pp) | Low downturn risk | ✅ Positive |
| **Geopolitics** | Iran 18% (+2pp); Hormuz normal by Dec only 46% | Live oil/shipping disruption, rising | ❌ Key tail risk |
| **Crypto** | BTC weak (36% chance ≥$67.5K, -21pp) | Immaterial to core model | ➖ Neutral |

---

**Bottom line for the workflow:** The news tape for RELY is among the strongest in the fintech space this week — record Q2, raised guidance, 10M users, and a genuine product re-rating catalyst (Global Card), all set against a macro environment of firm labor, cooling inflation, low recession odds, and calm volatility. The offsetting factors are valuation after an 85% YTD run, insider-sale optics, and a live Iran/Hormuz geopolitical tail-risk. This is a **fundamentally bullish news setup with execution/valuation risk** — a stance that leans toward **BUY on pullbacks / HOLD at current stretched levels**, with geopolitical headlines the key catalyst to monitor.

*(Note: This is the news-research input; final BUY/HOLD/SELL decision rests with the workflow's recommendation stage.)*

### Fundamentals
I now have comprehensive data across all financial statements (quarterly and annual). Let me compile the full analysis.

---

# Fundamental Analysis Report: RELY (Remitly Global, Inc.)

**Analysis Date:** 2026-08-12 | **Exchange:** NMS (Nasdaq) | **Sector:** Technology | **Industry:** Software – Infrastructure
**Ticker:** RELY | **Data retrieved:** 2026-08-12

---

## 1. Executive Summary

Remitly Global, Inc. (RELY) is a digital financial services / cross-border money transfer platform that has completed a dramatic financial transformation. The company:
- Delivered **first-ever full-year GAAP profitability in FY2025** (Net Income +$67.9M vs. −$37.0M in 2024).
- Grew revenue ~29–34% annually for three consecutive years, reaching **$1.81B TTM revenue**.
- Generated **$406.1M TTM operating cash flow** and **$375.1M TTM free cash flow** (quarterly sum), with a cash-rich balance sheet ($676.4M cash, only $38.3M debt).
- Reported a blockbuster **Q2 2026 (June 2026) quarter** with EPS of $0.93 — **boosted by a ~$141M one-time tax benefit** (valuation allowance release); pre-tax income was $64.6M.
- Trades at ~$24.26 (implied from market cap of $5.10B), **PE (TTM) 17.4x**, **Forward PE 15.0x**, with a beta of just 0.34.

**Bottom line:** RELY is a high-growth, newly profitable fintech with a fortress balance sheet, expanding margins, and shareholder-friendly capital allocation (buybacks initiated). The main caveat for traders is that TTM earnings are inflated by a one-time tax item — underlying quality of earnings should be assessed on pre-tax operating results.

---

## 2. Company Profile & Business Overview

- **Company:** Remitly Global, Inc.
- **Business:** Digital cross-border remittances and money transfer services (consumer fintech; classified under Technology / Software – Infrastructure).
- **Model:** Transaction-based fees on international money transfers; serves immigrant and diaspora customers globally; competes with Wise, Western Union, MoneyGram, and PayPal/Xoom.
- **Share count:** ~210.3M ordinary shares issued (Q2 2026); diluted share count ~221.0M.
- **Market Cap:** $5.10B | **Implied share price:** ~$24.26

**Price action context:**
| Metric | Value |
|---|---|
| 52-Week High | $27.15 |
| 52-Week Low | $12.08 |
| 50-Day Average | $22.28 |
| 200-Day Average | $17.70 |
| Beta | 0.343 (low volatility) |

The stock is trading ~43% above its 200-day average and near the upper end of its 52-week range — a strong uptrend with notably low volatility (beta 0.34).

---

## 3. Income Statement Analysis (Profitability Transformation)

### Revenue trajectory (annual)
| Year | Revenue ($M) | YoY Growth |
|---|---|---|
| 2022 | 653.6 | — |
| 2023 | 944.3 | +44.5% |
| 2024 | 1,264.0 | +33.9% |
| 2025 | 1,635.1 | +29.4% |
| **TTM (Jun-2026)** | **1,809.6** | **+~20% YoY (quarterly)** |

### Quarterly momentum (accelerating)
| Quarter | Revenue ($M) | Gross Profit ($M) | GM% | Operating Income ($M) | Net Income ($M) | Diluted EPS |
|---|---|---|---|---|---|---|
| Q2 2025 | 411.9 | 243.0 | 59.0% | 14.6 | 6.5 | $0.03 |
| Q3 2025 | 419.5 | 246.4 | 58.7% | 11.8 | 8.8 | $0.04 |
| Q4 2025 | 442.2 | 277.4 | 62.7% | 38.8 | 41.2 | $0.19 |
| Q1 2026 | 452.8 | 281.1 | 62.1% | 53.7 | 49.1 | $0.23 |
| **Q2 2026** | **495.2** | **307.3** | **62.1%** | **66.7** | **205.9** | **$0.93** |

**Key observations:**
- **Q2 2026 revenue grew +20.2% YoY** ($495.2M vs. $411.9M), with gross profit up +26.5% YoY.
- **Gross margin expanded** from ~59.0% (Q2 2025) to **62.1%** (Q2 2026), and from 50.0% (FY2022) to **61.5% TTM** — a consistent structural improvement.
- **Operating leverage is powerful:** Operating income rose from $14.6M (Q2 2025) to **$66.7M (Q2 2026)**, a 4.6x increase on ~20% revenue growth.
- **⚠️ Important quality-of-earnings note:** Q2 2026 net income of $205.9M includes a **−$141.3M tax provision (a one-time tax benefit)**, flipping a $64.6M pre-tax profit into a $205.9M reported profit. Diluted EPS of $0.93 is thus *not* recurring; underlying quarterly run-rate earnings power is closer to $0.25–0.30/share pre-tax.

### Profitability ratios (TTM)
| Metric | TTM |
|---|---|
| Revenue | $1,809.6M |
| Gross Profit | $1,113.8M (61.5% GM) |
| EBITDA | $199.2M–$229.3M (data vendor range) |
| Net Income | $305.0M (incl. one-time tax benefit) |
| Profit Margin | 16.9% |
| Operating Margin | 14.3% |
| EPS (TTM) | $1.39 |
| Forward EPS | $1.62 |
| ROE | 32.2% |
| ROA | 8.5% |

---

## 4. Balance Sheet Analysis (Fortress Position)

| Item ($M) | Jun-2026 | Mar-2026 | Dec-2025 | Sep-2025 | Jun-2025 | Dec-2024 |
|---|---|---|---|---|---|---|
| **Total Assets** | 1,567.5 | 1,385.8 | 1,458.7 | 1,213.7 | 1,166.2 | 1,012.9 |
| **Cash & Equivalents** | 676.4 | 649.1 | 542.4 | 476.9 | 515.9 | 368.1 |
| **Total Debt** | 38.3 | 39.3 | 192.1 | 35.5 | 32.4 | 16.3 |
| **Stockholders' Equity** | 1,126.8 | 907.4 | 868.8 | 797.2 | 764.9 | 665.5 |
| **Tangible Book Value** | 1,070.8 | 850.9 | 811.7 | 738.0 | 703.7 | 600.1 |
| **Working Capital** | 881.6 | 808.3 | 916.9 | 705.4 | 673.3 | 568.5 |

**Key observations:**
- **Cash position strengthened to $676.4M** — up 84% from Dec-2024 ($368.1M) — while total debt is a minimal $38.3M (mostly capital leases).
- **Debt management:** The company took on a $155M term loan in Q4 2025 (Total Debt spiked to $192.1M) and **repaid it in Q1 2026** (cash flow shows −$155M net short-term debt issuance). This appears to be temporary funding for seasonal working-capital needs, not a structural leverage increase.
- **Equity book value** grew 69% in 18 months ($665.5M → $1,126.8M), driven by retained earnings improvement and option exercises.
- **Retained earnings improved** from −$528.3M (Dec-2024) to **−$205.4M (Jun-2026)** — the accumulated deficit is being rapidly erased.
- **Current Ratio: 3.18x; Debt-to-Equity: 3.40** (vendor-calculated; note the D/E figure reflects the grossed-up customer-funding liabilities typical of remittance platforms — actual interest-bearing debt is minimal at ~$38M).
- Large swings in **Prepaid Assets** ($458.6M at Dec-2025 → $255.9M at Jun-2026) and **Other Current Liabilities** are characteristic of the remittance/customer-funds float and are **not** a sign of financial distress.

---

## 5. Cash Flow Analysis (Self-Funding Growth Engine)

| Metric ($M) | Q2 2026 | Q1 2026 | Q4 2025 | Q3 2025 | FY2025 | FY2024 |
|---|---|---|---|---|---|---|
| **Operating Cash Flow** | 134.6 | 81.9 | 149.6 | 40.0 | 325.1 | 111.6 |
| **Capital Expenditure** | (4.5) | (9.2) | (9.4) | (7.9) | (41.8) | (17.7) |
| **Free Cash Flow** | 130.1 | 72.7 | 140.2 | 32.1 | 283.3 | 93.9 |
| **Stock-Based Compensation** | 34.5 | 27.5 | 41.3 | 40.0 | 155.1 | 152.1 |
| **Share Repurchases** | (22.7) | (42.5) | (12.0) | (11.9) | (23.9) | 0 |

**Key observations:**
- **TTM operating cash flow ≈ $406.1M; TTM FCF ≈ $375.1M** — the company is now a serious cash generator (FCF margin ~20.7% of revenue TTM).
- **FY2025 FCF of $283.3M** was **3x** FY2024's $93.9M; FY2023 was only $57.7M; FY2022 was −$115.7M. The inflection is dramatic and durable.
- **Capex is light** (~$31M TTM, ~1.7% of revenue) — the platform is asset-light software infrastructure.
- **Shareholder returns:** RELY initiated **share repurchases in H2 2025** and has now bought back **~$65.2M in H1 2026** (Q1: $42.5M; Q2: $22.7M) plus ~$23.9M in H2 2025.
- **SBC remains meaningful** (~$155M annually, ~9.5% of revenue) — a dilution consideration, though offset by buybacks.
- **Net income → OCF conversion is strong**, with OCF running well ahead of GAAP net income in FY2025 (excluding the Q2-2026 tax benefit).

---

## 6. Valuation Analysis

| Metric | Value |
|---|---|
| Market Cap | $5.10B |
| Implied Price | ~$24.26 |
| PE (TTM) | 17.4x (inflated by one-time tax benefit) |
| Forward PE | 15.0x |
| Price / Book | 4.55x |
| EV | ~$4.46B (Market cap − $676.4M cash + $38.3M debt) |
| EV / Revenue (TTM) | ~2.5x |
| EV / EBITDA (TTM) | ~19.5–22.4x |
| P/FCF (TTM) | ~13.6x |
| EPS (TTM) | $1.39 |
| Forward EPS | $1.62 |

**Valuation context:**
- At ~2.5x EV/Revenue with 20–29% top-line growth, ~20% FCF margins, and first-year profitability inflection, RELY screens **attractive vs. high-growth fintech peers**.
- The **15x forward PE** is reasonable for a company growing earnings rapidly off a low base, with a 62% gross margin and 32% ROE.
- **Quality caveat:** TTM EPS of $1.39 includes the $0.93 Q2-2026 print, which contains the one-time tax benefit. On a pre-tax normalized basis, TTM EPS is roughly $0.75–0.80, putting the "clean" PE closer to 30x — still justifiable given growth but meaningfully higher than the headline 17.4x.

---

## 7. Investment Considerations

### Bull Case
1. **Proven growth at scale:** Revenue $653.6M (2022) → $1.81B (TTM), a 2.8x expansion in ~3.5 years, with 20%+ YoY growth persisting.
2. **Operating leverage inflection:** Gross margin up ~1,200bps since 2022 (50.0% → 61.5%); operating margin swung from −18.5% (2022) to +14.3% (TTM).
3. **First full year of GAAP profitability (2025), with TTM net income of $305M** including the tax benefit.
4. **Fortress balance sheet:** $676M cash, ~$38M debt, 3.18x current ratio; zero reliance on external capital for growth.
5. **Strong cash generation:** ~$375M TTM FCF (~20.7% FCF margin) funding buybacks; management returned ~$65M to shareholders in H1 2026.
6. **Low volatility profile (beta 0.34)** — attractive for risk-adjusted positioning.
7. **Durable competitive moat:** licensed money-transfer rails, established brand in remittance corridors, network effects.

### Bear Case / Risks
1. **Earnings quality:** Q2-2026's $0.93 EPS was boosted by a ~$141M one-time tax benefit; headline TTM PE (17.4x) understates the true multiple on clean earnings.
2. **Intense competition:** Wise, Western Union, MoneyGram, Zepz, and bank/FX providers compete aggressively on fees in the remittance space.
3. **Regulatory exposure:** Money-transmission licensing, AML/KYC compliance, and potential remittance-fee regulation are ongoing risks.
4. **FX sensitivity:** Exchange-rate movements impacted cash by −$0.9M in Q2 2026 and −$1.7M in Q3 2025; currency volatility affects revenue translation and customer demand.
5. **SBC dilution:** ~9.5% of revenue in stock comp (~$155M/yr) dilutes shareholders, only partially offset by buybacks.
6. **Balance-sheet float noise:** Large swings in prepaids/customer liabilities can confuse period-over-period comparisons.
7. **Momentum/valuation risk:** Stock is +43% above the 200-day average and near 52-week highs; near-term consolidation is possible.

---

## 8. Actionable Insights for Traders

1. **Focus on pre-tax earnings for valuation:** Strip out the Q2-2026 one-time tax benefit (~$141M) when modeling. Clean TTM EPS ≈ $0.75–0.80; forward EPS estimate of $1.62 implies continued strong underlying growth.
2. **Watch the revenue growth trajectory:** Q2-2026 (+20.2% YoY) is the key momentum metric; acceleration from Q1-2026 (+8.2% q/q sequential) signals healthy end-demand. Any deceleration below ~18% YoY would warrant re-rating risk.
3. **Monitor margin expansion:** Gross margin of ~62% and operating margin of ~14% are the structural value drivers. Continued expansion toward the high-60s GM would support a higher multiple.
4. **Track capital allocation:** The buyback program (~$65M in H1 2026) is a positive signal; combined with $676M cash, the company has ample dry powder for M&A or expanded buybacks.
5. **Seasonality awareness:** Q4 2025 OCF ($149.6M) vs. Q3 2025 ($40.0M) shows strong seasonal swings tied to holiday remittance volumes — don't annualize any single quarter's cash flow.
6. **Entry-level context:** At ~$24.26 (near the $27.15 high), a pullback toward the 50-day average ($22.28) would offer a more favorable risk/reward entry; support at the 200-day ($17.70) is well below current levels.
7. **Risk management:** Beta of 0.34 makes RELY a lower-volatility growth vehicle; however, given the one-time earnings boost, consider valuation on forward (15x) rather than trailing (17.4x) earnings.

---

## 9. Summary Table — Key Fundamental Points

| Category | Metric | Value (as of 2026-08-12) | Insight |
|---|---|---|---|
| **Identity** | Company / Ticker | Remitly Global, Inc. / RELY | Digital cross-border money transfer (fintech), Nasdaq |
| **Market Data** | Market Cap / Price | $5.10B / ~$24.26 | Near 52-wk high ($27.15); 43% above 200-day ($17.70) |
| **Valuation** | PE (TTM) / Fwd PE | 17.4x / 15.0x | Trailing PE flattered by one-time tax benefit |
| **Valuation** | EV/Revenue / EV/EBITDA | ~2.5x / ~19.5–22.4x | Reasonable for 20–29% grower with 62% GM |
| **Growth** | Revenue TTM / Q2-26 YoY | $1.81B / +20.2% | Consistent mid-20%+ growth; accelerating q/q |
| **Profitability** | FY2025 Net Income | +$67.9M (first profitable year) | From −$37.0M (2024), −$117.8M (2023) |
| **Profitability** | Net Margin / Op Margin (TTM) | 16.9% / 14.3% | Strong operating leverage post-inflection |
| **Earnings Quality** | Q2-2026 EPS | $0.93 (incl. ~$141M tax benefit) | Clean pre-tax EPS ≈ $0.30 for the quarter |
| **Balance Sheet** | Cash / Total Debt | $676.4M / $38.3M | Net cash position; 3.18x current ratio |
| **Balance Sheet** | Stockholders' Equity / TBV | $1.13B / $1.07B | Equity up 69% in 18 months; ROE 32.2% |
| **Cash Flow** | TTM OCF / TTM FCF | $406.1M / $375.1M | ~20.7% FCF margin; capex-light model |
| **Capital Returns** | Buybacks (H1 2026) | ~$65.2M | Buyback program initiated H2 2025 |
| **Risks** | Key watch items | Competition (Wise/WU), regulation, FX, SBC (~$155M/yr), one-time tax boost | Monitor clean EPS, GM trajectory, seasonal OCF |
| **Technicals** | Beta / Trend | 0.34 / Bullish (above 50-day & 200-day) | Low-vol growth; watch $22.28 (50-day) support |

---

**Analyst Conclusion:** RELY presents a compelling fundamental picture — a high-growth, newly profitable fintech with expanding margins, a net-cash balance sheet, ~$375M TTM FCF, and an active buyback program. The principal caveat is that TTM earnings include a large one-time tax benefit; on clean forward earnings (15x) the valuation remains reasonable for the growth profile. The dominant long-term risks are competitive pressure in remittances and regulatory/FX exposure.

**FINAL TRANSACTION PROPOSAL: BUY** — Fundamental strength (revenue growth +20% YoY, margin expansion to 62% GM / 14% op margin, net-cash balance sheet, ~$375M TTM FCF, buybacks) supports a bullish stance at ~$24.26; suggested accumulation on any pullback toward the $22–23 zone (50-day average) with forward PE of 15x providing a reasonable entry for a low-beta (0.34) growth holding.

## II. Research Team Decision

### Bull

Bull Analyst: # The Bull Case for RELY: A Rare Inflection Where Growth, Profitability, and Value Intersect

**Analysis Date: 2026-08-12 | Ticker: RELY (Remitly Global, Inc.)**

---

Look, I get why the bears are circling. A stock up 85% YTD makes people nervous. I've seen the "overbought" calls, the "good news is priced in" chatter, and the warnings about one-time tax benefits. But here's the thing—when I strip away the surface-level concerns and look at what's actually happening with RELY, I see one of the cleanest fundamental inflection points in fintech today. Let me walk you through exactly why the bull case doesn't just survive contact with the bear arguments—it wins.

---

## 1. The "This Run Is Exhausted" Argument Is Backwards

Let's address the elephant in the room first. Yes, RELY is up ~85% YTD and ~97% off its November 2025 low of $12.31. Bears will tell you that means the easy money is made. But here's what that framing misses: **the stock is still 45% below its all-time highs, and it just put up the best quarter in company history.**

The run from $12 to $24 wasn't speculation—it was repricing. The market finally recognized what the income statement was screaming: this company crossed the profitability threshold in a major way.

Look at the trajectory:
- **FY2022:** Revenue $653.6M, net loss of -$117.8M
- **FY2023:** Revenue $944.3M, net loss of -$37.0M
- **FY2024:** Revenue $1,264.0M, net loss of -$37.0M
- **FY2025:** Revenue $1,635.1M, *first-ever full-year GAAP profit of +$67.9M*
- **TTM:** Revenue $1.81B, net income $305M, **$375M in free cash flow**

This isn't a momentum stock—it's a **compounder that just flipped to self-funding mode**. A 20.7% FCF margin with capex of only ~1.7% of revenue? That's an asset-light software model that's hitting escape velocity.

And the stock at **15x forward earnings** for a company growing revenue 20%+ with 62% gross margins? That is not a bubble multiple. That's a reasonable entry point for a low-beta (0.34) growth story.

---

## 2. The Tax Benefit "Gotcha" Misses the Point Entirely

One of the bear's favorite weapons is the Q2 2026 one-time tax benefit. "EPS of $0.93 is inflated by a $141M valuation allowance release," they'll say. "Clean earnings are closer to $0.25-0.30 for the quarter."

Fine. Let's accept that completely. What does the clean picture actually look like?

- **Q2 2026 revenue:** $495.2M, +20.2% YoY
- **Q2 2026 gross margin:** 62.1%, up from 59.0% a year ago
- **Q2 2026 operating income:** $66.7M, up **4.6x** from $14.6M in Q2 2025
- **Q2 2026 pre-tax income:** $64.6M
- **Record adjusted EBITDA:** $115M at a 23% margin

Even excluding the tax benefit entirely, RELY earned **$64.6M pre-tax in a single quarter** on $495M of revenue. That's a 13% pre-tax margin. A year ago, operating income was $14.6M. The operating leverage here isn't an accounting artifact—it's the result of gross margin expanding from 59% to 62.1% while revenue grew 20%.

And here's the part bears conveniently ignore: **deferred tax asset valuation releases don't happen in a vacuum.** That $141M benefit exists *because* the company became sustainably profitable. The IRS doesn't let you recognize deferred tax assets unless you can demonstrate a history of profitability and a clear path forward. The tax benefit is actually the market's *most conservative validation* that the earnings turnaround is real.

But you know what? I don't even need the tax benefit. Give me the forward multiple on clean earnings:
- Forward PE: **15.0x**
- TTM FCF: **$375M** → P/FCF of just **13.6x**
- EV/Revenue: **2.5x** for a 20%+ grower

That's a reasonable multiple for a company at the beginning of a margin expansion story, not an exhausted one.

---

## 3. "Competition Will Crush Them" — Let's Look at the Actual Numbers

The bear thesis leans heavily on competition: Wise, Western Union, MoneyGram, PayPal/Xoom. "The remittance space is a fee war," they argue.

But here's the data that tells a different story:

**Remitly's gross margin is *expanding*:** 50.0% (FY2022) → 59.0% (Q2 2025) → **62.1% (Q2 2026)**. In a "fee war," gross margins contract. Remitly's are rising. That's what a company with pricing power and network effects looks like.

**The company isn't losing share—it's gaining it.** Active customers surpassed **10 million**, representing 10x growth since 2019. Q2 revenue grew +20.2% YoY on top of a $1.6B+ revenue base. The "disruptor" status isn't just narrative—Barron's wrote a feature titled *"This Stock Can Rally 35% as It Disrupts Global Remittance Markets."*

**Meanwhile, the "safe" incumbent is flashing distress signals.** Western Union pays a 13.5% dividend yield. That's not "value"—that's a market telling you the legacy franchise is in structural decline. A 13.5% yield means the market is pricing in serious risk to that dividend. Remitly, by contrast, is initiating buybacks, not paying dividends. One company is returning capital because it has nothing better to do; the other is investing in a $900B+ total addressable market.

**And the product moat is widening, not narrowing.** The newly launched **Remitly Global Card** transforms the company from a pure remittance play into a multi-currency global banking platform—spend, save, borrow, and send in one product. That's a TAM expansion from $900B in remittances into consumer banking, small business flows, and recipient-side services. This is exactly the kind of product-led expansion that forces bears to constantly redraw their assumptions.

---

## 4. The Balance Sheet Is a Fortress—and Getting Fortier

This is the part that really undermines the bear case. Bears like to paint RELY as a cash-burning growth story. Here's the reality:

| Metric | Value |
|---|---|
| Cash & Equivalents | **$676.4M** |
| Total Debt | **$38.3M** |
| Net Cash Position | **~$638M** |
| Current Ratio | **3.18x** |
| TTM Operating Cash Flow | **$406.1M** |
| TTM Free Cash Flow | **$375.1M** |
| Buybacks in H1 2026 | **~$65.2M** |

The company took on a $155M term loan in Q4 2025 for seasonal working capital needs and **repaid it in Q1 2026**. That's not financial stress—that's treasury management.

Equity book value grew 69% in 18 months, from $665.5M to $1.13B. Retained earnings improved from -$528.3M to -$205.4M. At this pace, the accumulated deficit gets erased entirely within the next two years.

RELY has $638M of net cash on a $5.1B market cap—that's **~12.5% of the market cap in cash alone**. When you adjust EV for that cash, the operating business trades at roughly 2.5x EV/Revenue. For a company with 62% gross margins, 20% revenue growth, and a newly profitable operating model?

That's not expensive. That's a gift.

---

## 5. The "Guidance Was Only In Line" Concern Ignores the Beat-and-Raise Momentum

The bears point out that Q3 2026 guidance of ~$506M was only "close to" analyst estimates. Fair. But let's put that in context:

- **FY2026 revenue guidance was *raised* to $1.978–1.988B.**
- Q2 revenue of $495.2M **beat** expectations.
- Q2 GAAP EPS of $0.93–$0.98 represented a **+268.97% earnings surprise** (Zacks).
- The company **beat on revenue, beat massively on EPS, reported record EBITDA**, and then *raised* the full-year number.

Bears will always find a nitpick. Let me show you what the trend actually looks like:

| Quarter | Revenue | YoY Growth | Operating Income |
|---|---|---|---|
| Q2 2025 | $411.9M | — | $14.6M |
| Q3 2025 | $419.5M | — | $11.8M |
| Q4 2025 | $442.2M | — | $38.8M |
| Q1 2026 | $452.8M | — | $53.7M |
| Q2 2026 | $495.2M | **+20.2%** | **$66.7M** |

Operating income went from $14.6M to $66.7M in four quarters—a **357% increase**—on revenue growth of just 20%. That's an operating leverage story that most SaaS companies can only dream of. Every incremental dollar of revenue is dropping with increasing efficiency to the bottom line.

---

## 6. The Macro Backdrop Couldn't Be More Supportive for Remittance Demand

Let's look at the macro data we have as of August 12, 2026:

- **Unemployment: 4.1% and falling** (from 4.3% in May). Remittance senders are overwhelmingly immigrant workers employed in the U.S. A strong labor market = steady income = steady remittance flows.
- **Inflation: cooling.** CPI fell -0.35% over the last three months and core PCE is benign. That means the dollars immigrants send home are going further—supporting recipient demand.
- **Dollar: stable-to-slightly-soft.** No FX shock threatening corridor economics. A stable USD is good for RELY's USD-sender model.
- **VIX: 15.28, down 11% month-over-month.** The risk environment is conducive to growth stocks.
- **Recession odds: only 8%** by end of 2026.
- **Fed funds rate: 3.63%.** Yes, high-for-longer is priced in, but RELY is now **GAAP-profitable with $638M net cash**—it doesn't need to borrow to fuel growth. Rate sensitivity is a bear argument designed for unprofitable growth stocks. That's not RELY anymore.

The only genuine macro risk is Iran/Hormuz and oil prices. I'll concede that. If oil spikes dramatically, it pressures both sender budgets and recipient purchasing power. But the prediction markets put U.S. invasion of Iran at just **18%**. It's a tail risk, not a base case—and at 0.34 beta, RELY is one of the lower-volatility ways to play the fintech space while still capturing growth.

---

## 7. "Insider Selling" Is a Headline, Not a Thesis

Another bear favorite: directors sold shares. Let me be precise about what actually happened:

- A director **exercised fully vested pre-IPO options at $0.64/share**—that's not selling conviction, that's tax planning. And after the sale, they still retain 261,094 shares plus 169,818 options.
- Another director's sale leaves a **$45.96M position intact**.

Executives are allowed to diversify. What matters is the *trend*. When insiders are selling into weakness and the company is still losing money, worry. When insiders exercise $0.64 options after a record quarter and still hold millions in stock, that's a non-event.

Meanwhile, the company itself is putting its money where its mouth is: **~$65.2M in buybacks during H1 2026.** Management believes the stock is worth buying. They're deploying the fortress balance sheet to reduce share count. That's the signal that actually matters.

---

## 8. Let's Talk About the Technical Setup—Because It Confirms the Fundamentals

The bears want to claim this stock is overextended and due for a crash. But the technical picture actually tells a story of **structural uptrend with healthy digestion**:

- **Price: $24.23** — above the 10 EMA ($23.96), 50 SMA ($22.34), and 200 SMA ($17.73)
- **Structure:** 10 EMA > 50 SMA > 200 SMA, all rising. Textbook bullish alignment.
- **RSI: 54.06** — this is *neutral*, not overbought. There's zero momentum exhaustion signal here. In fact, there's room to run before even reaching 60, much less 70.
- **MACD: 0.38, positive** — the histogram is flattening (-0.066 → -0.052), which is early evidence of momentum stabilizing, not rolling over.
- **Volume:** The August 6 breakout on 8.4M shares vs. 2-3M typical shows real participation. Pullback volume has been *declining* (4.3M → 3.0M → 3.2M), which is what healthy corrections look like—not distribution.
- **VWMA: 24.08** — price is trading *above* the volume-weighted average, confirming the buying is genuine.

The stock is **36.7% above the rising 200 SMA** and has successfully reclaimed the 10 EMA. The 50 SMA sits at $22.34 as a meaningful confluence support, and the Bollinger lower band at $22.01 aligns with it. So even in a deeper correction, there's a well-defined support zone around $22–22.5.

Bears see a stock that's run too far. I see a stock that's **building a base after a spike, reclaiming short-term momentum, and coiling for the next leg up**—with the earnings catalyst, product catalyst, and macro tailwinds all pointing in the same direction.

---

## 9. The Talent and Scale Moat

Let's not forget the qualitative factors. Remitly has:

- **10 million active customers**—a 10x increase since 2019
- A **licensed money-transfer infrastructure** across corridors that takes years and significant regulatory capital to replicate
- A **brand built on trust** in diaspora communities where reliability and speed matter more than price alone
- A product roadmap expanding into cards, credit, small business flows, and AI-driven personalization

Western Union's 13.5% dividend yield is the tell. The incumbent is milking a declining franchise. Remitly is acquiring its customers and building a full financial relationship with them. This is how disruptors compound for a decade.

---

## 10. The Bear's Best Argument—and Why Even That One Fails

The most sophisticated bear argument I've heard is this: *"Q2 guidance was only in line. The beat-and-raise cadence may be ending. At 15x forward earnings, you're paying for perfection."*

First, 15x forward earnings is **not** perfection pricing. For a company with:
- 62% gross margins
- 20% revenue growth
- 14.3% TTM operating margin
- 32.2% ROE
- $375M TTM FCF
- $638M net cash

...the peer group trades at much richer multiples. High-growth fintech with this margin profile typically commands 25-35x forward earnings. RELY at 15x is priced for *deceleration to low-teens growth at best*—not for the continued operating leverage that the last four quarters have demonstrated.

Second, even if Q3 comes in at guide, that's still **~$506M in revenue, a 23%+ EBITDA margin trajectory, and continued GAAP profitability**. The "disappointment" scenario is still a remarkably strong quarter.

Third, the Global Card launch hasn't even begun to show up in revenue. That's an **un-modeled catalyst**. When the multi-currency card expands to more markets—with spend, save, borrow, and send capabilities—the revenue mix shifts toward higher-value, recurring financial services. The option value embedded in this product roadmap is not in the consensus estimates.

---

## The Bottom Line

| Bear Argument | Bull Response |
|---|---|
| "Stock up 85% YTD—it's priced in" | Still 45% below ATH; 15x forward PE for 20% grower; earnings repricing isn't exhaustion |
| "EPS inflated by one-time tax benefit" | Pre-tax income grew 4.6x YoY; record EBITDA $115M; operating leverage is structural |
| "Competition will compress margins" | Gross margins are *rising* (59% → 62.1%); 10M users; product moat widening |
| "Guidance only in line" | Full-year guidance *raised*; beat-and-raise cadence intact; Q2 beats on every metric |
| "Macro headwinds" | Labor market firm, inflation cooling, recession odds 8%, VIX 15, dollar stable |
| "Insider selling" | $0.64 pre-IPO option exercises; insiders retain $45.96M+ positions; company buying back stock |
| "Geopolitical tail risk" | 18% Iran invasion odds; beta 0.34; tail risk, not base case |

**The bull case for RELY is simple:** This is a company that has just crossed the most important inflection point a business can cross—from cash-burning growth story to self-funding, GAAP-profitable, FCF-generating compounder. And it's doing so while still growing revenue 20%+ and expanding margins.

At 15x forward earnings, with a fortress balance sheet, a rising technical trend, record customer adoption, a new product catalyst, and a macro backdrop that supports remittance demand, the risk/reward is decisively skewed to the upside.

Bears will point to the run-up. They'll cite the tax benefit. They'll warn about chasing. But the evidence shows a company in the *early innings* of a profitability-driven re-rating, not the late stages of a speculative melt-up.

**My recommendation: BUY RELY at current levels, add on any pullback toward the $22–23 zone, and let operating leverage do the heavy lifting.**

Disclosure: This analysis is for informational purposes and reflects the bull case based on verified data as of August 12, 2026. Always conduct your own due diligence and position sizing appropriate to your risk tolerance.
Bull Analyst: # RELY: The Bear Just Confused a Compounder With a Coin Flip

Let me start by acknowledging the bear's presentation style — it's clean, it's confident, and it **cherry-picks data like a champion**. But when you actually put the bear's numbers next to the full picture, the thesis collapses under the weight of its own omissions. So let's go at it, point by point, because this is a debate worth having — and the evidence is squarely on the bull's side.

---

## 1. "Growth Is Decelerating" — The Most Misleading Chart on the Desk

The bear shows you this: 44% → 34% → 29% → 20%, and screams "deceleration!" It's technically true. It's also **completely misleading**, because it ignores what happens when a base grows. Let's do the actual math the bear skipped:

- 2023: **+$290M** in absolute revenue growth
- 2024: **+$320M** in absolute revenue growth
- 2025: **+$371M** in absolute revenue growth
- Q2 2026 alone: **+$83M YoY** — *in a single quarter*

That's not a company losing momentum. That's a company adding **more absolute revenue every single year** while growing on a base that has nearly tripled since 2022. The bear wants you to think 20% growth on $1.8B is the same as 20% growth on $650M. It isn't. **20% of $1.8B is $360M of incremental revenue — more than half of the company's entire 2022 revenue — in a single year.**

And here's the kicker: the bear conveniently stops at revenue growth and never mentions what's happening to the bottom line. Let's show the full picture:

| Quarter | Revenue Growth YoY | **Operating Income** | **Operating Income Growth** |
|---|---|---|---|
| Q2 2025 | — | $14.6M | — |
| Q3 2025 | — | $11.8M | — |
| Q4 2025 | — | $38.8M | — |
| Q1 2026 | — | $53.7M | — |
| Q2 2026 | +20.2% | **$66.7M** | **+357% vs. Q2 2025** |

You're telling me a company that grew operating income **4.6x** while growing revenue 20% is "a business losing its growth premium"? That's not a maturing business cooling off. **That's operating leverage hitting the inflection point every investor dreams of.** Revenue growth of 20% at this scale, with margins expanding this fast, is the *definition* of a compounder in its early innings — not late-stage exhaustion.

---

## 2. The Tax Benefit "Mirage" — You're Missing WHY It Exists

The bear calls the $141M deferred tax asset release "an accounting artifact" and claims the entire August 6 pop was built on it. Let me ask the bear a simple question: **Why did the company get to recognize that benefit at all?**

GAAP rules don't just let you wave a wand and release a valuation allowance. You have to demonstrate a **history of sustained profitability and convincing evidence that future profits will continue**. The IRS and auditors don't hand out $141M tax benefits to companies with a "mirage" P&L. The DTA release exists **precisely because RELY's earnings turnaround is durable and documented**.

But forget the accounting for a second — let's do what the bear refuses to do and look at the *clean* operations:

- Q2 2026 pre-tax income: **$64.6M**
- Q2 2026 adjusted EBITDA: **$115M at a 23% margin** — a record
- Q2 2026 revenue beat: **+2.19% above consensus**
- FY2026 guidance: **raised** to $1.978–1.988B

Even if you throw the tax benefit entirely in the trash — and I mean completely ignore it — the company still earned **$64.6M pre-tax in a single quarter**, which is nearly **5x** the operating income from a year earlier. The bear's "clean PE of 30x" is built on a TTM number that includes the low-profit quarters of 2025. But the run-rate is what matters: Q2 2026 clean EPS was ~$0.25–0.30, and Q3 is guided higher. **Annualize the clean run-rate and you're looking at $1.00–$1.20 of normalized earnings power — a ~20x multiple on a business growing 20% with a fortress balance sheet.** That's not "expensive." That's reasonably priced for a company with this margin trajectory.

---

## 3. "Rising Margins = Harvest Strategy" — That's Not What Harvesting Looks Like

This is the bear's most creative argument, and it collapses under one data point: **revenue grew 20% in the quarter.** A "harvest strategy" is what Western Union is doing — flat-to-declining revenue, milking corridors, paying out a 13.5% dividend yield because management has no growth opportunities. Western Union's dividend yield is **not** a distraction; it is the tell. The market prices WU for structural decline. That's what a harvest looks like.

RELY grew revenue 20%, grew gross profit **26.5%**, and grew operating income 357%. Gross margin expanded from 59.0% to 62.1% *while* revenue was accelerating sequentially (+9.4% QoQ). That's not milking existing corridors. That's **scale advantages and network effects** — the cost to serve an additional customer drops as the network grows. The bear says "it's a commodity, moving money." Tell that to Remitly's 10 million customers, who chose RELY's brand and reliability over the incumbents.

And the Global Card? The bear calls it "me-too" — Wise does it, Revolut does it. Fine. But here's what the bear refuses to acknowledge: **Remitly isn't entering banking from scratch. It's layering a card onto an existing 10-million-customer base that already trusts it for money movement.** Cross-selling a card to an engaged, high-frequency remittance user base is *dramatically* cheaper and easier than acquiring customers cold. The TAM expands from $900B in remittances to the broader consumer financial services market — and the infrastructure, licenses, and compliance rails are already built. That's not a "me-too product." That's a **distribution advantage** that Wise and Revolut would kill for.

---

## 4. "Fortress Balance Sheet = No Investment Opportunities" — Seriously?

The bear looks at **$676M in cash, $38M in debt, $375M in TTM free cash flow** — and calls it *stagnation*. This is the most backwards take in the entire bear thesis.

Let me walk through what that balance sheet actually enables:

1. **The company just launched the Global Card.** That's the "investment opportunity" the bear claims doesn't exist. It takes capital to build, market, and scale a global financial product. The cash is the fuel.
2. **The company initiated buybacks in H2 2025 and bought back ~$65M in H1 2026.** Why would a management team with "no investment opportunities" deploy capital into its own stock? Because they see value. They're not just talking — they're buying.
3. **M&A optionality.** With $638M of net cash, RELY can acquire smaller remittance players, corridor-specific licenses, or complementary fintech products without issuing a single share of dilution.

The bear says "buying at 52-week highs is poor capital allocation." The historical evidence says the opposite: **companies that buy back stock when they're profitable and growing, regardless of near-term price, tend to create enormous long-term value.** The market's short-term view of "high" is often the long-term view of "cheap" when you're a 20% grower at 15x forward earnings.

And let's not lose sight of the forest: $375M of TTM FCF at a 20.7% margin, with capex of just ~1.7% of revenue, means this business **prints cash**. Calling a cash machine "stagnant" is like calling a gold mine "just a hole in the ground."

---

## 5. The Beta/Volatility Trap — Let's Use Actual Data

The bear says a 0.34 beta is a "historical artifact" and the *real* risk is the $1.20 ATR. Let's concede the ATR is elevated — it is, at ~4.9% of price. But here's what the bear conveniently ignores: **elevated volatility after a 97% run from the November low is not a reason to sell; it's the cost of participating in a legitimate re-rating.** You don't get a 97% return without some volatility along the way.

The bear's deeper point is that low beta makes you complacent. Fine — let's use the bear's own ATR framework: with a $1.20 ATR, the distance from the current close of $24.23 to the 50 SMA support at $22.34 is roughly **1.6 ATRs**. That's not "one bad headline from disaster." That's **a defined, well-identified support zone** that's been rising all summer — from ~$20.50 in mid-June to $22.34 today.

And the bear's claim that the stock is "36.7% above the 200-day" is somehow dangerous? That 200-day SMA has been **rising steadily** from ~$16.50 to $17.73 — the long-term trend is up. Stocks in confirmed uptrends trade far above their 200-day. That's not a rubber band ready to snap; that's what a **structural uptrend looks like**.

---

## 6. Macro — The Bear's Headwinds Are Actually Tailwinds

Let me take each of the bear's macro "headwinds" and show why they're actually supportive:

**"High-for-longer rates are a valuation headwind."** For a company with $676M cash and $38M debt — a **net cash position of ~$638M** — high rates mean RELY is *earning* more interest income on its cash pile. The company doesn't need external capital. It's not a rate-sensitive borrower; it's a net beneficiary. And the 86% probability of zero cuts is already **fully priced** into the stock. The market has been living with 3.63% Fed funds for months, and RELY has gone from $12 to $24 through that entire period.

**"A strong dollar hurts remittance demand."** Actually, the broad dollar index has been **drifting lower** — from ~120.8 in late July to ~119.06 on August 7. The dollar is stable-to-soft, which is modestly *positive* for recipient purchasing power in key corridors like MXN and PHP. And more importantly, a strong U.S. labor market — unemployment at 4.1% and *falling* — means the immigrant workers who are RELY's core senders have jobs and income. **Steady employment in the U.S. is the single biggest driver of remittance volumes, and it could not be stronger right now.**

**"Hormuz is a live tail risk."** I'll concede this one — it's real. But the bear is treating an 18% probability as the base case. The prediction market also says **86% odds of no Fed cuts** (a headwind the bear emphasizes), and **8% odds of recession** (a tailwind the bear ignores). You can't cherry-pick the tail risks you like and ignore the ones you don't. At 0.34 beta with a fortress balance sheet, RELY is structurally better positioned than the average high-growth stock to absorb an oil shock.

---

## 7. The Technical "Distribution Top" — Let's Look at the Actual Tape

The bear call says August 6 was a "blow-off top" and the subsequent decline was "distribution." Let's look at what the bear left out:

**The pullback volume pattern is the opposite of distribution:**

- August 6 (spike): **8.4M shares** — real participation, real buying
- August 10: **4.3M shares**
- August 11: **3.0M shares**
- August 12: **3.2M shares**

Distribution is when a stock drops *on rising volume* — that's sellers aggressively exiting. What we're seeing is a pullback on **progressively declining volume** — that's sellers *drying up*. A "dead cat bounce" doesn't typically happen on lighter volume than the prior down days; that's the signature of a **healthy correction**.

And the data as of August 12 close:

- Price **$24.23**, back **above** the 10 EMA (23.96) and VWMA (24.08)
- 10 EMA > 50 SMA > 200 SMA — **perfect bullish alignment**, all rising
- RSI at **54.06** — neutral, with room to run before reaching any overbought level above 70
- MACD at **+0.38**, positive territory
- MACD histogram: **flattening from -0.066 to -0.052** — early evidence that momentum is stabilizing, not rolling over

The bear says a close below $22–22.5 would confirm the top. Fine — but that's a well-defined invalidation level, not a prediction. The current picture is a **pullback within an uptrend**, with the short-term pivot reclaimed.

---

## 8. Insider Sales — The Bear Found the Weakest Argument on the Board

The bear asks, "Why is a director selling at $24 instead of holding for decades?" Let me tell you, because this is important: **It's a $0.64 pre-IPO option exercise.** The director paid $0.64 for shares that now trade at $24 — a **3,650% gain**. They are *required* to pay taxes on the exercise. Selling a portion of exercised shares to cover the tax bill is the most normal, boring, standard practice in corporate America. And what did the director retain? **261,094 shares PLUS 169,818 options.** Another director retains a **$45.96M position**.

Meanwhile — and this is the part that should matter to you — **the company itself bought back $65.2 million of stock in H1 2026**. Management is allocating its own capital to buy at these "overvalued" prices. Who has better information about RELY's prospects: a director diversifying a small fraction of a multi-million-dollar position for tax purposes, or the management team spending corporate cash on buybacks? The answer is obvious.

---

## 9. The "Story Is Over" Claim — The Product Pipeline Says Otherwise

The bear's most audacious claim is that the "story is over." Let's review what just happened in the last 7 days:

- **Record Q2**: Revenue $495.2M, +20.2% YoY, record EBITDA at 23% margin
- **10 million active customers** — up 10x since 2019
- **Raised FY2026 guidance** to $1.978–1.988B
- **Launched the Remitly Global Card** — a multi-currency, spend/save/borrow/send product
- **Barron's published a feature calling for 35% upside**
- **StockTwits: 53% bullish vs. 0% bearish**
- **VIX at 15.28** — calm tape, no macro panic
- **Recession odds at 8%** — the demand backdrop is solid

Does this sound like a story that's "over"? The **Global Card hasn't contributed a single dollar of revenue yet**, and the company raised guidance *before* the card scales. That's an **un-modeled catalyst** on top of an already-beating core business. The market is paying 15x forward earnings for the core remittance business and getting the card, the AI push, small-business flows, and recipient-side services **for free**.

---

## Let's Settle the Real Debate

The bear keeps coming back to one thesis: *You're paying too much for a decelerating business with inflated earnings.*

Here's my response: **You're not paying 30x clean earnings. You're paying ~20x the *run-rate* earnings, 13.6x free cash flow, and 2.5x EV/revenue — for a company that just proved it can grow operating income 357% in a year, holds $638M of net cash, generates $375M of annual FCF, and has a new product catalyst that isn't even in the models yet.**

The bear asks you to believe that a fundamentally stronger company — profitable, cash-rich, growing, innovating — is *more* dangerous than the loss-making, growth-at-all-costs version from 2023. That's not analysis; that's nostalgia for a narrative that no longer applies.

**The bottom line:** This is a profitable, self-funding, 20%-growing fintech at 15x forward earnings with a rising technical structure and a monster product catalyst. The bears have spent hours telling you why the easy money is made. But the easy money was made by people who bought **before** the profitability inflection. The durable money is made by buying **after** the market confirms the inflection — and paying a reasonable multiple for what's now a proven, cash-generating machine.

**I'm buying RELY at $24.23. I'm adding on any dip toward $22–23. And I'm letting the operating leverage compound.**

The bear's case is clever. It's just not comprehensive. And in a debate, the side with the fuller evidence wins. Here, that's the bull.
Bull Analyst: # RELY: The Bear Keeps Fighting the Last War — I'm Investing in the Next One

**Ticker: RELY (Remitly Global, Inc.) | Date: 2026-08-12 | Price: $24.23**

You know what I appreciate about the bear's latest round? The consistency. Same charts, same tax-benefit talking point, same "failed breakout" reading, same insistence that a company growing operating income 357% year-over-year is somehow a deteriorating asset. But here's the thing about consistency: when you're consistently omitting the most important data points, you're not building a case — you're building a narrative. And narratives are exactly what the bear is telling you to avoid.

So let's settle this with the full dataset in front of us. Point by point.

---

## 1. "Growth Rate Has Been Cut in Half" — Measured in Percentages, Ignored in Dollars

The bear presented this exact table again:

| Period | Revenue Growth |
|---|---|
| FY2023 | +44.5% |
| FY2024 | +33.9% |
| FY2025 | +29.4% |
| Q2 2026 | +20.2% |

I'm going to present a table the bear left out — the one that actually matters for shareholder value creation:

| Period | Absolute Revenue Added | Operating Income |
|---|---|---|
| FY2023 | +$290.7M | Loss narrowing |
| FY2024 | +$319.7M | Loss narrowing |
| FY2025 | +$371.1M | **+$67.9M full-year profit** |
| Q2 2026 alone | +$83.3M YoY | **$66.7M in ONE quarter** |

Let's put this in perspective the bear refuses to acknowledge. The company added **$371M of incremental revenue in FY2025** — that's more than half of its *entire* FY2022 revenue base in a single year. And in Q2 2026, operating income hit $66.7M — up 4.6x from a year earlier.

The percentage decline from 44% to 20% looks scary when you stop the chart at the top line. But that "deceleration" is what happens when a company's revenue base nearly triples from $653M to $1.81B. The bear is essentially arguing that adding **$360M of new revenue per year** at 62% gross margins is a *problem*. I'll take that kind of "problem" every single day.

And here's the real kicker: the bear says "RELY is not accelerating." But look at the actual sequential trend:

- Q1 2026: Revenue $452.8M
- Q2 2026: Revenue $495.2M — **+9.4% sequential growth**

That is the strongest sequential growth in recent quarters. And Q3 guidance of ~$506M implies continued sequential growth. The company is not decelerating — it's **seasonally and sequentially expanding** on a massive revenue base.

---

## 2. The Tax Benefit — "It Doesn't Generate Cash" Is Exactly the Point

The bear says the tax benefit "doesn't generate cash." Let's make sure everyone understands what that means: **the company generated $134.6M of operating cash flow in Q2 2026 anyway.** And $406.1M over the trailing twelve months. The tax benefit is a balance-sheet item that recognized what the cash flow statement has been proving all along — this business is actually, genuinely, durably profitable.

The bear's math on "clean EPS" also deserves scrutiny. The bear says clean Q2 EPS is $0.22–0.24, "essentially flat with Q1." Let me just note the awkward implication: if the bear is right, then RELY earned $0.23 in Q1 2026 and $0.22–0.24 in Q2 2026 **while revenue grew from $452.8M to $495.2M and operating income grew from $53.7M to $66.7M.** So the "flat" earnings are actually the result of higher taxes on substantially higher pre-tax income — that's a *quality* problem, not an *earnings* problem.

And the "32x clean P/E" the bear keeps citing? Let's see how that works out going forward. The company is guiding to roughly $1.98B in FY2026 revenue. If operating margins just hold at Q2's level (~13.5%), that's roughly $267M of operating income for the year. Add interest income on $676M of cash (at ~4%, that's ~$27M), subtract a normalized tax rate, and you're looking at **$1.10–$1.20 of normalized forward EPS power** — or roughly **20x forward clean earnings** for a business growing 20% with $638M of net cash on the balance sheet.

Actually, let me do the comparison the bear keeps avoiding. Q1 2026 clean EPS of ~$0.23 on $452.8M revenue. Q2 2026 clean EPS of ~$0.24 on $495.2M revenue. The run-rate on that clean earnings power is over $1.00 per share. At $24.23, that's **~20-22x forward clean earnings** — a perfectly reasonable multiple for a 20% grower with expanding margins. The "30x" scare only works if you pretend Q3 and Q4 won't have higher revenue and continuing operating leverage. They will.

---

## 3. "Guidance Was Only In Line" — The Bear's Own Standard Indicts Every Great Stock

The bear says Q3 guidance of ~$506M is "in line with consensus" and treats it as a disappointment. Let's apply that standard consistently:

- Apple guides "in line" every quarter. Amazon guides "in line." Microsoft guides "in line."
- What matters is whether companies **beat and raise**. RELY just beat revenue by 2.19%, beat EPS by 269%, reported record EBITDA, and **raised full-year guidance.**
- The raised FY2026 guide of $1.978–1.988B implies H2 revenue of roughly $1.03B — which at ~20% growth on an increasingly profitable base implies **continued record operating income.**

The bear's "no room for error" claim only works if you accept the premise that the multiple is stretched. I've shown it isn't. At 15x forward reported earnings, or ~20x forward clean earnings, there's plenty of room for a modest miss without a catastrophic re-rating — and the fortress balance sheet means the company doesn't need capital markets even in a downturn.

---

## 4. The Global Card — "Me-Too" Is the Most Bullish Word in Fintech

The bear says the card is a "me-too" product because Wise, Revolut, and Nubank already exist. I'm going to respond to that with a question: **which of those companies has 10 million customers actively sending cross-border money through its rails on a recurring basis, and is now layering a card on top of that existing relationship?**

The bear's argument treats customer acquisition as the only moat. It isn't. **Distribution is the moat.** Remitly already has:

- A licensed, regulated money-transfer infrastructure across dozens of corridors
- 10 million active customers who transact with them regularly
- A brand built on trust in diaspora communities
- A transaction history that enables credit underwriting (the "borrow" feature)
- A cost structure that's already profitable before the card contributes anything

Cross-selling a multi-currency card to an existing, engaged, high-frequency customer base is dramatically cheaper than Wise or Revolut's cold-acquisition model. The bear says remittance customers are price-sensitive commodity buyers. Fine. That's exactly why a card that bundles send, spend, save, and borrow — a **full banking relationship** — increases switching costs and wallet share. It's the difference between being a fee-based utility and being a primary financial institution for 10 million people.

And "zero revenue contribution" is precisely the point. **The market is pricing only the core remittance business. The card, the AI push, the small-business flows, the recipient-side services — all of it is un-modeled optionality on top of 20% core growth.** That's not "paying up." That's getting the option for free.

---

## 5. The SBC Argument — A Real Cost, But the Math Still Works

The bear's most legitimate point is SBC dilution. $155M annually is real. Let's take it head-on rather than dismiss it:

- TTM FCF: $375M
- TTM SBC: $155M
- Post-SBC FCF: ~$220M
- Market cap: $5.1B
- Post-SBC P/FCF: ~23x

The bear presents this as revelatory. But here's the context the bear leaves out:

**The company just started buying back stock, and it's accelerating.** Repurchases went from $23.9M in H2 2025 to $65.2M in H1 2026 — a 173% increase. The buyback is not a "wash" — it's the *beginning* of a capital-return program from a company that was loss-making 18 months ago. And management explicitly stated the buyback program is ongoing.

Furthermore, a 23x post-SBC FCF multiple for a company growing revenue 20%, with operating income growing 4.6x, 62% gross margins, and $638M net cash is **not expensive for a quality fintech compounder**. For context, that's roughly in line with the S&P 500's P/FCF on a *post-dilution* basis — while RELY grows revenue more than 5x faster than the index.

And let's note something else the bear ignores: **a large portion of SBC is non-dilutive in practice because it's tied to performance and retention.** The company's diluted share count of ~221M is barely above the basic count of ~210M — a mere 5% dilution over the entire history of the company through a period of explosive growth, which is *extremely* disciplined for a fintech.

---

## 6. The Volatility "Trap" — Let's Quantify the Actual Risk/Reward

The bear says a $1.20 ATR on a $24 stock is terrifying. Let's actually look at it honestly:

- ATR of $1.20 is 4.9% of price. Elevated, yes — for a stock coming off an 85% YTD run and a record earnings week. Elevated ATR after a major catalyst is *normal*, not pathological.
- The "15% round trip" from $27.15 to $23.14? That's what happens after a +8% earnings pop — **profit-taking**. And crucially, the stock is still up from the pre-earnings price of ~$22.50. The "distribution" the bear describes left the stock *higher* than where it started the week.
- The bear's risk/reward math is selective. Yes, $17.73 is 27% lower — but that requires a **catastrophic scenario** where the company's trend, fundamentals, and macro backdrop all break simultaneously. Meanwhile, upside to $27.15 is only "12%" if you're measuring over a silly short-term window. What matters is the **12-24 month forward return** for a company with this fundamentals profile.

And if you actually want to talk about risk/reward, consider this: the stock trades at 20-22x clean forward earnings with a rising 50-day SMA at $22.34, a rising 200-day SMA at $17.73, and **a 200-day SMA that has risen from $16.50 to $17.73 over the last two months.** This is a stock in a confirmed uptrend that just reported blowout earnings. The path of least resistance is up.

---

## 7. The Technical Setup — Bear Sees Distribution, I See Accumulation

The bear's "failed breakout" reading ignores the most important technical fact: **RELY is up 85% YTD, is above a rising 200-day, above a rising 50-day, above the 10-day EMA, and has positive MACD.**

Let's look at the tape objectively:

| Indicator | Value | What It Actually Means |
|---|---|---|
| Price vs. 10 EMA | $24.23 > $23.96 | Reclaimed short-term pivot |
| Price vs. 50 SMA | $24.23 > $22.34 | Above medium-term trend |
| Price vs. 200 SMA | $24.23 > $17.73 | Confirmed long-term uptrend |
| RSI | 54.06 | **Neutral** — no exhaustion, room to run |
| MACD | +0.38 | Positive momentum |
| MACD histogram | -0.05, flattening | Consolidation, not reversal |
| Volume on pullback | 4.3M → 3.0M → 3.2M | **Drying up — sellers exhausting** |

The bear says "buyers aren't stepping in" — but the buyers stepped in on August 6 with 8.4M shares. What's happening now is a normal post-spike digestion on **declining volume**, which historically resolves in the direction of the primary trend. The primary trend is up. If you want to see a real distribution top, look at a stock that drops on *rising* volume after a parabolic move where **fundamentals disappoint**. That's not RELY. RELY's fundamentals *accelerated*.

---

## 8. Insider Sales — The Bear's "Top Signal" Is Actually a Tax Formality

The bear keeps hammering the insider sales. Let me be very precise about what actually happened, because this deserves finality:

- Director A exercised **pre-IPO options at $0.64 per share.** When you exercise options, you owe tax on the spread — in this case, roughly $23.59 per share of ordinary income. To pay that tax bill without selling personal assets, directors sell a portion of the exercised shares. This is **boring, standard, universal corporate practice.**
- Director A **retains 261,094 shares PLUS 169,818 options.** Director B retains a **$45.96M position.**
- The sales were **pre-scheduled under Rule 10b5-1 plans**, which are designed precisely to avoid the appearance of trading on material information.

The bear's question — "why not hold the shares and defer the tax bill?" — misunderstands how option exercises work. **You cannot defer the tax bill on an exercise.** The tax is due in the year of exercise, regardless of whether you sell or hold. Selling to cover the tax is not a statement about the stock; it's a statement about liquidity.

Now, compare that to what *buyers* are doing: the **company repurchased $65.2M of stock in H1 2026** — including $42.5M in Q1, before the Q2 earnings run-up. Management spent real corporate cash to buy stock at lower prices than today. Who has better information about RELY's prospects? A director managing personal taxes, or a management team that just raised guidance and launched a major new product?

---

## 9. The Macro "Tail Risks" — Let's Apply the Bear's Logic Consistently

The bear's macro case is: rates are high, dollar is strong, Hormuz is a live threat.

Here's what the bear leaves out:

- **The market has known about high rates for months.** The Fed has been at 3.63% since May, and the 10-year has been above 4.5% for weeks. RELY went from $12 to $24 *during this exact rate environment*. The "high-for-longer" risk is not new information; it's priced in.
- **RELY is a net beneficiary of high rates.** With $676M cash and only $38M debt, the company earns interest income. At a ~4% yield on cash, that's ~$27M of annual interest income — free money that flows to the bottom line.
- **The dollar is actually drifting lower**, from 120.8 to 119.06 over the past few weeks. The bear cites a "historically strong dollar" — but the trend over the last month is downward, which is modestly positive for recipient purchasing power.
- **Unemployment is 4.1% and falling.** This is the single most important macro variable for remittance demand. Immigrant workers are employed, earning, and sending money home. The labor market directly feeds RELY's top line.

Yes, Hormuz is a risk. I've conceded that from the beginning. But at 18% odds of US-Iran invasion and 8% odds of recession, the probability-weighted macro picture is *constructive*. The bear is asking you to price the 18% tail risk as if it's the base case while simultaneously telling you to ignore the 92% probability of no recession and the 86% probability of high rates that RELY benefits from. That's not analysis — that's cherry-picking.

---

## 10. The Fundamental Question the Bear Refuses to Answer

Here's what I want the audience to take away from this debate. The bear has spent hours telling you:

- The growth rate is decelerating (true, on a percentage basis, from an explosive base)
- The earnings beat is flattered by a tax benefit (true, but only partially)
- The stock is expensive (true, if you ignore the cash pile, the growth, the margins, and the buybacks)
- The technicals are weak (debatable, and the evidence is actually mixed-to-positive)
- The card is unproven (true — that's what makes it optionality)

But here's what the bear **cannot answer**: What would have to be true for RELY to be a good investment at this price?

The company is:

- Growing revenue 20% at scale ($1.81B annualized)
- Expanding gross margins to 62.1%
- Growing operating income 4.6x year-over-year
- Generating $406M of operating cash flow TTM
- Holding $638M of net cash
- Buying back stock
- Launching new products
- Operating in a $900B+ market with structural tailwinds
- Trading at ~20x forward clean earnings

If that's not a buy, what is? Would the bear prefer to buy RELY at $30 after the card generates its first $50M of revenue? At $35 after the market recognizes the banking optionality? Is the bear's only acceptable entry price at the 200-day SMA of $17.73 — which would require a **fundamental deterioration** that the bear's own data doesn't support?

That's not an investment framework. That's a hope that the market crashes so you can buy a quality company at a discount. It might happen. It might not. But waiting for a price that requires bad news doesn't make you smart — it makes you uninvested in a company that just proved it can compound.

---

## The Final Verdict

| Bear Claim | Reality |
|---|---|
| "Decelerating from 44% to 20%" | Adding $360M/yr of incremental revenue at 62% GM; operating income up 4.6x |
| "Tax benefit is the entire beat" | Pre-tax income was $64.6M; OCF was $134.6M; clean run-rate EPS power is $1.00+ |
| "30x clean P/E" | ~20x forward clean earnings; 15x forward reported; 13.6x FCF |
| "Card is me-too" | 10M-customer distribution + 30% y/y GM expansion + un-modeled optionality |
| "SBC dilutes" | Post-SBC FCF of ~$220M; buyback accelerating; only 5% cumulative dilution |
| "Volatility is a trap" | ATR elevated after catalyst; RSI 54; trend structure across all timeframes is up |
| "Failed breakout" | Price above all major averages; pullback on declining volume; MACD positive |
| "Insider selling" | $0.64 strike pre-IPO option exercise; 10b5-1 plan; retained millions; company buying back |
| "Macro headwinds" | Labor market strong; dollar softening; rates already priced; net cash beneficiary |

**I'm buying RELY at $24.23.** I'm adding on dips toward $22–23. I'm holding through the volatility because I'm investing in the next twelve quarters, not the last twelve minutes.

This is a profitable, self-funding, 20%+ grower with a fortress balance sheet, expanding margins, a new product catalyst, and a market that's still pricing it at a discount to its demonstrated earnings power. The bear's story is about what already happened — the 85% run, the tax benefit, the one-time pop. My story is about what happens next: the operating leverage, the card scale-up, the buyback acceleration, and the continued migration of the $900B remittance market to digital rails.

The easy money was made by whoever bought at $12 after the panic. The **durable** money — the kind that compounds for years — starts now, when the market has just begun to understand what this company actually is.

**BUY RELY. The evidence is on the side of the bulls.**
Bull Analyst: # Final Word From the Bull: The Bear Keeps Pricing the Rearview Mirror — I’m Pricing the Road Ahead

**RELY | Remitly Global, Inc. | 2026-08-12 | Price: $24.23 | Verdict: BUY**

The bear’s final case is beautifully written. It’s also the same selective story we’ve heard all debate: tax credit, decelerating percentages, failed breakout, insider sales, and a macro tail risk treated as the base case.

Let’s do this one final time — with the full dataset, not the cherry-picked version.

---

## 1. The Tax Benefit Is Not the Story. The Cash Flow Is.

The bear keeps saying the $0.93 EPS pop was “the entire beat.” Let me put the actual quarter on the table:

| Q2 2026 Metric | Value | Growth |
|---|---|---|
| Revenue | **$495.2M** | **+20.2% YoY** |
| Gross Profit | **$307.3M** | **+26.5% YoY** |
| Operating Income | **$66.7M** | **+357% YoY** |
| Adjusted EBITDA | **$115M** | **Record; 23% margin** |
| Operating Cash Flow | **$134.6M** | Strongly positive |

Yes, net income included a $141M non-cash tax benefit. Strip it out entirely. You still have a company that grew revenue 20%, expanded gross margin to 62.1%, grew operating income from $14.6M to $66.7M in a single year, and generated **$134.6M of operating cash flow in one quarter**.

The bear says the market only bought the headline EPS. But the cash flow statement doesn’t lie: **$134.6M of quarterly operating cash flow** is not an accounting artifact. That’s real money from a real business.

And here’s the math the bear refuses to do:

- FY2026 revenue guidance midpoint: **~$1.983B**
- At Q2’s operating margin of ~13.5%, that’s **~$267M of operating income**
- Add ~$27M of interest income on $676M of cash
- Normalize for taxes, and the company has **~$1.00+ of forward earnings power per share**

At $24.23, that’s **~20–24x forward clean earnings** — not 32x trailing clean earnings. The bear is using a trailing P/E at an earnings inflection point. That’s how you miss turnarounds.

---

## 2. “Growth Is Decelerating” — No, It’s Normalizing at a Very High Level

The bear shows: 44% → 34% → 29% → 20%. Then he stops.

Let’s add the next chapter:

- Q3 2025 revenue: **$419.5M**
- Q3 2026 guidance: **~$506M**
- Implied Q3 YoY growth: **~20.6%**

So the business is not collapsing into mid-teens growth. It is **holding 20%+ growth at a nearly $2B revenue base**. The full-year guidance midpoint of $1.983B vs. FY2025’s $1.635B implies **~21% growth for the full year**.

And the absolute dollar story is staggering:

- FY2023 added **$290.7M** in revenue
- FY2024 added **$319.7M**
- FY2025 added **$371.1M**
- Q2 2026 alone added **$83.3M YoY**

The bear wants you to be frightened by a percentage declining from 44% to 20% while the company adds more revenue in absolute dollars every single year. That’s not deterioration. That’s a company scaling from $653M to $1.8B in revenue and still compounding.

Now the bottom line operating leverage:

- Q2 2025 operating income: $14.6M
- Q2 2026 operating income: $66.7M
- Incremental margin YoY: **$52.1M / $83.3M = 62.6%**

That is what operating leverage looks like. The bear calls that “deceleration.” I call it the most beautiful word in finance: **compounding**.

---

## 3. The “Clean P/E Is 32x” Scare — Let’s Use Forward Earnings, Not a Trailing Tape

The bear’s signature move is computing a “clean” P/E on trailing earnings that include the low-profit quarters of 2025.

Here’s why that’s wrong:

- Trailing clean EPS includes Q3 2025 EPS of $0.04 and Q4 2025 EPS of $0.19
- The company has since inflected: Q1 2026 and Q2 2026 are both materially profitable
- Guidance is higher, margin is expanding, and the card launch is ahead

The right way to value an inflection stock is on **forward normalized earnings power**:

- Forward normalized EPS: **~$1.00–$1.20**
- Forward P/E at $24.23: **~20–24x**
- PEG ratio with 20% growth: **~1.0–1.2**

That is not “priced for perfection.” That is a reasonable price for a 20% grower with 62% gross margins, $638M of net cash, and a newly launched product category.

And even the bear’s beloved SBC-adjusted FCF math isn’t scary:

- TTM FCF: **$375.1M**
- TTM SBC: **$155.1M**
- Post-SBC FCF: **~$220M**
- EV: **~$4.46B**
- EV / Post-SBC FCF: **~20x**

A 20% revenue grower with 62% gross margins at 20x post-SBC free cash flow is not a bubble. It’s a quality growth stock at a fair multiple.

---

## 4. The Global Card Is Not Priced In — That’s the Point

The bear says the card has “zero revenue, zero adoption data.” Correct. It launched **one week ago**.

But here’s what the bear refuses to acknowledge: **the market is not paying for the card.** At 15x forward reported earnings, the market is paying for the core remittance business. The Global Card, the AI push, the small-business initiative, the recipient-side services — all of that is **un-modeled optionality**.

If the card works, it’s a new growth leg.
If the card takes time, the core business still grows 20% with rising margins.
If the card fails, you haven’t lost anything — because you never paid for it in the valuation.

The bear calls it a “me-too” product. The more accurate description: Remitly is layering a global banking product on top of **10 million existing, high-frequency customers** who already trust the brand with their international money movement. Cross-selling to an existing engaged base is a far cheaper and more powerful distribution advantage than cold acquisition.

And don’t forget: **Western Union’s 13.5% dividend yield is the market telling you the legacy model is dying.** Remitly is the one taking share.

---

## 5. The Technical Setup — Not a “Failed Breakout”

The bear’s technical narrative is “failed breakout, negative momentum, asymmetric risk.”

Here’s what the actual tape says as of August 12, 2026:

- **Price: $24.23** — above the 10 EMA ($23.96), above the 50 SMA ($22.34), above the 200 SMA ($17.73)
- **Trend alignment:** 10 EMA > 50 SMA > 200 SMA, all rising
- **RSI: 54.06** — neutral, not overbought, not rolling over
- **MACD: +0.38** — still positive
- **MACD histogram: −0.05** — negative but flattening from −0.066 to −0.052, early sign of stabilization
- **Volume:** Pullback days were 4.3M → 3.0M → 3.2M — progressively **lighter**, not heavy distribution

Let’s define a failed breakout correctly: a failed breakout is when a stock breaks out on huge volume, then **closes back below the breakout range**.

What actually happened? RELY broke out on August 6, pulled back, and **held well above the pre-earnings level around $22.50**. The August 12 close of $24.23 reclaimed the 10 EMA and closed above the VWMA of $24.08. That is not a failed breakout. That is a healthy post-earnings consolidation.

And on risk/reward:

- Downside to the 50 SMA at $22.34: **~8%**
- Upside to the August 6 high at $27.15: **~12%**
- Upside to Barron’s 35% target (~$32.70): **~35%**

If you use a rational trend-following stop below the $22.30–22.50 support zone, the asymmetry in favor of the buyer is roughly **4:1** over a 12-month horizon. The bear’s “27% downside” uses the 200-day SMA — a level you only reach if the fundamental trend breaks. That’s not a stop; that’s a nightmare scenario.

---

## 6. Insider Sales — Still Not the Signal the Bear Thinks It Is

Let’s settle this once and for all:

- A director exercised pre-IPO options at **$0.64/share**.
- The tax bill on that exercise is due **in the year of exercise**, regardless of whether the shares are sold.
- Selling a portion of the exercised shares to cover the tax is standard, unremarkable corporate practice.
- After the sale, the director **retains 261,094 shares plus 169,818 options**.
- Another director’s sale leaves a **$45.96M position intact**.

Meanwhile, what did the **company** do?

- It bought back **~$65.2M of stock in H1 2026**
- It raised guidance
- It launched a major new product
- It generated record EBITDA

Management is putting real corporate cash behind the stock. That signal matters far more than a director’s routine 10b5-1 tax-cover sale.

---

## 7. Macro — The Bear’s “Headwinds” Are Already Priced, and Some Are Tailwinds

- **Rates:** High-for-longer is fully priced. And with $676M cash and only $38M debt, RELY is a **net beneficiary** of higher rates, earning interest income on its cash pile.
- **Dollar:** The broad dollar index has actually drifted **lower** from ~120.8 in late July to ~119.06 in early August. The trend is not a strengthening dollar.
- **Labor market:** Unemployment is **4.1% and falling**. That is the single biggest driver of remittance send volumes. Immigrant workers have jobs and income.
- **Recession odds:** The prediction market puts U.S. recession odds at just **8%**.
- **VIX:** 15.28 and falling — calm risk appetite.

Yes, Hormuz and Iran is a live geopolitical risk. I’ve conceded that all along. But the base case is not an 18% invasion probability — it’s a 92% no-recession, calm-labor-market, 20% grower with net cash and a fortress balance sheet. You don’t refuse to buy quality companies because tail risks exist. You size positions accordingly — which is exactly what ATR-based risk management does.

---

## 8. The Bear’s “Contrarian Nightmare” Is Actually a Data Gap, Not a Sell Signal

The bear points to StockTwits 53% bullish / 0% bearish and says “euphoria.”

Let’s be precise: that’s a sample of **30 messages**, with **14 unlabeled**. That’s not a mania. That’s a thin data set.

And Reddit silence? The bear treats “no Reddit posts” as evidence that the story is fully priced. But earlier in the debate, the same absence of Reddit was called “a genuine data limitation.” You can’t use a data gap as a bearish indicator when it’s convenient and dismiss it as a data gap when it isn’t.

The reality is that RELY has a wall of worry — it’s called this entire bear case. The stock has already survived an earnings crash, an 85% run, insider-sale headlines, and a geopolitical spike. And it’s still trading above all major moving averages.

---

## The Final Question

The bear asks: “What has to go right for RELY to go up from here?”

Answer: **What is already going right.**

- Revenue growing 20% on a $1.8B base
- Q3 guidance implies ~20.6% YoY growth
- Gross margins expanding to 62.1%
- Operating income up 357% YoY
- Record EBITDA at 23% margin
- $375M TTM free cash flow
- $638M net cash
- Active buybacks
- 10 million customers
- A brand-new product catalyst that isn’t in the numbers yet

The bear’s demand for 25–30% growth acceleration is not an investment framework — it’s moving the goalposts. At $1.8B of revenue, a 20% organic grower with 62% gross margins and $638M net cash is a rare asset. The market is giving you the chance to own it at roughly 20x forward clean earnings.

**My recommendation remains: BUY RELY at $24.23. Add on weakness toward $22–23. Define risk below $22.30. And let operating leverage compound.**

The bear can keep the story. I’ll take the balance sheet, the cash flow, the guidance, and the trend. The evidence is on the bull’s side.
Bull Analyst: # The Bull's Closing Statement: The Bear Just Proved Our Point — This Is Priced for Doubt, Not for Perfection

The bear's final rebuttal is genuinely impressive. I'll give credit where it's due — that section on "the market has already rejected the growth narrative" was a **smart new angle**. The "15x to 20-24x" catch was sharp. And the repeated emphasis on the clean multiple is a fair discipline.

But here's the issue. **The bear's own final argument actually concedes the bull's entire thesis — he just doesn't realize it.** Let me show you, because this is where the debate finally gets settled.

---

## 1. Let's Address the "Gotcha" on the Multiple — Then Flip It

The bear is pointing to my "15x → 20-24x" journey as a concession. He says: "The bull quietly abandoned the anchor. Now he's at 20-24x forward clean earnings."

Fair catch. Let me be crystal clear about what those numbers actually represent:

- **15x forward** = the analyst consensus reported forward EPS of $1.62, which **includes** modeling for continued strong profitability going forward
- **20-24x forward clean** = the multiple if you **completely zero out** any future tax benefits and strip out the one-time item entirely — my conservative, "show-me-the-underlying-earnings" estimate

Here's the thing: both of these frames are **reasonable** for a company growing revenue 20% with 62% gross margins, $638M net cash, and a $900B market opportunity. Even the bear's harshest math — 32x trailing clean earnings — is a **trailing** number that includes Q3 2025's EPS of $0.04 and Q4 2025's EPS of $0.19, from *before* the company hit full operating leverage.

So the bear "caught" me walking back from 15x to 20-24x. But the real takeaway is: **even in the most conservative, strip-everything-out, assume-no-future-benefit scenario, you're paying roughly the S&P 500's market multiple for a business that's growing revenue 4x faster, expanding gross margins, and holding a net cash fortress.**

That's not a concession. That's a conclusion.

---

## 2. The "Market Has Rejected RELY" Argument — The Bear's Best Shot, and It Misses

The bear says: "On January 2, 2025, RELY closed at $22.40. Today it trades at $24.23. That's an 8% gain — while the company grew revenue more than 40% in the same period. The market has already rejected this story."

Let me tell you what actually happened in that window, because the bear is conveniently skipping the most important chapter.

In November 2025, the stock crashed from ~$16.40 to **$12.31** on an earnings print. Then, over the following months, it did this:

- Recovered from $12.31 all the way to **$27.15** in early August 2026
- That's a **+120% recovery** off the bottom
- And it's now trading at **$24.23** — still well above the January 2025 starting point

So which is it, bear? Is the problem that the market "rejected the story" — or is the problem that the stock went **from $12.31 to $24.23 in nine months** and you just don't like the price you'd have to pay today?

Because here's the critical context you're omitting: **January 2025's $22.40 price was pricing a loss-making company.** The company lost $37M in 2024. It was a story about growth at any cost. The market correctly de-rated it when growth slowed and losses persisted.

**Today, the exact same stock is a different company:** GAAP profitable, generating $406M in operating cash flow, holding $676M in cash, buying back stock, beating estimates, and launching new products.

The fact that the price is *only* at $24.23 — having fully recovered and exceeded pre-crash levels while the business transformed from cash-burning to cash-generating — is not evidence the market "rejected" the story.

**It's evidence the market hasn't fully caught up to the transformation yet.**

The stock is up 85% YTD. But look at the fundamentals: the company went from a net loss to $305M in TTM net income — a swing of over **$340M** — and the market cap is only $5.1B. When the market price doesn't fully reflect a fundamentally transformed company, that's not a "rejection." That's an **opportunity**.

---

## 3. The Bear Just Gave Us the Bull's Best Technical Argument

Here's what the bear wrote in his final round:

> *"The 200-day SMA is less than three ATRs away... The distance is 2.1 ATRs at $1.20/ATR — that's two bad weeks away."*

Wait — he's arguing that a stock trading **$6.50 above its 200-day moving average** — a 200-day that has **risen from $16.50 to $17.73 over the last two months** — is dangerous?

Let me put this in plain English. A rising 200-day that is being lapped by price at +36.7% isn't a "stretched rubber band." It's what every sustained uptrend looks like. Stocks in strong trends routinely trade 30-50% above their 200-day. That's not a sell signal — that's the **definition of a stock in a primary uptrend**.

And here's the part that really matters for risk/reward. The bear has spent four rounds telling you:

1. The stock is going to crash (downside to $17.73 = -27%)
2. But the 200-day is "2.1 ATRs away" — so it could get there in two bad weeks
3. But also, the 50-day at $22.34 is the "last line of defense"
4. But also, support at $22-22.5 is solid confluence

So which is it? Is the crash imminent because the stock is stretched, or is the stock going to find support at $22.34 (which is only 8% away) because that's a strong confluence zone?

Here's an honest framing the bear won't give you:

- **Downside risk (to the 50-day): -8%**
- **Upside to the August 6 high ($27.15): +12%**
- **Upside to Barron's $32.70 target: +35%**
- **Upside to fair value at 25x clean forward EPS ($1.10): $27.50 — and that's *before* any card contribution**

With a defined stop below $22.30, you're risking $1.93 to make $3-8. That's a **2:1 to 4:1 asymmetric setup** in the buyer's favor. The bear keeps repeating "downside to the 200-day is 27%" as if that's the base case. But you only reach the 200-day if the revenue growth re-accelerates AND the company craters — a thesis-breaking scenario. We don't invest in thesis-breaking scenarios; we stop out before them.

**The base case for RELY is: a 20% grower at a reasonable multiple, digesting a post-earnings spike, with fundamentals and trend both pointing up.**

---

## 4. The SBC "Round Trip" — Let's Kill This Once and For All

The bear's math: $65.2M buybacks vs $62M SBC in H1 2026 = "net share reduction of $3M — that's optics management."

Let me tell you what that $65.2M actually is:

**The first ten months of a brand-new buyback program.** The company initiated buybacks in Q4 2025. In H2 2025, it bought back $23.9M. In Q1 2026, $42.5M. In Q2 2026, $22.7M. That's a **173% increase in quarterly buyback pace from H2 2025 to H1 2026.**

The bear wants you to believe this is "maintenance." But what does the actual evidence show?

- The company has **$676M of cash** — nearly doubled from $368M at end of 2024
- It's growing the buyback **as profits grow**
- It generated **$375M of TTM FCF** — meaning the buyback is fully self-funded
- Management has guided revenue higher, launched a major new product, and is now deploying capital

The bear is describing what the buyback *isn't* today while ignoring what it *will* be: a company with $375M in annual FCF, trading at near 52-week highs, with accelerating buybacks, is in the **beginning of a capital-return story**, not the end.

And the dilution argument? Let's use the facts:

- Basic shares: ~210.3M
- Diluted shares: ~221M
- **Cumulative dilution over the company's entire history: ~5%**

That's *incredibly* disciplined for a fintech that grew from $653M to $1.8B in revenue. Most high-growth tech companies have diluted 15-25% over the same trajectory. And now the buyback is accelerating to offset it.

---

## 5. The Global Card: The Bear Asks "Why Didn't Management Guide With It?" — Here's the Answer

The bear's challenge: *"If the card were truly a game-changer, wouldn't management have guided with it? They didn't. Q3 guidance was in line. That tells you everything."*

Actually, it tells you exactly what a disciplined management team would do: **set guidance you can beat.**

Let's look at what Remitly actually did:

- **Q2 2026:** Beat revenue by 2.19%, beat EPS by 269%, reported record $115M EBITDA
- **FY2026 guidance:** **Raised** to $1.978-1.988B
- **Q3 guidance:** $506M — **in line with consensus**

Management beat the quarter, raised the year, and guided the next quarter in line. Then they launched a product that opens a $900B remittance TAM into consumer banking.

The bear sees "in line" and calls it a failure. I see "in line" and recognize it as **the setup for the next beat-and-raise.** This is how disciplined management teams operate. They set a beatable bar.

And let's be clear about what the card isn't: it's not a hedge-fund-style "story." It's a **distribution advantage**. Remitly has 10 million active customers who already send money through its rails. Cross-selling a card to that base costs a fraction of what Wise or Revolut spend on cold acquisition. The card isn't a "me-too" product. It's a **relationship expansion** with customers who already trust the brand.

---

## 6. The Bear's Macro Crisis Is Literally Improving In Real Time

The bear repeats: "10-year at 4.70% — long-duration assets at risk." "Dollar historically strong." "Hormuz is live."

Let me check the actual data from August 2026:

- **Unemployment: 4.1% and falling** — the core remittance-sender demographic is steadily employed
- **Inflation: cooling** — CPI down over the quarter, core PCE benign
- **VIX: 15.28, down 11% month-over-month** — the anxiety is literally declining
- **Recession odds: 8%** — a 92% chance the demand backdrop holds
- **Dollar: drifting lower** from ~120.8 to ~119.06 — modestly supportive, not a headwind
- **Rates:** RELY has $676M in cash and $38M in debt — a net beneficiary

The one real risk — Hormuz/Iran — is live, but the market has known about it for weeks and RELY has held its gains above the 50-day. At a 0.34 beta with a net cash balance sheet, RELY is structurally better positioned than the average high-multiple growth stock to absorb macro shocks.

---

## 7. The Bear Keeps Demanding Perfection — But the Stock Is Priced for Doubt, Not for Perfection

This is the most important reframe of all.

The bear says: "RELY is priced for perfection."

Let me test that claim. What is the market actually pricing right now?

- Revenue growth of ~20% — the company is already delivering that
- Gross margin of ~62% — already achieved
- Operating margin of ~13.5% — already achieved in Q2
- GAAP profitability — already achieved in FY2025
- Better-than-expected Q3 — **the stock's price does NOT depend on this.** Even if Q3 comes in exactly at guide, annualized clean earnings are still $1.00+, supporting the current price.

For this stock to crash to the 200-day, the market would need to believe:
- Growth collapses below 15%
- Gross margins compress
- The card fails *and* the core business deteriorates
- A global macro shock hits

That's not "perfection." **That's requiring a perfect storm of negatives.**

Meanwhile, what does the bull need for the stock to work?

- The core remittance business to keep growing 20% — **already happening**
- Margins to keep expanding — **already happening over four consecutive quarters**
- The card to contribute *something* — just one year of card revenue at even $50M would exceed what the market is paying for
- The buyback to continue — management is already doing it

Now tell me: whose case requires more perfection?

---

## 8. Let's Be Honest About What the Bear Is Actually Arguing

The bear keeps saying "great company, wrong price." Here's what that really means: he wants to buy RELY at the 200-day of $17.73 — a price that would imply:

- **Zero growth in earnings power from today**
- **A business that somehow doesn't deserve a premium to the market**
- **A 73% drawdown from the August high** — which would require a *fundamental catastrophe* for a company with record EBITDA, a beat-and-raise quarter, and 10M customers

That's not "waiting for a margin of safety." That's **waiting for a gift that isn't coming** — because the fundamentals are improving faster than the market is fully appreciating.

And here's the worst part of the bear's advice: **he's telling you to wait for a company that is "good" but "too expensive" — but at what point does he say buy?**

At 20x forward clean earnings? That's $22-23 — the stock is already there. At 18x? That's $20 — would require a growth scare. At 15x? That's $16.50 — would require the exact fundamental deterioration the bear's own data doesn't support.

The bear isn't running a framework. He's running a **hope for a crash.**

---

## The Bottom Line

After four rounds, here's where we are:

The bear's case rests on:
1. A tax benefit that doesn't affect cash flows
2. A growth rate percentage that ignores the absolute dollars scaling
3. A trailing clean multiple that ignores the forward earnings power
4. A card with no revenue — that the market isn't paying for anyway
5. A technical setup where the stock is actually above all major moving averages
6. Insider sales that are routine option exercises, while management buys back stock
7. A macro environment where the labor market is strong, inflation is cooling, and the VIX is falling
8. A "rejection" that is really just a recovery off a crash

My case rests on:
1. **Revenue growing 20% at a $1.8B scale**
2. **Operating income up 357% year-over-year**
3. **Gross margin at 62.1% and expanding**
4. **$375M TTM free cash flow**
5. **$638M net cash**
6. **Record EBITDA at a 23% margin**
7. **Raised FY2026 guidance**
8. **A new product catalyst that's entirely unmodeled**
9. **10 million active customers**
10. **A stock trading at roughly 20x forward clean earnings — approximately the market multiple — for a business growing 4x faster with a fortress balance sheet**

The bear keeps asking "what has to go right?" I'll answer with something more important: **what has to go wrong for the bear to be right?**

The stock would need to:
- Deliver terrible Q3 results (against a guide that's already set at a beatable level)
- See competitors steal share (despite four consecutive quarters of margin expansion and 10M+ users)
- Face a fundamental macro collapse (despite 8% recession odds)
- See insiders dump *entire* positions (not routine $0.64 option exercises)
- Have the market revalue the stock at lower multiples (despite consistent beats, raises, and a transforming business)

That's the definition of a "hope for the worst" investment framework.

**My recommendation remains: BUY RELY at $24.23. Add on any dip toward $22-23. Set your stop below $22.30 if you're trading. And if you're investing, hold through the volatility and let a 20% revenue grower with 62% gross margins and $638 million net cash compound.**

The bear can have the story. I'll take the balance sheet, the cash flow, the trend, and the compounding.

**BUY RELY.** The evidence is on the bull's side — now and after every single round of this debate.

### Bear

Bear Analyst: # The Bear Case for RELY: You're Buying a Decelerating Business at a Premium Multiple — Not an Inflection

---

**Analysis Date: 2026-08-12 | Ticker: RELY (Remitly Global, Inc.)**

---

I appreciate the thoroughness of the bull case. Truly. It’s the kind of pitch that makes you want to believe. But when I look at RELY, I don’t see a "compounder at the beginning of a margin expansion story." I see a **decelerating business that just reported a massive one-time tax benefit**, and the market is being asked to pay a premium multiple for a growth trajectory that is *slowing*, not accelerating.

The bull’s job is to tell you the story. My job is to show you the math. Let’s go through it point by point.

---

## 1. The Bull Says "Growth+" — The Data Says "Deceleration"

The bull shows you revenue growth of 44%, 34%, 29%, and then conveniently stops at "+20.2% YoY" as if that’s the exciting part. Let me put that trajectory in front of you without the spin:

| Year | YoY Growth | Signal |
|---|---|---|
| 2023 | +44.5% | Peak hype |
| 2024 | +33.9% | Decelerating |
| 2025 | +29.4% | Further deceleration |
| Q2 2026 | **+20.2%** | **Sharpest slowdown in company history** |

That is not "escape velocity." That is a company that has **cut its growth rate in half in three years**. The bull calls this a "mature compounder." I call it a **mature business losing its growth premium**.

The bull says, "The run from $12 to $24 was repricing a profitability inflection." I agree. But the *new* information is that **growth is now sub-20% trajectory**. This is precisely when the market re-rates a stock from "growth at a reasonable price" to "value with a growth problem." A stock priced at 15x forward earnings for 20% growth is only justified if that 20% is *accelerating*. It isn't. It's decelerating. The premium multiple is at risk the moment the next quarter shows 18%.

---

## 2. The Tax Benefit Is Not a "Gotcha" — It Is the Entire Earnings Story

The bull's most audacious claim is that the tax benefit is "the market's most conservative validation that the earnings turnaround is real." That is a heck of a spin. Let's look at the facts:

- **Q2 2026 net income: $205.9M**
- **Q2 2026 pre-tax income: $64.6M**
- **Q2 2026 tax provision: −$141.3M (a GAAP tax *benefit*)**

A $141M *negative* tax provision on a $64.6M pre-tax profit is not "conservative validation." **It is an accounting artifact.** It means that in the quarter, Remitly's tax bill was **negative $141M** — the company *received* a benefit equivalent to **more than twice its entire pre-tax earnings**.

Strip it out, and what do you get?

- Q2 2026 clean EPS: ~$0.25 (not $0.93)
- TTM clean EPS: ~$0.75–0.80 (not $1.39)
- Clean PE at $24.23: **~30x**, not 17.4x
- Clean Forward PE: **still ~25–30x** on an *optimistic* 2027 estimate

You are paying 30x clean earnings for a business growing revenue at 20% and *decelerating*. That is not "reasonable." It is **expensive**.

The bull will tell you to ignore the tax benefit. The problem is: **the market did not ignore it.** The stock popped 8% on the back of a "$0.93 EPS beat." The entire advance on August 6 was driven by an accounting artifact, not operational acceleration. When the market realizes the clean number is $0.25, the multiple re-rates violently.

---

## 3. The "Rising Gross Margin" Myth: It's Not Pricing Power, It's Mix Shift and Cost-Cutting

The bull says, "Gross margin is expanding from 59% to 62.1% — that's pricing power!" Let me ask a different question: **At what cost to volume growth?**

If your gross margin is expanding while your **growth rate is halving**, you are not displaying pricing power. You are displaying a business that is **milking its existing high-margin corridors** while losing share in lower-margin, higher-volume segments. That is not a moat. That is a **harvest strategy**.

The bull says, "Western Union's 13.5% dividend yield is a distress signal." That's a classic distraction. WU's gross margin is irrelevant here. What matters is that **Remitly's core product is a commodity — moving money**. Wise, MoneyGram, PayPal, and Zepz offer same-day, cross-border transfers at near-zero marginal cost. The fee war is not over; it's just entering its *most brutal phase*.

The Global Card is not a competitive moat. **It is a me-too product.** Wise already has a multi-currency card. Revolut has a full banking stack. Nubank, Mercado Pago, and a dozen neobanks in Latin America, Africa, and Asia are doing this *better* with *local* regulatory licenses. Remitly is late to a party where the host already has a 15-year head start.

---

## 4. The "Fortress" Balance Sheet Is a Sign of Capital Stagnation, Not Strength

The bull is impressed by $676M cash and $38M debt. I'm not. For a company with a "$900B TAM" and "asset-light software model," sitting on $676M in cash is a **statement of no investment opportunities**.

Why would a "disruptor" growing at 20% have **$375M of annual free cash flow** and **not be reinvesting it aggressively**? Why is it returning $65M to shareholders via buybacks instead of pouring money into the Global Card rollout, or acquiring smaller remittance players, or expanding into new corridors?

Let me tell you why: **Management sees the same deceleration I do.** They don't have high-ROI projects to fund. The buyback is not "conviction"; it is the *default* when you have nothing better to do with the cash. And they're doing it at **near 52-week highs** — the worst possible time to deploy capital for long-term shareholders.

The bull calls this "shareholder-friendly." I call it **poor capital allocation at an expensive price**.

---

## 5. The "0.34 Beta" Fallacy: This is Not a Low-Risk Stock

The bull repeats the 0.34 beta like a mantra. That beta is a **historical artifact of a stock that has been in a *declining trend* for three years until recently**. Beta is backward-looking, and it is measuring the *last* bull market, not the *next* one.

Look at the actual **current volatility**:

- ATR: **$1.20**, which is ~4.9% of price. That is **massive** for a stock trading at $24. The average daily range is larger than the annual dividend yield of the S&P 500.
- In the last 7 days, RELY swung from an **intraday high of $27.15 to a close of $23.14** — a **\~$4.00 round trip**, nearly **15%** in a single week.
- The stock is trading **36.7% above its 200-day moving average**. In a normal distribution, that is a **stretched rubber band** that snaps violently.

This is not a low-vol stock. It's a **high-beta growth name disguised as a sleepy fintech**. When the market sells off 2%, RELY will fall 5-6%, not 0.34×the market. The low beta is a trap for risk-averse investors.

---

## 6. The Macro Tailwinds Are Fading — and One Geopolitical Headline is a Catastrophic Tail Risk

Let's concede the bull's macro points: unemployment is 4.1%, inflation is cooling, the VIX is low, and recession odds are only 8%. Fine. But here's what the bull conveniently ignores:

- **Fed funds at 3.63%, 10Y at 4.70%, and 86% odds of ZERO cuts in 2026.** High-for-longer rates compress the present value of *every* long-duration asset, especially a 30x clean earnings company.
- **Dollar at ~119**: The bull calls a stable dollar "neutral." A *strong* dollar is actually a **headwind** for remittance demand. When the dollar is strong, it takes *more* local currency to send the same amount home. It discourages senders and reduces recipients' purchasing power. This is not neutral; it's a **slow bleed** for the industry.
- **Hormuz / Iran:** The bull dismisses this as "18% invasion odds." But look closer: **the odds of Hormuz traffic being normal by Aug 31 dropped to 3%**. Shipping is already disrupted *right now*. The risk is not "invasion"; it is *continued escalation* of regional instability that spikes oil prices and pressures the **core low-income sender base** that already struggles with cost-of-living inflation. A sudden 20% spike in oil destroys Remitly's volume growth from the exact demographic it depends on.

---

## 7. The Technical "Setup" Is a Top, Not a Base

The bull sees a healthy pullback and a reclaim of the 10 EMA. I see a **blow-off top on August 6 — the classic distribution day**:

- August 6: **Intraday high $27.15, closed $25.93** on 8.4M shares.
- August 7: Closed lower after the spike.
- August 8–10: **Closed $23.14**, down **\~11% from the high in three sessions**.
- August 11: 3.0M shares (declining volume) — **absence of buyers**, not confirmation of a "healthy pullback."
- August 12: Close of $24.23 is a **"dead cat bounce"** back to the 10 EMA, not a resumption.

The MACD histogram is **negative**. The RSI at 54 is neutral *only* because the stock just dropped from 66. This is not a coiled spring; it is a **failing breakout**. The "support zone" of $22.34–$22.01 (50 SMA + Bollinger lower) is **the last line of defense before a catastrophic breakdown** to the $17.73 (200 SMA), which is **26% below current prices**.

If a stock has a **$1.20 ATR**, the distance from $24.23 to $22.00 is **less than two standard deviations** of noise. You are one bad headline away from wiping out months of gains.

---

## 8. Insider Sales Are a Headline *and* a Thesis

The bull says the $0.64 pre-IPO option exercise is "tax planning." I ask: **Why is a director *choosing* to sell at $24 after a record quarter when the stock is 45% below ATH?**

If the company is a "compounder at the beginning of a margin expansion story," why not hold the shares and defer the tax bill for *decades*? The rational answer is: **insiders see the current price as close to fair value or better**. They have the most information. They are selling against a backdrop of *decelerating* growth, a *one-time* earnings beat, and a new product launch that has **zero** revenue contribution yet. That is not a vote of confidence; it is a **diversification event at a local top**.

---

## 9. The Bull's "Best Argument" Is Actually the Worst One

The bull's conclusion — "15x forward earnings for 20% growth is cheap" — rests on **two assumptions that are likely broken**:

1. **The 20% growth is sustainable.** It is not. Q2's +20.2% YoY was a *sequential* acceleration from Q1's +8.2% q/q, but Q3's guide of ~$506M **implies a sharp deceleration to mid-to-high teens growth** in H2 2026. This will not be a market-beating number; it will be a *confirmation* that the growth story is fading.

2. **The tax benefit will not distort the P&L.** It *already* distorted the P&L. Every analyst will adjust Q3 "EPS" down to ~$0.30 or lower. The stock price is **not going to hold 15x a number that is ephemeral**.

---

## The Bear's Rebuttal Table — Direct Answers to the Bull

| **Bull Argument** | **Bear Rebuttal** |
|---|---|
| "Growth + Profitability + Value" | You can't have a "value" multiple when clean PE is 30x. You have a *growth story at a value stock price* — until the story breaks. |
| "Still 45% below ATH" | That is not "upside"; that is **confirmation that the stock had a blow-off top and has been in a 3-year bear market** until this year's relief rally. |
| "Tax benefit validates profitability" | A negative $141M tax provision on $64.6M pre-tax income is **not a validation of operations**. It is a one-time accounting benefit. |
| "Rising gross margins" | They are rising **because growth is slowing**. High-margin existing corridors are being harvested while volume growth fades. |
| "Fortress balance sheet" | A fortress with no investment opportunities **is a warehouse, not a growth engine**. The buyback at 52-week highs is a misallocation of capital. |
| "Low beta = low risk" | A **$1.20 ATR** on a $24 stock is **5% daily volatility**. That is high-risk, not low-beta. |
| "Macro tailwinds" | High-for-longer rates, a strong dollar, and the **live** Hormuz disruption are structural headwinds the bull ignores. |
| "Insider sales are benign" | Insiders are **selling at the peak** after an 85% run — the most historically reliable **top signal** in existence. |
| "Technical setup is bullish" | A **failed breakout at $27.15** followed by a **negative MACD histogram** and declining volume is a **distribution top**, not a base. |

---

## Conclusion: The Math Does Not Support the Stock

Let me be crystal clear. I am not saying Remitly is a bad company. It is a good business with real revenue, real profit, and a real product. But **a good company can be a terrible investment at the wrong price** — and this is the wrong price.

You are being asked to pay:

- **30x clean earnings** for a company whose growth just halved;
- **15x forward earnings** on a number that includes a $141M one-time benefit;
- **~2.5x EV/Revenue** for a business whose growth is *decelerating*;
- **A full premium** for a product (Global Card) that has **zero revenue contribution** and faces entrenched competition;

...all while:

- The **MACD histogram is negative** ($0.38 MACD < $0.43 signal);
- The **stock is 37% above the 200-day SMA** and one ATR away from a test of the 50-day;
- **Insiders are selling** after an 85% run;
- **Geopolitical risk in the Strait of Hormuz is *live*, not hypothetical**.

The bull case is a beautiful narrative about what *could* be. The bear case is a cold, hard look at what *is*. The stock is up 85% YTD, the easy money has been made, and **every negative re-rating catalyst is now in play — a missed quarter, an oil shock, a macro selloff, or simply a market that finally adjusts the multiple for the deceleration it's seeing**.

My recommendation: **DO NOT BUY RELY at current levels. If you hold, take profits. If you're looking for a long entry, wait for the $17–18 zone (200-day SMA) or a clear *acceleration* in growth that doesn't rely on a tax artifact to flatter the P&L.**

This stock is not a gift. It's a **trap for momentum buyers who are late to a narrative that is about to change**. The data is on my side. Let's see who's left holding the bag when the growth scare hits, and the tax benefit is a footnote in the 10-Q.

**The bear case is simple: You are paying for a story that is over, with a P&L that is a mirage.** That is not investing. That is speculation with bad odds. I'll pass.
Bear Analyst: # The Bear Rebuttal: RELY’s “Blowout” Is a Tax Credit, Not a Breakout

I want to start by acknowledging the bull’s case is beautifully constructed. It hits all the emotional notes: “profitability inflection,” “fortress balance sheet,” “un-modeled catalyst.” But my job isn’t to tell you a story. My job is to price the story. And when you price RELY correctly — stripping out the one-time tax benefit, looking at the actual growth trajectory, and weighing the technical risk/reward — this is not a buy. This is a stock where the market is being asked to pay a premium for a narrative that is already in the price.

Let’s go through it.

---

## 1. The Bull’s “Growth Is Fine” Chart Is a Base-Effect Illusion

The bull says revenue growth of 20% on a $1.8B base is actually impressive because absolute dollars added are increasing. That’s true, but it’s also the least useful way to value a stock. Growth *rate* is what drives multiple expansion. And the growth rate has done this:

| Period | Revenue Growth |
|---|---|
| FY2023 | +44.5% |
| FY2024 | +33.9% |
| FY2025 | +29.4% |
| Q2 2026 | +20.2% |

That is not a company “accelerating.” That is a company that has **cut its growth rate by more than half in three years**. The bull can dress that up with absolute dollar math, but the market does not pay 30x clean earnings for a decelerating top line. It pays that multiple for *acceleration*. RELY is not accelerating. It is holding at 20% — and 20% growth with a 30x clean P/E is a very different proposition than 20% growth with a 15x forward P/E.

And here’s the kicker: the stock itself proves the point. At the start of this dataset in January 2025, RELY closed at **$22.40**. Today it’s **$24.23**. That’s roughly **+8%** — while revenue grew over 40% in that period. The market has already de-rated this growth story once. It can do it again.

---

## 2. The Tax Benefit Is Not a “Validation” — It *Is* the Beat

The bull says the $141M tax benefit should be celebrated because GAAP only allows it if earnings are durable. Let’s be clear about what happened:

- Q2 2026 pre-tax income: **$64.6M**
- Q2 2026 tax provision: **−$141.3M**
- Q2 2026 reported net income: **$205.9M**
- Reported EPS: **$0.93**

If you assume a normal tax rate on that $64.6M pre-tax profit, clean Q2 EPS is roughly **$0.22–0.24** — essentially **the same as Q1 2026’s $0.23**. The “blowout quarter” was, on a clean operational basis, **flat** with the prior quarter. The entire “earnings surprise” was an accounting credit.

Now, the bull says “the tax benefit validates the profitability turnaround.” No. A **negative $141M tax provision** does not validate operations. It is a one-time recognition of accumulated losses. It doesn’t generate cash. It doesn’t repeat. And it has already distorted the market’s perception of this quarter.

Strip it out:

- TTM reported EPS: **$1.39**
- EPS from tax benefit: **~$0.64** ($141M ÷ ~221M diluted shares)
- Clean TTM EPS: **~$0.75**
- Clean P/E at $24.23: **~32x**

So all this talk about “15x forward earnings” is built on a number that includes an accounting artifact. The real multiple is **over 30x clean earnings** for a business growing at 20% and decelerating. That is not a value. That is a premium.

---

## 3. Operating Leverage Is Real, But It’s Priced In

The bull loves the “operating income up 357%” stat. Let’s look at it honestly.

Yes, Q2 operating income of **$66.7M** is a huge improvement from **$14.6M** a year earlier. That *is* real operating leverage. But the market has already paid for it — the stock is up roughly **85% YTD** and **97% from the November 2025 low**. The question is: what is the *next* leg of upside?

The answer from guidance is: more of the same, not more than expected.

- Full-year guidance was raised to **$1.978–1.988B**.
- Q3 guidance of **~$506M** is essentially **in line** with consensus.
- The company did not blow the doors off Q3 guidance. It gave “close to estimates.”

When a stock trades at 30x clean earnings and **the guidance is only in line**, there is no room for error. If Q3 comes in at the low end, or if management merely reiterates rather than raises, the multiple compresses. That is the setup here.

Meanwhile, the “record EBITDA” of $115M is also being used to justify the stock. But at roughly $5.1B market cap, with a clean EV of about $4.5B, the stock trades at **~20x EV/EBITDA** on a record number. For a company growing at 20% and *slowing*, that is not a cheap multiple. It is a full multiple.

---

## 4. The Global Card Is Not a Moat — It’s a Late, Crowded Entry

The bull calls the Remitly Global Card a “re-rating catalyst” and an “un-modeled asset.” Let me translate that: **it has zero revenue contribution, zero proven adoption, and zero evidence it will move the needle.**

The card is a me-too product in one of the most crowded spaces in fintech. Wise has had a multi-currency account and card for years. Revolut has a global banking stack. Nubank, Mercado Pago, and dozens of neobanks already serve the same customer base with local licenses and established products. Remitly is entering that arena **late**, with a 10-million-customer base — respectable, but not dominant. And the card pushes RELY into credit, lending, and banking risk — areas where it has no track record. That’s not a free option. That’s potential capital consumption and regulatory exposure.

The bull says “cross-selling to an existing base is cheaper.” Fine. But cross-selling is not the same as sustainable competitive advantage. Remittance customers are among the most price-sensitive consumers in the world. They will switch for a better fee. That’s why the “moat” argument is weak: money movement is a commodity.

And one more thing: if the card were such a meaningful near-term catalyst, the company would have guided with it. It didn’t. It guided “in line.” That tells you management is not counting on the card to move 2026 numbers.

---

## 5. The “Fortress Balance Sheet” Doesn’t Mean What the Bull Thinks

Let’s concede the numbers:

- Cash: $676.4M
- Debt: $38.3M
- Net cash: ~$638M
- TTM FCF: $375.1M

That’s a solid balance sheet. But a solid balance sheet is **not a reason to overpay for a stock**. The bull also conveniently ignores the quality of that FCF:

- TTM stock-based compensation: **$155.1M**
- TTM FCF after SBC: **~$220M**
- Market cap at $5.1B: **~23x true FCF**

So the “13.6x FCF” headline is misleading. Once you subtract real shareholder dilution, RELY trades at **more than 20x post-SBC FCF**, for a company whose growth rate is falling. And the buybacks the bull brags about? In H1 2026, RELY bought back **$65.2M** of stock — while it issued **$62M** of stock-based comp in the same period. That is not aggressive capital return. That is virtually a wash. The company is not reducing share count meaningfully; it is just offsetting option issuance.

A cash-rich balance sheet is nice. It doesn’t make a 30x clean-earnings multiple cheap.

---

## 6. The Low Beta Is a Trap — The Real Volatility Is Right There

The bull keeps repeating “0.34 beta” as if RELY is a low-risk utility. Look at the actual tape:

- ATR: **$1.20**, roughly **5% of the stock price**.
- One week ago, RELY spiked to **$27.15**, then fell to **$23.14** — a **15% round trip in days**.
- The stock is trading **36.7% above its 200-day SMA**.

That is not low volatility. That is a high-beta growth stock wearing a disguise. Beta is backward-looking; it measured a stock that spent much of its recent history in a crash-and-recovery pattern. The current ATR tells you what you’ll actually experience: **$1-per-day swings are normal.** If you are risk-averse, this is not your stock.

And from a pure risk/reward standpoint, where are you today at $24.23?

- Upside to the August 6 high of $27.15: **+12%**
- Downside to the 50-day SMA at $22.34: **−8%**
- Downside to the 200-day SMA at $17.73: **−27%**

That is an asymmetric setup **against** the buyer. You are risking far more to the downside than you are being paid to the upside. And with a $1.20 ATR, those downside levels are not far away.

---

## 7. Technical “Reclaim” Is Not a Breakout

The bull says the close above the 10 EMA at $23.96 is a sign of stabilization. Let’s put that in context: RELY hit $27.15 on August 6, then immediately reversed. It is now trading **11% below that high**, with:

- MACD below its signal line
- MACD histogram negative
- RSI at 54, down from 66 — momentum rolling over, not building
- Volume on the latest bounce of 3.2M shares, versus 8.4M on the spike

The “declining volume on the pullback” the bull calls healthy? It can also mean **buyers are not stepping in**. In a distribution top, the first spike is on heavy volume, and every attempt to recover is on lighter volume. That is exactly what this tape looks like. This is not a coiled spring. It’s a failed breakout.

---

## 8. Sentiment and Insiders Are Sending the Opposite Signal

The bull points to Barron’s, StockTwits, and “zero bearish” retail sentiment as evidence of bullishness. I see that as a **contrarian warning**.

- StockTwits: 53% labeled bullish, **0% bearish**.
- Barron’s publishes a “35% upside” call after an 85% run.
- Retail is comfortable. There is no wall of worry for this stock to climb — just euphoria.

And then there are the insider sales. The bull calls the $0.64 option exercise “tax planning.” But notice: **the director chose to sell a large portion of shares at $24.23 after a record quarter, after an 85% run, and after the launch of a “transformative” product.** If the story were that good, why not hold? Why not wait for the un-modeled card catalyst to show up? Because insiders know the clean numbers are not as exciting as the headline $0.93 EPS.

The cluster of insider filings after earnings is a known caution flag. The company buybacks don’t erase that — especially when, after SBC, the buyback is barely keeping share count flat.

---

## 9. The Macro Risks Are Live, Not Tail

The bull concedes the Hormuz/Iran risk but calls it an “18% tail risk.” Let’s look at the prediction markets more carefully:

- Odds of Hormuz shipping returning to normal by Aug 31: **3%**
- Odds by Dec 31: **46%**
- Odds of US invasion of Iran before 2027: **18% and rising**

That is not a benign backdrop. The disruption is happening **now**. Oil supply risk is real. For RELY’s core customer — a low-income immigrant sender — an oil spike is a direct hit to disposable income. That is not a theoretical risk; that is a demand-risk to the core business.

Meanwhile, the macro setup the bull calls supportive is actually a mixed bag:

- 10-year Treasury at **4.70%** and 86% odds of **zero Fed cuts** in 2026 → pressure on long-duration equities.
- Fed funds at 3.63% → high-for-longer is not friendly to a 30x clean P/E stock.
- Dollar index near 119 → historically strong; any safe-haven surge in a geopolitical episode will hurt remittance demand and FX revenue.

Yes, unemployment is 4.1% and recession odds are low. But those are already in the price. The tail risks are not.

---

## Bottom Line: Good Company, Wrong Price, No Margin of Safety

Let me be clear: Remitly is not a fraudulent company. It’s a legitimate, growing, newly profitable fintech. That does not make it a buy at $24.23.

What you are actually buying at this price:

- **~32x clean trailing earnings**
- **~20x EV/EBITDA** on a record quarter
- **~23x post-SBC free cash flow**
- A business whose growth has gone from **44% to 20%**
- A Q2 “beat” driven primarily by a one-time tax credit
- A product pivot with zero revenue contribution
- A technical setup with poor risk/reward and negative momentum
- Insider selling after an 85% run
- A live geopolitical tail risk in the Strait of Hormuz

The bull is asking you to ignore the tax benefit, ignore the deceleration, ignore the insider sales, and pay up for an unproven card. That is not investing. That is catching a narrative at the wrong moment.

My recommendation: **Do not buy RELY at current levels. If you own it, take at least partial profits. If you want to own the growth story, wait for a better entry — ideally toward the $17–18 zone near the rising 200-day, or until the company demonstrates clean, ex-tax earnings acceleration that supports the premium multiple.**

Right now, the data says the risk is to the downside. The bull has the story. I’ll take the math.
Bear Analyst: # The Bear's Final Word on RELY: A $5.1 Billion Story Built on a One-Time Tax Credit and Hope

**Ticker: RELY | Date: 2026-08-12 | Price: $24.23 | Verdict: DO NOT BUY**

---

The bull makes a beautiful case. I'll give him that. He's passionate, he's thorough, and he has a remarkable ability to turn a **one-time tax credit into a vote of confidence**, a **decelerating growth rate into a base-effect illusion**, and a **failed breakout into a "healthy consolidation."**

But here's the thing about beautiful narratives: they're most dangerous when they're most convincing. And the bull's story — that this is a "compounder at the beginning of a margin expansion story" — is a narrative that **requires you to ignore the most important facts on the table**.

Let me walk through exactly why, with the full dataset in front of us.

---

## 1. The Tax Benefit Isn't a "Validation" — It's the *Only* Reason This Stock Popped 8%

Here's what actually happened on August 6. The market didn't rally because Remitly's core business *accelerated*. It rallied because the headline number — **$0.93 EPS** — looked like a blowout. Nobody trading that pop read the 10-Q footnote about the deferred tax asset valuation allowance release. They saw "GAAP EPS $0.93" and hit buy.

But here's the real math, one more time:

| Metric | Q2 2026 | The Truth |
|---|---|---|
| Reported Net Income | $205.9M | Includes **−$141.3M tax provision (a benefit)** |
| Pre-Tax Income | $64.6M | The actual operational result |
| Normalized Tax (25%) | ~$16M | What a real company pays |
| **Clean Net Income** | **~$48M** | What the company actually earned |
| Clean EPS | **~$0.22** | **Not $0.93** |

The bull will tell you "pre-tax income grew 4.6x year-over-year!" And it did. But let's be precise about what that means: Q2 2025's pre-tax income was tiny ($14.6M operating income), so the base was nearly zero. Growing from a near-zero base to $64.6M sounds impressive — until you realize that **Q1 2026 already earned $53.7M in operating income**. The sequential improvement from Q1 to Q2 was $13M on $42M of incremental revenue — a **31% incremental margin**, which is fine, but it's not the "escape velocity" the bull is selling.

And here's the kicker: **the stock is priced for the $0.93, not the $0.22.**

At $24.23:

- **Clean TTM P/E: ~32x**
- **Forward clean P/E (using the bull's own $1.00–$1.20 estimate): ~20–24x**

The bull says "20x forward clean earnings is reasonable for a 20% grower." Let me ask: **since when does a company whose growth rate has fallen from 44% to 20% deserve the same multiple as a company that's accelerating?** It doesn't. Growth deceleration demands multiple compression. That's not a rule I made up — that's how every mature growth stock gets re-rated. And RELY is *already* decelerating.

---

## 2. The "Absolute Dollars" Argument Is a Sleight of Hand

The bull's favorite chart: "Look, they added $371M of revenue in FY2025 — more than half of 2022's entire revenue!"

That's true. It's also **completely irrelevant** to the question of whether $24.23 is a good entry price.

Here's what actually matters for shareholders: **the stock went from $22.40 on January 2, 2025, to $24.23 today.** That's roughly **+8%** — while the company grew revenue over 40% in that same period. The market has already *de-rated* this stock once. It went through an earnings crash in November 2025 (down from $16.40 to $12.31 in a single day). The recovery from $12 to $24 is real, but **the market has consistently refused to assign RELY a premium multiple even during its best quarters.**

Why? Because the market sees what the bull refuses to acknowledge: **this is a commodity business with a decelerating growth rate and intense competition.**

The bull loves to compare RELY to Western Union — at least WU's 13.5% dividend yield tells you the market expects *something* for the risk of holding it. RELY offers no dividend, a buyback that barely offsets SBC dilution, and a "moat" that consists of... a 10-million-customer base in a market full of 10-million-customer competitors.

---

## 3. The Global Card Is the Bull's Most Dangerous Assumption

The bull calls the Remitly Global Card a "free option" and "un-modeled optionality." Let me translate that into honest language: **it's a product with zero revenue, zero adoption data, and zero proven demand that the bull is asking you to pay a premium for today.**

This card is entering a market where:

- **Wise** has had a multi-currency account + card for years, with deeper liquidity in more corridors
- **Revolut** has a full banking stack with over 50 million customers
- **Nubank, Mercado Pago, and dozens of neobanks** already serve the Latin American customer base that is Remitly's bread and butter — many with local banking licenses
- **The "borrow" feature puts RELY into consumer lending risk** — an area where it has no track record, no credit risk modeling history, and no regulatory expertise

The bull's argument is "cross-selling to an existing base is cheaper than cold acquisition." Fine. But cross-selling a *card* doesn't solve the fundamental problem: **remittance customers are the most price-sensitive, switching-prone customers in the entire financial services industry.** They will use Remitly's card if it's cheaper, and they will leave the moment Wise or someone else undercuts it.

The "moat" argument keeps collapsing into the same place: there is no moat. There's a **fee-based utility business** with a **new card product that faces entrenched competitors.** If the card were truly a game-changer, management would have guided with it. They didn't. Q3 guidance was **in line**. That tells you everything.

---

## 4. The Technical Picture Is a Failed Breakout, Not a Base

Let's look at what actually happened in the last week, because the bull's "healthy consolidation" reading is contradicted by the tape:

| Date | Close | Volume | Action |
|---|---|---|---|
| Aug 5 | ~$22.50 | — | Pre-earnings |
| Aug 6 | **$25.93** | **8.4M** | Earnings spike to $27.15 intraday |
| Aug 7 | Lower | — | Immediate reversal |
| Aug 10 | **$23.14** | 4.3M | **−10.8% from high in 2 sessions** |
| Aug 11 | $23.61 | 3.0M | Weak bounce |
| Aug 12 | $24.23 | 3.2M | Sub-10 EMA reclaim? Barely |

The bull says "declining volume = sellers exhausting." I say: **declining volume = buyers not showing up.** A stock that goes from $27.15 to $23.14 in three days and then can't get back above $24.50 on the next attempt isn't "coiling." It's **losing altitude**.

Look at the momentum:
- **MACD histogram: negative** — momentum is rolling over
- **RSI: 54** — down from 66, and the trajectory is *down*, not stabilizing
- **200-day SMA distance: +36.7%** — the stock is a rubber band stretched to the breaking point

And here's the risk/reward that the bull refuses to address honestly:

- **Upside to August 6 high ($27.15): +12%**
- **Downside to 50-day SMA ($22.34): −8%**
- **Downside to 200-day SMA ($17.73): −27%**

That is **asymmetric risk against the buyer**. You're risking 27% of downside to capture 12% of upside — for a stock that just showed you it can drop 11% in three days on no news other than profit-taking.

---

## 5. The Insider Sales Aren't "Tax Planning" — They're a Warning Shot

The bull's explanation — "directors have to sell to cover taxes on option exercises" — is technically true. It's also **the most commonly repeated rationalization in the history of insider selling**.

Let me ask a simpler question: **if you were a director with 261,094 shares of a stock that just reported a record quarter, launched a transformative product, and has "un-modeled optionality" — why would you sell *any* shares right now?**

The bull says "they retained most of their position." Fine. But the *act* of selling — even a small portion — at **the exact moment** the stock is up 85% YTD and trading near 52-week highs, **immediately after an earnings pop**, is a signal. Not because insiders are doing anything illegal — but because **insiders have the most complete picture of the business, and they chose to take chips off the table at this price.**

Meanwhile, the buyback the bull brags about? **$65.2M in H1 2026 against $62M in SBC in the same period.** That's not a capital return program. That's a *round trip*. The company is issuing $62M of stock options and then buying back $65M of stock to keep the share count roughly flat. That's not "management conviction" — that's **managing the optics of dilution**.

---

## 6. The Macro Picture Is More Dangerous Than the Bull Admits

The bull looks at unemployment at 4.1% and says "tailwind!" Let me look at the same data and see a different story:

- **10-year Treasury at 4.70%** — this is the discount rate for every long-duration asset. A stock at 32x clean earnings is *extremely* long-duration. Rising yields are the single biggest threat to that multiple.
- **Dollar at 119** — the bull says it's drifting lower. It's still *historically strong*. A strong dollar means recipients in Mexico, the Philippines, and Nigeria get *less local currency* for every dollar sent. That reduces the purchasing power of remittances and puts downward pressure on send volumes.
- **Hormuz disruption is LIVE** — the odds of normal shipping by August 31 collapsed to **3%**. This isn't a tail risk; it's an *active* supply disruption. Oil prices are climbing. RELY's core senders are low-income immigrants, the exact demographic most sensitive to rising fuel and food costs.

The bull says "rates are already priced in." Really? Then why is the stock 37% above its 200-day moving average — a level that historically corresponds to *high* multiple risk, not low? If everything was already priced in, the stock would be trading at a *reasonable* multiple, not a stretched one.

---

## 7. The Bull's "Unanswerable Question" Actually Has an Answer

The bull ends with a flourish: "What would have to be true for RELY to be a good investment at this price?"

I'll answer directly: **the company would have to deliver a beat-and-raise quarter *without* the benefit of a one-time tax credit, and *while* accelerating growth back toward the 25-30% range.** That's the bar. Not "20% growth with flat sequential clean EPS." Not "a card that has zero revenue." Not "operating income off a near-zero base."

You know how I know this is the right bar? Because that's what the market is pricing. At 32x clean TTM earnings, the market is paying for a company that's going to:

- Grow revenue at 25%+ for the next several years (not 20% and falling)
- Expand operating margins dramatically (not modestly)
- Successfully launch the Global Card into a hyper-competitive market (not just announce it)
- Continue beating-and-raising every quarter (not just one quarter with a tax benefit)

If any of those fail to materialize — and the evidence says *several* of them already are failing — the multiple compresses. And at 32x clean earnings, a multiple compression from 32x to 20x is a **37% stock price decline** even *without* any operational deterioration.

---

## 8. The Sentiment Picture Is a Contrarian Nightmare

The bull cites "StockTwits 53% bullish, 0% bearish" as evidence of a healthy setup. I see that as one of the most dangerous signals in the entire dataset.

**When retail is this one-sided bullish, there is no wall of worry for the stock to climb.** Everyone who wants to own it already owns it. The Barron's "35% upside" call? Published *after* an 85% run. That's not a catalyst; that's **the media cycle's way of telling you the story is fully priced**.

And the Reddit silence? The bull ignores it, but I find it telling. In the week of a record earnings beat, a new product launch, and an 8% single-day pop, there was **zero discussion** on r/stocks, r/investing, and r/wallstreetbets. That's not healthy skepticism — that's **a story that has been so thoroughly covered by mainstream media that even the retail crowds have nothing new to say about it.**

---

## The Bottom Line: The Bull Has a Story. I Have the Math.

Let me sum up where we actually stand, after three rounds of this debate:

| Question | Bull's Answer | Bear's Answer | The Data Says |
|---|---|---|---|
| Is growth accelerating? | "Absolute dollars are growing!" | **No — growth rate has halved** | 44% → 34% → 29% → 20% |
| Is the EPS beat real? | "Pre-tax income grew 4.6x!" | **Beat is mostly a tax credit** | $0.93 reported vs. ~$0.22 clean |
| Is the multiple reasonable? | "15x forward earnings!" | **32x clean TTM earnings** | Clean P/E ≈ 32x |
| Is the card a moat? | "Un-modeled optionality!" | **Zero revenue, crowded market** | No adoption data exists |
| Is the technical setup bullish? | "Healthy consolidation!" | **Failed breakout, negative momentum** | RSI rolling over, MACD negative |
| Are insiders signaling? | "Tax planning!" | **Selling after 85% run** | Multiple insider filings post-earnings |
| Is the macro supportive? | "Strong labor market!" | **Rates high, dollar strong, Hormuz live** | 10Y at 4.70%, zero cuts 86% priced |
| Is the stock cheap? | "13.6x FCF!" | **23x post-SBC FCF** | FCF after SBC ≈ $220M |

The bull keeps asking you to believe that a company trading at **32x clean earnings**, with **growth cut in half**, a **one-time tax benefit** inflating the quarter, a **product launch with zero revenue**, and **live geopolitical tail risks** is somehow a "gift" at $24.23.

I keep asking: **what has to go right for this stock to go up from here?** And the answer is: *everything* — a growth re-acceleration, a margin expansion, a successful card launch, clean ex-tax earnings beats, no geopolitical shock, no multiple compression, and a market that keeps paying 30x+ for a decelerating fintech. That's not a high-probability bet. That's a **hope for perfection** at a stock price that leaves no margin of error.

**My recommendation remains unchanged: DO NOT BUY RELY at $24.23.**

If you own it, take at least partial profits. The stock is up 85% YTD — that's a gift *you've already received*, not one you need to buy at a premium. If you want to own the story, wait for a better entry — the $17–18 zone near the rising 200-day SMA, or a quarter that shows **clean, ex-tax earnings acceleration** at a **reasonable multiple**.

The bull will call me a pessimist. I call myself a realist. Remitly is a good company — it's just a **terrible entry point**. The market has a way of correcting stories that get too far ahead of the math. And right now, the math says this stock is priced for perfection it hasn't yet earned.

**The evidence is in. The bull's story is a beautiful one. But the data — clean earnings, decelerating growth, insider sales, negative momentum, and live macro risks — says the risk sits firmly with the buyer at this price.**

I'll take the math over the story every time.
Bear Analyst: # The Bear's Final Rebuttal: RELY Is a Good Company at the Wrong Price — and the Bull Just Proved It

**RELY | Remitly Global, Inc. | 2026-08-12 | Price: $24.23 | Verdict: DO NOT BUY**

---

I have to hand it to the bull — that was a masterclass in narrative construction. The passion, the table work, the "I'll take the balance sheet over the story" closer. It's the kind of pitch that makes you want to ignore the math and just *believe*.

But here's the thing: the bull's final case actually **concedes every material point I've made** — he just dresses the concessions in optimism. Let me show you exactly what happened in that last argument, because once you see it clearly, the bull case doesn't just weaken. It collapses.

---

## 1. The Bull Just Admitted the "Clean P/E" Is 20–24x — Not 15x

Let's mark this moment. For three rounds, the bull's headline valuation hook was **"15x forward earnings."** That was the anchor. That was the "this isn't expensive" claim that made the whole thesis feel reasonable.

And then, in the final round, the bull quietly abandoned it.

Here's the new bull math: *"Forward normalized EPS: ~$1.00–$1.20. Forward P/E at $24.23: ~20–24x."*

Four rounds of debate, and the bull has now walked his valuation claim from **15x to 20–24x forward earnings** on a *normalized* basis he constructed himself. That's a 33–60% increase in the actual multiple you're paying. And it's still built on an estimate that assumes:

- Operating margins **hold at Q2's 13.5%** indefinitely
- Revenue hits the **top of guidance** 
- **No competitive fee compression** in the core remittance business
- The card, AI, and small-business initiatives **don't consume capital**

Every one of those assumptions is optimistic. And even with that optimism dialed in, you're paying **20–24x forward earnings for a business whose growth rate has gone from 44% to 20% and is still decelerating.** That's not the "cheap" the bull promised. That's a full price for a fading growth story.

---

## 2. The "Un-Modeled Optionality" Argument Is a Circular Trap

The bull's most repeated defense of the Global Card: *"If the card works, it's a new growth leg. If the card takes time, the core business still grows 20%. If the card fails, you haven't lost anything — because you never paid for it in the valuation."*

Read that again. **"You haven't lost anything because you never paid for it."**

But wait — **you're paying $24.23.** That price embeds the *hope* of the card working, the *expectation* of continued 20% growth, and the *premium* on an 85% YTD run. The bull can't have it both ways. Either the card is a catalyst worth paying for, or it's worthless optionality the market is ignoring. He's telling you it's both — which means he's telling you **the market is paying for a story that has no current financial substance.**

Here's what the card actually is: a **late entry** into a market Wise has dominated for years, where Revolut has 50M+ customers, where Nubank and Mercado Pago own the Latin American banking relationship, and where Remitly has **zero** track record in credit, lending, or banking regulation. The "borrow" feature means Remitly is about to take on **consumer credit risk** — an entirely new risk category — in the exact demographic (low-income, cross-border) that is most exposed to economic shocks.

The bull calls this "optionality." I call it **unproven execution in a hyper-competitive space, funded by a stock price that already assumes it works.**

---

## 3. The "Absolute Revenue Growth" Defense Proves the Market's Skepticism

The bull keeps pointing to the absolute dollar additions — $290M, $320M, $371M — as if that's evidence of health. Let me point to a fact the bull has never once addressed in four rounds:

**On January 2, 2025, RELY closed at $22.40. Today it trades at $24.23. That's an 8% gain — while the company grew revenue more than 40% in the same period.**

Think about what that means. The market had the entire profitability inflection, the revenue growth, the margin expansion, the 10M customer milestone, and the beat-and-raise quarter — and it still only pays 8% more than it did 18 months ago. **The market has already rejected the growth-premium narrative once.** The stock crashed from $16.40 to $12.31 on November 6, 2025, on earnings. It's recovered — but it's still barely above where it started the dataset. That's not the signature of a "compounder being discovered." That's the signature of a **market that sees the structural deceleration and refuses to pay up for it.**

The bull's "the market is giving you a gift" framing ignores that the market has already been here, done that, and gotten burned. The November 2025 crash wasn't a random dislocation — it was the market waking up to the growth slowdown. The recovery since then is real, but the market's resistance to a premium multiple is equally real.

---

## 4. The Technical "Reclaim" Is the Weakest Read of a Distribution Top

The bull points to the close above the 10 EMA at $23.96 as evidence of stabilization. Let me remind you what actually happened on the tape, because the bull keeps omitting the most important detail:

| Date | Action | Volume |
|---|---|---|
| Aug 6 | Spiked to **$27.15** intraday, closed $25.93 | **8.4M** |
| Aug 7–10 | Fell to **$23.14** — an **11% reversal** in two sessions | 4.3M |
| Aug 11 | Bounced to $23.61 | 3.0M |
| Aug 12 | Closed $24.23 | 3.2M |

The stock went from $27.15 to $23.14 — a **$4 round trip** — and the best the bull can say is that it's back above the 10 EMA. Meanwhile:

- **MACD histogram: negative** — the trend momentum is down
- **RSI: 54, down from 66** — momentum rolling over
- **Price vs. 200 SMA: +36.7%** — historically stretched
- **The "reclaim" of the 10 EMA happened on 3.2M shares** — two-thirds below the volume of the August 6 spike

The bull calls this "healthy consolidation." Let me define what a distribution top looks like: **a spike on massive volume, a failed follow-through, declining volume on bounces, and momentum divergence.** That is literally this chart.

And the risk/reward remains my favorite part of the bear case, because the bull still can't refute it:

- Upside to $27.15: **+12%**
- Downside to 50 SMA $22.34: **−8%**
- Downside to 200 SMA $17.73: **−27%**

To get to even $32.70 (Barron's 35% upside call), the stock needs to break out to **new all-time highs** — a level it hasn't seen in years. Meanwhile, the 200-day SMA is **less than three ATRs away.** The bull will tell you the 200-day is "only in a nightmare scenario." Then he'll tell you the stock doesn't even hit it because ATRs aren't that far. Pick one. The distance is 2.1 ATRs at $1.20/ATR — that's **two bad weeks** away.

---

## 5. The SBC "Round Trip" Is Not a Buyback Program

The bull celebrated "$65.2M in buybacks in H1 2026." Let's look at that number in full context:

- H1 2026 buybacks: **$65.2M**
- H1 2026 stock-based compensation: **$62.0M**
- Net share reduction: **~$3M**

The bull's "management conviction" is a net **3% capital return** after accounting for dilution. That's not a buyback program. That's **offsetting the printing press.** The company issues options to employees, then buys back just enough to keep the share count roughly flat. That's not shareholder enthusiasm — that's optics management.

And the bull wants credit for this as "evidence of management conviction." Imagine if management *really* believed the stock was a "gift" at $24. They have $676M of cash. They could buy back $200M, $300M, $500M of stock. They aren't. They're buying back just enough to neutralize the SBC. That's not conviction. That's **maintenance.**

---

## 6. The "Rates Are Already Priced" Argument Is Dangerous Because It's Always True — Until It Isn't

The bull says "high-for-longer is fully priced." Let me ask: priced into *what*? The stock is at **32x clean trailing earnings**. The 10-year Treasury is at **4.70%**. For a long-duration asset — and a 32x clean P/E is the definition of long-duration — every 50bps move in the 10-year reprices the entire equity value.

The market has "known about" high rates for months. That doesn't mean it's priced in. It means it's *tolerated* — until the next hot CPI print, the next oil shock, or the next geopolitical escalation. And when the tolerance breaks, the stocks with the highest multiples and the lowest earnings quality get hit hardest. A 32x clean-earnings fintech with a decelerating top line is exactly that.

Meanwhile, the Hormuz disruption isn't hypothetical — it's **live right now**. The prediction market says only **3% odds** of shipping returning to normal by August 31. Only **46%** by December 31. Oil is climbing. The core Remitly customer — a low-income immigrant sender — is exactly the demographic that cuts remittance volume first when fuel and food prices spike. The bull says "18% invasion odds." I say the disruption is already happening, and the demand risk is already compounding.

---

## 7. Let's Settle the Insider Question With a Question

The bull's explanation: directors exercise $0.64 pre-IPO options, sell a portion to cover taxes, retain large positions. It's a normal practice. I'll concede that.

But here's my question for the bull: **Why did the selling happen now — after a "blowout" quarter, after an 85% YTD run, after a "transformative" product launch, at near 52-week highs?**

If the story were truly inflectional, if the card were truly a game-changer, if the clean earnings power were truly $1.00–$1.20 forward, the rational move for any insider is to hold — exercise the options, pay the taxes from other assets, and wait for the multiple expansion the bull promises is coming. They didn't. They sold. **Into the strength. Into the news. Into the story.**

The bull asks us to believe management's buyback signal over insider sales. But we've established the buyback barely offsets SBC. The insider sales are actual, voluntary, post-earnings reductions by people with the most complete information about the business. In every dataset I've seen, that cluster pattern — multiple filings in the week after a big earnings pop — has historically been **a warning, not a non-event.**

---

## 8. The Bull's "Unanswerable Question" Is Answered — and It Proves My Point

The bull asks: *"What would have to be true for RELY to be a good investment at this price?"*

He then answers with his own framework: "What is already going right" — 20% revenue growth, record EBITDA, $638M net cash, buybacks, 10M customers, the card launch.

But that's not an answer. That's a **list of what the market already knows and has already paid for.** The stock is up 85% YTD. The market has already priced the record quarter, the guidance raise, the 10M customers, and the product launch. The question was never "has the company done well?" It's "**does the current price create a margin of safety for forward returns?**"

And the answer to *that* question is no:

- You're paying **32x clean trailing earnings** — a multiple that historically demands acceleration, not the deceleration RELY is delivering.
- The growth rate has **halved** from 44% to 20% and there is zero evidence of re-acceleration.
- The Q3 guide of ~$506M is **in line** — no beat-and-raise momentum beyond the quarter that had the tax benefit.
- The stock is **37% above its 200-day SMA**, at the upper end of its 52-week range, with a negative MACD histogram.
- Insiders are **selling into the strength** — not buying.
- Geopolitical risk is **live**, not hypothetical.

For RELY to be a good investment at $24.23, the company would need to grow back toward 25–30%, deliver clean ex-tax earnings acceleration, successfully launch the card into the teeth of entrenched competition, avoid any Hormuz escalation, and hold a 30x+ multiple in a 4.70% 10-year environment. That's not one hurdle — that's a **multi-year gauntlet of perfection.**

And even if all of that goes right, what's the upside? Barron's says 35% over an unspecified timeframe. Meanwhile, the downside to the 200-day SMA is 27% and requires only a normal correction, not a thesis break.

**That is not an investment. That is a lottery ticket with extra steps.**

---

## The Final Verdict

The bull ends with: *"The bear can keep the story. I'll take the balance sheet, the cash flow, the guidance, and the trend."*

I'll end with this: **Take all of it. Take the balance sheet. Take the cash flow. Take the guidance. Take the trend. And you still can't justify the price.**

A great company at the wrong price is a bad investment. RELY at $24.23 with a 32x clean trailing multiple, a halved growth rate, a one-time tax credit masking the "blowout," a stock that's gone nowhere in 18 months despite a 40% revenue expansion, insider selling into strength, a negative momentum tape, and live geopolitical tail risk — that is the definition of a **risk/reward skewed against the buyer.**

If you want to own the story, set your limit order at **$18–19** near the rising 200-day. Or wait for a quarter that shows **clean, ex-tax, sequential earnings acceleration** — not a tax-credit-flattered headline. That's the moment to buy. That's the margin of safety.

But buying here, today, after an 85% run, on a tax-credit beat, at a stretched multiple, with the tape rolling over? That's not investing. That's **paying full price for a narrative that hasn't finished writing itself — and the market has a habit of rewriting endings.**

**The verdict stands: DO NOT BUY RELY at $24.23. The evidence is on the bear's side — and the math doesn't care about the story.**
Bear Analyst: # The Bear's Final Word: The Bull Is Selling You a Story at a 30x Clean Multiple — I'm Showing You the Math

The bull just delivered what he calls his "closing statement." I call it the most revealing argument of the entire debate — because buried inside all that passion, the bull **conceded every material point** while pretending to win them. Let me show you exactly what happened, because once you see it, you'll understand why this stock is a **risk/reward trap at $24.23**.

---

## 1. The Bull Just Admitted the Multiple Isn't 15x — It's 20–24x, and He Thinks That's a Win

Let's mark this moment for the record.

For four rounds, the bull anchored his entire valuation case on **"15x forward earnings."** That was the hook. It was the "this isn't expensive, it's a gift" number that made everything sound reasonable.

And then, in his closing statement, the bull quietly walked it back:

> *"Forward P/E at $24.23: ~20–24x forward clean earnings."*

He didn't just concede the number — he tried to **spin the concession as a "conclusion."** He said, "even in the most conservative, strip-everything-out scenario, you're paying roughly the S&P 500's market multiple for a business growing revenue 4x faster."

Let's unpack that. He's saying: *"You're paying the same multiple as the S&P 500, but for a company with higher growth!"*

That's true — and it's also the **most dangerous argument in finance.** The S&P 500 is a collection of diversified businesses with decades of competitive stability, massive moats, and proven ability to return capital. RELY is a single-product remittance company whose growth rate has been **cut in half in three years**, whose earnings just got a **$141M one-time accounting boost**, and whose "un-modeled catalyst" is a card in a market where Wise, Revolut, and Nubank already dominate.

Paying an S&P 500 multiple for a single-product fintech with decelerating growth isn't "fair." It's **generous.** And it's built entirely on assumptions that could break with a single bad quarter.

---

## 2. The Bull's "Market Hasn't Caught Up" Argument Is Actually the Strongest Bear Signal

The bull made a big deal out of this:

> *"January 2025's $22.40 price was pricing a loss-making company. Today the stock is a different company — and it's ONLY at $24.23. The market hasn't fully caught up to the transformation."*

I've been waiting for this argument, because it's the single most bearish thing the bull has said all debate.

Let me spell it out: **The market has had 19 months to observe RELY's "transformation." It has watched revenue grow 40%+, watched the company go from losses to GAAP profitability, watched the margin expansion, watched the 10M customer milestone, watched the beat-and-raise quarters — and the stock has gone from $22.40 to $24.23.**

That's an **8% total return** while the company's fundamentals improved by hundreds of millions of dollars.

Who do you trust? The bull's narrative about what the stock *should* be worth? Or the **actual market price** — which reflects the collective wisdom of every buyer and seller who has access to the same data?

The market is telling you something. It's telling you that **the market does not believe this growth is worth a premium multiple.** It's telling you that the November 2025 crash wasn't a random dislocation — it was the market waking up to the reality of decelerating growth in a commodity business. And it's telling you that **even after the best quarter in company history, the stock barely trades above where it started.**

The bull calls this an "opportunity." I call it a **red flag the size of Texas.**

---

## 3. The Tax Benefit Is Not "Only $0.22 in Context" — It's the Reason the Stock Popped 8%

The bull says, "Strip out the tax benefit entirely. You still have a company that grew revenue 20%, expanded gross margins, and generated $134.6M of operating cash flow."

Fine. Let's strip it out and look at what's actually left:

| Q2 2026 | Reported | Clean (ex-tax benefit) |
|---|---|---|
| Net Income | **$205.9M** | **~$48M** |
| EPS | **$0.93** | **~$0.22** |

Do you know what the market traded on August 6? **The $0.93 headline.** The stock popped 8% because the headline number appeared to be a blowout — not because traders read the 10-Q footnote about the $141M valuation allowance release.

The bull says "the cash flow statement doesn't lie." Okay. But the cash flow statement has been *strong* for several quarters — and the stock didn't pop 8% on those prior prints. The only reason it popped this time was the **one-time accounting credit that made EPS look 4x better than the clean reality.**

When the market figures out that Q3 clean EPS will be ~$0.25–0.30 and the "blowout" was a tax artifact, the multiple **will** re-rate. The only question is how fast.

---

## 4. The Technical "Health" the Bull Sees Is Actually a Textbook Distribution Top

The bull called my technical analysis "the weakest read of a distribution top." Let me let the tape decide.

Here's what actually happened over the last five sessions:

| Date | Close | Volume | Context |
|---|---|---|---|
| Aug 6 | **$25.93** | **8.4M** | Spiked to $27.15 intraday — massive volume |
| Aug 7 | Lower | — | Immediate reversal from highs |
| Aug 10 | **$23.14** | 4.3M | **−11% from high in two sessions** |
| Aug 11 | $23.61 | 3.0M | Weak bounce on *declining* volume |
| Aug 12 | $24.23 | 3.2M | Barely reclaimed 10 EMA on 60% *lower* volume |

The bull sees "sellers exhausting." I see **buyers failing to show up.**

What does a distribution top look like? A spike on huge volume, a failed follow-through, declining volume on each bounce attempt, momentum rolling over, and price unable to reclaim breakout levels. **That is literally this chart.**

And the momentum data doesn't support the bull:

- **MACD histogram: NEGATIVE** — momentum is below zero
- **RSI: 54, down from 66** — the trend over the last week is *down*, not up
- **Price vs. 200 SMA: +36.7%** — historically stretched for a stock that just showed it can drop 11% in two days

The bull wants you to believe a "$24.23 close above the 10 EMA" is a bullish signal. Here's a more honest read: **the stock is $2.92 below its August 6 high despite reporting the "best quarter in company history."** If that was a real breakout, the stock would be making new highs on follow-through volume. It isn't. It's fading.

---

## 5. "In Line" Guidance Is Not a "Setup for a Beat" — It's a Ceiling on the Narrative

The bull's argument about guidance is perhaps his most creative yet:

> *"Q3 guidance of $506M in line with consensus? That's disciplined management setting a beatable bar!"*

That's a generous interpretation. Here's the ugly one: **the company just had the best quarter in its history, raised full-year guidance, launched a "transformative" product — and still chose to guide the next quarter at only "in line with estimates."**

If the Global Card were a "re-rating catalyst," why isn't ANY of it in the Q3 guide? If the business were accelerating, why not guide above consensus and blow the doors off? Why give the market *exactly* what it expects after an 85% run?

Because **the company can't guide above and beyond right now.** The product is unproven, the growth is decelerating, and the "beat-and-raise" cadence — the fuel for this entire rally — is running on fumes. Management knows this. The market will learn it.

---

## 6. The SBC "Dilution Is Only 5%" — Let's Look at the Real Math

The bull says cumulative dilution is only 5%, which he calls "incredibly disciplined." Let's test that against the actual numbers he himself cited:

- H1 2026 buybacks: **$65.2M**
- H1 2026 SBC: **$62.0M**
- **Net share reduction: ~$3M**

That's not a capital return program. That's **a treadmill.** The company issues $62M of stock to employees, then buys back $65M to keep the share count from exploding. The bull calls this "the beginning of a capital-return story." I call it **zero net return to shareholders.**

And the "fortress balance sheet" the bull keeps bragging about? **$676M of cash** is not an investment opportunity fund — it's a **warehouse for capital with no high-ROI projects to deploy it into.** If the Global Card were such a huge opportunity, management would be investing hundreds of millions into it, not buying back enough stock to barely offset dilution.

---

## 7. The Insider Sales — The Bull Still Can't Answer the One Question That Matters

The bull keeps insisting the $0.64 pre-IPO option exercise is "routine tax planning." Fine. Let me ask him the question he's never answered in four rounds:

**If the stock is about to re-rate from $24 to $32+ (Barron's target), if the Global Card is a "game-changer," if the company has "un-modeled optionality" — why would a director sell ANY shares at $24 after the best quarter in company history?**

Not because they need the money. Not because the tax bill is insurmountable — a director with a $45.96M position has other assets. No. They sold because **they looked at the same data the bull is looking at and made a different decision about what comes next.**

The bull says "management is buying back stock, that's the signal that matters." But we just established the buyback barely offsets SBC. Meanwhile, the insiders are **actually selling.** Which signal should you trust? The one where insiders are putting their own money at risk — or the one where they're taking chips off the table?

---

## 8. The Bull's "What Has to Go Wrong?" Question — Here's the Answer

The bull ended with a flourish:

> *"What has to go wrong for the bear to be right?"*

Let me give you the actual list, and notice how **mundane** these scenarios are — none of them require a global catastrophe:

1. **Q3 earnings come in at guide (~$506M)** — no beat-and-raise. The multiple compresses. The stock drops 10-15%. That's not a catastrophe; that's what happens when "in line" meets a 30x clean multiple.
2. **The market continues its current behavior** — the same behavior that's kept the stock flat for 19 months despite a 40% revenue expansion. The "re-rating" the bull promises simply doesn't happen.
3. **Wise or another competitor cuts fees in a key corridor** — gross margin *stops* expanding. The 62.1% becomes 61%, then 60%. The entire margin expansion thesis breaks.
4. **Hormuz disruption escalates** — oil spikes, low-income senders cut remittance volumes. Revenue growth drops from 20% to low-teens. The market de-rates the multiple further.
5. **The card gets a tepid rollout** — no adoption data, no revenue contribution, no "catalyst." It just becomes another me-too product announcement, and the "un-modeled optionality" evaporates.

None of these are tail risks. Most are **base-case scenarios** that require nothing more than **the continuation of current trends.**

---

## The Final Verdict: The Bull Has the Story. The Data Has the Truth.

After four rounds, the bull's case rests on:

- A **tax-credit-flattered earnings number** that he now admits produces a 20-24x forward multiple
- A **growth rate that's been cut in half** — and that he can only defend by talking about absolute dollars
- A **product catalyst with zero revenue, zero adoption data, and entrenched competitors**
- A **technical setup** that shows a failed breakout on declining volume
- **Insider sales** he can't explain beyond "routine tax planning"
- A **macro environment** where the one live tail risk (Hormuz) happens to be the exact risk that hits his core customer the hardest
- A **stock price that's gone nowhere for 19 months while the fundamentals "transformed"** — the market's actual verdict on the growth premium

The bull says "what has to go wrong?" I say: **look at what's already going wrong — and has been for months.**

The stock is $2.92 below its post-earnings high. The MACD is negative. The clean EPS is $0.22, not $0.93. The growth rate is 20% and falling. Insiders are selling. And the market, which has had 19 months to "catch up" to the transformation, has priced the stock at **8% above where it started.**

**My recommendation remains unchanged: DO NOT BUY RELY at $24.23.**

If you own it, take at least partial profits. The 85% YTD gain is a gift you've already received — don't hand it back. If you want to own the story, wait for the $17–18 zone near the rising 200-day SMA, or wait for a quarter that shows **clean, ex-tax, sequential earnings acceleration at a reasonable multiple.** That's the moment to buy. That's the margin of safety. That's how you make durable returns — not by chasing a narrative at a 30x clean multiple while the tape rolls over.

The bull will call me a pessimist. I call myself a **realist who's seen this movie before.** Remitly is a good company — it's just a **terrible entry point at $24.23.** The market has a way of correcting stories that get ahead of the math — and the math says the risk sits firmly with the buyer at this price.

**The verdict: DO NOT BUY. The evidence is on the bear's side. The math doesn't care about the story. And the story is all the bull has.**

### Manager
**Recommendation**: Overweight

**Rationale**: The debate was close, but the bull carried the core argument. The bear is right that the headline Q2 beat was flattered by a $141M deferred-tax-asset release: clean EPS is roughly $0.22–0.25, not $0.93, so RELY is not really trading at "15x forward earnings." On clean forward earnings the multiple is closer to 20–24x. The bear is also right that growth has decelerated from ~44% to ~20%, that SBC consumes a large share of FCF, and that buybacks are currently roughly offsetting dilution rather than shrinking the share count. The post-earnings tape looks more like a failed breakout/consolidation than a clean re-acceleration.

However, the bull won on the substance: RELY's profitability inflection is real and cash-backed, not an accounting mirage. Q2 pre-tax income was $64.6M, operating income grew 4.6x YoY to $66.7M, adjusted EBITDA hit a record $115M at a 23% margin, operating cash flow was $134.6M, and TTM FCF was ~$375M. Gross margin expanded to 62.1% while revenue grew 20%, and FY26 guidance was raised to ~$1.98B. With ~$638M net cash, a 20% grower at 20–24x forward clean earnings is not the bargain the bull claimed, but it is a reasonable price for a newly self-funding fintech with expanding margins. The bear's insider-sale argument is weak (routine pre-IPO option exercises with large retained positions), and the "fee war" argument is undercut by rising gross margins.

Net: the bear successfully removes the "cheap" label and demands discipline; the bull successfully establishes a genuine fundamental inflection. That argues for a constructive but not all-in stance—Overweight with disciplined entries and hard risk levels.

**Strategic Actions**: RELY (Remitly Global, Inc., NMS) — Build exposure gradually; do not chase.

1. Initiate or add a starter position near $24.23 sized at roughly half the intended overweight.
2. Add on pullbacks into the $22.00–23.00 zone (50-day SMA / lower Bollinger confluence). Add the remaining target only on a confirmed breakout above $27.15 on above-average volume.
3. Position sizing: target an Overweight of roughly 1.5–2x normal active weight. Cap initial capital at risk so a stop below $22.30 costs no more than about 50–75 bps of portfolio.
4. Risk management: for trading positions, exit on a daily close below $22.00–22.30. For longer-horizon positions, trim if RELY loses the 50-day SMA and breaks the rising trend.
5. Upside levels: first target $27–28; secondary $30–33 if Q3 clean ex-tax earnings accelerate, FY guidance is raised again, or Global Card adoption shows measurable revenue/customer engagement.
6. Monitoring ahead of Q3: clean ex-tax EPS (ex-DTA), revenue vs ~$506M guide, gross margin trajectory, SBC vs buybacks, insider filings, and Hormuz/oil tail risk. Re-evaluate on Q3: add on a clean beat-and-raise; trim if revenue growth slips below ~18% or gross margin compresses.

## V. Portfolio Manager Decision

Overweight