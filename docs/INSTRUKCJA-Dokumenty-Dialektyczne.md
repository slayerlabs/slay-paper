---
type: instrukcja
id: SZABLON-DIAL
title: "Szablon dokumentacji dialektycznej Slayer — jak ustawić dokumenty (uniwersalnie)"
status: aktywny
data: 2026-06-23
author: Arkadiusz Słota
---

# Szablon dokumentacji dialektycznej — instrukcja

> Uniwersalny wzór, **jak ustawiać dokumenty projektu w Slayer**: dialektyka (Cel → Teza ↔ Antyteza → Synteza) **+ twarda EWALUACJA stanu**. Skopiuj strukturę i wypełniaj. Działa dla badań, produktu, apki — czegokolwiek. Daj to komuś (albo agentowi AI), żeby ustawił dokumenty tak samo.

## Po co tak
- Każda **decyzja** argumentowana z **dwóch stron** (teza vs antyteza) i rozstrzygana **dowodem/pomiarem**, nie przeczuciem.
- **Ewaluacja** pilnuje, że wiemy, *co się NAPRAWDĘ dzieje* (działa / nie / co się zmieniło) — **nie zakładamy**.
- Agent AI i człowiek dostają jasną mapę + reguły.

## Struktura folderów (podstawowa)
```
docs/
├── INDEX.md            ← mapa: cel, nitki, ewaluacja, reference (ZACZNIJ TU)
├── 00-Cele/            ← po co projekt           (Cxx)
├── 10-Tezy/            ← tezy — propozycje         (Txx)
├── 15-Antytezy/        ← antytezy — steelman       (ATxx)
├── 25-Syntezy/         ← syntezy — rozstrzygnięcie + KRYTERIUM (Sxx)
├── 90-Ewaluacja/       ← ⭐ STAN: co działa, dowody, co się zmienia (REGULARNIE!)
├── 60-Reference/       ← słownik, źródła, dane (opcjonalnie)
└── (gdy trzeba)  20-Decyzje/  40-Architektura/  50-Runbooks/
```
Pliki agenta w root projektu: `CLAUDE.md` (auto-load Claude Code) + `AGENTS.md` (uniwersalne reguły).

## Przepływ dialektyczny
1. **Cel** (Cxx) — po co, dla kogo, **sukces (mierzalny)**, zakres.
2. **Teza** (Txx) — proponowane podejście.
3. **Antyteza** (ATxx) — **najmocniejszy** kontrargument (steelman), nie słomiany strach na wróble.
4. **Synteza** (Sxx) — rozstrzygnięcie + **KRYTERIUM = warunek obalenia** (konkretny test/pomiar, który może OBLAĆ — nie „akceptowalny %", tylko liczba/próg z góry). Synteza to *propozycja* — potwierdzana w Ewaluacji. **Bez warunku obalenia synteza jest niesprawdzalna.**

## ⭐ Ewaluacja — rzecz NAJWAŻNIEJSZA („co się dzieje")
Regularny dokument stanu projektu. Zasada: **żadnej tezy bez dowodu; nie zakładaj — sprawdź.** Łap własne błędy, zanim je ogłosisz (adwersarialnie podważaj własne wyniki).
- **✅ Działa** (z dowodem/liczbą) · **❌ Nie działa / otwarte** · **🔄 Co się zmieniło** · **Czy tezy/syntezy się bronią?** · **➡️ Następne kroki**.
- Aktualizuj **po każdym istotnym kroku** (eksperyment, deploy, ficzer, pomiar). To tu wychodzi prawda projektu — nie w założeniach.

## 🚪 Dwie bramki jakości (po co dialektyka, a po co ewaluacja)
Dialektyka i ewaluacja pilnują **dwóch różnych rzeczy** — potrzebujesz **obu**:
- **Bramka epistemiczna — DIALEKTYKA:** czy *rozumiem*, czy *papuguję*. Rozbicie na tezę↔antytezę→syntezę jest **antywzorcem na „wykucie wierszyka"**: żeby wsadzić myśl w ten kształt, musisz nazwać napięcie i je rozwiązać — nie da się wyrecytować z pamięci. Wymusza zrozumienie zamiast powtórzenia.
- **Bramka empiryczna — EWALUACJA:** czy synteza jest *prawdziwa w świecie*. Tego dialektyka **nie łapie** — łapie to liczba/test.

**Dowód, dlaczego potrzeba obu:** „stitch bije ensemble" było czystą, zrozumianą, porządnie rozpisaną syntezą — i **fałszywą**, dopóki zbalansowany held-out jej nie zabił. Dialektyka nie złapała kontaminacji; złapała ją ewaluacja. Stąd reguła z pkt 4: **każda synteza wychodzi z doczepionym warunkiem obalenia** (test, który może ją wywrócić). Inaczej masz tylko jedną bramkę — i pewność, że rozumiesz coś, co jest nieprawdą.

## 📄 Finał każdej nitki: dokument LaTeX → PDF
Dokumenty w Obsidianie to **warsztat** (dialektyka, ewaluacja). Dojrzała nitka/projekt **kończy się dokumentem LaTeX skompilowanym do `.pdf`** — to jest **artefakt-produkt**. Reguły, żeby wszystko wyglądało spójnie:
- **Matematyka zawsze w LaTeX, nigdy unicode.** `$\perp$` zamiast `⟂`, `$\alpha$` zamiast `α`, `$\le$` zamiast `≤`. Jeden mechanizm znaczków = spójny skład.
- **Formatka osobno od treści.** Wybieramy **jedną formatkę-wzorzec** (np. Overleaf, szablony typu „report"); nasze pliki `.tex` zawierają **tylko treść** (body/chapter) — żeby dało się podmienić formatkę bez ruszania merytoryki.
- **Każdy `.tex` podpisany autorem.**
- **Kompilacja przez CI** (GitHub Actions / GitLab CI): `.tex` w repo → **PDF jako artefakt**, zawsze w aktualnej formatce. Zmiana wzorca → wszystkie dokumenty odświeżają się spójnie.

## Konwencja
- `NN-Folder/IDxx-Krotka-Nazwa.md`; **unikalne basename** (Obsidian linkuje po nazwie — bez powtórek).
- Każdy węzeł: frontmatter (`type/id/title/status`) + treść + **Powiązania** (`[[...]]`).
- `INDEX` = tabela nitek (Teza | Antyteza | Synteza) + linki do Celu / Ewaluacji / Reference.

---

## Szablony do skopiowania

### INDEX
```markdown
# <Projekt> — indeks
> <jedno zdanie: po co projekt>. Szkielet do rozbudowy.

## Cel
[[Cxx-...]]

## Nitki dialektyczne (Teza ↔ Antyteza → Synteza)
| # | Teza | Antyteza | Synteza |
|---|------|----------|---------|
| 1 | [[Txx-...]] | [[ATxx-...]] | [[Sxx-...]] |

## Ewaluacja
[[90-Ewaluacja/Stan]] — co działa, dowody, co się zmienia.

## Reference
[[Glosariusz]] · [[Dane-...]]
```

### Cel (00-Cele/Cxx-...)
```markdown
---
type: cel
id: Cxx
title: "..."
status: aktywny
---
# Cxx — Cel
## Po co
## Dla kogo
## Sukces (mierzalne)
## Zakres (JEST / NIE w MVP)
## Powiązania
[[INDEX]]
```

### Teza (10-Tezy/Txx-...)
```markdown
---
type: teza
id: Txx
status: w-dyskusji
parents: ["Cxx"]
---
# Txx — <teza>
## Teza
<proponowane podejście>
## Antyteza ↔ Synteza
[[ATxx-...]] → [[Sxx-...]]
```

### Antyteza (15-Antytezy/ATxx-...)
```markdown
---
type: antyteza
id: ATxx
status: w-dyskusji
parents: ["Txx"]
---
# ATxx — <kontrteza> (steelman)
## Antyteza
<najmocniejsza wersja przeciwnego stanowiska>
## Granica
<kiedy/dlaczego nie>
## Powiązania
teza: [[Txx-...]] · synteza: [[Sxx-...]]
```

### Synteza (25-Syntezy/Sxx-...)
```markdown
---
type: synteza
id: Sxx
status: propozycja
parents: ["Txx", "ATxx"]
---
# Sxx — <rozstrzygnięcie>
## Synteza
<co wybieramy i dlaczego>
## Kryterium (co to rozstrzyga — POMIAR/DOWÓD)
<liczba / test / warunek>
## Powiązania
[[Txx-...]] ↔ [[ATxx-...]]
```

### ⭐ Ewaluacja (90-Ewaluacja/Stan.md)
```markdown
---
type: ewaluacja
id: EVAL
status: zywy-dokument
---
# Stan projektu — ewaluacja
> Żadnej tezy bez dowodu. Co się NAPRAWDĘ dzieje. Aktualizuj po każdym kroku.

## ✅ Działa (z dowodem)
| Co | Dowód (liczba/źródło/output) |
|---|---|

## ❌ Nie działa / otwarte
| Co | Co wyszło / czego brakuje |
|---|---|

## 🔄 Co się zmieniło (data)
- ...

## Czy tezy/syntezy się bronią?
- <Sxx>: ✅ potwierdzona / ⚠️ do rewizji / ❌ obalona — dlaczego

## ➡️ Następne kroki
1. ...
```

### Pliki agenta (gdy projekt = kod / vibe-coding)
```markdown
# CLAUDE.md  → krótki entrypoint: "Zacznij od docs/INDEX.md i AGENTS.md" + 3-5 twardych zasad.
# AGENTS.md  → reguły pracy: małe kroki, żadnej tezy bez dowodu, git add konkretne pliki,
#              sekrety w .env, + pętla pracy nad ficzerem + obowiązek AKTUALIZACJI Ewaluacji
#              + finał nitki: dokument LaTeX → PDF (matematyka w $...$, formatka osobno, CI).
```

---

## Checklist „ustaw od zera"
1. `docs/INDEX.md` + foldery `00-Cele 10-Tezy 15-Antytezy 25-Syntezy` **i `90-Ewaluacja`**.
2. Napisz **Cel** (mierzalny sukces).
3. Dla każdej decyzji: **Teza → Antyteza (steelman) → Synteza (z kryterium)**.
4. Załóż **Ewaluację** od razu (pusty szkielet) i **wypełniaj na bieżąco** — to nie dodatek, to rdzeń.
5. Projekt z kodem/agentem → dodaj `CLAUDE.md` + `AGENTS.md` (z obowiązkiem aktualizacji Ewaluacji).
6. Dokładaj `20-Decyzje / 40-Architektura / 50-Runbooks / 60-Reference`, gdy realnie potrzebne (nie na zapas).
7. **Finał:** gdy nitka dojrzeje → **dokument LaTeX → PDF** (formatka osobno, treść osobno, matematyka w `$...$`, kompilacja w CI).

## Powiązania
Przykłady żywe: `NaukaML/Badania/...` (badania), `DeployIQSteel/...` (produkt), `TFT-DuoCoach` (apka).
