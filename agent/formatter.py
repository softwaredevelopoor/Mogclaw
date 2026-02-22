from typing import Dict

from .types import Mode


MODE_VOICES = {
    "roast": {
        "prefix": "verdict:",
        "ending": "over.",
    },
    "rate": {
        "prefix": "tier check:",
        "ending": "locked.",
    },
    "approve": {
        "prefix": "approval lane:",
        "ending": "move.",
    },
}


def build_shareable_text(result: Dict, mode: Mode) -> str:
    voice = MODE_VOICES.get(mode, MODE_VOICES["rate"])
    tier = result["tier_short"]
    psl = result["psl_score"]
    signal_note = result["notes"]
    mogger_flag = "mogger" if result["mogger"] else "non-mogger"
    return (
        f"{voice['prefix']} {tier} | PSL {psl:.1f} | {mogger_flag} | "
        f"{signal_note} {voice['ending']}"
    )
