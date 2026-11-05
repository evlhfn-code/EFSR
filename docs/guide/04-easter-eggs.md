---
tags: [efsr, guide, easter-eggs]
---
# Easter Eggs

Easter Eggs are bought and levelled with **Black Eggs** on the second island of your plot. They reset on Rebirth. There are 22. The full list and formulas are in the [Easter Egg reference](../reference/easter-eggs.md).

## Hatching

Each hatch costs more than the last: 1, 2, 4, 8, 16, 35, 70, 125, 250, 500, 800, 1,200, 1,700, 2,200, 2,750, 3,400, 4,100, 5,000, 6,000, 7,500, 10,000, 12,500. All 22 cost **58,161** Black Eggs. With 500x Black Eggs that's quick. Good Knight is always the first hatch. Re-rolling destroys the egg and its levels.

## Cost types

| Group | Eggs | Cost of the next level from level n |
|---|---|---|
| Constant | Good Knight | 1 |
| "Main 7" (linear) | AFK, Demeaning, Dragon, Eggplant, Faberge, Newton, Wonderland | n + 1 |
| Turtle | Turtle | about n^1.5 |
| "Misc 13" (exponential) | Cactus, Garbage, Hourglass, Idol, King Cobra, Ninja, Present, Radioactive, Scientist, Super, Treasure, Unstable, Volcano | 2^(n+1) |

Every cost is multiplied by **0.95^Water** (the Water Phoenix Egg). The in-game Custom Value box accepts scientific notation (`1e300`) and suffixes.

## What to level

**Before your first Rebirth:** Good Knight (always beats unspent Black Eggs), then Dragon and Demeaning together (manual damage and crits), then Faberge (eggs).

**After Rebirth, with lots of Black Eggs:**

1. Let **Upgrade Best Easter Eggs** do the bulk. Patch #7 reworked it and the devs call it worth using now.
2. Keep the Misc 13 at **the same level**. Their effects all plateau:
   - Idol is maxed near level 1,500 (-8 chickens).
   - Hourglass is maxed near level 1,100 (+30 s).
   - Radioactive is maxed near level 2,900 (+75%).
   - Scientist and King Cobra are maxed near level 18,700.
   - Present is maxed near level 15,000.

   Past those points, extra levels only matter for the ability-duration eggs.
3. Put the rest into the Main 7, Good Knight and Turtle. Their costs grow slowly, so they soak up the bulk of a large Black Egg balance.

## Ability durations

The six +2 s eggs (Unstable, Volcano, Ninja, Treasure, Cactus, Super) decide how long abilities last. At about level 3,585 each, abilities last 2 hours. With a Mythic weapon on Decoy and Hamburger, that's enough to keep every ability Decoyed and active forever (see [Abilities](07-abilities.md)).

Use the [Easter Egg calculator](../../index.html#calc-easter) for exact costs and how many levels you can afford.
