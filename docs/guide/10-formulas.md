---
tags: [efsr, guide, formulas]
---
# Formulas

These are the original game's formulas (wiki), with the modded multipliers and Platinum costs from the Discord. `L` is the farm level and `n` an egg level. `floor(L/500)` is written `k`.

## Black Eggs

Per Mutated boss, before your first Rebirth:

`BE = (10 x Earth² + 1) x ((L - 80)/25)^1.3`

After Rebirth (RP is Rebirth Power as a decimal, so 25% is 0.25):

`BE = (10 x Earth² + 1) x (20 x (1 + RP)^(L/5 - 20) + ((L - 80)/25)^1.3)`

Modded: x500, x(1 + 1% x Abundance), x(1 + 2% x Prosperity x Prestiges), x event boosts.

Plus 1 pending Black Egg per 2,000 Hero levels bought in the run (before boosts).

## Gold Eggs and Rebirth Power

- `lifetime GE = 5 x log10(lifetime BE)`. New Gold Eggs: `5 x log10(new total / old total)`.
- Modded: x25 and x(1 + 1% x Abundance). Where the 25x sits in the formula is unconfirmed.
- `RP% = 25 - 23 x e^(-0.0003 x GE)`. Modded cap 30% (31.2% with upgrades), plateauing after 25%.
- `GE needed for RP = ln(23 / (25 - RP)) / 0.0003`

## Level stats

| Stat | Formula |
|---|---|
| Chicken HP, L ≤ 140 | `10 x (L - 1 + 1.55^(L-1))` |
| Chicken HP, 141 to 500 | `10 x (139 + 2.8583e26 x 1.145^(L-140))` |
| Chicken HP, 501 to 200,000 | `4.2275e48 x Π_{j=1..N} (1.145 + 0.001j)^min(500, L - 500j)` with `N = floor((L-1)/500)` |
| Chicken HP, above 200,000 | `1.24e25409 x 1.545^(L - 200001)` |
| Boss HP multiplier | `max(5, 10 + 0.4k - 5(1 - e^(-0.002 x Cobra)) x (1 + 0.5 x Acid))` |
| Boss timer (s) | `max(2, 30 - 2k + 30(1 - e^(-0.034 x Hourglass)) x (1 + 0.75 x Wind))` |
| Chickens per level | `max(2, 10 + 0.1k - 8(1 - e^(-0.025 x Idol)) x (1 + 0.125 x Sound x (1 + 0.02 x Resonance)))` |
| Mutated chance | `clamp(25 - 2k + 75(1 - e^(-0.013 x Radio)) x (1 + 0.25 x Magnetism), 5, 100)` % |
| Eggception chance | `min(100, 1 x 0.994^k x (1 + 99(1 - e^(-0.002 x Scientist)) x (1 + Electricity)))` % |

How Resonance multiplies Sound is an assumption based on its in-game text ("+2% Sound Egg effectiveness per level").

## Costs

| Thing | Next level from n | Total from a to b |
|---|---|---|
| Main 7 Easter Eggs, Phoenix Eggs (except Fire), Platinum standard | n + 1 | `(b(b+1) - a(a+1)) / 2` |
| Misc 13 Easter Eggs | 2^(n+1) | `2^(b+1) - 2^(a+1)` |
| Turtle | about n^1.5 | sum |
| Good Knight, Fire | 1 | `b - a` |
| Rebirth Boost (Platinum) | 2^n | `2^b - 2^a` |

Easter Egg costs are multiplied by `0.95^Water`.

## Heroes

- Every 25 levels after 175: x4 damage (x5 from 525 to 725). Every 1,000 levels: x10. Master Pai Mei doesn't get these.
- Garbage Egg cuts hire and upgrade costs by `99.99999999 x (1 - e^(-0.01n))` %.
