---
tags: [efsr, guide, platinum, modded]
---
# Platinum Eggs and Ascension

Platinum Eggs are the modded game's third reset layer (update #3). You **Ascend** at farm level **300,000** (patch #7). Pending Gold Eggs count toward Platinum Eggs, and pending Platinum Eggs show in the egg bar (update #8). Ascension gives your pending Gold Eggs before it resets you (patch #6).

## Upgrades

| Upgrade | Max | Effect |
|---|---|---|
| Rebirth Cap Increase | 550 (see note) | Raises the rebirth cap, helping unlock higher Black Egg earnings. |
| Rebirth Boost | 10 | Improves rebirth progression. |
| Level Skip | 40 | Skips farm levels to speed up progression. |
| Abundance | none | +1% Eggs, Black Eggs and Gold Eggs per level. |
| Prosperity | none | +2% Black Eggs per Prestige per level. |
| Resonance | none | +2% Sound Egg effectiveness per level. |

The upgrade menu shows Rebirth Cap Increase at **MAX LEVEL 550**, but update #8 says "Rebirth Cap Increase egg is uncapped". Check which one is true in game.

## Costs

These match every observed example, but they aren't confirmed game code.

- **Standard upgrades:** buying n levels from current level L costs `n x (2L + n + 1) / 2`. Level 1 costs 1, level 2 costs 2, and so on.
- **Rebirth Boost:** costs double each level. From L to L + n costs `2^(L+n) - 2^L`. All 10 levels cost 1,023.

## The community method

This is the community planner's distribution, not a proven optimum:

1. **Balanced start.** From 1K to 100K Platinum Eggs invested, favour Rebirth Cap Increase and Abundance, unlock Rebirth Boost early, and build Level Skip steadily.
2. **Level Skip before Prosperity.** Level Skip reaches 40 near 20K total invested.
3. **Prosperity stays low.** It gets at most 1% of the Abundance plus Prosperity budget, because players report its bonus may not compound. Resonance keeps a calibrated share. Levels you already own are kept.

Worked example: **200,000 Platinum Eggs** from zero.

| Upgrade | Levels | Cost |
|---|---|---|
| Rebirth Cap Increase | 0 → 448 | 100,576 |
| Rebirth Boost | 0 → 10 | 1,023 |
| Level Skip | 0 → 40 | 820 |
| Abundance | 0 → 401 | 80,601 |
| Prosperity | 0 → 39 | 780 |
| Resonance | 0 → 178 | 15,931 |
| **Spent** | | **199,731** (269 left) |

The [Platinum planner](../../index.html#calc-platinum) reproduces this exactly. It also takes your current levels and lets you change the weights.
