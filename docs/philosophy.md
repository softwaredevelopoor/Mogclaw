# Mogclaw Philosophy

Mogclaw is a satirical agent that mirrors an internet dialect (looksmax / trench meme culture) without claiming to produce objective truth about appearance.

## Why it exists
- Prototype a culturally-aligned agent, not a real evaluation tool.
- Clearly separate `scoring`, `prompts`, `output formatting`.
- Enable style iterations without touching core rules.

## Design principles
- **Short verdicts**: readable and shareable outputs.
- **Modular logic**: deterministic rules + future LLM layer extension.
- **Safe satire**: no targeting real individuals, no calls to harassment.
- **No pseudo-science**: no medical/biometric claims.

## Onchain-ready direction
Architecture designed to plug in:
- verdict event emitters,
- signed attestations,
- community reputation hooks.

These elements are not active in this bootstrap version.
