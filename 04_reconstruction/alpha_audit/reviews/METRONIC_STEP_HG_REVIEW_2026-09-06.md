# `delta`, `delta_e` und `X` im H/G-Schritt von H004

Stand: 2026-09-06. Begrenzte Quellenreview zu EDM II Druck 271--275 /
PDF 277--281. Gleichung (98) auf Druck 267 / PDF 273 und die bereits
direkt einschlaegigen Band-I-Regeln M2/M2a/M7 wurden nur zur
Symbolabgrenzung herangezogen.

## 1. Kurzbefund

H004 setzt in den unintegrierten H/G-Gleichungen zwei verschieden
geschriebene Variationsarten nebeneinander:

- alle Potentialterme tragen `delta_e`;
- der gemeinsame Grenz-/Zaehlerterm `X` traegt nur `delta`, ohne Index `e`.

Der Text definiert `delta_e` an dieser Stelle als metronische Variation der
internen Ladungsfeldkomponenten aus (98). `X(nu)` wird dagegen als
unbekannte metronische Funktion fuer den Anstieg der von der Struktur
erfassten Metronenzahl am Uebergang `j=3 -> j=4` eingefuehrt. Im geprueften
Abschnitt steht weder `delta_e X=delta X` noch eine Aussage, beide Schritte
haetten dieselbe Skalierung. Dass dasselbe `delta X/X` in H und G vorkommt,
ist eine gemeinsame Modellkomponente, keine gedruckte Operatoridentitaet.

## 2. Visuell gepruefte Quelle

Vollstaendig gelesen wurden die Vollseiten

- Druck 271 / PDF 277: Ansatz `alpha3=f-qF`;
- Druck 272 / PDF 278: `F=H+G`, Definition der Potentialpfade und von
  `X(nu)`, Beginn der unintegrierten Gleichungen;
- Druck 273 / PDF 279: Abschluss der unintegrierten Gleichungen,
  Logschreibweise, `X`-Metronintegral und integrierte Potentialterme;
- Druck 274 / PDF 280: Grenzen und ausgewertete Logarithmen;
- Druck 275 / PDF 281: Wahl der `A_i,B_i`, H/G-Endformen und asymptotische
  Spezialisierung von `Y`.

Bildpfade:
`tmp/pdfs/alpha3_book_origin/edm2-277.png` bis `edm2-281.png`.
Die Indizes wurden visuell gelesen; OCR ist kein Formelbeleg.

## 3. Zweck von H und G in der unmittelbaren Kette

Druck 271 setzt fuer die dritte Zonendeformation

```text
alpha3(k,q) = f(k)-q*F(k,q).
```

Druck 272 fordert `F=H+G`. `H` soll im Wesentlichen durch die internen
Ladungsfeldkomponenten `e_rho` und `e_omega` bestimmt sein, `G` durch
`e_delta`. Diese Aussage motiviert die Aufteilung, ist aber noch keine
Variationsgleichung.

Die folgenden Variationen werden bei konstanter `R3`-Distanz an der Grenze
der Zone `j=3` angesetzt. Die Striche in `V'=V(k=1)` und `V''=V(k=2)` sind
laut Text Indizes, keine Ableitungen.

## 4. Glyphentreue unintegrierte Gleichungen

Der Seitenumbruch liegt mitten im Satz zwischen Druck 272 und 273. In
linearer Schreibweise druckt H004:

```text
delta H / H
  = A1 * delta_e V_(omega) / V_(omega)
  + A2 * delta X / X
  + A3 * delta_e V_(rho rho) / V_(rho rho),

delta G / G
  = B1 * delta_e V_(rho rho)(G) / V_(rho rho)(G)
  + B2 * delta X / X
  + B3 * delta_e V_(rho rho) / V_(rho rho)
  + B4 * delta_e W / W.
```

Dabei tragen die linken Seiten `delta H` und `delta G` ebenfalls kein
Subskript `e`. Die Faktoren `A1,A2,A3` und `B1,...,B4` werden unmittelbar
zuvor als nur von `k` abhaengige Proportionalitaetsfaktoren eingefuehrt.

Direkt danach schreibt die Quelle dieselben Ansaetze logarithmisch:

```text
delta ln H
  = A1*delta_e ln V_(omega)
  + A2*delta ln X
  + A3*delta_e ln V_(rho rho),

delta ln G
  = B1*delta_e ln V_(rho rho)(G)
  + B2*delta ln X
  + B3*delta_e ln V_(rho rho)
  + B4*delta_e ln W.
```

Auch hier bleibt die Glyphentrennung unveraendert: `delta_e` nur bei den
Potentialen, unsubskribiertes `delta` bei `H`, `G` und `X`.

## 5. Was in den vier Potentialtermen variiert

H004 Druck 272 beschreibt die Potentiale nicht als vier beliebige Namen,
sondern ordnet ihnen folgende Pfade bzw. Komponenten zu:

| Term | Quelleigene Rolle der Variation |
| --- | --- |
| `V_(omega)` | Potential bezogen auf das auf Druck 272 gedruckte Produkt `e_omega*epsilon_+`; die spaeteren Grenzen sind `V_alpha,V_beta`. (98) selbst schreibt die Komponenten allgemein mit `epsilon_+/-`. |
| `V_(rho rho)` | Potential bezogen auf `e_rho^2`; derselbe Pfad erscheint mit `A3` in H und `B3` in G. |
| `V_(rho rho)(G)` | Variation zwischen `V_(rho rho)` und `V'_(rho rho)(q=1)`; der Strich fixiert `k=1`. |
| `W` | Variation zwischen `V_(omega omega)` und `V_(delta delta)`, also bezogen auf `e_omega^2` und `e_delta^2`. |

Gleichung (98), Druck 267 / PDF 273, definiert die dafuer benoetigten
Feldkomponenten mit `s=sqrt(eta_qk)` als

```text
e_rho=epsilon_+/-*s,
2*e_omega=epsilon_+/-*(1+s),
e_delta=epsilon_+/-*(1-s).
```

Damit ist der Index `delta` in `e_delta` bzw. `V_(delta delta)` der Name
einer Ladungsfeldkomponente. Er ist nicht das davorstehende
Variationszeichen `delta` und nicht dessen Index `e`.

Druck 273 sagt zusaetzlich: `delta_e` beziehe sich nur auf die Komponenten
in (98), nicht auf `epsilon_+/-=const`; deshalb diene
`V_(epsilon epsilon)=V_epsilon=const` als Referenz. Die spaetere Anweisung,
an Potential-Untergrenzen eine Variation zu addieren, aendert diese
Glyphenzuordnung nicht und fuehrt keine `delta_e X`-Notation ein.

## 6. Was `X(nu)` laut Quelle ist

`X` wird nicht als Potential und nicht als Funktion von
`V_(omega)`, `V_(rho rho)` oder `W` definiert. Druck 272 nennt es eine
unbekannte metronische Funktion, welche den Anstieg der von der betreffenden
Struktur erfassten Metronenzahl wiedergibt. Als Folge soll gelten

```text
X_nu = X_(nu-1)+X_(nu-2).
```

Die Ziffer `nu=z` wird auf Druck 273 der raeumlichen Grenze zwischen
`j=3` und `j=4` zugeordnet. Ueber diese Grenzschicht wird der X-Term separat
integriert:

```text
S_(z)^(z+1) delta ln X
  = ln X(z+1)-ln X(z-1)
  = ln[X(z+1)/X(z-1)]
  = ln Y.
```

Das Ergebnis wird aus beiden H/G-Gleichungen auf die linke Seite gezogen:

```text
ln H-A2*ln Y = [die beiden H-Potentialintegrale],
ln G-B2*ln Y = [die drei G-Potentialintegrale].
```

Dies ist die einzige direkte Verbindung von `X` mit H und G im geprueften
Abschnitt: derselbe additive Grenzbeitrag tritt mit unterschiedlichen
Gewichten auf. Eine funktionale Beziehung `X=X(V)` oder ein gemeinsamer
Variationsparameter fuer `delta X` und `delta_e V` wird nicht angegeben.

## 7. Unterschiedliche k-Gewichte desselben X-Terms

Druck 275 betont zuerst, die Konstanten `A_i,B_r` koennten frei vorgegeben
werden, und bezeichnet dann folgende Wahl als der Elektron-/Protonempirie
optimal angepasst:

```text
A1=B1=B4=1,
A2=(2*k+1)/2,
B2=k/2,
B3=k,
A3=1-4*k.
```

Nach dieser Wahl lauten die unintegrierten Ansaetze ausgeschrieben:

```text
delta H/H
  = delta_e V_(omega)/V_(omega)
  + (2*k+1)/2 * delta X/X
  + (1-4*k) * delta_e V_(rho rho)/V_(rho rho),

delta G/G
  = delta_e V_(rho rho)(G)/V_(rho rho)(G)
  + k/2 * delta X/X
  + k * delta_e V_(rho rho)/V_(rho rho)
  + delta_e W/W.
```

Somit ist die X-Variation zwar dieselbe geschriebene Groesse, aber ihr
Gewicht ist in H und G verschieden. Schon fuer festes `k` kann daraus keine
Gleichheit der gesamten H- und G-Variationen folgen.

Der auf Druck 274 vor dem ersten integrierten G-Logarithmus sichtbare
Koeffizient `B'_1` steht im unintegrierten Ansatz noch als `B1`; Druck 275
waehlt ebenfalls `B1=1`. Der unmittelbare Abschnitt definiert den Strich
am Koeffizienten nicht. Diese lokale Satzfrage aendert nicht den hier
eindeutigen Unterschied `delta_e V` gegen `delta X`.

## 8. Haben `delta_e X/X` und `delta X/X` dieselbe Skalierung?

Die erste Form kommt in den geprueften Gleichungen ueberhaupt nicht vor.
Quellengetreu lautet der Befund daher:

1. `delta_e` wird auf Druck 272 in der Groessenordnung `sqrt(tau)` fuer die
   internen Ladungsfeldkomponenten eingefuehrt.
2. Das `delta X` des grossen `X(nu)` erhaelt dort keine eigene
   Groessenordnung.
3. Das unmittelbar vorangehende kleine `delta x` bei der Hilfsanalyse von
   `f(x)` wird zwar ebenfalls der Groessenordnung `sqrt(tau)` zugeordnet;
   kleines `x` ist aber das Analyseargument von `f`, nicht die spaeter
   eingefuehrte Funktion `X(nu)`. Eine Uebertragung waere unbelegt.
4. Band I M7 beschreibt `delta_e` als klein skalierte metronische
   Variation und den Logarithmusuebergang nur approximativ. M2/M2a
   definieren dagegen das unsubskribierte `delta` als diskrete
   Rueckwaertsdifferenz. Diese Regeln erklaeren, warum die Glyphen nicht
   stillschweigend gleichgesetzt werden duerfen; sie liefern im
   H004-Abschnitt keine fehlende Skalengleichung fuer `X` nach.

## 9. Abschlussstatus

Quellenklar ist die Architektur

```text
F=H+G,
H/G-Gesamtvariation
  = gewichtete Ladungspotentialvariationen delta_e V/V
  + gemeinsamer, separat diskret integrierter Grenzterm delta X/X.
```

Offen bleibt, ob Heim einen einzigen tieferen Metronenschritt hinter beiden
Symbolen voraussetzt und wie dessen Skalierung von `X` mit derjenigen der
Ladungsfelder zusammenhaengt. Die sichtbaren Gleichungen behaupten nur die
additive Kopplung mit k-abhaengigen Koeffizienten; sie beweisen weder
`delta_e X=delta X` noch eine gemeinsame Schrittweite.
