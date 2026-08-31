All data gathered. I now have the verified snapshot (source of truth), full price history, and eight indicators. Let me compile the detailed report.

---

## APP (AppLovin Corporation) — Technical Analysis Report
**Analysis date: 2026-08-17 (latest completed trading row used: 2026-08-14 close)**
**Sector: Communication Services / Advertising Agencies — Exchange: NMS**

> ⚠️ **Data note:** The requested date 2026-08-17 (Monday) has no completed OHLC row — the raw feed shows only a volume placeholder and all indicators return N/A for 08-15 through 08-17. The **verified snapshot confirms 2026-08-14 as the latest trading row**. All exact figures below use that verified row as the source of truth; the standalone `get_stock_data` CSV agrees with it (close 315.44 on 08-14), so no reconciliation conflict exists.

---

### 1. Selected Indicators (8) and Why They Were Chosen

Given the market condition — a high-beta growth name in a **violent downtrend with a recent capitulation gap** — I selected a non-redundant mix covering trend, momentum, volatility, and volume:

| # | Indicator | Category | Why selected for this setup |
|---|---|---|---|
| 1 | `close_10_ema` | Moving Average | Fastest trend gauge; detects whether the post-crash bounce (303.76 → 315.44) can reclaim short-term momentum. Current value: **343.29** |
| 2 | `close_50_sma` | Moving Average | Medium-term trend + dynamic resistance. Price is ~30% below it, quantifying the severity of the breakdown. Current: **450.23** |
| 3 | `close_200_sma` | Moving Average | Long-term benchmark; confirms the strategic trend has rolled over. Current: **508.19** — price far below, a deeply bearish regime |
| 4 | `macd` | MACD | Core momentum engine; reads trend *velocity*. Currently **-39.65**, below signal **-33.44**, histogram **-6.21** — momentum is still accelerating down, not decelerating |
| 5 | `rsi` | Momentum | Flags capitulation/oversold. At **30.42**, right at the 30 line — near-oversold but not yet a confirmed reversal trigger |
| 6 | `boll_ub` | Volatility | Upper band (**467.61**) quantifies how far price has fallen relative to the 20-day mean (**380.12**); defines the "dead zone" a recovery must traverse |
| 7 | `atr` | Volatility | Risk management input. At **24.30** (~7.7% of price), it demands wide stops/small position sizes in this tape |
| 8 | `vwma` | Volume | Volume-weighted trend confirmation. At **366.34**, it sits above price — evidence the recent selling was absorbed on heavy volume and distribution dominates |

*(I deliberately skipped the redundant 200-day twins, MACD signal/histogram as separate picks, and the Bollinger middle/lower bands as primary picks since `boll_ub` + the verified `boll_lb`/`boll` values in the snapshot already cover the band structure.)*

---

### 2. Trend Narrative (all figures tool-supported)

**Long-term structure — broken.** APP rallied from ~$438 (Aug 2025) to a closing peak of **$733.60 on 2025-12-22**, then began a multi-month descent. By mid-2026 the stock had already fallen ~47% from that peak to **$391.98 on 2026-07-24**. The 200-day SMA at **508.19** versus price at **315.44** (a ~38% discount) confirms a fully bearish long-term regime — there is no golden-cross support left underneath.

**The August 2026 crash — a second leg down.** After a relief rally to **$419.70 (2026-08-04)** and **$417.80 (2026-08-05)**, the stock gapped and collapsed to **$335.67 on 2026-08-06** — a **-19.7% single-session drop** on volume of ~15.2M shares (roughly 2–3× normal). Selling continued to **$303.76 on 2026-08-12** (a cumulative **-27.6% from the 08-04 close** and **-58.6% from the December peak**). The decline since 08-05 has been relentless: every rally attempt (346.80 on 08-07, 339.00 on 08-10) has been sold.

**Short-term — tentative stabilization, no confirmation.** The last three sessions show a modest base: 303.76 → 312.67 → **315.44** (verified 08-14 close). RSI has ticked up from **26.60 (08-12)** to **30.42 (08-14)**, and price is holding ~7.8% above the lower Bollinger band (**292.63**). That is consistent with *exhaustion of the immediate downleg*, not a reversal.

**Momentum verdict — still bearish.** MACD at **-39.65** with a **-6.21** histogram means downside momentum is *still expanding*; the bounce so far is a drift, not a momentum turn. The 10-day EMA (**343.29**) and VWMA (**366.34**) are both overhead — the market has not reclaimed a single short-term average.

---

### 3. Key Levels & Actionable Insights

- **Immediate support:** Bollinger lower band **292.63**, then the round **300** zone (03-30 low was 372 — not relevant here; the 08-12 low of **303.76** is the operative pivot). A close below ~303 would likely reopen the downside toward the band and below.
- **First resistance:** 10-day EMA **343.29** (needs a close above to signal the bounce has legs).
- **Second resistance:** VWMA **366.34**, then the 20-day mean/Bollinger middle **380.12**.
- **Major resistance / trend-invalidation zone:** 50-day SMA **450.23** and 200-day SMA **508.19** — an enormous overhead supply stack; even an aggressive rally would face sellers there.
- **Risk metric:** ATR of **24.30** implies a 2×ATR stop ≈ **$48.6** (~15%). Position sizes must be cut accordingly; wide stops are the only way to survive this volatility, which cuts the reward-to-risk appeal of short-term trades.

**Actionable plays (for traders):**
1. **Trend-followers / new longs: stay out.** The setup (price < 10 EMA < 50 SMA < 200 SMA, negative and *widening* MACD, VWMA above price) has no bullish edge. Buying "cheap" here is catching a falling knife until at least the 10 EMA is reclaimed on a closing basis.
2. **Existing longs / swing traders:** treat any rally into **343–380** as a reduction/exit zone unless volume expands and MACD histogram turns positive (a cross back above signal). Hard invalidation for a bounce thesis: a daily close below **303.76**.
3. **Short-term counter-trend (aggressive only):** RSI at 30.42 + price above the lower band + capitulation volume on 08-06/08-12 supports a *scalable* bounce toward 343–366 — but this is a tactical trade against the primary trend, sized small, with the 303 pivot as the stop.
4. **Swing shorts:** the 343–366 zone offers a lower-risk entry to re-short with a stop above **380** (Bollinger middle); MACD structure supports continuation unless it rolls positive.

**Bottom line:** The trend, momentum, volume, and volatility indicators are unanimously bearish. The only bullish ingredients present are *mean-reversion* (RSI near 30) and *exhaustion* (lower-band proximity after a capitulation). Those favor a possible technical bounce, not a trend change. Primary stance: **risk-off / SELL** until the 10 EMA and VWMA are reclaimed; treat any strength as a sell/exit opportunity into 343–380.

---

### 4. Summary Table

| Factor | Verified Value (08-14) | Signal | Implication |
|---|---|---|---|
| Last close | $315.44 | — | Below every tracked average — bearish |
| 10-day EMA | $343.29 | Bearish | Immediate overhead resistance; first reclaim target |
| 50-day SMA | $450.23 | Bearish | Medium-term trend down; ~30% overhead |
| 200-day SMA | $508.19 | Bearish | Long-term regime broken; no support below |
| MACD / Signal / Hist | -39.65 / -33.44 / -6.21 | Bearish | Downside momentum still expanding |
| RSI (14) | 30.42 | Neutral-bullish | Near-oversold; improving from 26.6 (08-12) — exhaustion, not confirmation |
| Bollinger Upper / Middle / Lower | 467.61 / 380.12 / 292.63 | Bearish | Price in lower band zone; 292–304 is the last demand shelf |
| ATR (14) | 24.30 | High risk | ~7.7% of price; require wide stops / small size |
| VWMA | $366.34 | Bearish | Volume-weighted flow still favors sellers |
| Price action (08-04 → 08-12) | 419.70 → 303.76 (-27.6%) | Bearish | Second-leg crash; 08-12 low = 303.76 pivot |
| Recent 3-session close | 303.76 → 312.67 → 315.44 | Neutral | Tentative base forming; no breakout yet |

**Overall assessment:** SELL / risk-off for new capital; any bounce to 343–380 should be treated as distribution. A daily close above the 10 EMA (343) improves the near-term picture to "stabilizing"; only a reclaim of the 50 SMA (~450) would shift the medium-term structure back to neutral.

---

FINAL TRANSACTION PROPOSAL: **SELL**