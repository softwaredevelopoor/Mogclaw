# Mogclaw

Mogclaw = first **OpenClaw** agent focused on PSL / looksmax meme culture.

Short version: submit a mock profile, agent outputs a sharp, ironic, shareable verdict.

**No medicine. No real biometrics. No IRL harassment.**

---

## Core concept

Mogclaw classifies (satirically) based on:

- PSL score (fictional)
- Mogger vs non-mogger
- Tier: Chad / High-Tier Normie (HTN) / Low-Tier Normie (LTN)
- Conceptual visual signals (perceived symmetry, jawline, eye area, ratios *meme-level*)
- Trench archetypes + internet slang

Style de sortie:

- court
- sharp
- ironique
- meme-native

Exemples:

- "HTN mogging, slight eye asymmetry"
- "LTN, no jaw, over"
- "Chadlite potential, needs cut"

---

## PSL tiers (meme rubric)

> Satirical in-project rubric. This is **not** a scientific system.

- **9.0 - 10.0** → `Chad`
- **7.5 - 8.9** → `Chadlite`
- **6.0 - 7.4** → `High-Tier Normie (HTN)`
- **4.5 - 5.9** → `Mid Normie`
- **3.0 - 4.4** → `Low-Tier Normie (LTN)`
- **0.0 - 2.9** → `Subtier / Recovery Arc`

---

## Repo structure

```
.
├── agent/            # Pipeline OpenClaw-like: input -> scoring -> verdict text
├── prompts/          # Modes de jugement + prompt système
├── scoring/          # Logique PSL, règles de classification, pondérations
├── examples/         # Mock inputs / outputs pour démo
├── docs/             # Philosophie, garde-fous, disclaimers
├── LICENSE           # MIT
└── README.md
```

---

## Quickstart

### 1) Run local demo

```bash
python -m agent.pipeline
```

### 2) Use in your own script

```python
from agent.pipeline import MogclawAgent

agent = MogclawAgent()
verdict = agent.evaluate(
	{
		"subject": "mock_user_01",
		"self_description": "gym 3x/week, weak jaw angle, decent eye area",
		"signals": {
			"symmetry": 6.2,
			"jawline": 4.8,
			"eye_area": 6.8,
			"ratio_harmony": 5.9,
			"presentation": 6.5,
		},
	},
	mode="roast"
)
print(verdict["shareable_text"])
```

---

## Safety / satire disclaimer

Mogclaw is a **satirical cultural mirror** of looksmax + trench meme culture.

- Do not use to target real individuals.
- Do not use to harass, discriminate, or humiliate.
- Do not interpret scores as medical/biometric facts.
- Outputs = memetic fiction + style classification.

If deploying publicly, add a moderation filter and anti-abuse guardrails.

---

## Future hooks

- Onchain-ready event hooks (stub)
- LLM judgment layer pluggable into fixed rules
- Auto export to X posts (shareable text)

---

## License

MIT — voir `LICENSE`.