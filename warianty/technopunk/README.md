# Wariant: technopunk

Brandowy wariant formatki dla dokumentów Slayer idących na zewnątrz lub
wymagających pełnej tożsamości wizualnej projektu.

## Kiedy używać

- Zewnętrzne raporty / evalsy / briefy
- Dokumenty pitch-style (treść dojrzała, czas na opakowanie)
- Gdy marka ma aktywnie pracować

## Kiedy NIE używać

- Wewnętrzne robocze notatki (za dużo szumu)
- Druk B/W (scan bands, HUD corners niewidoczne)
- Output parsowany maszynowo

## Co dodaje względem base `szablon-dokumentu/`

| Element | Base sty | Technopunk |
|---|---|---|
| Font | Computer Modern | **Inter** (brandbook) + Source Code Pro |
| Tło | biały | **PAPIER** `#F2EFE7` |
| Kolory | standardowe | **KRAFT / BETON / ALERTRED / KOBALT** |
| Nagłówek | `\maketitle` | 3-kolumnowy 1/4-strony z logo |
| Sekcje | `\section` | `0x01 › Tytuł` z glitch |
| Tło stron | brak | crosshair pattern + scan bands + HUD corners |
| Stopka | brak | barcode + scan status + numer strony |
| Layout | 1 kolumna | **2 kolumny** (multicol, jak IEEE) |
| Glitch | brak | `\glitchline`, `\corr`, `\disruptline` |

## Wymagane paczki TeX Live

```
tlmgr install inter sourcecodepro pgfplots titlesec soul \
              eso-pic fancyhdr multicol ebgaramond cm-super
```

Wszystkie dostępne w TeX Live 2024+. Kompilacja: `pdflatex main.tex` ×2.

## Logo

Umieść plik `slayer-logo.png` obok `main.tex`. Formatka wykryje jego
brak i wstawi typograficzny placeholder (`SLAYER / AI LAB`).

## Teza / Antyteza / Synteza

**Teza:** Dokument Slayera powinien być wizualnie rozpoznawalny — tożsamość
marki buduje zaufanie czytelnika zanim przeczyta słowo treści.

**Antyteza:** Dekoracje zwiększają narzut kompilacji (+5 paczek), mogą
obniżyć czytelność na słabym druku, komplikują port na inne systemy.

**Synteza:** Wariant jako **opt-in** — base `szablon-dokumentu/slayer.sty`
zostaje czyste i przenośne. Technopunk aktywuje się przez podmianę jednego
pliku (`\usepackage{formatka/slayer}`). Zasada formatka⊥treść zachowana:
`tresc/*.tex` są identyczne strukturalnie jak w base.

**Warunek obalenia:** Jeśli wariant nie kompiluje się bez błędów na świeżym
BasicTeX 2024+ po `tlmgr install` wymaganych paczek — musi zostać uproszczony
do podzbioru, który kompiluje się bez problemów.
