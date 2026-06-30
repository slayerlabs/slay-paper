---
type: runbook
id: RB-LATEX-CI
title: "Runbook: dokument LaTeX → PDF w CI (formatka osobno od treści)"
status: aktywny
author: Arkadiusz Słota
date: 2026-06-23
created_at: 2026-06-23
---

# Runbook — LaTeX → PDF w CI

> Jak ustawić finał nitki: empiryczny raport „naukowy" (wykres + podpis na 1. stronie),
> kompilowany automatycznie do PDF. Cel: **spójny format** dla wszystkich dokumentów
> + artefakt do prezentacji / ściąga przed prelekcją. Działający przykład: `TFT-DuoCoach/paper/`.

## Zasada nadrzędna: formatka osobno od treści
Rozdziel **wygląd** od **treści**, żeby dało się podmienić formatkę bez ruszania merytoryki:
```
paper/
├── main.tex              ← wrapper (\documentclass + \usepackage{formatka/...} + \input)
├── formatka/slayer.sty   ← WYGLĄD (preambuła, marginesy, podpisy) — podmienialne
└── tresc/
    ├── 00-strona-tytulowa.tex   ← tytuł + PODPIS autorem + wykres z podpisem
    └── 10-tresc.tex             ← body: tylko \section/\akapit (to piszesz)
```
`tresc/*.tex` **nie zawiera** preambuły ani `\begin{document}` — sam content.

## Twarde reguły
1. **Matematyka zawsze w LaTeX, nigdy unicode** — `$\perp$` nie `⟂`, `$\alpha$` nie `α`, `$\le$` nie `≤`.
2. **Wykres + podpis na pierwszej stronie** — empiria widoczna od razu (`figure` + `\caption`).
   Wykresy w `pgfplots`/TikZ = bez plików binarnych, kompilują się same.
3. **Podpis autorem** na stronie tytułowej.
4. **Jedna formatka-wzorzec** dla wszystkich dokumentów (docelowo wspólne repo formatki;
   inspiracja: szablony Overleaf typu „report").

## CI — GitHub Actions (`.github/workflows/latex.yml`)
```yaml
on: { push: { paths: ['paper/**'] }, workflow_dispatch: {} }
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: xu-cheng/latex-action@v3
        with: { working_directory: paper, root_file: main.tex }
      - uses: actions/upload-artifact@v4
        with: { name: dokument-pdf, path: paper/main.pdf }
```
Push → Actions buduje `main.pdf` → pobierasz z **Artifacts**. (GitLab CI: analogicznie, obraz `texlive/texlive`, `latexmk -pdf`.)

## Lokalnie
`cd paper && latexmk -pdf main.tex` (lub `pdflatex main.tex` dwukrotnie — odnośniki).

## Nowy dokument
Skopiuj `paper/` → podmień `tresc/*.tex`, zostaw `formatka/`. Wygląd zostaje spójny.

## Powiązania
[[INSTRUKCJA-Dokumenty-Dialektyczne]] (sekcja „Finał: LaTeX → PDF").
