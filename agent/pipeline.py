from __future__ import annotations

import json
from pathlib import Path
from typing import Dict

from .formatter import build_shareable_text
from .types import MockProfile, Mode
from scoring.rules import evaluate_profile


class MogclawAgent:
    """OpenClaw-style modular agent: rules first, LLM layer optional."""

    def evaluate(self, profile: MockProfile, mode: Mode = "rate") -> Dict:
        scored = evaluate_profile(profile)
        result = {
            "subject": profile["subject"],
            "psl_score": scored.psl_score,
            "tier": scored.tier,
            "tier_short": _short_tier(scored.tier),
            "mogger": scored.mogger,
            "traits": scored.traits,
            "notes": scored.notes,
            "mode": mode,
        }
        result["shareable_text"] = build_shareable_text(result, mode)
        return result


def _short_tier(tier: str) -> str:
    mapping = {
        "High-Tier Normie": "HTN",
        "Low-Tier Normie": "LTN",
        "Mid Normie": "MN",
        "Subtier": "SUB",
    }
    return mapping.get(tier, tier)


def _load_example_input() -> MockProfile:
    """Load the first mock profile from examples."""
    repo_root = Path(__file__).resolve().parent.parent
    example_path = repo_root / "examples" / "mock_inputs.json"
    with example_path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    return data["profiles"][0]


def main() -> None:
    agent = MogclawAgent()
    profile = _load_example_input()
    for mode in ("roast", "rate", "approve"):
        verdict = agent.evaluate(profile, mode=mode)
        print(json.dumps(verdict, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
