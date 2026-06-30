---
type: instrukcja
id: SZABLON-DIAL
title: "Szablon dokumentacji dialektycznej Slayer — jak ustawić dokumenty (uniwersalnie)"
status: aktywny
author: Arkadiusz Słota
date: 2026-06-23
created_at: 2026-06-23
---

# Szablon dokumentacji dialektycznej — instrukcja

> Uniwersalny wzór, **jak ustawiać dokumenty projektu w Slayer**: dialektyka (Cel → Teza ↔ Antyteza → Synteza → Decyzja) **+ twarda EWALUACJA stanu**. Skopiuj strukturę i wypełniaj. Działa dla badań, produktu, apki — czegokolwiek. Reguły-kontrakt: [AGENTS.md](../AGENTS.md).

## Po co tak
- Każda **decyzja** argumentowana z **dwóch stron** (teza vs antyteza) i rozstrzygana **dowodem/pomiarem**, nie przeczuciem.
- **Ewaluacja** pilnuje, że wiemy, *co się NAPRAWDĘ dzieje* (działa / nie / co się zmieniło) — **nie zakładamy**.
- Agent AI i człowiek dostają jasną mapę + reguły; atomic `.md` + frontmatter = jednostka retrievalu (RAG/MCP).

## Struktura folderów (pod `docs/`)
```
docs/
├── INDEX.md            ← mapa: cel, nitki, ewaluacja, reference (ZACZNIJ TU; ledger auto)
├── 00-Cele/            ← po co projekt           (Cxx)
├── 10-Tezy/            ← tezy — propozycje         (Txx)
├── 15-Antytezy/        ← antytezy — steelman       (ATxx)
├── 25-Syntezy/         ← syntezy — rozstrzygnięcie + KRYTERIUM obalenia (Sxx)
├── 20-Decyzje/         ← ADR — decyzja podjęta     (Dxx)
├── 90-Ewaluacja/       ← ⭐ STAN: co działa, dowody, pętla empiryczna (REGULARNIE!)
├── 60-Reference/       ← słownik, źródła, dane     (Rxx)
└── (gdy trzeba)  30-Fakty/  40-Architektura/  45-Eksperymenty/  50-Runbooks/
```
Pliki agenta w root projektu: `AGENTS.md` (źródło prawdy reguł) + `CLAUDE.md` / `.cursor/rules/` (cienkie wskaźniki).

## Przepływ dialektyczny
1. **Cel** (Cxx) — po co, dla kogo, **sukces (mierzalny)** + kryterium falsyfikowalne, zakres.
2. **Teza** (Txx) — proponowane podejście. *Jeśli nie umiesz napisać przekonującej Antytezy w jednym zdaniu → to nie Teza, to ADR (`20-Decyzje/`).*
3. **Antyteza** (ATxx) — **najmocniejszy** kontrargument (steelman, $\ge 3$ punkty), nie słomiany strach na wróble.
4. **Synteza** (Sxx) — rozstrzygnięcie przez **zmienną kontekstową** (nie binarny wybór) + **KRYTERIUM = warunek obalenia** (konkretny test/pomiar/próg z góry, który może OBLAĆ — nie „akceptowalny %", tylko liczba). Synteza to *propozycja* — potwierdzana w Ewaluacji. **Bez warunku obalenia synteza jest niesprawdzalna.**
5. **Decyzja** (Dxx) — gdy alternatywa jasna: ADR z Reject/Implements/Reversibility/Action items.

## ⭐ Ewaluacja — rzecz NAJWAŻNIEJSZA („co się dzieje")
Regularny dokument stanu projektu. Zasada: **żadnej tezy bez dowodu; nie zakładaj — sprawdź.** Łap własne błędy, zanim je ogłosisz (adwersarialnie podważaj własne wyniki).
- **✅ Działa** (z dowodem/liczbą) · **❌ Nie działa / otwarte** · **🔄 Co się zmieniło** · **Pętla empiryczna** · **Czy tezy/syntezy się bronią?** · **➡️ Następne kroki**.
- Aktualizuj **po każdym istotnym kroku** (eksperyment, deploy, ficzer, pomiar). To tu wychodzi prawda projektu — nie w założeniach.

## 🚪 Cztery bramki jakości (każda łapie inny błąd — potrzebujesz WSZYSTKICH)
| # | Bramka | Pyta | Łapie |
|---|---|---|---|
| **0** | logiczno-definicyjna | terminy zdefiniowane/pierwotne? falsyfikowalne? | **bełkot** (GIGO) |
| **1** | epistemiczna — DIALEKTYKA | *rozumiem*, czy *papuguję*? | wykucie wierszyka |
| **2** | empiryczna — EWALUACJA | prawdziwe w świecie? | proxy / pareidolia |
| **3** | na ramę — ZEWNĘTRZNOŚĆ | właściwa rama/paradygmat? konwergencja zasłużyła? | ślepota ramy |

- **Bramka 1 (dialektyka)** jest antywzorcem na „wykucie wierszyka": żeby wsadzić myśl w kształt teza↔antyteza→synteza, musisz nazwać napięcie i je rozwiązać — nie da się wyrecytować z pamięci.
- **Dowód, że 1 nie wystarcza:** „stitch bije ensemble" było czystą, *zrozumianą*, porządnie rozpisaną syntezą — i **fałszywą**, dopóki zbalansowany held-out jej nie zabił. Dialektyka nie złapała kontaminacji; złapała ją ewaluacja. Stąd reguła pkt 4: **każda synteza wychodzi z doczepionym warunkiem obalenia**.
- **Bramka 0** (logika/definicje) działa zanim cokolwiek wejdzie w formę — bez niej forma wchłania bełkot (12 trybów porażki: [[Katalog-Grzechow-Rozumowania]]).
- **Bramka 3** (rama) pilnuje, czy w ogóle zadajesz właściwe pytanie. **Nie jest w pełni automatyzowalna** (self-reference wall) — ~80% łapie tani automat, ogon łapie człowiek z własną stawką; marker zewnętrzności = **obojętność, nie opór**. Rozważania: [[Bramka-Na-Rame]].

## 🔬 Pętla empiryczna (bramka 2 w praktyce — TYLKO twierdzenia z metryką)
> Kolejność CELOWA: **najpierw mierzysz, potem szukasz rozwiązania** (lek na confirmation bias).

`Sanity → Problem → (R1 prior-art light) → Zapis liczbowy → Baseline (+ próg z góry) → (R2 research PO baseline) → Metoda (jedna, apple-to-apple) → Weryfikacja (CI/p vs baseline vs próg)`

- **Baseline:** najprostszy darmowy, uczciwy (random → TF-IDF/in-degree → BM25), ZMIERZONY.
- **Próg z góry:** zdefiniuj PRZED testem (+Xpp) — anty-p-hacking/HARKing.
- **Higiena:** train/test bez przecieku; progu NIE strój na teście; raportuj CI/wariancję, nie samą średnią.
- **GRANICA:** proces / konwencja / ADR (brak metryki) → pętla **NIE** obowiązuje (nie rób cargo-cultu — kroki bez myślenia = forma bez treści).

Kotwica: REFORMS (Science Advances 2024) · arXiv:2511.21354 · arXiv:2409.12116 · Manning i in. *Introduction to IR* rozdz. 8.

## 📄 Finał każdej nitki: dokument LaTeX → PDF
Dokumenty w `docs/` to **warsztat** (dialektyka, ewaluacja). Dojrzała nitka/projekt **kończy się dokumentem LaTeX skompilowanym do `.pdf`** — to **artefakt-produkt** (szablon: `szablon-dokumentu/`). Reguły:
- **Matematyka zawsze w LaTeX, nigdy unicode.** `$\perp$` zamiast `⟂`, `$\alpha$` zamiast `α`, `$\le$` zamiast `≤` (lint w CI).
- **Formatka osobno od treści** — `tresc/*.tex` to czysty content; zmiana wyglądu = jeden plik `formatka/slayer.sty`.
- **Każdy `.tex` podpisany autorem · wykres + podpis na 1. stronie · kompilacja w CI** (PDF jako artefakt).

## Konwencja
- `NN-Folder/IDxx-Krotka-Nazwa.md`; **unikalne basename** (Obsidian linkuje po nazwie — bez powtórek).
- Każdy węzeł: frontmatter (standard w [AGENTS.md §8](../AGENTS.md): `type/id/title/status/parents/author/date/created_at`) + treść + **Powiązania** (`[[...]]`).
- `INDEX` = tabela nitek (Teza | Antyteza | Synteza) + Decyzje + linki do Celu / Ewaluacji / Reference; ledger auto przez `scripts/generate-ledger.py`.

## Szablony
**Realne szablony = pliki `docs/<folder>/_TEMPLATE.md`** (jedno źródło prawdy, bez rozjazdu z prozą). Start nowego węzła:
1. Skopiuj `_TEMPLATE.md` z właściwego role-foldera (np. `docs/10-Tezy/_TEMPLATE.md`) → `Txx-Krotka-Nazwa.md`.
2. Nadaj `id` (sprawdź unikalność: `grep ^id: docs/**/*.md`), `title`, `created_at`; uzupełnij `parents`.
3. Dopisz węzeł do `docs/INDEX.md` (lub uruchom `python3 scripts/generate-ledger.py`).

Frontmatter — pełna specyfikacja i pola opcjonalne (`synthesizes`/`implements`/`rejects`/`data_decyzji`) w [AGENTS.md §8](../AGENTS.md).

### Mini-przykład: gotowy węzeł (Synteza) — żeby nie trzeba było otwierać folderu
```markdown
---
type: synteza
id: S1
title: "Cache warstwowy zamiast pełnego in-memory"
status: propozycja
parents: ["T1", "AT1"]
synthesizes: ["T1", "AT1"]
author: Ula
date: 2026-06-30
created_at: 2026-06-30
---

# S1 — Cache warstwowy zamiast pełnego in-memory

## Synteza
Zmienna kontekstowa = rozmiar gorącego zbioru. Mieści się w RAM (< ~2 GB) → in-memory (T1);
powyżej → L1 in-memory + L2 na dysku (AT1 miała rację dla dużych zbiorów). Nie binarny wybór.

## Kryterium obalenia (POMIAR / DOWÓD — próg z góry)
p99 latencji L2 < 5 ms na zbiorze 10 GB. Jeśli p99 > 5 ms — synteza upada, wracamy do
pełnego in-memory z shardingiem. (Próg ustalony PRZED testem — anty-HARKing.)

## Powiązania
[[../10-Tezy/T1-cache-in-memory]] ↔ [[../15-Antytezy/AT1-koszt-ram]]
```

## Checklist „ustaw od zera"
1. `docs/INDEX.md` + foldery `00-Cele 10-Tezy 15-Antytezy 25-Syntezy 20-Decyzje` **i `90-Ewaluacja`** (szablony już są w repo).
2. Napisz **Cel** (mierzalny sukces + kryterium falsyfikowalne).
3. Dla każdej decyzji: **Teza → Antyteza (steelman) → Synteza (z warunkiem obalenia)** → w razie czego **ADR**.
4. Załóż **Ewaluację** od razu (pusty szkielet) i **wypełniaj na bieżąco** — to nie dodatek, to rdzeń. Twierdzenia z metryką → **pętla empiryczna** (baseline-first).
5. Projekt z kodem/agentem → `AGENTS.md` + `CLAUDE.md` (obowiązek aktualizacji Ewaluacji; 4 bramki).
6. Dokładaj `20-Decyzje / 40-Architektura / 50-Runbooks / 60-Reference`, gdy realnie potrzebne (nie na zapas).
7. **Finał:** gdy nitka dojrzeje → **dokument LaTeX → PDF** (formatka osobno, treść osobno, matematyka w `$...$`, kompilacja w CI).

## Powiązania
[[INDEX]] · [[Katalog-Grzechow-Rozumowania]] · [[Bramka-Na-Rame]] · [[Runbook-LaTeX-CI]] · kontrakt: [AGENTS.md](../AGENTS.md).
