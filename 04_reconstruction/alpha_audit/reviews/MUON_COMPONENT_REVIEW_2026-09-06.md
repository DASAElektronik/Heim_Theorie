# H006 x3/mu-: Komponenten- und Ladungszuordnung

Stand: 2026-09-06. Eng begrenzte visuelle Quellenreview von H006
Druck/PDF2--3 und bedingtem N=0-Kontext auf Druck/PDF8. Keine Besetzungs-
oder Massenrechnung.

## 1. Ergebnis

H006(III) ordnet dem Eintrag

```text
x3 (0111)_0(-1,-1) == x3 (0111)_0(-1) == (mu-) Pseudosingulett
```

quellenintern eindeutig die Konfigurationswerte

```text
epsilon=+1, k=1, B=0, P=1, Q=1, kappa=1, C=0
```

zu. Wegen `P=1` besitzt die allgemeine Ladungsdarstellung die beiden
nullbasierten Stellen `x=0,1`. Direktes Einsetzen in H006(II) ergibt fuer
beide Stellen `q_x=-1` und daher `q=|q_x|=1`. Die doppelte Ladungsliste der
Tabelle ist somit kein OCR-Zufall, sondern stimmt mit der gedruckten
Ladungsformel ueberein.

Die anschliessende Gleichsetzung mit einer einstelligen Liste und die
Bezeichnung „Pseudosingulett“ zeigen eine von H006 behauptete
Zusammenziehung/Identifikation. Die geprueften Seiten erklaeren jedoch
nicht, ob dies als exakt ein physischer Zustand, als degenerierte formale
Komponenten oder als andere Identifikationsregel zu lesen ist. Insbesondere
ist weder `(0111)` noch `(-1)` ein Besetzungsquadrupel `n1..n4`.

## 2. Quelle und Bildkontrolle

Quelle:

`01_sources/heim_primary/Massenformel_nach_B_Heim_1982.pdf`

H006 ist die IGW-Wiedergabe 2002/2003 eines auf 25.2.1982 datierten und
Heim zugeschriebenen Textes, kein hier authentifiziertes Urschriftfaksimile.

Visuell geprueft:

- Druck/PDF2: Symboldefinitionen und Gleichung (I);
- Druck/PDF3: Ladungsformel (II), allgemeine Multiplettdarstellung und
  Tabellenzeile `x3` in (III);
- Druck/PDF8: Bedeutung von `N=0`, `f=0` und Auswahl des
  Besetzungsquadrupels, nur als spaeterer Kontext.

Bildanker:

- `tmp/pdfs/n0_alias/h006-02.png`
- `tmp/pdfs/n0_alias/h006-03.png`
- `tmp/pdfs/n0_alias/h006-08.png`

Die Bilder sind der tragende Beleg fuer Indizes, Vorzeichen und die
Gleichsetzung der beiden `x3`-Schreibweisen. Die PDF-Textschicht wurde nicht
als Ersatz fuer die visuelle Lesung benutzt.

## 3. Wie die Signatur gelesen wird

H006 Druck/PDF3 gibt vor (III) die allgemeine Darstellung an:

```text
x_nu (epsilon*B, epsilon*P, epsilon*Q, epsilon*kappa)_(epsilon*C)
     (q_0,...,q_P).
```

Die Tabelle steht ausdruecklich unter „Moegliche Multipletts fuer
`epsilon=+1`“. Deshalb werden die vier Ziffern der `x3`-Signatur `(0111)`
bei positivem `epsilon` unmittelbar gelesen als:

| Signaturstelle | Wert | Folgerung |
|---|---:|---|
| `epsilon*B` | 0 | `B=0` |
| `epsilon*P` | 1 | `P=1` |
| `epsilon*Q` | 1 | `Q=1` |
| `epsilon*kappa` | 1 | `kappa=1` |
| Subskript `epsilon*C` | 0 | `C=0` |

Die Zeile steht im Abschnitt `k=1`. Unabhaengig davon gibt H006(I)
`B=k-1`, was fuer `k=1` erneut `B=0` liefert. Aus `I=P+1` folgt formal
`I=2`; die Ladungsliste wird aber nullbasiert als `q_0,...,q_P` notiert.
Fuer `P=1` sind das genau die Stellen `x=0` und `x=1`.

Die Symbolprosa auf Seite 2 beschreibt Komponenten zunaechst mit
`1<=x<=I`, waehrend (II) ausdruecklich `0<=x<=P` und die Tabelle
`q_0,...,q_P` verwendet. Fuer die vorliegende Substitution ist deshalb der
unmittelbare Definitionsbereich von (II) massgebend. Eine stillschweigende
Gleichsetzung dieser null- und einsbasierten Schreibweisen ueber den lokalen
Ladungsnachweis hinaus wird nicht vorgenommen.

Diese Ziffern sind Konfigurations-/Multiplettangaben. Sie sind keine vier
Zonenbesetzungen und keine aus einer Masse ermittelten Parameter.

## 4. Direkte Substitution in Gleichung (II)

H006(II), Druck/PDF3, druckt fuer `0<=x<=P`:

```text
2*q_x = (P-2*x)[1-kappa*Q*(2-k)]
        + epsilon[k-1-(1+kappa)*Q*(2-k)] + C,
q=|q_x|.
```

Setze nur die aus (III) gelesenen Werte
`epsilon=k=P=Q=1` und `C=0`. Dann gilt:

```text
1-kappa*Q*(2-k) = 1-1 = 0,
k-1-(1+kappa)*Q*(2-k) = 0-2 = -2.
```

Die beiden Kopplungsstellen enthalten in der Quelle `kappa`; das freie `k`
steht weiterhin in `(2-k)` und `k-1`. Im vorliegenden Tabellenfall sind
`k=kappa=1`, weshalb die numerische Substitution zwar gleich aussieht, die
Symbole aber nicht allgemein vertauschbar sind.

Der erste, von `x` abhaengige Summand verschwindet also an beiden Stellen.
Damit folgt ohne numerische Naeherung:

```text
x=0: 2*q_0 = -2, also q_0=-1,
x=1: 2*q_1 = -2, also q_1=-1,
jeweils q=1.
```

Dies reproduziert exakt die in (III) gedruckte Liste `(-1,-1)`. Die
einstellige Schreibweise `(-1)` entsteht nicht durch eine andere Wahl von
`x`, sondern wird von der Quelle selbst mit der zweistelligen Schreibweise
gleichgesetzt.

## 5. Komponentenidentitaet: belegt und offen

Quellenbelegt ist:

- Die formale Regel `I=P+1` liefert bei `P=1` zwei Komponentenstellen.
- Die Ladungsregel (II) gibt beiden Stellen dieselbe Ladungszahl `-1`.
- (III) setzt `x3(0111)_0(-1,-1)` mit `x3(0111)_0(-1)` gleich.
- Die resultierende Zeile wird `(mu-) Pseudosingulett` genannt.

Nicht auf den geprueften Seiten definiert ist:

- welches mathematische Aequivalenzkriterium die zwei Stellen zu einer
  einstelligen Liste zusammenzieht;
- ob eine Multiplizitaet von zwei erhalten bleibt oder vollstaendig
  identifiziert wird;
- ob beide formalen `x`-Werte in spaeteren Formeln getrennt durchlaufen
  werden duerfen;
- ob die Quellenbezeichnung `(mu-)` bereits eine unabhaengig hergeleitete
  physikalische Identifikation oder zunaechst eine Tabellenzuordnung ist.

Fuer einen Eingabevertrag darf deshalb quellenfest `q_x=-1,q=1` benutzt
werden. Die Komponentenstelle muss aber entweder explizit festgelegt oder
die Gleichheit beider Eingaben vor einer Zusammenziehung gezeigt werden.
Eine doppelte Gewichtung oder Zustandszahl darf aus `(-1,-1)` nicht ohne
weitere Quellenregel erfunden werden.

## 6. Bedingter N=0-Anschluss

Die Ueberschrift auf Druck/PDF3 bezeichnet (III) als moegliche Multipletts
der Grundzustaende. Druck/PDF8 praezisiert spaeter den Rechenkontext:
Die Resonanzordnung `N>=0` waehlt Besetzungsparameterquadrupel `n_j`; bei
`N=0` wird `f=0` und (XXVI) soll die `n_j` des Zustands bestimmen.

Damit ist `x3` ein quellenbelegter Kandidat fuer einen H006-internen
N=0-Auswahlversuch. Daraus folgt noch nicht:

- ein bestimmtes `n=(n1,n2,n3,n4)`;
- `W_(nu,x)`, denn dafuer muss die Strukturpotenz (XVI)--(XIX) mit
  `kappa=1` ausgewertet werden;
- ein bestimmter `K4/W4`-Zweig;
- eine Masse oder ein Vergleich mit einer beobachteten Myonmasse.

Anders als beim zuvor untersuchten `x2/e-`-Fall verschwindet der
`kappa`-Anteil nicht schon durch `kappa=0`; hier gilt gerade `kappa=1`.
Das Elektron-Nulltupel darf daher nicht als vermeintlich gleiche
Mesonenbelegung importiert werden.

## 7. Enger Eingabestatus

Vor einer weiteren Auswahlrechnung ist aus H006 sicher festhaltbar:

```text
Quelle/Fassung = H006
Tabellenanker  = Druck/PDF3, (III)
epsilon,k      = +1, 1
B,P,Q,kappa,C  = 0, 1, 1, 1, 0
x-Bereich      = 0,1
q_x            = -1 fuer beide formalen Stellen
q              = 1
N              = 0 nur als benannter Folgekontext
n_j, K_j, W    = noch nicht aus dieser Review bestimmt
Masse          = nicht berechnet
```

Der positive Abschluss ist die versionsgebundene Komponenten- und
Ladungsbruecke. Die Pseudosingulett-Identifikation, die Besetzung und der
Auswahlzweig bleiben getrennte naechste Fragen.

## 8. Statischer Code-Nachtrag

Zusaetzlich wurden am 2026-09-06 ausschliesslich lesend geprueft:

- `04_reconstruction/alpha_audit/muon_selection_inputs.json`;
- `scripts/audit_muon_selection.py`;
- die vom Skript aufgerufenen reinen Hilfsfunktionen `mathematical_pi`,
  `eta_k_q`, `equation_rhs`, `solve_branches`, `stringify` und
  `verify_sources` aus `scripts/audit_alpha.py`.

Kein historisches Programm wurde ausgefuehrt. Diese Codegegenlesung ist
eine Implementierungspruefung, kein neuer Quellen- oder Physikbeleg.

### 8.1 Positiver Quellenanschluss

Der JSON-Vertrag friert genau den oben belegten Zustand ein:

```text
x3/mu-, epsilon=1, k=P=Q=kappa=1, C=0,
x=[0,1], qx=-1, q=1, N=0.
```

`validate_inputs` vergleicht dieses Zustandsobjekt kanonisch mit einer
festen Codekonstante; dadurch werden auch als Integer getarnte Bool-Werte
zurueckgewiesen. `component_charge` verwendet nach erneuter
Glyphenkontrolle die richtige H006-(II)-Form:

```text
(P-2x)[1-kappa*Q*(2-k)]
+ epsilon[k-1-(1+kappa)Q(2-k)] + C.
```

Beide zugelassenen Indizes liefern im festen Vertrag `q_x=-1`.

Die reduzierte Strukturpotenz stimmt mit der getrennten Quellenreduktion
fuer `k=P=Q=kappa=q=1` ueberein:

```text
d  = eta_(1,1),
w1 = d*A16,
w2 = A26+d^2*A31,
w  = w1+(1+w2)^0 = 1+d*A16.
```

Der Code prueft dabei `1+w2` auf Endlichkeit und Nichtnullsein, bevor er
den Exponenten null auswertet. Er behandelt den potenziell undefinierten
Ausdruck also nicht still als belangloses `0`-Produkt. Weitere fuer die
Reduktion relevante Nenner/Domaenen werden vor der Auswahl geprueft.

Auch der Basisanstieg ist fuer `Q_j=(3,3,2,1)` und `k=1` richtig reduziert:

```text
g = 27*alpha1+9*alpha2+2*alpha3+exp(-1/3),
W = g*w.
```

Die drei Greedy-Schritte benutzen die Koeffizienten
`(alpha1,alpha2,alpha3)` mit Potenzen `(3,2,1)`. Der vierte Schritt wird
nur fuer `0<W4<=1` ausgewertet und nutzt `K4_raw=-3 ln(W4)`, also den
H006-Fall (b) bei `k=Q4=1`. Fall (a)/(c) wird ausdruecklich abgebrochen und
nicht durch eine erfundene Sonderregel geschlossen.

### 8.2 Fassungs- und Sensitivitaetsachsen

Der Vertrag deklariert drei reine Zahlenprofile und je zwei vorab benannte
Lesarten fuer `A16` und die `alpha3`-Wurzel, insgesamt zwoelf Zellen. Die
zweite `xi`-Variante und die linkassoziative `A16`-Variante sind als
Sensitivitaeten benannt, nicht als durch einen Zielwert ausgewaehlte
Quellenfassungen.

Die `alpha3`-Form ist die festgehaltene H006-Lesart, nicht die spaetere
H010-Form. `A16` hat als Default die dokumentierte Nennerproduktlesart;
die linkassoziative Variante bleibt sichtbar getrennt. `A26` verwendet die
bereits dokumentierte Nennerproduktnormalisierung. Der Exponentialoperator
und der Logarithmus bleiben mathematische Funktionen; ein gedruckter
`e`-Wert ersetzt nur die als Koeffizient auftretende Eulersche Zahl.

Der Code importiert aus `audit_alpha` keine moderne Vergleichszahl in die
Rechnung. Er ruft nur den 1982-Hilfszweig fuer nacktes `alpha/beta` auf.
JSON und Validierung verlangen zugleich:

```text
comparison_or_fit_inputs = [],
dimensional_constants = {},
target_fitting = false,
mass_evaluation = false.
```

Es gibt keinen Aufruf eines Massenrechners, keine `mu`-Konstante, keinen
kg-/MeV-Faktor und kein Sollmassenfeld. Das Ergebnisobjekt bezeichnet seinen
Scope ebenfalls als W-/Auswahldiagnostik ohne Masse oder physikalische
Unsicherheit.

### 8.3 Konkrete Code- und Vertragsgrenzen

1. **Ladungsinvariante nach Review gehaertet.** Der aktualisierte Code
   berechnet `component_charge(x)` fuer beide Stellen und bricht nun ab,
   falls ein Ergebnis nicht `STATE["qx"]` entspricht oder sein Betrag von
   `STATE["q"]` abweicht. Damit ist die Quelle-zu-Zustand-Bruecke nicht nur
   Ausgabe, sondern Laufzeitinvariante. Die neuen Tests decken auch einen
   gemockten abweichenden Ladungswert ab.

2. **Semantische Metadaten nach Review gesperrt.** `FIXED_POLICY` fixiert
   nun Schema, Datum, Normalisierungs-ID, das vollstaendige Quellobjekt mit
   Pfad/Hash/Locator/Provenienz, Exp-/Log-Policy, Auswahlpfad und die
   massenfreien Scopefelder. `validate_inputs` weist unbekannte oder fehlende
   Top-Level-Felder sowie Abweichungen davon zurueck. Zustand, Profile,
   Alpha-Modell und Lesarten bleiben separat exakt verglichen; JSON-basierte
   Vergleiche unterscheiden dabei auch `false/true` von `0/1`.

3. **Bewusste Grenze: Quellhashpruefung ist optional.** `--verify-sources` prueft H006, der
   normale Rechenlauf und `--check` tun dies nicht automatisch. Ein
   erfolgreicher Snapshotvergleich allein ist daher keine Quellenpruefung.

4. **Bewusste Grenze: Grenzentscheidungen sind punktweise
   Decimal-Entscheidungen.** Die
   Vergleiche im Greedy-Loop, die Einteilung `W4=0`, `0<W4<=1`, `W4>1` und
   `floor(-3 ln W4)` arbeiten mit einem endlichen Decimal-Punktwert. Das
   Skript erlaubt 40--200 Stellen und berichtet Abstaende, konstruiert aber
   keine nach aussen gerundeten Intervalle. Nahe einer K-/Fallgrenze kann
   der Code allein deshalb keine zertifizierte Entscheidung beanspruchen.
   Stabilitaet ueber mehrere Praezisionen ist ein guter Regressionstest,
   aber nicht automatisch ein Intervallbeweis.

5. **Bewusste Grenze: `exact_zone_boundary_in_decimal_evaluation` ist enger als
   mathematische Exaktheit.** Das Feld testet nur, ob ein mit der aktuellen
   Decimal-Auswertung erzeugter Randabstand exakt als Decimal-Null vorliegt.
   Es darf nicht als Quellenbeweis einer exakten algebraischen Zonengrenze
   beschrieben werden.

6. **Der Algorithmus ist absichtlich zustandsspezifisch.** Die Reduktion
   von (XVI)--(XIX) ist hart auf den `x3`-Vertrag zugeschnitten; sie ist kein
   generischer Heim-Zustandsloeser. Die Schleifengrenze `10000` ist ein
   technischer Abbruch des Diagnosecodes, keine Quellenobergrenze.

### 8.4 Schluss des Codechecks

Der nachgehaertete Zahlenpfad bleibt im vereinbarten Scope: H006-gebundene
`x3`-Eingaben, `W`, Fall-(b)-Auswahl und Rest-/Strukturdiagnostik, ohne
Massenimport oder Fit. Die zuvor offenen Punkte Ladungsinvariante und feste
Metadaten sind im Code geschlossen und durch Mutationstests abgesichert.
Die verbleibenden Reichweitengrenzen sind die optionale Ausfuehrung der
Quellhashpruefung und die bewusst nicht als Intervallzertifikat ausgegebenen
Decimal-Grenzentscheidungen.

Die gemeldete unabhaengige Hochpraezisionsgegenrechnung verglich 252
gemeinsame Werte mit maximaler absoluter Abweichung unter `1e-115` und
denselben `K/n`; 15 Tests decken nun auch Policy-/Typmutationen und die
Ladungsinvariante ab. Es wurden dafuer keine neuen Profile oder
Snapshotwerte eingefuehrt. Diese Kontrollen erhoehen die Reproduzierbarkeit,
ersetzen aber kein nach aussen gerundetes Intervallzertifikat. Auch die
technischen Haertungen leiten weder die Pseudosingulett-Deutung noch eine
physikalische Myonmasse her.
