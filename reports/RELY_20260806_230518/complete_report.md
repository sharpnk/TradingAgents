# TradingAgents Investment Report

**Ticker:** RELY
**Date:** 2026-08-06
**Depth:** Deep (5 rounds)

## I. Analyst Team Reports

### Market
All data is in hand and the verified snapshot is consistent with my indicator calls (no discrepancies — e.g., 50 SMA 22.06, 200 SMA 17.59, 10 EMA 24.08, RSI 66.30, MACD 0.56, signal 0.45, ATR 1.09 all match). Here is the full analysis.

---

FINAL TRANSACTION PROPOSAL: **BUY**

# RELY (Remitly Global, Inc.) — Technical Analysis Report
**Analysis date:** 2026-08-06 | **Exchange:** NMS | **Sector:** Technology / Software-Infrastructure

## 1. Indicator Selection (8 of 8 slots used)

I selected a non-redundant, multi-layer toolkit spanning trend, momentum, volatility, and volume:

| # | Indicator | Role | Why it was selected (no redundancy) |
|---|---|---|---|
| 1 | `close_50_sma` | Medium-term trend | Defines the current uptrend slope and dynamic support; faster than the 200 SMA but slower than EMAs — bridges short and long horizons. |
| 2 | `close_200_sma` | Long-term trend | The strategic regime filter; together with the 50 SMA it flags the golden-cross posture and tells us whether we're in a bull or bear structure. |
| 3 | `close_10_ema` | Short-term momentum | Fastest trend layer for timing entries/exits around the recent base; catches the immediate shift underway this week. |
| 4 | `macd` | Momentum direction | Measures the speed of the EMA spread; directly signals whether upside momentum is accelerating or fading. |
| 5 | `macds` | Momentum trigger | Paired with MACD to identify the fresh bullish crossover — complementary, not duplicative (line vs. smoothed trigger). |
| 6 | `rsi` | Overbought/oversold + divergence | Flags exhaustion risk at extremes (70/30) and confirms momentum breadth; distinct from MACD because it is bounded and mean-reverting. |
| 7 | `atr` | Volatility / risk sizing | Gives concrete stop-loss and position-size math (today's expansion matters — see §4). |
| 8 | `vwma` | Volume-weighted price | Confirms whether the rally is backed by real volume participation vs. thin tape; unique volume dimension not covered by any other pick. |

I deliberately avoided `boll`/`boll_ub`/`boll_lb` as selections (partially redundant with the 20 SMA/volatility story) but used the verified snapshot's Bollinger values as corroborating evidence in §4.

## 2. Verified Market Snapshot (Source of Truth — 2026-08-06)

- **OHLC:** Open 25.98 / High 27.15 / Low 24.11 / **Close 25.93** / Volume 8,330,700
- **MAs:** 10 EMA 24.08 | 50 SMA 22.06 | 200 SMA 17.59
- **Momentum:** RSI 66.30 | MACD 0.56 | Signal 0.45 | Histogram +0.11
- **Volatility/bands:** ATR 1.09 | Boll middle 23.78 | Upper 25.55 | Lower 22.01

## 3. Trend Analysis — Strong, Multi-Timeframe Bull Structure

**Long-term (200 SMA):** RELY closed at 25.93, **~47% above the 200 SMA (17.59)**, which has been rising steadily (≈15.89 on 2026-04-08 → 17.59 now). The stock is firmly in a long-term uptrend and has been since the February earnings gap (2026-02-18 close 13.61 → 02-19 close 17.14 on 22.9M volume).

**Medium-term (50 SMA + golden cross):** Price is **~17.5% above the 50 SMA (22.06)**, and the 50 SMA is rising (~15.28 on 04-08 → 22.06). The 50 SMA crossed above the 200 SMA around mid-April 2026 (50 SMA 15.99 vs 200 SMA 15.85 on 2026-04-17) — a textbook **golden cross** that has never been re-tested. The spread between the averages is widening, which is classic bullish alignment.

**Short-term (10 EMA):** Price (25.93) sits **7.7% above the 10 EMA (24.08)**, which turned up sharply this week (23.35 on 08-03 → 23.58 → 23.67 → 24.08). The 10 EMA is the first dynamic support for any dip.

**Price structure:** After the late-July consolidation base (closes 22.53–23.45 between 07-24 and 07-31), RELY broke out: 23.98 (08-03) → 24.63 (08-04) → 24.07 (08-05) → **25.93 (08-06)**, today printing the highest close in the dataset and a new intraday high of 27.15 (previous peak was 25.75 on 07-16). Today's move is **+7.7% versus the 08-05 close of 24.07** — a decisive, volume-backed breakout.

## 4. Momentum, Volatility & Volume Analysis

**MACD (fresh bullish crossover):** MACD (0.56) is now above its signal (0.45) — the histogram flipped from **−0.02 on 08-05 to +0.11 on 08-06**, i.e., a brand-new bullish crossover on the breakout day. The MACD line has been positive since late June (crossed zero around 06-24/06-25), so today's crossover re-accelerates an already-bullish oscillator rather than starting from scratch. This is a high-quality confirmation of the breakout.

**RSI (room before overbought):** At **66.30**, RSI has room before the 70 overbought line. The tape shows a pattern to respect: RSI hit 70.5 (07-06/07-07) and 70.5 (07-16) and each time the stock pulled back several percent (e.g., 07-16's 70.5 preceded the drop from 25.23 to 22.53 by 07-24). Today's 66.3 reading says momentum is strong but not yet at the historical stall zone — a pullback into the 66–70 zone is the watch area for near-term exhaustion.

**Volatility (ATR expansion):** ATR rose to **1.09** from 0.94 (08-05) and ~0.85–0.90 in mid-July — the highest reading of the lookback. Today's intraday range (24.11–27.15) was an enormous ~12.6% of the open, and the close (25.93) finished *below* the open (25.98) after tagging 27.15. That wicking action at the highs, combined with a close **1.5% above the upper Bollinger band (25.55)**, is the main caution flag: the stock is extended and volatile, so chase-entries carry elevated short-term whipsaw risk.

**Volume confirmation (VWMA):** VWMA (23.94) is well below price, and today's 8.33M shares is roughly **3–4× the 1.8–3.1M range seen in late July** — a real volume expansion, not a low-participation drift. Rising VWMA (23.54 on 08-05 → 23.94) confirms that the recent advance is volume-supported.

## 5. Actionable Insights & Trade Framework

**Bias: Bullish (BUY) with disciplined entry mechanics.**

- **Trend alignment is unambiguously positive:** price > 10 EMA > 50 SMA > 200 SMA; golden cross intact; MACD just gave a fresh bullish crossover; RSI 66 with headroom; breakout on 3–4× volume. Every layer agrees.
- **Do not chase above the upper band.** With price extended ~1.5% above Bollinger upper (25.55), RSI approaching the historical stall zone (70+), and an ATR-expanded day that closed below its open, the higher-probability entries are:
  - **Pullback entry zone: ~24.1–24.8** — the rising 10 EMA (24.08) and 1×ATR below Friday's close (25.93 − 1.09 ≈ 24.84). This area coincides with the top of the prior breakout base.
  - **Breakout continuation entry:** a daily close above today's intraday high of **27.15** would confirm the next leg with no overhead supply in the 1-year window.
- **Risk management:** ATR = 1.09 (~4.2% of price). A **stop near 23.75 (2×ATR below close)** is the key structural line — it converges with the 20-day SMA (Bollinger middle 23.78) and the late-July breakout shelf, giving a confluence-based invalidation level. Size positions so that a 2×ATR stop costs no more than your defined portfolio risk.
- **Take-profit/watch:** First resistance is the 27.15 intraday high; above it, the chart is open (no 1-year supply). Trail stops under the 10 EMA (currently 24.08) once in profit, and re-evaluate if RSI closes above 70 with negative divergence (price making new highs while MACD/RSI fail to).

## 6. Key Points Summary

| Aspect | Observation (2026-08-06) | Implication |
|---|---|---|
| Price vs. 200 SMA | 25.93 vs 17.59 (+47%) | Strong long-term uptrend |
| Golden cross | 50 SMA crossed 200 SMA mid-April 2026; spread widening | Bullish regime, never re-tested |
| Price vs. 50 SMA | 25.93 vs 22.06 (+17.5%) | Trend extended but intact |
| 10 EMA | 24.08, rising sharply | Near-term support / first dip-buy zone |
| MACD | 0.56 > signal 0.45; hist +0.11 (fresh bullish cross 08-06) | Momentum re-accelerating on breakout |
| RSI | 66.30 (below 70) | Strong but approaching overbought stall zone |
| Bollinger | Close 25.93 above upper band 25.55 | Extended; mean-reversion risk if it fails to hold |
| ATR | 1.09 (highest in lookback); intraday range 24.11–27.15 | Elevated volatility — size stops/positions accordingly |
| Volume / VWMA | 8.33M shares (~3–4× recent); VWMA 23.94 rising | Breakout is volume-confirmed |
| Entry strategy | Buy pullbacks 24.1–24.8 or breakout close > 27.15 | Disciplined entry avoids chasing the upper band |
| Invalidation | Daily close below ~23.75 (2×ATR ≈ 20 SMA) | Trend thesis damaged below this confluence |
| Final proposal | **BUY** | Bullish bias with pullback-entry discipline |

**Note on data integrity:** All exact values above are taken from the verified market snapshot for 2026-08-06 and match the `get_stock_data` / `get_indicators` outputs; no conflicts were detected. No support/resistance bounces or historical validations are claimed beyond the concrete dates and prices cited from tool output.

### Sentiment
**Overall Sentiment:** **Bullish** (Score: 7.2/10)
**Confidence:** Medium

## RELY (Remitly Global, Inc.) — Sentiment Report
**Period:** 2026-07-30 to 2026-08-06 | **As of:** 2026-08-06

### 1. Source-by-source breakdown

**News / institutional framing (4 headlines, 4 positive — decisively bullish).**
Every headline in the 7-day window is constructive and centered on Q2 FY2026 earnings, reported ~2026-08-05:
- **Barron's** published an explicit bullish call: the stock "can rally 35% as it disrupts global remittance markets," citing a $900B+ World Bank-sized remittance market and a ~$5B market cap for RELY.
- **MarketBeat** earnings-call highlights: revenue +20% YoY to $495M, record adjusted EBITDA of $115M (23% margin), and CEO Sebastian Gunningham noting the company "surpassed 10 million" active customers.
- **Zacks** reports earnings and revenue surprises of +268.97% and +2.19% for the June 2026 quarter.
- **StockStory** notes RELY "exceeded the market's revenue expectations" (sales +20.2% YoY to $495.2M), guided next quarter to ~$506M (close to consensus), and posted GAAP EPS of $0.93, "significantly above" estimates, with the stock soaring.

This is a clean, one-directional institutional narrative: strong beat, record profitability, scale milestone, and at least one house call for meaningful upside.

**StockTwits (30 messages; 10 Bullish / 0 Bearish / 20 unlabeled).**
Among labeled messages, the ratio is a lopsided 100% bullish (10:0). Retail tone is post-earnings exuberance:
- Technical momentum: "@JFDI" — "big ol base" and "Ohhhhh $RELY ...we goin' stage 2?"; "@kiwitc2000" — "Chart suggests breakout possible"; "@MarketPulsee" flags RELY among names hitting **new 52-week highs** on 2026-08-06; "@fundamentalCo" — "I want more!!!" and "I hope you all made huge gains!!".
- Fundamentals/milestone: "@BlazarBeta" — "just crossed 10 million active customers. Ten-bagged since 2019. The growth is real, now they need to prove they can monetize it"; "@MarketIntel_" echoes the 10M milestone; the StocktwitsEarnings recap notes GAAP EPS $0.98 (+3166.67% YoY), revenue $495.16M (+20.23% YoY), and FY2026 revenue guidance of $1.978–1.988B.
- Cautionary undercurrent (unlabeled but visible): "@NovaNoble" — "valuation still looks wrong... it needs to show me, not tell me"; older posts from "@My_Nuts_Are_Heavy" flag SBC outweighing buybacks and dilution risk; "@howardlindzon" notes RELY now has more revenue than Western Union ($WU).
- Data-quality caveats: only 10 of 30 messages carry an explicit label, and several messages fall outside the 7-day window (mid-June to mid-July), so the live-window sample is roughly a dozen messages. Zero bearish labels is bullish but also one-sided — there is no bearish counterweight in the feed.

**Reddit (r/wallstreetbets: 1 tangential post; r/stocks and r/investing: none).**
There is effectively **no dedicated Reddit engagement** on RELY in the window. The only r/wallstreetbets item is a MSFT→META rotation thesis that merely mentions the ticker via the RSS feed, with no scores/comments and no RELY-specific content. r/stocks and r/investing returned no posts. The broader retail-community chatter that would confirm or contest the StockTwits momentum has not materialized — this is absence of signal, not a bearish signal.

### 2. Cross-source divergences and alignments
- **News ⇄ StockTwits: fully aligned.** Institutional coverage (beat, record EBITDA, 10M customers, 35%-upside call) and retail sentiment (52-week highs, "stage 2," breakout chatter) point the same direction. No bearish institutional headlines exist to counter the retail enthusiasm.
- **Reddit ⇄ everything: silent, not divergent.** The gap is coverage, not disagreement; it slightly lowers confidence in the breadth of the read.
- **Intra-source nuance (StockTwits):** momentum traders are exuberant about the technical breakout while a minority of valuation-focused users remain skeptical ("needs to show me, not tell me," SBC vs. buybacks). This is a healthy tension rather than a directional split.
- The one structural mismatch worth flagging: Q3 guidance (~$506M) is only "close to analysts' estimates" and FY guidance implies continued ~20% growth, not an acceleration — so the beat-and-raise narrative is real but not explosive, and the 35% Barron's upside call rests on monetization of the 10M+ customer base that some retail users are explicitly questioning.

### 3. Dominant narrative themes
1. **Q2 earnings beat and profitability inflection** — the single dominant theme across all four news items and the earnings-related StockTwits posts (record 23% adjusted EBITDA margin, triple-digit GAAP EPS growth, +268.97% earnings surprise).
2. **Scale milestone: 10M+ active customers** (10x since 2019) — repeated verbatim across MarketBeat, StockTwits, and the earnings recap; framed as both validation and an unresolved monetization question.
3. **Technical breakout / 52-week-high momentum** — multiple StockTwits users describing base formation, "stage 2," and new-high printing; a sentiment signal that the earnings event has converted conviction into price action.
4. **Valuation debate** — Barron's sees 35% upside; some retail users still see "valuation looks wrong"; the SBC/buyback dilution thread from late June lingers in the feed.

### 4. Catalysts and risks
**Catalysts (from the data):**
- Q2 FY2026 beat (revenue $495.2M, +20.2% YoY; adjusted EBITDA $115M / 23% margin; GAAP EPS $0.93–0.98) reported 2026-08-05.
- FY2026 revenue guidance of $1.978–1.988B and Q3 guide of ~$506M (in line with consensus).
- 10M active-customer milestone — a potential long-term monetization narrative hook.
- New 52-week-high momentum plus broad sector strength (financials, fintech) noted in StockTwits feeds.
- Continued regulatory license expansion in key remittance markets (AXLFI thematic posts).

**Risks (from the data):**
- Q3/FY guidance is only in-line ("close to analysts' estimates"), so forward estimates were not reset higher — the beat may already be priced in at new highs.
- Valuation skepticism persists even among engaged retail users; the "show me, not tell me" post and SBC-vs-buyback dilution concern temper the bullish case.
- One-sided sentiment (10 Bullish / 0 Bearish on StockTwits) plus 52-week-high chatter raises the risk of short-term over-extension and contrarian pullback.
- Reddit's silence means no independent community validation of the momentum thesis — the retail signal is concentrated in a single, small platform sample.

### 5. Summary table of key sentiment signals

| Signal | Direction | Source | Supporting evidence |
|---|---|---|---|
| Q2 beat: revenue +20% YoY to $495M, record 23% EBITDA margin | Bullish | Yahoo Finance news (MarketBeat, Zacks, StockStory) | "Exceeded expectations... stock soars"; earnings surprise +268.97% |
| Upside call: stock "can rally 35%" | Bullish | Barron's | Disrupting $900B+ global remittance market, ~$5B cap |
| Scale milestone: 10M+ active customers (10x since 2019) | Bullish | MarketBeat, StockTwits (@BlazarBeta, @MarketIntel_) | Repeated across sources; monetization still questioned |
| Labeled StockTwits sentiment | Bullish | StockTwits (10:0 labeled) | 33% of all messages labeled Bullish, 0% Bearish |
| Technical momentum | Bullish | StockTwits (@JFDI, @kiwitc2000, @MarketPulsee) | "stage 2?", "breakout possible", new 52-week high 08-06 |
| Valuation caution | Mildly Bearish | StockTwits (@NovaNoble, @My_Nuts_Are_Heavy) | "needs to show me, not tell me"; SBC vs buybacks |
| Forward guidance in-line, not raised | Neutral/Mild risk | StockStory | Q3 ~$506M "close to analysts' estimates" |
| Broader retail community | Silent | Reddit (r/wallstreetbets, r/stocks, r/investing) | No substantive RELY threads; only tangential mention |

**Bottom line:** Sentiment for RELY is Bullish, driven by a clean earnings-beat news cycle and exuberant but one-sided retail positioning on StockTwits (52-week highs, breakout chatter). The bullish case is broad but not deep: Reddit is silent, the labeled StockTwits sample is small, and a minority of engaged users plus in-line forward guidance temper the enthusiasm. Treat this as momentum-sentiment fuel to weigh alongside fundamentals and technicals, not as a standalone price call.

### News
# RELY (Remitly Global, Inc.) — News & Macro Research Report
**Date:** 2026-08-06 | **Ticker:** `RELY` (NASDAQ/NMS) | **Identity confirmed:** Remitly Global, Inc. (Technology / Software - Infrastructure; digital remittance/payments)

---

## 1. Executive Summary

`RELY` enters this window in a powerful fundamental and technical uptrend, punctuated by a **Q2 CY2026 earnings beat (reported Aug 5)** that sent shares soaring. Revenue grew ~20% YoY to ~$495M, adjusted EBITDA hit a record $115M (23% margin), GAAP EPS of $0.93 crushed consensus (+269% earnings surprise), and the company crossed **10 million customers**. This comes after a +62% first-half 2026 run and ~+80% YTD appreciation.

The macro backdrop is supportive but carries two live risks: (1) **geopolitical oil risk** from the Strait of Hormuz/Iran situation that triggered a VIX spike to 20.7 on July 29 and hit growth/remittance names (including `RELY`) in risk-off sessions; and (2) **rising 10-year Treasury yields** (4.63%, peaked 4.75% on July 31) pressuring high-multiple stocks. Offsetting this: recession odds are low (8% for US by end-2026), the Fed is on hold at 3.63% with an 88% market-implied probability of *no* cuts in 2026, CPI is decelerating, and unemployment fell to 4.2% — a constructive backdrop for remittance volumes, which track immigrant labor income.

---

## 2. Company-Specific News (RELY) — Past Week & Recent Context

| Date | Headline | Signal |
|---|---|---|
| 2026-08-05 | **Q2 Earnings Call Highlights** (MarketBeat) | Revenue +20% YoY to $495M, above guidance; record adj. EBITDA $115M (23% margin); surpassed 10M customers — bullish |
| 2026-08-05 | **Q2 Earnings and Revenues Top Estimates** (Zacks) | Earnings surprise +268.97%, revenue surprise +2.19% — strong beat |
| 2026-08-05 | **Exceeds Q2 CY2026 Expectations, Stock Soars** (StockStory) | Sales +20.2% YoY to $495.2M; Q3 guide ~$506M (in line with estimates); GAAP EPS $0.93 well above consensus |
| 2026-08-05 | **Barron's: "This Stock Can Rally 35%..."** | Positive — $900B+ global remittance market, ~$5B market cap, disruptive growth story |
| 2026-07-30 | **ACV Auctions, Fiverr, Remitly Falling** (StockStory) | Risk-off: Trump declared Iran ceasefire "over," oil higher, yields up — hit `RELY` alongside other growth names |
| 2026-07-23 | **Motley Fool: "2 Exceptional Growth Stocks... Great Buys in 2026"** | Positive — Remitly + Adyen underappreciated |
| Mid-July | **IBD: Breakout Above Cup-With-Handle Buy Zone** | Technical — buy zone breakout; **lawmakers easing remittance tax** on certain transfers (policy tailwind) |
| 2026-07-10 | **"Why Remitly Global Jumped 62.4% in H1 2026"** (Motley Fool) | Momentum confirmation |
| 2026-06-26 | **Cantor Fitzgerald: Overweight, $28 PT** | Analyst support (~15%+ above mid-July price of ~$23.86) |

**Key context:** Stock at ~$23.86 (mid-July), 52-week high $24.44, +13% 1-month, +80% YTD, +38% 1-yr TSR. Simply Wall St. raised the valuation question ("Is the stock already expensive?"), and the stock's beta to risk-off geopolitics was demonstrated on July 30.

---

## 3. Macroeconomic Environment (FRED data, as of 2026-08-06)

- **Fed Funds Rate:** 3.63% — unchanged over the window. **Policy on hold.**
- **10Y Treasury:** 4.63% (up +8bp / +1.76% over the month; intra-window peak 4.75% on Jul 31). **Rising discount rates = headwind for growth valuations.**
- **Yield Curve (10s−2s):** +0.44%, steepening from +0.36% (peak +0.47% Jul 31). Positively sloped — no recession signal from the curve.
- **CPI:** 332.6 (Jun), down −0.42% from May — **disinflationary trend**.
- **Core PCE:** 130.27 (Jun), +0.13% over window — tame.
- **Unemployment:** 4.2% (Jun), down from 4.3% — **solid labor market**; supports remittance income flows.
- **Real GDP:** Q2 2026 = $24,270.6B, +0.37% QoQ — modest but positive growth.
- **VIX:** 15.81 (Aug 5) — settled from a 20.66 geopolitical spike (Jul 29); risk appetite recovering.

**Macro takeaway for RELY:** Disinflation + stable labor market + positive (steepening) yield curve + low recession odds = a fundamentally supportive backdrop for consumer payments/remittances. The main macro overhang is the 10Y at ~4.6%+ and the Fed's higher-for-longer stance (88% probability of *no* 2026 cuts), which caps multiple expansion for high-growth software names.

---

## 4. Geopolitical Risks (Oil / Middle East)

- **Strait of Hormuz:** Traffic-normal-by-Aug 31 implied probability is just **12%** (Sept 30: 26%); Iran charging Hormuz fees by Oct 31: **40%**. Oil is rising on reopening concerns; Asian govt bonds fell and US futures slipped on fresh Hormuz worries this week.
- **US–Iran:** Effective ceasefire by Aug 31 is priced at **88%** (up +29pp WoW) — a material de-escalation signal; but a final nuclear deal by year-end is only ~32% (Aug 31: 3%).
- **Direct RELY linkage:** `RELY` sold off alongside ACV/Fiverr on July 30 when the Iran ceasefire was declared "over." Remittance corridors (especially to the Middle East/South Asia) and risk appetite are both sensitive to these headlines. An oil-price spike would feed inflation → reinforce Fed's no-cut stance → higher yields → multiple compression for `RELY`. Conversely, continued de-escalation (88% ceasefire odds) removes the near-term drag.

---

## 5. Prediction Market Signals

| Market | Implied Probability | Read |
|---|---|---|
| No Fed rate cuts in 2026 | **88%** | Higher-for-longer; no near-term rate-cut catalyst |
| US recession by end-2026 | **8%** (−4.5pp WoW) | Low recession risk; risk-on tilt |
| US–Iran effective ceasefire by Aug 31 | **88%** (+29pp WoW) | Geopolitical tension de-escalating |
| Hormuz traffic normal by Aug 31 | 12% | Residual oil-supply risk persists |
| Iran charges Hormuz fees by Oct 31 | 40% | Possible structural oil-cost shock later in Q3 |

---

## 6. Actionable Trading Insights

1. **Post-earnings momentum is strong** — beat-and-raise execution, record EBITDA margins (23%), and GAAP profitability make `RELY` fundamentally credible, not just momentum. Q3 guide (~$506M) is in line, so the next catalyst is Q3 execution and any remittance-tax policy follow-through (IBD noted lawmakers easing remittance taxes).
2. **Watch the 10Y yield (4.63%) as the swing factor** — `RELY` is a high-multiple growth stock (+80% YTD); a break above ~4.75–4.8% in the 10Y would pressure the whole software complex, including `RELY`.
3. **Geopolitical beta cuts both ways** — Hormuz headlines hit `RELY` on July 30, but prediction markets now price an 88% effective ceasefire by end-August; a confirmed normalization would likely unwind the oil-risk premium and support the stock. Monitor the Aug 15/Aug 31 Hormuz resolution dates as near-term event risk.
4. **No Fed cut catalyst in 2026 (88% probability)** — do not position for a dovish surprise; the bull case for `RELY` must come from company fundamentals and remittance market share gains, not multiple expansion.
5. **Macro tailwinds for remittance volumes** — US unemployment at 4.2% and falling, disinflation (CPI down 0.42%), and a positive yield curve support the immigrant/remitter labor-income base that drives `RELY`'s volumes.
6. **Valuation guardrail** — after +80% YTD and a $24.44 high, the stock is no longer cheap (Simply Wall St. flagged expensiveness); analyst targets ($28 Cantor) and the Barron's +35% thesis imply upside, but the risk/reward now depends on continued beat-and-raise quarters.

---

## 7. Summary Table — Key Points

| Category | Key Point | Date / Window | Implication for RELY |
|---|---|---|---|
| **Company — Q2 results** | Revenue $495M (+20% YoY), adj. EBITDA $115M record (23% margin), GAAP EPS $0.93; >10M customers | 2026-08-05 | Strong positive; beat-and-raise credibility |
| **Company — Guidance** | Q3 revenue guide ~$506M, near consensus | 2026-08-05 | Neutral-to-positive; next catalyst is Q3 execution |
| **Company — Price action** | +62% H1, +80% YTD, 52-wk high $24.44, ~$23.86 mid-July | Jul 2026 | Strong momentum; extended vs. fundamentals |
| **Company — Analyst view** | Cantor Overweight $28 PT; Barron's 35% upside; Motley Fool top pick | Jun–Aug 2026 | Bullish consensus; supports upside case |
| **Company — Policy** | Lawmakers easing remittance tax on certain transfers | Jul 2026 | Tailwind for volumes/unit economics |
| **Company — Risk** | Sold off July 30 on Iran ceasefire collapse headlines | 2026-07-30 | High geopolitical beta; risk-off vulnerability |
| **Macro — Rates** | Fed funds 3.63% (hold); 10Y 4.63% (peak 4.75% Jul 31) | Aug 2026 | Higher-for-longer caps multiple expansion |
| **Macro — Inflation** | CPI −0.42% MoM; core PCE +0.13% | Jun 2026 | Disinflation supports consumer spending power |
| **Macro — Labor/Growth** | Unemployment 4.2% (falling); GDP +0.37% QoQ | Jun–Aug 2026 | Supports remittance income base |
| **Macro — Volatility** | VIX 15.81 (spiked 20.66 Jul 29, settled) | Aug 2026 | Risk appetite recovering after Hormuz scare |
| **Markets — Fed** | 88% probability of no 2026 rate cuts | Aug 2026 | No dovish catalyst expected |
| **Markets — Recession** | US recession by end-2026: 8% (−4.5pp WoW) | Aug 2026 | Low macro tail-risk for the trade |
| **Markets — Geopolitics** | US–Iran ceasefire by Aug 31: 88% (+29pp); Hormuz normal by Aug 31: 12% | Aug 2026 | Oil risk easing but unresolved; monitor Aug 15/31 |
| **Net Read** | Strong fundamental momentum + supportive macro vs. valuation stretch + 10Y yield/geopolitical overhangs | 2026-08-06 | Constructive bias; upside tied to earnings execution and de-escalation, downside tied to yields/geopolitics |

*Note: This is a news/macro research report for trading context, not a formal investment recommendation. Event dates to monitor: Hormuz traffic-normal resolution (Aug 15, Aug 31), Fed communications, and any remittance-tax legislation updates.*

### Fundamentals
I have all the data needed. Let me compile a comprehensive fundamental analysis report for Remitly Global, Inc. (RELY).

---

# Fundamental Analysis Report: Remitly Global, Inc. (RELY)
**Analysis Date:** 2026-08-06 | **Exchange:** NMS | **Sector:** Technology / Software – Infrastructure

## 1. Company Profile & Business Overview

**Remitly Global, Inc.** is a digital financial services platform focused on cross-border remittances and money movement, serving immigrant communities and their families worldwide. The company operates a mobile-first platform enabling international money transfers, and has been expanding into broader financial services (banking/money management products). It competes with traditional money-transfer operators (Wise, Western Union, MoneyGram) but differentiates via a fully digital, lower-cost, higher-transparency model.

**Key snapshot (as of 2026-08-06):**
| Metric | Value |
|---|---|
| Market Cap | $5.46B |
| Shares Outstanding | ~210.3M |
| Implied Share Price | ~$25.96 |
| 52-Week Range | $12.08 – $27.15 |
| Beta | 0.343 (low volatility) |
| TTM Revenue | $1.73B |
| TTM Net Income | $105.6M |
| TTM EPS | $0.52 |
| Forward PE | 15.70 |
| Book Value / Share | $4.13 |

**Price context:** The stock is trading near its 52-week high ($27.15), ~18% above its 50-day average ($21.95) and ~48% above its 200-day average ($17.54), reflecting strong positive momentum through the past year. The low beta (0.34) suggests this is a defensive-growth name that moves less than the broader market.

## 2. Income Statement — Profitability Transition Complete

### Annual revenue & profitability trajectory:
| Fiscal Year | Revenue | YoY Growth | Gross Margin | Operating Income | Net Income | Diluted EPS |
|---|---|---|---|---|---|---|
| 2022 | $653.6M | — | 50.0% | -$121.0M | -$114.0M | -$0.68 |
| 2023 | $944.3M | +44.5% | 56.4% | -$114.2M | -$117.8M | -$0.65 |
| 2024 | $1,264.0M | +33.9% | 59.2% | -$39.1M | -$37.0M | -$0.19 |
| 2025 | $1,635.1M | +29.4% | 60.2% | +$77.5M | +$67.9M | +$0.31 |

**2025 was the inflection year:** Remitly crossed into GAAP profitability for the first time, with net income of $67.9M and positive operating income of $77.5M. This came from continued strong top-line growth (~29% YoY) combined with meaningful operating leverage.

### Quarterly progression (latest data):
| Quarter | Revenue | Gross Margin | Operating Income | Net Income | Diluted EPS |
|---|---|---|---|---|---|
| Q1 2025 | $361.6M | 60.2% | $12.2M | $11.4M | $0.05 |
| Q2 2025 | $411.9M | 59.0% | $14.6M | $6.5M | $0.03 |
| Q3 2025 | $419.5M | 58.7% | $11.8M | $8.8M | $0.04 |
| Q4 2025 | $442.2M | 62.7% | $38.8M | $41.2M | $0.19 |
| **Q1 2026** | **$452.8M** | **62.1%** | **$53.7M** | **$49.1M** | **$0.23** |

**Q1 2026 (reported ~May 2026) was a standout quarter:**
- Revenue of $452.8M, up **+25.2% YoY** and +2.4% QoQ (accelerating into seasonally-strong H2)
- **Net income of $49.1M** — the largest quarterly profit in company history; net margin of 10.8% (vs. 3.1% in Q1 2025)
- Operating income margin expanded to **11.9%** (vs. 3.4% in Q1 2025), a ~850 bps YoY improvement
- Gross margin reached **62.1%**, up ~190 bps YoY

### TTM roll-up (Q2 2025 – Q1 2026):
- Revenue: **$1,726M** | Gross Profit: **$1,049M** (60.8% margin)
- Operating Income: **~$119M** | Net Income: **$105.6M** | EPS: **$0.52**
- Profit Margin: 6.1% | Operating Margin: 14.4% (SBC-adjusted basis, per fundamentals data)

### Expense structure (Q1 2026, % of revenue):
- Cost of revenue: 37.9% (improving, driven by FX and payout-channel efficiencies)
- R&D: $79.6M (17.6%) — continued product investment
- Sales & Marketing: $86.4M (19.1%) — the largest operating line; reflects customer-acquisition spend, with efficiency improving as revenue outpaces spend
- G&A: $55.1M (12.2%)

**Key insight:** The operating model is showing classic SaaS-like operating leverage. Every incremental revenue dollar is dropping to the bottom line at an increasing rate. TTM net income of $105.6M vs. a $37.0M net loss two years ago demonstrates a dramatic fundamental transformation.

## 3. Balance Sheet — Strong Liquidity, Low Leverage

### Capital structure evolution (annual):
| Metric | 2022 | 2023 | 2024 | 2025 | Q1 2026 |
|---|---|---|---|---|---|
| Total Assets | $696.0M | $1,036.3M | $1,012.9M | $1,458.7M | $1,385.8M |
| Cash & Equivalents | $300.6M | $323.7M | $368.1M | $542.4M | $649.1M |
| Total Debt | $9.2M | $143.0M | $16.3M | $192.1M | $39.3M |
| Stockholders' Equity | $480.1M | $529.3M | $665.5M | $868.8M | $907.4M |
| Retained Earnings | -$373.5M | -$491.3M | -$528.3M | -$460.3M | -$411.3M |

### Liquidity & solvency highlights:
- **Net cash position:** $649.1M cash vs. $39.3M total debt at Q1 2026 → **~$610M net cash** (a net cash position of ~11% of market cap)
- **Current ratio: 2.84** — very healthy short-term liquidity
- **Working capital:** $808.3M at Q1 2026 (up from $626.6M a year earlier)
- **Debt paydown:** The company drew a $155M term loan in Q4 2025 and **fully repaid it in Q1 2026** (Total Debt fell from $192.1M to $39.3M, which is now mostly capitalized leases). This confirms ample cash generation and no reliance on debt.
- **Accumulated deficit narrowing:** Retained earnings improved from -$528.3M (2024) to -$411.3M (Q1 2026) as profits accumulate.

**Note on D/E ratio:** The fundamentals feed shows Debt/Equity of 4.33, which is **inconsistent with the balance sheet** (actual total debt of $39M vs. equity of $907M ≈ 0.04x). This vendor figure appears distorted by the large gross revolving/settlement debt flows in the TTM cash flow statement (billions issued and repaid quarterly related to remittance float/custodial settlement, not economic leverage). Traders should rely on the balance-sheet view: **RELY is effectively debt-free with net cash.**

### Balance-sheet asset quality:
- Receivables of $315.9M and prepaid assets of $268.0M are largely tied to remittance settlement timing (customer funds in transit) — a normal feature of the money-transfer model, not credit risk
- Goodwill is modest ($54.9M, ~4% of assets), so no impairment overhang
- Net PPE of $70.1M is small — the business is asset-light

## 4. Cash Flow — Powerful FCF Engine

### Annual cash flow summary:
| Metric | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| Operating Cash Flow | -$108.7M | $66.8M | $111.6M | **$325.1M** |
| Capital Expenditure | -$7.1M | -$9.1M | -$17.7M | -$41.8M |
| **Free Cash Flow** | **-$115.7M** | **$57.7M** | **$93.9M** | **$283.3M** |

### Quarterly FCF:
| Quarter | Operating CF | FCF |
|---|---|---|
| Q1 2025 | $80.8M | $67.2M |
| Q2 2025 | $93.3M | $74.3M |
| Q3 2025 | $1.4M | $1.5M (seasonal trough) |
| Q4 2025 | $149.6M | $140.2M |
| **Q1 2026** | **$81.9M** | **$72.7M** |

### Cash flow insights:
- **FY2025 FCF of $283.3M** was ~3x the prior year — FCF margin of ~17% of revenue, a very high conversion rate for a fintech
- TTM FCF per fundamentals: **$181.7M** (Q3 2025's seasonal trough drags the TTM figure; the underlying run-rate is ~$290M+ annualized based on Q4'25/Q1'26)
- **CapEx is light** ($41.8M in 2025, ~2.6% of revenue) — the model is highly scalable with minimal fixed-asset intensity
- **Stock-based compensation** is significant: $155.1M in 2025 (9.5% of revenue), moderating to $27.5M in Q1 2026 (6.1% of revenue). This is the primary reason adjusted (non-GAAP) profitability is much higher than GAAP. SBC dilution is being partially offset by buybacks.
- **Share repurchases initiated:** $23.9M in 2025 and $42.5M in Q1 2026 — a new capital-return program signaling management confidence; share count stabilized at ~210.3M in Q1 2026
- Large gross debt issuance/repayment flows ($2-7B/quarter) reflect the custodial/float nature of remittance settlement (customer funds), not operating leverage

## 5. Valuation Analysis

| Valuation Metric | Value | Interpretation |
|---|---|---|
| Market Cap | $5.46B | — |
| P/E (TTM) | 49.9x | Elevated on trailing GAAP earnings |
| Forward P/E | 15.7x | Implies strong FY2026/27 EPS growth to ~$1.65 |
| P/B | 6.29x | Premium to book, typical of asset-light tech |
| EV (Mkt Cap − net cash) | ~$4.85B | — |
| EV/TTM Revenue | ~2.8x | Reasonable for a ~25-30% grower |
| EV/TTM EBITDA | ~34x (vendor) / ~28x (normalized quarterly roll-up) | Growth-adjusted |
| TTM FCF Yield | ~3.3% (on $181.7M) to ~5.2% (on $283M FY25) | Attractive for a growth company |

**Valuation takeaway:** On trailing earnings, RELY looks expensive (~50x), but the market is paying for the trajectory: Q1 2026 annualized net income of ~$196M, Forward P/E of ~15.7x, and a 25%+ revenue growth rate. If the company sustains Q1 2026's ~11% net margin, FY2026 EPS could plausibly land near $0.90-$1.00 GAAP (with forward adjusted EPS potentially higher), justifying the forward multiple.

## 6. Key Ratios & Quality Metrics

- **ROE (TTM):** 12.95% — solid, and rising quickly given the profit ramp
- **ROA (TTM):** 6.56%
- **Profit Margin (TTM):** 6.1% (up from -2.9% in FY2024)
- **Operating Margin (TTM, adj.):** 14.4%
- **Gross Margin (TTM):** ~60.8%, trending up (62.1% in Q1 2026)
- **Current Ratio:** 2.84
- **Effective Tax Rate:** ~5.8% in Q1 2026 (NOL carryforwards shield much of the taxable income; tax rate will normalize as NOLs are consumed)
- **Beta:** 0.343 — low correlation to market, defensive characteristics

## 7. Growth Drivers & Risks

### Growth drivers:
1. **Digital remittance penetration** remains in early innings; RELY has a leading mobile-first position with a low-cost model
2. **Operating leverage:** S&M and G&A as % of revenue are declining while gross margins expand (62%+); each marginal dollar is increasingly profitable
3. **Product expansion** beyond transfers (banking/money-management services) adds TAM and attach rates
4. **Seasonal strength:** Q4 (holiday remittances) and H2 are typically the strongest periods; Q4 2025 FCF of $140M shows the seasonal peak
5. **Balance-sheet optionality:** ~$610M net cash and $283M FY25 FCF fund expansion and the new buyback program without dilution risk

### Risks:
1. **Valuation dependence on growth delivery:** At ~50x TTM earnings, any growth deceleration or margin disappointment would compress the multiple
2. **SBC dilution:** $155M/yr of stock comp (9.5% of revenue) dilutes shareholders; offset only partially by buybacks
3. **Regulatory/FX exposure:** Cross-border payments carry regulatory, compliance, and currency volatility risks; FX movements can swing revenue and margins (note the $9.1M FX effect on cash in 2025)
4. **Competition:** Wise, PayPal/Xoom, Western Union, and banking incumbents are all investing in the same corridor economics; customer-acquisition costs (S&M = 19% of revenue) are the swing factor
5. **Tax normalization:** The ~6% effective tax rate benefits from NOLs; as these are used up, the tax burden rises, tempering net margin growth
6. **Seasonal lumpiness:** Q3 2025's FCF trough ($1.5M) demonstrates meaningful working-capital swings tied to settlement timing
7. **Data quirk to monitor:** The vendor-reported D/E of 4.33 is misleading (driven by settlement float); actual leverage is minimal — verify against the balance sheet before modeling credit risk

## 8. Actionable Insights for Traders

1. **Fundamental inflection confirmed:** RELY has transitioned from loss-making to a high-margin, high-FCF business. Q1 2026 (net income $49.1M, 10.8% margin) is the strongest quarter on record and sets up a strong FY2026 if the trajectory holds.
2. **Momentum alignment:** Price (~$26) is above both the 50-day ($21.95) and 200-day ($17.54) averages and near the 52-week high ($27.15) — the trend and fundamentals are aligned; watch for a breakout above $27.15 or resistance there.
3. **Forward PE of 15.7x** suggests sell-side consensus expects ~3x EPS growth into FY2026/27. A beat-and-raise cycle (like Q1 2026) is the primary catalyst to close the gap between trailing (49.9x) and forward (15.7x) multiples.
4. **Low beta (0.34) makes RELY a portfolio diversifier** — high-growth fundamentals with equity-market-like downside cushioning; but low beta also means less volatility-driven trading opportunity.
5. **Watch H2 seasonality:** Q4 is the seasonal FCF/revenue peak; Q3 tends to be a trough (Q3 2025 FCF was just $1.5M). Traders should not read Q3 softness as deterioration.
6. **Net cash + $283M FY25 FCF + buybacks** provide a shareholder-friendly floor under the stock; the $42.5M Q1 2026 buyback is a positive signal.
7. **Key catalysts to monitor:** quarterly earnings (next report ~Aug 2026 given Q2 2026 end), guidance raises, corridor/market expansion announcements, and any tax-rate guidance changes.

## 9. Summary Table

| Category | Key Point | Supporting Evidence |
|---|---|---|
| **Identity** | Remitly Global, Inc. — digital cross-border remittances/fintech | Software-Infrastructure, NMS, ~210.3M shares |
| **Revenue Growth** | Strong, durable 25-30% growth | FY25 +29.4% ($1.635B); Q1 2026 +25.2% ($452.8M) |
| **Profitability** | First GAAP-profitable year in 2025; record Q1 2026 | FY25 NI $67.9M; Q1 2026 NI $49.1M (10.8% margin) |
| **Margins** | Expanding across the board | GM 62.1% (Q1'26); OM 11.9% (Q1'26) vs 3.4% (Q1'25) |
| **Balance Sheet** | Net cash ~$610M; minimal real debt | Cash $649.1M vs debt $39.3M (Q1 2026) |
| **Cash Flow** | Powerful FCF generation | FY25 FCF $283.3M (~17% margin); Q1 2026 FCF $72.7M |
| **Liquidity** | Very strong | Current ratio 2.84; working capital $808.3M |
| **Capital Returns** | New buyback program underway | $23.9M (2025) + $42.5M (Q1 2026) repurchases |
| **Valuation** | Expensive on trailing, reasonable on forward | TTM P/E 49.9x; Forward P/E 15.7x; EV/Rev ~2.8x |
| **Momentum** | Price near 52-week high with strong trend | High $27.15 vs price ~$25.96; above 50/200-DMA |
| **Risk Profile** | Low market beta, seasonal FCF lumpiness | Beta 0.343; Q3 2025 FCF trough $1.5M |
| **Watch Items** | SBC dilution, tax-rate normalization, competition | SBC $155M (2025); effective tax ~6% (NOL-supported) |

**Bottom line:** Remitly's fundamentals have undergone a decisive, verifiable inflection — from deep losses to record profitability, ~$283M annual FCF, a net-cash balance sheet, and accelerating operating leverage, all while maintaining 25%+ revenue growth. The stock trades at a premium on trailing GAAP earnings but at ~15.7x forward earnings, implying the market expects the Q1 2026 profit trajectory to continue. The combination of strong momentum (price near 52-week high), low beta, and improving fundamentals makes RELY an attractive fundamental-growth candidate, with the key risk being multiple compression if growth decelerates or margins plateau.

## II. Research Team Decision

### Bull

Bull Analyst: **The Bull Case for RELY: This Isn’t a Momentum Story — It’s a Profitability Inflection Story**

Bear, I hear the objection before you even finish it: “RELY is up 80% YTD, it just printed a 52-week high, RSI is 66, the close is above the upper Bollinger Band, and Q3 guidance is only in-line. How much upside is actually left?”

Fair question. Now let me show you why it’s the wrong question.

---

### 1. The Growth Opportunity Is Still in Early Innings

Remitly is attacking a **$900B+ global remittance market** — that’s the World Bank-sized opportunity Barron’s just highlighted. RELY’s TTM revenue is roughly $1.7B. Do the math: this company has barely scratched the surface of its addressable market.

- **10 million active customers** — up 10x since 2019. That’s not a ceiling; that’s the base.
- Digital remittance penetration is still low. Legacy players built branches; Remitly built a mobile-first, lower-cost, higher-transparency platform.
- The model is scalable: **CapEx is only ~2.6% of revenue**. This is software infrastructure, not a capital-heavy lender.

The bear says “the growth is already priced in.” But a company growing revenue 20-25% with a fraction of 1% share of a $900B market is nowhere near “done.”

---

### 2. The Earnings Beat Wasn’t Just “Good” — It Was an Inflection

Look at the progression, because this is the heart of the bull case:

- FY2023: **net loss of -$117.8M**
- FY2024: **net loss of -$37.0M**
- FY2025: **net income of +$67.9M** — first GAAP-profitable year
- Q1 2026: **net income of $49.1M** — record at the time
- Q2 2026: **revenue +20% YoY to ~$495M**, **record adjusted EBITDA of $115M (23% margin)**, and **GAAP EPS crushed expectations**

This is not a one-quarter fluke. Gross margin expanded to **62.1%** in Q1 2026. Operating margin went from **3.4% to 11.9% year over year**. That’s the definition of operating leverage: the fixed infrastructure is already built, and every incremental dollar is dropping through to the bottom line at an increasingly higher rate.

The bear can call it “one good quarter.” I call it the confirmation of a multi-year structural transition.

---

### 3. Balance Sheet and Cash Flow Kill the “Dilution” Scare

Bear, you love to bring up stock-based compensation. Let’s put it in context:

- SBC was **9.5% of revenue in FY2025**, but moderated to **6.1% in Q1 2026** — the trend is improving.
- The company has initiated buybacks: **$23.9M in 2025 and $42.5M in Q1 2026**. Management is returning capital while still investing.
- Net cash position is roughly **$610M** — $649M cash vs. only $39M debt.
- FY2025 free cash flow was **$283.3M**, a ~17% FCF margin.

A company with that balance sheet doesn’t need to dilute shareholders to fund growth. It can self-fund, buy back stock, and still hold a war chest. The “dilution” argument is backward-looking and increasingly irrelevant.

---

### 4. Competitive Advantages Are Widening

The bear says Remitly is just another money-transfer app. That ignores the moat:

- **10M customers** create network effects, brand trust, and valuable corridor data.
- **Regulatory licenses** in key remittance corridors take years to replicate.
- **Mobile-first, lower-cost architecture** gives it a structural advantage over Western Union-style branch networks.
- It’s expanding beyond transfers into broader financial services — more attach rate, more revenue per customer, more TAM.

And the market is noticing. Barron’s published an explicit bullish call saying RELY **“can rally 35% as it disrupts global remittance markets.”** Cantor Fitzgerald had an Overweight with a $28 price target before the latest beat. The institutional narrative is constructive, not skeptical.

---

### 5. The Technical Setup Confirms the Fundamental Story

Let’s go to the tape, as of 2026-08-06:

- Price **$25.93** is above the 10 EMA ($24.08), the 50 SMA ($22.06), and the 200 SMA ($17.59).
- The **golden cross** from April is intact and the spread is widening.
- **MACD just printed a fresh bullish crossover** — histogram flipped from -0.02 to +0.11 on the breakout day.
- **Volume was 3-4x the recent average** — this breakout is real participation, not a head-fake.
- RSI is **66.30** — strong, but still below the 70 stall zone.

The bear will say “it’s extended above the Bollinger Band.” Fine. I’m not telling anyone to chase $27.15.

The disciplined bull entry is either:

- A pullback into **$24.1–$24.8**, or
- A confirmed daily close above **$27.15**.

And the invalidation is clear: a daily close below **$23.75** would break the 20-day SMA, the breakout shelf, and the 2x ATR level. That’s a defined-risk trade with an open upside.

---

### 6. Let Me Debunk the Bear’s Biggest Objections Directly

**“Valuation is too rich at ~50x trailing earnings.”**  
Trailing earnings are irrelevant right after an inflection. The stock trades at **~15.7x forward earnings** with an **EV/Revenue of ~2.8x** and a net cash balance sheet. You don’t value a company on the loss-making quarters from two years ago. You value it on the earnings power of a 10M-customer platform growing 20%+.

**“Q3 guidance is only in-line, not a big raise.”**  
In-line guidance at ~20% growth with record margins is not a problem. FY2026 guidance of **$1.978–1.988B** means the back half still needs to deliver ~$1.03B in revenue. That’s continued strong execution, not deceleration. And given management’s history, they tend to underpromise and overdeliver.

**“Sentiment is one-sided; Reddit is silent.”**  
Reddit silence is not a bearish signal. The news flow is uniformly bullish: Q2 beat, record EBITDA, 10M customers, Barron’s, Cantor, Zacks, StockStory. Retail chatter on StockTwits is 10-0 bullish among labeled messages. Sentiment is fuel, not the thesis. The thesis is fundamentals.

**“Macro: 10-year yields at 4.63%, no Fed cuts, Hormuz risk.”**  
The macro environment is actually supportive for remittance volumes: unemployment at **4.2%**, CPI decelerating, yield curve positively sloped, and recession odds only **8%**. The Iran/Hormuz headline caused a dip in July, but prediction markets now imply an **88% probability of an effective U.S.-Iran ceasefire by Aug 31** — and the VIX has settled back to 15.81. Plus, RELY has a **beta of 0.34**; it’s a low-volatility compounding story, not a high-beta momentum casino.

---

### The Bottom Line

The bear case is basically: “It’s gone up a lot, and it’s not cheap on trailing GAAP earnings.”

The bull case is stronger: Remitly is a profitable, net-cash, 20%-growing fintech platform with a massive TAM, a widening moat, record margins, fresh analyst upside calls, and a technically confirmed breakout. The stock has room to run — and even if it pulls back first, the entry zones and invalidation levels give us a disciplined way to own it.

**That’s why this is a BUY.**

Buy the pullback near **$24.10–$24.80**, or add on a confirmed close above **$27.15**. Keep your stop under **$23.75**, and let the fundamental inflection do the heavy lifting.

RELY isn’t just a momentum trade. It’s the market finally pricing in a company that has turned growth into profit. The bears are looking at the rearview mirror. I’m looking at the road ahead.
Bull Analyst: Bear, you made a logical, well-structured case. I’ll give you credit for that. But I’m going to show you why the “great company, bad price” argument collapses once you update the numbers, correct the valuation math, and put the technical “warning” in context.

Let’s go point by point.

## 1. The 50x trailing P/E argument is already stale

You keep leaning on the trailing P/E from the pre-Q2 snapshot. That is yesterday’s earnings power. The whole market just got the Q2 FY2026 print:

- Revenue **+20% YoY to ~$495M**
- Record adjusted EBITDA of **$115M — a 23% margin**
- GAAP EPS of **$0.93–$0.98** for Q2 alone
- **10 million active customers**

Do the math with Q2 included. At a **~$5.46B market cap** and roughly 210M shares out, TTM EPS is no longer $0.52. With the Q2 print layered in, TTM EPS lands around **$1.40**, which puts trailing P/E **under 19x** — not 50x.

A company growing revenue 20% with record margins and GAAP profitability at **under 19x trailing earnings** is not hyper-priced. It is reasonably priced for a durable compounder.

## 2. “Decelerating growth” is the wrong lens

Yes, revenue growth has gone from 44% to 34% to 29% to 20%. That is called scaling. It is not collapse.

Every year, the base gets bigger. The absolute dollar growth is still massive: Remitly added roughly **$370M in revenue in FY2025** and just printed another **~20% growth quarter** while *expanding* EBITDA margin to 23%.

Here’s the part you’re missing: the profit engine is accelerating even as the revenue growth rate normalizes. That is the exact setup that creates multi-year stock appreciation.

- FY2023: net loss of -$118M
- FY2024: net loss of -$37M
- FY2025: net income of +$68M
- Q2 2026: GAAP EPS of $0.93 in a single quarter

That is not a maturing, overvalued story. That is an operating inflection.

## 3. “In-line guidance” is not bad news

You’re treating Q3 guidance of ~$506M as if management failed to raise. But they just delivered a beat, record EBITDA, and a 10M customer milestone. Guidance that is *in line* with consensus still implies ~20% revenue growth.

Not every quarter has to be a blowout for the stock to go higher. The bull case is built on **execution over multiple years**, not one guidance raise. And Q2 itself came in *above guidance* — which is the pattern that matters.

## 4. The technical setup is not a warning — it’s confirmation

You point to the upper wick on August 6 and say “rejection.” I look at the same candle and see:

- **+7.7% close** versus the prior day
- A close at **$25.93**, the highest close in the dataset
- **3–4x** the recent average volume
- A fresh **MACD bullish crossover**
- RSI at **66.3**, still below the 70 stall zone
- Price above the 10 EMA, 50 SMA, and 200 SMA

Yes, there was an intraday wick from $27.15. That’s called volatility after a 7.7% breakout, not a reversal. The close was 5 cents below the open — noise. The close was **$1.86 above the prior close** — signal.

And I’m not telling anyone to chase it. My buy zones are **$24.10–$24.80** or a confirmed close above **$27.15**. A disciplined entry with a stop under **$23.75** is not stepping in front of a freight train. It’s defining risk.

## 5. The moat is real — and it’s widening

You say the moat is weak because Wise, PayPal, Western Union, and banks compete. But look at the evidence:

- Remitly has **10 million active customers**, up 10x since 2019.
- Gross margin is **62%+** and trending higher.
- Adjusted EBITDA margin hit **23%** — meaning the business is *not* being forced to buy growth with margin destruction.
- It has regulatory licenses, corridor density, and data advantages that take years to replicate.

The 19% sales-and-marketing spend isn’t a sign of weakness. It’s investment in a 10M-customer base that’s driving 20% revenue growth and record profitability. If customer acquisition costs were out of control, margins would be *falling*, not hitting records.

## 6. Macro is not the headwind you think it is

The base case is actually supportive:

- Unemployment at **4.2%** — supports remittance income
- CPI decelerating
- Yield curve positively sloped
- US recession odds only **8%**
- VIX back down to **15.81**

Yes, the 10-year is at 4.63%, and there’s no Fed cut expected in 2026. That is known and largely priced. And yes, Hormuz is a tail risk — but prediction markets now imply an **88% probability of a U.S.-Iran ceasefire by August 31**.

RELY also has a **beta of 0.34**. It is not a high-beta momentum casino. It’s a low-volatility, profitable growth company.

## 7. Sentiment being one-sided doesn’t mean “no one left to buy”

A tiny StockTwits sample with 10 bullish labels and 0 bearish labels is not evidence of a crowded trade. It’s evidence of a quiet, positive tape.

Institutional coverage is constructive: Barron’s sees 35% upside, Cantor is Overweight. The company has a **$5.46B market cap** in a **$900B remittance market**. That is not “fully owned.” That’s early innings.

## The risk/reward is in my favor

Let’s put it in concrete terms:

- Upside to Barron’s 35% call: **~$35**
- Invalidation stop under **$23.75**
- Reward-to-risk: roughly **4:1**

That is the bull case, Bear. Not “buy at any price” — but upside asymmetry at a moment when the company just proved it can convert 20% revenue growth into record profits.

RELY isn’t a story stock anymore. It’s a profitable, net-cash, 20%-growing fintech with a low beta and a massive addressable market. The bears can keep waiting for a 30% dip that may never come.

**I’m buying the pullback, or adding on the breakout — and I’m buying RELY.**
Bull Analyst: Bear, I appreciate the discipline. But your entire case rests on a handful of assumptions that don’t survive contact with the actual numbers. Let’s go through them one by one, because when you strip away the rhetoric, this is still a **BUY** — not because RELY is a “good story,” but because it’s a profitable, net-cash, 20%-growing fintech platform that the market is still under-appreciating.

---

## 1. The “One-Time Mirage” Argument Is a Red Herring

You keep hammering the “under 19x trailing P/E” claim as if I built the whole bull case on it. But step back: I don’t need Q2’s GAAP EPS to make the valuation argument. Use the operating numbers that are actually clean:

- Q2 FY2026 revenue: **~$495M, +20% YoY**
- Q2 adjusted EBITDA: **record $115M, 23% margin**
- Q1 FY2026 GAAP net income: **$49.1M**
- FY2025 free cash flow: **$283.3M**
- Net cash: **~$610M**
- Forward P/E: **~15.7x** — from consensus data, not my imagination

Even if you want to haircut the Q2 GAAP print for every conceivable one-time item, the core trajectory is undeniable. Annualize Q2’s $115M EBITDA and RELY trades at roughly **10–11x EV/EBITDA** on a ~$4.85B enterprise value. That is not a hyper-growth multiple. That is a reasonable multiple for a company growing revenue 20% with record margins and a net-cash balance sheet.

You want to argue the “quality of earnings”? Fine. The company generated **$283M of free cash flow in FY2025** and **$72.7M in Q1 2026 alone**. Real cash, not tax flattery. The bears keep focusing on one quarter’s EPS composition while ignoring the cash engine underneath.

---

## 2. “Decelerating Growth” Is Not the Same as “Bad Growth”

Yes, revenue growth has gone from 44% to 34% to 29% to 20%. That happens when you grow from $653M to $1.7B. The law of large numbers is not a fundamental flaw.

But here’s what matters: **the profit engine is accelerating.**

| Period | GAAP Net Income |
|---|---|
| FY2023 | **-$117.8M** |
| FY2024 | **-$37.0M** |
| FY2025 | **+$67.9M** |
| Q1 FY2026 | **+$49.1M** |
| Q2 FY2026 | Record adjusted EBITDA **$115M** |

That is the exact opposite of deterioration. Revenue growth is normalizing as the base scales, but the operating leverage is kicking in — gross margin is **62%+**, operating margins expanded from 3.4% to 11.9% year over year, and the company just posted a 23% adjusted EBITDA margin.

The bear wants you to pay for the past. I’m paying for the future earnings power of a 10-million-customer platform. And Q3 guidance of ~$506M still implies roughly **20% growth**. If that’s a “disappointment,” then every company on Earth should be so lucky.

---

## 3. The Moat Is Wider Than You Admit

You list Wise, PayPal/Xoom, Western Union, and banks as if their existence disproves Remitly’s competitive position. But Remitly has been competing against those names since day one — and has grown from zero to **10 million active customers** and **~$1.7B TTM revenue**.

Let’s put that in perspective: one market observer on StockTwits noted that RELY now has **more revenue than Western Union**. The company has:

- **10x customer growth since 2019.**
- Gross margins expanding to **62%+**.
- Regulatory licenses in corridors that take years to replicate.
- A mobile-first, lower-cost architecture vs. legacy branch networks.
- A **0.2% share of a $900B market** — meaning the runway is enormous even if competitors exist.

If this were a commodity business with no moat, gross margins would be collapsing as RELY “buys” growth. Instead, margins are **rising**, and adjusted EBITDA margin just hit a record 23%. That doesn’t happen when customer acquisition costs are out of control. It happens when the unit economics are improving.

S&M at 19.1% of revenue isn’t a sign of weakness — it’s investment. The proof is in the payoff: revenue is growing 20%, margins are at records, and the customer base just crossed 10 million.

---

## 4. The SBC/Buyback Math Is Moving in the Bull’s Direction

The bear loves to point out that FY2025 SBC of $155M exceeded buybacks of $23.9M. But that’s a trailing snapshot, not the trajectory.

Look at Q1 FY2026:

- Stock-based compensation: **$27.5M**
- Buybacks: **$42.5M**

**Buybacks exceeded SBC in the most recent quarter.** SBC as a percentage of revenue has also moderated from **9.5% in FY2025 to 6.1% in Q1 2026**. The share count has stabilized at roughly **210.3M shares**.

And remember: the company is generating **$283M of annual FCF** while still funding growth. That gives management the flexibility to offset dilution, buy back stock, and invest in expansion — all at the same time. The “dilution nightmare” is fading in the rearview mirror.

---

## 5. The Technical “Warning” Is Actually a Breakout

You call the August 6 candle a “rejection wick.” Let’s look at what actually happened:

- Close: **$25.93** — the highest close in the dataset
- Prior close: **$24.07** — so RELY gained **+7.7%**
- Volume: **8.33M shares** — roughly **3–4x** the recent average
- MACD: fresh **bullish crossover**
- RSI: **66.3** — strong but still below the 70 stall zone
- Trend: price above 10 EMA, 50 SMA, and 200 SMA; golden cross intact

Yes, there was an intraday spike to $27.15 and a fade into the close. But the close was **$1.86 above the prior close** and in the upper portion of the day’s range. That’s not a rejection pattern — that’s volatility on a volume-backed breakout.

And I’m not asking anyone to chase. My plan is clear:

- **Pullback entry: $24.10–$24.80**
- **Breakout entry: confirmed close above $27.15**
- **Invalidation: daily close below $23.75**

The reward-to-risk from the pullback zone to Barron’s ~$35 target is still heavily in the bull’s favor — roughly **4:1 or better** depending on fill. If you’re worried about ATR whipsaw, size the position accordingly. That’s what risk management is for.

---

## 6. One-Sided Sentiment Is Not a Contrarian Signal

You say the StockTwits tape is 10-0 bullish and Reddit is silent, so “who’s left to buy?”

I see it differently.

Reddit silence means the broader retail crowd **hasn’t piled in yet**. Institutional coverage is positive: Barron’s sees 35% upside, Cantor is Overweight, Zacks and StockStory both flagged the earnings beat. The sentiment report scores RELY **7.2/10 Bullish** — constructive, not euphoric.

If this were a crowded, fully-owned trade, you’d see Reddit threads everywhere and a 10-0 labeled StockTwits sample would be the norm. Instead, you have a quiet, positive tape and a company that just reported a **+269% earnings surprise** and crossed a major customer milestone. That’s not a top signal. That’s a story still in its early innings.

---

## 7. Macro Is Not the Headwind You Think It Is

You’re pointing at the 10-year yield at 4.63% and Hormuz risk. But RELY has rallied **80% YTD** *with* the 10-year at these levels. The market has already absorbed the “higher for longer” reality.

The macro backdrop is actually supportive for remittances:

- Unemployment at **4.2%** and falling — supports immigrant labor income
- CPI decelerating — supports consumer purchasing power
- Recession odds: **8%** — low tail risk
- Yield curve positively sloped — no recession signal
- VIX back to **15.81** — risk appetite recovering
- U.S.-Iran ceasefire probability by Aug 31: **88%** — geopolitical risk easing

RELY also has a **beta of 0.34**. That means it is not a high-beta momentum casino. It’s a low-volatility compounder. If the market de-risks, RELY should decline *less* than the averages — and if the oil scenario doesn’t materialize, the stock has significant upside headroom.

---

## The Bottom Line

Bear, you’re making a very disciplined bear argument. I respect that. But the discipline is focused on the wrong metrics.

You’re using:

- A trailing P/E that ignores the forward earnings power,
- A growth deceleration narrative that ignores the profit acceleration,
- A technical “rejection” that ignores the highest close in the dataset,
- And a sentiment concern that ignores the fact that institutional ownership is still building.

RELY is a **profitable, net-cash, 20%-growing fintech with a 10-million-customer base, a 62% gross margin, record EBITDA, a $900B market opportunity, and a forward P/E near 15.7x.**

That’s not a momentum trade. That’s a fundamental inflection.

**I’m buying RELY.** I’ll buy the pullback near **$24.10–$24.80**, or add on a confirmed close above **$27.15**. My risk is defined below **$23.75**, and my upside is the Barron’s $35 target and beyond.

The bears are worried about the price. I’m focused on the value — and the value keeps compounding.
Bull Analyst: Bear, you say I’ve repeated myself three times. The truth is, I’ve updated the evidence as it came in — and the latest evidence keeps making the bull case stronger. You keep calling this a “great company, bad price” story. But every time you try to prove the price is bad, you have to ignore the most important numbers. Let’s go one final round.

## 1. The “tax artifact” argument is actually a gift to the bull

You’ve figured out that Remitly has NOLs and a low effective tax rate. Great — that’s not a mirage, that’s a real balance-sheet asset that shields cash taxes for years. And even if I completely throw out Q2 GAAP EPS, the bull case doesn’t break.

Look at the cash engine:

- FY2025 free cash flow: **$283.3M**
- Q1 2026 free cash flow: **$72.7M**
- Net cash: **~$610M** — $649M cash against just $39M debt
- Enterprise value: roughly **$4.85B**

That puts RELY at about **17x FY2025 FCF** for a company growing revenue ~20% with record margins. That is not a hyper-growth momentum multiple. That is a reasonable multiple for a profitable, net-cash compounder. You want to argue about one quarter’s tax line? Fine. The cash flow doesn’t care about your tax-line objection.

## 2. “Annualizing the best quarter” — no, I’m following the multi-year trend

You say I’m annualizing one good quarter. I’m not. I’m looking at the sequence:

- FY2023: **-$117.8M** net loss
- FY2024: **-$37.0M** net loss
- FY2025: **+$67.9M** net income — first GAAP-profitable year
- Q1 2026: **+$49.1M** net income, record at the time
- Q2 2026: **record $115M adjusted EBITDA**, 23% margin, GAAP EPS crushed estimates

That is not a one-quarter story. That is a structural profitability inflection. Revenue growth is normalizing because the base is getting bigger — but the profit margin is expanding. That’s the exact combination that builds multi-year stock gains.

And the “in-line guidance” scare? Q2 revenue came in **above guidance**. Management’s pattern is to guide conservatively, then beat. Q3 guidance of ~$506M still implies ~20% growth. A 20% grower with a 23% EBITDA margin does not need to raise guidance every single quarter to be a good investment.

## 3. Decelerating revenue growth is not deteriorating quality

Yes, growth went from 44% to 34% to 29% to ~20%. That’s what happens when revenue goes from $653M to a ~$2B run rate.

But let’s put the absolute growth in perspective:

- FY2024 added roughly **$320M** of revenue
- FY2025 added roughly **$371M** of revenue
- A 20% grower at $2B adds roughly **$400M a year**

The “deceleration” is a base effect, not a collapse. Meanwhile, the company went from losing $118M to generating $283M of free cash flow in two years. If that’s “maturing,” I want more mature companies.

## 4. SBC and buybacks: you’re using last year’s math

The bear keeps pointing to FY2025 SBC of $155M vs. buybacks of $23.9M. But what happened in the most recent quarter?

- Q1 2026 SBC: **$27.5M**
- Q1 2026 buybacks: **$42.5M**

Buybacks exceeded stock compensation. SBC as a percentage of revenue fell from **9.5% to 6.1%**. The share count stabilized at ~210.3M. The buyback program is new and accelerating. A one-year-old snapshot is not the trajectory.

And even with SBC as a real expense, RELY is still GAAP-profitable and FCF-positive. The “adjusted EBITDA adds back SBC” critique doesn’t change the fact that the company produced $72.7M of FCF in Q1 alone.

## 5. The August 6 candle is not a rejection — it’s a higher close

You keep pointing to the wick. Let me point to the close.

- The previous high close was **$25.75** on July 16.
- The August 6 close: **$25.93** — a **new closing high**.
- Volume: **8.33M shares**, roughly 3–4x the recent average.
- MACD: fresh bullish crossover.
- RSI: **66.3**, still below the 70 level that stalled the stock twice in July.

If the breakout had failed, RELY would have closed below $25.75. It didn’t. It closed above the old high on huge volume. The intraday spike to $27.15 and fade was fast money taking profits after a 7.7% move. The close is the signal.

And my trade plan isn’t “chase at $27.” My plan is:

- Buy the pullback into **$24.10–$24.80**
- Or add on a confirmed close above **$27.15**
- Invalidation: daily close below **$23.75**, which converges with the 20-day SMA and the breakout shelf

From $24.50, risk to $23.75 is about $0.75. Upside to Barron’s ~$35 target is over $10. That’s a reward-to-risk of more than **10:1**. The bear says the entry risks whipsaw — that’s what position sizing is for. The setup is not “buy at any price.” It’s “define your risk and let the fundamental trend work.”

## 6. The moat is wider than you admit

You call Remitly a customer-acquisition treadmill because S&M is 19% of revenue. But if that were true, margins would be collapsing — not hitting records.

What actually happened:

- Gross margin: **62%+** and rising
- Adjusted EBITDA margin: **23%**, a record
- Revenue growth: **~20%** while margins expand

That means the customers it acquires are becoming profitable faster. That’s not a treadmill. That’s a well-oiled acquisition engine with improving unit economics.

10 million active customers, 10x since 2019, in a $900B market — that’s still roughly **0.2% penetration**. The runway is enormous. Regulatory licenses, corridor density, and brand trust in immigrant communities are not trivial to replicate. Remitly has been competing with Wise, PayPal/Xoom, and Western Union from day one and has grown to more revenue than Western Union — according to market observers. That’s not a company being crushed by competition. That’s a company taking share.

## 7. Quiet sentiment is not a contrarian top signal

You say StockTwits being 10-0 bullish and Reddit being silent means “who’s left to buy?”

I see it the opposite way. Reddit silence means the broader retail crowd **hasn’t discovered it yet**. The sentiment score is **7.2/10** — constructive, not euphoric. Institutional coverage is positive but not mania: Barron’s sees 35% upside, Cantor had an Overweight target at $28, Zacks and StockStory both flagged a beat-and-raise cycle.

When RELY is all over Reddit with rocket emojis, I’ll start worrying. A quiet, positive tape after a major earnings inflection is exactly the kind of setup that still has room to run.

## 8. Macro is a manageable overhang, not a dealbreaker

The 10-year at 4.63%? That’s the backdrop of an **80% YTD rally**. Higher-for-longer is already known and largely priced. No Fed cuts? The market knows that too.

Meanwhile:

- Unemployment is **4.2%** — supportive for remittance income
- CPI is decelerating
- US recession odds: **8%**
- Yield curve is positively sloped
- VIX back to **15.81**
- U.S.–Iran ceasefire odds by Aug 31: **88%**, up 29 points week over week

The Hormuz story is a real tail risk. But it’s a tail risk, not the base case. And if the market does de-risk, RELY has a beta of **0.34** — it should fall less than the broader market. Meanwhile, the upside from here is a profitable, net-cash, 20%-growing fintech in a massive market. That’s asymmetric.

## Final word

Bear, you keep saying the market is “priced for perfection” and the stock is “priced as if the next five years have already happened.”

But a company with:

- 10 million customers
- $610M net cash
- $283M FY25 FCF
- 23% adjusted EBITDA margin
- 20% revenue growth
- A ~$1.98B FY revenue guide
- And a $900B TAM

...trading at roughly 17x FY25 FCF and ~15.7x forward earnings is not priced for perfection. It’s priced for what the company just proved it can do.

You’re looking at the rearview mirror — 50x trailing GAAP, one-time tax benefits, a wick on one candle. I’m looking at the fundamental trajectory — profits, cash, customers, and a massive market that’s still barely penetrated.

RELY is a great company — and at these levels, it’s also a great risk/reward.

**BUY RELY.** Buy the pullback near $24.10–$24.80, or add on a confirmed close above $27.15. Invalidation below $23.75. Let the compounding do the rest.
Bull Analyst: # Bull Analyst — Final Word: “The Bear Keeps Fighting the Last War. RELY Is Winning the Next One.”

Bear, I’m going to give you credit where it’s due: you have consistently focused on the metrics that *used* to matter for RELY — the trailing P/E from a pre-inflection era, the revenue growth deceleration curve, the SBC drag from two years ago, and a single intraday wick on a record-volume breakout day.

But here’s the problem with your entire framework, laid out plainly: **you are treating a profitability inflection as if it’s already fully complete, and treating a 20% grower with a 23% EBITDA margin and $610M net cash as if it’s a maturing utility.** The data says otherwise. Let me show you — one final time, with the actual numbers — why the bull case is not just stronger, it’s the only case that correctly prices the next 12 months.

---

## 1. You Keep Moving the Goalposts on Valuation. Let Me Plant the Flag.

You accused me of “rotating through valuation frameworks.” Let me be direct: I’m not rotating to confuse anyone. I’m showing you that **every honest framework points to the same conclusion** — RELY is reasonably valued for what it now is.

**Frame 1: EV/Revenue.** RELY trades at roughly **2.8x EV/Revenue** on TTM revenue of ~$1.73B. For a company growing top line 20% with a 62% gross margin and a net-cash balance sheet, that is not a hyper-growth multiple. That’s a reasonable growth multiple.

**Frame 2: EV/EBITDA.** Annualize Q2 2026’s record **$115M adjusted EBITDA** — a figure the company *actually delivered*, not a projection — and that’s roughly **$460M in run-rate EBITDA**. Against an enterprise value of ~$4.85B, that’s **~10.5x EV/EBITDA**. Even if you haircut that by 20% to account for seasonality, you’re still at ~13x. A 20% revenue grower with expanding margins at 10–13x EBITDA is not “priced for perfection.” It’s priced for execution — which the company just delivered.

**Frame 3: Forward P/E.** 15.7x forward earnings based on the current earnings trajectory. The bear says that assumes a “hockey stick.” But the company just guided FY2026 revenue to **$1.978–1.988B**, which implies ~20% growth with record margins already in hand. Q1 delivered $49.1M GAAP net income. Q2 delivered GAAP EPS of $0.93–$0.98. The “hockey stick” is not hypothetical — it’s already happening.

And for my final point on the bear’s favorite attack: even if we completely zero out Q2’s GAAP EPS as a “tax artifact,” the **core earnings power is undeniable** — $283M FY2025 FCF, $72.7M Q1 2026 FCF, record 23% adjusted EBITDA margin. You cannot tax-artifact away cash flow.

---

## 2. The “Decelerating Growth” Argument Ignores the Profitability Acceleration

This is the heart of your case, so let me address it head-on.

Yes, revenue growth has gone from 44% to 20% over three years. That is what happens when a company scales from $653M to ~$2B in revenue. It’s called the law of large numbers — and it’s not a bug, it’s a feature.

But look at what happened at the **same time**:

| Period | Revenue Growth | Net Income / Adjusted EBITDA |
|---|---|---|
| FY2023 | +44.5% | **-$117.8M** net loss |
| FY2024 | +33.9% | **-$37.0M** net loss |
| FY2025 | +29.4% | **+$67.9M** net income, **$283.3M FCF** |
| Q1 2026 | +25.2% | **+$49.1M** net income, **$72.7M FCF** |
| Q2 2026 | ~+20% | **$115M record EBITDA, 23% margin** |

The bear story is: “Growth is slowing.” The bull story is: **The profit engine is accelerating.** It went from losing $118M to generating $283M in free cash flow in two years, while gross margins expanded from 50% to 62% and EBITDA margins hit a record 23%.

That is not a company in decline. That is a company hitting its operating leverage inflection point — the exact moment when revenue growth starts converting disproportionately to profit. **That is precisely where multi-year stock gains are created.**

---

## 3. The Technical “Rejection” Is Actually a Confirmed Breakout

Bear, you keep looking at the intraday wick to $27.15 and calling it a failure. Let me put the full candle in context:

- **Close: $25.93 — a new all-time closing high.** The prior high close was $25.75. RELY closed *above* it on the most important day of the recent cycle.
- **Volume: 8.33M shares — roughly 3–4x the recent average.** This is institutional participation, not a low-volume head-fake.
- **MACD: fresh bullish crossover** — histogram flipped from -0.02 to +0.11 on the breakout day.
- **RSI: 66.3** — strong, but below the 70 stall zone that marked July pullbacks. There is still momentum headroom.
- **Trend structure:** Price above 10 EMA ($24.08) → 50 SMA ($22.06) → 200 SMA ($17.59). Golden cross intact. Every layer of trend is aligned bullish.

Yes, there was a fade from the high. That happens on a 7.7% breakout day when short-term traders take profits. The market’s verdict is the **close**, and the close was a **new high on 3–4x volume with a fresh MACD crossover**. That’s not a rejection pattern — that’s a breakout.

And my trade plan protects you either way:

- **Pullback entry: $24.10–$24.80** — the rising 10 EMA and the top of the breakout base
- **Breakout entry: confirmed daily close above $27.15**
- **Invalidation: daily close below $23.75** — converging with the 20-day SMA and the breakout shelf

From $24.50, risk to $23.75 is $0.75. Upside to the Barron’s $35 target is over $10. **That is better than 10:1 reward-to-risk.** The bear calls that a “coin flip.” I call it the best risk/reward in fintech right now.

---

## 4. The Moat Is Real, and the Numbers Prove It’s Widening

Your “treadmill” argument claims RELY is buying growth with 19.1% S&M spend. But if that were true, **margins would be contracting, not expanding to records.**

Here’s what actually happens when a company has a customer-acquisition treadmill:

- Gross margins stagnate or shrink
- EBITDA margins compress
- Customer acquisition costs rise faster than revenue

Here’s what RELY is doing:

- **Gross margin: 62.1% in Q1 2026, up 190 bps YoY — expanding**
- **Adjusted EBITDA margin: 23% — a record**
- **Revenue growth: 20% while margins expand**

That is the opposite of a treadmill. That is a **scalable acquisition engine with improving unit economics**. The company is spending to acquire customers, and those customers are becoming profitable faster than the spend grows. That’s how you get from -$118M to +$68M net income in two years.

And on competition: RELY has been fighting Wise, PayPal/Xoom, Western Union, and MoneyGram since day one. The result? **10 million active customers, up 10x since 2019. More revenue than Western Union, according to market observers. A 62% gross margin.** In a $900B market, RELY has roughly **0.2% share**. The opportunity is enormous, and the company is winning.

---

## 5. SBC and Buybacks: The Trend Is Your Friend

You keep quoting FY2025 SBC of $155.1M vs. $23.9M in buybacks. That’s a historical snapshot, and it’s already outdated.

**The most recent quarter:**
- Q1 2026 SBC: **$27.5M**
- Q1 2026 buybacks: **$42.5M**

**Buybacks exceeded SBC in the most recent quarter.** SBC as a percentage of revenue fell from **9.5% to 6.1%**. Share count stabilized at ~210.3M. The buyback program is new and ramping — management just proved with actual cash that they believe the stock is worth buying.

And let me add one more thing: the company generated **$283M in FY2025 FCF** and holds **~$610M net cash**. It can fund buybacks, invest in growth, and expand into new markets — all without dilution. That is the opposite of a share-count problem.

---

## 6. Sentiment Being Quietly Positive Is Not a Top Signal

You say StockTwits being 10-0 labeled bullish and Reddit silent means “who’s left to buy?”

I say: Reddit silence means the broader retail crowd **hasn’t piled in yet**. When this stock is all over Reddit with rocket emojis and meme-level enthusiasm, *then* I’ll worry about crowding. Right now, the sentiment score is **7.2/10 Bullish** — constructive but not euphoric. Institutional coverage is positive but not mania: Barron’s sees 35% upside, Cantor is Overweight, Zacks and StockStory flagged the beat.

The bear says “the story is fully transmitted.” But RELY is a **$5.46B market cap company in a $900B market**. That is not a fully-owned, everyone-has-heard-the-story situation. That is a company with **0.2% penetration** of its addressable market, in the early stages of institutional adoption.

---

## 7. Macro Is a Manageable Overhang, Not a Dealbreaker

Let’s be clear about what the macro data actually says on 2026-08-06:

- **Unemployment: 4.2% and falling** — this supports remittance volumes directly. Immigrant labor income is the fuel for RELY’s business.
- **CPI decelerating, down 0.42% month-over-month** — disinflation supports consumer purchasing power in remittance corridors.
- **US recession odds: 8%** — that means a 92% probability of *no* recession. There is no macro tail risk in the base case.
- **Yield curve positively sloped: 10s-2s at +0.44%** — no recession signal from the curve.
- **VIX settled back to 15.81** from the Hormuz spike to 20.66. Risk appetite is recovering.
- **U.S.-Iran ceasefire odds: 88% by Aug 31, up 29 points week-over-week.** The geopolitical risk that spiked on July 30 is de-escalating.

Yes, the 10-year is at 4.63% and the market expects no Fed cuts in 2026 — **but that’s the backdrop of an 80% YTD rally.** The market has already absorbed higher-for-longer. And with a **beta of 0.34**, RELY falls less than the market in risk-off episodes while still delivering a 20%-grower’s upside in risk-on phases. That is an asymmetric profile in the bull’s favor.

---

## 8. “No Catalyst” Is the Weakest Bear Argument of All

The bear asks: “What’s the next catalyst?”

Let me list what’s actually on the calendar:

1. **Q3 FY2026 earnings** — due in roughly 90 days. Management’s pattern is to guide conservatively, then beat. Q2 came in *above* guidance. The next print is a live catalyst.
2. **Q4 seasonal strength** — Q4 is Remitly’s strongest quarter for revenue and FCF (Q4 2025 FCF was $140.2M). We are entering the seasonally strongest part of the year.
3. **Remittance tax policy tailwind** — lawmakers are already working on easing remittance taxes on certain transfers. That’s a direct volume and unit-economics catalyst.
4. **Product expansion beyond transfers** — the company is building broader financial services on top of its 10M-customer base. Every new product is a new revenue line.
5. **Institutional adoption** — a $5.46B cap in a $900B market, with a 7.2/10 sentiment score and Reddit still silent, is not fully-owned. Institutional money is still in early innings.
6. **Guidance raise potential** — the company beat in Q2 and guided Q3 in line. If Q3 comes in above guidance — which is management’s historical pattern — the next guide could be raised, resetting forward estimates higher.

A company growing 20% with record margins, entering its seasonally strongest period, with a beat-and-raise pattern, in the early stages of institutional adoption — that’s not “no catalyst.” That’s a pipeline of catalysts.

---

## The Real Risk/Reward Math

Let’s do the honest risk/reward at $25.93:

**Upside:**
- Barron’s target: **~$35** — **+35%**
- Cantor Overweight target: **$28** — **+8%** (published *before* the Q2 beat)
- If the seasonally strong H2 delivers another beat-raise cycle, fair value based on 15-18x forward earnings on FY2027 estimates is **$35–40** — **+35% to +54%**

**Downside:**
- My invalidation is a daily close below **$23.75** — the 20-day SMA, the breakout shelf, and the 2x ATR confluence. That’s **-8.4%** from current price.
- Even a pullback to the 50-day SMA at **$22.06** would be **-15%** — and that would be a buying opportunity, not a disaster, in the context of a maintained uptrend.

From the pullback entry of **$24.50**, the risk to invalidation is **$0.75**, and the upside to the Barron’s target is **$10.50**. **That is a 14:1 reward-to-risk setup.**

The bear says the downside to the 200-day SMA is -32%. That would require a complete breakdown of the fundamental story — the profitability inflection, the 10M customer base, the 62% gross margins, the net-cash balance sheet. I’m not paying for that scenario. I’m paying for the one the company just proved it can deliver.

---

## The Bottom Line

Bear, you came into this debate with a clear thesis: *“Great company, bad price.”*

But here’s what you couldn’t do:

- You couldn’t explain why a 20% top-line grower with a 23% EBITDA margin, $283M in FCF, and $610M net cash deserves to be avoided at a forward P/E of 15.7x and an EV/EBITDA of ~10-13x.
- You couldn’t explain why the first GAAP-profitable year in company history, followed by a record Q1 and a record Q2, is somehow a negative.
- You couldn’t explain why a fresh all-time closing high on 3-4x volume with a MACD crossover is a “rejection” while a quiet tape with no participation would somehow be better.
- And you couldn’t reconcile “the stock is overvalued” with “the company is growing revenue 20%, expanding margins to record levels, and still holds 0.2% share of a $900B market.”

The bear case rests on a trailing P/E from a pre-inflection era, a single candle wick, and a fear of catalysts that are actually lining up. The bull case rests on **what the company just proved it can do — profitably, with real cash, in a massive market.**

RELY has turned the corner. It is no longer a story stock. It is a profitable, net-cash, 20%-growing fintech platform entering its seasonally strongest period, with institutional coverage still building, and a market opportunity that remains barely penetrated.

That’s not priced for perfection. That’s priced for what’s already happening — and the market is still early in recognizing it.

**BUY RELY.**

Buy the pullback into **$24.10–$24.80**, or add on a confirmed daily close above **$27.15**. Invalidation below **$23.75**. Let the compounding do the rest.

The bears can wait for a 30% dip — and watch it never come. I’m investing in the profitability inflection that’s already here.

### Bear

Bear Analyst: **Bear Analyst: “You’re Not Buying a Great Company — You’re Buying a Great Story at the Worst Time.”**

Bull, I’ll give you credit: that was a polished pitch. You hit all the high notes — $900B TAM, 10 million customers, record EBITDA, net cash, golden cross. If you’d made this argument six months ago, I’d have nodded along.

But you’re making it **after** RELY is up 80% YTD, after it printed a 52-week high, after a one-day 7.7% spike on 3–4x volume, after closing above the upper Bollinger Band, and after the company guided **in line** for Q3, not above. That’s not the time to be a buyer. That’s the time to ask what’s already priced in.

Let me show you why the bull case is really a case for patience, not purchase.

---

## 1. The Growth Story Is Decelerating — Not Accelerating

The bull wants you to believe this is “early innings” in a massive market. But look at the actual revenue trajectory:

- FY2023: **+44.5% YoY**
- FY2024: **+33.9% YoY**
- FY2025: **+29.4% YoY**
- Q1 2026: **+25.2% YoY**
- Q2 2026: **~+20% YoY**

That is a clean, uninterrupted deceleration. Every single year, growth has slowed. The $900B market story sounds great, but RELY is growing *slower* now than it was two years ago — while trading at a **~50x trailing GAAP P/E** (based on TTM net income of $105.6M through Q1 2026) and an **EV/EBITDA in the high-20s to mid-30s**.

You’re not buying an inflection; you’re buying a company that’s maturing — and paying a hyper-growth multiple for it.

---

## 2. The “Profitability Inflection” Is Real, But the Market Already Knows

Yes, Remitly turned GAAP-profitable. Yes, Q2 was a beat. But the stock didn’t just rise in a vacuum — it’s up **~80% YTD** and sitting near its all-time high **$27.15**. The question isn’t “did Remitly execute?” It’s “how much of that execution is already in the price?”

Consider the most dangerous parts of the bull’s own evidence:

- **Q3 guidance of ~$506M is only in line with consensus.** After a monster earnings beat, management did not raise the bar. That tells me the Q2 beat may have pulled forward demand or benefited from one-time timing. There is no fresh catalyst to push the stock higher from here.
- **Forward P/E of ~15.7x sounds cheap, but it assumes EPS roughly triples from trailing levels.** You’re being asked to pay today for a hockey-stick that hasn’t happened yet. If Q3 or Q4 disappoints even slightly, that forward multiple expands — and the stock de-rates fast.
- **Stock-based compensation is the elephant in the room.** RELY burned **$155M in SBC in FY2025** — that’s 9.5% of revenue. The buybacks you cite? **$23.9M in 2025 and $42.5M in Q1 2026** — combined, they cover less than half of last year’s SBC. Management is *still* diluting shareholders; the buyback is a PR gesture, not a capital-return program.

The “inflection” is real. It’s also priced in.

---

## 3. The Technical Setup Is a Short-Term Warning, Not a Buy Signal

You pointed to the golden cross, the MACD crossover, and the volume expansion. Fine. But let’s look at what the tape *actually* did on the breakout day:

- Open: **$25.98**
- High: **$27.15**
- Low: **$24.11**
- Close: **$25.93**

RELY tagged a new high, then gave back **more than $1.20 from the highs** and closed *below its open*. That is not a clean breakout candle — that’s a **rejection wick**.

Add this:

- RSI is **66.3** — just below the **70 level** where RELY stalled twice in July, leading to multi-percent pullbacks.
- ATR is **$1.09**, the highest in the lookback. The stock is suddenly *twice as volatile* as it was a month ago.
- Price closed **1.5% above the upper Bollinger Band (25.55)**. Mean reversion is the base case, not the exception.

You say “buy the pullback at $24.10–24.80 and stop at $23.75.” That’s a 4–8% loss if the stop hits, and with an ATR over a dollar, a normal overnight move can trigger it. You’re asking investors to step in front of a freight train and hope it pauses politely at the 10 EMA.

---

## 4. The “Moat” Is Not as Wide as the Bull Claims

Remitly is a good digital remittance company. But “good” is not “moat.”

- **Wise** is the low-cost digital leader in cross-border payments.
- **PayPal/Xoom**, **Western Union**, and **MoneyGram** have decades of regulatory licenses, corridor relationships, and brand trust.
- **Banks and neobanks** are embedding remittance into their own apps.

How is RELY defending itself? By spending **19.1% of revenue on Sales & Marketing**. That’s the largest operating expense line. The “operating leverage” story only works if customer acquisition costs don’t keep rising. But in a crowded, price-transparent market, **every competitor can undercut on fees**. Remittance customers are notoriously price-sensitive and have almost zero switching costs.

The 10 million customer milestone is nice. But 10 million customers in a $900 billion market also tells you how much competition exists — and how much RELY has to spend to win each one.

---

## 5. Macro Is Not Your Tailwind — It’s Your Overhang

The bull says the macro is supportive. Let’s check the *actual* setup:

- **10-year Treasury at 4.63%**, recently peaked at 4.75%.
- Market-implied probability of **no Fed cuts in 2026: 88%**.
- **Hormuz/Strait of Hormuz risk**: only **12% probability** of traffic normalization by Aug 31, and **40% probability** Iran charges fees by Oct 31.

That last one is critical. An oil shock would:

1. Push inflation higher,
2. Force the Fed to stay hawkish,
3. Drive the 10-year up,
4. Compress the multiple on every high-growth software stock, including RELY.

RELY already demonstrated its geopolitical beta on **July 30**, when it sold off alongside other growth names on Iran ceasefire headlines. A low beta of 0.34 doesn’t protect you from a sector de-rating; it just means RELY won’t fall as fast as ARKK. But it also won’t rise as fast in a risk-on melt-up.

You’re paying a premium for a stock with no near-term Fed catalyst and real oil tail-risk.

---

## 6. Sentiment Is One-Sided — and That’s a Warning, Not Validation

You point to StockTwits being 10-0 bullish among labeled messages. I see that differently: **a tiny sample where nobody disagrees** is exactly the setup you see at short-term tops.

Reddit? Silence. r/stocks and r/investing have nothing substantive on RELY. That means the broader retail crowd isn’t participating — so who’s the marginal buyer after today’s spike?

And among the few skeptics who *are* watching, the comments are telling:

> “Valuation still looks wrong… it needs to show me, not tell me.”
> “SBC outweighing buybacks.”

The news flow is uniformly bullish — Barron’s, Zacks, StockStory, Cantor — which means the bullish thesis has been fully transmitted to the market. **When everyone already owns the story, there is no one left to buy it.**

---

## Final Word

Bull, I’m not saying Remitly is a bad company. It’s a solid, growing, now-profitable fintech. But a good company is not the same thing as a good investment at any price.

At **$25.93**, you are:

- Paying **~50x trailing GAAP earnings**,
- Buying after an **80% run**,
- Chasing a stock **above its upper Bollinger Band**,
- With **in-line guidance**, not raised guidance,
- A **decelerating growth rate**,
- A **heavy SBC overhang**,
- And a **one-sided sentiment tape** that historically marks short-term peaks.

The bull says “the bears are looking at the rearview mirror.” I’m looking at the *risk/reward*: at this price, the downside to the 50-day SMA at **$22.06** is 15%, and the downside to the 200-day SMA at **$17.59** is 32%. The upside to the Barron’s call is 35% — if everything goes perfectly.

**My recommendation: do not buy RELY at this price.** If you’re already long, take profits or tighten risk hard. If you’re not long, wait for the pushback — a real one, not a 5% dip — because when the RSI exits the 70s, the 10 EMA gives way, and the volume fades, this stock is going to remind everyone that **momentum is not a strategy.**

RELY is a great company. It’s just not a great buy right now.
Bear Analyst: **Bear Analyst: “Great Company, but You’re Paying a Momentum Price for a Decelerating Story.”**

Bull, I’ll give you this: you know how to tell a good story. You led with the $900B TAM, the 10 million customers, the record EBITDA, the “under 19x trailing earnings” — it all sounds very polished.

But I’m going to do what a good bear does: I’m going to check the math, question the quality of the earnings, and ask what the market is actually paying for today. Because once you strip away the enthusiasm, RELY’s risk/reward at **$25.93** is not in the bull’s favor.

---

## 1. That “Under 19x Trailing P/E” Is Built on a One-Time Mirage

You made a big deal out of the updated EPS math. Let’s actually do it.

- Market cap: **~$5.46B**
- Shares out: **~210.3M**
- Q2 GAAP EPS: you say **$0.93–$0.98**

That implies Q2 net income of roughly **$195–$206M**. Now compare that to the company’s own adjusted EBITDA print for Q2: **$115M**.

Think about that for a second. GAAP net income cannot be **$80M higher than adjusted EBITDA** unless there is a large non-operating item in the quarter — almost certainly a tax-related benefit, likely tied to the company’s NOL position and the release of a valuation allowance. The fundamental report already flags the effective tax rate at only **~5.8%** because of NOL carryforwards.

So you’re taking a one-time non-cash tax benefit and using it to declare that RELY trades at **under 19x trailing earnings**. That is not honest valuation math. Strip out the one-time item and the core trailing P/E is still meaningfully elevated — in the high-30s to 40s.

And if you want to use forward P/E instead, you’re relying on sell-side estimates that imply EPS roughly triples from today’s core run-rate. The company itself guided revenue **in line** for Q3, not above. When a company has a “blowout” quarter and doesn’t raise the bar, you should ask why.

---

## 2. The Growth Story Is Decelerating — That’s Not “Scaling,” That’s Maturing

You say “44% to 34% to 29% to 20% is scaling, not collapse.” Fine. But what is the multiple paying for?

Let’s look at the actual revenue trajectory:

| Period | Revenue Growth |
|---|---|
| FY2023 | +44.5% |
| FY2024 | +33.9% |
| FY2025 | +29.4% |
| Q1 2026 | +25.2% |
| Q2 2026 | ~+20% |

That is a **clean and persistent deceleration**. The bull wants you to pay a hyper-growth valuation for a company whose growth rate is now converging toward the low-20s. And what does Q3 guidance tell us? **~$506M, roughly in line with consensus.** Not a blowout raise. Not acceleration. Just “we’ll keep growing about 20%.”

The $900B TAM sounds massive, but RELY’s penetration story is also the story of a fragmented, brutally competitive market. Remittances are a price-transparent commodity. Customers have almost zero switching costs. Remitly is winning share because it is spending enormously to win it.

How much? **Sales & Marketing is the largest operating expense at 19.1% of revenue.** That’s not a moat. That’s buying customers.

---

## 3. The “Moat” Is Not as Wide as You Think

Bull, you called the competitive advantages “widening.” Let’s test that.

- **Wise** is the low-cost digital leader with a strong brand in cross-border payments.
- **PayPal/Xoom** has distribution and brand trust.
- **Western Union and MoneyGram** have decades of regulatory licenses and corridor relationships.
- **Banks and neobanks** are embedding remittances directly into their apps.

Yes, Remitly has 10 million active customers. But in a $900B market, 10 million customers and ~$1.7B TTM revenue means this is still a small player in a crowded field. Regulatory licenses are table stakes — the big competitors already have them.

And what happens when competition heats up? Remitly has to invest more in S&M, or cut take rates, or both. That is not a “widening moat.” That is a **fight for share in a commodity business**.

---

## 4. SBC and Buybacks: The Math Still Doesn’t Add Up

You tried to wave away dilution risk by pointing to the buyback program. Let’s check the numbers:

- FY2025 stock-based compensation: **$155.1M**
- FY2025 buybacks: **$23.9M**
- Q1 2026 buybacks: **$42.5M**
- Combined buybacks 2025 + Q1 2026: **$66.4M**

That is still **less than half** of FY2025 SBC. The shareholder is still being diluted on a cumulative basis. One quarter where buybacks exceeded SBC doesn’t undo years of stock compensation.

And remember, the “record 23% adjusted EBITDA margin” adds back SBC. That’s a non-GAAP metric that conveniently ignores a real cost to shareholders. If you back out SBC, the picture is far less impressive.

Management is not returning capital. Management is partially offsetting dilution while issuing stock as compensation. That is not a shareholder-friendly story; it’s a standard growth company story.

---

## 5. The Technical Setup Is a Warning, Not a Breakout Confirmation

You pointed to the August 6 candle as “confirmation.” Let’s look at the same candle with honest eyes:

- Open: **$25.98**
- High: **$27.15**
- Low: **$24.11**
- Close: **$25.93**

RELY tagged **$27.15**, then gave back **more than $1.20 from the high** and closed below the open. That’s a **rejection wick**, not a clean breakout.

Now add the rest of the tape:

- RSI: **66.3**, heading into the exact zone where RELY stalled twice in July. Both prior 70+ RSI readings were followed by multi-percent pullbacks.
- ATR: **$1.09**, the highest in the lookback. This is not a calm, low-risk setup.
- Close: **1.5% above the upper Bollinger Band**. Mean reversion is the base case, not the exception.
- Price vs. 50 SMA: **~17.5% above** the 50-day. Price vs. 200 SMA: **~47% above** the 200-day.

You say “don’t chase; buy the pullback at $24.10–$24.80.” But look at your own trade plan:

- Entry at $24.10, stop under $23.75 = **$0.35 of risk**. That’s less than one-third of the current ATR. A normal overnight move will stop you out.
- Entry above $27.15, stop under $23.75 = **~12.5% risk** to make the Barron’s target.

That’s not a 4:1 reward-to-risk setup. That’s a plan to get whipsawed in either direction.

---

## 6. Sentiment Is One-Sided — That’s a Red Flag, Not Fuel

You say StockTwits being 10-0 bullish is “a quiet, positive tape.” I see it differently.

That is a **tiny sample** where nobody disagrees. Reddit has no substantive RELY engagement. The news flow is uniformly bullish: Barron’s, Zacks, StockStory, Cantor. The bull narrative is fully transmitted to the market.

And even in that positive tape, there are cracks:

> “Valuation still looks wrong… it needs to show me, not tell me.”
> “SBC outweighing buybacks.”

When the story is this one-sided, the question is: **who’s left to buy?** The stock just ran 80% YTD. The catalyst just happened. The guidance is in line. There is no fresh catalyst to push the stock higher from here.

---

## 7. Macro Is Not Your Tailwind — It’s an Overhang

You call the macro environment “supportive.” Let’s reconsider:

- **10-year Treasury at 4.63%, with a recent peak of 4.75%.** Higher discount rates hurt high-multiple growth stocks.
- **No Fed cuts expected in 2026: 88% probability.** There is no near-term policy catalyst.
- **Hormuz risk:** only **12% probability** of normal traffic by Aug 31, and **40% probability** Iran charges fees by Oct 31.

An oil shock pushes inflation higher, keeps the Fed hawkish, sends yields up, and compresses multiples across the software complex — including RELY.

And don’t tell me the low beta protects you. RELY sold off on July 30 on Hormuz headlines. Beta is backward-looking. It won’t save you from a sector de-rating.

---

## The Bottom Line

Bull, I’m not here to tell you Remitly is a bad company. It’s a real business with real momentum, a net-cash balance sheet, and improving profitability. But “good company” and “good buy at this price” are two completely different questions.

At **$25.93**, you are:

- Paying for a one-time, tax-flattered EPS to justify a low P/E,
- Buying after an **80% YTD run**,
- Chasing a stock **above the upper Bollinger Band**,
- With **in-line guidance**, not raised guidance,
- A **decelerating growth rate**,
- Heavy **SBC dilution** that buybacks only partially offset,
- And a **one-sided sentiment tape** that historically marks short-term peaks.

The downside to the 50-day SMA at **$22.06** is about **15%**. The downside to the 200-day SMA at **$17.59** is about **32%**. The upside to Barron’s call is 35% — if everything goes perfectly.

I’d rather miss the next 5% than own a stock that is this extended, with this little new information to drive it higher. If you’re already long, take profits or tighten risk. If you’re not long, wait for a real reset — not a 5% dip, but a consolidation that builds a new base.

RELY might be a great company. At **$25.93**, it’s not a great risk/reward.

**Recommendation: Avoid / Do Not Buy at current levels.**
Bear Analyst: Bull, you’ve now delivered essentially the same speech three times. The melodies change, but the chorus stays the same: *“profitable, net-cash, 20%-growing, forward P/E 15.7x, buy the pullback.”*

I’m going to keep this simple: the facts haven’t changed just because you repeated them.

---

## 1. That “Sub-19x Trailing P/E” Is a Tax Artifact, Not an Earnings Breakthrough

You keep leaning on Q2 GAAP EPS of **$0.93–$0.98**. Let’s translate that into actual dollars:

- ~210M shares × $0.95 midpoint ≈ **$200M of Q2 net income**
- Q2 adjusted EBITDA was **$115M**

A company cannot generate GAAP net income that is *nearly double* its adjusted EBITDA without a massive non-operating item. The fundamental report already flags the tell: an effective tax rate of only **~5.8%**, driven by NOL carryforwards, and likely a valuation-allowance release.

That means your “under 19x trailing P/E” is, in large part, a **one-time tax benefit**. Strip it out — as any honest valuation should — and the core trailing multiple is still in the **high-30s to 40s**. That’s not a value multiple. That’s a momentum multiple.

---

## 2. Annualizing the Best Quarter Is Not a Valuation Strategy

You say: “Annualize Q2’s $115M EBITDA and RELY trades at 10–11x EV/EBITDA.”

Sure. And if I annualize my best month of the year as my “run-rate,” I can justify almost any price.

The problem is that management **did not guide to that run-rate**. They guided Q3 revenue to **~$506M, in line with consensus**. Not above. If the business were truly on a $460M annualized EBITDA trajectory, they would have raised guidance. They didn’t.

The fundamentals report itself shows **EV/TTM EBITDA in the high-20s to mid-30s**, depending on the adjustment. That’s not cheap. And if you treat stock-based compensation as the real expense it is — because it is — the multiple gets even worse.

---

## 3. Growth Is Decelerating, Not “Scaling Into Strength”

Let’s put the revenue trajectory in one table again, because the bull keeps hoping it will disappear:

| Period | Revenue Growth |
|---|---|
| FY2023 | +44.5% |
| FY2024 | +33.9% |
| FY2025 | +29.4% |
| Q1 2026 | +25.2% |
| Q2 2026 | ~+20% |

That is a **clean, persistent deceleration**. The “$900B TAM” story is real, but so is the growth slowdown. And what is the market being asked to pay for that deceleration? A forward P/E of **15.7x** that only works if EPS roughly **triples** from the current core run-rate.

That’s not “under-appreciated.” That’s priced for perfection.

---

## 4. SBC and Buybacks: The Math Still Doesn’t Work

You cite Q1 2026 buybacks of **$42.5M** vs. SBC of **$27.5M** as proof the dilution problem is solved.

Let’s zoom out:

- FY2025 SBC: **$155.1M**
- FY2025 buybacks: **$23.9M**
- Q1 2026 buybacks: **$42.5M**
- Combined buybacks: **$66.4M**

That’s still **less than half** of FY2025 SBC alone. One quarter of buybacks exceeding SBC does not reverse years of stock-compensation dilution. And remember: the “record 23% adjusted EBITDA margin” **adds back stock-based compensation**. It’s a non-GAAP measure that conveniently ignores a real cost to shareholders.

The buyback isn’t “capital return.” It’s a partial offset to ongoing dilution.

---

## 5. The August 6 Candle Is a Rejection, Not a Breakout

You keep calling the tape “confirmed.” Here’s what actually happened:

- Open: **$25.98**
- High: **$27.15**
- Low: **$24.11**
- Close: **$25.93**

RELY tagged **$27.15**, gave back **more than $1.20**, and closed **below its open**. That’s a textbook rejection wick.

Add the rest of the technical picture:

- RSI at **66.3** — approaching the **70 level** that has marked two pullbacks in July.
- ATR at **$1.09** — the highest in the lookback.
- Close **1.5% above the upper Bollinger Band**.
- Price **~47% above the 200-day SMA**.

And your trade plan? Either:

- Buy the pullback at **$24.10–$24.80** with a stop at **$23.75** — that’s only **$0.35 of risk**, less than one-third of ATR. Normal noise stops you out.
- Or buy a breakout above **$27.15** with a stop at **$23.75** — that’s **~12.5% risk** for a target based on a Barron’s article.

That’s not a 4:1 reward-to-risk setup. That’s a plan to get whipsawed.

---

## 6. The “Moat” Is a Customer-Acquisition Machine

You say Remitly has a widening moat.

What the data shows:

- Sales & Marketing is the **largest operating expense at 19.1% of revenue**.
- The company has **10 million customers in a $900B market** — that’s roughly **0.2% share**.
- Competitors include **Wise, PayPal/Xoom, Western Union, MoneyGram**, and banks embedding remittances into their apps.

Remittance is a **price-transparent commodity** with low switching costs. Customers go where the fee is lowest. That’s why RELY has to spend nearly one-fifth of revenue on marketing to keep growing.

That’s not a moat. That’s a treadmill.

---

## 7. Sentiment Being One-Sided Is Not a “Quiet Positive Tape”

You say StockTwits at 10-0 bullish is “constructive, not euphoric.”

I see it differently:

- It’s a **tiny sample** with zero bearish counterweight.
- **Reddit is silent** — no independent retail validation.
- The news cycle is uniformly bullish: Barron’s, Zacks, StockStory, Cantor.

When everyone already knows the story, the question is: **who is left to buy?** The stock is up 80% YTD, just printed a 52-week high, and the catalyst has already happened. Q3 guidance is in line. There is no fresh fuel.

---

## 8. Macro Is Not Your Tailwind

- 10-year Treasury at **4.63%**, recently **4.75%**.
- Market-implied probability of **no Fed cuts in 2026: 88%**.
- Strait of Hormuz normalization by Aug 31: only **12%**.
- Iran charging Hormuz fees by Oct 31: **40%**.

An oil shock pushes inflation up, keeps the Fed hawkish, drives yields up, and compresses multiples across the software complex. RELY already proved its vulnerability on **July 30**, when it sold off on Iran/Hormuz headlines.

Beta of 0.34 won’t save you in a sector-wide de-rating. It just means you fall slower.

---

## Final Word

Bull, Remitly is a **real company** with **real momentum** and **real profitability**. I’m not disputing that.

But at **$25.93**, the market is asking you to pay for:

- A one-time tax-flattered EPS,
- A decelerating growth curve,
- In-line guidance rather than a raise,
- Heavy SBC that buybacks only partially offset,
- A technical rejection wick at the high,
- One-sided sentiment,
- And a macro backdrop that offers no near-term catalyst.

The downside to the **50-day SMA at $22.06** is **~15%**. The downside to the **200-day SMA at $17.59** is **~32%**. The upside to the bull’s own Barron’s target is 35% — if everything goes perfectly.

RELY might be a great company. At this price, it’s not a great risk/reward.

**Recommendation: Avoid / Do Not Buy at current levels. If you’re long, take profits or tighten risk. If you’re not long, wait for a real reset — not a 5% dip.**

Momentum is not a strategy. And right now, RELY is priced as if the next five years of perfect execution have already happened.
Bear Analyst: # Bear Analyst — Final Rebuttal: “You’re Not Buying a Great Company at a Fair Price. You’re Buying a Great Company at the Peak of a Narrative.”

Bull, I’ll give you credit for one thing: you finally stopped calling a one-time tax-flattered GAAP quarter “under 19x trailing earnings” and started using cash flow. That’s progress. But the fact that you had to rotate through three different valuation frameworks in the same debate is exactly the problem. You’re not valuing RELY. You’re collecting whatever metric makes the purchase feel justified at $25.93 after an 80% run.

Let me finish this debate the right way: with the actual data, the actual risk/reward, and the actual question every investor should ask before buying into a post-earnings spike.

---

## 1. The Valuation Keeps Moving Because the Story Keeps Needing Help

You opened with **“under 19x trailing earnings.”** I showed you that Q2 GAAP EPS of $0.93–$0.98 implies roughly **$200M of quarterly net income — nearly double the company’s own $115M adjusted EBITDA print.** That is not a durable earnings number. That is an NOL/tax-valuation-allowance event, and you already know it, because you immediately abandoned that valuation when I pressed on it.

Then you switched to **“17x FY2025 FCF.”**

But FY2025 FCF was $283M. Q1 2026 FCF was $72.7M, annualizing to roughly $290M. **That means cash generation is flat, not growing.** You’re paying 17x for a cash flow machine that isn’t compounding yet — while the revenue growth rate slides from 44% to 20% over three years. That is not “inflection.” That is operating leverage showing up *before* the business has proven it can accelerate or even hold its growth rate. It’s also before factoring in that the **SBC burden is still extremely heavy** relative to cash returned.

Then you switched to **“15.7x forward earnings.”**

That number depends on sell-side estimates that assume EPS roughly triples from core run-rate. The company just guided Q3 **in line**, not above. Nobody gets to claim a cheap forward multiple when the forward numbers depend on a hockey stick the company itself did not endorse.

Three valuations. Three different stories. The one common element? All of them require perfect execution from a stock already trading near its all-time high.

---

## 2. The August 6 Candle Is Not a Breakout — It’s a Warning, and You Know It

Bull, you emphasized the close. Let’s look at the whole day, because that’s what a real technical analyst does.

| Time | Price |
|---|---|
| Open | $25.98 |
| High | $27.15 |
| Low | $24.11 |
| Close | $25.93 |

The stock tagged $27.15, then sold off more than **$1.20**, closing **below its open** after nearly a 13% intraday range. The highest-volume day in the entire lookback produced a close that was **barely above the prior close** relative to the session’s rage. Yes, the close printed above the prior July high. But that’s a **rejection wick**, not a clean continuation.

Now look at what else was flashing at that exact close:

- **RSI 66.3**, probing the exact 70 zone that produced two multi-percent pullbacks in July.
- **ATR $1.09**, the highest in the entire lookback — a stock that had been a quiet, low-volatility compounder is now a volatile momentum name.
- **Price 1.5% above the upper Bollinger Band** — mean reversion is the statistical base case.
- **Price 47% above the 200-day SMA** — that is not “defined risk.” That is extension.

And your trade plan reflects the tension you can’t escape:

- **Buy the pullback at $24.10–$24.80 with a stop at $23.75.** That’s $0.35–$1.05 of risk in a market with a $1.09 ATR. Normal overnight noise stops you out before you even get a chance to be right.
- **Buy the breakout above $27.15 with the same stop.** That’s **12.5% risk** to reach a target that came from a Barron’s article and a Cantor target published when the stock was lower.

You’re offering a plan that works only if the market behaves politely. The indicator data — ATR, RSI, Bollinger position — all say the market is not polite right now.

---

## 3. This Is Not “Scaling.” This Is Deceleration, and the Multiple Isn’t Built for It

Look at the actual revenue trajectory you’ve been dancing around for three rounds:

- **FY2023: +44.5%**
- **FY2024: +33.9%**
- **FY2025: +29.4%**
- **Q1 2026: +25.2%**
- **Q2 2026: +20%**

Every single period, the number gets smaller. You call it “law of large numbers.” I call it a company whose market penetration story is real but whose **growth rate is now converging toward the low-20s while the stock trades at a momentum multiple.**

Now, what did the company guide for Q3?

**~$506M, roughly in line with consensus.**

Not above. Not a raise. The company just printed a “blowout” quarter, and management’s very next message to the market was: **the trajectory stays the same.** That’s not the behavior of a company about to accelerate. That’s the behavior of a company that already front-loaded the good news.

In the last quarter, the market paid up for a beat. The next three months offer **no equivalent catalyst**. The stock is now a hostage to macro headlines, Hormuz oil risk, and the 10-year yield — none of which are in RELY’s control.

---

## 4. The “Moat” Is Actually a Customer-Acquisition Machine

Let’s put the S&M and customer numbers side by side, because the bull’s “widening moat” is the weakest point in his entire case:

- **10 million active customers** — up 10x since 2019, but still roughly **0.2% of the $900B remittance market**.
- **Sales & Marketing is the largest expense at 19.1% of revenue.**
- **Gross margin is 62%** — yes. And the company has to spend nearly a third of that gross margin on S&M to keep growing.

This isn’t a pharmaceutical company with patent protection. This is a **digital money-transfer business in the most price-transparent, commodity-like segment in finance.** Customers choose whichever corridor and fee structure is cheapest at that moment. There is no switching cost. There is no network effect that locks a sender into one app. There is nothing preventing Wise, PayPal/Xoom, Western Union, MoneyGram, or a bank from undercutting the exact corridor RELY is extracting margin from.

Regulatory licenses? Table stakes. The largest competitors already have them. Corridor density? It takes years to build, yes — but every major player on that list has already built it.

The moat is real, but it is **not widening**. It’s being defended every single quarter by spending nearly one out of every five dollars of revenue. If the customer-acquisition engine were truly efficient, S&M would be shrinking as a percentage of revenue. It isn’t — it’s the largest operating line.

---

## 5. SBC and Buybacks: The Math Does Not Add Up, No Matter How You Frame It

Bull, you pointed to Q1 2026:

- SBC: **$27.5M**
- Buybacks: **$42.5M**

And claimed the dilution problem is solved.

Let me zoom out and show you what “solved” actually looks like:

- FY2025 SBC: **$155.1M**
- FY2025 buybacks: **$23.9M**
- Q1 2026 buybacks: **$42.5M**

Total buybacks over the last five reported quarters: **$66.4M**.

That is **less than half of FY2025 SBC alone.** You are still net-diluted. The share count is not shrinking. It’s flat at ~210M — and that’s *with* a very recent buyback program. The EBITDA margin that the bull quotes as “record 23%” conveniently **adds back SBC**, which is a real cost that is paid, primarily, in stock. It doesn’t show up in cash tax expense? Right. But it **absolutely** shows up in shareholder dilution.

The buyback is not a capital-return program. It is a **partial offset to an ongoing, large, and only gradually moderating equity-compensation program.** That’s a different story — and a less bullish one.

---

## 6. Sentiment Is Not “Quiet and Positive.” It’s One-Sided, Tiny, and Late.

You now argue that Reddit silence means “the crowd hasn’t discovered the stock yet.”

Bull, the crowd doesn’t need to be on Reddit for a stock to be overextended. The crowd is already on StockTwits, and the StockTwits tape is **10 bullish messages, 0 bearish, among labeled samples.** Zacks, Barron’s, StockStory, MarketBeat, Cantor, Motley Fool — the news cycle has been uniformly bullish for a full window. Institutions have coverage. The story has been told.

The stock is up **80% YTD** and just printed a 52-week high. The events that created the positive tape — the earnings beat, the customer milestone, the Barron’s call — have already happened. **There is no fresh information left to push this higher in the short term.**

And what did the actual engaged users say, even in that bullish tape?

> *“Valuation still looks wrong… it needs to show me, not tell me.”*
> *“SBC outweighing buybacks.”*

When the most active observers of the stock are already debating whether the story is over-heated, that is not a “quiet, constructive setup.” That is how the rollover starts — quietly, before the headlines turn.

---

## 7. Macro Is Not Your Tailwind. It’s Your Overhang.

The bull wants to paint the macro backdrop as “supportive” because unemployment is 4.2% and CPI is decelerating.

Then why is this stock falling on Hormuz headlines?

Because the market is not pricing RELY on the macro *base case*. The market is pricing RELY as a high-multiple growth software name that is **sensitive to the discount rate and to risk appetite**. That’s what happened on July 30, when the stock sold off on Iran ceasefire headlines. That’s what the 10-year yield at 4.63% means. And what does the future hold?

- **88% probability of no Fed cuts in 2026** — zero policy support.
- **12% probability of Hormuz traffic normalization by Aug 31** — oil risk unresolved.
- **40% probability of Iran charging Hormuz fees by Oct 31** — that is not a tail risk. That is a coin flop on a geopolitical event that would raise oil prices, raise inflation, raise yields, and compress the multiple on every unprofitable and high-multiple growth stock — including this one.

A beta of 0.34 doesn’t save you in a sector de-rating. It just means RELY falls more slowly than the index — while still getting repriced downward. The bull is asking you to ignore a live macro risk because the base case is okay. The base case is already priced.

---

## 8. The Earnings Beat Is the Top, Not the Launchpad

Let me ask you the question the bull has avoided all debate:

**What is the next catalyst that takes this stock meaningfully higher?**

- Q2 earnings? Already reported. Already celebrated. Already in the price.
- Q3 guidance? Already guided. Already in line.
- A guidance raise before Q3? Management just gave its latest guidance. It was in line.
- A new product, acquisition, or market expansion? Nothing announced.
- A Fed cut? 88% probability it doesn’t happen in 2026.
- A Hormuz ceasefire? The market is already pricing an 88% probability of effective U.S.–Iran ceasefire by Aug 31. That’s in the tape, too.

The stock at $25.93 has already received the news. The 80% YTD rally is the market doing exactly what the bull described: pricing in the profitability inflection. That means the next leg up requires **new information**, not a replay of the last quarter’s print.

When you buy after an earnings blowout, after in-line guidance, after an 80% run, and after a rejection wick at the high — you’re not early. You’re late, with a wide stop and a target that comes from financial media rather than the company’s own financial model.

---

## Final Word: The Asymmetry Is Not on the Bull’s Side

Let’s do the real risk/reward math at $25.93:

**Downside:**

- 50-day SMA at $22.06 — **-15%**
- 200-day SMA at $17.59 — **-32%**
- The gap from current price back to the upper Bollinger Band at $25.55 — **-1.5%** — is the only “support” above the 50-day.

**Upside:**

- Barron’s call: ~$35 — **+35%**, assuming perfect macro, no Hormuz escalation, continued margin expansion, and a guidance raise that hasn’t come yet.
- Analyst target: $28 (Cantor) — **+8%** from current price.

That is not a 4:1 asymmetric setup. That is a **coin flip with a bullish tilt** — and a coin flip is a terrible risk-adjusted use of capital after a stock has already tripled from its lows.

---

# Bear Verdict

**RELY is a real company. Remitly has real customers, a real balance sheet, and a real profitability inflection. None of that is in dispute.**

What is in dispute is whether buying RELY at $25.93, on 2026-08-06, after +80% YTD, at RSI 66, above the upper Bollinger Band, with in-line guidance, decelerating revenue, heavy SBC, one-sided sentiment, and a live geopolitical tail risk is a sensible investment.

**It is not.**

The bull case is fully transmitted. The stock has already absorbed the good news. The next catalyst is months away, and the technicals suggest what goes up this fast can correct just as quickly.

**Recommendation: DO NOT BUY at current levels.**

- If you already own RELY: **take partial profits, tighten your stop** — and recognize that momentum can reverse faster than fundamentals catch up.
- If you don’t own it: **wait for one of two things** — either a genuine consolidation that builds a new base over weeks, or a reset to the 50-day SMA near $22–$23, where the reward-to-risk rebalances in your favor.
- Above all: **do not confuse a great company with a great entry price.**

At $25.93, RELY is a stage-two momentum trade dressed up as long-term investing. The story is excellent. The price is premature.

That’s the bear case — and that’s why I’m **avoiding RELY here**.
Bear Analyst: # Bear Analyst Final Rebuttal: The Story Is Great. The Price Is the Problem.

Bull, you’ve done something impressive over this debate: you’ve managed to argue the exact same thesis three times, with three different valuation frameworks, while calling the same price action a “breakout” every time. But the underlying facts haven’t changed.

Let me be very clear about what I’m actually saying:

**RELY is a real company with real customers, real revenue, and a real profitability inflection.**  
I have never disputed that. What I am disputing is whether **RELY at $25.93, after an 80% YTD run, after a one-day post-earnings spike, after closing above the upper Bollinger Band, with in-line guidance and a live geopolitical tail risk** is a rational entry point.

It is not.

Let me walk through exactly why the bull case collapses under scrutiny.

---

## 1. The “Under 19x Trailing Earnings” Argument Was a Tax Artifact, and You Know It

Bull, you opened this debate by claiming RELY trades at “under 19x trailing earnings” using Q2 GAAP EPS of $0.93–$0.98.

Let’s do the math:

- ~210M shares × ~$0.95 = **~$200M of Q2 net income**
- Q2 adjusted EBITDA: **$115M**

A company cannot generate GAAP net income that is **nearly double its adjusted EBITDA** unless there is a massive non-operating item in the quarter. The fundamental research flags exactly the tell: an effective tax rate of only ~5.8%, driven by NOL carryforwards and likely a valuation-allowance release.

That is a one-time, non-cash tax benefit. It is not a durable earnings breakthrough.

Strip it out — as any honest valuation must — and the core trailing multiple is still in the **high-30s to 40s**. That is not a value multiple. That is a momentum multiple.

Then you switched to “17x FY2025 FCF.” But FY2025 FCF was $283M, and Q1 2026 FCF was $72.7M — annualizing to roughly $290M. **Cash generation is flat, not compounding.** You’re paying 17x for a cash-flow machine that isn’t growing yet.

Then you switched to “15.7x forward earnings.” That number depends on sell-side estimates that assume EPS roughly triples from the core run-rate. The company just guided Q3 **in line**, not above. Nobody gets to claim a cheap forward multiple when the forward numbers depend on a hockey stick the company itself did not endorse.

Three valuations. Three different stories. The one common element? All of them require perfect execution from a stock already trading near its all-time high.

---

## 2. The Growth Story Is Decelerating — That’s Not “Scaling,” That’s Maturing

Let’s look at the actual revenue trajectory:

| Period | Revenue Growth |
|---|---|
| FY2023 | +44.5% |
| FY2024 | +33.9% |
| FY2025 | +29.4% |
| Q1 2026 | +25.2% |
| Q2 2026 | ~+20% |

Every single period, the number gets smaller. You call it “the law of large numbers.” I call it **a company whose growth rate is converging toward the low-20s while the stock still carries a momentum multiple.**

And what did management guide for Q3?

**~$506M, roughly in line with consensus.**

Not above. Not a raise. The company just printed a “blowout” quarter, and management’s very next message to the market was: *the trajectory stays the same.*

That is not the behavior of a company about to accelerate. That is the behavior of a company that already front-loaded the good news. The market paid up for the Q2 beat. The next three months offer **no equivalent catalyst**.

---

## 3. The August 6 Candle Is a Warning, Not a Breakout

You keep pointing to the close. Let’s look at the whole session:

- Open: **$25.98**
- High: **$27.15**
- Low: **$24.11**
- Close: **$25.93**

RELY tagged $27.15, gave back **more than $1.20**, and closed **below its open** after a nearly 13% intraday range. That is a textbook **rejection wick**, not a clean continuation.

Now add everything else flashing at that close:

- **RSI 66.3** — probing the exact 70 zone that produced two multi-percent pullbacks in July.
- **ATR $1.09** — the highest in the entire lookback. The stock that was positioned as a low-volatility compounder has become a volatile momentum name.
- **Price closed 1.5% above the upper Bollinger Band** — mean reversion is the statistical base case.
- **Price is ~47% above the 200-day SMA** — that is not “defined risk.” That is extension.

And your trade plan reflects the tension you can’t escape:

- **Buy the pullback at $24.10–$24.80 with a stop at $23.75.** That’s $0.35–$1.05 of risk in a market with a $1.09 ATR. Normal overnight noise stops you out before you even get a chance to be right.
- **Buy the breakout above $27.15 with the same stop.** That’s **12.5% risk** to reach a target that came from a Barron’s article and a Cantor target published when the stock was lower.

You’re offering a plan that works only if the market behaves politely. The indicator data — ATR, RSI, Bollinger position — all say the market is **not polite right now**.

---

## 4. The “Moat” Is a Customer-Acquisition Machine, Not a Competitive Fortress

You call the moat “widening.” Let’s look at what the numbers actually show:

- **Sales & Marketing is the largest operating expense at 19.1% of revenue.**
- The company has **10 million active customers in a $900B market** — that’s roughly **0.2% share**.
- Competitors include **Wise, PayPal/Xoom, Western Union, MoneyGram**, and banks embedding remittances into their own apps.

Remittance is a **price-transparent commodity** with low switching costs. Customers go where the fee is lowest. That’s why RELY has to spend nearly one out of every five dollars of revenue on marketing to keep growing.

Regulatory licenses? Table stakes. The largest competitors already have them. Corridor density? It takes time, but every major player on that list has already built it.

The momentum in the customer count is real. But 10 million customers at 0.2% penetration of a $900B market tells you two things: the runway is large, **and the competition is intense.** A company with a widening moat would not need to spend 19% of revenue on S&M just to hold its growth rate.

That’s not a moat. That’s a treadmill.

---

## 5. SBC and Buybacks: The Math Still Doesn’t Add Up

You keep pointing to Q1 2026:

- SBC: **$27.5M**
- Buybacks: **$42.5M**

And claiming the dilution problem is solved.

Let me zoom out:

- FY2025 SBC: **$155.1M**
- FY2025 buybacks: **$23.9M**
- Q1 2026 buybacks: **$42.5M**

Total buybacks over the last five reported quarters: **$66.4M**. That is **less than half of FY2025 SBC alone.**

You are still net-diluted. The share count is not shrinking. It’s flat at ~210M.* And the “record 23% adjusted EBITDA margin” conveniently **adds back stock-based compensation** — a real cost that is paid, primarily, in stock.

The buyback is not a capital-return program. It is a **partial offset to an ongoing, large equity-compensation program.** That’s a different story — and a less bullish one.

---

## 6. Sentiment Is Not “Quiet and Positive.” It’s One-Sided, Tiny, and Late.

You now argue that Reddit silence means “the crowd hasn’t discovered the stock yet.”

Bull, the crowd doesn’t need to be on Reddit for a stock to be overextended. The crowd is already on StockTwits, and the labeled tape is **10 bullish, 0 bearish.** Zacks, Barron’s, StockStory, MarketBeat, Cantor, Motley Fool — the news cycle has been uniformly bullish for a full window. Institutions have coverage. The story has been told.

The stock is up **80% YTD** and just printed a 52-week high. The events that created the positive tape — the earnings beat, the customer milestone, the Barron’s call — have already happened. **There is no fresh information left to push this higher in the short term.**

And even in that bullish tape, the most engaged observers were saying:

> *“Valuation still looks wrong… it needs to show me, not tell me.”*  
> *“SBC outweighing buybacks.”*

When the people already watching the stock are debating whether the story is over-heated, that is not a “quiet, constructive setup.” That is how the rollover starts — quietly, before the headlines turn.

---

## 7. Macro Is Not Your Tailwind. It’s Your Overhang.

You keep describing the macro backdrop as supportive because unemployment is 4.2% and CPI is decelerating.

Then why did RELY sell off on July 30 on Hormuz headlines?

Because the market is not pricing RELY on the macro *base case*. The market is pricing RELY as a high-multiple growth software name that is **sensitive to the discount rate and to risk appetite.**

Let’s review what the future actually looks like:

- **88% probability of no Fed cuts in 2026** — zero policy support.
- **12% probability of Hormuz traffic normalization by Aug 31** — oil risk unresolved.
- **40% probability of Iran charging Hormuz fees by Oct 31** — that is not a tail risk. That is a coin flip on a geopolitical event that would raise oil prices, raise inflation, raise yields, and compress the multiple on high-growth stocks.

A beta of 0.34 doesn’t save you in a sector de-rating. It just means RELY falls more slowly than the index — while still getting repriced downward.

---

## 8. The Real Risk/Reward Is Not on the Bull’s Side

Let’s do the honest math at $25.93:

**Downside:**

- 50-day SMA at **$22.06** — **-15%**
- 200-day SMA at **$17.59** — **-32%**
- The only nearby “support” above the 50-day is the upper Bollinger Band at **$25.55** — **-1.5%**

**Upside:**

- Cantor target: **$28** — **+8%** from current price, and that target was published *before* the latest beat.
- Barron’s call: **~$35** — **+35%**, assuming perfect macro, no Hormuz escalation, continued margin expansion, and a guidance raise that hasn’t come yet.

That is not a 14:1 asymmetric setup. That is a **coin flip with a bullish tilt** — and a coin flip is a terrible risk-adjusted use of capital after a stock has already tripled from its lows.

---

## Final Verdict

Bull, I’m not saying RELY is a bad company. I’m saying you’re buying a great company at a momentum peak, after the good news has already been delivered, with a technical setup that is flashing over-extension, and a fundamental guidance that offers no near-term acceleration.

The bull case is fully transmitted. The stock has already absorbed the earnings beat. The next catalyst is months away. And the technicals suggest that what goes up this fast can correct just as quickly.

**My recommendation: DO NOT BUY RELY at current levels.**

- If you already own RELY: **take partial profits and tighten your stop.**
- If you don’t own it: **wait for a genuine consolidation or a reset to the 50-day SMA near $22–$23**, where the risk/reward rebalances in your favor.
- Above all: **do not confuse a great company with a great entry price.**

At $25.93, RELY is a momentum trade dressed up as long-term investing. The story is excellent. The price is premature.

That’s the bear case. And that’s why I’m **avoiding RELY here.**

### Manager
**Recommendation**: Overweight

**Rationale**: This was a genuinely close debate between two well-constructed cases. Here's how it broke down:

**Where the Bull won the argument:**

The profitability inflection is undeniable. RELY went from a -$117.8M net loss in FY2023 to generating $283M in free cash flow in FY2025, with record adjusted EBITDA of $115M (23% margin) in Q2 2026. The bull correctly demonstrated that across every honest valuation framework, RELY is not priced for perfection: ~17x FY2025 FCF, ~2.8x EV/Revenue, ~10-13x EV/EBITDA on run-rate, and a forward P/E of ~15.7x. These are reasonable multiples for a 20% revenue grower with expanding margins, a net-cash balance sheet of ~$610M, and a massive $900B TAM with only ~0.2% penetration.

The bear's strongest valuation critique — that the Q2 GAAP EPS was inflated by a one-time tax benefit — was effectively neutralized when the bull pivoted to cash flow and EBITDA frameworks that don't depend on that quarter's tax line. A company generating $283M in FCF with a net-cash balance sheet and improving unit economics doesn't need a tax artifact to justify a reasonable multiple.

The bull also won on the moat argument. The bear called RELY a "treadmill" because of 19.1% S&M spend, but margins are expanding — not contracting — which is the opposite of what a customer-acquisition treadmill looks like. Gross margins at 62%+ and rising, EBITDA margins at a record 23%, and 10x customer growth since 2019 against established competitors tells you this is a company winning share, not barely holding on.

**Where the Bear won the argument:**

The entry timing concern is legitimate. The stock is up ~80% YTD, just printed a 52-week high, closed above the upper Bollinger Band, and the August 6 candle had a notable rejection wick from $27.15 back to a close of $25.93. RSI at 66.3 is approaching the 70 zone that produced two multi-percent pullbacks in July, and ATR has expanded to $1.09 — meaning volatility has picked up. The bear is right that the Q2 catalyst is now fully absorbed and Q3 guidance was only in-line, not raised, leaving no immediate catalyst to drive the stock higher in the near term.

The bear also scored points on SBC: cumulative buybacks of $66.4M over five quarters are still less than half of FY2025's $155M SBC. While Q1 2026 showed buybacks exceeding SBC, the multi-year dilution story hasn't been fully resolved yet. The "record 23% adjusted EBITDA margin" does add back SBC, which is a legitimate cost.

The sentiment point also has some merit: a 10-0 bullish StockTwits tape and uniformly bullish news flow after an 80% run means the story has been transmitted. There's no "under-the-radar" discount here.

**Why the Bull's fundamental case ultimately carries more weight — but with timing discipline:**

The bear's core argument is essentially: "great company, bad price right now." But the price — when measured against forward fundamentals rather than trailing GAAP artifacts — isn't bad at all. A 20% grower with a 23% EBITDA margin, $283M FCF, and $610M net cash at ~15.7x forward earnings is not expensive. The bear couldn't produce a valuation framework that made RELY look genuinely overvalued once the one-time tax benefit was stripped out — the cash flow and EBITDA multiples are simply too reasonable.

However, the bear's timing concerns are real enough to warrant discipline. This is not a "buy at any price" situation. The bull's own trade plan acknowledges this: buy the pullback near $24.10-$24.80, or add on a confirmed close above $27.15, with invalidation below $23.75. That is a disciplined, risk-defined approach that respects both the fundamental opportunity and the near-term technical extension.

The recommendation is Overweight — not a full Buy — because the bullish conviction on fundamentals is high, but the entry price discipline matters. The appropriate action is to be positioned for exposure, add on pullbacks that reset the reward-to-risk, and avoid chasing the post-earnings spike. A Hold rating would understate the strength of the fundamental case; a Buy would understate the near-term timing risk.

**Strategic Actions**: 1. **Core position**: Maintain or initiate a starter position at current levels (~$25.93), but size it conservatively — no more than 50-60% of the intended full position size. The fundamental inflection is real and time in the market matters.

2. **Add on pullbacks**: Scale into the position aggressively if RELY pulls back into the $24.10–$24.80 zone, which converges with the rising 10 EMA (~$24.08) and the top of the prior breakout base. This is where reward-to-risk is most attractive (~14:1 to the Barron's $35 target).

3. **Breakout add**: Add the remaining position on a confirmed daily close above $27.15. A close above the Aug 6 high would confirm the breakout is genuine and clear the way toward $30+.

4. **Hard stop**: Invalidation trigger is a daily close below $23.75. This level converges with the 20-day SMA, the breakout shelf, and roughly 2x ATR below the pullback entry zone. A close below here would break the near-term uptrend structure and suggest the post-earnings spike was indeed a blow-off top. Honor this stop without hesitation — if triggered, step back and reassess.

5. **Position sizing**: Given ATR has expanded to $1.09 (roughly 4.2% of price), size the position so that a stop-out at $23.75 from a $24.50 average entry represents no more than 1-2% of portfolio NAV. The higher volatility demands smaller position size to maintain the same risk budget.

6. **Upside targets**: First target $28 (Cantor pre-beat target, ~8% from current). Second target ~$35 (Barron's call, ~35% from current). If Q3 earnings in ~90 days deliver another beat-and-raise cycle, consider raising targets to $35-40 based on 15-18x forward FY2027 estimates. Trail stops higher as the stock moves in your favor — use the 20-day SMA or the rising 10 EMA as a trailing stop guide once the position is in profit.

7. **Monitor**: Watch Q3 earnings for a potential guidance raise (management has a pattern of conservative guidance followed by beats), the Hormuz/Iran situation (currently 88% ceasefire probability by Aug 31, but monitor the 40% risk of Iran charging fees by Oct 31), and SBC/buyback trends in the next quarterly filing to confirm the dilution trajectory continues to improve.

## V. Portfolio Manager Decision

Overweight