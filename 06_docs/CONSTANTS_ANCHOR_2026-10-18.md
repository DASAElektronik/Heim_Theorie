# Konstantenkorrektur und Elektronenanker

2026-10-18, Etappe 40; Ausgang `442adf7` plus uncommittierter Etappe39.
[Quellenvertrag](../00_admin/CONSTANTS_ANCHOR_PLAN.md),
[Seiten, Editionen und Hashes](../03_notes/CONSTANTS_ANCHOR_SOURCES_2026-10-18.md).

## Ergebnis

H004 Druck349 beschreibt ausdrücklich, gemessene Elektronenmasse und
Elementarladung zusammen mit hbar und c einzusetzen und daraus gamma,
epsilon0 und mu0 rückwärts zu bestimmen. Druck371 verweist für die
Tabellenkonstanten genau auf dieses Verfahren. Eine mit diesen Konstanten
anschließend reproduzierte Elektronenmasse oder Ladung ist daher kein
unabhängiger Vorhersagetest derselben Eingabegrößen.

Der Rückweg ist algebraisch rekonstruierbar. Ein vollständiger numerischer
Nachvollzug der historischen Kalibrierung bleibt offen: Die geprüften
Stellen listen die ursprünglichen ungerundeten Eingaben und den vollständigen
damaligen Elektronenfaktor nicht auf. Die hier ausgeführte Zahlendiagnose
prüft nur gedruckte Endwerte. Sie bestätigt die Verträglichkeit von
c, epsilon0 und mu0 bei Druckrundung; die bedingte29-Editionsbrücke liefert
eine kleine Abweichung zur gedruckten Ladung.

## 1. Quelleninhalt und Eingaberollen

Heim setzt auf349 den Elektronzustand mit n1=n2=n3=n4=0 in112 ein.
Er berichtet zunächst eine exakte Wiedergabe der empirischen Masse und
Ladung und erläutert dann die Rückrechnung. Diese Reihenfolge beweist
keinen unabhängigen Test mit einem dokumentierten, vorab fixierten
Konstantensatz. Auf371 steht zudem, dass die korrigierten Konstanten
auch für numerische Untersuchungen im vorausgehenden Text benutzt wurden.

| Größe | Rolle im Rückweg nach349 | Hier geprüft |
|---|---|---|
| m_e, Betrag e | Empirische Anker | Rolle belegt; ursprüngliche Zahlentokens offen |
| hbar, c | Weitere empirische Eingaben | Rolle belegt; h auf371 nicht mit hbar verwechseln |
| Elektronenfaktor D_e | Eigene Kurzbezeichnung für dimensionslosen Teil von112 | Bedingt festgehalten, nicht neu angepasst |
| gamma | Aus Massenskala und m_e zurückgerechnet | Symbolische Inversion |
| R_- | Aus29 und e bestimmter Wellenwiderstand | Bedingte H003/H004-Brücke |
| epsilon0, mu0 | Aus R_- und c bestimmbar | Beziehung und Druckkonsistenz |

Der Vermerk371 nennt hbar, epsilon0, mu0 und gamma gemeinsam als
Korrekturgegenstand, druckt dann aber h. Daraus wird kein zusätzlicher
unabhängiger h-Fit abgeleitet;349 behandelt hbar als Eingabe. Die genaue
Vorher-/Nachherliste bleibt eine Provenienzfrage.

## 2. Eigene algebraische Rekonstruktion der Massenskala

Aus Heims97, mit s0=1 m und positiven Größen:

```text
c mu s0 = pi^(1/4) (3 pi s0 gamma hbar)^(1/3) sqrt(c hbar/(3 gamma))
mu = pi^(7/12) 3^(-1/6) gamma^(-1/6) hbar^(5/6) c^(-1/2) s0^(-2/3)
mu^6 = pi^(7/2) hbar^5 / (3 gamma c^3 s0^4).
```

112 lautet M=mu alpha_+ (K+F+H+phi). Für n=0 verschwinden F und H.
Wir definieren **D_e=alpha_+ (K_e+phi_e)**, sodass m_e=mu D_e. alpha_+
ist hier der Massenfaktor aus97, nicht die Feinstrukturkonstante und
nicht die gleichnamige Zweigbezeichnung aus105. Bei festem D_e>0 folgt:

```text
gamma = pi^(7/2) hbar^5 D_e^6 / (3 c^3 s0^4 m_e^6).
```

Die Einheit ist m³ kg^-1 s^-2; s0 darf in der Dimensionsprüfung nicht
weggelassen werden. Dies ist unsere Umformung von Heims Gleichungen,
keine neue physikalische Theorie. Sie wurde gegen die ursprüngliche97-Form
mit synthetischen Werten geprüft, ohne einen neuen D_e zu kalibrieren.

Bei derselben Skala und festgehaltenen dimensionslosen Faktoren gilt für
eine weitere Masse M_x=m_e D_x/D_e. Relative Massenbeziehungen können
damit weiterhin prüfbaren Inhalt haben. Ob D_x und D_e unabhängig von den
verglichenen Messmassen bestimmt wurden, bleibt gesondert zu prüfen:
Etappe39 belegt gerade den empirischen Ursprung des F_S-Ansatzes.
Wenn man F_S bei einer Konstantenänderung erneut extrahiert, ist D_e
nicht automatisch fest; der obige Rückweg ist ausdrücklich bedingt.

## 3. Eigene Rekonstruktion des elektromagnetischen Rückwegs

H003 Druck248/(29), positive Ladungsgröße:

```text
eta = pi/(4+pi^4)^(1/4), vartheta = 5 eta + 2 sqrt(eta) + 1
4 pi^2 e = 3 sqrt(2 vartheta hbar/R_-)
R_- = 9 vartheta hbar / (8 pi^4 e^2).
```

Mit den auf H004349 genannten Beziehungen folgt eindeutig:

```text
c sqrt(epsilon0 mu0)=1, R_- sqrt(epsilon0)=sqrt(mu0)
epsilon0 = 1/(c R_-), mu0=R_-/c.
```

R_- ist hier keine zusätzliche unabhängige Messbedingung. H003242
definiert den Wellenwiderstand entsprechend. H0031998 und H0041996 werden
als getrennte Ausgaben geführt; die Verwendung dieser29 ist eine benannte
Brücke. H004301 verwendet29 ausdrücklich weiter, während105 die
Alpha-Näherung29a ersetzt. Deshalb wird hier nicht zusätzlich die
105-Kopplung mit e²R_-/(4pi hbar) gleichgesetzt.

## 4. Was liefern die gedruckten Endwerte?

Vor Rechnung fixiert: H004371 gibt h=6.626173e-34 J s,
gamma=6.672131e-11 m³ kg^-1 s^-2, epsilon0=8.854323e-12 F/m,
mu0=1.256618e-6 H/m und e=1.602188e-19 C an. Angenommen wird Rundung
zur nächsten letzten gedruckten Stelle, jeweils ± eine halbe letzte
Einheit. Das ist eine Prüfannahme und keine Quellenangabe zur Fehlerrechnung.

M00615 liefert als historische Vergleichsgröße c=299792458 ±1.2 m/s
(eine Standardabweichung). Die genaue Verwendung dieses Datensatzes
durch Heim ist nicht nachgewiesen.

| Diagnose | Ergebnis | Einordnung |
|---|---|---|
| c aus 1/sqrt(epsilon0 mu0), zentrale Druckwerte | 299792443.193 m/s | Zentralwerte allein unterscheiden sich um etwa14.8 m/s |
| c-Bereich aus Druckrundung | etwa299792375.086 bis299792511.301 m/s | Historischer Zentralwert liegt darin |
| c² epsilon0 mu0=1 bei historischem c | Exakter rationaler Produktbereich enthält1 | Kein Konflikt unter der Rundungsannahme |
| R_-=sqrt(mu0/epsilon0) | 376.724580381 Ohm | Abgeleitete Größe |
| e aus29 und hbar=h/(2pi) | 1.60218938759e-19 C | Etwa0.866 ppm über gedrucktem e |
| e-Bereich aus h/epsilon0/mu0-Druckrundung | [1.60218914515,1.60218963003]e-19 C | Numerische Endpunktauswertung |
| Gedruckter e-Bereich | [1.6021875,1.6021885]e-19 C | Keine Überlappung mit dem29-Bereich |

Der c-Test benutzt rationale Brüche und ist innerhalb der deklarierten
Rundungsbox exakt. Die irrationalen29-Endpunkte sind bei60 und90
Dezimalstellen stabil ausgewertet, aber kein zertifiziertes Intervallverfahren.
Eine zweite direkte Rechnung mit der unquadrierten29 und Python/math
ergibt1.60218938758978e-19 C. Die Lücke liegt weit über diesen numerischen
Rechenunterschieden. Auch die großzügige rechteckige Rundungsbox erlaubt
keine Ladungsüberlappung; die zusätzliche c-Bedingung würde sie nur einschränken.

Das ist ein **bedingter Darstellungsbefund** zwischen dieser29-Lesung und
den371-Endwerten. Ob Druckfehler, andere historische Fassung oder weitere
Rechenschritte dafür verantwortlich sind, ist nicht geklärt. Die damalige
PDG-Ladungsunsicherheit beträgt rund2.9 ppm: Eine interne Rundungsabweichung
von0.866 ppm ist nicht gleichbedeutend mit empirischer Widerlegung.
Es wurde kein Wert passend korrigiert.

## 5. Genauigkeit und verbleibende Grenzen

Aus der Inversion folgt bei festem s0 die lineare relative Sensitivität:

```text
d gamma/gamma = 6 dD_e/D_e + 5 dhbar/hbar - 3 dc/c - 6 dm_e/m_e.
dR_-/R_- = dhbar/hbar - 2 de/e  (vartheta fest).
```

Gleiche Anzahl gedruckter Stellen bedeutet deshalb nicht automatisch
gleiche physikalische Genauigkeit. Für eine Unsicherheitsbilanz fehlen
insbesondere Kovarianzen und Modellunsicherheiten. M006 nennt für hbar
5.4 ppm und die SI-Elektronenmasse5.1 ppm; diese Zahlen belegen keine
pauschale Übertragung von sieben sicheren Dezimalstellen. Eine statistische
Fehlerfortpflanzung mit erfundener Unabhängigkeit wurde nicht vorgenommen.

Abgeschlossen ist die eng begrenzte Klärung des Rückrechnungsverfahrens
und seiner Eingaberollen. Nicht abgeschlossen ist die vollständige
numerische Reproduktion der gedruckten gamma-Korrektur oder der
historischen F_S-Kalibrierung. Die nächste Einheit sollte den originalen
Konstantensatz und die29-Fassung im frühen Tabellen-/Rechenstand suchen,
insbesondere zu der auf371 erwähnten Nachrechnung vom26.7.1982. Erst mit
einer belegten Fassung und einem vollständigen D_e-Vertrag weiterrechnen.

## 6. Reproduktion und Integrität

```powershell
py -3.13 -B scripts/audit_constants_anchor.py --check
py -3.13 -B -m unittest discover -s tests
py -3.13 -B scripts/validate_finding_register.py
```

[Diagnosecode](../scripts/audit_constants_anchor.py),
[Ergebnisse](../05_analysis/constants_anchor_results.json),
[Tests](../tests/test_constants_anchor.py). Sechs neue Tests,360 insgesamt
bestanden. Quellenhashes bestätigt;49 frühere Registereinträge erhalten.
FIND-050 dokumentiert den Quellenbefund samt begrenzter Diagnose;
50 Befundgruppen sind keine Zählung unabhängiger Theoriefehler.
Alte Rechner, Eingaben, Ergebnisdateien und49 Normalisierungen unverändert.
Ein Agent, kein externes Peer Review. Kein Commit oder Push.
