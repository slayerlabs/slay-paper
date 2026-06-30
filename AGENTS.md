# AGENTS.md — reguły pracy + kontrakt formatu (uniwersalny szkielet Slayer)

> **Źródło prawdy reguł.** Per-narzędzie cienkie wskaźniki tylko tu odsyłają: `CLAUDE.md` (Claude Code), `.cursor/rules/` (Cursor). Skopiuj ten plik do projektu i **dołóż kontekst** (stack, dane, cel) na dole.
>
> **Dla DOWOLNEGO agenta AI** (Claude / GPT / Codex / Cursor / Cline / Aider / …): gdy widzisz ten format (foldery `docs/00-Cele/10-Tezy/15-Antytezy/25-Syntezy/20-Decyzje/90-Ewaluacja` + frontmatter `type/id`), **stosuj go BEZWZGLĘDNIE** — nie spłaszczaj do „zwykłych notatek", nie wymyślaj własnej struktury, nie pomijaj bramek. Ten plik to **kontrakt**.

## 0. Istota — PO CO to jest (nie pomijaj; bez tego stosujesz formę bez treści)
To **nie** folder z notatkami. To **knowledge-engineering system**: dokumentujemy *myślenie*, nie sam wynik. Po co:
1. **Nie powtarzać** tych samych dyskusji co pół roku — audit trail każdej nieoczywistej decyzji.
2. **Wrócić** do projektu po przerwie bez utraty kontekstu.
3. **Onboarding** człowieka/AI: czyta kilka atomic plików w kolejności → pełny kontekst, zero 1-on-1.
4. **Atomic markdown + frontmatter** = idealna jednostka dla RAG / MCP retrieval (patrz §9).

**Reguła nadrzędna:** *żadnej tezy bez dowodu; nie zakładaj — sprawdź.* Forma istnieje, by **wymusić myślenie**, nie żeby je udawać.

## 1. Najpierw przeczytaj
`docs/INDEX.md` — mapa projektu (cel, nitki, ewaluacja, reference). Decyzje rozstrzygnięte w `docs/25-Syntezy/` i `docs/20-Decyzje/` — trzymaj się ich albo **świadomie** zaktualizuj dokument (nie dryfuj po cichu).

## 2. Reguły twarde
1. **Małe kroki.** Jeden kawałek na raz; pokaż CO + DLACZEGO; czekaj na „dalej".
2. **Żadnej tezy bez dowodu.** Nie zgaduj formatów/API/danych — sprawdź w docs / realnej odpowiedzi.
3. **`git add <konkretne pliki>`** (NIGDY `git add .`); sensowny commit message. **PR-only**: feature branch → PR (nie pushuj na `main`/`Deploy` bezpośrednio).
4. **Sekrety NIGDY do repo** → `.env` (w `.gitignore`); commituj `.env.example` (bez wartości).
5. **Weryfikuj, zanim ogłosisz.** Nie mów „działa" bez zbudowania/odpalenia; adwersarialnie sprawdź własny wynik.
6. **Dowód przeczy decyzji (Syntezie)? STOP.** Zgłoś człowiekowi, zapisz w `docs/90-Ewaluacja/Stan.md`; nie dryfuj po cichu.

## 3. Struktura — WYMUSZONA (dokładnie te podkatalogi pod `docs/`, NIE inne)
| Folder | Rola | Prefiks ID |
|---|---|---|
| `00-Cele/` | po co (mierzalny sukces + kryterium falsyfikowalne) | `C` |
| `10-Tezy/` | propozycja podejścia | `T` |
| `15-Antytezy/` | **steelman** kontrargumentu (≥3 punkty, NIE strawman) | `AT` |
| `25-Syntezy/` | rozstrzygnięcie przez zmienną kontekstową + **kryterium obalenia** | `S` |
| `20-Decyzje/` | ADR (decyzja podjęta): Reject/Implements/Reversibility/Action items | `D` |
| `90-Ewaluacja/` | ⭐ STAN: co działa (z liczbą), co nie, co się zmieniło — **rdzeń, nie dodatek** | — |
| `60-Reference/` | cudze pomysły / dane / glosariusz (soczewki) | `R` |
| *(opcjonalnie)* `30-Fakty/` `40-Architektura/` `45-Eksperymenty/` `50-Runbooks/` | gdy realnie potrzebne | `F/A/E/RB` |

Nie twórz innych top-level role-folderów. Dane/domenę trzymaj w `60-Reference/` lub poza role-folderami. Każdy nowy dokument = wpis w `docs/INDEX.md` (ledger auto: `scripts/generate-ledger.py`).

## 4. Dialektyka: Cel → Teza ↔ Antyteza → Synteza → Decyzja
- **Teza ↔ Antyteza:** jeśli nie umiesz w **jednym zdaniu** napisać Antytezy brzmiącej **realnie przekonująco** → to nie Teza, to ADR (`20-Decyzje/`). To wymusza prawdziwe myślenie o alternatywach, nie post-fakto racjonalizację.
- **Synteza ≠ binarny wybór:** integruje T+AT przez **zmienną kontekstową**; wychodzi z **warunkiem obalenia** (liczba/test/próg z góry). Bez niego synteza jest niesprawdzalna — co najwyżej *zrozumiana* (bramka 1), nie *sprawdzona* (bramka 2).

## 5. CZTERY bramki jakości (potrzebujesz WSZYSTKICH — każda łapie inny błąd)
| # | Bramka | Pyta | Łapie | Kto/jak |
|---|---|---|---|---|
| **0** | logiczno-definicyjna | terminy zdefiniowane/pierwotne? twierdzenie falsyfikowalne? | **bełkot** (GIGO) | automat/dyscyplina |
| **1** | epistemiczna (dialektyka) | rozumiem, nie papuguję? | wykucie wierszyka | rozbicie na T↔AT→S |
| **2** | empiryczna (ewaluacja) | prawdziwe w świecie? | proxy / pareidolia | liczba/test/próg (§6) |
| **3** | na ramę (zewnętrzność) | właściwa rama/paradygmat? czy konwergencja zasłużyła? | **ślepota ramy** | ~80% automat + ogon człowiek z własną stawką |

- **Kolejność błędu:** bramka 0 łapie bełkot zanim w ogóle wejdzie w formę; 1 — czy myśl jest moja; 2 — czy jest prawdziwa; 3 — czy zadałem właściwe pytanie w ogóle.
- **Dowód, że 1 nie wystarcza:** „stitch bije ensemble" było czystą, *zrozumianą* syntezą — i **fałszywą**, dopóki zbalansowany held-out jej nie zabił. Dialektyka nie złapała kontaminacji; złapała ją ewaluacja. Stąd: **każda synteza wychodzi z doczepionym warunkiem obalenia**.
- **Bramka 3 nie jest w pełni automatyzowalna** (self-reference wall: co specyfikujesz, jest wewnątrz ramy i dziedziczy jej ślepe plamy). Marker prawdziwej zewnętrzności = **obojętność, nie opór** (anty-Ty to Ty z minusem — ta sama oś, maksymalnie wchłanialny). Szczegóły i mechanizmy na te ~80%: [docs/Bramka-Na-Rame.md](docs/Bramka-Na-Rame.md). Tryby porażki rozumowania (12 grzechów) jako checklist 0–2: [docs/Katalog-Grzechow-Rozumowania.md](docs/Katalog-Grzechow-Rozumowania.md).

## 6. Bramka 2 w praktyce — Pętla empiryczna (TYLKO twierdzenia z metryką)
> Kolejność CELOWA: **najpierw mierzysz, potem szukasz rozwiązania** (lek na confirmation bias).

`Sanity → Problem → (R1 prior-art light) → Zapis liczbowy → Baseline (+ próg z góry) → (R2 research PO baseline) → Metoda (jedna, apple-to-apple) → Weryfikacja (CI/p vs baseline vs próg)`

- **Sanity:** czy MY już tego nie zmierzyliśmy? (rzut na Ewaluację).
- **Baseline:** najprostszy darmowy, uczciwy (random → TF-IDF/in-degree → BM25), ZMIERZONY.
- **Próg z góry:** zdefiniuj PRZED testem (+Xpp) — anty-p-hacking/HARKing.
- **Research PO baseline:** zakotwiczony w zmierzonej luce; cytuj prior-art, nie wynajduj.
- **Higiena:** train/test bez przecieku; progu NIE strój na teście; raportuj CI/wariancję, nie samą średnią.
- **GRANICA:** proces / konwencja / ADR (brak metryki) → pętla **NIE** obowiązuje; bramka = dialektyka + retrospektywna adopcja. **Nie rób cargo-cultu** (kroki bez myślenia = forma bez treści).

Kotwica: REFORMS (Science Advances 2024) · arXiv:2511.21354 · arXiv:2409.12116 · Manning i in. *Introduction to IR* rozdz. 8.

## 7. Decyzja: co piszę?
- realne napięcie z alternatywą → **Teza + Antyteza (+ Synteza)**
- decyzja już podjęta (jasna alternatywa) → **ADR** (`20-Decyzje/`)
- bugfix > 30 min → **Runbook** (`50-Runbooks/`)
- empiryczny test/A-B → **Eksperyment** (`45-Eksperymenty/`)

## 8. Frontmatter (KAŻDY plik) — standard
```yaml
type: <cel|teza|antyteza|synteza|decyzja|fakt|powod|reference|ewaluacja|runbook>
id: <PRE><N>            # unikalne i NAMESPACED (np. C1/T1/AT1/S1/D1; sub-domena: CC/TC/…)
title: "..."
status: <aktywny|w-dyskusji|propozycja|zaakceptowana|...>
parents: ["<id>"]
author: ...
date: <YYYY-MM-DD>      # data źródła/analizy (może być wsteczna)
created_at: <YYYY-MM-DD> # maszynowa data utworzenia, NIEzmienna (≠ date)
```
ID **unikalne** — przed nadaniem sprawdź realny zbiór (`grep ^id:`), nie prozę INDEX-u. **Unikalne basename** pliku (`NN-Folder/IDxx-Krotka-Nazwa.md`) — Obsidian linkuje po nazwie.

## 9. MCP (`optimal-context` / `vault_*`) — dlaczego format jest maszynowo-czytelny
Dokumenty są **jednostką retrievalu**: atomic `.md` + frontmatter → indeksowane semantycznie (e5-large/Qdrant). Agent sięga przez `vault_read` / `vault_find` / `vault_search`. Pisz tak, by `id` / `title` / `type` **jednoznacznie identyfikowały węzeł**; jeden plik = jeden węzeł rozumowania (nie sklejaj wielu ról w jednym pliku).

## 10. Pętla pracy nad ficzerem
Wybierz jedną pozycję z roadmapy → zaplanuj na głos (najmniejszy działający kawałek) → napisz → **uruchom/pokaż → sprawdź** → commit → zmiana koncepcyjna = notka w `docs/` (Teza/Antyteza/Synteza **z warunkiem obalenia**) + aktualizacja Ewaluacji.

## 11. Finał nitki: dokument LaTeX → PDF
Dojrzała nitka → **dokument LaTeX → PDF** (artefakt-produkt). Szablon: `szablon-dokumentu/`. Twarde reguły:
- **Matematyka zawsze w LaTeX, nigdy unicode** — `$\perp$` nie `⟂`, `$\Delta$` nie `Δ`, `$\le$` nie `≤` (lint w CI).
- **Formatka ⟂ treść** — `tresc/*.tex` to czysty content; zmiana wyglądu = jeden plik `formatka/slayer.sty`.
- **Wykres + podpis na pierwszej stronie** (empiria od razu widoczna) · **podpis autorem** · **kompilacja w CI** (PDF jako artefakt).

## 12. Git / higiena
- PR-only (feature branch → PR), `git add` konkretne pliki, sensowny message. Bez sekretów w repo.
- Nowy dokument = wpis w `docs/INDEX.md` (uruchom `scripts/generate-ledger.py`).
- Dojrzała nitka → opcjonalnie artefakt-produkt (LaTeX → PDF; matematyka w `$...$`, formatka osobno).

---
## Kontekst projektu (UZUPEŁNIJ przy kopiowaniu)
- **Stack:** …
- **Dane / źródła:** …
- **Cel + odbiorca:** …
- **Czego NIE robimy (na teraz):** …
