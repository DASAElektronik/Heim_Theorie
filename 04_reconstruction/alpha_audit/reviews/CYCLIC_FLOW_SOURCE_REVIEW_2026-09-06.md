# Quellenreview: zyklischer Kondensorfluss, Eigenfrequenz und Wellenlaenge

Stand 2026-09-06. Eng begrenzte Rekonstruktion der unmittelbaren
Quellenkette zu EDM2 Druck160/161, besonders Gleichung (76). Die Aufgabe ist
nicht, die gesamte Synmetronik zu beurteilen oder die H-Kreiswelle mit einem
spaeteren eigenen Ringmodell gleichzusetzen.

## Ergebnis

Die Quelle definiert Zyklizitaet als **periodische Rueckkehr eines
Kondensorflussaggregates vom Anfangszustand A zu C=A**. Unter einer geeigneten
Projektion kann die zyklische Flussbewegung als Schwingungsprozess aufgefasst
werden; daraus ordnet Heim dem zyklischen Fluss eine Eigenfrequenz `eta` und
mit seiner Flussgeschwindigkeit `w_f` die Wellenlaenge

```text
lambda = w_f / eta
```

als **Aggregatdiameter** zu. Das ist eine quellenbelegte interne
Begriffs-/Modellkette.

Nicht daraus ableitbar sind eine H-Kreis-Mode mit `N=1`, die Gleichsetzung
des Aggregatdurchmessers mit einem H-K-Schalenmeridian oder -umfang, eine
Standard-Randbedingung, ein Bezugssystem fuer die gebundene
Elektronenwelle oder allgemein `w_f=c`. Der Satz `m c lambda = h` wird auf
Druck161 ausdrücklich als **empirischer Quantendualismus** bezeichnet, der
in (76) eine „vertiefte Interpretation“ finde; die untersuchte Passage
liefert keine Herleitung seines universellen Zahlenwerts aus der Zyklizitaet.

## Visuell kontrollierte Quellkette

| Quelle | Buchseite / PDF-Folio | Quelle sagt | Reichweite |
|---|---:|---|---|
| EDM2 (75), S. 157 / PDF 164 | 157 / 164 | Die Signaturtransposition/Feldaktivatoren bilden die Existenzbedingung (75) fuer einen Kondensorfluss; der Text verortet diesen in Kopplungsstrukturen. | Vorbedingung eines Kondensorflusses, nicht schon eine H-Welle oder ein Kreisoperator. |
| EDM2, S. 158 / PDF 165 | 158 / 165 | Systeme aus Quellen/Senken koennen bei (75) Kondensorfluesse verursachen; einzelne Fluesse koennen sich in Klassen `1 <= v <= 6` zu Flussaggregaten zusammenschliessen. | Definiert ein aggregiertes Strukturobjekt, kein Einteilchen-Ring. |
| EDM2, S. 159 / PDF 166 | 159 / 166 | Ein aufgeteiltes Aggregat fuehrt den Anfangszustand A entweder in einen Finalzustand `C != A` oder verlaeuft „zyklisch, also rotatorisch“, und fuehrt A ueber B periodisch zu `C = A` zurueck. `A != C` stoere die Kopplungsstruktur und sei mit der geforderten zeitlichen Stabilitaet unvereinbar. | Das ist die konkrete Definition der Zyklizitaet: Zustandsrueckkehr. Sie ist keine ausgesprochene raeumliche Phasenperiodizitaet auf einem Kreis. |
| EDM2 (76), S. 160 / PDF 167 | 160 / 167 | Fasst die Zyklizitaetsforderung mit `A=C` zusammen: Sie ist Bedingung fuer zeitliche Definition/Stabilitaet des kompositiven Terms. Jeder zyklische Kondensorfluss habe wegen Rotation Spin; bei ausgeglichenen Spins koenne eine spinfreie Kondensation vorliegen. | Liefert Zeitstabilitaet, Rotation und Spinbezug; keine Modenzahl, Radius oder Randwertgleichung. |
| EDM2, S. 161 / PDF 168 | 161 / 168 | Eine zyklische Flussbewegung kann „bei geeigneter Projektion“ als Schwingungsprozess aufgefasst werden. Der zyklische Kondensorfluss der kompositiven Kondensation ordne „immer eine Eigenfrequenz eta“ zu; mit `w_f` definiere sie `lambda = w_f/eta` als Aggregatdiameter. Aus Kompressorisostasie setzt der Text `m lambda = const`, weil `w_f = const` sein muesse, und nennt anschliessend `m c lambda=h` den empirischen Quantendualismus. | Diese Seite ist der direkte Anker fuer eta und lambda. Weder `w_f=c` noch H-Zuordnung noch der Wert `h` folgen dort als eigene Ableitung. |
| EDM2 (76a,b), S. 162 / PDF 169 | 162 / 169 | Eine Flussperiode ist abgelaufen, wenn alle Kondensorfluesse des Aggregats einmal gewirkt haben. `A=C` muss nicht schon nach einer Periode gelten; im allgemeinen werde es erst nach einer Periodenzahl `omega > 1` wiederhergestellt. | `omega` ist eine Zahl von Flussperioden/Zustandsrueckkehr, keine gedruckte raeumliche Wellenwindungszahl. Insbesondere kein Beleg fuer `N=1`. |
| EDM2 (77)--(78), S. 172--174 / PDF 178--180 | 172--174 / 178--180 | Der Text behandelt die Flussrichtung als zeitliche Lageaenderung und ergaenzt Gesetzmaessigkeiten zu Flussgeschwindigkeit und Diameter. Auf S.173: fuer Zeitkondensationen/Photonen gilt `m c lambda=h` bei photonischer Feldmasse und daher `w_f=c`; fuer Gravitonen `w_f=omega>c`. Allgemein sei `w != c`; `w=c` nur unter der dort genannten Bedingung, dass der `(x5,x6)`-Zustand mit `epsilon-dot=0` und `eta-dot=0` zeitlich unveraendert bleibe. Das System (78) druckt `w_f=w >= c` und `m lambda=mu lambda_0=const`. | Die unmittelbare Passage nennt das H-Atom nicht. Ihre Identitaet von `w_f` mit dem Imaginaerteil der Weltgeschwindigkeit ist aber mit der H-Stabilitaetsaussage auf S.300/PDF306 zur bedingten Teilbruecke kombinierbar; siehe Nachtrag. |

## Was genau aus (76) folgt - und was nicht

Die direkte Kette ist:

```text
Existenzbedingung (75) fuer Kondensorfluss
  -> Flussaggregat mit zyklischer Zustandsrueckkehr A -> B -> C=A
  -> zeitliche Stabilitaet nach (76)
  -> bei geeigneter Projektion Schwingungsauffassung
  -> Eigenfrequenz eta und lambda=w_f/eta als Aggregatdiameter.
```

Die Gleichung `A=C` ist in dieser Kette die Rueckkehr der
Kondensorsignatur/Struktur zum Anfangszustand. Sie ist nicht mit der
separaten, in der Alpha-Passage vorkommenden Integrationskonstante `A` oder
mit deren Proportionalitaetsbeziehungen gleichzusetzen.

Der Buchstabe `eta` auf S.161 bezeichnet die Eigenfrequenz des zyklischen
Kondensorflusses. Er ist aus dieser Passage nicht als `eta_qk`, `eta_1k`
oder eine der eta-Groessen der spaeteren Ladungsfeld-/Alpha-Formeln
definiert. Eine solche Identifikation waere eine zusaetzliche, bislang
unbelegte Bruecke.

## Entscheidung zu den gezielten Fragen

| Frage | Quellenstatus |
|---|---|
| H-Kreismode oder `N=1`? | **Nicht gefunden.** Rotatorische Zustandszyklen und die Periodenzahl `omega` ersetzen keine raeumliche Kreis-Randbedingung oder ihre Modenauswahl. |
| `w_f=c`? | **Bedingt quellenintern gestuetzt.** Die unmittelbare Flusspassage gibt `w_f=w>=c` und eine Bedingung fuer `w=c`; Druck300/PDF306 gibt im H-Fall `w=c` fuer denselben als Imaginaerteil der Weltgeschwindigkeit bezeichneten Wert. Die verbleibende Objektidentifikation H-Elektronenwelle = Flussaggregat ist offen; siehe Nachtrag. |
| Zeit/Frame der H-Welle? | **Nicht gefunden.** Die Quellen sprechen von zeitlichem Stabilitaetsintervall, kosmischer Bewegung und `(x5,x6)`-Zustand, aber verbinden dies nicht mit einer konkreten Bezugsrahmen- und Zeitdefinition fuer EDM2 S.276/277/301. |
| Absolutes `m c lambda=h`? | **Als empirische Relation genannt, nicht hier hergeleitet.** S.161 bezeichnet sie als empirisch; S.173 beschraenkt die explizite `c`-Fassung auf Zeitkondensationen/Photonen mit photonischer Feldmasse. |
| `lambda=w_f/eta`? | **Definiert.** Auf S.161 als Wellenlaenge/Aggregatdiameter der bei geeigneter Projektion als Schwingung betrachteten zyklischen Flussbewegung. |

## Nachtrag: quelleninterne Teilbruecke zu `w_f=c` im H-Fall

Eine erneute Gegenlesung von EDM2 Druck300/PDF306 und Druck173--174/PDF179--180
liefert eine positive, aber bedingte Teilbruecke. Die Gleichsetzung ist
nicht bloss formgleich:

1. In der H-Passage steht ausdruecklich: Das H-Atom sei ein Zustand
   dynamischer zeitlicher Stabilitaet; die zugehoerigen Koordinaten
   `x5, x6` blieben zeitlich konstant, `x5-dot=x6-dot=0`, **was `w=c` fuer
   den Imaginaerteil der Weltgeschwindigkeit `Y` zur Folge habe**.
2. In der allgemeinen Flusspassage S.173 steht ausdruecklich, dass wegen
   der nur imaginaeren, kondensorflussfaehigen Struktureinheiten fuer die
   Flussgeschwindigkeit `w_f=w` zu setzen sei. Derselbe Satz bezeichnet
   `w` als Imaginaerteil der Weltgeschwindigkeit; (78) auf S.174 druckt
   erneut `w_f=w>=c`.

Damit ist quellenintern die folgende **konditionale** Kette zulaessig:

```text
H-Stabilitaet -> x5-dot=x6-dot=0 -> w=c fuer Im(Y)
struktureller Kondensorfluss -> w_f=w
---------------------------------------------------
wenn der H-Wellengegenstand dieser strukturelle Kondensorfluss ist:
w_f=c.
```

Die mittlere Identifikation ist nicht im selben Schritt ausgesprochen:
Die H-Seiten nennen die zirkulaere Elektronenwelle und ihre
K-Schalen-/R6-Korrespondenz, die S.161-174 dagegen den zyklischen
Kondensorfluss und seinen Aggregatdiameter. Eine Textstelle, die gerade
die H-Elektronenwelle mit dem `lambda=w_f/eta`-Flussaggregat identifiziert,
wurde in diesem begrenzten Durchgang nicht gefunden. Ebenso sind
`x5-dot=x6-dot=0` (S.300) und die auf S.173 verwendeten Ableitungen des
`(x5,x6)`-Zustands nicht als explizit dieselbe Komponentenparametrisierung
ausgewiesen; beide Passagen setzen jedoch jeweils direkt `w=c` als Folge
des zeitlich unveraenderten Zustands.

Folglich verbessert der Nachtrag den Quellenstatus von `w_f=c` von einer
rein externen Annahme zu einer **bedingt quellenintern gestuetzten
Teilbruecke**. Er liefert weder eine universelle Aussage `w_f=c` noch eine
Gleichsetzung von `w_f` mit der Phasengeschwindigkeit der H-Kreiswelle.

## Begrenztes Suchprotokoll

Als Suchhilfe diente der vorhandene EDM2-Volltext mit den Begriffen
`Zyklizitaet`, `Zyklizitaetsforderung`, `Kondensorfluss`, `Flussaggregat`,
`Flussperiode`, `Eigenfrequenz`, `Aggregatdiameter`,
`Flussgeschwindigkeit`, `Kompressorisostasie`, `A=C` und `(76)`.
Die tragenden Seiten 157--162, die direkte spaetere Geschwindigkeits-
und Diametererklaerung auf 172--174 sowie die H-Stabilitaetspassage auf
Druck300/PDF306 wurden visuell kontrolliert. Nicht
verfolgt wurden die vollstaendige Theorie aller Kondensationstypen oder
etwaige weitere, nicht direkt verknuepfte Vorkommen von Wellenbegriffen.

Render: `tmp/pdfs/cyclic_flow/edm2-164.png` bis `-169.png` und
`-178.png` bis `-180.png`; H-Kontext: `tmp/pdfs/wave_closure/edm2-306.png`.
