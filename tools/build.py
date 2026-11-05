#!/usr/bin/env python3
"""Build the EFSR Modded Field Guide.

Reads data/*.json and docs/guide/*.md, then writes:
  docs/reference/*.md   reference notes generated from the data
  docs/README.md        vault index (map of content)
  site/artifact.html    page fragment (for the claude.ai Artifact)
  index.html            full standalone page (GitHub Pages / open locally)

Standard library only:  python3 tools/build.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "data/efsr-data.json").read_text(encoding="utf-8"))
CHICKENS = json.loads((ROOT / "data/chickens.json").read_text(encoding="utf-8"))
GUIDE_DIR = ROOT / "docs/guide"
REF_DIR = ROOT / "docs/reference"


def md_table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "|".join("---" for _ in head) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |")
    return "\n".join(out)


def front(tags):
    return "---\ntags: [" + ", ".join(tags) + "]\n---\n"


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def build_reference():
    cost = {"constant": "1", "linear": "n + 1", "turtle": "about n^1.5", "exp": "2^(n+1)"}
    write(REF_DIR / "farmers.md", front(["efsr", "reference"]) + "# Heroes\n\n"
          + DATA["farmersNote"] + "\n\n"
          + md_table(["#", "Hero", "Hire cost", "DPS at Lv 1", "Ability", "Notable upgrades"], DATA["farmers"]))
    write(REF_DIR / "easter-eggs.md", front(["efsr", "reference", "easter-eggs"]) + "# Easter Egg Reference\n\n"
          + "Costs are in Black Eggs, before the Water discount (x 0.95^Water). n is the current level.\n\n"
          + md_table(["Easter Egg", "Effect", "Next level costs"], [[e["name"], e["effect"], cost[e["cost"]]] for e in DATA["easterEggs"]])
          + "\n\n## Hatch and re-roll costs\n\n"
          + md_table(["Hatch #", "Hatch cost", "Re-roll cost"],
                     [[i + 1, f"{c:,}", f"{DATA['rerollCosts'][i]:,}"] for i, c in enumerate(DATA["hatchCosts"])])
          + "\n\nGuide: [Easter Eggs](../guide/04-easter-eggs.md)")
    write(REF_DIR / "phoenix-eggs.md", front(["efsr", "reference", "phoenix-eggs"]) + "# Phoenix Egg Reference\n\n"
          + md_table(["Phoenix Egg", "Effect", "Next level costs"],
                     [[e["name"], e["effect"], "1" if e["cost"] == "constant" else "n + 1"] for e in DATA["phoenixEggs"]])
          + "\n\nGuide: [Phoenix Eggs](../guide/05-phoenix-eggs.md)")
    p = DATA["platinum"]
    write(REF_DIR / "platinum.md", front(["efsr", "reference", "platinum", "modded"]) + "# Platinum Upgrade Reference\n\n"
          + p["unlock"] + "\n\n"
          + md_table(["Upgrade", "Max", "Effect", "Note"],
                     [[u["name"], f"{u['max']:,}" if u["max"] else "none", u["effect"], u.get("note", "")] for u in p["upgrades"]])
          + "\n\n" + p["costNote"] + "\n\nGuide: [Platinum Eggs](../guide/06-platinum-eggs.md)")
    rows = []
    for i, c in enumerate(CHICKENS):
        end = CHICKENS[i + 1][0] - 1 if i + 1 < len(CHICKENS) else 855
        rows.append([f"{c[0]:,} to {end:,}", c[1], c[2] or "-"])
    write(REF_DIR / "chickens.md", front(["efsr", "reference"]) + "# Chickens\n\n"
          + "Chicken types cycle every 855 levels. Minimum boss DPS is the original game's, without boosts.\n\n"
          + md_table(["Levels", "Chicken", "Min. DPS for the boss"], rows))
    t = lambda s: "-" if s is None else (f"{s // 3600} h" if s >= 3600 else f"{s // 60} min" if s >= 60 else f"{s} s")
    write(REF_DIR / "abilities.md", front(["efsr", "reference", "abilities"]) + "# Ability Reference\n\n"
          + md_table(["Key", "Ability", "From", "Effect", "Duration", "Cooldown", "Duration egg"],
                     [[a["key"], a["name"], a["from"], a["effect"], t(a["dur"]), t(a["cd"]), a["egg"]] for a in DATA["abilities"]])
          + "\n\nGuide: [Abilities and Combos](../guide/07-abilities.md)")
    items = md_table(["Rarity", "Weapon cooldown cut", "Wings", "Trail crit"],
                     [[r["name"], f"{r['weaponCd']}%", f"+{r['wingsAps']} attacks/s", "none" if r["trailCrit"] is None else f"+{r['trailCrit']}%"] for r in DATA["rarities"]])
    boxes = md_table(["Box", "Price"] + [r["name"] for r in DATA["rarities"]],
                     [[b["name"], f"{b['price']:,}"] + ([f"{o}%" if o else "-" for o in b["odds"]] if b["odds"] else ["trophies only", "", "", "", "", ""]) for b in DATA["boxes"]])
    dealer = md_table(["Dealer", "Diamonds", "Effect", "Source"], [[d["name"], d["price"], d["effect"], d["src"]] for d in DATA["dealer"]])
    passes = md_table(["Pass", "Effect", "Source"], [[d["name"], d["effect"], d["src"]] for d in DATA["passes"]])
    caps = md_table(["What", "Value", "Notes", "Source"], [[c["what"], c["value"], c["note"], c["src"]] for c in DATA["caps"]])
    write(REF_DIR / "items-and-shop.md", front(["efsr", "reference", "items"]) + "# Items, Shop and Caps\n\n## Item rarities\n\n" + items
          + "\n\n## Boxes\n\n" + boxes + "\n\n## Dealer\n\n" + dealer + "\n\n## Passes and products\n\n" + passes
          + "\n\n## Modded caps\n\n" + caps + "\n\nGuide: [Items, Diamonds and the Dealer](../guide/08-items-and-diamonds.md)")
    log = [front(["efsr", "reference", "modded"]) + "# Update Log\n\nFrom the EFSR [REBORN] Discord, oldest first.\n"]
    for u in DATA["updates"]:
        log.append(f"\n## {u['id']}\n\n" + "\n".join(f"- {i}" for i in u["items"]))
    write(REF_DIR / "update-log.md", "\n".join(log))


def build_index():
    guide = sorted(GUIDE_DIR.glob("*.md"))
    def title(p):
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
        return p.stem
    lines = [front(["efsr", "index"]) + "# EFSR Modded Field Guide",
             "",
             "Calculators and a guide for **Egg Farm Simulator [MODDED]** (the EFSR group's re-creation of SirMing's 2018 game).",
             "Permanent boosts: 250,000x White Eggs, 10x Diamonds, 500x Black Eggs, 25x Gold Eggs.",
             "",
             "The interactive calculator is [index.html](../index.html). These notes are the same guide as plain Markdown, ready for an Obsidian vault.",
             "",
             "## Guide", ""]
    lines += [f"- [{title(p)}](guide/{p.name})" for p in guide]
    lines += ["", "## Reference", ""]
    lines += [f"- [{title(p)}](reference/{p.name})" for p in sorted(REF_DIR.glob("*.md"))]
    lines += ["", "## Sources", "",
              "- EFSR [REBORN] Discord: update logs #2 to #8, the bug-fix update, the hotfix and the community Platinum Egg planner.",
              "- [Egg Farm Simulator RBLX Wiki](https://egg-farm-simulator-rblx.fandom.com/) (original game; CC BY-SA).",
              f"- [Roblox listing]({DATA['game']['url']})."]
    write(ROOT / "docs/README.md", "\n".join(lines))


def build_site():
    notes = {}
    for p in sorted((ROOT / "docs").rglob("*.md")):
        rel = p.relative_to(ROOT / "docs").as_posix()
        if rel.startswith(("guide/", "reference/")):
            notes[rel] = p.read_text(encoding="utf-8")
    js = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tpl = (ROOT / "site/app.template.html").read_text(encoding="utf-8")
    page = (tpl.replace("/*__DATA__*/null", js(DATA))
               .replace("/*__CHICKENS__*/null", js(CHICKENS))
               .replace("/*__NOTES__*/null", js(notes)))
    assert "__DATA__" not in page and "__NOTES__" not in page
    write(ROOT / "site/artifact.html", page)
    head, sep, rest = page.partition("<header")
    full = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
            + head + "</head>\n<body>\n" + sep + rest + "\n</body>\n</html>")
    write(ROOT / "index.html", full)


if __name__ == "__main__":
    build_reference()
    build_index()
    build_site()
    print("built: docs/reference/*.md, docs/README.md, site/artifact.html, index.html")
