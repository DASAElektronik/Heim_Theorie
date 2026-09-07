# Ein Elektronfall: gedruckte Formel und spaetere Programme

Stand: 2026-09-06, Etappe 17 ab `99a2efa`. Vertrag vor Rechnung:
`ca9abb1`. Enger Umfang: H006-x2/e-, N=0; keine anderen Teilchen.

Nachtrag Etappe18: [Die Quellenverfolgung](ALPHA3_ORIGIN_2026-09-06.md)
belegt beide H010-alpha3-Terme im BuchII275/278 und im fotografierten
FORTRAN-Listing mit Datumszeilen1982 (H015PDF22). Die unten genannten
Unterschiede zu H006 bleiben; eine erst spaete Programmaenderung darf
daraus nicht abgeleitet werden. Alte Eingaben, Rechnungen und Snapshots
sind unveraendert. Die Buchkoeffizienten sind ausdruecklich empirisch gewaehlt.

## Ergebnis

Wir koennen den **archivierten spaeteren Programmwert** fuer diesen einen
Elektronfall mit eigenem Code nachvollziehen. Dazu gehoeren jedoch andere
alpha3-Formeln und andere Eingaben als in unserer bisherigen H006-Rechnung.
Die beiden Zahlen sind daher keine zwei Auswertungen derselben Formel mit
bloss unterschiedlicher Rechnergenauigkeit.

| Festgelegtes Profil | Eigene Rechnung in kg | Mit H010-Umrechnung in MeV/c^2 |
| --- | ---: | ---: |
| Bisherige H006-N0-Lesart | 9.07801746451643e-31 | 0.50923948726363 |
| Aktive H010-Pascal/C-Formeln und Standardwerte, reelle Hochpraezisionsrechnung | 9.10938089197690e-31 | 0.51099884670320 |

Die Differenz betraegt rund **0.3454876 % des H006-Ausgangswerts**.
Das ist kein Vergleich mit der heutigen gemessenen Elektronenmasse.
Die Einheitenumrechnung verwendet fuer beide Zeilen denselben archivierten
Faktor `5.6095892e29` MeV/c^2 pro kg, keinen neu importierten modernen Wert.

Die gespeicherte Datei `C 0.66/output_plus_neutrino.txt` gibt
`0.510998846703200` an. Unsere ideale reelle Rechnung liefert
`0.5109988467032000658474...`; Differenz etwa `6.58e-17` MeV/c^2,
kleiner als die letzte gedruckte Stelle. Das ist ein positiver Anschluss
an **diese Ausgabe**, keine physikalische Bestaetigung und kein Nachweis
eines exakt wiederholten historischen Programmlaufs.

## 1. Der entscheidende Unterschied sitzt in alpha3

Es geht hier um den Hilfskoeffizienten alpha3, nicht um die nackte
Feinstrukturkonstante alpha und nicht um die Massenfaktoren alpha+/-.
Setze d=eta(k=1,q=1), s=sqrt(d), a=nacktes alpha und R=(1-s)/(1+s).

```text
H006, bisherige explizite Profillesart:
alpha3 = 1 - a*xi^3*(1+s)^3/(3*d^3) - 2*sqrt(xi*d)/e * R^2

H010, aktive Pascal-/C-Zeilen:
alpha3 = 1 - a*xi^3*(1+s)  /(3*d^3) - 2*xi*d/e       * R^2
```

In H006 steht der Faktor `(1+s)` innerhalb der dritten Potenz. Im Code
steht er ausserhalb. Ausserdem besitzt der zweite Korrekturterm im Code
keinen Wurzeloperator mehr. Beide Unterschiede sind im betrachteten Fall
aktiv, also weder weggekuerzt noch bloss verschiedene Schreibweisen.

Die Folge ist hier besonders leicht nachvollziehbar:

```text
n=0:  K=H=0,
G = 144*alpha1 + 56*alpha2 + 12*alpha3 + 4,
M = mu*alpha+*(G+Phi).

Bei sonst festen Eingaben:
Delta M = 12*mu*alpha+*Delta alpha3.
```

Die grosse Phi-Formel, der zusammengefasste Codeausdruck `kgh=K+G+H`,
mu und die abschliessende Massenklammer stimmen im untersuchten N0-Fall
algebraisch ueberein. Die Konfigurationsindizes stimmen nach der expliziten
Verschiebung H006-x=1 <-> Code-x=2 ueberein. Kein Teilchenwechsel.

Fundstellen: H006 Druck/PDF5 (IX)--(XII); Pascal0.62c Zeilen383--384,
520--546; C0.66 Zeilen807--808,998--1026. Die vollstaendige statische
Gegenlesung und Quellhashes stehen in der
[Formelreview](../04_reconstruction/alpha_audit/reviews/HISTORICAL_N0_FORMULA_REVIEW_2026-09-06.md).

## 2. Was den Zahlenunterschied wie stark beeinflusst

Vor der Rechnung wurden sechs Wechsel festgelegt. Alle 64 Kombinationen
sind dokumentierte Gegenrechnungen; gemischte Zellen sind **keine behaupteten
historischen Fassungen**. In jeder Zelle werden die Auswahlmargen erneut
geprueft. Alle bleiben auf dem gleichen bedingten n=0-Pfad.

Die Tabelle zeigt zwei vollstaendige Wege zwischen identischen Endpunkten.
Ein ppm bedeutet ein Millionstel des unveraenderten H006-Ausgangswerts.
Die zweite Spalte fuehrt die Wechsel von oben nach unten aus; die dritte
in umgekehrter Reihenfolge, hier nur zur leichteren Zuordnung gleich sortiert.

| Wechsel H006 -> H010 | Beitrag in Reihenfolge 1, ppm | Beitrag bei umgekehrter Reihenfolge, ppm |
| --- | ---: | ---: |
| Potenzklammer in alpha3 | +3471.59572733 | +3471.87251141 |
| Wurzelfaktor in alpha3 | -0.13152590 | -0.13152373 |
| Vorgegebenes statt errechnetes nacktes alpha | -0.02326911 | -0.35736761 |
| Xi als goldener Schnitt statt gedruckter Dezimalzahl | +0.00023250 | +0.00023975 |
| Hbar des spaeteren Codes | -13.56247442 | -13.51551553 |
| Gamma des spaeteren Codes | -3.00238254 | -2.99203644 |
| Gesamt | +3454.87630786 | +3454.87630786 |

Die Potenzklammer dominiert auf beiden Wegen. Einzelbeitraege sind wegen
Wechselwirkungen aber nicht eindeutig: Ein anderer Alpha-Wert wirkt auf
eine andere alpha3-Formel anders. Nur die Gesamtdifferenz der festgelegten
Endpunkte ist unabhaengig von der Reihenfolge. Das Ergebnis ist keine
statistische oder experimentelle Ursachenschaetzung.

Neben beiden Ketten enthaelt der Snapshot die sechs isolierten Wechsel
am gemeinsamen Ausgangspunkt und jede minimale/maximale Achsenwirkung
ueber das vollstaendige Raster. Die Summe der sechs isolierten Wechsel
ist deshalb nicht automatisch die Gesamtdifferenz.

## 3. Die Programme berechnen ihr nacktes Alpha hier nicht selbst

Pascal und C setzen aktiv `alpha=1/137.03599976`, im Code als CODATA1998
kommentiert. Die alternative Heim-Alpha-Berechnung steht dort nur in einem
auskommentierten Testblock. Unser bestehendes H006-Profil berechnet dagegen
die festgelegte `1982_source_literal`-Lesart mit Kehrwert
`137.049188026664...`. Die alten Alpha-Fragen verschwinden somit nicht
dadurch, dass der archivierte H010-Ausgabewert nachvollzogen werden kann.

Weitere aktive Unterschiede sind hbar=`1.054571596e-34` statt
`1.0545887e-34` Js und gamma=`6.6733198e-11` statt `6.6732e-11`
m^3/(kg s^2). c und s0 bleiben gleich. Die genaue aktive Zuweisung zaehlt:
Im Pascaltext werden aeltere Werte ueberschrieben; entsprechende Bloecke
im C-Text sind deaktiviert. Beta ist ebenfalls vorgegeben, geht nach
regulaerer Nullreduktion hier aber nicht in die Masse ein. Beide
A36-Domaenen sind im eigenen Raster positiv geprueft.

Das spaetere H010-Archivprofil hat somit Eingaben, darunter einen empirischen
Alpha-Wert. Es ist keine parameterfreie Ableitung allein aus Geometrie.
Quellenherkunft, aktive Zeilen und Bannergrenzen:
[Konstantenreview](../04_reconstruction/alpha_audit/reviews/HISTORICAL_N0_CONSTANTS_REVIEW_2026-09-06.md).

## 4. Was die Rundung erklaert und was nicht

Der analytisch zertifizierte letzte Schritt bleibt
`K4=-3*ln(exp(-1/3))=1`. Ein geringfuegig zu grosser numerischer Rest kann
den berechneten Rohwert unter 1 druecken. Abschneiden wuerde dann K4=0
und n4=-1 ergeben. Die historische Dokumentation beschreibt gerade ein
solches Problem; Pascal0.62c verwendet `trunc(v+1e-10)`, C0.66 aktiv einen
vorzeichenabhaengigen Zuschlag von `1e-7`. Die C-README erbt trotzdem
den aelteren Pascal-Changelogabsatz. Text und aktive Funktion sind getrennt.

Unsere Rechnung uebernimmt keinen dieser pauschalen Zuschlaege. Fuer
diesen Fall liefern die ersten drei Greedy-Schritte in jeder Zelle die
notwendigen positiven Abstaende; danach gilt die exakte Identitaet.
Es ist kein allgemeiner Rundungsalgorithmus fuer andere Zustaende.

Als separat vorab festgelegte Diagnose ergibt allein n4=0 -> -1 bei
festgehaltenem historischen Rest:

```text
Delta M = -4*mu*alpha+
M(n4=-1) = 0.501711750952360223... MeV/c^2.
```

Das stimmt innerhalb der Druckaufloesung mit der als Pascal0.61
bezeichneten Zeile `0.501711750952360` der historischen Vergleichsdatei
ueberein. Dieser nachtraegliche Abgleich eines vorher festgelegten
Diagnoseschritts macht die archivierte Erklaerung quantitativ plausibel.
Er belegt nicht, welchen Compilerlauf die Datei tatsaechlich dokumentiert.
Insbesondere ist er **nicht** die Erklaerung der H006/H010-Potenzabweichung.

Die Quelle dafuer ist die Datei
`Pascal 0.62/compared results of Heim 1982 implementations.txt`,
Kopf und Elektronzeile 03; nicht das ungeoeffnete
Excel-Workbook. Die dort ebenfalls vorhandenen experimentellen
Vergleichsspalten werden hier nicht ausgewertet.

## 5. Eine ausdrueckliche Grenze unserer eigenen Wurzellesung

Die hochaufgeloeste H006-Seite zeigt ein Wurzelzeichen, aber keinen
eindeutig abgrenzenden horizontalen Wurzelstrich. Deshalb ist
`sqrt(xi*d)` eine festgehaltene Lesart, kein typographisch lueckenloser
Beweis gegen die Alternative `sqrt(xi)*d`.

Wir haben die Alternative separat und ohne Massenziel gerechnet. Sie
ergibt im sonst unveraenderten H006-Profil
`9.07801749271749e-31 kg`, also rund `2.82e-39 kg` mehr. Diese kleine
Sensitivitaet erklaert die viel groessere H006/H010-Differenz nicht.
Die sichere Aussage bleibt bei beiden Lesarten: H010 enthaelt dort
gar keine Wurzel. Der alte Rechner und seine drei Snapshots bleiben
unveraendert; seine Normalisierungsnotiz hat einen sichtbaren Nachtrag.

## 6. Warum diese Fassungen voneinander abweichen, bleibt offen

Die gelesenen Readmes und Kommentare rechtfertigen diese beiden konkreten
alpha3-Aenderungen nicht. Allgemeine Hinweise auf andere Klammerkorrekturen
sind kein Nachweis, dass genau die gefundene alpha3-Form beabsichtigt oder
von Heim autorisiert war. Auch eine gut passende Masse entscheidet diese
Editionsfrage nicht. Ein Druck-, Uebertragungs- oder Herleitungsfehler bleibt
jeweils moeglich, ohne hier bereits als Ursache bewiesen zu sein.

Zusaetzlich traegt die gespeicherte Ausgabe einen C0.62-Kopf, die vorliegende
Quelle dagegen C0.66. Archivierte Codekommentare zum DESY-Programm ersetzen
kein verifiziertes Original von 1982. Unser Zahlenanschluss hebt diese
Provenienzgrenze nicht auf.

Der naechste sinnvolle Quellenauftrag ist daher eng: Woher kommen gerade
die beiden alpha3-Korrekturterme und ihre Potenzen? Konkreter Suchanker
ist die Codereferenz `(3-5) f(kq,k)` neben alpha3 (Pascal376/C797),
zusammen mit dem im Codeheader genannten Formelblattdatum 17.9.1978.
Das ist ein Hinweis fuer die Suche, keine bereits verifizierte Urschrift.
Diese Spur gegen H006(IX) und die schon erfassten Buch-/Manuskriptstellen
verfolgen; Originalfassung oder konkretes Erratum hinzunehmen, falls auffindbar.
Den G-Wert nicht auf eine gewuenschte Zahl setzen und keine Formel nach
der Elektronenmasse auswaehlen. Breite moderne Widerlegungsrecherche und
vollstaendiges Teilchenspektrum bleiben weiterhin nachgeordnet.

## 7. Nachrechnen und Sicherung

Eingaben: `04_reconstruction/alpha_audit/historical_n0_inputs.json`.
Vertrag: `NORM-HISTORICAL-N0-COMPARISON.md` im selben Ordner.
Rechner: `scripts/audit_historical_n0.py`.
Ergebnis: `05_analysis/historical_n0_results.json`.

```powershell
py -3.13 scripts/audit_historical_n0.py --check --verify-sources
py -3.13 -m unittest discover -s tests -q
```

16 neue Tests pruefen unter anderem alle Masken und Auswahlmargen,
Gleichheit mit dem unveraenderten H006-Rechner, getrennte Wurzellesart,
80/120-Stellenstabilitaet, exakte n4-Schrittform, Mu-Skalierung und die
Rueckwirkungsfreiheit veraenderter Vergleichswerte. Eigene unabhaengig
berechnete Zahlenanker sichern den Anschluss als Dauerregression.

Die unabhaengige Gegenrechnung verwendet Machin-pi, eine e-Reihe,
Newtonwurzeln, eine andere Alpha-Loesung und die mu^12-Identitaet.
Sie bestaetigt 65 Zellen mit je 21 Feldern in drei Vergleichsgruppen:
eigene80/120, Snapshot80 gegen eigene120, API120 gegen eigene120.
Die groesste relative Snapshotabweichung ist kleiner als `6.78e-78`.
Beide Attributionsketten und alle Marginalbereiche sind mitgeprueft.
Root hat alle drei ausfuehrbaren eigenen Codebloecke der
[Mathematikreview](../04_reconstruction/alpha_audit/reviews/HISTORICAL_N0_NUMERICS_REVIEW_2026-09-06.md)
nach Durchsicht separat erneut ausgefuehrt.

Zehn Rechenchecks (die alten neun unveraendert), die verfuegbaren
Quellhashes und alle 127 Tests bestehen. FIND-029 fasst den eng begrenzten
Versions-/Implementierungsvergleich zusammen; nun 29 Befundgruppen, nicht
29 Fehler. Die 49 CSV-Normalisierungszeilen behalten ihren Status.

Alle vielen Dezimalstellen beschreiben nur Rechenpraezision unter festen
Eingaben. Sie sind keine physikalische Unsicherheitsangabe. Die Agenten-
Gegenpruefungen sind interne Kontrollen, kein externes Peer Review.
