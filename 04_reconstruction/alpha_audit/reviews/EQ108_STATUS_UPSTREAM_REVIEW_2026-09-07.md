# Status von (108) vor und nach der diskreten Auswahl — Quellenreview

## Ergebnis

H004 druckt (108) auf Druck S. 330 als Gleichung. Im hier visuell
geprüften Anschluss steht jedoch **keine** Regel, die einen Rest dieser
Gleichung nach einer ganzzahligen Auswahl erlaubt, projiziert oder mit
einer Toleranz versieht. Die Gleichheit steht vielmehr am Ende einer
eingeschränkten Modellkette: Die Externzone wird mit (79b)/(79c) nur in
"überaus guter Näherung" behandelt, der Selektor wird zunächst mit
`delta M + Delta ~ W(vx)` motiviert, und die konkreten Bestimmungsstücke
`f`, `w` und später `F_im`/`A_im` bleiben teilweise unbekannt,
vorgeschlagen oder heuristisch aus Grundzustandsdaten reduziert.

Das rechtfertigt weder, (108) als uneingeschränkte exakte Feldgleichung
auszugeben, noch einen nichtverschwindenden diskreten Rest als von Heim
zugelassene Projektion auszugeben. Die Passage enthält keine explizite
Brücke zwischen diesen beiden Aussagen.

## Quelle und visueller Umfang

Primärquelle H004: Burkhard Heim, *Elementarstrukturen der Materie 2*,
2. unveränderte Auflage (1996), PDF SHA-256
`F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.

Vollseitig visuell geprüft wurden Druck S. 321–330 / PDF 327–336 und
Druck S. 331–335 / PDF 337–341. Das umfasst den verlangten unmittelbaren
Vor- und Nachlauf von (108); OCR diente ausschließlich als Locator.

| Druck / PDF | Inhalt für die Statusfrage | Render |
| --- | --- | --- |
| 321–324 / 327–330 | Strukturprinzip, Externzonen-Näherung, `W`-Aufbau und `A=A(k)` | `tmp/pdfs/book_selection_source/edm2-327.png` bis `edm2-330.png` |
| 325–330 / 331–336 | heuristische `z`-/`A`-Wahl, formaler Generator, (107a,b), (108)/(108a) | `tmp/pdfs/book_selection_source/edm2-331.png` bis `edm2-336.png` |
| 331–335 / 337–341 | Status von `F_im`, `w`, Grenzwerten sowie `A_im` und `Y_k` | `tmp/pdfs/a16_book/edm2-337.png` bis `edm2-341.png` |

Keine neue Numerik, keine Änderung der Eingaben und keine Aussage über
nicht gelesene Buchstellen erfolgten.

## Gedruckte Einführungs- und Gleichheitskette

1. Druck S. 322 / PDF 328 erklärt die äußere Zone `j=4` bei den
   betrachteten physikalischen c-/d-Strukturen für in "überaus guter
   Näherung" dem dritten Gültigkeitsbereich `tau -> 0` zugehörig. Für
   diese Zone wird daher die Gültigkeit von (79b)/(79c) und ein Verlauf
   `mu_+ exp(-A N_(4))` angeführt. Das ist die explizite
   Näherungsannahme am Externterm.

2. S. 323 / PDF 329 schlägt
   `Delta=mu_+(exp(-A N_(4))-1)` vor und formuliert
   `delta M+Delta ~ W(vx)` als Auswahlprinzip. Erst *bei Verwendung von*
   `mu_+` als Proportionalitätsfaktor schreibt der Text
   `mu_+ W=delta M+Delta` und daraus den dimensionslosen `W`-Ausdruck.
   Der Text trennt damit die motivierende Proportionalität von der
   anschließenden normierten Darstellung; keine Resttoleranz steht dort.

3. S. 324–325 / PDF 330–331 verbindet den Exponent erneut mit
   (79b)/(79c), nennt `A=A(k)`, und gewinnt für den
   Protosimplexgenerator nach einer möglichen ganzzahligen Auswahl
   `z=1,3,5` die Wahl `z=3` oder `z=5` ausdrücklich heuristisch. Die
   Eigenschaft `(2 xi-1)^2=5` legt laut Text heuristisch `z=5` und für
   `k=1` `Q_4 A=1/3` nahe; dann wird
   `3 Q_4 A(k)=2k-1` und die Generatordarstellung mit Gleichheitszeichen
   hingeschrieben. Das ist kein allgemeiner Herleitungsbeweis eines
   abweichenden `A=1/5`-Zweigs.

4. S. 327 / PDF 333 erweitert die Gleichung mit `F(N)>=1`, `F=1+f(N)`,
   `f(0)=0`, `f(N)>0` für `N>0`. Dort heißt es konditional: *Wenn* `W`,
   die Strukturpotenz `w` und `f` auf die Quantenzahlen zurückgeführt
   werden können, wäre die kubische Beziehung eine Auswahlregel der
   zulässigen P4-Gitterpunkte. Das ist kein nachträglicher
   Gleichungs-zu-Ganzzahl-Projektor.

5. S. 330 / PDF 336 druckt schließlich

   ```text
   alpha1*N1^3 + alpha2*N2^2 + alpha3*N3
     + exp[-(2k-1)*N4/(3Q4)] = W(vx)*(1+f(N)),       (108)
   W(vx)=g(k,q)*w(vx).
   ```

   Der Absatz nennt `f` und `w` zugleich "noch unbekannte
   Bestimmungsstücke" und gibt nur Eigenschaften in (108a) an, darunter
   `f(N>=0)>=0`, `delta_N f>0`, `delta_N N=1`, `0<=N<=L_N<infinity`, die
   angezeigte Form von `w`, `w=w*` und unterstrichenes `w_k(n_j=0)=0`.
   Die Gleichheit ist im gedruckten Selektormodell also formell, nicht
   mit einem `+/-`-Rest versehen. Die Eigenschaften erlauben keine
   sichtbare, freie Verschiebung der Gleichung nach einer Auswahl.

## Unbekannte Funktionen, empirische Reduktion und `Y_9`

- Auf S. 330–331 / PDF 336–337 wird `w` den Quantenzahlen und
  metronischen R3-Selektorfunktionen `F_im(mu_s)` zugeordnet. Die Form
  von `F_im` könne "vorläufig nicht deduziert" werden; die Existenz wird
  anschließend als Bedingung akzeptiert. Das ist ein Quellenstatus der
  Konstruktion, keine gedruckte Residualregel für (108).
- S. 333–334 / PDF 339–340 sagt für `F_im` und `F` Konvergenz gegen
  endliche reelle Grenzwerte. Der Satz, der Approximationsfehler liege
  "mit Sicherheit weit unter der Meßbarkeitsgrenze", bezieht sich auf
  diese Grenzwertsubstitution in beobachtbarer R3-Umgebung und gilt
  ausdrücklich nur, sofern `A_im` und `A` richtig bestimmt werden. Er
  beziffert weder eine Abweichung der linken und rechten Seite von (108)
  noch eine zulässige Änderung eines gewählten `N_j`.
- S. 335 / PDF 341 sagt, `F_im` sei bislang nicht explizit herleitbar;
  damit gelte dies auch für `A_im` und `A_66`. Unter Verwendung
  empirischer Grundzustandsdaten könnten die Koeffizienten heuristisch
  auf Grenzwerte und Kopplungskonstanten zurückgeführt werden. Die
  auftretenden Unsicherheitsfaktoren werden mit `Y_k`, `k>3`, bezeichnet;
  die sichtbare Zeile für `A_16` enthält konkret `Y_9`.

Diese Aussagen qualifizieren die Herkunft der Koeffizienten. Sie sagen
nicht, dass `Y_9` oder ein anderer Faktor nach Kenntnis einer
Ganzzahlabweichung gewählt werden darf, und sie definieren keine
Resttoleranz für (108).

## Begrenzter Nichtfund und Konsequenz für die Anschlussdiagnose

In den vollseitig geprüften Druckseiten 321–335 wurde keine der folgenden
Anweisungen gefunden:

- eine quantitative Restgrenze für (108),
- eine Projektion von einem reellen Gleichheitswert auf ein nahes
  ganzzahliges `N_j`-Quadrupel,
- eine Regel, die nach einer TRC-/Sättigungsentscheidung die Differenz
  beider Seiten von (108) vernachlässigt oder kompensiert,
- eine Anweisung, ein `Y_k` zur Beseitigung eines solchen Restes zu
  bestimmen.

Das ist ein lokaler Nichtfund. Er beweist weder, dass außerhalb dieses
Umfangs keine Ergänzung existiert, noch eine Autorenabsicht oder einen
globalen Fehler. Für die bisherige eigene Sättigungsdiagnose folgt nur:
Die Quellenseite stützt die diskrete Auswahlstruktur und die formale
Gleichheit jeweils in ihrem erläuterten Modellrahmen; sie liefert hier
keine gedruckte Erlaubnis, einen verbleibenden eigenen Skalarrest als
zulässige Projektion zu behandeln.
