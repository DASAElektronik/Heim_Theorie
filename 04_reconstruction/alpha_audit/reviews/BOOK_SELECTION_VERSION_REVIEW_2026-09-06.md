# Buchauswahl H004 gegen H006/H015: W4, W5, W6 und TRC

Stand: 2026-09-06. Eng begrenzter Quellen- und Fassungsvergleich ohne
Massenrechnung. Gleiche Strukturideen werden nicht als Beleg einer
vollstaendig identischen Fassung behandelt.

## 1. Kurzergebnis

H004 Druck 340--342 bietet eine deutlich ausfuehrlichere Auswahlvorschrift
als H006 Druck/PDF 9 und der fotografierte Typoskripttext H015 PDF 42:

- H004 trennt den Rest `W4`, den reellen logarithmischen Zwischenwert `W5`
  und den nach einem Transfer erreichten Wert `W6`.
- H004 definiert einen benannten Operator `TRC` und gibt neben dem
  Abschneiden einen eingegrenzten `0,99...99`-Sonderfall an.
- Fuer `W4>1` formuliert H004 einen gegebenenfalls wiederholten Transfer
  mit Anfangsbesetzung `N'_(3)`, Summenform und Endbesetzung
  `N_(3)=N'_(3)-mu`.
- H006/H015 verwenden an der entsprechenden Stelle den logarithmischen
  Wert unmittelbar als `K4` und beschreiben nur einen `K3`-Rueckschritt
  samt Addition. Vor-/Nachwert und Restupdate bleiben dort offen.

H004 klaert damit mehrere Ablaufdetails der Buchfassung. Es beweist nicht,
dass diese ausfuehrlichere Vorschrift wortgleich zur auf 1982 datierten
Typoskriptfassung oder zur IGW-Wiedergabe gehoert.

## 2. Quellen und visuelle Pruefung

### H004

`01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf`

SHA-256:
`F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.

Vollstaendig visuell geprueft: Druck 340--342 / PDF 346--348.
Arbeitsbilder:
`tmp/pdfs/book_selection_version/h004-346.png` bis `h004-348.png`.

### H006

`01_sources/heim_primary/Massenformel_nach_B_Heim_1982.pdf`

SHA-256:
`F74DA0DAC8496BCD01226F54D88598152D67E1C954943AF61D0EC1811F5527BE`.

Vollstaendig visuell gegengelesen: Druck/PDF 9. H006 ist die
IGW-Wiedergabe 2002/2003 eines dort Heim zugeschriebenen und auf 1982
datierten Textes, kein hier authentifiziertes Urschriftfaksimile.
Bildanker: `tmp/pdfs/k4_w4_h006/h006-p9-600-09.png`.

### H015

`01_sources/heim_primary/alpha3_origin/Heim_DESY_1982_Archivscan.pdf`

SHA-256:
`C242599F7AAF68BB8E2F3C7756A24687E86FAD879E4D0E22C00585A32403317F`.

Vollstaendig visuell gegengelesen: PDF 42, fotografierter Typoskriptkoerper
mit sichtbarer Blattnummer `- 6 -` und Fussnote auf dem folgenden
sichtbaren Blattteil `- 7 -`. H015 ist ein heutiger Scan fotografierter
Blaetter; der Hash authentifiziert nicht das Papieroriginal.
Bildanker: `tmp/pdfs/alpha3_origin/desy-42.png`.

## 3. Eingabevertrag und erste Exhaustion in H004

Druck 340 sagt, mit (108)--(110d) koennten fuer jeden `V6`-Punkt die
Groessen `W`, `a` und `b` numerisch bestimmt werden. Dann wird gesetzt:

```text
W1 = W*(1+f).
```

Die Auswahlvariablen der Buchfassung heissen `N_(j)`. Das Buch laesst die
positiven ganzen Zahlen bis zum jeweiligen Maximalwert anwachsen:

```text
alpha1*N_(1)^3 <= W1,
alpha1*(N_(1)+1)^3 > W1,
W2 = W1-alpha1*N_(1)^3,

alpha2*N_(2)^2 <= W2,
W3 = W2-alpha2*N_(2)^2,

alpha3*N_(3) <= W3,
W4 = W3-alpha3*N_(3).
```

Diese Gleichheiten und Maximalbedingungen sind als Exhaustionsverfahren
formuliert, nicht mit einem Naeherungszeichen. Erst nach Abschluss setzt
Druck 342

```text
n_j = N_(j)-Q_j.
```

H006/H015 nennen die homologen Auswahlzahlen dagegen `K_j` und setzen
spaeter `n_j=K_j-Q_j`. Die strukturelle Entsprechung erlaubt den Vergleich,
aber keinen stillen Symbol- oder Eingabetransfer zwischen den Fassungen.

Zudem beginnt H006/H015 den Algorithmus ausdruecklich fuer `N=0` oder
`N>=2` und verlangt `Q=Q(0)` statt der unbekannten Funktion `Q_N=Q(N)`.
H004 formuliert den vorliegenden Abschnitt nach Druck 340 fuer
Protosimplexgeneratoren und `N>=0`. Auch deshalb ist keine vollstaendige
Gleichheit des Eingabevertrags belegt.

## 4. H004: exakte W4-Bereiche

Druck 341 teilt nicht in die drei beschrifteten Faelle (a)--(c), sondern
druckt zwei Bereiche:

```text
0 <= W4 <= 1
```

oder

```text
1 < W4 < (alpha3*N_(3))_max.
```

Der zweite Bereich koenne bei `k=2` wegen `alpha3>1` auftreten. H006/H015
listen demgegenueber:

```text
(a) W4=0,
(b) 0<W4<=1,
(c) W4>1.
```

Die Zusammenfassung von Null- und positivem Einheitsintervall in H004 ist
noch kein inhaltlicher Widerspruch, weil H004 `W4=0` spaeter gesondert als
Divergenz behandelt. Der zusaetzliche gedruckte obere Bereich
`(alpha3*N_(3))_max` ist in H006/H015 an dieser Stelle jedoch nicht
vorhanden.

## 5. TRC ist nicht pauschal ein floor-Operator

H004 definiert `TRC` woertlich dadurch, dass Dezimalstellen nicht
aufgerundet, sondern abgeschnitten werden. Es nennt eine Ausnahme:

```text
TRC(0,99...99) = 1,
```

wenn sich die Neunerfolge bis zu einer Dezimalstelle `x` erstreckt, die
unter der Messbarkeitsschranke liegt. Als Gegenbeispiel druckt die Quelle

```text
TRC(e) = 2.
```

Fuer nichtnegative Werte ausserhalb des Sonderfalls wirkt das wie die
ganzzahlige Abschneide-/floor-Funktion. Wegen des ausdruecklichen
`0,99...99`-Sonderfalls ist `TRC` aber nicht quellengetreu pauschal mit dem
mathematischen floor-Operator gleichzusetzen. Das Buch gibt keinen
Zahlenwert fuer `x` und keine maschinelle Toleranz an.

H006/H015 benennen keinen `TRC`-Operator. Ihr Vermerk verlangt ebenfalls
Abschneiden statt Aufrunden und behandelt `,99...99=1` als Identitaet,
grenzt die Neunerfolge aber nicht mit der in H004 gedruckten
Messbarkeitsschranke/Dezimalstelle `x` ein.

## 6. H004: W5, Saettigung und regulaere Auswahl

Zur Bestimmung der vierten Besetzung definiert Druck 341 den zunaechst
reellen logarithmischen Wert `W5` durch die exakte Gleichheit

```text
(2k-1)*W5 = -3*Q4*ln(W4).
```

Die anschliessende Ganzzahlwahl ist ein getrennter Schritt.

### 6.1 Saettigung

Bei

```text
W4=0  ->  W5 -> infinity
```

oder bei

```text
W5 > alpha3*N_(3)
```

gilt nach H004 die Maximalbesetzung

```text
N_(4) = TRC(alpha3*N_(3)).
```

Zusaetzlich brauche `beta4=1` aus (107a) nur dann durch

```text
N_(4) = TRC(alpha3*N_(3))-1
```

beruecksichtigt zu werden, wenn

```text
TRC(alpha3*N_(3)) > alpha3*N_(3).
```

Das ist eine explizite Sattigungs-/Zaehlauswahl, keine Loesung von
`ln(0)`. Der zweite Sattigungsgrund `W5>alpha3*N_(3)` ist in der
H006/H015-Fallbeschreibung nicht entsprechend ausgeschrieben.

### 6.2 Regulaerer Bereich

Ist dagegen

```text
W5 <= alpha3*N_(3),
```

dann setzt H004

```text
N_(4) = TRC(W5).
```

H006/H015 schreiben fuer `0<W4<=1` unmittelbar

```text
K4*(2k-1) = -3*Q4*ln(W4)
```

und verlangen erst im nachfolgenden Vermerk Ganzzahligkeit/Abschneiden.
Sie unterscheiden den reellen Logwert nicht durch ein eigenes Symbol von
der schliesslich ganzzahligen Auswahlzahl.

Im H006/H015-Nullfall wird als maximaler Wert

```text
K4 = alpha3*K3
```

gesetzt. Eine dem Buch entsprechende `TRC`-Schreibweise und die bedingte
`beta4`-Korrektur stehen dort nicht in der Fallpassage.

## 7. H004: negativer W5 und Transferwert W6

Druck 341 sagt, bei `k=2` sei auch `W5<0` moeglich. Ist Zone `j=3`
urspruenglich mit `N'_(3)` besetzt, koenne wegen des gleichen linearen
Charakters von `G4` und `delta3 G3=alpha3*N'_(3)` ein
Protosimplextransfer von `j=3` nach `j=4` erfolgen.

Der Text beginnt den Schritt mit

```text
W6 = W5 + alpha3*N'_(3)
```

und bezeichnet die naechste absteigende Zugabe mit
`alpha3*(N'_(3)-1)`. Er gibt die Wiederholung anschliessend in Summenform:

```text
W6 = W5 + alpha3*sum_mu (N'_(3)+1-mu) >= 0,
N_(3) = N'_(3)-mu.
```

Zusaetzlich fordert die Quelle

```text
W6 <= alpha3*N_(3)
```

gemaess (107) und merkt an, im Allgemeinen genuege `mu=1`, um `W6>=0`
zu erreichen. Fuer `W4>1` wird dann

```text
N_(4)=TRC(W6)
```

gesetzt, vorausgesetzt der Transfer belaesst `N_(3)>=0`. Andernfalls sei
der Term als `c`- oder `d`-Struktur verboten. Druck 342 begruendet weiter,
warum ein analoger Transfer von `j=2` nach `j=3` oder von `j=1` nach
`j=2` nach der dortigen Polynomstruktur nicht moeglich sei.

Damit legt H004 Anfangsbesetzung, absteigende Zugaben, Wiederholungszahl,
Endbesetzung und zwei Nachbedingungen ausdruecklicher fest als H006/H015.
Es handelt sich weiterhin um eine vom Buch behauptete Auswahlregel; die
Seiten liefern keinen separaten Beweis, dass sie aus allen denkbaren
Eingaben eine zulaessige Loesung erzeugt.

## 8. Enger Vergleich des W4>1-Falls

| Punkt | H004 Buchfassung | H015 fotografierter Text | H006 IGW-Wiedergabe |
|---|---|---|---|
| negativer Logwert | eigenes Symbol `W5<0` | `K4<0` | erste Stelle druckt nacktes `K<0`; danach `K4<0` |
| Rueckschritt | `N_(3)=N'_(3)-mu` | `K3` um 1 vermindert | `K3` um 1 vermindert |
| Addition | absteigende Reihe ab altem `N'_(3)` | `alpha3*K3` zu `K4<0`, Vor-/Nachwert nicht indiziert | ebenso; Vor-/Nachwert nicht indiziert |
| neuer Wert | `W6` mit Summenform | neuer `K4>=0` | neuer `K4>=0` |
| Wiederholung | „so oft ... bis“, Summenindex `mu` | keine Schleife formuliert | keine Schleife formuliert |
| Nachpruefung | `W6>=0`, `W6<=alpha3*N_(3)`, `N_(3)>=0` | nur neuer Wert `K4>=0`; `K3>0`, sonst verboten | ebenso; K3=0-Prosa in den Haupttext integriert |
| Ganzzahlabschluss | `N_(4)=TRC(W6)` | allgemeiner Abschneidevermerk fuer `K_j` | allgemeiner Abschneidevermerk fuer `K_j` |

H015 setzt die `K3=0`-Erklaerung als Sternfussnote auf den folgenden
sichtbaren Blattteil; H006 integriert denselben Gedanken in den laufenden
Absatz. Diese Satzanordnung und die H006-Formelnummern duerfen nicht als
Beweis einer unveraenderten Urschrift behandelt werden.

## 9. Was der Vergleich belegt und offen laesst

Belegt ist:

- Alle drei Quellen verwenden eine kubisch-quadratisch-linear-
  exponentielle Exhaustionsidee und bilden vor der vierten Auswahl einen
  nichtnegativen Rest `W4`.
- Die logarithmische Umkehrung hat denselben lokalen Faktor
  `-3Q4/(2k-1)`.
- Alle drei verbinden die vierte Besetzung mit einer oberen Strukturgrenze
  aus dritter Besetzung und `alpha3` sowie mit einer Abschneideentscheidung.
- H004 praezisiert diese Idee durch `TRC`, `W5`, `W6`, Sattigung und eine
  iterative Transferform.

Offen bleibt:

- ob H004 eine redaktionelle Ausarbeitung, theoretische Revision oder nur
  ausfuehrlichere Darstellung derselben Autorvorstellung ist;
- ob die in H004 verwendeten `N_(j)` in jedem Eingabekontext exakt dieselben
  Werte wie H006/H015-`K_j` annehmen;
- ob der H004-Transfer unter allen zulaessigen Eingaben terminiert und alle
  gedruckten Bedingungen zugleich erfuellt;
- welche endliche numerische Regel die jeweilige `0,99...99`-Erkennung
  implementieren soll.

Der engste quellenfeste Schluss ist daher: **Die Buchfassung schliesst den
W4>1-Ablauf wesentlich weiter als H006/H015, insbesondere durch die
expliziten Zwischenwerte W5/W6 und die `mu`-Transferfolge. Sie ist aber
nicht ohne weiteren Editionsbeleg als wortgleiche oder rueckwirkend
verbindliche Fassung des 1982 zugeschriebenen Textes einzusetzen.**
