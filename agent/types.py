from dataclasses import dataclass
from typing import Dict, Literal, TypedDict


Tier = Literal[
    "Chad",
    "Chadlite",
    "High-Tier Normie",
    "Mid Normie",
    "Low-Tier Normie",
    "Subtier",
]

Mode = Literal["roast", "rate", "approve"]


class SignalSet(TypedDict):
    symmetry: float
    jawline: float
    eye_area: float
    ratio_harmony: float
    presentation: float


class MockProfile(TypedDict):
    subject: str
    self_description: str
    signals: SignalSet


@dataclass
class ScoreBreakdown:
    psl_score: float
    tier: Tier
    mogger: bool
    traits: Dict[str, float]
    notes: str
