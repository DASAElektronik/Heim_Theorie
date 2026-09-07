# Konfigurationszahl und Auswahlregel (98a)

Stand2026-09-06, achte begrenzte Etappe, Ausgangscommit2b46b5d.
Ziel: den Gesamtzusammenhang rekonstruieren und unsere Arbeitsbefunde bei
neuen Quellenverbindungen erneut pruefen. Kein abschliessendes Theorieurteil.

## 1. Was jetzt klarer ist

Die Konfigurationszahl k ist bei Heim kein erst fuer Alpha erfundener Faktor.
Sie stammt aus seiner Beschreibung diskreter innerer Strukturstufen. Der
Ansatz `L*Delta=k` verbindet diese Strukturzahl mit einer relativen Aenderung
des Ladungsfeldes; daraus entsteht die bereits verwendete Familie eta_qk.
Die Verknuepfung ist im Text ausdruecklich ein moeglicher Ansatz, kein dort
bewiesener Quantisierungssatz.

Die anschliessende Auswahlregel (98a) hat eine nachvollziehbare Quellkette,
aber zwei Probleme im untersuchten Abschnitt:

- Die aufeinanderfolgenden Positivitaets-/Potentialbedingungen sind in der
  gedruckten Form nicht miteinander vereinbar. Eine Richtung wechselt;
  bei der anschliessenden Umformung stimmen Richtung und ein Term nicht.
- Die gedruckte Grenzfunktion liefert fuer q=2 den Wert
  `u_2=1.963489198102715...`, nicht den behaupteten Bereich `2<u_2<3`.

Gleichzeitig ergeben sich positive Kontrollen: Der letzte Umformungsschritt
von der gedruckten eta-Schranke zur k-Schranke stimmt. Die angegebenen
Bereiche fuer q=1,3,4 und der Ausschluss aller ganzen q>=5 werden fuer diese
Grenzfunktion bestaetigt. Ihre globalen Maxima bleiben k_max=2 und q_max=3,
obwohl das konkrete Paar (q,k)=(2,2) wegfaellt.

Die bisherige Buch-Alpha-Spezialisierung benutzt (1,1) und (1,2); beide
bleiben in dieser Auswahl enthalten. Ein lokaler Befund aendert damit nicht
automatisch alle nachfolgenden Zahlen. Die [Zusammenhangskarte](../04_reconstruction/alpha_audit/CONFIGURATION_DEPENDENCIES.md)
trennt belegte Verbindungen, Annahmen und offene Pruefanlaesse.

## 2. Was L, Delta, q und k bedeuten

Band I Druck244/PDF250 bezeichnet q>=0 ausdruecklich als ganze elektrische
Ladungsquantenzahl und verwendet `Q_plusminus=q*epsilon_plusminus`.
Die Ganzzahligkeit ist somit ein Quellenbefund, nicht aus den spaeter
ausprobierten Zahlen q=1,2,3,4 geraten.

Band II Druck263/264, PDF269/270, beschreibt k als positive ganzzahlige
Kondensorziffer bzw. Konfigurationszahl. Die Quelle verbindet damit
`kappa=k^2` und `Z_k=2^(k^2)`. Elektron und Proton motivieren dort induktiv
die Betrachtung der beiden Kandidaten k=1 und k=2. Diese Motivation ist
noch kein Beweis, dass keine weiteren k moeglich sind.

Auf Druck265/PDF271 steht, in unserer eindeutigen Schreibweise:

```text
Delta = (epsilon_prime/epsilon)^4 - 1,
L = Dimensionszahl kondensierender manifester Ereignisse,
L*Delta = k > 0  [moeglicher Ansatz],
L = L(R4) = 4    [Begruendung ueber d-Hermetrie im Quellenmodell].
```

Delta ist eine relative Aenderung der vierten Potenz, kein Abstand und kein
Differentialoperator. L,Delta und k sind dimensionslos. Unter der gesetzten
Identifikation folgt fuer den positiven Quotienten (gleiches Ladungsvorzeichen)
`epsilon_prime/epsilon=(1+k/4)^(1/4)`; ohne diese Zweigwahl ist zunaechst
nur der Betrag des Quotienten bestimmt.
Beispielsweise sind Delta=1/4 fuer k=1 und Delta=1/2 fuer k=2.
Ein Bezug zur zugrundeliegenden Geometrie ist damit benannt; eine unabhaengige
Herleitung gerade der Identifikation L*Delta=k wurde hier nicht gefunden.

Auf Druck266/PDF272 folgt die interne Protosimplex-Skala
`(mu*f/M)^4=1+(q/pi)^4*(4+k)`. Mit `M=mu*f*eta_qk` ergibt sich

```text
eta_qk = pi / [pi^4+q^4*(4+k)]^(1/4),
eta_q = eta_q0,  eta = eta_10.
```

k=0 ist dabei ein formales Etikett fuer die externe Familie; die interne
Auswahl untersucht k>=1. Fuer q=0 wird eta_0k=1 unabhaengig von k, doch die
folgende u_q-Funktion dividiert durch q und ist dort nicht anwendbar.
Die schon geklaerte Buchindexreihenfolge (q,k) bleibt erhalten.

## 3. Der genaue Herleitungsknoten

Die Quelle setzt auf II268/PDF274 dimensionslose Verhaeltnisse von Potentialen
bzw. Energien an. Zur Entlastung der Notation nennen wir
`a=eta_q`, `e=eta`, `x=1/eta_qk`; e ist hier KEINE elektrische Ladung.
Es gilt fuer positive q: `0<a<=e<1`.

```text
V1=a*x,
V2=(1+sqrt(a))^2/(4e),
Q1=a^2/sqrt(e),
Q2=sqrt(e).
```

Bei Q2 steht kein Index q unter der Wurzel. Eine zwischenzeitliche abweichende
Lesung in unserer Gegenpruefung wurde nach hochaufgeloester Bildkontrolle
verworfen. Sie ist keine zweite Heim-Fassung und wird nicht weitergerechnet.
Auch Unterstreichungen in den davor definierten Potentialquotienten duerfen
nicht weggelassen werden; sonst wuerden verschiedene Groessen scheinbar gleich.

Auf II269/PDF275 folgen drei unterschiedliche Aussagen:

| Ebene | Gedruckte Aussage | Gewoehnliche algebraische Folge |
|---|---|---|
| I | F2-F1+G2-G1>0; spekulativ F_i=V_i und G_i=Q_i | V1+Q1<V2+Q2 |
| II | Danach steht V1+Q1>V2+Q2 | Gegenteil von Ebene I |
| III | Danach steht x<B_q | Nicht die Umformung von Ebene II |

Die Quelle bezeichnet ihre F/G-Zuordnung selbst als spekulativ. Der
nachfolgende Konflikt entsteht aber bereits unter dieser Zuordnung mit
normaler Arithmetik; dazu braucht es keine moderne physikalische Gegenannahme.

Setzen wir die Potentialverhaeltnisse direkt ein, erhalten wir fuer das
eigene Residuum R (nicht Heims Delta aus L*Delta=k):

```text
R = V1+Q1-V2-Q2 = a*(x-D_q),
D_q = (1+sqrt(a))^2/(4ea) + sqrt(e)/a - a/sqrt(e).
```

Die gedruckte Schranke ist dagegen

```text
B_q = (1+sqrt(a))^2/(4ea) + sqrt(e) - a/sqrt(e),
D_q-B_q = sqrt(e)*(1/a-1) > 0.
```

Ebene I entspricht x<D_q, Ebene II x>D_q und Ebene III x<B_q.
Ebene II und III sind damit sogar unvereinbar. Die gedruckte B-Bedingung
ist hingegen eine strengere, hinreichende Bedingung fuer Ebene I, nicht
deren aequivalente Umformung. Ein zusaetzliches Gesetz koennte prinzipiell
eine strengere Auswahl begruenden; ein solches wurde an diesem Uebergang
nicht gefunden. Eine eindeutige historische Reparatur folgt daraus nicht.

Ein direkter Test bei (q,k)=(1,1) liefert
`R=-0.012553363208798956...`: Ebene I und die B-Auswahl sind erfuellt,
die gedruckte V/Q-Zeile II nicht. Das ist ein lokaler, reproduzierbarer
Konsistenztest, kein experimenteller Ausschluss einer Teilchenkonfiguration.

## 4. Die Grenzfunktion nachgerechnet

B_q ist fuer q>=1 positiv. Deshalb ist mit (98) der Schritt

```text
x < B_q  <=>  k < u_q = (pi/q)^4*(B_q^4-1)-4
```

korrekt. Die Ungleichung ist strikt; vor der Auswahl erfolgt keine zusaetzliche
Rundung auf Ausgabestellen. Mathematisches pi,80 signifikante Dezimalstellen intern:

| q | Berechnetes u_q | Gedruckter Bereich | Positive ganze k mit k<u_q |
|---:|---:|---|---|
| 1 | 2.063799031006 | 2<u_1<3 | 1,2 |
| 2 | 1.963489198103 | 2<u_2<3 | 1 |
| 3 | 1.239666657763 | 1<u_3<2 | 1 |
| 4 | 0.100757928773 | 0<u_4<1 | keine |
| 5 | -0.884599369019 | u_q<0 fuer ganze q>4 | keine |

Die Abweichung bei q=2 wurde unabhaengig mit festem pi-Praefix und Decimal
gegengerechnet. Unser Rechner benutzt dagegen eine iterative pi-Berechnung.
Der80/120-Stellen-Vergleich stimmt weit ueber die benoetigte Genauigkeit
hinaus ueberein. Diese numerischen Checks sind keine eigene zertifizierte
Intervallrechnung; der Abstand zu2 betraegt rund0.03651, nicht eine letzte
unsichere Druckstelle. An den alten Rechenprofilen wird nichts geaendert.

### Warum die Paarliste nicht nur ein endlicher Suchlauf ist

Mit a=eta_q schreiben wir
`F(a)=a*B_q=(1+sqrt(a))^2/(4e)+a*sqrt(e)-a^2/sqrt(e)`.
Aus den elementaren Schranken `3<pi<22/7` folgen
`49/50<e<1` und fuer ganze q>=5: `a<=eta_5<22/49<9/20<e/2`.
Auf diesem Bereich ist
`F'(a)=(1+1/sqrt(a))/(4e)+sqrt(e)-2a/sqrt(e)>0`.

Mit `sqrt(9/20)<84/125` ergibt sich eine rein rationale obere Schranke:

```text
F(a) < (1+84/125)^2/(4*49/50) + 9/20 - (9/20)^2 < 1.
```

Somit B_q<1/eta_q und u_q<0 fuer alle ganzen q>=5. Die rationalen
Vergleiche werden exakt als Brueche geprueft. Zusammen mit q1..4 ist die
Auswahl daher vollstaendig **innerhalb dieser einzelnen gedruckten Bedingung**:
`{(1,1),(1,2),(2,1),(3,1)}`. Sie ist kein Nachweis der Existenz dieser
Zustaende unter allen Gesetzen des Gesamtmodells.

Die Grenzen q_max=3 und k_max=2 sind keine Erlaubnis fuer jedes Paar im
kartesischen Produkt. Insbesondere ist (3,2) schon durch Heims eigenen
angegebenen Bereich fuer q=3 ausgeschlossen.

### Warum wir keine einzelne Richtung still korrigieren

Die aus den Potentialverhaeltnissen folgende D-Schwelle liefert eine andere
k-Grenze. Bei q=1 ist sie etwa6.22688, bei q=5 etwa16.82971. Die
vorgelagerte Bedingung I wuerde allein daher auch (5,1) erlauben, waehrend
die gedruckte B-Auswahl es ausschliesst. Weitere Modellbedingungen koennen
dies einschraenken; keine dieser Varianten ist hier zur richtigen
physikalischen Auswahl erklaert worden.

## 5. Bedeutung fuer Alpha und das Gesamtbild

Band II295/296, PDF301/302, verbindet die Konfigurationen heuristisch mit
Elektron und Proton: In der Quellenreihenfolge (k,q) sind es (1,1) und
(2,1), also in eta-Reihenfolge (q,k) genau (1,1) und (1,2).
II299-302 verwendet daraus eta_11,eta_12,A_1,A_2 im H-System.

Damit ist jetzt nicht nur eine Indexdefinition gefunden, sondern auch der
physikalisch gemeinte Verbindungspfad. Er verwendet empirische und
heuristische Zuordnungen, ist also keine ausschliesslich voraussetzungsfreie
Herleitung. Der q=2-Befund entfernt keinen dieser beiden Buch-Alpha-Faktoren.

Die1982-Zusammenfassung kennt passende k-Zuordnungen, ihre Formeln bleiben
aber eine eigene Fassung. Die1989-Auswertung verwendet ausserdem eta_22;
die Anwendbarkeit von Buch(98a) auf diesen Faktor ist eine getrennte
Versions-/Bedeutungsfrage. Ein algebraischer Faktor ist nicht automatisch
die Behauptung eines realisierten Zustands. Deshalb wird weder eine1989-
Formel verworfen noch der Faktor still ersetzt.

Die neuen Befunde sind im [Register](../04_reconstruction/alpha_audit/FINDING_REGISTER.json)
mit begrenzter Tragweite aufgenommen. Sie bleiben revidierbar bei einer
belegten anderen Definition, einem Erratum oder einer bislang fehlenden
Querverbindung. Die alte H-Energieordnung und der Matrixbefund sind eigene
Probleme und werden nicht durch blosses Zaehlen mit diesem Knoten vermischt.

## 6. Quellen, Reproduktion und Anschluss

Tragende Quelle H004, EDM2 Druck263-269/PDF269-275, visuell geprueft;
H003 Druck244/245 und H004 Druck295/296 fuer die Bedeutungsbruecken.
Dateihashes/Pruefumfang stehen im Rechner und den drei Reviews:

- [Quellenkette](../04_reconstruction/alpha_audit/reviews/CONFIGURATION_SELECTION_SOURCE_REVIEW_2026-09-06.md)
- [Abhaengigkeiten und Versionen](../04_reconstruction/alpha_audit/reviews/CONFIGURATION_DEPENDENCY_REVIEW_2026-09-06.md)
- [Unabhaengige Mathematik](../04_reconstruction/alpha_audit/reviews/CONFIGURATION_SELECTION_MATH_REVIEW_2026-09-06.md)

Die neue Diagnose verwendet keine Messwerte und keine angepassten Parameter.
Originaltranskriptionen sowie sechs alte Rechner/Inputs/Snapshots bleiben
unveraendert. Berechnete Ergebnisse:
`05_analysis/configuration_selection_diagnostics.json`.

Abschlusspruefung:86 Tests bestehen, davon9 neue fuer diese Diagnose.
Der unabhaengige Mathematikreview hat zusaetzlich1057 numerische und
Bool-Felder gegen eigene100-stellige Rechnungen kontrolliert. Der
Abstandsschutz vor strikten Vergleichen und die zulässigen Praezisionsgrenzen
sind getestet; dies wird nicht als zertifizierte Intervallarithmetik ausgegeben.

```powershell
py -3.13 scripts/audit_configuration_selection.py --check --verify-sources
py -3.13 scripts/validate_finding_register.py
py -3.13 -m unittest discover -s tests -q
```

Naechster sinnvoller Zusammenhang: die in II269 benutzte Exponentialnaeherung
und ihre Rueckverweise (79)/(79a), einschliesslich der Bedeutung von F/G
und ihrer Zuordnung zu den Potentialverhaeltnissen. Das verfolgt eine
konkrete offene Verbindung statt neue freie Ersatzformeln zu erfinden.
Die1989-eta_22-Verwendung bleibt dabei eine getrennte Seitenfrage. Danach
Massenabhaengigkeiten B50/Gamma-Q_N und die uebergreifende Verstaendnisbilanz.
