#!/usr/bin/env python3
"""
Run TradingAgents Deep analysis bypassing the TUI entirely.
Uses the correct config keys and saves reports to disk.
"""
import sys, os, time
from pathlib import Path

TICKER = sys.argv[1].upper() if len(sys.argv) > 1 else "SPY"

os.chdir("/Users/ll/src/TradingAgents")
sys.path.insert(0, "/Users/ll/src/TradingAgents")

os.environ["TRADINGAGENTS_LLM_PROVIDER"] = "deepseek"
os.environ["TRADINGAGENTS_DEEP_THINK_LLM"] = "deepseek-v4-pro"
os.environ["TRADINGAGENTS_QUICK_THINK_LLM"] = "deepseek-v4-flash"
os.environ["TRADINGAGENTS_OUTPUT_LANGUAGE"] = "English"

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(usecwd=True))

from tradingagents.default_config import DEFAULT_CONFIG
from tradingagents.graph.trading_graph import TradingAgentsGraph

# Deep research = 5 rounds
config = DEFAULT_CONFIG.copy()
config["max_debate_rounds"] = 5
config["max_risk_discuss_rounds"] = 5

ta = TradingAgentsGraph(config=config)

TIMESTAMP = time.strftime("%Y%m%d_%H%M%S")
SAVE_PATH = Path(f"/Users/ll/src/TradingAgents/reports/{TICKER}_{TIMESTAMP}")

print(f"=== Starting {TICKER} Deep Analysis ({TIMESTAMP}) ===", flush=True)

import traceback
try:
    state, decision = ta.propagate(TICKER, "2026-07-06")
    print(f"\nSUCCESS! {TICKER} Decision: {decision}", flush=True)

    # Save report to disk (same structure as CLI save_report_to_disk)
    SAVE_PATH.mkdir(parents=True, exist_ok=True)
    sections = []

    # 1. Analysts
    analysts_dir = SAVE_PATH / "1_analysts"
    analyst_parts = []
    for key, filename in [("market_report", "market.md"), ("sentiment_report", "sentiment.md"),
                           ("news_report", "news.md"), ("fundamentals_report", "fundamentals.md")]:
        if state.get(key):
            analysts_dir.mkdir(exist_ok=True)
            (analysts_dir / filename).write_text(state[key], encoding="utf-8")
            analyst_parts.append((filename.replace(".md", "").title(), state[key]))
    if analyst_parts:
        content = "\n\n".join(f"### {name}\n{text}" for name, text in analyst_parts)
        sections.append(f"## I. Analyst Team Reports\n\n{content}")

    # 2. Research
    if state.get("investment_debate_state"):
        research_dir = SAVE_PATH / "2_research"
        debate = state["investment_debate_state"]
        research_parts = []
        for key, filename in [("bull_history", "bull.md"), ("bear_history", "bear.md"),
                               ("judge_decision", "manager.md")]:
            if debate.get(key):
                research_dir.mkdir(exist_ok=True)
                (research_dir / filename).write_text(debate[key], encoding="utf-8")
                research_parts.append((filename.replace(".md", "").title(), debate[key]))
        if research_parts:
            content = "\n\n".join(f"### {name}\n{text}" for name, text in research_parts)
            sections.append(f"## II. Research Team Decision\n\n{content}")

    # 3. Trading
    if state.get("trading_plan"):
        trading_dir = SAVE_PATH / "3_trading"
        trading_dir.mkdir(exist_ok=True)
        (trading_dir / "trader.md").write_text(state["trading_plan"], encoding="utf-8")
        sections.append(f"## III. Trading Plan\n\n{state['trading_plan']}")

    # 4. Risk
    if state.get("risk_discussion_state"):
        risk_dir = SAVE_PATH / "4_risk"
        risk = state["risk_discussion_state"]
        risk_parts = []
        for key, filename in [("aggressive_risk", "aggressive.md"), ("neutral_risk", "neutral.md"),
                               ("conservative_risk", "conservative.md")]:
            if risk.get(key):
                risk_dir.mkdir(exist_ok=True)
                (risk_dir / filename).write_text(risk[key], encoding="utf-8")
                risk_parts.append((filename.replace(".md", "").title(), risk[key]))
        if risk_parts:
            content = "\n\n".join(f"### {name}\n{text}" for name, text in risk_parts)
            sections.append(f"## IV. Risk Management Team\n\n{content}")

    # 5. Portfolio Manager (decision)
    if decision:
        portfolio_dir = SAVE_PATH / "5_portfolio"
        portfolio_dir.mkdir(exist_ok=True)
        (portfolio_dir / "decision.md").write_text(decision, encoding="utf-8")
        sections.append(f"## V. Portfolio Manager Decision\n\n{decision}")

    # Write consolidated report
    complete = "# TradingAgents Investment Report\n\n"
    complete += f"**Ticker:** {TICKER}\n"
    complete += f"**Date:** 2026-07-06\n"
    complete += f"**Depth:** Deep\n\n"
    complete += "\n\n".join(sections)
    (SAVE_PATH / "complete_report.md").write_text(complete, encoding="utf-8")

    print(f"\n✓ Report saved to: {SAVE_PATH}", flush=True)
    print(f"  Complete report: complete_report.md", flush=True)

except Exception as e:
    traceback.print_exc()
    sys.exit(1)
