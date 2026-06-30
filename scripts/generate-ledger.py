#!/usr/bin/env python3
"""generate-ledger — auto-spis węzłów dialektycznych do docs/INDEX.md.

Skanuje docs/**/*.md, czyta frontmatter (type/id/title/status/parents) i wstawia
posortowaną tabelę między znaczniki `<!-- LEDGER:START ... -->` / `<!-- LEDGER:END -->`
w docs/INDEX.md. Bez zależności zewnętrznych (sam stdlib).

Użycie:
  python3 scripts/generate-ledger.py          # przepisz INDEX.md w miejscu
  python3 scripts/generate-ledger.py --check   # tylko sprawdź (CI); exit 1 gdy nieaktualny
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS = REPO_ROOT / "docs"
INDEX = DOCS / "INDEX.md"

# Wszystko od znacznika START do END (włącznie ze znacznikami) — markery zachowujemy.
BLOCK_RE = re.compile(
    r"(<!-- LEDGER:START.*?-->)(.*?)(<!-- LEDGER:END -->)",
    re.DOTALL,
)

# Kolejność ról wg numerycznego prefiksu role-foldera; reszta (np. docs/) na koniec listy ról,
# ale dokumenty z docs/ (instrukcja/runbook/reference) trafiają przed role-foldery alfabetycznie.


def parse_frontmatter(text: str) -> dict | None:
    """Minimalny parser frontmatteru YAML (płaskie key: value + proste listy)."""
    if not text.startswith("---"):
        return None
    lines = text.splitlines()
    if lines[0].strip() != "---":
        return None
    fm: dict[str, str] = {}
    for i in range(1, len(lines)):
        line = lines[i]
        if line.strip() == "---":
            return fm
        m = re.match(r"^([A-Za-z_][\w]*):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            fm[key] = val
    return None  # brak zamykającego ---


def clean_scalar(val: str) -> str:
    val = val.strip()
    if len(val) >= 2 and val[0] in "\"'" and val[-1] == val[0]:
        val = val[1:-1]
    return val


def clean_list(val: str) -> list[str]:
    val = val.strip()
    if val.startswith("[") and val.endswith("]"):
        val = val[1:-1]
    out = []
    for item in val.split(","):
        item = clean_scalar(item)
        if item:
            out.append(item)
    return out


def collect_nodes() -> list[dict]:
    nodes = []
    for path in sorted(DOCS.rglob("*.md")):
        if path.name == "_TEMPLATE.md" or path.resolve() == INDEX.resolve():
            continue
        fm = parse_frontmatter(path.read_text(encoding="utf-8"))
        if not fm or "id" not in fm or "type" not in fm:
            continue
        node_id = clean_scalar(fm["id"])
        if "<" in node_id or ">" in node_id:  # nieuzupełniony placeholder szablonu
            continue
        rel = path.relative_to(DOCS).as_posix()
        nodes.append(
            {
                "id": node_id,
                "type": clean_scalar(fm.get("type", "")),
                "title": clean_scalar(fm.get("title", "")),
                "status": clean_scalar(fm.get("status", "")),
                "parents": clean_list(fm.get("parents", "")),
                "path": rel,
            }
        )
    # Sort: po folderze (zero-padded prefiksy sortują się poprawnie), potem po id.
    nodes.sort(key=lambda n: (n["path"].rsplit("/", 1)[0] if "/" in n["path"] else "", n["id"]))
    return nodes


def render_ledger(nodes: list[dict]) -> str:
    if not nodes:
        return (
            "> **Ledger** (auto): brak węzłów — skopiuj `_TEMPLATE.md` z role-foldera, "
            "nadaj `id`, i uruchom ponownie `python3 scripts/generate-ledger.py`."
        )
    rows = [
        f"> **Ledger** (auto, {len(nodes)} węzłów). NIE edytuj ręcznie — `scripts/generate-ledger.py`.",
        "",
        "| id | typ | tytuł | status | parents | plik |",
        "|---|---|---|---|---|---|",
    ]
    for n in nodes:
        parents = ", ".join(n["parents"]) if n["parents"] else "—"
        title = n["title"] or "—"
        link = f"[{Path(n['path']).name}]({n['path']})"
        rows.append(
            f"| {n['id']} | {n['type']} | {title} | {n['status']} | {parents} | {link} |"
        )
    return "\n".join(rows)


def build_index_text() -> str:
    original = INDEX.read_text(encoding="utf-8")
    nodes = collect_nodes()
    ledger = render_ledger(nodes)

    def repl(m: re.Match) -> str:
        return f"{m.group(1)}\n{ledger}\n{m.group(3)}"

    new_text, count = BLOCK_RE.subn(repl, original)
    if count == 0:
        sys.stderr.write(
            "BŁĄD: nie znaleziono znaczników <!-- LEDGER:START --> / <!-- LEDGER:END --> w docs/INDEX.md\n"
        )
        sys.exit(2)
    return new_text


def main() -> int:
    if not INDEX.exists():
        sys.stderr.write(f"BŁĄD: brak {INDEX}\n")
        return 2
    check = "--check" in sys.argv[1:]
    new_text = build_index_text()
    current = INDEX.read_text(encoding="utf-8")
    if check:
        if new_text != current:
            sys.stderr.write(
                "Ledger w docs/INDEX.md jest NIEAKTUALNY. Uruchom: python3 scripts/generate-ledger.py\n"
            )
            return 1
        print("OK: ledger aktualny.")
        return 0
    if new_text != current:
        INDEX.write_text(new_text, encoding="utf-8", newline="\n")
        print(f"Zaktualizowano {INDEX.relative_to(REPO_ROOT).as_posix()} (ledger).")
    else:
        print("Bez zmian: ledger już aktualny.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
