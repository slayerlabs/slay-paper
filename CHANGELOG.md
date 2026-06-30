# Changelog

Odwrotnie chronologicznie. Każdy wpis: co i **dlaczego**, nie tylko co.

## 2026-06-30 — Komplet mechanik dialektyki (PR #5)

Domknięcie luki mechanik względem `dialektyka-starter`. slay-paper przestaje być
„tylko LaTeX + 2 bramki" i staje się kompletnym starterem knowledge-engineering —
zachowując pipeline LaTeX/CI, Katalog grzechów i Bramkę-na-ramę.

### Dodane
- **4 zunifikowane bramki jakości** (było 2): 0 logiczno-definicyjna · 1 epistemiczna ·
  2 empiryczna · 3 na-ramę. Kolejność 0 → 3 = od najtańszego do najdroższego sprawdzenia.
- **Fizyczny szkielet `docs/`**: role-foldery `00-Cele/10-Tezy/15-Antytezy/25-Syntezy/`
  `20-Decyzje/90-Ewaluacja/60-Reference` z `_TEMPLATE.md` + `docs/INDEX.md` z auto-ledgerem.
- **Pętla empiryczna baseline-first** (AGENTS §6): Sanity → Baseline → próg z góry
  (anty-HARKing) → research PO baseline → weryfikacja vs próg.
- **`scripts/generate-ledger.py`** (stdlib, tryb `--check`) + CI `ledger.yml`: auto-spis
  węzłów w INDEX z frontmatteru. Domyka aspirującą referencję `scripts/generate-ledger`.
- **`scripts/lint-math-unicode.py`** + wpięcie w `latex.yml`: reguła „matematyka zawsze
  w LaTeX, nigdy unicode" egzekwowana teraz także na markdown (wcześniej tylko `.tex`).
- Standard frontmatter (`date`/`created_at`, namespaced `id`), routing
  Teza/ADR/Runbook/Eksperyment, sekcja MCP — w AGENTS.

### Zmienione
- **AGENTS.md**: z „reguł pracy" na pełny **kontrakt formatu** (źródło prawdy).
- **INSTRUKCJA**: 2 → 4 bramki + pętla empiryczna + inline mini-przykład gotowej Syntezy;
  szablony wskazują realne `_TEMPLATE.md` (jedno źródło, zero rozjazdu z prozą).
- **Katalog grzechów**: meta → 4 bramki, 12 grzechów otagowanych bramką, frontmatter.
- **Bramka-na-ramę**: frontmatter + pozycja jako kanoniczna bramka 3.
- **README**: 4 bramki, rozbudowane drzewo, kroki użycia (warsztat + artefakt).

### Naprawione
- **Wisząca referencja**: AGENTS/CLAUDE/.cursor kazały „zacznij od `docs/INDEX.md`",
  a plik nie istniał. Teraz istnieje (z ledgerem).
- 10 naruszeń reguły math-w-LaTeX w prozie markdown skonwertowanych na `$...$`/słowa.

### Review (Xavier) — wszystkie uwagi zaadresowane
- **Bramka 3 niedoprecyzowana operacyjnie** → AGENTS §5: 3 mechanizmy na ~80%, każdy
  z własnym testem; explicite „brak checklistu by design, wymaga zewnętrznej interwencji".
- **Katalog brak tagu `[B3]`** → jawna nota, że jest zamierzony (self-reference wall).
- **`generate-ledger.py` brak multiline YAML** → docstring: parser CELOWO minimalny.
- **INDEX puste tabele + redundancja z ledgerem** (uwaga D + drobne) → ręczne tabele usunięte;
  `generate-ledger.py` generuje teraz CAŁOŚĆ (Cele · Nitki T↔AT→S rekonstruowane z relacji ·
  Decyzje · Pozostałe węzły). INDEX = jedno źródło prawdy (frontmatter); puste sekcje pokazują
  jawne `_(brak)_`, nie stub-tabele.
- **INSTRUKCJA straciła inline przykłady** → przywrócony mini-przykład gotowej Syntezy.

### Podziękowania
Dzięki **@Xavier** (Digital Agent, OpenClaw) za gruntowny, rzeczowy review — werdykt „ship it" + 5 trafnych uwag polish, wszystkie zaadresowane (A–C, E w `45615b8`; D w `3814bb0`). 🙂
