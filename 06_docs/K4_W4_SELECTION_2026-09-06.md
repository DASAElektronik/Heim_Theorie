# K4/W4: Ganzzahlauswahl und Erhalt der Restgleichung

2026-09-06, Etappe 25. Ausgang `e0055c9`, Plancheckpoint `28a9edc`.
Enger Folgeauftrag der [Verstaendnisbilanz](UNDERSTANDING_BALANCE_STAGE24_2026-09-06.md).
Keine neue Teilchenmasse, kein Fit und keine Aenderung alter Rechenprofile.

## 1. Ergebnis

Die gedruckte Vorschrift ist **kein allgemeiner exakter Loeser der
unveraenderten gruppierten Restgleichung** unter den unten genannten
positiven Eingabeannahmen. Der reelle Logarithmusschritt in Fall (b) stimmt;
das anschliessende Abschneiden erhaelt die Gleichheit nur bei einem bereits
ganzzahligen Ergebnis. Die endliche Kappung in (a) und der Rueckschritt in
(c) erhalten die lokale Restgleichung ebenfalls nicht.

Die Quelle begruendet die Ganzzahligkeit durch das Zaehlen von
Strukturentitaeten und die Kappung durch endliche Strukturgrenzen. Diese
Motivation ist gefunden. Sie beweist aber nicht, dass die daraus gewaehlte
ganze Zahl weiterhin die vorherige Gleichung loest.

Beide Sonderfaelle und der Ganzzahlvermerk stehen auch im fotografierten
H015-Typoskript. Der Befund kann daher nicht einfach dem fehlenden Index
oder der Exponentenklammer der spaeteren H006-Wiedergabe zugeschrieben werden.
Ein bestimmter betroffener Teilchenzustand oder Massenfehler ist damit
noch nicht nachgewiesen. Auch die Lesart einer zusaetzlichen diskreten
Auswahl-/Naeherungsregel bleibt von einer exakten Gleichungsloesung zu trennen.

## 2. Quelle und explizite Normalisierung

Tragend sind H006 Druck/PDF9, (XXX)/(XXXI), Faelle (a)--(c), Vermerk und
(XXXII), sowie separat H015 PDF42/Blatt6 samt Fussnote. H006 S.5/6/10 und
H015 PDF43/Blatt7 liefern Struktur-/Grenzkontext. Vollseiten wurden visuell
geprueft; die kleine K4-Stelle im Typoskript zusaetzlich vergroessert.
[Quellenumfang und Hashes](../03_notes/K4_W4_SOURCES_2026-09-06.md).

H006 ist eine IGW-Wiedergabe 2002/2003 eines Heim zugeschriebenen Texts;
H015 ist ein heutiger Scan fotografierter Blaetter. Datums-/Signaturabbildung
ersetzt keine Authentifizierung. Die beiden Quellen bleiben getrennt.
H006 schreibt im ersten Satz zu (c) `K<0`, H015 sichtbar `K4<0`.
Die nachfolgende H006-Prosa nennt selbst K4. Keine stille Textkorrektur.

Unsere eigenen Kurzzeichen sind

```text
a = alpha3 > 0, W3 >= 0, k >= 1, Q4 > 0,
lambda = (2k-1)/(3Q4) > 0,
m = floor(W3/a), r = W3-a*m.
```

`m` ist der vor dem Sonderfall gewaehlte K3-Wert, `r` das dortige W4.
Es gilt `0 <= r < a`. Die obere Grenze folgt aus der maximalen ganzen
K3-Wahl. Damit kann Fall (c) nur bei `a>1` auftreten. Dies ist ein
lokaler Satz unter `a>0`, kein Beweis, welche Heim-Zustaende ihn erreichen.
Die Quellwerte k=1 bzw. k=2 liefern aus (X) Q4=1 bzw. Q4=15
und damit lambda=1/3 bzw. lambda=1/15;
der Beweis braucht nur lambda>0. Die Alpha-Positivitaet wird nicht fuer
alle denkbaren Zustaende ungeprueft behauptet.

Mit `K_j=n_j+Q_j` lautet der untersuchte Rest aus (XXXI):

```text
a*K3 + exp(-lambda*K4) = W3.                 (R)
```

Vorangegangene K1/K2, W3 und a bleiben fest. Verwendet wird der
gruppierte Restgleichungs-Teilpfad, nicht die abweichende H006(XIV)-Zeile.
Wir messen den Fehler als **linke Seite minus rechte Seite** von (R).
Nichtnegativitaet, Ganzzahligkeit und die zusaetzliche Quellschranke
`K4<=a*K3` aus (XIII)/(XXXII) werden getrennt von (R) geprueft.
Negative Besetzungen `n_j` bleiben erlaubt, sofern `K_j>=0`.

## 3. Die drei Faelle

| Fall | Quellenregel, paraphrasiert | Ergebnis fuer (R) | Verbleibende Bedeutung/Grenze |
| --- | --- | --- | --- |
| (a) r=0 | Unendliches K4 verwerfen; endliche Grenze K4=a*m verwenden, danach Ganzzahlvermerk beachten | Bei unveraendertem K3=m ist der Rest exp(-lambda*K4)>0; auch eine ganzzahlige Grenze loest das nicht | Kappungsentscheidung, keine endliche Loesung des Nullrests; andere K3-Werte sind hier nicht generell ausgeschlossen |
| (b) 0<r<=1 | Reell x=-ln(r)/lambda bestimmen; Nachkommastellen abschneiden, ausser nachgewiesener Integeridentitaet | Reell exakt; nach j=floor(x) Gleichheit genau dann, wenn x ganzzahlig ist | Expliziter Rest und Schranken unten; Strukturkappe separat pruefen |
| (c) r>1 | K3 um eins verringern und a*K3 zum negativen Logwert addieren; K3=0 verbietet den Schritt | Danach waere exp(-lambda*K4)=r+a>1 noetig, unmoeglich fuer K4>=0 | Gilt unabhaengig vom alten/neuen K3 im Additionsterm; keine Aussage ueber veraenderte K1/K2 oder eine neue Gleichung |

### (a): Warum die Kappe die Null nicht erzeugt

Fuer jedes endliche reelle K4 ist der Exponentialterm strikt positiv.
Bei `r=0` und `K3=m` kann er daher die geforderte Null nicht erreichen.
Die Quelle kennt die logarithmische Divergenz und ersetzt sie bewusst
durch eine obere Strukturgrenze. Das ist eine weitere Regel, keine
algebraische Umformung der unveraenderten Gleichung.

Dieser Schluss ist enger als ein Unloesbarkeitssatz fuer alle K3:
Beim eigenen Testwert `a=W3=1` liefert die Maximalwahl m=1,r=0.
Das andere Paar K3=K4=0 erfuellt (R) und die Kappe exakt. Es wird
nicht als Quellenkorrektur oder Teilchenzustand eingefuehrt.

### (b): Exakter Rest des Abschneidens

Schreibe `x=j+theta`, `j=floor(x)`, `0<=theta<1`. Dann ist

```text
R = exp(-lambda*j)-r
  = r*(exp(lambda*theta)-1)
  = exp(-lambda*j)*(1-exp(-lambda*theta)).

0 <= R < exp(-lambda*j)*(1-exp(-lambda)) <= 1-exp(-lambda),
0 <= R/r < exp(lambda)-1.
```

R ist null genau bei theta=0. Die Schranken betreffen ausschliesslich
diesen Exponentialrest im Fall (b), nicht die ganze Massenformel, keine
Massenunsicherheit und nicht die Sonderfaelle (a)/(c).
Vor der Integerisierung verlangt die Strukturkappe zusaetzlich
`r>=exp(-lambda*a*m)`; sie folgt nicht schon aus `0<r<=1`.
Nach dem Abschneiden ist `j<=a*m` gesondert zu pruefen. Eine eingehaltene
Kappe kann mit einer verletzten Restgleichung zusammen auftreten.

Die gedruckte Neunerfolge ist kein vollstaendiges numerisches Zertifikat:
Eine **unendlich periodische** 0.999... ist eins, endlich viele Neunen sind
kleiner als eins. Die Quelle nennt hier keine endliche Praezision oder
Toleranz. Wir behalten die bisherige Vorgabe: echte analytische Identitaet
oder zertifizierte Entscheidung; kein frei gewaehltes Epsilon und kein
Aufrunden, weil ein Ergebnis besser zu einer Masse passt.

### (c): Warum beide Additionslesarten das Problem behalten

Bei K3_neu=m-1 wird fuer dieselbe rechte Seite
`W3-a*(m-1)=r+a` benoetigt. Dieser Wert liegt ueber eins; fuer endliches
K4>=0 liegt der Exponentialterm dagegen in `(0,1]`.
Auch ein erneutes Logarithmieren des vergroesserten Rests gaebe K4<0.

Mehr noch: Fuer jeden ganzzahligen K3<=m ist der benoetigte Rest mindestens
r>1; fuer K3>=m+1 ist er wegen r<a negativ. Somit gibt es **bei festem
W3 und a** in Fall (c) ueberhaupt kein Paar aus ganzzahligem K3>=0 und
reellem K4>=0, das (R) erfuellt. Das ist kein Unloesbarkeitssatz ueber alle
vier Zonen oder geaenderte W3-Werte.

Die alten Pseudocode-Lesarten setzen mit x=-ln(r)/lambda:

```text
Nachwertlesart: x_neu = x+a*(m-1),
Vorwertlesart:  x_neu = x+a*m.
```

Quellenseitig ist dieser Bezug nicht eindeutig indiziert. Akzeptanz oder
ausgewaehltes K4 koennen sich unterscheiden. Fuer jedes danach akzeptierte
K4>=0 gilt aber `R<=1-(r+a)<0`. Weder diese Ambiguitaet noch das fehlende
H006-Indexzeichen beseitigt den Gleichungskonflikt bei festem W3.

## 4. Kleine nachrechenbare Zeugen

Alle folgenden Werte sind **eigene mathematische Testeingaben**, keine
aus (IX)/(XVI) hergeleiteten Heim-Teilchenwerte. Es gilt lambda=1/3.

| Fall | Eingabe a,W3; gewaehltes m,r | Ausgabe | Rest in (R) |
| --- | --- | --- | --- |
| (a) | a=2,W3=2; m=1,r=0 | K3=1,K4=2 | exp(-2/3)>0 |
| (b) | a=1,W3=11/4; m=2,r=3/4 | 0<-3ln(3/4)<1, daher K3=2,K4=0 | genau 1/4 |
| (c), Nachwert | a=2,W3=11/2; m=2,r=3/2 | K3_neu=1,K4=0 | genau -5/2 |
| (c), Vorwert | dieselbe Eingabe | K3_neu=1,K4=2 | exp(-2/3)-7/2<0 |

Die beiden (c)-Ergebnisse folgen aus `-2<-3ln(3/2)<-1`. Diese Intervalle
und die Abschneideentscheidungen sind rational zertifiziert, nicht aus
gerundeten Dezimalzahlen abgelesen. Alle Tabellen-Ausgaben halten
`0<=K4<=a*K3` ein. Die Kappe allein garantiert also keine Gleichheit.

Die (a)/(c)-Zeugen lassen sich zusaetzlich mit den eigenen Werten
alpha1=1,alpha2=alpha3=2,K1=3,K2=2 in die vorgelagerten Maximalschritte
einbetten und erfuellen die Ungleichungen (XIII)/(XXXII). Dies beweist
weder eine gemeinsame Herkunft dieser Alpha-Werte aus Heims Formeln noch
die gesamte Zonenuebergangsvorschrift bei Gleichheit. Es beseitigt nur
den Einwand, die genannten Ungleichungen allein muessten den Rest schliessen.

## 5. Tragweite und naechste Frage

FIND-035 fasst **einen zusammenhaengenden bedingten Algorithmusbefund**
zusammen, nicht drei neue Theoriefehler. Die exakt-loesende Interpretation
scheitert unter den deklarierten Voraussetzungen; eine eigenstaendige
diskrete Auswahl-/Saettigungsinterpretation ist dadurch noch nicht widerlegt.
Fuer sie fehlen im geprueften Umfang eine praezise Ersatzrelation bzw.
Restbewertung und die Verbindung zu den physikalisch zugelassenen Eingaben.

Der alte Elektron-N0-Fall bleibt unveraendert: Dort ist im gruppierten
Pfad `r=exp(-1/3)` und `K4=1` analytisch, also R=0. Kein frueherer
Massenausgabewert wird hier korrigiert. Mehr Hardwarepraezision wuerde die
gezeigten exakten Nichtnullreste nicht entfernen.

Naechster begrenzter Auftrag ist deshalb ein **Erreichbarkeits- und
Eingabevertrag fuer einen weiteren H006-N0-Fall**, noch keine Masse:
Die unmittelbar folgende Tabellenkonfiguration x3/mu- aus H006 Druck/PDF3,
(III), als vorab benannten Kandidaten pruefen. Die Quelle bezeichnet
x3(0111) mit den Ladungslisten (-1,-1) bzw. zusammengezogen (-1) als
Pseudosingulett; daraus wird noch kein Besetzungstupel abgeleitet.
Zuerst diese Komponentenidentifikation pruefen, dann W aus (XV)--(XIX)
und erforderlichen Matrixeintraegen
quellengetreu herleiten, dann ihren Auswahlzweig und Rest untersuchen.
Komponenten-/Index- oder Eingabeluecken sind ein zulaessiger Abschluss;
kein Wechsel zu einem guenstigeren Fall nach Zahlenresultat. Eine moegliche
Zonenuebergangsregel muss dabei explizit hinzukommen, nicht still angenommen
werden. Allgemeine N>0-Dynamik und H/G-Pfade bleiben eigene offene Aufgaben.

## 6. Gegenkontrollen und Sicherung

- [H006-Quellenreview](../04_reconstruction/alpha_audit/reviews/K4_W4_REPRINT_REVIEW_2026-09-06.md)
- [H015-Archivreview](../04_reconstruction/alpha_audit/reviews/K4_W4_ARCHIVE_REVIEW_2026-09-06.md)
- [Unabhaengige Mathematikreview](../04_reconstruction/alpha_audit/reviews/K4_W4_MATH_REVIEW_2026-09-06.md)
- [Isolierte Tests](../tests/test_k4_w4_selection.py)

Root hat die tragenden Originalseiten selbst gelesen, die Restsaetze
separat abgeleitet und den neuen Testcode vollstaendig gegengelesen.
Die Tests benutzen Fraction sowie rationale Log-/Exp-Intervalle mit
expliziten Reihenrestschranken. Keine historische Fremdsoftware ausgefuehrt.
Diese internen Gegenkontrollen sind kein externes Peer Review.

Vierzehn neue Tests und 199 Tests insgesamt bestehen; zehn alte
Snapshot-/Quellchecks und die Registermetadatenpruefung sind bestanden.
Alte Rechner, Eingaben,
Snapshots und 49 CSV-Normalisierungen bleiben erhalten. Die historische
Lesentscheidung `resolved` wird nicht zu einem Validierungsbeweis umgedeutet.
Heims Quellenideen und unsere mathematische Kritik bleiben nach
[SOURCE_ATTRIBUTION](../00_admin/SOURCE_ATTRIBUTION.md) getrennt zugeschrieben.
