# Bramka na ramę i zewnętrzność (notatka robocza)

> Warstwa głębiej niż [[Katalog-Grzechow-Rozumowania]]. Zapis rozważań do kontynuacji.
> Uwaga uczciwa: framingi poniżej są autorstwa LLM (RLHF-stronniczy ku zgodzie).
> Waż je asymetrycznie: **niezgodę modelu traktuj ciężej niż jego zgodę**.

## Problem

Masz dwie bramki na **twierdzenia**: epistemiczną (rozumiem, nie papuguję) i empiryczną
(warunek obalenia). Brakuje bramki na **ramę**. Dialektyka steelmanuje antytezę *wewnątrz*
ramy, nigdy konkurencyjnego paradygmatu. Aparat jest ślepy na błędy, których rama nie umie
nawet zadać jako pytania.

## Twarde ustalenia

1. **Konwergencja to czujnik dymu, nie meta.** „Wszystko się spina" jest pojedynczym
   zdarzeniem poznawczym najbardziej wartym nieufności. Czasem to realny atraktor, ale musi
   sobie na to zasłużyć (przetrwać atak na ramę), tak jak synteza zasługuje przetrwaniem testu.
2. **Kompletnej automatycznej bramki-na-ramę NIE DA SIĘ zbudować.** Self-reference wall:
   cokolwiek w pełni zautomatyzujesz, w pełni wyspecyfikujesz, a co specyfikujesz, jest wewnątrz
   ramy i dziedziczy jej ślepe plamy. Rok szukania „tego mechanizmu" zawiódł, bo szukał rzeczy
   buildowalnej, a ta rzecz jest **społeczna**.
3. **Sprzeciw ≠ zewnętrzność.** Anty-Ty to Ty z odwróconym znakiem (ta sama oś, ten sam
   słownik, te same pytania), więc maksymalnie wchłanialny. Marker prawdziwej zewnętrzności to
   **obojętność, nie opór**: rama, która nie wie, że istniejesz, i przejmuje się innymi pytaniami.
4. **Zewnętrzność daje tylko agent z własną stawką** → ludzie + publikacja, nie gadżet.
   Recenzent optymalizuje pod siebie, narzędzie optymalizuje pod Twój spec.
5. **Architektura jest warstwowa:** tani automat łapie ~80% błędów ramy, rzadki człowiek
   (Slayer) łapie ogon, którego automat strukturalnie nie widzi. Automat nie zastępuje ludzi,
   tylko zwiększa zasięg, żeby rzadka obcość szła dalej.
6. **LLM (w tym ja) = tani, częściowy importer ram, ale RLHF-stronniczy ku zgodzie.**
   Świeży kąt = sygnał; stałe „tak, i..." = szum. Zauważasz sygnał, wchłaniasz szum.

## Mechanizmy na te 80% (każdy = HIPOTEZA z własnym testem)

- **Frontier jako enumerator ram, nie walidator.** Adwersarialnie: „wymień 5 tradycji, które
  uznałyby to za źle postawione, i ich najmocniejszy kontrargument". *Test: czy daje coś,
  czego sam bym nie wymyślił?*
- **Własny consistency-validator wycelowany NA ZEWNĄTRZ.** Lint spójności po heterogenicznym
  korpusie zewnętrznym; niezgoda niezależnych źródeł = pęknięcie ramy. *Test: precision/recall
  na wstrzykniętych sprzecznościach.*
- **Rekomender odległości ramowej.** Ściągaj rzeczy o niskim podobieństwie do mojego ramowania,
  a wysokiej trafności tematycznej (odwrotność normalnego rekomendera). Systematyzacja
  szczęśliwego trafu z .pdf. *Test: hit-rate użytecznych ataków vs szum.*

## Pytania do siebie (tripwire + katapulta, NIE ucieczka)

Detekcja: *Czy ostatnio cokolwiek mnie zaskoczyło, czy tylko potwierdzało? Co musiałoby być
fałszem, żeby się NIE spięło? Ile czasu szukałem dowodów PRZECIW vs ZA?*
W-ramie: *Czy moja alternatywa używa mojego słownika (= moja rama z minusem)? Kto rozwiązuje
to, nie wiedząc, że istnieję? Które pytanie uważam za głupie (tam siedzi cudza rama)?*
Realność: *Ta zgoda przyszła od kogoś z własną stawką, czy od narzędzia pod mnie? Jaka najleniwsza
istniejąca rzecz już to robi i czemu jej nie biorę?*
Katapulta: *Co najmniejszego odpalę DZIŚ, co może wyjść źle? Kogo z imienia zapytam w tym tygodniu?*

**Pytanie-kręgosłup:** czy moja ostatnia godzina wyprodukowała MYŚL, czy RZECZ, którą świat
może odrzucić? Podpis pętli = rosnąca głębia + znikający artefakt. Jeśli myśl, wyjdź do rzeczy.

## Falsyfikowalny pierwszy krok (katapulta dla tego wątku)

Idea zbieżna: mikro-model z dokumentów jako „lepszy index.md" dla systemów agentycznych.
Jakość modelu = funkcja jakości docsów (dane nie wnioskują o sobie), więc to downstream
dyscypliny bramek. Granica: może wydobyć strukturę utajoną (realna generalizacja), nie może
wytworzyć nowej prawdy.

Pierwsze liczby zamiast kolejnej godziny rozważań:
- **held-out link recovery:** odłóż część `[[linków]]`/syntez, trenuj na reszcie, sprawdź czy
  mikro odzyskuje odłożone relacje lepiej niż płaski index + retrieval i niż frontier. Odzyskuje
  niewidziane → zgeneralizował. Nie → zapamiętał (wierszyk).
- **consistency-F1:** wstrzyknij znane sprzeczności, zmierz wykrycie. Spójność ≠ prawda
  (korpus może być spójnie fałszywy) — to druga bramka, komplementarna, nie zamiennik.
- **ściana danych:** korpus docsów jest malutki → ryzyko memoryzacji zamiast generalizacji.
  Dźwignie: model na tyle mały, że musi kompresować; augmentacja (frontier jako generator, nie
  źródło prawdy); mierz memoryzację wprost.

## Warunek obalenia tej notatki

Jeśli istnieje sposób na **kompletną** automatyczną bramkę-na-ramę (bez agenta z własną stawką),
punkt 2 i 4 są błędne i notatkę trzeba przepisać. Dotąd: brak takiego mechanizmu = teza trzyma.
