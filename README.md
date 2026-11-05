# EFSR Modded Field Guide

Calculators and a guide for **Egg Farm Simulator [MODDED]**, the EFSR group's re-creation of SirMing's 2018 Egg Farm Simulator. Its permanent boosts are **250,000x White Eggs, 10x Diamonds, 500x Black Eggs and 25x Gold Eggs**.

Open [`index.html`](index.html) in a browser. It's one self-contained page that works offline, apart from fonts and the Markdown renderer, and also works on GitHub Pages.

## What's in it

**Calculators**

| Calculator | What it answers |
|---|---|
| Black Eggs per Run | What a Retire at level X is worth, with Mutated chance, Earth, Rebirth Power, the 500x boost and Platinum bonuses |
| Gold Eggs & Rebirth Power | Gold Eggs from a Retire (5 per 10x lifetime Black Eggs, x25), and Gold Eggs needed for each Rebirth Power step |
| Platinum Planner | The community's Platinum Egg split. It reproduces the 200K example exactly. |
| Easter Eggs | Cost from level A to B, highest affordable level, effect at a level, Misc 13 even split, hatch costs |
| Phoenix Eggs | Gold Egg costs and the best Earth / Water split for a budget |
| Level Stats | Chicken and boss health, boss timer, DPS needed, chickens per level, Mutated and Eggception chance, and where each egg runs out |
| Hero Levels | Damage multiplier from levels (x4 every 25, x10 every 1,000) |
| Diamonds & Abilities | Rain income at 10x, Auto-Egg prices, box odds, ability cooldowns and uptime |
| Number Converter | Game suffixes (K to D) to and from scientific notation |

All the maths runs in log space, so numbers like `1e5,820` work.

**Guide.** Eleven notes in [`docs/guide`](docs/guide):
- Start here
- What's different in Modded
- Progression by stage
- Easter Eggs
- Phoenix Eggs
- Platinum Eggs
- Abilities
- Items and diamonds
- Bosses and events
- Formulas
- Open questions

**Reference.** Notes in [`docs/reference`](docs/reference) generated from the data: Heroes, Easter, Phoenix and Platinum eggs, abilities, items, chickens and the update log.

## Obsidian

[`docs/`](docs/README.md) is a ready Obsidian vault folder. It uses plain relative links, so it reads the same in Obsidian and on GitHub. To sync it into your vault, pull the repo on your PC and run `/obsidian-sync` there.

## Editing

- Game data: [`data/efsr-data.json`](data/efsr-data.json). Modded multipliers, caps, Platinum upgrades, eggs, Heroes, items and the update log live here.
- Guide text: [`docs/guide/*.md`](docs/guide).
- Page: [`site/app.template.html`](site/app.template.html). This holds the styles, calculators and layout.

Then rebuild (standard library only):

```sh
python3 tools/build.py
```

This regenerates `docs/reference/*.md`, `docs/README.md`, `index.html` and `site/artifact.html`.

## Sources

- **EFSR [REBORN] Discord:** update logs #2 to #8, the bug-fix update, the hotfix and the community Platinum Egg planner. Modded values come from here and override everything else.
- **[Egg Farm Simulator RBLX Wiki](https://egg-farm-simulator-rblx.fandom.com/):** base-game formulas, Heroes, eggs and items from the original game, licensed CC BY-SA.
- **[Roblox listing](https://www.roblox.com/games/70588073988808/Egg-Farm-Simulator).**

Anything not yet confirmed for the modded game is listed in [Open Questions](docs/guide/11-open-questions.md) and labelled in the calculators. This is a fan project and isn't affiliated with the game's developers.
