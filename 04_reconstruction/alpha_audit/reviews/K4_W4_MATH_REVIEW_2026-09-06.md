# K4/W4: unabhaengige skalare Restgleichungspruefung

2026-09-06, Etappe 25. Nur gewoehnliche reelle Algebra der vorgegebenen
Restgleichung, keine Massenrechnung oder allgemeine Zustandssuche.
Gelesen: K4_W4_PLAN, HT-F-1982-SELECTION-ALGO sowie die alten Entscheidungen
W4-CASES und INTEGER-DECIMAL-RULE. Diese fixieren Lesprofile, keine bewiesene
Gleichungserhaltung. Keine eigene PDF-/Glyphenpruefung in dieser Review.

## 1. Quellenannahmen und genaue Eingangsdomäne

Uebernommene gruppierte Restgleichung, nicht die abweichende XIV-Lesart:

```text
a = alpha3 > 0, k >= 1, Q4 > 0, W3 >= 0,
c = (2k-1)/(3Q4) > 0,
a*K3 + exp(-c*K4) = W3, K3 ganzzahlig >= 0, K4 >= 0.
```

W3 und die vorangegangenen K1/K2-Schritte bleiben fest. Zunaechst ist K4
reell, erst danach wird die Ganzzahlvorschrift untersucht. Negative n_j
sind dadurch nicht ausgeschlossen; K_j und n_j sind verschiedene Groessen.

Ruecksprache mit alpha_versions (H006) und book_derivation (H015): Beide
Dokumente nennen die drei Faelle, den K3-Rueckschritt und die Addition.
H006s nacktes `K<0` wird nicht still korrigiert; H015 schreibt hier K4.
Keines bezeichnet Vor-/Nachwert im Additionsterm eindeutig oder schreibt
ausdruecklich eine erneute W4-Berechnung. Die beiden Lesarten bleiben getrennt.
Die Schranke K4<=a*K3 ist laut H006-Quellenreview auch in XIII/XXXII enthalten;
sie wird hier als weitere Strukturbedingung, nicht als Folgerung der
Restgleichung benutzt. Dies ist uebernommene Quellenlesung, kein eigener
Nachweis ihres physikalischen Ursprungs.

## 2. Was die Greedy-Wahl erzwingt

Setze m=floor(W3/a) und r=W3-a*m. Dann gilt exakt

```text
0 <= r < a;  W3-a*(m+1) < 0.
```

Die obere Grenze ist strikt. Fall(c), r>1, ist daher nur bei a>1 moeglich.
Er ist unter diesen lokalen Annahmen erreichbar, etwa a=3,W3=8,m=2,r=2.
Das ist ein eigener mathematischer Zeuge, kein nachgewiesener Heim-Zustand.
Bei r=0 ist der logarithmische K4-Wert nicht endlich definiert.

## 3. Fall(a): endliche Saettigung ist keine exakte Nullrestloesung

Die Lesregel setzt K4_raw=a*m und danach gegebenenfalls K4=floor(a*m).
Beide Werte sind endlich und nichtnegativ, beide halten K4<=a*m ein.
Bei unveraendertem K3=m ist der Gleichungsfehler jedoch genau
exp(-c*K4)>0. Auch ganzzahliges a*m loest dieses Problem nicht.
Nur der Grenzwert K4 gegen unendlich bringt den Exponentialrest gegen null;
er ist kein zulaessiger endlicher K4-Wert und verletzt jede feste endliche Kappe.

Dieser Schluss betrifft den gewaehlten m-Wert. Anders als bei Fall(c)
folgt hieraus keine Unmoeglichkeit aller anderen K3: Beim synthetischen
a=W3=1 liefert Greedy m=1,r=0, aber K3=K4=0 erfuellt dieselbe Gleichung
und die zusaetzliche Schranke exakt. Dies ist keine vorgeschlagene Reparatur.

## 4. Fall(b): reelle Loesung, Ganzzahlfehler und Strukturkappe

Fuer 0<r<=1 ist x=-ln(r)/c>=0 die eindeutige reelle Loesung bei K3=m.
Mit j=floor(x), theta=x-j in [0,1) wird der Fehler nach Integerisierung

```text
R = a*m+exp(-c*j)-W3
  = exp(-c*j)-r = r*(exp(c*theta)-1)
  = exp(-c*j)*(1-exp(-c*theta)).
0 <= R < exp(-c*j)*(1-exp(-c)) <= 1-exp(-c),
0 <= R/r < exp(c)-1.
```

R verschwindet genau fuer theta=0, also echte Ganzzahligkeit von x.
Ein analytischer Nachweis r=exp(-c*j) rechtfertigt diesen Sonderfall;
eine endliche Folge von Neunen oder epsilon-Naehe beweist ihn nicht.
Es wird weder aufgerundet noch ein Toleranz-Fit eingefuehrt.

Die reelle Strukturkappe x<=a*m entspricht zusaetzlich r>=exp(-c*a*m).
Sie folgt nicht aus r in (0,1]. Nach floor muss die Kappe separat am
integerisierten Wert geprueft werden. Sie kann dann gelten, obwohl die
Restgleichung verletzt wird: a=1,W3=11/4,c=1/3 ergibt m=2,r=3/4,
0<x<1 und j=0, somit R=1/4 trotz erfuellter Kappe. Bei a=1,W3=1/2,c=1
verletzt x>0 sogar die reelle Kappe a*m=0; j=0 haelt sie ein, bleibt aber
keine Gleichungsloesung. Alle Werte sind synthetische Diagnoseeingaben.

## 5. Fall(c): Rueckschritt und zwei Additionslesarten

Fuer r>1 ist x=-ln(r)/c<0. Bei m=0 nennt die Lesregel den Term verboten.
Bei m>0 wird K3_neu=m-1; der fuer die unveraenderte Gleichung benoetigte
Exponentialrest ist dann r+a>1. Kein K4>=0 kann diesen Rest erzeugen.
Ein Neuberechnen des Logarithmus dieses Restes wuerde erneut K4<0 geben.

Noch staerker, aber weiterhin bei festem W3,a: Fuer jeden ganzzahligen
K3<=m ist W3-a*K3>=r>1; fuer K3>=m+1 ist er negativ. Daher gibt es in
diesem Fall ueberhaupt kein nichtnegatives K3/K4-Paar mit ganzzahligem K3,
das dieselbe Restgleichung erfuellt. Eine Aenderung von K1/K2, W3 oder
der Gleichung selbst ist in diesem Nachweis ausdruecklich nicht untersucht.

Die alten Lesprofile halten den urspruenglichen Logwert fest und setzen

```text
post: x_neu = x+a*(m-1),
pre:  x_neu = x+a*m.
```

Sie unterscheiden sich um a; ihre Nichtnegativitaetsentscheidung kann
verschieden ausfallen. Vor floor ist bei Additionsindex h=m-1 oder m
der Gleichungsfehler r*(exp(-c*a*h)-1)-a <= -a < 0.
Nach floor und nur bei akzeptiertem K4>=0 gilt weiterhin
R<=1-(r+a)<0. Eine erfuellte Kappe K4<=a*(m-1) aendert dies nicht.

Ein eigener Zeuge a=3,m=1,r=2,c=1 wird post wegen negativem x_neu verworfen,
pre dagegen vor der Strukturkappenpruefung akzeptiert. Root schlug getrennt
a=2,m=2,r=3/2,c=1/3 vor; die unabhaengigen Logintervalle bestaetigen:
post ergibt nach floor K4=0, pre K4=2. Beide erfuellen die Nachwertkappe 2,
aber ihre Fehler sind -5/2 bzw. exp(-2/3)-7/2<0. Keine Variante ist damit
als Autorenabsicht, gueltige Dilatationsdynamik oder physikalisch korrekt bestimmt.

## 6. Unabhaengige Zertifikate und Reichweite

Die neue isolierte Datei tests/test_k4_w4_selection.py importiert nur
unittest und Fraction, keinen bestehenden Rechner und keine Fremdsoftware.
Sie enthaelt 14 Tests einschliesslich Domains und bewusster Unterscheidung
von analytischer Integeridentitaet und endlicher Dezimalnaehe.
Fuer positive rationale v wird ln(v) mit t=(v-1)/(v+1) ausgewertet:
2*sum(j=0..n-1,t^(2j+1)/(2j+1)), Restbetrag hoechstens
2*abs(t)^(2n+1)/((2n+1)*(1-t*t)). Das Vorzeichen der Restreihe liefert
gerichtete rationale Intervalle. Fuer exp(x>=0) wird die Taylorreihe bis n
mit naechstem Term geteilt durch 1-x/(n+2) nach oben begrenzt, sofern
x<n+2; negative Argumente werden durch Kehrwertintervalle erfasst.
Die verwendeten 48 Terme liefern exakte rationale Zertifikate, keine
aus gerundeten Dezimalzahlen abgeleiteten Ganzzahlentscheidungen.

```powershell
py -3.13 -B -m unittest discover -s tests -p test_k4_w4_selection.py -v
```

Ausgefuehrt: alle 14 neuen Tests bestanden (Exitcode 0); anschliessend
bestand auch die gesamte bestehende Suite mit 199 Tests. Kein --write,
kein Fremdprogrammlauf, keine Aenderung alter Tests oder Rechner.

Ein enger Zusatztest bettet die a/c-Zeugen in synthetische vorgelagerte
Maxima ein: alpha1=1,alpha2=alpha3=2,K1=3,K2=2, W3=2 beziehungsweise 11/2.
Dann liegen W2=10 beziehungsweise 27/2 in [8,18) und W1=37 beziehungsweise
81/2 in [27,64). Die angegebenen K1/K2 sind somit maximal. Bei K3_neu=1
und K4=2 beziehungsweise 0/2 gelten XIII mit dem gedruckten rechten alpha3
und die drei XXXII-Ungleichungen: K4<=2<=8<=54, 4<=16 und 60<=162.
Auch K3_vor=2 erfuellt die zweite XXXII-Schranke mit 12<=16.
Die Koeffizienten sind frei gewaehlte synthetische Inputs, nicht aus einem
gemeinsamen Heim-Parametersatz gewonnen. Geprueft sind nur Maxima und
Ungleichungen, nicht die folgende Gleichheits-/Zonenuebergangsvorschrift.
Vorhandene XIII-Transkription und fruehere eigene XXXII-Review wurden dazu
gezielt gelesen. Diese Einbettung macht die Restgleichungsfehler nicht zu
Nachweisen fuer reale Teilchen, zeigt aber, dass die genannten lokalen
Ungleichungen allein sie nicht ausschliessen.

Die Fallregeln koennen als eigene diskrete Auswahl-/Saettigungsvorschrift
gelesen werden. Dann ist ihr Sinn nicht allein die exakte Loesung der
hier festgehaltenen Gleichung; eine begruendete Ersetzung oder Fehlerregel
waere zusaetzlich zu benennen. Diese Review beweist keine solche Dynamik
und repariert keine Regel. Gleichungserhaltung, Nichtnegativitaet,
Strukturkappe und physikalische Zulaessigkeit bleiben getrennte Fragen.
Keine neue Masse, keine allgemeine Resonanzsimulation, keine Nachlass-
oder Gesamtwiderlegung. Alte Normalisierungen und Rechner bleiben unveraendert.
