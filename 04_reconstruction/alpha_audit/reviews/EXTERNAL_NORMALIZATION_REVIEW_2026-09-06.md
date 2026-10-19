# Externzone: Referenz, Normierung und Buchgleichung (108)

Stand: 2026-09-06. Eng begrenzte Quellenreview von H004 Druck 322--330 /
PDF 328--336 mit den unmittelbar benannten Rueckverweisen (79b/c),
(98b)--(98e) sowie dem auf Druck 325 gelesenen Verweis auf (96b). Die
Originalseite von (96b) wurde in dieser Etappe nicht neu visuell gelesen.
Keine Masse, kein Y9-Fit und keine Aenderung der kanonischen Eingaben.

## 1. Kurzergebnis

Die Buchpassage laesst nicht pauschal eine Normierung offen. Sie legt drei
verschiedene Bezugsschritte explizit fest:

1. Der **leere** `R3` ist `N_(j)=0`, also `n_j=-Q_j`. Der vorgeschlagene
   Externzonenbeitrag wird durch Subtraktion seines Wertes bei `N_(4)=0`
   auf diesen Bezug normiert.
2. Die **Gerueststruktur** ist `n_j=0`, also `N_(j)=Q_j`. An diesem anderen
   Punkt definiert das Buch den Basisanstieg `g(k,q)`.
3. Die Resonanzordnung `N=0` setzt die Anregungsfunktion `f(0)=0`, legt aber
   fuer sich allein weder `n_j=0` noch `N_(j)=0` fest.

Die Skala ist ebenfalls sichtbar: `mu_+` multipliziert die dimensionslose
Auswahlgroesse `W`; Druck 323 schreibt `mu_+ W=delta M+Delta`. Offen bleibt
nicht diese algebraische Amplituden-/Referenzwahl, sondern die Herleitung
des Uebergangs vom raeumlichen Naeherungsverlauf (79b/c) zum diskreten
Besetzungsverlauf `exp[-A N_(4)]` samt Fehlerkontrolle. Das spaeter
eingesetzte `A(k)` wird auf Druck 324--325 heuristisch gewaehlt, nicht aus
einer der beiden auf Druck 178 mit `alpha` beziehungsweise `A`
bezeichneten raeumlichen Groessen deduziert.

Eine veraenderte Externzonenfunktion darf deshalb nicht nur im linken
`N_(4)`-Term ausgetauscht werden. Derselbe Funktionswert am Geruestpunkt
`N_(4)=Q_4` steckt in `g` und damit in `W=g w`.

## 2. Quelle und Sichtumfang

H004:

`01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf`

SHA-256:
`F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.

Vollstaendig visuell gelesen:

- Druck 322--330 / PDF 328--336:
  `tmp/pdfs/coupled_existence/edm2-328.png` bis `edm2-336.png`;
- Druck 277--278 / PDF 283--284, (98b)--(98e):
  `tmp/pdfs/book_pseudosinglet/edm2-283.png` und `edm2-284.png`;
- Druck 178--179 / PDF 184--185, (79b/c):
  `tmp/pdfs/exponential_context/edm2-184.png` und `edm2-185.png`.

Die PDF-Textschicht und vorhandenen Reviews dienten nur der Navigation;
die tragenden Gleichungen, Indizes und Bezugspunkte wurden an den
Vollseiten gelesen. (96b) wurde nur in der Anwendung/Rueckverweisung auf
Druck 325 erfasst, nicht an seiner eigenen Gleichungsseite gegengelesen.

## 3. Der leere Bezugspunkt und `mu_+`

Druck 322 setzt

```text
N_(j)=n_j+Q_j>=0.
```

Das Minimum `N_(j)=0`, also `n_j=-Q_j`, bezeichnet dort den leeren `R3`
und den irrealen `V6`-Bezugspunkt. Das ist gerade **nicht** die spaeter
verwendete Geruestbelegung `n_j=0`.

Fuer die Externzone `j=4` beruft sich der Text auf die Approximationen
(79b)/(79c) und setzt den Verlauf

```text
mu_+ exp[-A N_(4)].
```

Bei `N_(4)=0` ist sein Wert `mu_+`. Daher wird als Differenz zum leeren
Bezug vorgeschlagen:

```text
Delta = mu_+ exp[-A N_(4)]-mu_+
      = mu_+{exp[-A N_(4)]-1}.
```

Dies ist eine ausdrueckliche Endpunktnormierung `Delta(0)=0`. Sie ist eine
Quellenannahme, keine aus (79b/c) bewiesene Erhaltungsgleichung.

Druck 278, (98d), schreibt die Masse bereits als

```text
M(c,d)=mu_+ [dimensionslose Klammer].
```

Druck 323 verwendet dann `mu_+` als Proportionalitaetsfaktor:

```text
mu_+ W = delta M+Delta.
```

Damit ist `W` in dieser Konstruktion dimensionslos. Druck 329 gibt fuer
die Externzonen-Anregungsstufe ausserdem `mu_+ c^2 ~= 9.28717 keV` an.
Die gepruefte Passage verwendet `mu_+` somit als bereits eingefuehrte
Massenskala und liefert einen Energiewert; sie leitet die fundamentale
Skala auf diesen Seiten nicht neu her.

## 4. Warum in (108) kein sichtbares `-1` bleibt

Nach Division durch `mu_+` steht auf Druck 323 zunaechst

```text
W = sum_j alpha_j delta_j G_j + ... + exp[-A N_(4)]-1.
```

Unmittelbar danach setzt die Quelle `alpha_4=1` und
`delta_4 G_4=1`. Der konstante `j=4`-Beitrag hebt daher das `-1` der
externen Referenzdifferenz auf. Erst nach dieser Kompensation folgt

```text
alpha_1 N_(1)^3 + alpha_2 N_(2)^2 + alpha_3 N_(3)
+ exp[-A N_(4)] = W.
```

Die reine Exponentialform ist somit buchintern an die Kombination aus
Referenzsubtraktion, `alpha_4=1` und `delta_4G_4=1` gebunden. Das ist mehr
als eine nackte, unnormierte Einsetzung; es ist aber weiterhin nur so
belastbar wie der vorgeschlagene Externzonenansatz.

## 5. Wie `A` tatsaechlich festgelegt wird

Druck 324 trennt den diskreten Parameter von der frueheren raeumlichen
Formel. `A=A(k)` soll wegen der verschiedenen `Q_4(k)` nur von `k`
abhaengen. Fuer den Sigma-Term sei der zuvor gebrauchte Selektorgrenzwert
nicht verfuegbar; der Text sagt deshalb ausdruecklich, `A` bleibe ungleich
`ln xi`.

Druck 178 verwendet dabei zwei auseinanderzuhaltende Groessen mit
ueberlappender Symbolik. In der Extremumbedingung steht zunaechst

```text
alpha = lambda_(kl)/a = A;
```

das dortige grosse `A` ist also die Abkuerzung des Quotienten. Am unteren
Seitenende wird der asymptotische Verlauf dagegen als

```text
exp[(lambda_(kl)-a)r] = exp(-alpha*r)
```

geschrieben; der dortige positive **Abklingexponent** ist demnach
`alpha=a-lambda_(kl)`. Weder das Quotienten-`A` der Extremumbedingung noch
dieses spaetere Abkling-`alpha` wird auf Druck 324--325 mit dem diskreten
`A(k)` in `exp[-A(k)N_(4)]` gleichgesetzt.

Die anschliessende Festlegung auf Druck 325 erfolgt in Annahme- und
Heuristiksprache:

- Fuer `k=2`, `n_4=0` wird angenommen,
  `exp[-A Q_4]=1/e`; mit `Q_4=15` folgt `A(2)=1/15`.
- Fuer `k=1`, `Q_4=1` wird `A(1)=z/15` mit positiver ganzer Zahl
  `1<=z<15` angesetzt. Die Teilbarkeitsforderung reduziert auf
  `z=1,3,5`.
- Die Quelle verwirft `z=1` mit dem Satz, dann werde `Q_4A` fuer beide
  `k` identisch. Woertlich als Produkt gelesen passt diese Begruendung
  nicht zu den unmittelbar gedruckten Werten: Bei `k=1` waere
  `Q_4A=1/15`, bei `k=2` dagegen `Q_4A=1`. Identisch waeren die beiden
  **A-Werte**. Diese enge Text-/Algebraunsicherheit wird nicht zu einer
  neuen Fehlerzaehlung ausgeweitet.
- Zwischen `z=3` und `z=5` wird heuristisch `z=5` gewaehlt, weil der Text
  `(2xi-1)^2=5` unter Verweis auf (96b) heranzieht. Belegt ist hier diese
  Anwendung auf Druck 325; die Originalstelle (96b) wurde nicht neu
  visuell geprueft.

Damit erhaelt das Buch

```text
(Q_4 A)_(k=1)=1/3,   (Q_4 A)_(k=2)=1,
3 Q_4 A(k)=2k-1.
```

Die explizite Buchform lautet folglich

```text
exp[-(2k-1) N_(4)/(3Q_4)].
```

`A` ist damit fuer die spaetere Rechnung bestimmt. Bestimmt bedeutet hier
jedoch **heuristisch festgelegt**, nicht aus (79b/c) mit einer
Fehlerschranke hergeleitet.

## 6. Geruestbezug, `g(k,q)` und `W`

Druck 325 bezeichnet `n_j=0` als Gerueststruktur zeitlich konstanter
Terme. Wegen `N_(j)=n_j+Q_j` gilt an diesem Punkt

```text
N_(j)=Q_j,
```

nicht `N_(j)=0`. Einsetzen in den Protosimplexgenerator ergibt

```text
g(k,q) = alpha_1 Q_1^3 + alpha_2 Q_2^2 + alpha_3 Q_3
       + exp[-(2k-1)/3].
```

Der Text nennt `g(k,q)` den Basisanstieg von `n_j=-Q_j` nach `n_j=0`
und schreibt

```text
W/g = w,   also W=g*w.
```

Bei `n_j=0` wird `w=1`, sodass dort `W=g`. Druck 330 wiederholt in (108)
dieselben Beziehungen. `g` ist dabei konstant hinsichtlich der
Gitterkoordinate `x_4`, aber nicht eine universelle, von `k,q` unabhaengige
Zahl.

Das Exponentialglied von `g` ist genau die Externzonenfunktion am
Geruestpunkt `N_(4)=Q_4`. Deshalb gehoert die Externzonenapproximation
nicht nur zur linken Seite der Auswahlgleichung, sondern auch zum
Referenzterm, der ueber `g` die rechte Seite `W` bestimmt.

## 7. Resonanz-`f(0)` ist ein dritter Bezug

Druck 326--327 fuehrt fuer Anregungen die Resonanzordnung `N>=0` und einen
multiplikativen Faktor

```text
F(N)=1+f(N),   f(0)=0,   f(N)>0 fuer N>0
```

ein. Auf Druck 330 lautet die rechte Seite deshalb

```text
W(vx)[1+f(N)].
```

Der Grundzustand bei Resonanzordnung `N=0` besitzt laut Druck 326 seine
jeweilige Besetzung `n_j(0)`. Aus `f(0)=0` folgt nur, dass der
Anregungsfaktor eins ist. Es folgt weder `n_j=0` (Geruest) noch
`N_(j)=0` (leerer `R3`). Ebenso ist der auf Druck 322 bezeichnete irreale
`V6`-Bezugspunkt eine andere Funktion/Notation als die spaetere
Resonanzfunktion `f(N)`.

## 8. Beidseitige Korrekturalgebra

Dieser Abschnitt ist eine algebraische Folgerung aus den gedruckten
Bezuegen, keine zusaetzliche Heim-Formel. Schreibe

```text
P(N) = alpha_1 N_(1)^3+alpha_2 N_(2)^2+alpha_3 N_(3),
B    = alpha_1 Q_1^3+alpha_2 Q_2^2+alpha_3 Q_3.
```

Ersetze die rohe Externzonenfunktion `E(x)=exp(-Ax)` durch irgendeine
Funktion `F(x)`, waehrend `mu_+`, `alpha_j`, `alpha_4=1` und die
Referenzsubtraktion fest bleiben. Dann erzwingt dieselbe Buchalgebra

```text
T_F = P(N)+1+F(N_(4))-F(0),
g_F = B   +1+F(Q_4)  -F(0),
W_F = g_F*w.
```

Nur fuer die Originalfunktion mit `E(0)=1` reduzieren diese Ausdruecke
sofort auf `P+E(N_(4))` und `B+E(Q_4)`. Eine Korrektur allein von
`F(N_(4))` auf der linken Seite waere daher nicht quellkonsistent, sofern
sie `F(Q_4)-F(0)` veraendert.

Mit `F=E+h` aendert sich fuer den Resonanzgrundzustand `f(0)=0` der
Residualausdruck `R=T-W` um

```text
Delta R = h(N_(4))-w*h(Q_4)+(w-1)h(0).
```

Bei endpunktnormalisierter Abweichung `h(0)=0` bleibt
`Delta R=h(N_(4))-w h(Q_4)`. Fuer allgemeine Resonanzordnung kommt auf der
rechten Seite zusaetzlich der Faktor `1+f(N)` hinzu. Diese Identitaet
beweist keine konkrete Korrekturfunktion; sie zeigt nur, warum eine
einseitige Fehleruebertragung den im Buch selbst definierten Referenzwert
uebersehen wuerde.

## 9. Was fuer die Bruecke (79b/c) -> `N_(4)` offen bleibt

Positiv belegt ist:

- (79b) beschreibt im dritten Gueltigkeitsbereich einen raeumlichen
  Naeherungsverlauf `psi(r)~exp(-alpha r)` mit `alpha>0`. Dieses `alpha`
  ist der am unteren Ende von Druck 178 verwendete Abklingexponent
  `a-lambda_(kl)`, nicht der zuvor mit grossem `A` abgekuerzte Quotient
  `lambda_(kl)/a`; (79c) ergaenzt
  fuer einen benachbarten Bereich `r=r(nu)` und einen angenaehert
  konstanten radialen Schritt.
- Druck 322 behauptet die Anwendbarkeit dieser Approximationen auf die
  Externzone und setzt die Amplitude sowie den leeren Endpunkt explizit
  ueber `mu_+` und die Differenz `F(N_4)-F(0)` fest.
- Druck 323 bindet den Beitrag an die dimensionslose Auswahlgroesse `W`;
  Druck 325 bestimmt den spaeter verwendeten Exponentenfaktor heuristisch.
- Derselbe Ansatz wird am Geruestpunkt in `g` eingesetzt und wirkt damit
  auf beide Seiten von (108).

Auf den geprueften Seiten nicht gezeigt wird:

- eine explizite Abbildung des raeumlichen Produkts
  `(a-lambda_(kl))*r` beziehungsweise des (79b)-Abklingexponenten auf das
  diskrete Produkt `A*N_(4)` oder eine Herleitung eines
  Besetzungsschritts aus `delta r -> beta`;
- eine Fehler- oder Restschranke fuer die Anwendung der asymptotischen
  Approximation auf alle zulaessigen `N_(4)`;
- eine Herleitung der `1/e`-Annahme fuer die `k=2`-Geruestbelegung;
- ein Beweis, dass die heuristische Wahl `z=5` gegenueber `z=3` durch die
  metronische Funktion eindeutig erzwungen ist.

Der quellenfeste Schluss lautet daher nicht „Normierung fehlt“, sondern:
**Amplitude, leerer Referenzwert, Geruestreferenz und diskreter
Exponentenfaktor sind im Buch explizit gesetzt; die raeumlich-diskrete
Herleitungs- und Fehlerbruecke bleibt in diesem Abschnitt unvollstaendig.**

## 10. Suchgrenze

Geprueft wurden die vollstaendigen Druckseiten 322--330 und die direkt
benoetigten Gleichungsseiten (79b/c), (98b)--(98e). Der Verweis auf (96b)
wurde auf Druck 325 gelesen; seine eigene Gleichungsseite gehoerte nicht
zum neuen visuellen Umfang. Andere
Fremdfeldselektoren, die gesamte metronische Extremwerttheorie und eine
Neuberechnung der Massenkoeffizienten lagen ausserhalb dieses Auftrags.
Der Negativbefund betrifft diese konkrete Anschlusskette, nicht das gesamte
Werk oder unveroeffentlichtes Material.
