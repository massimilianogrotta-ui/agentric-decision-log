#!/usr/bin/env python3
"""
Record a decision in the agentric-decision-log repository.
Usage: python3 record_decision.py --title "Titolo" --context "Contesto" --decision "Decisione" [--agents "hermes,max"]
"""
import os, sys, argparse
from datetime import date
from pathlib import Path

REPO = Path(__file__).parent

def next_id():
    existing = list(REPO.glob("decisioni/*/*/*.md"))
    if not existing:
        return 1
    ids = []
    for f in existing:
        try:
            ids.append(int(f.stem.split("_")[1]))
        except (IndexError, ValueError):
            continue
    return max(ids) + 1 if ids else 1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--context", required=True)
    parser.add_argument("--decision", required=True)
    parser.add_argument("--agents", default="hermes,max")
    parser.add_argument("--type", default="decision", choices=["decision", "post-mortem", "procedure"])
    args = parser.parse_args()

    today = date.today()
    nid = f"{next_id():03d}"
    slug = args.title.lower().replace(" ", "-")[:40]
    fname = f"decisioni/{today.year}/{today.month:02d}/{today}-{nid}-{slug}.md"
    fpath = REPO / fname
    fpath.parent.mkdir(parents=True, exist_ok=True)

    agents = [a.strip() for a in args.agents.split(",")]
    content = f"""---
id: {nid}
type: {args.type}
date: {today}
status: accepted
agenti: [{', '.join(agents)}]
---

# {args.title}

## Decisione
{args.decision}

## Contesto
{args.context}

"""
    fpath.write_text(content)
    
    os.chdir(str(REPO))
    os.system(f"git add -A && git commit -m 'decision: {args.title}' && git push")
    
    print(f"✅ Decisione registrata: {fname}")

if __name__ == "__main__":
    main()
