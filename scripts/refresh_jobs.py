#!/usr/bin/env python3
"""Publish a small, source-attributed Adzuna Canada contract feed for GitHub Pages."""
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

OUT = Path("opportunities/data/jobs.json")
TERMS = ["cyber security", "information security", "GRC", "IT risk", "cloud security", "security architect", "IT project manager"]
CONTRACT = re.compile(r"\b(contract|contractor|freelanc|temporary|fixed.term|consultant)\b", re.I)

def fetch(term):
    params = urlencode({
        "app_id": os.environ["ADZUNA_APP_ID"],
        "app_key": os.environ["ADZUNA_APP_KEY"],
        "results_per_page": 50,
        "what": term,
        "where": "Canada",
        "max_days_old": 21,
        "content-type": "application/json",
    })
    url = "https://api.adzuna.com/v1/api/jobs/ca/search/1?" + params
    with urlopen(Request(url, headers={"User-Agent": "QUN-Consulting-Opportunities/1.0"}), timeout=25) as response:
        return json.load(response).get("results", [])

def main():
    if not os.getenv("ADZUNA_APP_ID") or not os.getenv("ADZUNA_APP_KEY"):
        raise SystemExit("Set ADZUNA_APP_ID and ADZUNA_APP_KEY as GitHub Actions secrets.")
    found = {}
    errors = []
    for term in TERMS:
        try:
            results = fetch(term)
        except Exception as exc:
            errors.append(f"{term}: {type(exc).__name__}")
            continue
        for item in results:
            title = item.get("title") or ""
            desc = re.sub("<[^>]+>", " ", item.get("description") or "")
            typ = item.get("contract_type") or ""
            text = " ".join([title, desc, typ])
            if not (CONTRACT.search(text) or item.get("contract_time") == "part_time"):
                continue
            url = item.get("redirect_url")
            if not url or not url.startswith("https://"):
                continue
            ident = str(item.get("id") or url)
            found[ident] = {
                "id": ident,
                "title": title[:180],
                "company": (item.get("company") or {}).get("display_name", "Not specified")[:120],
                "location": (item.get("location") or {}).get("display_name", "Canada")[:140],
                "description": desc[:360],
                "date": item.get("created", ""),
                "url": url,
                "source": "Adzuna",
                "contract": True,
            }
    if errors and not found:
        raise SystemExit("All searches failed; preserving existing feed. " + ", ".join(errors))
    if not found:
        print("No matching contracts; preserving existing feed to avoid accidental empty publication.")
        return
    rows = sorted(found.values(), key=lambda x: x["date"], reverse=True)[:200]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"updated_at": datetime.now(timezone.utc).isoformat(), "source": "Adzuna Canada", "jobs": rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Prepared {len(rows)} published listings; {len(errors)} term searches failed.")

if __name__ == "__main__":
    main()
