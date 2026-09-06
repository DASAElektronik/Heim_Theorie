# Was bedeuten Energie, Masse und Wellenlaenge vor Heims Alpha-Gleichung?

Stand: 2026-09-06. Vierte begrenzte Rekonstruktionsetappe.
Ausgangspunkt: `CHARGE_DERIVATION_2026-09-06.md` und der Energieordnungsbefund.

## Ergebnis in verstaendlicher Form

Wir haben die verwendeten Formeln bis zu frueheren Buchstellen verfolgt.
Heim setzt vor seiner Alpha-Gleichung nicht einfach die gewoehnliche
Bewegungsenergie eines Elektrons und dessen de-Broglie-Wellenlaenge ein.
Er verwendet `E_k=pc` und `lambda_H=h/(mc)`. Das steht tatsaechlich im Druck
und ist kein OCR-Fehler. Die Bezeichnung dieser Energie als kinetisch hat
Vorlaeufer in Band I. Die physikalische Rechtfertigung folgt daraus nicht.

Bei der Geschwindigkeit aus dem kleinen Buchzweig ist `pc` rund 274-mal
so gross wie die uebliche, von der Ruheenergie getrennte Bewegungsenergie.
Die Wellenlaengen `h/p` und `h/(mc)` unterscheiden sich um rund den Faktor137.
Dies sind Unterschiede zwischen Formeln, keine Rundungsfehler. Es bleibt
zu klaeren, ob Heim unterschiedliche physikalische Groessen meint und wie
diese an seine Energieerhaltung und seine Atomgeometrie angeschlossen sind.

Unsere Diagnose ersetzt keine Quellformel. Sie zeigt genau, welche Schritte
eine begruendete Neuformulierung benoetigen wuerden.

## 1. Quellen und Begriffszuordnung

Die PDF-Seiten werden einzeln geprueft: In Band I ist der Offset zur
gedruckten Seite NICHT konstant. Beispielsweise Druck12=PDF20,
Druck81=PDF88, Druck233=PDF239. OCR allein reicht fuer diese Angaben nicht.

| Quelle | Was dort steht | Was daraus noch nicht folgt |
|---|---|---|
| EDM1 Druck12 / PDF20 | `m*sqrt(1-beta^2)=m0`, `p=mv`, `E_Q=pc`; Wellenfeldansatz und `p*lambda=h` als de-Broglie-Gleichung | Dass jede spaeter verwendete Wellenlaenge dieselbe Welle bezeichnet |
| EDM1 Druck81 / PDF88 | `E_k^2=(M^2-M0^2)c^4`, positive Form `E_k=Mcv`; als kinetische Energie und bekannte Darstellung bezeichnet | Gleichheit mit der gewoehnlichen Bewegungsenergie |
| EDM1 Druck233 / PDF239 | `mc*lambda_C=h`, metaphorischer Radius; dort ausdruecklich keine zirkulaere Welle | Uebertragbarkeit dieser Aussage aus dem lokalen Neutralteilchenkontext auf jedes gebundene System |
| EDM1 Druck242 / PDF248 | `E_+=ch/lambda_q`, `lambda_q=2*pi*r_q` fuer die photonische Komponente | Dieselbe Kreiswellen-Deutung fuer ein massives Elektron |
| EDM1 Druck288 / PDF294, (H1) | `m=m0/sqrt(1-beta^2)`, `E^2=p^2*c^2`, `p*lambda=h`, `nu=c/lambda` | Physikalische Ableitung von `E=pc` als mechanischer Bewegungsenergie |
| EDM2 Druck299/300 / PDF305/306 | Energieaufteilung `X+E=const`, ohne Ruheanteile; `v_H=c*alpha` | Dass Ausschluss der Ruheanteile automatisch `E=pc` begruendet |
| EDM2 Druck301 / PDF307 | `E_k=m*v_H*c`, `mc^2=ch/lambda_H`, `lambda_H=2*pi*r_H`, `y=r_H*sqrt(1-alpha^2)` | Eine vollstaendige kinematische Herleitung dieser gemeinsam eingesetzten Beziehungen |

Quellenagenten und Hauptagent haben die tragenden Seiten visuell kontrolliert.
Die Quelle nennt die Ausdruecke invariant bzw. aus Relativitaet folgend.
Das ist ein zu pruefender Quellenanspruch, keine von uns bestaetigte Eigenschaft.
Insbesondere ist der Betrag `pc` bei gewoehnlichem Wechsel des Inertialsystems
kein Lorentzskalar; eine invariante Gleichungsform ist von einem invarianten
Zahlenwert zu unterscheiden. Was Heims `A_-` im jeweiligen Zusammenhang
leisten soll, muss gesondert rekonstruiert werden.

Editionsgrenze: EDM1 ist die dritte, geaenderte Auflage1998; EDM2 die zweite,
unveraenderte Auflage1996. Die gefundenen Band-I-Stellen sind sachliche
Quellenanker. Ohne Vergleich frueherer Ausgaben behaupten wir damit keinen
historischen Erstbeleg der genauen Formulierungen.

## 2. Drei verschiedene Energieausdruecke

Wir schreiben zur Entflechtung der Symbole:

```text
beta = v/c,  0<beta<1
s = sqrt(1-beta^2),  gamma = 1/s
m = gamma*m0,  p = m*v.
```

`m0` bezeichnet die Ruhemasse. `m` bezeichnet in dieser Lesart eine
geschwindigkeitsabhaengige Masse. Die Verwendung derselben Lesart fuer
`m(v_H)` in Band II ist eine dokumentierte Brueckenannahme: Die lokale
Band-II-Passage druckt die genaue Funktion nicht noch einmal aus.

| Groesse | Ausdruck | In Einheiten `m0*c^2` |
|---|---|---|
| Energie einschliesslich Ruheanteil | `E_tot=mc^2` | `gamma` |
| Uebliche Bewegungsenergie | `T=E_tot-m0*c^2` | `gamma-1` |
| Heims hier verwendete positive Energie | `E_pc=pc=beta*mc^2` | `beta*gamma` |

Die Standard-Bewegungsenergie ist bereits in Einsteins Originalarbeit1905,
Paragraph10, Druck920/PDF30 als `mu*c^2*(1/sqrt(1-(v/c)^2)-1)` angegeben
(dort heisst die Lichtgeschwindigkeit `V`). Wir verwenden diese historische
Primaerquelle ausschliesslich zur Begriffskontrolle, nicht als vorgezogene
Recherche nach neueren Widerlegungen:
[Einstein1905, Originalscan](https://myweb.rz.uni-augsburg.de/~eckern/adp/history/einstein-papers/1905_17_891-921.pdf).

Die Unterscheidung laesst sich ohne Messwerte sehen:

```text
pc = sqrt(E_tot^2 - (m0*c^2)^2)
T  = E_tot - m0*c^2.
```

Eine Wurzel aus der Differenz der Quadrate ist nicht die Differenz der
Groessen. Heims Gleichung ist algebraisch mit `p=mv` und `m=gamma*m0`
vertraeglich, wenn wir damit eine Groesse `pc` definieren. Die Identifikation
dieser Groesse mit mechanischer Bewegungsenergie ist ein anderer Schritt.

Ein exaktes Lehrbeispiel: Fuer `v=0.6c` sind `s=0.8`, `gamma=1.25`.
Dann betraegt die Gesamtenergie `1.25*m0*c^2`, die Bewegungsenergie
`0.25*m0*c^2`, aber `pc=0.75*m0*c^2`. Letzteres ist dreimal so gross.

Allgemein folgt

```text
pc/T = beta/(1-s) = (1+s)/beta > 1.
```

Bei kleinen Geschwindigkeiten ist `pc` fuehrend proportional zu `v`,
waehrend `T` fuehrend proportional zu `v^2` ist. Beide verschwinden fuer
v gegen null; das macht sie trotzdem nicht austauschbar.

Auch die Arbeitserhaltung braucht eine klare Zuordnung: Unter den hier
verwendeten mechanischen Definitionen folgt aus `p=gamma*m0*v`
die Beziehung `dT=v*dp`, waehrend `d(pc)=c*dp` gilt. Wird stattdessen `pc`
in eine Arbeits-/Potentialbilanz eingesetzt, muss die passende physikalische
Begruendung oder eine geaenderte Dynamik angegeben werden. Sie folgt nicht
allein aus dem Lorentzfaktor. Noch kein Urteil ueber alle Heim-Energiebegriffe.

Korrektur unserer vorherigen Notiz: `mc^2` in EDM2 Druck301 pauschal
Ruheenergie zu nennen war nicht gerechtfertigt. Bei `m=gamma*m0` gehoert
der Ruheanteil zu `m0*c^2`. Der fruehere Korrelationsbericht wird entsprechend
praezisiert; die Rechnung aendert sich nicht.

## 3. Die Wellenlaengenfrage

Aus dem konkret eingesetzten `mc^2=ch/lambda_H` folgt zwingend

```text
lambda_H = h/(mc).
```

Die anderweitig im Buch angegebene Beziehung `p*lambda=h` liefert dagegen
bei demselben `p=m*v`:

```text
lambda_dB = h/p = h/(beta*mc)
lambda_dB/lambda_H = 1/beta.
```

Gleichheit der zwei Wellenlaengen wuerde `beta=1` verlangen, ausserhalb
des verwendeten massiven Teilchenbereichs. Dies ist NUR dann ein Widerspruch,
wenn wirklich dieselbe Welle, Masse und Bezugsbeschreibung gemeint sind.
Verschiedene Wellenlaengen koennen widerspruchsfrei nebeneinander existieren.

Band I unterscheidet sogar Kontexte: Auf Druck233 wird die Compton-Skala
nicht als Kreiswelle aufgefasst; auf Druck242 wird eine Kreiswelle fuer
eine photonische Komponente verwendet. Band II Druck301 benoetigt eine
zirkulaere Elektronenwelle. Ein nachvollziehbarer Uebergang zwischen diesen
Kontexten ist die offene Aufgabe. Die Namensaehnlichkeit allein ersetzt ihn
nicht. `h/(mc)` nennen wir hier deshalb Compton-artig, nicht automatisch
die mit der invarianten Ruhemasse definierte Compton-Wellenlaenge.

## 4. Welche Laenge berechnet die Quellenkette?

Die Quelle setzt Umfang, Wellenlaenge und Lorentzfaktor zusammen:

```text
lambda_H=2*pi*r_H,   y=r_H*s.
```

Mit `L0=hbar/(m0*c)` als blosser Laengeneinheit folgt bedingt:

```text
r_H = hbar/(mc) = L0*s
y   = L0*s^2 = L0*(1-beta^2).
```

Beim kleinen Buchzweig ist `y/L0` rund0.99994675. Die Rechnung erzeugt also
eine Laenge nahe dieser Compton-Skala. Damit haben wir keinen beobachteten
Wasserstoffradius bestimmt. Der Quellenkontext nennt `y` zwar die Distanz
zwischen p und e; die Verbindung zu einer definierten Messgroesse bleibt
zu pruefen. Keine gemessene Elektronenmasse und kein moderner Atomradius
wurden in diesen dimensionslosen Vergleich eingegeben.

Die pauschale Verkuerzung eines K-Schalenmeridians um `s` ist in der
untersuchten Passage gesetzt, nicht durch eine ausgeschriebene Transformation
einer Kreisbewegung hergeleitet. Bezugssystem, Gleichzeitigkeit und die Art
der geometrischen Laenge muessen dazu erst feststehen.

## 5. Warum diese Begriffe fuer Alpha entscheidend sind

Die Energiegleichung unmittelbar vor (105) lautet

```text
e_minus^2*(1-C) = 4*pi*epsilon0*y*E.
```

Wir halten sie fuer die Diagnose fest und benennen zwei moegliche
Ersetzungsschritte getrennt. Schreibe allgemein

```text
E = f(beta)*mc^2
lambda = g(beta)*h/(mc)
r = lambda/(2*pi),  y=r*s
alpha_prime = e_minus^2/(4*pi*epsilon0*hbar*c).
```

Dann kuerzen sich m und die dimensionalen Konstanten heraus:

```text
K := alpha_prime*(1-C) = g(beta)*f(beta)*s.
```

Alle Terme hier sind dimensionslos. Vor dem Kuerzen haben `y*E` und
`hbar*c` beide die Einheit Joule mal Meter. Die Ladungsgleichung hat auf
beiden Seiten die Einheit Coulomb zum Quadrat.

| Rechnung | Energie f | Wellenlaenge g | Rechte Seite fuer K |
|---|---|---|---|
| Quellenansatz | `beta` | `1` | `beta*s` |
| Nur Energie probeweise ersetzt | `1-s` | `1` | `s*(1-s)` |
| Energie und Wellenlaenge probeweise ersetzt | `1-s` | `1/beta` | `s*(1-s)/beta` |

Die letzten beiden Zeilen sind unsere ungefitteten Diagnosen, keine
Behauptungen Heims und keine fertigen Alternativtheorien. Sie behalten
andere ungeklaerte Quellenannahmen unveraendert bei. Auch die Festsetzung
des kinematischen beta als physikalische Kopplung alpha wird dadurch nicht
neu begruendet. Die Ausgaben sind Vorwaertsvergleiche bei gleichem beta,
keine neu berechneten Alpha-Vorhersagen.

Fuer beta=0.6 ergeben sich exakt `K=12/25`, `4/25` und `4/15`.
Bei kleinen beta sind die fuehrenden Terme `beta`, `beta^2/2` und `beta/2`.
Ein Austausch der Energieformel ist deshalb keine kleine lokale Reparatur
an der bestehenden Alpha-Rechnung.

## 6. Zahlen ohne nachtraegliche Anpassung

Der Rechner verwendet fuenf vorher festgelegte beta-Lehrwerte und zusaetzlich
den kleinen Buchzweig bei `Y3=1`. Fuer diesen werden nur mathematisches pi,
die source-geprueften Buchindizes und die bisherigen Buchformeln eingesetzt.
Ein gemessener Alpha-Wert ist kein Input.

```text
C = A1*A2 = 0.0000115280930597...
K = alpha_prime*(1-C) = 0.0072971602978640...
beta_source = 0.0072973545975671...
pc/T = 274.0682732644...
lambda_dB/lambda_H = 137.0359609952...
```

Dass die letzte Zahl nahe dem bekannten inversen Alpha liegt, ist hier
keine neue Vorhersage: Sie ist per Definition der Kehrwert unseres aus der
Quellgleichung berechneten beta. Die bereits festgestellten Druckpaarprobleme
und die offene Bestimmung von Y3 bleiben bestehen.

Numerik: Decimal mit80 Stellen; Gegenrechnung mit120 Stellen, exakte
rationale Beispiele und stabile Auswertung von `1-s=beta^2/(1+s)`.
Die vorhandene Hardware reicht fuer diese Aufgabe. Mehr Rechengenauigkeit
kann die begrifflichen Unterschiede nicht beseitigen.

## 7. Abgrenzung, Pruefung und naechster Schritt

Die Umkehr der fehlerhaften Energieintervallordnung aus der vorigen Etappe
loest keine der hier gezeigten Begriffsfragen. Wiederholtes `E_k=pc` spricht
gegen einen isolierten Druckfehler genau dieser Formel, beweist aber keine
konsistente alternative Dynamik.

Die naechste klar begrenzte Aufgabe ist deshalb die operative Bedeutung
von `A_-` und der lokalen Energie-/Arbeitsbilanz: Kann die invariante Form
als eine definierte Groesse gelesen werden, und welche Messgroesse meint
sie? Daran anschliessend Kreisgeometrie und Wellenzuordnung explizit machen.
`L*Delta=k`, Auswahlregel(98a) sowie B50/Gamma-Q_N bleiben in der Queue.
Das ganze Theoriegebaeude ist damit noch nicht verstanden oder bewertet.

Code: `scripts/audit_energy_kinematics.py`.
Ergebnisse: `05_analysis/energy_kinematics_diagnostics.json`.
Normalisierung: `NORM-ENERGY-KINEMATICS-DIAGNOSTICS.md`.
Unabhaengige Reviews im Verzeichnis `04_reconstruction/alpha_audit/reviews/`:

- `ENERGY_MASS_SOURCE_REVIEW_2026-09-06.md`
- `WAVELENGTH_KINEMATICS_SOURCE_REVIEW_2026-09-06.md`
- `ENERGY_KINEMATICS_MATH_REVIEW_2026-09-06.md`

### Lokale Quellenprovenienz

- EDM1: `01_sources/heim_primary/Burkhard Heim - 1998 - Elementarstrukuren der Materie 1.pdf`.
  SHA256 `49C79028C4F5B4FEE97F0541EF1655C37755C3C3C2FD3A10DD6E72CB454DE459`.
- EDM2: `01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf`.
  SHA256 `F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.
- Einstein1905: `01_sources/mainstream_reference/Einstein_1905_Elektrodynamik.pdf`.
  Download2026-09-06 vom oben verlinkten Universitaetsarchiv; Druck920/PDF30
  als Bild gelesen. SHA256 `F907CD496A6A1ABF07E7E78C2111A63DAB1E9D8F2491BCC0C391B872CB3C49B4`.

Keine dieser fremden PDF-Dateien wird im Git veroeffentlicht. Unsere Berichte,
Quellenlokatoren, Rechnungen und Pruefungen sind versioniert.
