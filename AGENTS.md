# AGENTS.md — reguły pracy (uniwersalny szkielet Slayer)

> **Źródło prawdy reguł.** Per-narzędzie cienkie wskaźniki tylko tu odsyłają: `CLAUDE.md` (Claude Code), `.cursor/rules/` (Cursor). Skopiuj ten plik do projektu i **dołóż kontekst** (stack, dane, cel) na dole.

## Najpierw przeczytaj
`docs/INDEX.md` — mapa projektu (cel, dialektyka, ewaluacja). Decyzje rozstrzygnięte w `25-Syntezy/` — trzymaj się ich albo **świadomie** zaktualizuj dokument.

## Reguły (twarde)
1. **Małe kroki.** Jeden kawałek na raz; pokaż CO + DLACZEGO; czekaj na „dalej".
2. **Żadnej tezy bez dowodu.** Nie zgaduj formatów/API/danych — sprawdź w docs / realnej odpowiedzi.
3. **`git add <konkretne pliki>`** (NIGDY `git add .`); sensowny commit message.
4. **Sekrety NIGDY do repo** → `.env` (w `.gitignore`); commituj `.env.example` (bez wartości).
5. **Weryfikuj, zanim ogłosisz.** Nie mów „działa" bez zbudowania/odpalenia; adwersarialnie sprawdź własny wynik.
6. **Dowód przeczy decyzji (Syntezie)? STOP.** Zgłoś człowiekowi, zapisz w `90-Ewaluacja/Stan.md`; nie dryfuj po cichu.

## Pętla pracy nad ficzerem
Wybierz jedną pozycję z roadmapy → zaplanuj na głos (najmniejszy działający kawałek) → napisz → **uruchom/pokaż → sprawdź** → commit → zmiana koncepcyjna = notka w `docs/` (Teza/Antyteza/Synteza **z warunkiem obalenia**) + aktualizacja Ewaluacji.

## Dwie bramki (po co to wszystko)
- **Epistemiczna = dialektyka** — czy *rozumiem*, czy papuguję.
- **Empiryczna = warunek obalenia** doczepiony do każdej syntezy — test, który może oblać.

Sama dialektyka nie łapie błędu empirycznego (zrozumiana synteza bywa fałszywa) — łapie go ewaluacja. Patrz `docs/INSTRUKCJA-Dokumenty-Dialektyczne.md`.

## Finał nitki
Dojrzała nitka → **dokument LaTeX → PDF** (matematyka w `$...$`, formatka osobno od treści, kompilacja w CI). Szablon: `szablon-dokumentu/`.

---
## Kontekst projektu (UZUPEŁNIJ przy kopiowaniu)
- **Stack:** …
- **Dane / źródła:** …
- **Cel + odbiorca:** …
- **Czego NIE robimy (na teraz):** …
