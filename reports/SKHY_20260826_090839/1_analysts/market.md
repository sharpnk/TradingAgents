# SKHY (SK hynix Inc.) — Technical Indicator Selection & Trend Report
**Analysis date: 2026-08-26 | Exchange: NMS | Sector: Technology / Semiconductors**

---

## 1. Data coverage & discrepancy flags

**Coverage:** The OHLCV feed contains 34 trading rows from 2026-07-10 through 2026-08-26 only. The verified snapshot's recent-closes series confirms the same window. This matters because it caps how much history the averages can "see."

**Discrepancies to flag (per instructions, the verified snapshot is the source of truth):**
- **08-26 close:** raw `get_stock_data` shows **159.32** (vol 3,989,713); the verified snapshot shows **159.53** (vol 3,992,196). Minor intra-source difference; I use 159.53 below.
- **close_200_sma = close_50_sma = 155.27:** both in the indicator output and the verified snapshot. With only ~34 bars of history, the 200 SMA is **not a genuine 200-day average** — it has collapsed onto the 50 SMA. Treat the "long-term trend" layer as unconfirmed/placeholder, not as a validated death/golden-cross benchmark.

---

## 2. Indicator selection (8, non-redundant)

| # | Indicator | Why selected for this market context |
|---|---|---|
| 1 | `close_50_sma` | Medium-term trend spine; price vs. 50 SMA defines the current regime and acts as dynamic support (currently 155.27, rising). |
| 2 | `close_200_sma` | Included for long-term context, but **flagged as degenerate** (equals 50 SMA here) due to insufficient history. |
| 3 | `close_10_ema` | Fast filter (158.35) to time entries against the slower averages and cut noise in a choppy tape. |
| 4 | `macd` | Momentum engine; positive (2.05) and above its signal (1.34) — confirms the recovery off the August low. |
| 5 | `rsi` | Overbought/oversold gauge; at 51.77 it is neutral, i.e., there is room to run without an extreme-stretch warning. |
| 6 | `boll_ub` | Upper band (173.82) marks the immediate resistance/overbought zone where profit-taking appeared (171.38 on 08-17). |
| 7 | `boll_lb` | Lower band (133.15) defines the downside extreme used to frame reversal-risk and stop levels. |
| 8 | `atr` | Elevated at 11.08 (~7% of price) — critical for position sizing and stop placement in this high-volatility name. |

I deliberately **excluded** `macds`/`macdh` (already represented via the verified MACD config), `vwma` (volume series contains outliers and only ~34 rows), and `boll` (inferred from UB/LB spread) to avoid redundancy.

---

## 3. Trend analysis

**Big-picture price path (concrete dates/closes):**
- 2026-07-14: spike close **193.92** (intraday high 194.80) after a 07-13 drop to 152.35 — an extreme volatility episode.
- 2026-07-29: selloff low close **126.79** (session low 124.80).
- 2026-08-10: secondary low close **135.29** — a **higher low** vs. 07-29.
- 2026-08-17: recovery high close **171.38**.
- 2026-08-24: pullback low close **155.37**.
- 2026-08-26: **159.53** (verified).

**Structure:** From the 08-10 low (135.29), the tape has printed a series of higher lows (135.29 → 141.65 → 154.41) and higher highs (165.67 → 166.33 → 171.38), i.e., a **recovery uptrend with sharp two-way swings** rather than a smooth trend. The most recent swing pulled back from 171.38 to 155.37 before Friday's bounce to 159.53.

**Moving-average alignment (current):**
- Price **159.53** > 10 EMA **158.35** > 50 SMA **155.27** → short- and medium-term alignment is **constructive**.
- The 50 SMA has been **rising** (152.55 on 08-11 → 155.27 on 08-26), consistent with a basing/recovery regime.
- 200 SMA = 155.27 (degenerate; see flag) — cannot be used as a true long-term confirmation.

**Momentum (MACD/RSI):**
- MACD crossed from negative (−0.95 on 08-13) to positive (+0.35 on 08-14) and now sits at **2.05**, above the signal (**1.34**), histogram **+0.71** → **bullish momentum configuration**.
- RSI **51.77** (neutral) — recovered from ~33.6 (07-29) but far from overbought, so the rally is not stretched by this gauge.

**Volatility:**
- ATR **11.08**, down from ~19–25 in mid/late July → volatility is **normalizing but still high** (~7% of price).
- Bollinger spread is wide (UB 173.82 / LB 133.15, mid 153.49); the upper band has drifted down (178.7 → 173.8) while the lower band has risen (123.2 → 133.1) — bands are **converging**, consistent with the post-spike compression.

**Volume context:** The spike days carried heavy volume (07-10: ~107.7M; 07-14: ~72.6M), while the last several sessions have seen contraction (08-26: ~3.99M). Declining volume during the current consolidation means the bounce is not yet backed by a clear volume expansion — a caution against overcommitting.

---

## 4. Key levels & actionable insights

**Resistance cluster:**
- **171.4–173.8** — 08-17 close high (171.38) plus Bollinger upper band (173.82). A daily close above ~174 would signal a resumption toward the 07-14 spike area (~194).
- Note: near-term upside from 159.53 to 173.82 is only ~8.2%.

**Support cluster (the buy zone):**
- **158.3** — 10 EMA (immediate).
- **155.3–153.5** — 50 SMA / Bollinger middle (strong confluence), reinforced by the 08-24 pullback low (155.37).
- **133–135** — lower band / 08-10 low; only relevant on a deep retest.

**Actionable framework (given ATR ~11):**
1. **Constructive, not aggressive:** momentum (MACD) and MA alignment favor the long side, but the name remains a high-volatility, two-way tape (proven by ±20% swings in July). Trade size should reflect ATR ≈ 11.
2. **Preferred entry:** accumulation into the **155–158** support zone (10 EMA / 50 SMA / Bollinger mid confluence) rather than chasing at 159.5 mid-band.
3. **Breakout trigger:** a daily close above **~171.4–173.8** with volume expansion opens the path toward the ~194 spike high; otherwise expect continued range work.
4. **Risk management:** with ATR ≈ 11, a stop ~1×ATR below entry (~145–148 if buying 155–158) is a defensible volatility-based placement; invalidation of the recovery thesis is a close back below ~150 and, more decisively, below 135 (08-10 low).
5. **RSI/MACD guardrails:** RSI has room (no overbought warning below 70); watch MACD for a negative histogram cross as the first sign the recovery leg is stalling.

**Overall stance:** **BUY on pullbacks (accumulate into 155–158), hold existing longs, with ATR-based stops.** Not a chase-here setup at mid-band with contracting volume, and not a sell — the trend structure and momentum remain positive while the 50 SMA is rising and price holds above it.

---

## 5. Summary table

| Metric | Value (2026-08-26, verified) | Read |
|---|---|---|
| Close | 159.53 *(raw feed shows 159.32 — flagged)* | Above all key short/medium averages |
| 10 EMA | 158.35 | Price +0.7% above — short-term positive |
| 50 SMA | 155.27 (rising) | Price +2.7% above — medium-term positive |
| 200 SMA | 155.27 **= 50 SMA (degenerate)** | Insufficient history; do not use as long-term signal |
| MACD / Signal / Hist | 2.05 / 1.34 / +0.71 | Bullish momentum configuration |
| RSI | 51.77 | Neutral — no overbought/oversold edge |
| Bollinger Mid / UB / LB | 153.49 / 173.82 / 133.15 | Mid-band price; resistance ~171–174; bands converging |
| ATR | 11.08 (~7% of price) | Elevated but normalizing; size positions and stops accordingly |
| Trend structure | Higher lows since 08-10 (135.29) | Recovery uptrend, choppy |
| Key resistance | 171.38 (08-17) / 173.82 (UB) | Breakout trigger ~174 |
| Key support | 158.3 / 155.3–153.5 / 135.3 | Accumulation zone 155–158; invalidation <135 |
| Volume | Contracting into consolidation (3.99M on 08-26) | Bounce lacks volume confirmation — stay disciplined |

**Bottom line:** SKHY is in a choppy but structurally positive recovery above a rising 50 SMA, with bullish MACD and neutral RSI — yet still inside a wide Bollinger range with elevated ATR. The disciplined play is to **buy dips into 155–158** (or wait for a confirmed close above ~174), manage risk with ~1×ATR stops, and avoid chasing mid-band.

FINAL TRANSACTION PROPOSAL: **BUY**