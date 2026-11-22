---
type: reference
id: R-RYGOR
title: "Rygor proporcjonalny do stawki — poziomy decyzji, koszty, losowy audyt"
status: propozycja
parents: []
author: Arkadiusz Słota
date: 2026-11-01
created_at: 2026-11-01
---

# Rygor proporcjonalny do stawki

> Uzupełnienie reguły nadrzędnej z [AGENTS.md](../AGENTS.md) (*żadnej tezy bez dowodu*). Nie zastępuje jej, tylko odpowiada na jej koszt: dochodzenie do prawdy zużywa czas, compute i uwagę ludzi, a kolejne procedury mogą ograniczać sprawczość bardziej, niż poprawiają decyzje. Źródło: propozycja zewnętrznego recenzenta (2026-11-01), przyjęta do dyskusji przez autora szablonu; status `propozycja`, dopóki nie przejdzie warunku obalenia z §8.

## 1. Zasada

- **Siła wymaganego dowodu rośnie z konsekwencją błędnej decyzji i kosztem jej odwrócenia.** Innego rygoru wymaga pomysł na nową funkcję aktywacji, a innego publikacja zbioru danych, który może zawierać informacje wrażliwe.
- **Hipoteza to nie teza.** Hipoteza nie musi mieć dowodu, ale musi być **jawnie nazwana hipotezą** (`[HIPOTEZA]`, `[INFERENCE]`, status `propozycja`) i mieć warunek obalenia.
- **Poziom rygoru ustalasz przed wynikiem.** Inaczej proporcjonalność staje się wymówką: niewygodny wynik, więc „to jednak mało ważna decyzja”.

## 2. Cztery poziomy

| poziom | kiedy | jak działamy | kto sprawdza | koszt |
|---|---|---|---|---|
| **Eksploracja** | skutek łatwo odwracalny, nic nie wychodzi na zewnątrz | autor próbuje sam, oznacza hipotezy, zapisuje wynik | nikt z góry; tylko losowy audyt (§6) | niski |
| **Weryfikacja** | wynik, na którym ktoś będzie budował | drugi wykonawca sprawdza kluczowe dowody i przypadki graniczne | jeden niezależny recenzent | średni |
| **Decyzja istotna** | zmienia kierunek pracy albo budżet w ramach zatwierdzonego limitu | niezależny audyt, bramki empiryczne z progiem z góry, zatwierdzenie | audytor + właściciel decyzji | wysoki |
| **Decyzja nieodwracalna** | lista z §3 | kontrola człowieka: uprawnienia, skutki, plan awaryjny | człowiek odpowiedzialny | najwyższy |

## 3. Zamknięta lista decyzji nieodwracalnych (zawsze pełny rygor)

Lista jest zapisana z góry i nie wybiera się jej w locie:
1. publikacja (repozytorium publiczne, strona, karta modelu, zbiór danych, wynik liczbowy);
2. usunięcie danych, wag albo historii;
3. płatność i każdy wydatek ponad budżet zatwierdzony z góry;
4. trening albo wydanie na danych o niepewnym statusie prawnym lub z możliwymi danymi wrażliwymi;
5. zmiana kodu, który wykonuje się na cudzej maszynie albo z cudzymi uprawnieniami;
6. zmiana opublikowanej liczby (zawsze z zapisem obu wersji).

Rozszerzyć listę może każdy. Skrócić ją może tylko decyzja na poziomie „nieodwracalna”.

## 4. Poziom wpisany przed działaniem

- Przy każdej decyzji poza eksploracją autor zapisuje **jedno słowo poziomu** przed rozpoczęciem pracy (w zadaniu, notatce albo opisie PR).
- **Podnieść poziom wolno zawsze. Obniżyć tylko z uzasadnieniem i podpisem kogoś innego niż autor.**
- Ocena „to nie wymaga sprawdzenia” to też decyzja. Najgroźniejszy błąd to nie błędna decyzja, tylko błędna ocena, że decyzja nie wymaga weryfikacji, bo psuje sam mechanizm ostrożności i powiela się w kolejnych zadaniach.

## 5. Pięć kosztów przy wyborze poziomu

1. **Compute:** tokeny, GPU, energia.
2. **Czas:** opóźnienia przez komunikację i audyty.
3. **Uwaga człowieka:** ile decyzji wymaga zaangażowania osoby odpowiedzialnej.
4. **Ryzyko:** koszt niewykrytego błędu.
5. **Koszt utraconej okazji:** czego nie zbadano, bo zasoby poszły gdzie indziej.

Poprawność lokalnych decyzji nie gwarantuje optymalności całego programu badawczego: tydzień na udowodnienie mało istotnej tezy to tydzień, w którym wartościowsza hipoteza nie została przetestowana.

## 6. Losowy audyt rygoru

- Co okres (np. tydzień) audytor **niezależny od autorów** losuje N decyzji z poziomów „eksploracja” i „weryfikacja” i ocenia, jaki poziom powinny były mieć.
- Raport: liczba decyzji, które powinny były mieć wyższy poziom, z przedziałem ufności.
- Losowanie jest konieczne. Bez niego system uczy się, że przy zadaniach uznanych za łatwe nikt nie sprawdza pracy.
- N i progi z §8 ustala się przed pierwszym audytem. Przy progu 10 % potrzeba co najmniej ok. 30 decyzji: przy zerze zaniżonych górna granica CI95 wynosi wtedy ok. 3/N (reguła trzech).

## 7. Chroniona niezależność kontroli

- Rola kontrolna (recenzent, bramka) ma **obowiązek przedstawić najmocniejsze uzasadnione zastrzeżenie także wtedy, gdy wszyscy, łącznie z operatorem, popierają rozwiązanie.** Nie musi sprzeciwiać się na siłę, ale nie może być nagradzana wyłącznie za zgodność z grupą.
- System, który dobrze przewiduje oczekiwania jednej osoby, rzadziej przynosi jej obce perspektywy. Przy decyzjach dotykających rzeczywistych ludzi niezależne spojrzenie innych ludzi jest ważniejsze niż symulowana niezależność agentów.

## 8. Warunek obalenia tej zasady

Zasada jest hipotezą, dopóki nie przejdzie dwóch sprawdzeń:
- **Bezpieczeństwo:** próg $p_0$ ustala się z kosztu przeoczenia przed pierwszym audytem (np. 10 %, nie dla każdej stawki ten sam), a liczy się łączne $n$ decyzji z audytów §6, nie liczba audytów. Trzy stany: **górna** granica CI95 odsetka decyzji zaniżonych o poziom $\le p_0$ oznacza wsparcie, **dolna** granica $> p_0$ obalenie (obniżone poziomy wracają w górę, zasadę się poprawia), a pomiędzy wynik jest nierozstrzygnięty i audyty trwają. Warunek na dolnej granicy przechodziłby prawie zawsze przy małym $n$, więc niczego by nie sprawdzał.
- **Sens:** średni czas od pomysłu do zapisanego wyniku na poziomie „eksploracja” spada wobec stanu sprzed zasady. Jeśli nie spada, zasada kosztuje, a nie oszczędza.

## 9. Przykład z praktyki (anonimowo)

Reguła losowania w bootstrapie, zapisana w karcie pomiaru jako „szczegół techniczny”, dała przedziały ufności 1,09–1,32 raza za wąskie, a pokrycie nominalnego przedziału 95 % wyniosło ok. 85 % (symulacja na danych z replikacji). Przeszła przez wszystkie bramki, bo nikt nie uznał jej za decyzję wymagającą sprawdzenia. Złapała ją dopiero zewnętrzna replikacja na pełnym zbiorze. Błąd w zadaniu był mały, a błąd w ocenie stawki przeszedł niezauważony. To argument za §4 i §6.
