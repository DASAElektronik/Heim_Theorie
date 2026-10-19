# Externe Exponentialnäherung und `N_(4)` — Quellenreview (2026-09-06)

## Auftrag und Ergebnis

Dieser enge Review verfolgt nur die Brücke von EDM II (79)/(79b)/(79c),
Druck S. 175–179, zu der äußeren `j=4`-/`N_(4)`-Verwendung auf S. 322–324.
Die Quelle stellt eine **bedingte, näherungsweise Formbrücke** her: Für die
äußere Sigma-Zone soll die dritte Gültigkeitsregion und damit die
Exponentialnäherung gelten; daraus wird ein Term `mu_+ exp(-A N_(4))` in
einen dimensionslosen Selektor `W` überführt. Sie druckt in diesem Umfang
jedoch weder `r=N_(4)` noch `alpha=A`, noch eine Gleichheit der Amplitude
von (79) mit `mu_+` oder `W`.

Damit ist eine Parameter-, Skalen- oder Fehlerfortpflanzung von der
räumlichen Näherung zu einem `N_(4)`-Auswahlwert nicht quellenrein
geschlossen. Das ist ein lokaler Nichtfund im nachstehend genannten
Seitenumfang, keine Aussage über das Gesamtwerk.

## Visuell geprüfte Primärstellen

Primärquelle H004: Burkhard Heim, *Elementarstrukturen der Materie 2*,
2. unveränderte Auflage (1996), lokale PDF SHA-256
`F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.

Vollseitig geprüft wurden Druck S. 175–179 / PDF 181–185 sowie Druck
S. 322–324 / PDF 328–330. Renderpfade:

- `tmp/pdfs/external_approximation/edm2-181.png` bis `edm2-185.png`
- `tmp/pdfs/external_approximation/edm2-328.png` bis `edm2-330.png`

Die bereits vorhandenen Berichte `EXPONENTIAL_CONTEXT_2026-09-06.md` und
`EXPONENTIAL_SOURCE_REVIEW_2026-09-06.md` wurden vorab gelesen. Ihre
skalare Groß-`r`-Asymptote und Restschranke werden hier **nicht** als neuer
Befund wiederholt; sie betreffen eine ausdrücklich eigene skalare
Normalisierung von (79), nicht schon den folgenden `N_(4)`-Anschluss.

## Gedruckte Kette

| Stelle | Sichtbarer Inhalt | Status für den Anschluss |
| --- | --- | --- |
| II 175–177 / PDF 181–183, (79) | Die Lösung enthält `exp(lambda_kl mu)` mit tensoriellem Vorfaktor und einer von `mu`, `T`, `K=lambda_kl T`, `a` und `lambda_kl` abhängigen Klammer. | Ausgangsform; weder `N_(4)` noch `mu_+`/`W` an dieser Stelle. |
| II 178–179 / PDF 184–185, (79b), (79c) | Für `tau -> 0` steht `lim(mu;n)=r`; bei großem `r` wird `psi(r) ~ exp(-alpha r)`, `alpha>0`, angegeben. (79c) druckt `r=r(nu)`, `delta r -> beta=const>0`. | Räumliche asymptotische Form in der dritten Gültigkeitsregion. `nu` wird hier nicht mit dem späteren Konfigurationsindex `k` gleichgesetzt. |
| II 322 / PDF 328 | Die äußere Zone `j=4` aller physikalischen c-/d-Strukturen sei so beschaffen, dass die dritte Gültigkeitsregion `tau -> 0` „in überaus guter Näherung“ gelte. Für die Sigma-Zone werde deshalb die Gültigkeit von (79b)/(79c) angeführt und ein Verlauf `mu_+ exp(-A N_(4))` benutzt; bei `N_(4)=0` am V6-Referenzpunkt ist er `mu_+`. | Explizite kontextuelle Anwendung der Näherung auf die äußere Zone; noch keine gedruckte Variablenidentifikation. |
| II 323 / PDF 329 | Es wird `Delta = mu_+ exp(-A N_(4))-mu_+ = mu_+(exp(-A N_(4))-1)` gebildet. Der Text nennt `delta M+Delta ~ W(vx)` als Auswahlprinzip und setzt bei Verwendung von `mu_+` als Proportionalitätsfaktor `mu_+ W=delta M+Delta`. Daraus folgt ein `W` mit Endterm `exp(-A N_(4))-1`; nach den folgenden Differenzidentitäten steht `exp[-A(n_4+Q_4)]` im ausgeschriebenen Selektorausdruck. | Eine quellenseitige Baselinesubtraktion und bedingte Normierung des `N_(4)`-Terms in `W`; kein Nachweis einer absoluten Feldamplitude aus (79). |
| II 324 / PDF 330 | Direkt anschließend heißt die Abklingkonstante im `W`-Term `A=A(k)`; ihre `k`-Abhängigkeit wird mit verschiedenem `Q_4` für `k=1,2` begründet. Die exponentielle Besetzung der punktförmigen Sigma-Zone wird erneut mit (79b)/(79c) und der dritten Gültigkeitsregion verbunden. | Positiver Beleg für eine spätere, k-abhängige `A`-Rolle; keine gedruckte Gleichung `A=alpha` oder `r=N_(4)`. |

## Was die Quelle tatsächlich normiert

Die Passage S. 322–323 liefert mehr als eine bloße Formähnlichkeit:

1. Sie verwendet `N_(4)=0` als Referenz, bei der der **unnormierte** Term
   `mu_+ exp(-A N_(4))` den Wert `mu_+` hat.
2. Sie subtrahiert gerade diesen Referenzwert und nennt die Differenz
   `Delta`.
3. Bei der ausdrücklich konditional formulierten Wahl von `mu_+` als
   Proportionalitätsfaktor erhält `W` den dimensionslosen Anteil
   `exp(-A N_(4))-1`.

Dies ist keine quellenbelegte Aussage `H(0)=1` für eine separat definierte
Skalarfunktion: `H` und jene Normalisierung gehören zum späteren
Diagnosemodell, nicht zur Buchnotation. Ebenso folgt daraus nicht, dass
der vollständige (79)-Präfaktor exakt `mu_+` ist. Der Text verwendet
`mu_+` hier als den gewählten Proportionalitätsfaktor der
Auswahlgleichung.

## Nicht gedruckte Identifikationen und Fehlerrahmen

Im geprüften Anschluss fehlen insbesondere:

- eine Gleichung oder Umrechnungsregel `r=N_(4)` (auch keine sichtbare
  affine oder skalenbehaftete Variante);
- eine Gleichung `alpha=A`; `alpha` bezeichnet in (79b) die räumliche
  Abklingrate, während S. 324 `A=A(k)` für den Selektorterm schreibt;
- eine Gleichung zwischen dem tensor-/feldseitigen Vorfaktor von (79) und
  `mu_+`, `Delta` oder `W`;
- ein quantitatives Fehlermaß für die auf S. 322 als „überaus gute
  Näherung“ bezeichnete Übertragung: kein Schwellenwert für `r` oder
  `nu`, keine Skala zwischen radialem Schritt und `N_(4)`, keine
  Amplitudenunsicherheit und keine Restungleichung.

Die Buchpassage erlaubt daher nicht, eine aus einer eigenen skalarisierten
(79)-Restschranke gewonnene Zahl automatisch als Fehler von
`exp(-A N_(4))`, `Delta` oder `W` auszugeben. Auch die einfache Schranke
`0 < exp(-A N_(4)) <= 1` wäre nur unter zusätzlich gesicherten
Vorzeichenannahmen `A>=0`, `N_(4)>=0` eine algebraische Bereichsaussage;
sie ist keine Abschätzung des Näherungsfehlers.

## Präzise Reichweite

Als Autorenbehauptung ist die Anwendung von (79b)/(79c) auf die äußere
Sigma-Zone und die nachfolgende `W`-Normierung belegt. Als eigene, nicht
quellenbelegte Ergänzung blieben jede konkrete `r`-zu-`N_(4)`-Zuordnung,
jede Gleichsetzung der beiden Abklingparameter, eine absolute
Feldnormalisierung und ein numerisches Fehlerbudget. Es wurde weder eine
Massenrechnung noch ein Fit durchgeführt und keine Formel still
korrigiert.
