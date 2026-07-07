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

Dialektyka (1) nie łapie błędu empirycznego — dlatego **sercem metody jest Bramka 2** (niżej). Bramka 3 nie jest w pełni automatyzowalna: [docs/Bramka-Na-Rame.md](docs/Bramka-Na-Rame.md).

## ⭐ Bramka 2 — pętla empiryczna (serce metody)

Najbardziej wyróżniająca część. Odwraca naturalną (i błędną) kolejność pracy:

> **Najpierw MIERZYSZ, potem szukasz rozwiązania.** Nie „mam pomysł → udowodnię, że działa" (to confirmation bias), tylko „mam problem → baseline → próg → dopiero metoda".

Kolejność celowa:

`Sanity → Problem → (R1 prior-art light) → Zapis liczbowy → Baseline (+ próg z góry) → (R2 research PO baseline) → Metoda (jedna, apple-to-apple) → Weryfikacja (CI/p vs baseline vs próg)`

- **Próg z góry** — definiujesz PRZED testem (+X pp). Anti-p-hacking / anti-HARKing: nie da się dostroić wniosku do wyniku.
- **Baseline** — najprostszy, darmowy, uczciwy i **ZMIERZONY** (random → TF-IDF/in-degree → BM25). Bez baseline „lepiej" nic nie znaczy.
- **Higiena** — train/test bez przecieku; progu NIE stroisz na teście; raportujesz CI/wariancję, nie samą średnią.
- **Warunek obalenia** — każda synteza nosi konkretny pomiar, który może ją OBALIĆ. Bez tego jest niesprawdzalna.
- **Granica** — proces / konwencja / ADR (brak metryki) → pętla NIE obowiązuje (nie rób cargo-cultu; kroki bez myślenia = forma bez treści).

**Dlaczego to najważniejsze:** zrozumiana, ładnie rozpisana synteza potrafi być **fałszywa**, dopóki uczciwy held-out jej nie obali — a tego Bramka 1 (dialektyka) NIE łapie. Bramka 2 to moment, w którym projekt mówi, co dzieje się **NAPRAWDĘ**, a nie co założyłeś. Adwersarialnie podważaj własne wyniki, zanim je ogłosisz.

Pełny model + procedura: [AGENTS.md](AGENTS.md) §5–6 · [docs/INSTRUKCJA-Dokumenty-Dialektyczne.md](docs/INSTRUKCJA-Dokumenty-Dialektyczne.md) · 12 trybów porażki: [docs/Katalog-Grzechow-Rozumowania.md](docs/Katalog-Grzechow-Rozumowania.md).

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
