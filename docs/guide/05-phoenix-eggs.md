---
tags: [efsr, guide, phoenix-eggs]
---
# Phoenix Eggs and Rebirth Power

Phoenix Eggs are bought with **Gold Eggs** at the Phoenix on the last island. They survive Retirement. You can pay 1,000 diamonds when you Rebirth to refund every Gold Egg spent.

| Egg | Effect | Next level costs |
|---|---|---|
| Earth | Black Eggs from Mutated Bosses x (10 x n² + 1) | n + 1 |
| Water | Easter Egg costs x 0.95^n | n + 1 |
| Fire | +100% damage per level | 1 |
| Sound | +12.5% Idol effectiveness per level (about -1 chicken per level) | n + 1 |
| Wind | +75% Hourglass effectiveness (+22.5 s boss timer) | n + 1 |
| Acid | +50% King Cobra effectiveness (-2.5x boss health) | n + 1 |
| Magnetism | +25% Radioactive effectiveness (+18.75% Mutated chance) | n + 1 |
| Electricity | +100% Scientist effectiveness (+100x Eggception chance) | n + 1 |

Each "helper" Phoenix Egg only works if its Easter Egg is at or near its plateau: Sound needs Idol, Wind needs Hourglass, Acid needs King Cobra, Magnetism needs Radioactive, and Electricity needs Scientist.

## Gold Eggs

You earn **5 Gold Eggs for every 10x more lifetime Black Eggs** you have claimed:

`lifetime Gold Eggs = 5 x log10(lifetime Black Eggs)`

The modded game multiplies Gold Eggs by **25x** and Abundance adds +1% per level. How exactly the 25x applies inside that formula isn't confirmed. The calculator applies it to the result. Pending Gold Eggs are claimed by Rebirthing (beat level 300).

## Rebirth Power

Rebirth Power multiplies the Black Eggs a Mutated boss drops by (1 + RP) for every 5 levels past 100:

`Black Eggs per boss = (10 x Earth² + 1) x (20 x (1 + RP)^(level/5 - 20) + ((level - 80)/25)^1.3) x boosts`

Original formula: `RP = 25 - 23 x e^(-0.0003 x lifetime Gold Eggs)` percent, capped at 25%. The modded cap is 30% (growth plateaus after 25%), and 31.2% with every upgrade. Past 25%, read your Rebirth Power from the Phoenix in game and enter it in the calculator.

## How to spend

1. **Earth and Water together.** The wiki's efficiency score is Earth² / 0.95^Water, so the best split for any budget keeps both rising. The [Phoenix calculator](../../index.html#calc-phoenix) finds the best split for a budget. Earth stops mattering once Rebirth Power takes over. The wiki suggests stopping around level 32, and well under 100 even late.
2. **Fire** for damage. 10 levels is about 10x, 100 levels about 100x.
3. **Sound**, once Idol is near its plateau. Fewer chickens per level is the main speed lever late game.
4. **Magnetism, Wind and Acid** as you go deep enough that the mutation chance, boss timer or boss health start failing. The calculator shows where each one runs out.
5. **Electricity** for Eggceptions (big White Egg spikes with Fertilizer and Newton).
