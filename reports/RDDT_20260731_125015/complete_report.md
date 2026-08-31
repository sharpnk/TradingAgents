# TradingAgents Investment Report

**Ticker:** RDDT
**Date:** 2026-07-31\n**Depth:** Deep (5 rounds)

## I. Analyst Team Reports

### Market
All data gathered and verified. Here is my detailed analysis.

---

FINAL TRANSACTION PROPOSAL: **SELL**

**Instrument:** RDDT (Reddit, Inc. — Communication Services / Internet Content & Information, NYQ)
**Analysis date:** 2026-07-31

---

## 1. Market Context — A Verified Breakdown Session

The verified snapshot confirms a violent one-day breakdown on 2026-07-31:

| Field | Value |
|---|---:|
| Open | 147.70 (gap down ~17.0% from prior close 178.04) |
| High / Low | 151.36 / 135.22 |
| Close | 143.45 |
| Volume | 25,076,271 (~5–8× normal recent daily volume) |

The close of **143.45** is **−19.4%** from the 2026-07-30 close of 178.04, on the largest volume print in the dataset — a capitulation-style / news-driven distribution day. Price closed in the lower third of the day's range (close 143.45 vs. low 135.22), meaning sellers retained control into the close.

*Note on data consistency:* the raw `get_stock_data` row and the verified snapshot agree exactly on OHLC; volume differs trivially (25,071,426 vs. 25,076,271 — ~4.8k shares, immaterial). The verified snapshot is used as the source of truth throughout.

---

## 2. Indicator Selection (8, Complementary, Non-Redundant)

I selected indicators across four families so that each adds a distinct lens without duplication:

| Family | Indicator | Why chosen for this market |
|---|---|---|
| Trend | close_50_sma | Medium-term trend reference; price is now decisively below it; flags dynamic resistance overhead |
| Trend | close_200_sma | Long-term benchmark; its rollover defines the secular downtrend and the failed July reclaim |
| Trend | close_10_ema | Short-term responsiveness; quantifies how stretched price is from the near-term average (mean-reversion risk) |
| Momentum | macd | Confirms whether momentum has flipped bearish after the July peak |
| Momentum | rsi | Flags overbought/oversold extremes; critical after a one-day 17-point collapse |
| Volatility | boll_lb | Measures the extreme downside band break; defines risk/reward of chasing shorts |
| Volatility | atr | Sets stop distances and position size in a suddenly high-volatility tape |
| Volume | vwma | Confirms whether the move is backed by volume-weighted distribution |

I deliberately excluded `boll`/`boll_ub` (covered by `boll_lb` context), `macds`/`macdh` (covered by `macd`), and `close_200_sma`'s faster peers to avoid redundancy.

---

## 3. Detailed Trend & Indicator Analysis

### 3.1 Price structure — a failed rally and a lower high
- Dataset-wide peak close: **270.71** (2025-09-18); 2026 peak close: **258.93** (2026-01-13).
- After the Feb–Mar 2026 selloff (Feb 12 low 127.71/close 131.07; Mar 27 close 121.84; Mar 30 low 119.27), RDDT ground higher into a July rally that peaked at **203.27** close (2026-07-14, intraday high 207.54 on 07-06).
- That July high is a **lower high** vs. both the Jan 2026 and Sep 2025 peaks — a classic bear-market rally structure. The rally briefly poked above the 200 SMA in early July (close 200.86 vs. 200 SMA 184.20 on 07-06) and failed, rolling over into the 07-31 breakdown.

### 3.2 Moving averages — full bearish alignment
- Verified 2026-07-31: **10 EMA 172.56**, **50 SMA 175.29**, **200 SMA 180.09**. Price (143.45) is below all three.
- **50 SMA < 200 SMA** (175.29 < 180.09) — the 50/200 "death cross" regime has persisted since approximately mid-March 2026 and has not been reclaimed.
- The 200 SMA itself is **rolling over** (declining from ~193.64 in mid-May 2026 to 180.09), confirming long-term trend deterioration rather than a mere pullback.
- Price sits **−16.9% below the 10 EMA** (143.45 vs. 172.56) — an extreme short-term negative stretch. While that signals oversold extension, in a confirmed downtrend the first move is usually a bounce *into* resistance (10 EMA → 50/200 SMA zone) rather than a reversal.

### 3.3 MACD — fresh, deep bearish cross
- Verified: **MACD −3.48**, signal **+0.36**, histogram **−3.84**.
- As recently as 07-30, MACD was only −0.63; the line collapsed to −3.48 in one session. The histogram flipped sharply negative from a positive state a few days earlier — momentum has decisively turned down from the July highs. No bullish divergence is present yet; the cross is fresh and deep, favoring continued downside pressure.

### 3.4 RSI — at the doorstep of oversold, not yet confirmed reversal
- Verified: **RSI 31.32**, down from 48.31 on 07-30 — a ~17-point one-day collapse.
- Not yet below the 30 oversold threshold. In strong downtrends RSI can stay suppressed for extended periods. The reading warns against *chasing* shorts at the extreme, but it does not yet provide a bullish reversal trigger.

### 3.5 Bollinger Bands — extreme downside band break
- Verified: middle **184.62**, upper **214.82**, lower **154.43**.
- Close 143.45 is **~7% below the lower band** — a severe downside volatility expansion. The lower band fell from 163.76 (07-30) to 154.43 in one day as volatility exploded. This is statistically stretched and raises the probability of a short-term bounce/squeeze, but it is also exactly what persistent breakdowns look like in the early phase; a close back *above* 154.43 would be the first sign of stabilization.

### 3.6 ATR — volatility regime change
- Verified: **ATR 13.72**, up from ~11.5 the prior session and ~8–9 in May–June. At ~9.6% of price, ATR is signaling that normal stop distances and position sizes must roughly double to survive noise. Any new trade should size to tolerate ~1.5–2× ATR (~$20–27) of adverse excursion.

### 3.7 VWMA — volume-weighted confirmation of distribution
- **VWMA 169.05** (indicator feed, 2026-07-31; not in verified snapshot but consistent with the tape). Price closed ~15% below VWMA, confirming that the session's heavy volume was dominated by sellers (distribution), not vacuum-driven noise. Prior distribution warnings: 07-22 (−8.3% on 8.99M shares) and elevated 07-30 volume (11.63M) before the 25.08M capitulation day.

---

## 4. Synthesis & Actionable Insights

**Regime:** Confirmed downtrend (lower highs since Jan 2026; death-cross MA alignment; declining 200 SMA) with a fresh momentum breakdown. The 07-31 gap-down-and-close-near-lows on record volume is a trend-continuation signal, not a bottom signal.

**Key levels (from verified/raw data):**
- **Immediate downside reference:** the 2026-02-12 low 127.71 (close 131.07), then the Mar 2026 lows 119.27–125.
- **First resistance / stabilization trigger:** 154.43 (old Bollinger lower band) — a reclaim here would reduce short-term downside extension.
- **Next resistance:** 169–172 (VWMA / 10 EMA), then 175–180 (50 SMA / 200 SMA). Any rally into these zones is a lower-risk shorting/exit area unless volume confirms a reclaim.

**What would invalidate the bearish view:** a daily close back above the 200 SMA (~180) on strong volume — currently ~25% away — or a bullish MACD crossover after an RSI oversold washout (RSI < 30 followed by a higher low). None of these are present.

**Risk guidance:** With ATR at 13.72, use wide stops or reduced size; do not add longs on the basis of "cheapness." For shorts, the 7% below-band stretch argues for waiting for a bounce toward 154–160 rather than chasing the close.

---

## 5. Summary Table

| Indicator | Value (2026-07-31) | Signal | Actionable Insight |
|---|---|---|---|
| Close | 143.45 (−19.4% d/d) | Breakdown | Gap-down close near lows on record volume = distribution, not bottom |
| Volume | 25.08M | Capitulation print | ~5–8× normal; confirms institutional selling (07-22 and 07-30 also elevated) |
| close_10_ema | 172.56 | Bearish | Price −16.9% below; extreme short-term stretch; first resistance on any bounce |
| close_50_sma | 175.29 | Bearish | Price below; 50 < 200 (death-cross regime since ~mid-Mar) |
| close_200_sma | 180.09 | Bearish/rolling over | Long-term downtrend confirmed; July rally failed to hold above it |
| macd | −3.48 (signal +0.36, hist −3.84) | Fresh deep bearish cross | Momentum flipped down from July highs; no divergence to fade it |
| rsi | 31.32 | Approaching oversold | Doorstep of 30; warns against chasing shorts but no reversal trigger yet |
| boll_lb | 154.43 (middle 184.62, upper 214.82) | Extreme downside break | Close ~7% below band; first stabilization signal = reclaim of 154.43 |
| atr | 13.72 | Volatility spike | ~9.6% of price; double stop distances / halve position size |
| vwma | 169.05 | Distribution confirmed | Close ~15% below VWMA; sellers dominated at volume |

**Bottom line:** The technical picture is unambiguously bearish after 07-31 — trend, momentum, volatility, and volume all align to the downside. The only near-term caution is the oversold stretch, which argues for entering shorts on strength toward 154–160 rather than chasing, and for exiting/reducing longs rather than adding. Recommendation: **SELL** (reduce/exit long exposure; avoid new longs; consider shorts on bounces with ATR-sized stops).

### Sentiment
**Overall Sentiment:** **Mildly Bearish** (Score: 3.6/10)
**Confidence:** Medium

# Sentiment Report — RDDT (Reddit, Inc.; NYQ; Communication Services / Internet Content & Information)
**Period:** 2026-07-24 → 2026-07-31 | **Analysis date:** 2026-07-31

---

## 1. Source-by-source breakdown

### 1a. News headlines (Yahoo Finance / Barron's / Bloomberg / Investopedia / others) — BEARISH, high volume
The news flow is dominated by a single event: RDDT's **worst intraday drop on record** on Friday 2026-07-31 (headlines cite −20% to −23.2%) following Q2 2026 earnings. Critically, the earnings themselves were a **beat-and-raise**: revenue of $804.9M (+61.1% YoY, handily above consensus), EBITDA well above estimates, and strong forward guidance (StockStory, GuruFocus). Yet the selloff was driven by four overlapping fears:

1. **No new AI data-licensing deals announced** — Bloomberg explicitly frames the record plunge as disappointment over the "dearth of new AI deals," with investors wanting a visible shift in revenue streams.
2. **US daily active users metric disappointed** — slowing US DAU growth despite record revenue.
3. **"Choppy" search-referral warning** — CEO Steve Huffman warned of volatile search referrals and traffic (Investopedia, Proactive, Stocktwits), stoking fears that **Google's AI Mode / AI search changes** are cannibalizing Reddit's traffic.
4. **Google relationship friction** — Wells Fargo flagged GOOGL friction raising AI-licensing risk (Stocktwits).

Secondary institutional/analyst takes: Barron's ran a contrarian piece ("The Earnings Selloff Is a Buying Opportunity," "Reddit has become the voice of the internet") and a cautionary piece ("The Search Traffic Trap"); 24/7 Wall St. framed the Alphabet-vs-Reddit divergence as a fault line in the social-media investment thesis; Trefis warned RDDT is "the best house on the block" but costs "top-of-the-market" price. Legal news: a federal court cleared Reddit to advance anti-circumvention claims against **Perplexity AI and SerpApi** — a potentially positive catalyst buried under the selloff. Overall institutional framing: decisively bearish on the stock's near-term price action, while acknowledging fundamental strength.

### 1b. StockTwits — BULLISH (contrarian), moderate sample
30 messages: **Bullish 16 (53%), Bearish 1 (3%), Unlabeled 13**. Despite the record crash, retail sentiment on StockTwits is overwhelmingly bullish — a textbook contrarian divergence from the news flow. Themes: "squeeze into close" (TaoistTrader), "squeeze!!! Back to $200 next week" (Burn0505), "gap fill next week" (AndreKostolany), "probably closing around 150 today" (QuietTrader), "looking forward to the rebound" (retiredyoung), and bullish fundamentals commentary calling Reddit "one of the stickiest businesses of all" with a "gigantic monetization runway" (amberajax2point0). The few bearish/noise posts are mostly non-fundamental: "Woke app 🗑️" (stephenk81), "glad to see Reddit taking a hit. Worst social media app on the market" (Lirik), "Solded it" (madewa12), "sold this pop" (TheGmork). One substantive bearish note stands out (Indablack): Reddit "may win a legal battle (Perplexity) and still lose the strategic war" as AI companies pull answers into their own products, removing search traffic — the same structural thesis driving the selloff. Note the sample is one session's worth of messages concentrated after the crash, so the bullish tilt likely reflects active dip-buyers talking into the close rather than the broader holder base.

### 1c. Reddit community (r/wallstreetbets, r/stocks, r/investing) — BEARISH/frustrated, very sparse
Only r/wallstreetbets produced mentions (4 posts); **r/stocks and r/investing were silent** on RDDT in the past 7 days. The WSB posts show real pain: "RDDT GUH — Down 27k in a single day, doubled down and ready to be a BAGHOLDER"; "Fuck Reddit — They absolutely crush top and bottom line earnings expectations, stocks down -23%. FML." A pre-earnings post (7/27) was bullish ("What a great day to own Reddit calls... load up before earnings"), consistent with the crowd having been positioned long into the report and getting caught in the crash. This is a small sample, but the emotional register is capitulation/frustration — retail longs who were positioned for a beat-and-raise catalyst and were punished by a sell-the-news reaction.

---

## 2. Cross-source divergences and alignments

- **Divergence (primary):** Institutional/news framing is **bearish** (record crash, structural AI-search threat) while StockTwits retail is **bullish** (53% Bullish vs 3% Bearish, squeeze/dip-buying rhetoric). This is the classic "retail leans in while institutions sell" configuration — a caution flag for the dip-buying thesis, since the bear case here is structural (traffic cannibalization) rather than just valuation.
- **Divergence (secondary):** StockTwits bullishness vs. WSB frustration. The two retail communities are reacting differently: WSB holders are underwater and angry; StockTwits traders are buying the close/oversold bounce.
- **Alignment:** Every source acknowledges the Q2 beat was strong. The disagreement is entirely about interpretation — near-term buying opportunity vs. structural AI-search threat to the traffic model.
- **Alignment:** Both news and StockTwits (Indablack) converge on the AI-search/AI-licensing theme as the decisive narrative — even bullish retail is framing the trade as a "squeeze/rebound" rather than disputing the AI thesis.

---

## 3. Dominant narrative themes

1. **AI search threat to traffic** — Google AI Mode/AI Overviews and Perplexity-type products pulling answers out of Reddit's pages; the "search traffic trap" (Barron's). This is the single dominant theme across news and the only substantive bearish StockTwits post.
2. **"Choppy"/volatile search referrals** — Huffman's own words became the headline risk, signaling management uncertainty about the Google channel.
3. **AI data-licensing monetization** — investors want new licensing deals as a revenue-stream shift; the absence of new deals was a top-3 disappointment, and the Perplexity/SerpApi lawsuit is the live legal lever.
4. **US DAU deceleration** — quality-of-growth concern even amid 61% revenue growth.
5. **Beat-and-raise but stock craters** — a valuation/sentiment disconnect: strong fundamentals overwhelmed by multiple compression and AI-fear repricing.
6. **Contrarian dip-buying / squeeze** — the StockTwits counter-narrative ("back to $200," "gap fill," "stickiest business on earth").

---

## 4. Catalysts and risks

**Catalysts (could improve sentiment):**
- Legal progress in the Perplexity/SerpApi anti-circumvention suit (court already cleared claims to advance).
- Any new AI data-licensing deal announcement — the market is clearly pricing deals as the next re-rating catalyst.
- Stabilization/recovery of Google search referrals; any clarification of the Google relationship.
- Oversold technicals (record one-day drop) — a reflexive bounce is plausible, as StockTwits traders anticipate.
- Continued strong Q3 execution on ads and engagement (strong guidance already given).

**Risks (could worsen sentiment):**
- Continued cannibalization of US traffic by Google AI Mode → further DAU/referral deterioration.
- US DAU metric keeps disappointing in future prints.
- Prolonged absence of new AI licensing deals → revenue-mix concerns persist.
- Valuation risk: Trefis flags top-of-market pricing; multiple compression can continue even with strong fundamentals.
- Legal overhang: the Perplexity suit is a double-edged sword (protects content but signals hostile posture to AI partners).
- Weekend gap risk: 30-message retail sample and WSB bagholders suggest fragile positioning into Monday.

---

## 5. Key sentiment signal summary

| Direction | Source | Supporting evidence |
|---|---|---|
| Bearish | News — Yahoo/Barron's/Bloomberg | Record intraday drop (−20% to −23%); "no new AI deals"; "US daily users metric disappoints"; "choppy search referrals" warning |
| Bearish | News — Wells Fargo via Stocktwits | GOOGL friction raises AI-licensing risk; selloff beyond the earnings beat |
| Bearish | News — Trefis | "Best house on the block costs the most" — valuation stretched |
| Bullish | News — Barron's | "Earnings selloff is a buying opportunity"; Reddit as "voice of the internet" |
| Bullish | StockTwits | 16 Bullish (53%) vs 1 Bearish (3%) of 30; squeeze/gap-fill/rebound-to-$200 calls |
| Bullish | StockTwits | Fundamentals: "stickiest business," "monetization scaling like a mofo," "exceeded earnings expectations" |
| Bearish | StockTwits (isolated) | Indablack: win the Perplexity case, lose the strategic AI-search war |
| Bearish | Reddit r/wallstreetbets | "RDDT GUH — down 27k, ready to be a BAGHOLDER"; "crush expectations, stock down -23%. FML." |
| Bullish | Reddit r/wallstreetbets (pre-earnings, 7/27) | "What a great day to own Reddit calls... load up before earnings" |
| Silent | r/stocks, r/investing | No posts mentioning RDDT in the past 7 days |

---

## 6. Bottom line

The dominant signal this week is the **record crash on AI-search and AI-licensing fears**, and the institutional/news framing remains bearish — the concerns are structural, not just technical. That is partially offset by a genuine beat-and-raise quarter, a couple of contrarian institutional voices, and a sharply **bullish retail crowd on StockTwits (53% Bullish / 3% Bearish) buying the dip into the close**. The bullish retail tilt is itself a contrarian caution: dip-buying into a structural traffic narrative has historically been a poor entry, and the WSB cohort that loaded up pre-earnings is already underwater and capitulating. Net assessment: **Mildly Bearish** — sentiment is dominated by a bearish event and structural fears, with a bullish retail counter-current that is insufficient (and partly contra-indicative) to flip the aggregate read. This is a signal for the trader to weigh against fundamentals and technicals, not a price call.

*Data caveats: StockTwits sample is small (30 messages, single post-crash session); Reddit community data is sparse (only 4 WSB posts; r/stocks and r/investing silent), which caps confidence at medium. News sample is substantive (~20 headlines) and is the highest-quality input here.*

### News
I now have comprehensive data across company news, macro indicators, and prediction markets. Let me compile the full research report.

---

# RDDT (Reddit, Inc.) — News & Macro Research Report
**Analysis Date:** 2026-07-31 | **Exchange:** NYQ | **Sector:** Communication Services / Internet Content & Information

## 1. Company-Specific News: Record Crash After a Blowout Quarter

**The headline event (July 31):** RDDT suffered its **worst intraday drop on record (~-20% to -23%)** on Friday despite reporting Q2 2026 results that beat on nearly every metric. This is the dominant, market-moving story of the week.

**The fundamental beat (masked by the selloff):**
- **Revenue: $804.9M, +61.1% YoY** — handily beat consensus (StockStory).
- **EBITDA well above estimates**; company hit a **$1M revenue-per-employee milestone** (GuruFocus).
- Raised forward guidance ("beat-and-raise" quarter per 24/7 Wall St.) with record revenue and strategic pivots highlighted on the earnings call (Zacks).

**Why the stock cratered despite the beat:**
1. **No new AI data-licensing deals announced** — Bloomberg notes investors were hoping for a shift in revenue streams toward AI licensing; the absence disappointed.
2. **US daily active users (DAU) metric disappointed** — slowing US user growth (Yahoo Finance, Stocktwits/Wells Fargo).
3. **"Choppy" search referrals warning** — CEO Steve Huffman flagged volatile search referrals/traffic late in the June quarter, raising fears that **Google's AI search changes** could structurally alter Reddit's traffic acquisition (Investopedia, Proactive).
4. **GOOGL friction** — Wells Fargo flagged elevated AI-licensing risk tied to Reddit's relationship with Google (Stocktwits). Notably, Alphabet jumped ~6% the same day Reddit fell ~23%, crystallizing the divergence narrative.

**Legal/catalyst overlay:** A federal court cleared Reddit to advance anti-circumvention copyright claims against **Perplexity AI and SerpApi** — part of Reddit's crusade against AI data scraping (Stocktwits). This is a double-edged sword: it protects content value (supportive of future licensing revenue) but signals ongoing friction with AI companies that could otherwise be licensing partners.

**Contrarian/positive takes:**
- Barron's published a **bullish "buying opportunity" piece** ("Reddit Is Due for Big AI Bump"), arguing Reddit is "the voice of the internet" and central to AI's future.
- Motley Fool asks whether the stock is "finally too cheap to ignore," while Trefis warns it remains the "best house on the block" but "costs the most" (valuation premium).

## 2. Macro Context (FRED Data)

- **Inflation cooling:** CPI fell to **332.57 (June)** from 333.98 in May (-0.42% MoM); core PCE rose just +0.13% over the window. Disinflation is intact.
- **Rates:** Fed funds effective **3.63%** — steady, no cuts this year. **10Y Treasury spiked to 4.67%** (from 4.45% in early May, +4.9%), with the 10Y crossing 4.71% on July 23. The yield curve (10Y-2Y) sits at **+0.45** — modestly positive, no inversion.
- **Labor:** Unemployment **4.2%** (down from 4.3%), still healthy.
- **Volatility:** VIX **17.09** after spiking to 20.66 on July 29 (Fed-day turmoil) — elevated but not panic-level; markets "bounced back from Fed day turmoil" (Barron's).

**Key tension for RDDT:** Rising long-end yields (4.67% 10Y) pressure high-multiple growth stocks — RDDT is among the highest-multiple names in the sector (Trefis).

## 3. Prediction Markets

- **Fed cuts 2026: 89% probability of ZERO rate cuts in 2026** (up +4.4pp on the week) — the market has fully priced out the cutting cycle. No hike/cut repricing near-term; policy is a neutral-to-slightly-restrictive backdrop.
- **US recession by end of 2026: 12%** (+2pp on the week) — macro tail-risk is low; not a recessionary tape, but slightly deteriorating.
- **AI regulation:** US AI safety bill before 2027: 17% (fell -16.5pp) — low regulatory risk to AI licensing monetization.
- No direct RDDT/Google antitrust prediction markets exist; equity-specific event coverage is limited.

## 4. Synthesis & Actionable Insights

- **The stock is repricing a single structural risk:** Google AI-search disruption of referral traffic + absence of new AI licensing deals. This is a real fundamental risk (traffic is a top-of-funnel driver), not just a sentiment issue.
- **The selloff is extreme vs. the fundamentals:** A 61% revenue-growth, beat-and-raise quarter met with a record -20%+ single-day drop is an outsized reaction; history suggests such dislocations can offer entry points, but the search-referral overhang is unresolved and could persist into Q3 (next earnings).
- **Catalysts to watch:** (a) any new AI data-licensing announcements (Perplexity suit resolution or new partners), (b) Google search-traffic stabilization commentary, (c) US DAU re-acceleration, (d) 10Y Treasury direction (4.67% and rising = headwind for the multiple).
- **Valuation:** Even after the crash, Trefis notes RDDT still commands a top-of-market multiple; the bar for execution remains high.
- **Conflicting analyst framing:** Wells Fargo (bearish on GOOGL friction/licensing risk) vs. Barron's (bullish dip-buy thesis). The near-term tape is dominated by the bearish framing; the medium-term case hinges on AI licensing actually materializing.

**Bottom line:** RDDT is in a high-conviction, high-uncertainty moment — exceptional fundamentals colliding with a structural traffic/Google concentration risk and a hawkish rate backdrop. The week's news flow is decisively negative (record crash, DAU miss, no AI deals, search volatility warning), with only contrarian dip-buy arguments as support.

---

## Key Points Summary Table

| Category | Key Finding | Date/Source | Implication for RDDT |
| --- | --- | --- | --- |
| **Stock event** | Worst intraday drop on record, ~-20% to -23% | 2026-07-31 (Yahoo/Bloomberg/StockStory) | Severe negative momentum; high short-term downside risk |
| **Earnings** | Q2 rev $804.9M (+61.1% YoY), EBITDA beat, raised guidance | 2026-07-31 (StockStory, GuruFocus) | Fundamentals strong; supports medium-term value case |
| **AI licensing** | No new AI data-licensing deals announced | 2026-07-31 (Bloomberg) | Key growth narrative stalled; negative for AI-revenue premium |
| **User metrics** | US DAU metric disappointed; slowing US growth | 2026-07-31 (Yahoo, Wells Fargo via Stocktwits) | Core engagement growth decelerating |
| **Traffic risk** | "Choppy" search referrals; Google AI-search volatility warning | 2026-07-31 (Investopedia, Proactive) | Structural concentration risk on Google traffic |
| **Legal** | Court allows anti-circumvention suit vs Perplexity/SerpApi | 2026-07-31 (Stocktwits) | Protects content value; may complicate future AI partnerships |
| **Sector divergence** | GOOGL +6% same day RDDT -23%; AMZN earnings lift AI trade | 2026-07-31 (24/7 Wall St., MT Newswires) | Market rotating toward AI beneficiaries, away from traffic-dependent platforms |
| **Analyst split** | Wells Fargo bearish (GOOGL friction) vs Barron's bullish (dip-buy) | 2026-07-31 | Elevated uncertainty; wide outcome distribution |
| **Rates** | Fed funds 3.63% (steady); 10Y at 4.67%, +22bp over 90d | FRED, 2026-07-29 | Higher discount rate pressures high-multiple growth stock |
| **Fed policy** | 89% probability of NO Fed cuts in 2026 (+4.4pp wk) | Polymarket, 2026-07-31 | No near-term rate relief catalyst |
| **Recession** | US recession by end-2026: 12% (+2pp wk) | Polymarket, 2026-07-31 | Macro backdrop OK; ad spending risk low but not zero |
| **Inflation** | CPI down -0.42% MoM; core PCE +0.13% | FRED, June 2026 | Disinflation intact; supports current rate stance |
| **Volatility** | VIX 17.09 after 20.66 spike on Jul 29 | FRED, 2026-07-30 | Market jittery; RDDT-specific vol likely elevated |
| **AI regulation** | US AI safety bill before 2027: 17% (down 16.5pp) | Polymarket, 2026-07-31 | Low regulatory obstacle to AI licensing monetization |

**Follow-up needs:** A price/technical analysis of RDDT's post-crash chart and a valuation model would sharpen the BUY/HOLD/SELL recommendation; the macro and news picture alone supports a **defensive near-term stance with a watchful eye on AI-licensing catalysts**.

### Fundamentals
All data has been retrieved successfully. I now have comprehensive fundamentals, quarterly and annual income statements, balance sheets, and cash flow statements for RDDT. Let me compile the full analysis.

---

# Comprehensive Fundamental Analysis Report: RDDT (Reddit, Inc.)
**Analysis Date:** 2026-07-31 | **Sector:** Communication Services | **Industry:** Internet Content & Information | **Exchange:** NYQ

---

## 1. Executive Summary

Reddit, Inc. has completed a remarkable fundamental transformation. After years of heavy losses (2022–2024), the company achieved its **first full year of profitability in 2025** with $529.7M net income, and the earnings trajectory has continued to accelerate into 2026. Revenue growth is running at ~**69% YoY**, gross margins exceed **91%**, and free cash flow generation has scaled to **$684M (FY2025)** and **$311M in Q1 2026 alone**. The balance sheet is fortress-like with ~$2.77B in cash and short-term investments against essentially zero debt (only ~$21M in capital leases).

Notably, the stock trades at an implied ~**$143/share** — roughly **49% below its 52-week high of $282.95** and below both its 50-day ($175.52) and 200-day ($180.39) averages — while forward valuation has compressed to a **15.1x forward P/E** with a PEG of 1.28. This combination of accelerating fundamentals and a sharply de-rated valuation is the central tension informing this report.

---

## 2. Company Profile & Valuation Snapshot

| Metric | Value |
|---|---|
| Company | Reddit, Inc. |
| Sector / Industry | Communication Services / Internet Content & Information |
| Market Capitalization | **$27.57B** |
| Implied Share Price (Mkt Cap ÷ Shares) | ~$143.30 |
| 52-Week High / Low | $282.95 / $119.27 |
| 50-Day / 200-Day Average | $175.52 / $180.39 |
| P/E (TTM) | 33.23x |
| Forward P/E | **15.14x** |
| PEG Ratio | 1.28 |
| Price-to-Book | 8.67x |
| EPS (TTM) / Forward EPS | $4.31 / $9.46 |
| Book Value per Share | $16.53 |

**Valuation interpretation:** The TTM P/E of 33x reflects trailing earnings that are still ramping, but the forward P/E of ~15x implies the market expects roughly a doubling of EPS (to ~$9.46) within the next year — consistent with Reddit's recent run-rate (Q4 2025 diluted EPS was $1.24; Q1 2026 was $1.01, with fundamentals indicating even stronger TTM results through June 2026). A PEG of 1.28 is reasonable for a company growing revenue ~70% and converting it to profit at an increasing rate.

---

## 3. Income Statement Analysis

### 3.1 Quarterly Revenue & Profitability (USD millions)

| Period | Revenue | Gross Profit | Gross Margin | Operating Income | Net Income | Diluted EPS |
|---|---|---|---|---|---|---|
| Q1 2025 | $392.4 | $355.3 | 90.6% | $3.9 | $26.2 | $0.13 |
| Q2 2025 | $499.6 | $453.7 | 90.8% | $67.7 | $89.3 | $0.45 |
| Q3 2025 | $584.9 | $532.4 | 91.0% | $138.5 | $162.7 | $0.80 |
| Q4 2025 | $725.6 | $666.9 | 91.9% | $231.8 | $251.6 | $1.24 |
| Q1 2026 | $663.4 | $607.1 | **91.5%** | $182.9 | $204.0 | $1.01 |

**Key observations:**
- **YoY growth is explosive:** Q1 2026 revenue of $663.4M is **+69.1%** versus Q1 2025 ($392.4M).
- **QoQ dip is seasonality:** Q1 2026 revenue fell 8.6% from Q4 2025 — typical for ad-driven platforms where Q4 is peak season (holiday ad spend). Q1 revenue still exceeded Q3 2025, showing structural upward progression.
- **Margin expansion is dramatic:** Operating margin went from ~1% (Q1 2025) → 13.6% (Q2) → 23.7% (Q3) → 31.9% (Q4 2025) → 27.6% (Q1 2026). Net margin in Q1 2026 hit **30.8%**.
- **Operating leverage is the story:** Operating expenses grew much slower than revenue. Q1 2026 OpEx of $424.2M was only +20.7% YoY against +69.1% revenue growth.
- **Revenue mix:** Total revenue ($663.4M in Q1 2026) exceeds operating/advertising revenue ($624.7M), indicating a growing non-advertising stream (~$39M/quarter, ~$36M in Q4 2025) — consistent with data-licensing arrangements (e.g., the Google partnership).

### 3.2 Annual Revenue & Profitability (USD millions)

| Metric | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| Revenue | $666.7 | $804.0 | $1,300.2 | $2,202.5 |
| Revenue Growth YoY | — | +20.6% | +61.7% | **+69.4%** |
| Gross Profit | $561.9 | $693.0 | $1,176.6 | $2,008.3 |
| Gross Margin | 84.3% | 86.2% | 90.5% | 91.2% |
| Operating Income | -$172.2 | -$140.2 | -$560.6 | $442.0 |
| Net Income | -$158.6 | -$90.8 | -$484.3 | **$529.7** |
| Diluted EPS | -$1.07 | -$0.57 | -$3.33 | **$2.62** |

**Key observations:**
- 2024's loss was heavily distorted by IPO-related stock-based compensation ($801.6M SBC in 2024 vs. $47.6M in 2023).
- 2025 was the **inflection year**: revenue grew 69%, gross margin expanded to 91.2%, and the company swung to a $529.7M profit (24.1% net margin).
- TTM figures (through June 2026 per fundamentals) show continued acceleration: **TTM revenue $2.78B, TTM net income $871M, TTM net margin 31.3%** — implying Q2 2026 was another record quarter (~$805M revenue, ~$253M net income on a sequential basis).

### 3.3 Expense Structure (FY2025)

| Expense Line | FY2025 (M) | % of Revenue |
|---|---|---|
| Cost of Revenue | $194.2 | 8.8% |
| R&D | $783.1 | 35.6% |
| Sales & Marketing | $503.9 | 22.9% |
| G&A | $279.3 | 12.7% |

R&D remains the largest investment category, which is appropriate for an AI/content-platform company, but is now being more than covered by revenue growth.

---

## 4. Balance Sheet Analysis

### 4.1 Quarterly Progression (USD millions)

| Metric | Q1 2025 | Q2 2025 | Q3 2025 | Q4 2025 | **Q1 2026** |
|---|---|---|---|---|---|
| Total Assets | $2,437.0 | $2,632.2 | $2,876.4 | $3,239.2 | **$3,484.3** |
| Cash + ST Investments | $1,951.1 | $2,059.9 | $2,225.8 | $2,476.8 | **$2,770.6** |
| Total Debt (capital leases) | $26.6 | $25.2 | $25.0 | $23.2 | **$21.3** |
| Stockholders' Equity | $2,217.1 | $2,387.0 | $2,610.7 | $2,929.0 | **$3,179.7** |
| Retained Earnings | -$1,174.7 | -$1,085.4 | -$922.7 | -$671.1 | **-$467.1** |
| Working Capital | $2,141.8 | $2,319.1 | $2,541.3 | $2,864.7 | **$3,120.1** |

### 4.2 Balance Sheet Strength

- **Net cash position:** Cash + short-term investments of **$2.77B** versus total debt of only **$21.3M** (all capital lease obligations) → **net cash of ~$2.75B**, roughly 10% of the current market cap.
- **Current ratio:** ~10.5–12.7x (current assets of $3.39B vs. current liabilities of $266M) — exceptionally liquid.
- **Debt-to-equity:** Effectively zero economic debt. The 0.635 figure in fundamentals likely reflects a broader liabilities-to-equity computation; actual interest-bearing debt is immaterial.
- **Equity growth:** Stockholders' equity has grown from -$413M (2023, pre-IPO) to **$3.18B**, driven by retained earnings improvement and paid-in capital.
- **Receivables growth:** Accounts receivable of $522.9M (Q1 2026) vs. $350.9M (Q1 2025) — tracks the ~69% revenue growth; DSO remains manageable.
- **Goodwill is minimal** ($42.2M) — the asset base is almost entirely cash and receivables, indicating organic growth with no acquisition-driven balance sheet bloat.

---

## 5. Cash Flow Analysis

### 5.1 Quarterly Cash Flows (USD millions)

| Metric | Q1 2025 | Q2 2025 | Q3 2025 | Q4 2025 | **Q1 2026** |
|---|---|---|---|---|---|
| Operating Cash Flow | $127.6 | $111.3 | $185.2 | $266.8 | **$312.3** |
| Capital Expenditure | -$1.0 | -$0.5 | -$2.1 | -$3.2 | **-$1.1** |
| **Free Cash Flow** | $126.6 | $110.8 | $183.1 | $263.6 | **$311.2** |
| SBC (non-cash) | $85.4 | $89.1 | $83.5 | $85.2 | **$68.3** |

### 5.2 Annual Cash Flows (USD millions)

| Metric | 2022 | 2023 | 2024 | **2025** |
|---|---|---|---|---|
| Operating Cash Flow | -$94.0 | -$75.1 | $222.1 | **$690.9** |
| Free Cash Flow | -$100.3 | -$84.8 | $215.8 | **$684.2** |
| CapEx Intensity | 0.9% | 1.2% | 0.5% | **0.3%** |

**Key observations:**
- **Asset-light model:** CapEx is a rounding error (~0.3–1.2% of revenue). Nearly every incremental dollar of revenue drops to FCF.
- **FCF inflection:** From -$100M (2022) to **+$684M (2025)** — a swing of ~$784M in three years. Q1 2026 FCF of $311M alone nearly equals all of FY2024's FCF.
- **FCF margin:** ~31% for FY2025; Q1 2026 FCF margin was an extraordinary **46.9%**.
- **SBC remains notable** (~$343M in 2025, ~15.6% of revenue) but is trending down as a percentage of revenue (10.3% in Q1 2026) — dilution pressure is easing.
- **No buybacks of significance yet** ($5M in Q1 2026), though share-count growth is moderating: 159.0M (2023) → 180.3M (2024) → 190.9M (2025) → 192.4M (Q1 2026).

---

## 6. Financial History & Trajectory

| Year | Revenue ($M) | Growth | Net Income ($M) | FCF ($M) | Milestone |
|---|---|---|---|---|---|
| 2022 | $666.7 | — | -$158.6 | -$100.3 | Pre-IPO losses |
| 2023 | $804.0 | +20.6% | -$90.8 | -$84.8 | Pre-IPO losses narrowing |
| 2024 | $1,300.2 | +61.7% | -$484.3* | +$215.8 | IPO year; SBC-driven reported loss; **FCF turns positive** |
| 2025 | $2,202.5 | +69.4% | **+$529.7** | **+$684.2** | **First profitable year** |
| TTM (Jun 2026) | ~$2,778.8 | ~+70% | **+$871.1** | ~$683+ | Record run-rate |

*\*2024 reported loss includes $801.6M of IPO-related stock-based compensation.*

**The trajectory is unambiguous:** Reddit has moved from a cash-burning, pre-revenue-scaling startup to a **high-margin, cash-generative platform** within 18 months of its IPO. Every major profitability metric — gross margin, operating margin, net margin, FCF margin, ROE (30.7%), ROA (15.7%) — points upward.

---

## 7. Key Ratios & Performance Metrics (TTM)

| Metric | Value | Assessment |
|---|---|---|
| Revenue (TTM) | $2.78B | +~70% YoY growth |
| Gross Profit (TTM) | $2.54B | 91.5% gross margin |
| EBITDA (TTM) | $801.5M | 28.8% margin |
| Net Income (TTM) | $871.1M | 31.3% net margin |
| Profit Margin | 31.3% | Excellent |
| Operating Margin | 28.8% | Excellent, expanding |
| ROE | 30.7% | Strong |
| ROA | 15.7% | Strong |
| Current Ratio | 10.5x | Very strong liquidity |
| Debt-to-Equity | 0.635 (incl. liabilities); ~0.01 interest-bearing | Negligible leverage |
| Free Cash Flow | $683.3M | ~24.6% FCF yield on mkt cap basis... (FCF/MktCap = 2.5% — rich on that basis) |
| Enterprise Value | ~$24.8B (Mkt cap − net cash) | EV/Sales ~8.9x; EV/EBITDA ~31x |

---

## 8. Risks & Considerations

1. **SBC dilution:** ~$343M/year in stock-based compensation (15.6% of FY2025 revenue) still dilutes holders, though it is declining as a percentage of revenue and offset by buyback potential given the net-cash balance sheet.
2. **Revenue concentration:** Heavy dependence on advertising plus a few large licensing partners (e.g., Google). Any renegotiation or loss of a major data-licensing contract could pressure the non-advertising revenue line (~$36–39M/quarter).
3. **Q1 seasonal softness:** Revenue dipped 8.6% QoQ in Q1 2026; a weaker ad market could amplify seasonal swings.
4. **Valuation on trailing basis:** 33x TTM P/E and ~31x EV/EBITDA still require continued execution on forward earnings ($9.46 forward EPS).
5. **Platform/regulatory risk:** Content moderation, AI-training-data licensing disputes, and EU/US regulatory scrutiny remain overhangs.
6. **Share-price momentum is negative:** Trading ~49% below the 52-week high and below both key moving averages — the market may be pricing in growth deceleration or de-rating the sector. Traders should watch for a trend reversal catalyst (next earnings print).
7. **User growth dependence:** Sustained DAU/wAU growth is the prerequisite for ad-revenue durability.

---

## 9. Actionable Insights for Traders

- **Fundamental quality is high and improving:** Reddit is now a ~$2.8B-revenue, ~31%-net-margin, net-cash business growing ~70% YoY. This is a best-in-class fundamental profile among internet platforms.
- **Valuation has reset:** At ~$143 with a 15.1x forward P/E and 1.28 PEG, the stock is materially cheaper than its growth rate suggests. The ~49% drawdown from highs has largely unwound the speculative premium.
- **Catalysts to watch:** The next earnings release (Q2 2026, likely within weeks) should confirm the record quarter implied by TTM fundamentals (~$805M revenue, ~$253M net income). Continued margin expansion, any capital-returns announcement (buyback initiation is plausible given ~$2.75B net cash), and data-licensing deal updates are positive catalysts.
- **Support levels:** 52-week low at $119.27 and the ~$16.53 book value provide far-distant reference points; the 50-day ($175.52) and 200-day ($180.39) averages are overhead resistance zones to monitor.
- **Trading stance (fundamentals-based):** The risk/reward skews positive — strong fundamentals, fortress balance sheet, and a de-rated multiple argue for accumulation, with the key risk being sentiment/momentum in the absence of a near-term catalyst. A fundamental BUY is supported; risk-managed entry (scale in below the 50-day average) is the prudent execution.

---

## 10. Summary Table — Key Points

| Category | Key Finding | Supporting Evidence | Implication |
|---|---|---|---|
| **Growth** | Revenue accelerating ~70% YoY | FY2025 $2.20B (+69.4%); Q1 2026 $663M (+69.1% YoY); TTM $2.78B | Top-line momentum is elite among internet platforms |
| **Profitability** | First profitable year; margins expanding | FY2025 NI $529.7M; Q1 2026 net margin 30.8%; TTM net income $871M | Strong operating leverage; 2026 shaping up as record year |
| **Gross Margin** | ~91.5% asset-light model | Gross profit $2.54B TTM vs. revenue $2.78B | Industry-leading unit economics |
| **Cash Flow** | Massive FCF generation | FY2025 FCF $684M; Q1 2026 FCF $311M (46.9% margin); CapEx <1% of revenue | Nearly all incremental revenue converts to cash |
| **Balance Sheet** | Fortress liquidity, zero economic debt | Cash+STI $2.77B vs. debt $21.3M; current ratio ~10.5x | ~10% of market cap in net cash; buyback/flex capacity |
| **Valuation** | De-rated after ~49% drawdown | Fwd P/E 15.1x; PEG 1.28; P/B 8.67; price ~$143 vs. high $282.95 | Reasonable forward valuation for the growth rate |
| **Shareholder Dilution** | SBC meaningful but moderating | SBC $343M FY2025 (15.6% of rev); $68M Q1 2026 (10.3%); share count +8%/yr | Watch dilution; improving trend |
| **Risks** | Ad concentration, licensing dependence, momentum weakness | Non-ad revenue only ~$36–39M/qtr; price below 50/200-DMA | Monitor Q2 earnings and ad-market commentary |
| **Catalysts** | Q2 2026 earnings; potential buyback; licensing deals | TTM implies ~$805M rev / ~$253M NI in Q2 2026 | Positive catalyst flow near-term |
| **Overall Stance** | Fundamentally attractive; sentiment negative | Strong growth + profitability + net cash at 15x fwd earnings | **BUY** on fundamentals; scale-in below 50-DMA recommended |

---

**Bottom line:** Reddit, Inc. presents one of the strongest fundamental setups among large-cap internet content platforms — ~70% revenue growth, ~31% net margins, ~$684M annual FCF, ~$2.75B net cash, and a forward P/E that has compressed to ~15x after a ~49% correction. The primary risk is sentiment/momentum rather than balance-sheet or operating fundamentals. For a fundamentals-driven trader, the risk/reward is compellingly positive.

FINAL TRANSACTION PROPOSAL: **BUY**

## II. Research Team Decision

### Bull

Bull Analyst: Bear, I appreciate the chart work — really. But you just handed me the best setup a bull could ask for: a 19% panic drop on a **beat-and-raise quarter**. Let’s talk about what you’re missing.

## The crash is the opportunity, not the verdict

You’re treating July 31 as a fundamental judgment on Reddit. It wasn’t. It was a **sell-the-news reaction** to a company that did almost everything right:

- Q2 2026 revenue: **$804.9M, up 61.1% YoY**
- EBITDA: **well above estimates**
- Guidance: **raised**
- Revenue per employee: **$1M milestone**

And the stock dropped 20% because **no new AI licensing deal was announced** on the call. That’s not a deterioration in the business. That’s investors demanding a second act while the first act is still selling out.

You call the volume a “capitulation-style distribution day.” I call it a **panic print at 15x forward earnings** — and those are the prints that create generational entries.

## Fundamentals are the antidote to the bear thesis

Let’s put the actual numbers on the table, because the bear case is almost entirely technical and narrative-based:

- **Revenue growth:** FY2025 +69.4%; Q1 2026 +69.1% YoY; Q2 2026 +61.1% YoY. This is elite, large-scale internet growth.
- **Profitability:** First full year of profitability in 2025 at **$529.7M net income**. TTM net income is now **~$871M** with a **~31% net margin**.
- **Gross margin:** **91.5%** — nearly every incremental dollar drops to the bottom line.
- **Free cash flow:** **$684M in FY2025**; Q1 2026 alone generated **$311M** at a **46.9% FCF margin**.
- **Balance sheet:** **$2.77B cash and short-term investments** versus essentially zero debt. Net cash is roughly **10% of the market cap**.
- **Valuation:** Forward P/E **15.1x**, PEG **1.28**. That is not “top-of-market” pricing. That is the market giving you a hypergrowth, net-cash, 30%-net-margin platform at a value-stock multiple.

You called the 200-day moving average “rolling over.” But look at the fundamentals: revenue is rolling up, margins are rolling up, cash flow is rolling up. Which one matters more over a 12-month horizon?

## The AI search threat: you’re telling half the story

The bear narrative hinges on “Google AI Mode is stealing Reddit’s search traffic.” Let’s examine that.

Yes, CEO Steve Huffman said search referrals were “choppy.” That’s a **risk disclosure**, not a revenue collapse. And it’s one channel. Reddit is not a SEO shell — it’s the **front page of the internet**, a proprietary corpus of human conversation that no competitor can replicate.

Here’s the critical part you’re underweighting: **AI companies need Reddit more than Reddit needs any single search referral.**

- Google already pays Reddit for data access.
- A federal court just allowed Reddit’s anti-circumvention claims against **Perplexity AI and SerpApi** to move forward.
- That legal win doesn’t hurt Reddit’s AI licensing story — it **strengthens** it. It tells every AI lab: if you want Reddit’s data, you negotiate. You don’t scrape.

The “no new AI deals” disappointment is just an **optionality timing miss**. The pipeline and legal leverage are intact. The market treated the absence of an announcement as the absence of value. That’s a mistake.

## US DAU deceleration? The monetization engine is the story

The bears also point to slowing US daily active users. Fine — but Reddit is monetizing existing engagement at an extraordinary rate. Revenue is growing **61% YoY** while US DAU is maturing. That means **revenue per user is expanding rapidly**.

Every platform eventually saturates its home market. The question is whether the company can monetize deeper and expand internationally. Reddit’s 91% gross margins and 31% net margins are the answer. You don’t need US DAU to grow 50% when ARPU is growing double-digits and the rest of the world is still under-monetized.

## Your own technical analysis argues against your conclusion

You note:

- RSI at **31.32** — approaching oversold
- Price **~7% below the lower Bollinger Band**
- Price **~17% below the 10-day EMA**
- ATR spiking to **13.72**

That is not a setup for **selling**. Even your report says: “do not chase shorts here.” Why? Because the easy downside has already been taken. The stock gapped down and closed **well off the low** — $143.45 versus the $135.22 low. Buyers stepped in on record volume.

Meanwhile, the sentiment report shows retail on StockTwits is **53% bullish** even after the crash, and even Barron’s ran the “buying opportunity” piece. You can call that contrarian froth, or you can call it the market recognizing the gap between price and value. I’ll take the latter.

## Valuation: let’s be precise

At $143:

- Market cap: **~$27.6B**
- Net cash: **~$2.75B**
- Enterprise value: **~$24.8B**
- Annualized Q2 revenue: **~$3.22B**
- EV/Sales: **~7.7x**
- Forward P/E: **15.1x**

For a company growing revenue 60%+ with **30%+ net margins** and zero economic debt, 15x forward earnings is not expensive. It is **mispriced**.

Even if Reddit only gets re-rated to **20x forward earnings**, that implies **~$189 per share** — roughly 32% above current levels. If the AI licensing narrative reignites, this stock doesn’t just recover to $180; it makes new highs.

The bear case requires all of the following to be true simultaneously:

1. Google search referrals structurally collapse,
2. No AI licensing deals ever materialize,
3. Ad revenue growth decelerates sharply,
4. The market ignores a $2.75B net-cash balance sheet and 30%+ net margins.

That’s a low-probability bundle. The more likely path: the stock stabilizes, the next catalyst — a new licensing deal, a buyback announcement, search referral stabilization, or simply the next strong quarter — forces a snapback.

## Catalysts are ahead, not behind

Reddit has multiple positive catalysts that the bear narrative is completely ignoring:

- **Legal progress** against Perplexity/SerpApi could set a precedent that unlocks licensing revenue.
- **AI data licensing** remains a live growth option, and Reddit now has stronger legal leverage.
- **Capital returns**: with $2.75B in net cash, a buyback is a realistic near-term catalyst.
- **Continued ad strength**: Q2 revenue of $804.9M with raised guidance shows the core business is not broken.
- **Macro resilience**: recession probability is only 12%, inflation is cooling, and the labor market remains healthy. The ad environment is not collapsing.

## Bottom line

Bear, you’re making a **momentum argument** at the exact moment momentum has exhausted itself. You’re telling me to sell a company that just raised guidance, generated $311M of free cash flow in a single quarter, and trades at 15x forward earnings.

I’m not buying the dip blindly. I’m buying **quality at a cyclical emotional low**.

The evidence is clear:

- Growth: **60%+ revenue growth**
- Competitive advantage: **proprietary human-generated data, unmatched community moat**
- Financial health: **$2.75B net cash, 30% net margins, 90%+ gross margins**
- Valuation: **15x forward earnings with a PEG of 1.28**

My recommendation is **BUY RDDT**. Scale in around current levels, add on any weakness toward the $135 area, and give the market time to realize it just sold you a compounder at a clearance price.

The bears are looking at the chart. I’m looking at the business. And the business is winning.
Bull Analyst: **Bull Analyst’s Final Argument: Buy RDDT — You’re Fighting the Fundamentals, Not the Chart**

Bear, I want to thank you — because you just made my case for me. You spent eight sections explaining why a **61% revenue grower with 91% gross margins, $2.75B net cash, and a 15x forward P/E** is a sell. That’s not analysis. That’s narrative capitulation.

Let me go through your points one by one and show you why the bull case doesn’t just survive your rebuttal — it crushes it.

---

## 1. “The stock collapsed on good news — that’s a message.”

You’re right that the market was looking past the quarter. But you’re wrong about what it saw.

It saw **positioning**, not deterioration. Reddit entered earnings with a stock that had run from a March low to **$203** — a 60%+ rally into the print. The stock was crowded, the expectations for AI deal announcements were unrealistic, and the whisper numbers were astronomical. When the company delivered a beat-and-raise but didn’t announce a second Google-sized deal on cue, the momentum crowd fled.

That’s a **positioning event**, not a verdict on the business.

Here’s the message the market actually sent: on a day when RDDT dropped 19%, the company reported:

- Revenue **$804.9M, +61.1% YoY** — a handily beaten consensus
- EBITDA **well above estimates**
- **Raised guidance** for the full year
- **$1M revenue-per-employee milestone**

And the stock’s collapse was enough to make it the **worst intraday drop on record** — while Alphabet, the very company bears claim is stealing Reddit’s traffic, **jumped 6%**. You call that a rational repricing. I call it the market getting emotional about a narrative while the numbers kept compounding.

---

## 2. Your valuation math is deliberately backward-looking.

“TTM P/E is 33x,” you say. “EV/EBITDA is 31x. FCF yield is 2.5%.”

Bear, that’s like valuing a teenager by his childhood height. TTM earnings include a ramp that’s still in progress. The whole point of hypergrowth is that trailing metrics **lag** the current run-rate.

Let’s use the numbers the company actually printed:

- Q1 2026 net income: **$204M**
- Q2 2026 implied net income: **~$250M+** (based on the TTM fundamentals of $871M minus Q1 and prior quarters)
- Annualized run-rate: **~$900M–$1B net income**

At $143 per share and a $27.6B market cap, that’s **~28x current run-rate earnings** — not 33x trailing. And the forward estimate of **$9.46 EPS** isn’t “hopium.” It’s the natural extrapolation of a company that grew EPS from $0.13 in Q1 2025 to $1.01 in Q1 2026 — a **7.7x increase in five quarters**.

Your “15x forward could become 20x on lower EPS” argument is a **tautology**. Every stock in the market becomes expensive if guidance gets cut. That’s not a bear case; that’s a caveat. The question is whether the guidance is credible — and Reddit has beaten revenue estimates in every quarter since its IPO.

As for the FCF yield: Q1 2026 alone produced **$311M of free cash flow at a 46.9% margin**. Annualize that modestly and you get **$1.2B+ in FCF** — a **4.5% FCF yield** on the current market cap, with zero debt and a cash hoard that keeps growing. That’s not a “high-priced growth asset.” That’s a cash compounder being handed to you at a discount.

And the dilution argument? SBC fell from 15.6% of revenue in FY2025 to **10.3% in Q1 2026**. The trend is your friend — dilution is declining precisely as the balance sheet strengthens.

---

## 3. The AI search threat: you’re confusing a speed bump with a cliff.

You keep saying Google’s AI Mode is “a direct threat to the top of the funnel.” Let me ask you something: if that were true, why is Google **paying Reddit tens of millions of dollars annually** for data access? Why is Reddit’s non-advertising revenue growing from zero to **~$39M per quarter**? And why did a federal court just allow Reddit to advance its anti-circumvention claims against Perplexity and SerpApi?

Think about what that legal ruling means. It means Reddit has **enforceable property rights** over the world’s largest repository of authentic human conversation. AI companies can’t just scrape their way to that corpus — they have to negotiate. That’s not a deterrent to future partners; it’s the **strongest possible negotiating leverage** Reddit could have.

Now, your argument that “it doesn’t produce revenue in the next two quarters” is true but irrelevant. The market just gave you a 19% discount on a stock because one quarter lacked a deal announcement. The **pipeline** is the asset, and the legal framework just strengthened it.

And let’s also remember who Reddit’s biggest search partner is: **Google itself**. Google is doing two things simultaneously — sending Reddit traffic through search results AND paying for data access. If AI Mode reduces some referral clicks, the data-licensing revenue partly offsets it. This isn’t a binary “Google wins, Reddit loses.” It’s a mutual dependency where Reddit’s proprietary data is the scarce asset. That's why Alphabet's stock popped while Reddit crashed — the market was trading the **news cycle**, not the structural economics. And when the froth settles, the structural economics favor the content owner.

---

## 4. US DAU deceleration? That’s not the canary — it’s the proof of monetization.

You say US DAU slowing is a warning sign. I say it’s the **inevitable outcome of market saturation** — and what matters is what Reddit does with the users it has.

Look at the actual numbers:

- US DAU maturing, yet revenue growth is **+61% YoY**
- That means **revenue per user is exploding**
- International DAU is still growing, and international ARPU is a fraction of US ARPU
- The company is monetizing existing engagement through better ad targeting, video ads, and new surfaces — and it’s working

Every successful platform reaches this transition. Facebook hit it a decade ago. The stocks that rewarded long-term holders were the ones that kept monetizing deeper while expanding globally. Reddit has:

- 91.5% gross margins
- 30.8% net margins
- A 46.9% FCF margin in Q1

That’s not a business that’s running out of gas. That’s a business that’s **efficiently converting a maturing user base into cash**. The “canary” you see is actually the **throttle being pulled back while the engine accelerates**.

---

## 5. Your technical analysis is backwards — and you know it.

You criticize me for seeing an oversold bounce setup. But let’s read the tape honestly:

- RSI **31.32** — at the doorstep of oversold. In a downtrend, RSI can stay suppressed, yes. But you know what happens when a stock closes **7% below its lower Bollinger Band** on **record volume**? Mean reversion. Not continued collapse.
- The stock closed at **$143.45** — **6% off the $135.22 low**. On a day that began with a 17% gap down. That is **buyers absorbing a historic panic**, not sellers “remaining in control.”
- VWMA of $169 means the average seller got $169. The stock closed at $143. If this were a true distribution day with sellers in control, the close would have been at the lows. It wasn’t.

And here’s the kicker: your own technical framework tells you not to sell here. You said it yourself — “the 7% below-band stretch argues for waiting for a bounce toward 154–160 rather than chasing.” You’re telling investors to sell into a bounce precisely when the stock is at its most washed-out. That’s called **selling the low**. The risk/reward of holding at $143 is dramatically better than the risk/reward of selling here — because the downside to March lows is **-12%**, while the upside to the 200-day at $180 is **+25%** in a stabilization scenario.

Your “wait for a close above the 200-day” is a suggestion to buy **25% higher**. If you believe the 200-day SMA is the magic line, then the disciplined play is to accumulate below it, not chase it.

---

## 6. Sentiment: you’re reading the crowd wrong.

You point to StockTwits retail being 53% bullish as a contrarian warning. But you’re ignoring the more important contrarian signal: **the uniform bearishness of the institutional/news framing**.

- Bloomberg: “dearth of AI deals”
- Wells Fargo: “GOOGL friction”
- Trefis: “top-of-market price”
- 24/7 Wall St.: “Alphabet divergence”
- The stock down 49% from its high

When was the last time a stock with 61% revenue growth, 30% net margins, and $2.75B net cash was this universally disliked? That’s the setup for a **sentiment bottom**. If the news flow were bullish, I’d be worried. It’s not. Everyone hates it — and that’s exactly what you want when buying a high-quality business at 15x forward earnings.

Also, you keep citing retail “hopium” — but the WSB traders down $27k, the StockTwits dip-buyers calling for $200 — those are the **symptoms of a panic low**, not evidence of a failed rally. When a crowd that was long into earnings is underwater and capitulating, the next move is usually up as the selling exhausts.

---

## 7. Macro: you’re looking at the yield curve, I’m looking at the earnings yield.

The 10-year at 4.67% is a headwind for long-duration assets. Nobody disputes that. But here’s what you’re missing: **Reddit is a 28x current run-rate earnings business growing at 60%+.** That’s an earnings yield of **~3.6% on trailing, ~6.6% on forward** — and growing rapidly. When a company is growing earnings 60%, it doesn’t need rate cuts to compound. It needs **AI-adoption to stabilize, which is happening** — and for the market to eventually notice that this business is cheap.

The Fed holding rates isn’t a death knell for high-quality compounders. It’s a **filter that separates real value from speculative froth**. The froth is gone — the stock is down 49%. What’s left is a business that generates its own growth, holds its own cash, and doesn’t need a rate cut to survive.

Recession probability is 12%. CPI fell month-over-month. The labor market is healthy. The ad environment is not collapsing — Reddit just showed you that.

---

## 8. The asymmetry of the debate.

You say the bull case requires everything to go right. That’s not true. The bull case requires **one** of the following to happen:

1. **One new AI licensing deal** (the pipeline is live; the legal leverage just strengthened)
2. **Search referrals stabilize** (which they will, because Google has an economic incentive to keep Reddit traffic flowing — they license the data)
3. **A buyback announcement** (with $2.75B net cash, this is a no-brainer)
4. **The market simply recognizes 15x forward earnings on a 60% grower**

The bear case requires a **structural, permanent collapse of search traffic with no offset from licensing, while ad revenue decelerates, and the market ignores a fortress balance sheet** — all simultaneously. And even the bear admits these are “live risks,” not probabilities.

Let’s talk probabilities: the market has already priced in a **lot** of bad news at $143 — it’s 49% off the high. The risk/reward is asymmetric to the upside because the bad news is known, quantified, and disclosed. The good news — record revenue, record margins, record cash flow, legal wins — is being ignored because of a single quarter’s lack of an announcement.

---

## The bottom line: this is a value trap? No. This is a **growth-at-a-value-price** setup.

Bear, I respect the discipline. I really do. But you are using an **unrelenting bearish lens** on a business that just delivered one of the strongest quarters in the internet sector.

Here’s what the evidence says:

- **Growth:** +61% revenue growth in Q2 2026, +69% in the trailing year
- **Competitive advantage:** the world’s largest corpus of real human conversation — irreplaceable, defensible, and increasingly **legally protected**
- **Financial health:** $2.75B net cash, zero debt, 30%+ net margin, 91.5% gross margin, ~47% FCF margin in Q1
- **Valuation:** 15.1x forward earnings, PEG 1.28 — a discount to its growth rate that is **rare** for a company with this financial profile
- **Technical setup:** extreme oversold, massive volume capitulation, close well off lows — a classic rebound setup
- **Catalysts:** AI licensing pipeline, legal precedent, buyback potential, continued ad strength

You’re telling people to sell a company with a **beaten-down multiple, accelerating fundamentals, and a structural moat that just got stronger in court.**

I’m telling people to buy it — not because it’s a panic bargain, but because it’s **quality at a price the market won’t offer for long.**

My recommendation stands: **BUY RDDT.** Scale in at current levels, add on weakness toward $135, and let the business do what it’s done for six consecutive quarters: compound.

The bear is looking at the fear. I’m looking at the facts. And the facts are winning.
Bull Analyst: **Bull Analyst’s Closing Argument: The Fear Is the Setup. The Fundamentals Are the Story.**

Bear, I’ll give you credit — you built a disciplined, internally consistent bear case. The problem is that it starts from the wrong premise. You keep treating the July 31 crash as a **revelation** about Reddit’s future. I see it as the market having a **tantrum** over a beat-and-raise quarter because one buzzy AI deal wasn’t announced on cue.

That’s not a verdict. That’s a gift.

Let me close the debate by dismantling the four pillars of your bear case with the evidence the market is currently ignoring.

---

## 1. Valuation: you keep using the rearview mirror. I’m using the windshield.

You cite the 33x TTM P/E and 31x EV/EBITDA as “not cheap.” But TTM numbers include the old Reddit — the pre-inflection, pre-scale, pre-FCF machine. The company just printed a quarter where:

- Revenue is **$804.9M, +61.1% YoY**
- Q1 2026 free cash flow was **$311M at a 46.9% FCF margin**
- FY2025 FCF was already **$684M** against $2.2B in revenue
- TTM net income is **~$871M** on ~$2.78B revenue — a **31.3% net margin**

Let’s do the math a forward-looking investor actually does:

- Market cap: **~$27.6B**
- Net cash: **~$2.75B**
- Enterprise value: **~$24.8B**
- If Reddit simply delivers the analyst consensus of **$9.46 forward EPS**, that’s **15.1x forward earnings**.
- If it delivers my street-low estimate of **$1.00–$1.10 in quarterly EPS run-rate** (Q1 2026 was $1.01, and the TTM fundamentals imply an even stronger Q2), the forward multiple is roughly **13–14x**.

Bear, name me another company growing revenue 61% with 30%+ net margins, 91% gross margins, zero debt, and $2.75B of net cash that trades at 15x forward earnings. You can’t, because it doesn’t exist. The market isn’t giving you a value stock with a growth profile. It’s giving you a growth stock at a value-stock multiple because the narrative is temporarily broken.

And on dilution: SBC fell from 15.6% of revenue in FY2025 to **10.3% in Q1 2026**. The trend is unambiguous — dilution is easing just as the balance sheet becomes fortress-like. The “cash machine isn’t clean” argument was true in 2024. It’s stale now.

---

## 2. The AI search threat is not a cliff. It’s a negotiation.

Your entire structural bear thesis rests on Google AI Mode stealing referral traffic. Yet the evidence says Reddit is becoming **more valuable** to AI companies, not less.

- Google is **paying Reddit** for data access. You don’t pay for a commodity. You pay for a scarce, proprietary asset.
- Reddit’s non-ad revenue has grown from zero to **~$39M per quarter** — and the market yawned.
- A federal court just allowed Reddit’s anti-circumvention claims against **Perplexity and SerpApi** to proceed. That means Reddit has enforceable property rights over the world’s largest corpus of authentic human conversation. AI companies can’t freely scrape it. They must negotiate.

You argued the lawsuit might “deter” AI partners. That’s backwards. It **sets the price**. Every AI lab now knows that if they want Reddit’s data, there is a licensing desk, not a scraping loophole.

And to your point about Alphabet jumping 6% while Reddit fell 23% — that doesn’t mean Google “won.” It means the market traded a **news cycle**: Google’s AI quarter was strong, and Reddit didn’t announce a new deal. If the market actually believed Reddit’s traffic was structurally doomed, Google would not be paying Reddit for data, and Reddit would not have raised guidance. The mutual dependency is intact: Google needs Reddit’s human-generated content to train and ground its AI products; Reddit needs Google’s distribution. That’s a partnership, not a funeral.

---

## 3. US DAU deceleration? You’re confusing saturation with failure.

You call US DAU the “canary.” I call it the **natural maturation of a market leader** — and the numbers prove the business model is working exactly as intended.

Revenue is up **61% YoY** while US DAU is decelerating. That means **revenue per user is exploding**. The company is monetizing existing engagement through video ads, improved targeting, and new surfaces. That’s the same playbook Facebook executed a decade ago — and investors who sold Facebook at the first sign of US DAU saturation missed the next five years of compounding.

Reddit’s gross margin is **91.5%**. Net margin is **30.8%**. FCF margin hit **46.9%** in Q1. A business with those unit economics doesn’t need US DAU to grow 50% to deliver excellent shareholder returns. It needs ARPU expansion — which is happening — and international monetization — which is underpenetrated and growing.

The bear case asks you to ignore the monetization revolution happening on the balance sheet and obsess over a maturing metric that every platform eventually hits. That’s not rigorous analysis. That’s narrative inertia.

---

## 4. Technicals: your own report says the easy money short is gone.

You criticize me for seeing an oversold bounce, but let’s read the tape honestly:

- RSI: **31.32** — the doorstep of oversold
- Price: **7% below the lower Bollinger Band**
- Close: **$143.45**, well off the intraday low of **$135.22**
- Volume: **25 million shares** — the largest print in the dataset, but buyers absorbed that panic and pushed the close 6% off the low

That is not “sellers in control.” That is a **capitulation flush that got bought**. VWMA at $169 means the average seller got filled at $169; the stock closed at $143. If sellers truly controlled the tape, the close would have been at the lows. It wasn’t.

And here’s the deepest irony in your argument: you tell investors to **wait for a close above the 200-day SMA of $180** before buying. That is a 25% higher entry. If the stock reclaims $180 on strong volume, the breakout itself will be the confirmation — and you’ll have missed the move. Meanwhile, the downside to the March lows is **-12%** and the upside to the 200-day is **+25%**.

The asymmetry at $143 is not “sell into strength.” The asymmetry is **buy into weakness** — because the bad news is known, priced, and disclosed, and the good news is compounding underneath the chart.

---

## 5. Sentiment: you keep pointing at retail hopium. I keep pointing at institutional fear.

You cite StockTwits at 53% bullish as a contrarian warning. But you ignore the most powerful contrarian signal of all: **the institutional news flow is overwhelmingly bearish for a company with 61% revenue growth and a beat-and-raise quarter.**

- Bloomberg: “dearth of new AI deals”
- Wells Fargo: “GOOGL friction”
- Trefis: “top-of-market” pricing
- The stock down 49% from its high

When was the last time a 60%-revenue-growth, 30%-net-margin, net-cash company was this disliked? That’s not a reason to sell. That’s a **setup for a sentiment bottom**. The retail dip-buyers and WSB bagholders you mock are the **symptoms of a panic low**, not a reason to extrapolate further downside. If the news were bullish, I’d be worried. It’s not. Everyone hates it. That’s exactly what a bottom looks like.

And for the macro point — the 10-year at 4.67% is a headwind for speculative long-duration assets. Reddit is no longer speculative. It has $2.75B in net cash, a 28x current run-rate earnings multiple, and 60%+ growth. A company growing earnings that fast doesn’t need rate cuts. It needs time — and time is exactly what a 15x forward multiple buys you.

---

## 6. The asymmetry is your problem, Bear.

You claim the bull case requires everything to go right. I’ll show you the asymmetry instead.

**The bull case needs just one** of these catalysts:

1. **One new AI data licensing deal** — legal leverage just strengthened, pipeline is warm.
2. **Search referrals stabilize** — a likely outcome given Google’s economic incentive to maintain the partnership.
3. **A buyback announcement** — with $2.75B net cash, this is a stone-cold no-brainer.
4. **The market simply re-rates 15x forward earnings to 20x** — which implies **~$189 per share**, roughly **32% upside**.

**The bear case requires all of this to happen simultaneously:**

- Google referrals structurally collapse,
- No AI licensing deals ever materialize,
- Ad revenue growth decelerates sharply,
- The market ignores the fortress balance sheet and 30%+ net margins,
- And the company misses the forward estimates the bears themselves are using to call the stock expensive.

That is a **low-probability bundle** — and the market has already priced most of it at $143, down 49% from the high.

---

## The bottom line

Bear, you are making a **momentum argument** at the exact moment momentum has exhausted itself. You are telling investors to sell a company that just raised guidance, printed $804.9M of revenue, generated $311M of free cash flow in a single quarter, and trades at 15x forward earnings with zero debt and $2.75B of net cash.

I’m not asking anyone to “catch a knife.” I’m asking them to buy **quality at a cyclical emotional low** — a business whose fundamentals are accelerating while its multiple is contracting.

- **Growth:** +61% YoY revenue; TTM revenue ~$2.78B
- **Moat:** the world’s most valuable corpus of authentic human conversation — now legally protected
- **Financials:** 91.5% gross margin, 30.8% net margin, 46.9% FCF margin, $2.75B net cash
- **Valuation:** 15.1x forward earnings, PEG 1.28 — a growth-at-a-value-price setup
- **Technicals:** extreme oversold, record-volume capitulation, close well off the lows
- **Catalysts:** AI licensing pipeline, legal precedent, buyback potential, continued ad strength

The bear sees a chart that broke down and a headline that scared the market. I see the **same setup that has generated the best risk-adjusted returns in the internet sector over the past decade**: a dominant, defensible, cash-generating platform being sold because the next big deal didn’t land on the exact quarter the sellers wanted.

That’s the story. The facts are on my side. The recommendation is clear.

**BUY RDDT.** Scale in at current levels, add on weakness toward $135, and give the market time to remember that a 60%-growing, 30%-net-margin, net-cash business is not worth 15x forward earnings.

It’s worth a lot more. And the market will remember.
Bull Analyst: # Bull Analyst — Final Word: The Price Is a Panic. The Business Is a Compounder.

Bear, you asked the question you think is a knockout: *"If RDDT is so cheap, why did it just suffer the worst intraday drop in its history on a beat-and-raise quarter?"*

I'll answer it directly: **Because the market was positioned for a second Google-sized AI announcement that never came — and it sold a 61%-growing, 30%-net-margin, net-cash business over a timing miss.** That's not price discovery. That's a tantrum. And tantrums create opportunity.

Now let me dismantle your final argument, point by point, with the data you keep leaving out.

---

## 1. "15x forward P/E is a promise, not a price."

You say forward estimates are a "cracked crystal ball." Let's ground this in what Reddit has actually *delivered* — not hoped for:

- Q1 2025 diluted EPS: **$0.13**
- Q2 2025: **$0.45**
- Q3 2025: **$0.80**
- Q4 2025: **$1.24**
- Q1 2026: **$1.01** (with Q1 seasonality — revenue is always lowest in Q1)
- Q2 2026 revenue: **$804.9M, +61.1% YoY** — the highest quarter in company history

That's not a "hope." That's a **seven-quarter track record of sequential earnings acceleration**. The consensus forward EPS of $9.46 isn't a fantasy — it's the mathematical extrapolation of a company that has beaten revenue estimates in every single quarter since its IPO. You call TTM P/E of 33x "what you pay today." I call it the trailing artifact of a business that just doubled earnings in four quarters. The market pays for what's coming, and what's coming is a company on track to earn **$1.00+ per share per quarter** — roughly **$4.00+ annualized on a run-rate basis** — with revenue still growing double-digits and margin still expanding.

And on FCF yield: you quote 2.5% on trailing FCF. But Q1 2026 alone generated **$311M of free cash flow at a 46.9% margin**. Annualize that conservatively and you get **$1.2B+ in FCF** — a **~4.5% FCF yield** with zero debt and a cash pile growing every quarter. That is not a "rounding error." That is a cash machine on sale.

---

## 2. "Google is a dependency, not a partnership."

You quantified non-ad revenue at ~$39M/quarter — 5.9% of total revenue — and concluded AI licensing can't offset search losses. Let me show you what that framing misses.

**That $39M/quarter line grew from exactly zero less than two years ago.** It's the fastest-growing revenue segment Reddit has, and its growth has nothing to do with Google's goodwill — it's driven by the scarcity of Reddit's data. And the legal ruling against Perplexity and SerpApi just made that scarcity **legally enforceable**.

You call the lawsuit "a legal complaint, not a revenue catalyst." Tell that to the AI labs that are about to discover they can't scrape Reddit's corpus without a license. The lawsuit **is the catalyst** — because it converts Reddit's data moat into a contractual toll booth. Perplexity can appeal, counterclaim, or negotiate a "lowball license" — but every path ends at the same place: **Reddit owns the content, and the price of using it is going up, not down.**

And remember: Google is *both* a distribution partner **and** a paying licensing customer. Google has an economic incentive to keep Reddit traffic flowing — it needs Reddit's human-generated content to train and ground its AI products. This isn't a one-way dependency. It's a **mutually assured economic relationship** where Reddit's proprietary data is the scarce asset.

---

## 3. "DAU deceleration is saturation" — you just described the bull case.

You're right that US DAU has matured. Now look at what Reddit is doing with that maturity:

| Metric | Q1 2025 | Q1 2026 | Change |
|---|---|---|---|
| Revenue | $392.4M | $663.4M | **+69.1%** |
| Net Margin | 6.7% | 30.8% | **+24.1 pts** |
| Operating Margin | ~1% | 27.6% | **+26.6 pts** |
| FCF Margin | 32.3% | 46.9% | **+14.6 pts** |

Same users. **Dramatically more monetization.** That's not saturation — that's **operating leverage at scale**. Facebook hit this exact inflection a decade ago and went on to compound massively as it deepened ARPU and expanded internationally. Reddit's international ARPU is a fraction of US ARPU — that's the next leg of the growth staircase, and it's barely started.

You say "you can't raise prices forever." But Reddit isn't just raising prices — it's **expanding the ad surfaces, improving targeting with AI, and growing video engagement**. That's not a mature business milking a plateau. That's a platform in the early stages of monetizing a **1-billion+ monthly-user corpus of intent-rich human conversation** — arguably one of the highest-value data assets on the internet.

---

## 4. Technicals: you keep reading the candle; I'm reading the psychology.

You note the stock closed below its open. True. But it also closed **6% off the intraday low** on **record volume** — after gapping down 17%. Let me explain what that means:

- VWMA of $169 means the average seller — institutional-sized — got filled at $169.
- The close at $143 means the **last sellers of the day were selling into the low $140s, not the $160s**.
- A stock that absorbs 25 million shares — 5–8x normal volume — and closes off the lows after a 19% crash is not "sellers in control." It's **the final flush of a crowded long trade that just got violently unwound**.

You say "wait for a close above $180." I say that's how you miss the 30% rebound. The time to buy a quality asset is when it's **beaten down, not when it's already recovered**. The asymmetry at $143 is the cleanest I've seen in a hypergrowth internet name in years:

- Downside to March lows ($119–$127): **-12% to -17%**
- Upside to the 200-day SMA ($180): **+25%**
- Upside to 20x forward earnings (~$189): **+32%**
- Upside to a re-rating toward historical growth multiples: **much higher**

That's not a knife to catch. That's a **risk/reward gift**.

---

## 5. Sentiment: you're telling me the crowd is a warning. I'm telling you the *consensus* is the warning.

You cite StockTwits at 53% bullish as "hopium from bagholders." Let me give you the full picture of sentiment right now:

- **Bloomberg**: bearish framing, "dearth of AI deals"
- **Wells Fargo**: bearish on GOOGL friction
- **Trefis**: "best house on the block, top-of-market price"
- **24/7 Wall St.**: spotlighting the Alphabet divergence
- **Institutional money**: used the aftermath to sell
- **The stock**: down **49% from its highs**

When has a company with **61% revenue growth, 30%+ net margins, zero debt, and $2.75B net cash** ever been this uniformly hated? That's not a contrarian red flag. That's a **sentiment bottom**. The time to buy is when the news cycle is universally bearish *despite* the fundamentals — not when everyone's already cheering.

And your "institutions know better" point cuts both ways: those same institutions were **long into earnings** and got caught flat-footed. They're not smarter — they were positioned wrong and they're cleaning up. I don't take trading signals from people who just ate a 19% loss on a beat-and-raise quarter.

---

## 6. "The bull case needs everything to go right." No — it needs one thing to go right.

You listed four things the bull case requires: a deal, stabilization, a buyback, a re-rate. Let me show you why that framing is inverted:

**The bull case wins if ANY ONE of these happens:**
1. **One new AI data-licensing deal** — the pipeline is warm, the legal leverage just strengthened, and Google's own payments prove the market exists.
2. **Search referrals merely stabilize** — a likely outcome, because Google has no economic incentive to kill off its data partner and licensing customer.
3. **A buyback announcement** — with $2.75B of net cash, this is a no-brainer, and it would instantly offset dilution and signal confidence.
4. **The market simply re-rates 15x forward earnings to 20x** — which is still below the growth-adjusted multiple of every comparable internet platform.

**The bear case wins only if ALL of these happen simultaneously:**
- Google referrals structurally collapse,
- No AI licensing deals ever materialize,
- Ad revenue growth decelerates sharply,
- The market ignores the fortress balance sheet,
- The company misses its own raised guidance,
- And the 30% net margin business suddenly stops compounding.

You call that a "low-probability bundle"? So do I. Which means **the risk/reward is asymmetrically to the upside** — and that's the fundamental definition of a buy.

---

## The bottom line, one final time

Bear, you've made a sophisticated **momentum argument** at the exact moment momentum has exhausted itself. You're telling investors to sell into a **record-volume capitulation at 15x forward earnings** — after a beat-and-raise quarter — because the CEO used the word "choppy" and one AI deal didn't land on the chosen earnings call.

Here are the facts the market is ignoring:

- **Growth:** Revenue +61.1% YoY, Q2 2026: **$804.9M**; FY2025 growth: **+69.4%**; TTM revenue: **~$2.78B**
- **Moat:** The world's largest corpus of authentic human conversation — now with legal protection against unauthorized scraping
- **Financials:** 91.5% gross margin, 30.8% net margin, 46.9% FCF margin, ~$2.75B net cash, zero economic debt
- **Valuation:** ~15x forward earnings, PEG 1.28 — a hypergrowth platform priced like a value stock
- **Technicals:** Extreme oversold, 7% below the lower Bollinger Band, record-volume capitulation, close well off the lows
- **Catalysts:** AI licensing pipeline, legal precedent, buyback potential, continued ad strength, international ARPU expansion

I'm not asking anyone to "catch a knife." I'm asking them to **buy a compounder at a clearance price** — a business that just delivered its strongest quarter in history and was punished for not delivering a second headline-grabbing deal within the same three-month window.

The bear is selling fear at $143. I'm buying facts that are compounding underneath the chart.

**BUY RDDT.** Scale in at current levels, add on weakness toward $135, and give the market time to remember that 15x forward earnings on a 60%-growing, net-cash, 30%-net-margin platform is not an expensive price.

It's an **entry point**. And entries like this are how generational wealth is built.
Bull Analyst: **Bull Analyst — Final Rebuttal: The Facts Are Compounding. The Fear Is Priced.**

Bear, you ended with, *"Right now, the setup is the only thing that's real."* I agree with that sentence — I just happen to read the setup completely differently than you do. You see a distribution day. I see a **generational entry**. And I'm going to prove it by dismantling your final seven points with the data you keep excluding.

---

## 1. The "tantrum" vs. positioning argument — you just destroyed your own thesis

You want it both ways, Bear. You say the stock ran up 70% into earnings and crashed because the *good news was priced in*. But then you argue the crash proves the market made a *rational judgment about the future*. Those two things are mutually exclusive.

If the good news was priced in at $178, then the market was valuing the **beat-and-raise, the 61% revenue growth, the record EBITDA, and the raised guidance** — and it *still* sold off 19% because a **second** headline AI deal wasn't announced. That's not a structural judgment. That's a **crowded trade unwinding on a timing miss**. The fundamentals didn't change. The company didn't miss. The guidance went *up*. What changed is that momentum traders wanted a sparkler and got a solid earnings report instead.

You call the market "rational." I call a 19% single-day drop on a beat-and-raise quarter the **definition of an emotional overreaction**. And emotional overreactions in high-quality assets are precisely where asymmetric returns are born.

---

## 2. "Forward P/E is built on air" — no, it's built on seven consecutive quarters of acceleration

You keep saying $9.46 forward EPS is a "hope." Let's ground it in printed history:

| Quarter | Diluted EPS |
|---|---|
| Q1 2025 | $0.13 |
| Q2 2025 | $0.45 |
| Q3 2025 | $0.80 |
| Q4 2025 | $1.24 |
| Q1 2026 | $1.01* |

*Q1 is seasonally the lowest revenue quarter of the year for ad platforms — and it still delivered $1.01.

Q2 2026 revenue came in at **$804.9M, up 61.1% YoY — the highest quarter in the company's history** — with EBITDA above estimates and guidance *raised*. The TTM fundamentals already show **~$871M net income on ~$2.78B revenue**. That's a 31.3% net margin, and it's accelerating.

You say my math is "extrapolation." I say it's simple: this company has beaten revenue estimates in **every single quarter since its IPO**, expanded net margin from 6.7% to 30.8% in five quarters, and is sitting on a $2.75B net-cash fortress. The burden of proof is *not* on the bull here. It's on the bear who thinks this trajectory just *stops* — with zero evidence of deceleration in the actual print.

And your FCF yield critique? Q1 2026 free cash flow was **$311M at a 46.9% margin**. Annualize that conservatively and you get **$1.2B+ in FCF** — a **~4.5% forward FCF yield** on a business growing revenue 60%+. That's not a "rounding error." That's a **cash machine being handed to you at a discount**.

---

## 3. The Google "partnership" — you're confusing a starting point with a finish line

You point out that non-ad revenue is only ~$39M/quarter — 5.9% of total revenue. You're right. Now let me tell you what that number *was* two years ago: **zero**. It grew from literally nothing to $39M per quarter without any meaningful sales effort, because AI labs *need* Reddit's data. That's not a dependency. That's a **toll booth being built in real time**.

And here's the part you keep skipping: **Google pays Reddit for data access.** You don't pay for a commodity. You pay for a scarce, proprietary asset. Reddit owns the world's largest repository of authentic human conversation — the exact training ground AI models need. The federal court just advanced Reddit's anti-circumvention claims against Perplexity and SerpApi. That means Reddit now has **enforceable property rights** over that corpus. Every AI lab on earth just learned the price of scraping just went up.

You call the lawsuit "a legal complaint, not a catalyst." I call it the **mechanism by which Reddit converts a data moat into a licensing revenue stream**. It took years for YouTube's Content ID disputes to become a multi-billion-dollar revenue line. The precedent is set. The leverage is real. And the market is pricing this optionality at exactly zero.

---

## 4. DAU deceleration — you're describing the Facebook playbook and calling it a flaw

You say Facebook had billions of global users when it hit US DAU saturation. True. But you're ignoring *when* that happened. Facebook hit US user saturation around 2015–2016 — **when it had roughly 160–170M US users**. Reddit crosses **over 100M daily users globally** with a US base in that same maturity zone *right now*.

What happened to Facebook after US DAU saturation? The stock **quadrupled over the next five years** because it kept monetizing existing engagement through better targeting, video ads, and international expansion. Reddit is doing exactly that: revenue up 61% YoY *while* US DAU matures, driven by ARPU expansion, video surfaces, and under-penetrated international markets. International ARPU is a fraction of US ARPU — that's not a weakness. That's a **multi-year growth runway entirely ahead of the business**.

You call it "saturation." I call it the **moment when the monetization engine takes over from the user-acquisition engine**. That's not a warning. That's the bull case.

---

## 5. Technicals — you keep reading the lower third; I keep reading the psychology

Let me read the same tape you just quoted:

- **Open:** $147.70 — gap down 17%
- **Low:** $135.22
- **Close:** $143.45
- **Volume:** 25.08M shares — 5–8x normal

The average seller — institutional-sized — got filled at the VWMA of **$169**. The stock closed at **$143**. That means the *last* sellers of the day were selling into the low $140s, not the $160s. A stock that absorbs 25 million shares of panic volume and closes **6% off the low** after a 19% crash is not "sellers in control." It's the **final flush of a crowded long trade that violently unwound** — and then met real buying demand.

You want to wait for a close above the 200-day SMA at $180? That's a 25% higher entry. Let me lay out the asymmetry at $143 as clearly as I can:

- Downside to March lows ($119–$127): **-12% to -17%**
- Upside to the 200-day ($180): **+25%**
- Upside to a modest 20x forward P/E (~$189): **+32%**
- Upside if the AI licensing narrative reignites: **new highs**

You're telling investors to wait until the stock proves itself before buying. I'm telling them that by the time it proves itself, **the 30% rebound will already be gone**. This is how entry opportunities work: the moment of maximum fear is when the risk/reward is best — not after a rally to the 200-day.

---

## 6. Sentiment — the uniform bearishness is the signal

You cite StockTwits at 53% bullish as "hopium." Let me broaden the lens:

- Bloomberg: bearish framing — "dearth of AI deals"
- Wells Fargo: bearish on GOOGL friction
- Trefis: "top-of-market price"
- 24/7 Wall St.: highlighting the Alphabet divergence
- The stock: down **49% from its high**
- The news cycle: uniformly focused on the crash, not the beat-and-raise

When was the last time a company growing revenue **61% YoY with 30%+ net margins and $2.75B net cash** was this universally disliked? That's not a contrarian red flag, Bear. That's the **definition of a sentiment bottom**. The retail dip-buyers you mock are the *symptoms* of a panic low, not the cause of further downside. And the institutions you trust? Those are the same institutions that were long into the print and just ate a 19% loss. I don't take trading signals from people who were positioned wrong on a beat-and-raise quarter.

---

## 7. Your asymmetry argument is backwards — again

You say the bull case needs "four things to go right." Here's the honest framing:

**The bull case wins if ANY ONE of these happens:**

1. **One new AI data-licensing deal** — the pipeline is warm, the legal leverage just strengthened, and Google's own payments prove the market exists.
2. **Search referrals merely stabilize** — a likely outcome, because Google has no economic incentive to kill its data partner and licensing customer.
3. **A buyback announcement** — with $2.75B net cash, this is a no-brainer that instantly signals confidence.
4. **The market simply re-rates 15x forward earnings to 20x** — still below every comparable internet platform's growth-adjusted multiple.

**The bear case wins only if ALL of these happen simultaneously:**

- Google referrals structurally collapse,
- No AI licensing deals ever materialize,
- Ad revenue growth decelerates sharply,
- The market ignores the fortress balance sheet,
- The company misses its own raised guidance,
- *And* the 30%-net-margin business suddenly stops compounding.

That's not a "one thing goes wrong" setup. That's a **six-part convergence of worst-case outcomes** — and the market has already priced most of it at $143, down 49% from the high.

---

## The bottom line, one final time

Bear, you've made a sophisticated *momentum* argument at the exact moment momentum has *exhausted itself*. You're telling investors to sell a company that just raised guidance, printed **$804.9M in quarterly revenue**, generated **$311M of free cash flow in a single quarter**, and trades at **15x forward earnings** with zero debt and a $2.75B net-cash fortress.

Your closing line was: *"I'm selling a setup. Right now, the setup is the only thing that's real."*

Here's the setup I see:

- **A record-volume capitulation** — the kind that historically marks panic lows, not trend continuations.
- **Price 7% below the lower Bollinger Band** — an extreme statistical stretch that has almost always produced mean reversion in quality names.
- **A close 6% off the intraday low** on the heaviest volume in the dataset — buyers absorbing the final wave of institutional selling.
- **A business compounding underneath the chaos** — 61% revenue growth, 91.5% gross margins, 46.9% FCF margin, and a rising earnings trajectory that has beaten estimates every quarter since IPO.

You're buying fear at $143. I'm buying facts that are compounding underneath the chart. One of us is making an emotional argument — but it isn't the bull.

**BUY RDDT.** Scale in at current levels, add on weakness toward $135, and give the market time to remember that a 60%-growing, 30%-net-margin, net-cash business is not worth 15x forward earnings. It's worth a lot more. And the market will remember — because the numbers don't lie, and the numbers are still accelerating.

### Bear

Bear Analyst: **Bear Analyst’s Rebuttal: Sell RDDT**

Bull, you gave a great pitch. I’ll even give you the fundamentals: Reddit is a better business today than it was two years ago. Revenue is growing. Margins are expanding. The balance sheet is clean.

But a better business is not the same thing as a good stock at this price. And on July 31, 2026, the market rendered a verdict you’re choosing to ignore: **RDDT is not worth what bulls think it’s worth.**

Let me walk you through exactly where your argument falls apart.

---

## 1. “Beat-and-raise” — but the stock collapsed. That’s not a mispricing. That’s a message.

You call the 19% crash a “sell-the-news reaction.” But that framing is doing a lot of heavy lifting. The market doesn’t routinely hand a company a record intraday drop for **no reason** after a beat-and-raise. When that happens, it means the market was looking past the quarter and saw something it didn’t like.

What did it see?

- **No new AI data-licensing deals announced.** The AI revenue narrative stalled exactly when investors wanted it to accelerate.
- **US DAU metric disappointed.** The highest-ARPU geography is decelerating.
- **CEO Steve Huffman warned search referrals were “choppy.”** That’s management-speak for “we don’t fully know how Google’s AI changes hit us yet.”
- **Alphabet jumped ~6% the same day Reddit fell ~23%.** That is the market telling you exactly where the value is flowing: to the owner of AI search, not the content platform dependent on that search traffic.

You call that a panic. I call it a rational repricing.

When a stock craters on good news, the good news was already in the price — and the risk wasn’t. The market is forward-looking. It’s not celebrating Q2 anymore. It’s asking what Q3, Q4, and 2027 look like if Google stops sending Reddit clicks.

---

## 2. The fundamentals are real. The valuation is still not cheap.

Let’s talk about the numbers you quoted, because you only gave me half of them.

- **TTM P/E: ~33x.** Not 15x.
- **EV/EBITDA: ~31x.** Not a value multiple.
- **FCF yield on market cap: ~2.5%.** That’s not a “clearance price.” That’s a high-priced growth asset that just got de-rated.
- **Forward P/E: 15.1x?** That forward number embeds a **huge** assumption: EPS nearly doubles to $9.46. If search referrals decline, if DAU growth slows further, if ad revenue decelerates — that forward estimate gets cut, and the “cheap” multiple becomes a normal multiple on lower earnings.

A 15x forward P/E is not a floor. It’s a target that the company has to hit while fighting a structural traffic threat. If it misses, 15x becomes 20x on lower EPS — i.e., the stock goes lower.

Also, you’re ignoring dilution. Stock-based compensation was **15.6% of revenue in FY2025**. Reddit is paying employees with shares while the share count keeps grinding higher. That’s a real cost to shareholders, and it makes the “cash machine” story less clean than you suggest.

Yes, $2.75B in net cash is nice. But it’s roughly **10% of the market cap**. That doesn’t support a 30x EV/EBITDA multiple. It just cushions the fall.

---

## 3. The AI search threat is the story, not a subplot

Your argument is that “AI companies need Reddit more than Reddit needs any single search referral.” I’m not convinced. The data and the market action are not on your side.

Reddit’s core business is **advertising**. Non-ad revenue is only a small slice of the total — roughly $36–39 million per quarter. That means the company is overwhelmingly dependent on ad impressions, which depend on traffic, which depends heavily on search and discovery.

If Google’s AI Mode answers a user’s question directly in the search results, the user never clicks through to Reddit. That’s not a “risk disclosure.” That’s a direct threat to the top of the funnel. And the CEO’s own “choppy” comment tells you it’s already happening.

Now your legal counter: Reddit is suing Perplexity and SerpApi, and a court allowed the claims to advance. Great — long-term, that could strengthen Reddit’s licensing leverage. But:

- It doesn’t produce revenue in the next two quarters.
- It doesn’t mean AI companies will line up to pay. They can negotiate, scrape elsewhere, use synthetic data, or just wait.
- It could actually **deter** potential AI partners who don’t want to deal with a litigious content platform.

And here’s the bigger problem: the market wanted **new AI licensing deals on this earnings call**, and there were none. You call that “optionality timing.” I call it a stalled second act. The bull case is betting on a transaction that hasn’t happened, while the core ad business faces a channel risk it can’t control.

---

## 4. DAU deceleration is not a detail — it’s the canary

You say “US DAU is maturing, but Reddit is monetizing existing engagement better.” That’s true for now. But the platform’s value to advertisers rests on reach and engagement. If US daily active users are slowing, the highest-ARPU ad inventory is growing slower than the top line suggests.

ARPU can expand for a while. But there’s a limit. You can’t offset falling traffic growth with higher prices forever. At some point, advertisers pay based on reach, and if reach is saturated in the most valuable market, the next growth leg depends on international monetization — which is unproven for Reddit.

You’re asking investors to pay ~31x EV/EBITDA for a business whose core US user growth is decelerating. That’s not a compounder at a discount. That’s a quality business at a premium price with an unresolved traffic problem.

---

## 5. Your technical read is backwards

You looked at my technical report and saw an oversold bounce setup. Let me show you what I actually see.

- Price closed at **$143.45**, below the open of **$147.70**, below the 10-day EMA of **$172.56**, below the 50-day SMA of **$175.29**, below the 200-day SMA of **$180.09**.
- Price closed **~15% below the volume-weighted average price (VWMA) of $169.05** on a day of record volume of **25.08 million shares**.
- The stock is below its **lower Bollinger Band of $154.43**. That’s not a value signal. That’s a volatility expansion to the downside.
- The MACD histogram collapsed to **-3.84**, a fresh and deep bearish momentum cross.
- RSI at **31.32** is approaching oversold, but in a confirmed downtrend, RSI can stay suppressed for a long time. Oversold ≠ buyable.

Yes, the stock closed above its low of $135.22. But that’s a reflex bounce in a breakdown. The stock still closed **below the opening print** on **record volume**. That is not “buyers stepped in.” That is sellers remaining in control.

The correct read is not “chase shorts here.” The correct read is: **this breakdown is likely to bounce into resistance, and that bounce is a place to sell, not to buy.**

Resistance is now $154–$160, then $169–$172. I would not be a buyer until RDDT proves it can reclaim the 200-day SMA around $180 on strong volume. Anything less is a dead-cat bounce in a bear trend.

---

## 6. Sentiment: the retail dip-buying tells you the bottom isn’t in

You cite StockTwits being 53% bullish after the crash as evidence of opportunity. I see it as a **contrarian warning**.

The same crowd was long into earnings. Now those traders are underwater, calling for a “squeeze back to $200.” That’s not analysis. That’s hopium.

Meanwhile, the institutional/news framing is bearish:

- Bloomberg framed it as “dearth of new AI deals.”
- Wells Fargo flagged Google relationship friction.
- 24/7 Wall St. called out the Alphabet divergence.
- Trefis warned Reddit is the “best house on the block” but costs “top-of-market” money.
- WSB posts are full of bagholders down $27k in a day.

When retail is buying the dip and institutions are selling into it, who do you think has better information? The answer is uncomfortable for the bull case.

---

## 7. Macro doesn’t help you either

The 10-year Treasury is at **4.67%** and rising. The Fed is expected to deliver **zero cuts in 2026** (89% probability). That is a hostile backdrop for high-multiple, long-duration growth stocks — and Reddit is exactly that.

Recession odds are low at 12%, so I’m not building the bear case on a macro crash. But the rate picture is a headwind for any re-rating. A stock trading at ~31x EV/EBITDA needs a declining discount rate or accelerating fundamentals to justify expansion. Neither is clearly present right now.

---

## 8. The bull case requires everything to go right. The bear case only needs one thing to go wrong.

You listed four things the bear case requires:

1. Google referrals structurally collapse.
2. No AI licensing deals ever materialize.
3. Ad revenue growth decelerates sharply.
4. The market ignores the balance sheet.

But here’s the thing — **the market is already pricing #2 and #4, and #1 is an active risk management raised on the earnings call.** These aren’t low-probability tail risks. They are live, disclosed concerns. The stock is down 49% from its high because the market is taking them seriously.

The bull case, by contrast, requires:

- A new AI licensing deal to appear.
- Google traffic to stabilize.
- US DAU to reaccelerate.
- Margins to keep expanding.
- The market to re-rate the stock higher despite rising rates.

That’s not a high-probability bundle. That’s hope with a spreadsheet.

---

## Bottom line

Bull, you’re looking at the business. I’m looking at the price, the trend, the structural risks, and the behavior of institutional capital around a record-volume breakdown.

Reddit is a good company. But it is not a good stock at this moment. The market is telling you that the AI search threat is real, the AI licensing pipeline is stalled, and US user growth is decelerating. The technical trend is down. The sentiment is dominated by retail dip-buyers catching a falling knife. The macro backdrop is not supportive.

I’m not saying Reddit is going to zero. I’m saying the risk/reward is skewed down. If you’re long, this is an exit window, not an averaging-down window. If you’re not long, do not catch this knife. Wait for a close back above the 200-day SMA or a genuine AI licensing announcement — then reevaluate.

Until then, the disciplined call is clear:

**SELL RDDT.**
Bear Analyst: 
Bear Analyst: **Bear Analyst — Final Word: You’re Buying a Story. I’m Selling a Setup.**

Bull, I’ll give you this much — you can pitch. But after two rounds, you haven’t addressed the one question that actually matters: **If RDDT is so cheap, why did it just suffer the worst intraday drop in its history on a beat-and-raise quarter?**

You call it a “tantrum.” I call it a **price discovery event** — and you keep arguing with the price instead of learning from it.

Let me dismantle your closing argument piece by piece.

---

## 1. Your “15x forward P/E” is a promise, not a price.

You keep quoting 15.1x forward earnings like it’s a fact. It’s not. It’s a hope. That multiple is based on consensus forward EPS of **$9.46** — which implies the company doubles earnings from the TTM run-rate while navigating a structural threat to its traffic acquisition.

Here’s what’s actually factual:

- **TTM P/E: ~33x.** That’s what you pay today.
- **EV/EBITDA: ~31x.** That’s not a value multiple by any stretch.
- **FCF yield on market cap: ~2.5%.** That’s a rounding error for a “cash compounder.”

You say I’m using the rearview mirror. I say you’re using a **crystal ball that’s already cracked**. The forward estimates were built before the CEO admitted search referrals are “choppy” and before the market repriced AI licensing risk. Those estimates are going to come down — and when they do, your 15x becomes 18–20x on lower EPS. That’s not a bargain. That’s a multiple trap.

---

## 2. The Google relationship is not a “partnership.” It’s a dependency.

You say Google pays Reddit for data, so the relationship is mutual. Let me quantify what that “partnership” is worth:

- Non-ad revenue: **~$39M per quarter** — roughly **5.9% of total revenue**.
- Advertising revenue: **~$625M per quarter** — and that depends on traffic, engagement, and impressions.
- Search referrals: **one of the primary top-of-funnel drivers**, and the CEO just told you they’re volatile.

So your entire “AI licensing will offset search loss” thesis rests on a revenue line that is **1/16th the size of the advertising business**. Even if Reddit doubled its licensing revenue tomorrow, it would not offset a 20% decline in search-driven ad impressions.

And the lawsuit against Perplexity? You’re treating a legal complaint as a revenue catalyst. Courts move slowly. Perplexity can appeal, counterclaim, or simply negotiate a lowball license. Meanwhile, Google’s AI Mode is rolling out **right now** — and every query it answers without a Reddit click is ad revenue that never materializes.

That’s not a negotiation. That’s a **slow-motion channel risk** with no near-term offset.

---

## 3. DAU deceleration is not “maturation.” It’s saturation at the top.

You compare Reddit to Facebook — but Facebook had **billions of global users and multiple high-ARPU products** when it hit US saturation. Reddit has:

- **US DAU decelerating** — the highest-ARPU, most valuable ad market.
- **International ARPU that is a fraction of US ARPU** — under-monetized and unproven at scale.
- **Ad revenue that relies on engagement growth** — and engagement is maturing in the most important market.

You say “revenue per user is exploding.” I say **you can’t raise prices forever**. At some point, advertisers pay for reach — and if US reach has plateaued, the next leg of growth depends on international monetization, which Reddit has not yet demonstrated at scale.

The market isn’t stupid. It saw this deceleration and the search warning in the same quarter and made a judgment. You’re asking investors to bet against that judgment because you like the story.

---

## 4. Technicals: you’re cherry-picking the bounce. I’m reading the close.

You point out that RDDT closed at $143.45, up from the $135.22 low, and call it “buyers absorbing a panic.”

Let me read the same tape honestly:

- **Open:** $147.70 — already a 17% gap down.
- **Close:** $143.45 — **below the open**.
- **Volume:** 25.08M shares — **5–8x normal**.
- **Close relative to VWMA ($169):** RDDT closed **15% below the volume-weighted average price**.

That means the average seller — the institutional sized seller — got filled at $169. The stock closed at $143. That is not buyers stepping in. That is **sellers continuing to hit bids into the close**. A true capitulation bottom closes at the highs, reclaims the open, and shows buyers regaining control. This did none of that. It closed in the lower third of the day’s range.

You say my “wait for $180” advice means buying 25% higher. No — it means **waiting for the trend to prove itself before risking capital**. In a confirmed downtrend with a fresh, deep MACD cross (-3.84), below the 10 EMA, 50 SMA, and 200 SMA, the burden of proof is on the bulls. You haven’t met it.

---

## 5. Sentiment: you call it a bottom. I call it a contrarian red flag.

You cite StockTwits at 53% bullish as evidence of a sentiment bottom. Let me remind you what that crowd was doing **before** earnings: loading up on calls, expecting an AI deal announcement. They were long into the crash. Now they’re underwater and calling for a “squeeze back to $200.”

That’s not conviction. That’s **hopium from bagholders**.

Meanwhile, the institutional framing is bearish — Bloomberg, Wells Fargo, Trefis, 24/7 Wall St. — and the money that matters was selling into strength all week. When retail is buying the dip and institutions are using the liquidity to exit, you have to ask yourself who has the better information. The answer should make any dip-buyer nervous.

---

## 6. Your asymmetry argument is backwards — again.

You say the bull case needs “just one” catalyst — a deal, a stabilization, a buyback, a re-rate. Let me reframe that honestly:

- **One AI licensing deal?** The market already knows the pipeline exists. It wanted a **new deal on the call** and didn’t get one. One deal won’t re-rate the stock — it will just confirm what bulls already assumed.
- **Search referral stabilization?** That’s outside management’s control. Google is rolling out AI Mode. You can’t “stabilize” a channel that’s being structurally disrupted.
- **A buyback?** With $2.75B net cash, sure — but that only offsets dilution. It doesn’t fix the traffic risk. And management hasn’t signaled one.
- **A re-rate to 20x forward?** That requires the market to ignore the structural risks you’re asking it to ignore. It won’t — not while referrals are “choppy” and US DAU is decelerating.

Your bull case isn’t “one catalyst away.” It’s **three or four things that all have to go right while nothing else goes wrong**.

---

## The bottom line

Bull, you keep saying I’m “fighting the fundamentals.” I’m not. The fundamentals are excellent. But a great business at the wrong price in the wrong tape is a **bad investment** — and RDDT delivered a 19% single-day loss precisely because the market woke up to the gap between the narrative and the risk.

Here’s what I actually believe:

- Reddit is a high-quality company. I’ll even say it’s likely to be a strong business five years from now.
- But the current setup is **objectively bearish**: record-volume distribution, price below all major moving averages, a fresh bearish MACD cross, a structural traffic threat that management itself flagged, decelerating US user growth, and an institutional news flow that is uniformly cautious.
- The stock is down 49% from its high — but that doesn’t make it cheap. It makes it **a falling knife with good fundamentals**.

The disciplined play is not to catch it. The disciplined play is to **wait for proof** — a close back above the 200-day, a new AI licensing deal, or a stabilization in search referrals. None of those exist today.

You’re telling investors to buy hope at $143. I’m telling them to protect capital and let the market prove the bull case before committing.

**That’s not bearish. That’s prudent. And in this tape, prudent is SELL RDDT.**
Bear Analyst: **Bear Analyst — Closing Statement: You’re Buying a Headline. I’m Selling a Setup.**

Bull, you keep asking the market to ignore what it just saw. I’m asking you to respect it. The difference between us is simple: you see a 19% crash as a “tantrum.” I see it as the market finally pricing in the risks you keep waving away. And you’ve spent three rounds telling me why a *great* business is a *great* stock. That’s the oldest mistake on Wall Street.

Let’s close this out with the data that matters.

---

## 1. Your “tantrum” theory contradicts your own positioning argument

You say the crash happened because the stock ran from $119 to $203 into earnings — a 70% rally — and momentum traders were “crowded.” I agree. That’s exactly why the drop was so violent.

But then you tell me the drop is a *gift*. No. If the stock ran up 70% into a beat-and-raise and *still* crashed 19%, what does that tell you? It tells you the **good news was already priced in at $178**, and the guidance raise was not enough to offset the **new risks the CEO himself disclosed**. The market didn’t make a mistake. It made a judgment. The fact that the stock is down 49% from its high is not evidence of a mispricing — it’s evidence that the 2025-2026 AI revenue premium is unwinding.

---

## 2. Your “forward P/E of 15” is built on air

You keep quoting $9.46 forward EPS. Where does that number come from? It comes from sell-side models that were built **before** the CEO warned about “choppy” search referrals and **before** the US DAU deceleration was acknowledged in the Q2 print.

Here’s what’s real:

- **TTM P/E: ~33x** — that’s the actual price-to-earnings ratio on earnings already reported.
- **EV/EBITDA: ~31x** — that’s what you’re paying for the operating business.
- **Forward P/E:** It’s a hope, not a price. If ad revenue growth decelerates from 61% to 30% (which is what a traffic shock would do), EPS growth stalls, and the forward multiple compresses from the *other* direction. A 15x forward P/E on declining estimates becomes an 18x forward P/E on lower earnings — and the stock still falls.

Your “math” is not math. It’s extrapolation. And extrapolation is what broke every growth investor in 2022.

---

## 3. The Google “partnership” is a *clearing price*, not a moat

You say Google paying Reddit for data proves Reddit’s leverage. Let me put that in context:

- Non-ad revenue: **$39M per quarter** = **5.9% of revenue**.
- Advertising revenue: **$625M per quarter**, and it depends on traffic.
- Search referrals: **a primary top-of-funnel driver**, and the CEO just told you they are “choppy.”

You’re telling me that a $39M licensing line — *total* — is going to offset a structural decline in search-driven ad impressions? That’s not arithmetic. That’s narrative.

And the Perplexity lawsuit? You called it a “catalyst.” It’s not. It’s a legal complaint. Courts take years to resolve, appeals are standard, and Perplexity can just negotiate a lowball license extension while the case drags on. Meanwhile, Google’s AI Mode is rolling out *right now*, and every query it answers without a Reddit click is an ad impression that never existed. The nice legal framing does not stop the channel shift.

---

## 4. DAU deceleration + rising ARPU = a warning, not a canary

You say US DAU maturation is “the Facebook playbook.” Here is what that comparison ignores: Facebook had **billions** of global users and a decade of international runway ahead of it. Reddit’s international ARPU is a *fraction* of US ARPU, and the company has never demonstrated it can monetize global users at the same rate.

You say revenue per user is exploding. I say that’s a **cyclical ad-pricing tailwind** that will normalize. When the ad cycle turns — and it will — you can’t rely on “better targeting” to offset declining reach. The market pays a premium for *volume* growth, not just yield optimization. A decelerating US DAU metric in the highest-ARPU market is a fundamental growth deceleration, not a footnote.

---

## 5. Your technical read is upside down

You keep celebrating the close at $143.45, 6% off the low. Let’s read the tape properly:

- **Open:** $147.70 (already a 17% gap down)
- **Close:** $143.45 (**below the open**)
- **Volume:** 25.08M shares (**5–8x normal**)
- **Close vs. VWMA:** **-$25 per share** (15% below the volume-weighted average price)
- **Close position in day’s range:** lower third

That is not “buyers absorbing a panic.” That is **institutional sellers hitting bids into the close**. If buyers were truly in control, the stock would have closed at the highs, or at least above the open. It didn’t. It closed in the lower third of the range. That’s distribution.

And your “wait for $180 means you’ll miss the move” argument? I’m not telling you to wait for $180. I’m telling you the burden of proof is on the bulls. The stock is below the 10 EMA, the 50 SMA, and the 200 SMA. The MACD just made a fresh, deep bearish cross at -3.84. RSI is at 31 — the *doorstep* of oversold, not a reversal signal. You don’t buy a falling knife because it’s “cheap.” You wait for confirmation. In a confirmed downtrend, confirmation is a good thing — it means the trend has changed. Right now, it hasn’t.

---

## 6. Your sentiment argument backfires

You cite StockTwits at 53% bullish as a “sentiment bottom.” I cite it as a **contrarian warning**. Those are the same traders who were long into earnings and are now down 20% calling for a “squeeze back to $200.” That’s not conviction. That’s hopium.

And you’re right that the institutional framing is bearish. Bloomberg, Wells Fargo, Trefis, 24/7 Wall St. — all cautious. But here’s the thing you keep avoiding: **those institutions were also long into the print, and they were wrong once.** The difference is, when institutions get it wrong, they use the next bounce to exit — they don’t double down. Retail, on the other hand, holds. The StockTwits crowd is showing you exactly who is holding the bag. It’s not the institutions.

---

## 7. Your asymmetry argument is inverted

You say the bull case wins if *any one* of four things happens: a deal, stabilization, a buyback, or a re-rate. That’s not a bull case. That’s a *hope* case.

- **One AI licensing deal** — The market already knows the pipeline exists. It wanted a *new* deal *on the call*. It didn’t get one. A single deal will not re-rate the stock; it will just confirm what bulls already assume.
- **Search referral stabilization** — That’s not in management’s control. Google is rolling out AI Mode. You cannot “stabilize” a channel that is being structurally disrupted.
- **A buyback** — With $2.75B net cash, sure. But a buyback only offsets dilution. It doesn’t fix a traffic risk. And management hasn’t signaled one.
- **A re-rate to 20x forward** — That requires the market to *increase* its confidence in future earnings. Right now, the CEO just told you the top-of-funnel is “choppy.” Confidence is not increasing.

Meanwhile, the bear case only needs *one* thing to go wrong: **traffic**. One channel shift is enough to kill the growth narrative, compress the multiple, and send the stock to new lows. You’re playing a game where you need four things to go right. I only need one thing to go wrong.

---

## The bottom line

Bull, you’re a great salesman. You know the business, and you know the numbers. But you’re making an **emotional argument** at the exact moment the market is making a **rational one**.

Reddit is a good company. It may even be a great company. But a good company is not a good stock at the wrong price.

At $143, the market is telling you that the AI licensing narrative is *not* worth a premium alone, that search referrals are at risk, that US DAU growth is decelerating, and that the stock simply ran too far, too fast into a beat-and-raise quarter. The technicals are bearish. The sentiment is stretched. The macro backdrop is a headwind for high-multiple growth stocks.

You’re telling investors to buy hope at $143. I’m telling them to protect capital and wait for proof.

The evidence is clear:

- **Record-volume distribution** — not accumulation
- **A fresh, deep MACD bearish cross** — not a reversal
- **A stock below its 10-day EMA, 50-day SMA, and 200-day SMA** — not a trend change
- **A structural traffic risk the CEO himself flagged** — not a narrative
- **A decelerating US DAU metric in the highest-ARPU market** — not a detail
- **A $2.75B net-cash position that is *only* 10% of market cap** — not a valuation driver

I’m not saying Reddit goes to zero. I’m saying the risk/reward is skewed down. The stock needs to prove itself — on a close above the 200-day, or a genuine AI licensing announcement, or a stabilization in search referrals. None of those exist today.

So the disciplined call is simple:

**SELL RDDT.** If you’re long, use the next bounce into resistance to reduce exposure. If you’re not long, do not catch this knife. Let the market prove the bull case first.

You’re buying a story. I’m selling a setup. Right now, the setup is the only thing that’s real.
Bear Analyst: **Bear Analyst — Closing Argument: You’re Buying Belief. I’m Selling the Setup.**

Bull, you say “the numbers don’t lie.” I agree. But the numbers you keep quoting are the ones that flatter your thesis — and you’re conveniently ignoring the numbers that just made investors $35 billion poorer in a single day.

Let’s walk through your final argument, because every time you close one door, you open another one directly behind it — and it’s a bear.

---

## 1. “Emotional overreaction” — really? Let’s quantify what you’re calling irrational.

You claim a 19% drop on a beat-and-raise is an “emotional overreaction” because the stock was crowded. That’s precisely why it *wasn't* irrational.

If a stock runs from $119 to $203 into an event, and the event — even a good one — fails to deliver the *one thing* the momentum crowd was waiting for, the stock de-rates violently. That’s how markets work. The market wasn’t pricing Q2 fundamentals at $178; it was pricing Q2 **plus** an AI deal announcement at $178. When the deal didn’t come, the market did what it does: it found the clearing price.

You call that a tantrum. I call it price discovery. The difference matters, because price discovery respects **risk**. Tantrums don’t.

And here’s the thing — even your theory admits the stock was overbought, overextended, and owned by the wrong people. If the buying case requires a selloff to reset positioning, then **the selloff isn’t the opportunity. The selloff is the evidence that the prior price was built on sand.**

---

## 2. “Seven quarters of acceleration” is backward-looking — and it’s already cracking.

Your EPS table is real printed history. Q1 2026 EPS was $1.01. Great. And then what happened in Q2 2026? The company told us:

- Search referrals are **“choppy”** — not stabilizing, choppy.
- US DAU — the highest-ARPU market — **decelerated**.
- No new AI licensing deal.

The forward EPS of $9.46 you build your entire valuation on was compiled **before those disclosures.** Those estimates are already stale. If sell-side models get cut by 10–15% over the next 30 days — and they will — your 15.1x forward P/E becomes 17–18x on **lower** earnings. That’s not a bargain. That’s a multiple that was calculated on a guess that already broke.

And your FCF yield — 4.5% “annualized” on a single quarter — is the same extrapolation trap. You annualize a best quarter and treat it as the run-rate. That’s not analysis; that’s hope. Q1 had a 46.9% FCF margin. Q2 had record revenue and materially higher costs. FY2025’s full-year FCF margin was ~31%. If I use **actual trailing FCF**, the FCF yield on market cap is ~2.5%. That’s what a durable cash-compounder trades at when the market’s already convinced it’s a cash machine. Reddit’s market is not convinced — and at 2.5%, it’s not priced like one either.

---

## 3. The Google “partnership” is a dependency wearing a suit.

Here’s your own number, Bull: **$39 million per quarter** in non-ad revenue — roughly 5.9% of revenue. That’s the “toll booth.” Let’s test the toll booth logic:

If the toll booth were worth anything today, why didn’t the market react? Because the market did the math. Even if Reddit **doubles** licensing revenue to $78M/quarter, it’s still less than 12% of total revenue — while the **ad business**, which is 90%+ of revenue, depends on traffic. Traffic depends on search referrals. Referrals are “choppy.” That isn’t a moat. That’s a clearing price with a ribbon on it.

And your legal argument cuts against you. You say the Perplexity lawsuit is a “catalyst” that forces every AI lab to pay up. But legal proceedings take years. Perplexity can countersue. Other AI labs can litigate or delay. Meanwhile, Google’s AI Mode is rolling out **today**, and every answer it renders without a click to Reddit is ad revenue that never gets booked. You’re asking the market to wait for a legal resolution to save a traffic model that’s eroding in real time. That’s not optionality — that’s a latency risk.

The market isn’t stupid. It saw the same quarter and marked Reddit down because **one channel and one revenue line dominated the risk portfolio**. That’s not mispricing. That’s pricing.

---

## 4. The Facebook comparison is historically lazy.

You keep reaching for the Facebook playbook. But Facebook hit US DAU saturation with **1.5 billion global users**, a massive international base, and years of proven ARPU expansion. Reddit has **barely over 100M daily users** and an international ARPU that’s still a fraction of the US.

What you call “the early stages of the monetization engine” is better described as **unproven internationally**. The fact that the US — the highest-ARPU, most proven ad market — is decelerating while the rest of the world remains unproven is a gap, not a runway. And any slowdown in US reach reduces the ad revenue that pays for international expansion. You’re pricing the international story before it’s built. The market is waiting for proof.

---

## 5. The tape does not support your psychology read.

You keep pointing to the close at $143.45, off the $135.22 low. Let me read the full tape, including the part you’re editing out:

- **Open:** $147.70 (gap down 17%)
- **Close:** $143.45 — **below the open**
- **Volume:** 25.08 million shares, the largest print in the dataset
- **Close vs. VWMA:** ~$169 VWMA → closed **15% below the volume-weighted average price**
- **Close position in day’s range:** **lower third**

That is not a capitulation low with buyers in control. Buyers in control reclaim the open. Buyers in control close in the upper third of the range relative to VWMA. This stock closed in the **lower third** of its range on **record volume**, **below the opening print**, and **15% under the average execution price**. That is distribution — plain and simple.

Your asymmetry table is a work of fiction. You compare downside to the March lows (-12% to -17%) and call it limited, while the upside to the 200-day is +25%. That forgets the context: the March lows were **pre-crash lows** in a market that hadn’t yet priced the AI search threat. If referrals keep deteriorating, $119 isn’t the floor — it’s the next waypoint. And the path to $189 requires a re-rating that would only happen if the market suddenly decides the disclosed risks don’t matter. Nothing in the current evidence suggests that’s coming.

---

## 6. Sentiment — your strongest point is actually your weakest.

You say the uniform bearishness means we’re at a “sentiment bottom.” But uniformly bearish **institutional framing** on a **record-volume distribution day** in a **confirmed downtrend** isn’t a contrarian buy signal. It’s a **coherent thesis** — one that the stock’s price action is validating.

The institutions were wrong once — they were long into the print. But they’re not wrong twice. They’ll use the next bounce to exit, not to buy more. Meanwhile the StockTwits crowd — the same one that was long into earnings — is now “buying the dip” on a stock that just collapsed on a beat-and-raise. That’s not conviction. That’s the exact crowd that ate the 20% drop. They are the effect, not the cause, of the trade.

---

## 7. You keep saying the bull needs “one thing to go right.” Let me reframe what “right” means.

A new AI deal? The market already knew the pipeline existed. It wanted progress on the call. One deal will confirm the narrative, not re-rate it.

Referrals stabilizing? That’s a hope, not a control.

A buyback? That offsets dilution; it doesn’t fix traffic risk.

Re-rate to 20x forward? That requires upward earnings revisions, not downward ones. Right now, the direction of revisions is lower.

The bear case, meanwhile, isn’t that “everything goes wrong.” It’s that **one thing — traffic — continues deteriorating**, and the market continues to compress the multiple. That’s not six simultaneous failures. That’s a single channel shift doing what single channels do.

---

## The bottom line, Bull.

Reddit is a good company. If I had to own a high-quality internet asset for five years, it’s on the shortlist. But this isn’t a “which company do I respect most” debate. It’s an investability debate. And the answer at $143, with a broken chart, decelerating US DAU, a CEO warning about the top of the funnel, no new AI licensing deals, a bearish MACD cross at -3.84, a close below all major moving averages, and a record-volume distribution day, is not “buy.”

It’s “sell.” **Sell into the bounce. Don’t catch this knife.**

The data that matters:

- Close: $143.45, **below the open**, closed in the lower third of the day's range
- Below 10 EMA ($172.56), 50 SMA ($175.29), 200 SMA ($180.09)
- MACD: -3.48, fresh deep bearish cross
- RSI: 31.3, approaching oversold — not a reversal signal
- VWMA: $169, price closed 15% below it on 25M shares
- Forward estimates: built before "choppy" search referrals and before the US DAU deceleration was confirmed
- Non-ad revenue: ~$39M/quarter, 5.9% of revenue — not a moat, not a buffer
- TTM P/E: ~33x, EV/EBITDA ~31x — at no point a value stock

Buy it if you believe the market is wrong **and** that management’s own warnings are just theater. But don’t buy it with capital you need to compound.

You said the setup is the only thing that’s real. I agree — and the setup is a breakdown, not an entry.

**Recommendation: SELL RDDT.**

### Manager
**Recommendation**: Overweight

**Rationale**: This was a genuinely high-quality debate with strong arguments on both sides. The Bull Analyst made the more persuasive long-term fundamental case: RDDT delivered a beat-and-raise quarter ($804.9M revenue, +61.1% YoY, raised guidance) and was punished 19% in a single day because a second AI licensing deal wasn't announced on cue. That reads as a positioning-driven capitulation — a crowded trade unwinding — not a structural verdict on the business.

The Bear Analyst's strongest counterarguments — the technical breakdown below all major moving averages, the CEO's "choppy" search referral disclosure, the decelerating US DAU metric, and the risk that forward estimates get cut — are legitimate and cannot be dismissed. The 19% crash on record volume with a close below the open is genuinely concerning price action.

However, the bear case ultimately asks for too much: a structural collapse of Google referrals, permanent failure of the AI licensing pipeline, sharp ad deceleration, and the market ignoring a $2.75B net-cash fortress — all simultaneously. Meanwhile, the bull case only needs one of several catalysts (a new licensing deal, search stabilization, a buyback, or a simple re-rate from 15x to 20x forward earnings) to produce meaningful upside.

The asymmetry at $143 is compelling: ~12-17% downside to March lows vs. ~25-32% upside to the 200-day SMA or a modest 20x forward P/E re-rate. The fundamentals — 61% revenue growth, 91.5% gross margins, 30.8% net margins, 46.9% FCF margin, $2.75B net cash, zero debt — are too strong to justify a Sell rating. But the technical damage and genuine traffic risk warrant measured position sizing rather than an aggressive Buy.

The Bull Analyst wins the debate on the weight of the fundamental evidence, but the Bear Analyst's near-term caution is respected. Overweight is the appropriate rating: constructive, with gradual scaling in.

**Strategic Actions**: 1. **Position sizing**: Initiate or add to the position at roughly 60-75% of a full conviction weight. This reflects the strong fundamental setup but respects the near-term technical damage and traffic risk.

2. **Entry strategy**: Scale in across two to three tranches. First tranche at current levels (~$143-148). Second tranche on any weakness toward the $135 area (the intraday low from the crash day). Reserve a third tranche for a confirmed reclaim of the 10-day EMA (~$172) or 50-day SMA (~$175) — this would signal the downtrend is stabilizing. Do not chase above $155-160 (the lower Bollinger Band / initial resistance) without a fundamental catalyst.

3. **Stop-loss / risk management**: Place a hard stop at $119 (the March pre-crash lows). This represents roughly -17% downside from current levels against +25-32% upside to the 200-day or a 20x forward P/E re-rate — a favorable ~1.5:1 to 2:1 risk/reward ratio.

4. **Catalyst watch**: The position should be actively managed around the following events:
   - Any new AI data-licensing deal announcement (could drive $15-25+ upside in a session)
   - Q3 2026 earnings — the key test of whether "choppy" search referrals translated into revenue impact
   - Any buyback or capital-return announcement (credible given $2.75B net cash)
   - A close above the 200-day SMA (~$180) on above-average volume — a trend-change signal
   - Further legal developments in the Perplexity/SerpApi anti-circumvention case

5. **Sizing guardrails**: Do not exceed a position size where a 20% adverse move (to ~$115) would cause material portfolio damage. The 49% drawdown from highs demonstrates this stock can be volatile even around strong quarters.

## V. Portfolio Manager Decision

Overweight