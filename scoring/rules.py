from __future__ import annotations

from typing import Dict

from agent.types import MockProfile, ScoreBreakdown, Tier

WEIGHTS = {
    "symmetry": 0.22,
    "jawline": 0.24,
    "eye_area": 0.20,
    "ratio_harmony": 0.18,
    "presentation": 0.16,
}


def evaluate_profile(profile: MockProfile) -> ScoreBreakdown:
    signals = profile["signals"]
    weighted_score = sum(signals[key] * WEIGHTS[key] for key in WEIGHTS)
    psl_score = _clamp(weighted_score, 0.0, 10.0)

    tier = _tier_from_score(psl_score)
    mogger = psl_score >= 6.0
    notes = _build_notes(signals, tier)

    return ScoreBreakdown(
        psl_score=round(psl_score, 2),
        tier=tier,
        mogger=mogger,
        traits={k: round(v, 2) for k, v in signals.items()},
        notes=notes,
    )


def _tier_from_score(score: float) -> Tier:
    if score >= 9.0:
        return "Chad"
    if score >= 7.5:
        return "Chadlite"
    if score >= 6.0:
        return "High-Tier Normie"
    if score >= 4.5:
        return "Mid Normie"
    if score >= 3.0:
        return "Low-Tier Normie"
    return "Subtier"


def _build_notes(signals: Dict[str, float], tier: Tier) -> str:
    weak = min(signals, key=signals.get)
    strong = max(signals, key=signals.get)
    weak_label = weak.replace("_", " ")
    strong_label = strong.replace("_", " ")

    if tier == "Chad":
        return f"apex frame, {strong_label} carrying"
    if tier == "Chadlite":
        return f"high ceiling, polish {weak_label}"
    if tier == "High-Tier Normie":
        return f"HTN mogging, slight {weak_label} gap"
    if tier == "Mid Normie":
        return f"mid-pack, boost {weak_label}"
    if tier == "Low-Tier Normie":
        return f"LTN lane, {weak_label} holding back"
    return f"rebuild arc, start with {weak_label}"


def _clamp(value: float, min_v: float, max_v: float) -> float:
    return max(min_v, min(value, max_v))
