# slay-paper 📄

**Uniwersalna formatka + schemat pracy Slayer** — jedno źródło prawdy dla dokumentów.
Od dialektyki (jak myślimy) do empirycznego raportu LaTeX → PDF (jak to wydajemy).

## Co tu jest
```
slay-paper/
├── AGENTS.md                    ← reguły pracy (ŹRÓDŁO prawdy dla agenta) — kopiuj do projektu
├── CLAUDE.md  .cursor/rules/    ← cienkie wskaźniki → AGENTS.md (Claude Code / Cursor)
├── szablon-dokumentu/           ← KOPIUJ to do projektu jako paper/
│   ├── main.tex                 ← wrapper (wiring; nie pisz tu treści)
│   ├── formatka/slayer.sty      ← WYGLĄD (podmienialny bez ruszania treści)
│   └── tresc/
│       ├── 00-strona-tytulowa.tex   ← tytuł + PODPIS autorem + wykres z podpisem
│       └── 10-tresc.tex             ← body: tylko sekcje/akapity (to piszesz)
├── .github/workflows/            ← CI: .tex → PDF (artefakt) + lint unicode-math + ledger-check
├── scripts/generate-ledger.py   ← auto-ledger INDEX z frontmatteru węzłów
└── docs/                         ← WARSZTAT: dialektyka + ewaluacja (knowledge-engineering)
    ├── INDEX.md                  ← mapa nitek + ledger (ZACZNIJ TU)
    ├── 00-Cele/ 10-Tezy/ 15-Antytezy/ 25-Syntezy/ 20-Decyzje/ 90-Ewaluacja/ 60-Reference/  ← role-foldery + _TEMPLATE.md
    ├── INSTRUKCJA-Dokumenty-Dialektyczne.md   ← schemat pracy (4 bramki + pętla empiryczna)
    ├── Katalog-Grzechow-Rozumowania.md        ← 12 trybów porażki (checklist bramek 0–2)
    ├── Bramka-Na-Rame.md                      ← bramka 3 (zewnętrzność, notatka robocza)
    └── Runbook-LaTeX-CI.md                    ← jak ustawić LaTeX→PDF w CI
```

## Schemat pracy (skrót)
1. **Warsztat** (`docs/`): Cel → Teza ↔ Antyteza → Synteza → Decyzja (ADR), a nad wszystkim ⭐**Ewaluacja** + pętla empiryczna („co się NAPRAWDĘ dzieje", żadnej tezy bez dowodu). Szkielet role-folderów z `_TEMPLATE.md` jest w repo.
2. **Finał** dojrzałej nitki: **dokument LaTeX → PDF** (ten szablon). Obsidian = warsztat; PDF = artefakt-produkt.

## Cztery bramki jakości (rdzeń metody)
| # | Bramka | Łapie |
|---|---|---|
| **0** | logiczno-definicyjna | bełkot (GIGO) — niezdefiniowane / niefalsyfikowalne |
| **1** | epistemiczna (dialektyka) | wykucie wierszyka — czy *rozumiem*, czy papuguję |
| **2** | empiryczna (ewaluacja) | proxy / pareidolia — **warunek obalenia** doczepiony do syntezy |
| **3** | na ramę (zewnętrzność) | ślepota ramy — czy w ogóle zadałem właściwe pytanie |

Dialektyka (1) nie łapie błędu empirycznego — zrozumiana synteza bywa fałszywa, łapie ją ewaluacja (2). Dlatego **żadna synteza bez warunku obalenia.** Pełny model + procedura (pętla empiryczna baseline-first): [AGENTS.md](AGENTS.md) §5–6 · [docs/INSTRUKCJA-Dokumenty-Dialektyczne.md](docs/INSTRUKCJA-Dokumenty-Dialektyczne.md). Bramka 3 nie jest w pełni automatyzowalna: [docs/Bramka-Na-Rame.md](docs/Bramka-Na-Rame.md).

## Pliki agenta (vibe-coding)
`AGENTS.md` = źródło prawdy reguł; `CLAUDE.md` i `.cursor/rules/` tylko odsyłają tam (jedno źródło, zero rozjazdu między narzędziami). Kopiując do projektu — uzupełnij sekcję „Kontekst projektu" w `AGENTS.md`.

## Twarde reguły formatki
- **Matematyka zawsze w LaTeX, nigdy unicode** — `$\perp$` nie `⟂`, `$\Delta$` nie `Δ`, `$\le$` nie `≤`.
- **Formatka $\perp$ treść** — `tresc/*.tex` to czysty content; zmiana wyglądu = jeden plik `formatka/slayer.sty`.
- **Wykres + podpis na pierwszej stronie** (empiria od razu widoczna) · **podpis autorem**.

## Jak użyć w nowym projekcie
1. **Warsztat:** skopiuj `docs/` (INDEX + role-foldery + `_TEMPLATE.md`) i `AGENTS.md`; uzupełnij „Kontekst projektu". Twórz węzły z `_TEMPLATE.md`, każdy = wpis w INDEX (`python3 scripts/generate-ledger.py`).
2. **Artefakt:** skopiuj `szablon-dokumentu/` → `<projekt>/paper/`; pisz w `paper/tresc/`, zostaw `paper/formatka/`.
3. **CI:** dodaj workflow (jak `.github/workflows/latex.yml`) → push buduje PDF jako artefakt + lint unicode + ledger-check.

## Kompilacja lokalnie
`cd szablon-dokumentu && latexmk -pdf main.tex` (lub `pdflatex main.tex` $\times 2$).
