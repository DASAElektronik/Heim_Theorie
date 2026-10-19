# `xi` und der Rückverweis (96b) — Quellenreview (2026-09-06)

## Ergebnis und enger Umfang

Der Rückverweis von II 325 auf (96b) hat eine konkrete, im Buch sichtbare
Kette. `xi` entsteht dort aus einem positiven Grenzverhältnis einer
vorgeschlagenen metronischen Funktion `F`, kombiniert mit dem eingeführten
Kreationsselektor bzw. der Fibonacci-Rekurrenz. Die Gleichung

```text
xi^2 - xi = 1,     xi > 0,     daher 2 xi = 1 + sqrt(5)
```

ist in dieser Kette eine Buchalgebra; folglich ist auch
`(2 xi - 1)^2 = 5` ihre unmittelbare algebraische Konsequenz. Die Kette
beginnt aber nicht mit einer ausformulierten Lösung eines Feldproblems:
Die Existenz/Form der Funktion `F(nu)` und ihr Anschluss an das `(+7)`-
Feld werden im Text ausdrücklich als mögliche bzw. spekulative Annahmen
eingeführt. Die Zahl 5 ist somit in dieser Darstellung nicht frei gewählt,
aber ihr Auftreten trägt die vorausgehenden Hypothesen.

Geprüft wurde ausschließlich EDM II, Druck S. 246–251 / PDF 252–257,
einschließlich des für (96b) nötigen unmittelbaren Kontextes. Das ist kein
Gesamtwerk-Nichtfund und keine Prüfung späterer Fassungen oder einer
Massen-/Sensitivitätsrechnung.

## Quelle und Sichtprüfung

Primärquelle H004: Burkhard Heim, *Elementarstrukturen der Materie 2*,
zweite unveränderte Auflage (1996), lokale Datei SHA-256
`F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.

Vollseitig visuell geprüft:

- Druck 246–251 / PDF-Folios 252–257;
- Render: `tmp/pdfs/xi_origin/edm2-252.png` bis `edm2-257.png`.

OCR diente nur zur Navigation; die hier aufgeführten Formeln und
Qualifikationen wurden am Bild kontrolliert.

## Die sichtbare Kette

| Stelle | Gedruckter Schritt | Status |
| --- | --- | --- |
| II 246–247 / PDF 252–253 | `k=0` wird ausgeschlossen, weil dann kein synmetronischer Grundfluß existiere, der `(+7)` im Sinn c oder d verursache. Die folgende Diskussion ordnet das äußere R3-Ladungsfeld und Konjunktive den d-Strukturen zu. | Kontext für die `(+7)`-Feldrolle; noch keine `xi`-Definition. |
| II 248 / PDF 254 | Für eine variable Größe `u=K` heißt es, man **könnte spekulativ annehmen**, dass eine metronische Funktion `F(nu)` eine metaphorische „Oberfläche“ des Ladungsfeldes über R3-Zellen `nu=z` und `nu=z-1` definiere. Das R3-Strukturfeld `(+7)` wird dabei über Potentiale `W_j` angesprochen. | Explizit hypothetischer Ausgangspunkt für `F`. |
| II 248–249 / PDF 254–255 | Unter Verwendung von (79b) und (79c) darf für diese Funktion `F ~ 1/psi ~ exp(alpha r(nu))` gesetzt werden; der Text verbindet `nu -> infinity` mit `delta r -> beta=const>0`. | Quellenbehauptete, asymptotische Form; keine unabhängige exakte Definition von `F`. `nu` ist hier nicht der spätere Konfigurationsindex `k`. |
| II 249 / PDF 255 | Nach Potentialindizierung und metronischer Integration steht ein Verhältnis `F(z):F(z-1)` in `K`. Direkt danach wird der Kreationsselektor `delta^2 phi - 3 delta phi + phi = 0` eingeführt und als `phi(n)=phi(n-1)+phi(n-2)` ausgeschrieben; die daraus aufgebaute Klasse heißt Fibonacci-Reihen. | Der Text stellt diese Rekurrenz als Selektorbedingung für die betreffende Klasse dar. |
| II 250 / PDF 256 | Mit `F(r)=F(r-delta r)+F(r-2 delta r)` und dem Exponentialansatz bildet der Text den positiven Grenzwert `xi=lim F(r):F(r-delta r)`. Er erhält `xi=1+1/xi`, also `xi^2-xi=1`; wegen `0<xi<infinity` werde nur der positive Zweig betrachtet: `2xi=1+sqrt(5)`. | Direkt gedruckte Herleitung und positive Zweigwahl. |
| II 250 / PDF 256 | Beim Übergang der d-Internstruktur in R3 über das durch (79b)/(79c) beschriebene `(+7)`-Feld liege `z` sehr hoch; deshalb dürfe für das unbekannte Verhältnis `F(z):F(z-1)=xi` gesetzt werden. Anschließend steht `K=A xi eta^2(1-sqrt(eta))` mit einer frei verfügbaren Konstanten `A>0`. | Der Anschluss an `xi` ist eine sehr-gute-Näherungssetzung für ein zuvor unbekannt genanntes Verhältnis, nicht eine exakt definierte Feldlösung. |
| II 251 / PDF 257, (96b) | Die abschließende Zeile enthält erneut `2xi=1+sqrt(5)` innerhalb der Korrekturformel. In ihrem unmittelbaren Kontext stehen außerdem `beta≈1`, eine zur Elektronenempirie „optimal angepaßte“ Proportionalitätssetzung sowie später die Einsetzung `Y_2=1`. | (96b) übernimmt `xi`; diese zusätzlichen Annahmen gehören zur dortigen korrigierten Massenrelation, nicht zur bloßen quadratischen Identität für `xi`. |

## Bedeutung für den späteren Verweis auf 5

Der auf II 325 benutzte Ausdruck `(2xi-1)^2=5` folgt aus der auf II 250
und erneut in (96b) gedruckten positiven Lösung. In diesem engen Sinn ist
der Verweis auf 5 quellenintern nachvollziehbar und keine nachträgliche
numerische Erfindung.

Er zwingt für sich allein jedoch nicht die spätere Wahl eines bestimmten
`z`-Kandidaten oder einer Abklingkonstante `A(k)`: II 250 verwendet ein
lokales `A>0` als frei verfügbare Konstante in `K`; II 325 verwendet `A(k)`
in einem anderen Externzonen-/Selektorausdruck. Eine Gleichung dieser beiden
`A`-Rollen wurde im hier geprüften Rückverweis nicht gefunden. Ebenso wird
keine Gleichsetzung mit `A16`, `F_im`, `F_S` oder einer späteren
Massennormalisierung behauptet.

## Belegt, Annahme, offen

- **Belegt:** Fibonacci-Rekurrenz, positive Auswahl von `xi`, die Formel
  `2xi=1+sqrt(5)`, ihr Wiederauftreten in (96b), und der gedruckte
  `(+7)`-/R3-Übergang als Motivationskontext.
- **Als Annahme bzw. Näherung bezeichnet:** die angenommene metronische
  Funktion `F(nu)`, ihre Beziehung `F~1/psi`, und die hohe-`z`-Ersetzung
  des unbekannten Quotienten durch `xi`.
- **Offen im Umfang:** eine vollständige Feldgleichung/Randbedingung, die
  `F` eindeutig erzeugt; ein Fehlermaß der hohen-`z`-Näherung; eine
  quellenbelegte Identität zwischen dem hier verwendeten `A` und späterem
  `A(k)`; sowie jede daraus abgeleitete Mess- oder Massenbewertung.

Keine Eingaben, älteren Reviews oder Originaldateien wurden verändert.

## Nachtrag: Band-I-Anker zum Selektorstatus

Nach dem anfänglichen Band-II-Review wurden eng ergänzend Band I,
Druck S. 125–126 / PDF 131–132, visuell geprüft. Quelle H003 hat die
SHA-256 `49C79028C4F5B4FEE97F0541EF1655C37755C3C3C2FD3A10DD6E72CB454DE459`;
geprüfte Render sind `tmp/pdfs/xi_selector/edm1-131.png` und
`tmp/pdfs/xi_selector/edm1-132.png`.

Diese beiden Seiten präzisieren den Status der in II 249 verwendeten
Rekurrenz:

- I 125 / PDF 131 erklärt eine Selektorgleichung allgemein als ein
  **System von Bedingungen**, das aus einer unendlichen Mannigfaltigkeit
  denkbarer metronischer Funktionen eine Schar auswählt. Als Beispiel
  stehen Fibonacci-Folgen `a_n=a_(n-1)+a_(n-2)` mit streng steigenden,
  positiven aufeinanderfolgenden Gliedern und endlichem positivem
  Quotienten.
- I 126 / PDF 132 leitet aus genau dieser Rekurrenz die
  Selektorgleichung `delta^2 phi-3 delta phi+phi=0` her und nennt sie
  Kreationsselektor. Der Text leitet sie also aus der Rekurrenz ab;
  er behauptet nicht, dass sie als universelles Gesetz bereits aus einem
  Exponentialwachstum folge.
- Dieselbe Seite begründet den Grenzwert des Folgeverhältnisses mit dem
  im Beispiel genannten monotonen Wachstum und erhält daraus
  `xi=1+1/xi`, `xi^2-xi=1` und den positiven Zweig. Unabhängig davon ist
  bei positiven Startwerten die Fibonacci-Rekurrenz selbst eine saubere
  mathematische Grenzwertgrundlage: ihre Quotienten konvergieren zum
  positiven charakteristischen Wurzelwert. Diese letzte Aussage ist
  elementare Rekurrenzalgebra unsererseits, nicht eine zusätzliche
  Autorenbehauptung.

Der Band-I-Anker verstärkt damit die Aussage „Fibonacci-Selektor“ in der
Herkunftskette, ohne die in II 248–250 ausdrücklich hypothetische
Funktion `F(nu)`, den `(+7)`-Feldanschluss oder die hohe-`z`-Näherung in
eine vollständige Feldherleitung umzudeuten.
