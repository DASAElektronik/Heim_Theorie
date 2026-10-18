# Der fotografierte Konstantensatz und seine Ausgabe

2026-10-18, Etappe41. Ausgang `b2c1113`.
[Vertrag](../00_admin/HISTORICAL_CONSTANTS_PLAN.md),
[Quellenumfang und Hashes](../03_notes/HISTORICAL_CONSTANTS_SOURCES_2026-10-18.md).

## Ergebnis

Im bereits archivierten H015-Scan ist ein konkreter früher Programmstand
greifbar: GINIT aufPDF5 weist die Konstanten zu, PDF27 zeigt ihre Ausgabe.
Die17 geprüften Ausgabezeilen lassen sich mit diesen Eingaben innerhalb
der angenommenen Druckrundung nachrechnen. Das ist ein positiver lokaler
Reproduktionsbefund. Mehrere Zeilen sind bloße Wiedergaben fester Eingaben;
17 passende Zeilen sind weder17 Vorhersagen noch17 unabhängige Experimente.

Der gefundene Konstantensatz ist **nicht der korrigierte Satz aus H004371**.
Die Ladungsformel stimmt algebraisch mit der in Etappe40 verwendeten29
überein. Eine abweichende Formel im geprüften GINIT-Block erklärt die
kleine H004-Ladungsdifferenz deshalb nicht. Historische Zwischenstände
oder Druck-/Übertragungsursachen bleiben offen.

Zudem stehen ALFA und BETA im fotografierten Programm als feste
Kehrwerte. Die betreffende Programmausgabe ist daher kein Nachweis,
dass diese beiden Zahlen dort aus Heims Kopplungsgleichung berechnet wurden.
Ihre ursprüngliche Herkunft wird dadurch noch nicht bestimmt.

## 1. Was ist historisch belegt?

H015 enthält Fotografien von Listings und Ausgaben. AufPDF18 steht im
Programmbanner H.D.Schulz26/7/82. Im Kommentar steht17/03/82, während
der Compilerkopf bei GINIT DATE82.223/09.22.04 zeigt. PDF27 wiederholt
den26/7/82-Banner. Diese sichtbaren Angaben sind eine konkretere Spur
als allein die späteren Pascal-Kommentare; sie beweisen aber weder die
Echtheit des Papieroriginals noch den exakten Rechenlauf vom26.7.1982,
auf den der Buchanhang verweist.

MAIN ruft GINIT vor der Teilchenschleife auf. GINIT enthält die folgenden
Zuweisungen. Q in den Literalen ist die fotografierte FORTRAN-Schreibweise;
im neuen Diagnosecode wird es als Dezimalexponent gelesen, ohne historische
Compilerarithmetik zu emulieren.

| Größe | H015 GINIT, PDF5 | Rolle |
|---|---|---|
| PI | 3.1415926535Q0 | Feste Näherungszahl, nicht mathematisches pi importiert |
| EBN | QEXP(1.Q0) | Berechnet |
| HQ=hbar | 1.0545887Q-34 J s | Feste Eingabe |
| C | 2.99792458Q8 m/s | Feste Eingabe |
| GAM | 6.6732Q-11 m³ kg^-1 s^-2 | Feste Eingabe |
| RG | 376.73037659Q0 Ohm | Feste Eingabe |
| S0 | 1.Q0 m | Einheitsstrecke |
| FAKMEV | 0.05609545Q31 MeV/kg | Fester Umrechnungsfaktor |
| XI | 1.61803399Q0 | Feste Näherungszahl |
| ALFA | 1.Q0/137.03602725Q0 | Fester Kehrwert |
| BETA | 1.Q0/1.00001411Q0 | Fester Kehrwert |

Die nachfolgenden Größen ETA, THETA, EQ, AMU, ALFP und ALFM werden
ausgerechnet. Die Überschrift "abgeleitete Konstanten" im Ausdruck ist
allein keine verlässliche Klassifikation: Darunter stehen auch FAKMEV,
ALFA und BETA, deren Zahlen im Listing fest zugewiesen sind.
ALFP/ALFM sind die Massenfaktoren, nicht ALFA/BETA.

## 2. Lokale Nachrechnung des Initialisierungsblocks

Eigene normalisierte Transkription von GINIT ISN0015-0023:

```text
ETA = PI/(4+PI^4)^(1/4)
THETA = 5 ETA + 2 sqrt(ETA) + 1
EQ = 3/(4 PI^2) sqrt(2 THETA HQ/RG)
AMU = PI^(1/4) (3 PI S0 GAM HQ)^(1/3) sqrt(C HQ/(3 GAM))/(C S0)
TEMP1 = 1 - (2/3) XI ETA^2 (1-sqrt(ETA))
ALFP = TEMP1/(ETA^2 ETA^(1/3)) - 1
ALFM = TEMP1/(ETA ETA^(1/3)) - 1.
```

Der Code hält PI/XI wie fotografiert fest; mathematisches pi oder der
exakte goldene Schnitt würden ein anderes Profil erzeugen. ALFA/BETA
werden nicht durch eine Formel aus einer anderen Ausgabe ersetzt.
Die Ergebnisse waren durch den Ausdruck vorab bekannt. Ein Abgleich
mit unabhängigen Messdaten gehört nicht zu diesem Test.

| Größe | Eigene Nachrechnung | Fotografierter Ausdruck PDF27 |
|---|---:|---:|
| ETA | 0.9899896408182263 | 0.98998964Q+00 |
| THETA | 7.939912666907718 | 0.79399127Q+01 |
| EQ in C | 1.602177452229043e-19 | 0.16021775Q-18 |
| AMU in kg | 2.259021874177218e-31 | 0.22590219Q-30 |
| ALFP | 0.01832211507605286 | 0.18322115Q-01 |
| ALFM | 0.008128344941398045 | 0.81283449Q-02 |

Alle17 erfassten Zeilen einschließlich der übrigen Eingabewiedergaben
liegen innerhalb einer halben letzten gedruckten Einheit. Das ist die
ausdrücklich angenommene Rundungsregel, keine neue Aussage über
historische Messunsicherheiten. Die60-/90-Dezimalstellenläufe stimmen
in den gespeicherten16 signifikanten Stellen überein. Eine separate
direkte math/binary64-Rechnung liefert EQ=1.602177452229043e-19 C und
AMU=2.259021874177222e-31 kg, ebenfalls innerhalb der Druckrundung.
Es handelt sich nicht um eine bitgenaue IBM-REAL*16-Emulation.

## 3. Welche Fassungen dürfen nicht gleichgesetzt werden?

| Gegenstand | Fotografiertes H015 | H004371 / Etappe40 | Spätere H010-Standardwerte |
|---|---|---|---|
| hbar | 1.0545887e-34 | Dort h=6.626173e-34; erst durch2pi teilen | 1.054571596e-34 |
| gamma | 6.6732e-11 | 6.672131e-11 | 6.6733198e-11 |
| R_- / RG | 376.73037659 | Aus epsilon0/mu0 etwa376.724580381 | 376.730313461 |
| alpha^-1 | 137.03602725 fest zugewiesen | 137.03596147 gedruckte105-Ausgabe | 137.03599976 fest zugewiesen |
| Ladungsausgabe | 1.6021775e-19 C gerundet | 1.602188e-19 C gedruckt | Eigener späterer Konstantensatz; kein1982-Beleg |

Die H010-Spalte folgt dem vorhandenen statischen Konstantenreview;
GVALUES/GINIT im Pascal wurden erneut gelesen. Dort sind mehrere alte
Werte als "Sch" erhalten, werden aber von späteren Zuweisungen ersetzt.
H015 belegt jetzt einige dieser alten Konstanten direkt im fotografierten
Listing. Es belegt nicht die Identität des gesamten H010-Programms.

Auch der H010-Vergleichstext mit FORTRAN im Titel ist zu trennen: Er
nennt eine Ausgabeliste vom2002-12-02 und Pascal2006, trägt aber weiterhin
den26/07/82-Programmbanner. Seine gedruckten Konstanten entsprechen dem
späteren Profil. Der alte Banner allein datiert also keine konkrete Ausgabe.

Die H006/IGW-Darstellung enthält denselben dimensionalen hbar/c/gamma-
Zahlensatz wie H015, nach dem bisherigen Quellenreview. Daraus folgt
keine vollständige Fassungsgleichheit: Formeln, Kopplungseingaben und
Rundungsregeln müssen jeweils separat zugeordnet werden.

## 4. Bedeutung für den bisherigen Befund

Positiv: Ein konkret fotografierter Initialisierungsstand ist jetzt
quellengebunden und seine Ausgabe lokal reproduziert. Die29-Formel ist
auch in dieser frühen Programmspur vorhanden; sie ist nicht erst durch
die spätere Pascal-/C-Abschrift belegt.

Offen: Die eigentliche Konstantenkorrektur des Buchanhangs wird hier
nicht nachgerechnet. Das Programm weist gamma/RG/hbar fest zu; dieser
GINIT-Block löst sie nicht rückwärts aus e und m_e. Dass der Ausgabekopf
zum im Buch erwähnten Kontrolllauf gehört oder dass beide denselben
Konstantensatz benutzt hätten, ist nicht nachgewiesen. Die0.866-ppm-
Diagnose der Etappe40 bleibt auf ihren eigenen H003/H004-Vertrag begrenzt.
Sie wird weder durch H015 ersetzt noch durch dessen andere Zahlen erklärt.

Ein sinnvoller nächster Einzelauftrag ist nun der **Elektron-N0-Zweig
dieses H015-Programms**: Zustand, GBASE-/GMASS-Formeln und Umrechnung
vorab festhalten, dann gegen den fotografierten Elektronenausdruck
prüfen. Das wäre ein historischer Reproduktionstest, kein unabhängiger
physikalischer Vorhersagetest. Die H004-Kalibrierung und ursprüngliche
F_S-Datenprovenienz bleiben davon getrennte offene Fragen.

## 5. Reproduktion und Integrität

```powershell
py -3.13 -B scripts/audit_historical_constants.py --check
py -3.13 -B -m unittest discover -s tests
py -3.13 -B scripts/validate_finding_register.py
```

[Eingabetranskription](../04_reconstruction/alpha_audit/historical_constants_inputs.json),
[Diagnosecode](../scripts/audit_historical_constants.py),
[Ergebnisse](../05_analysis/historical_constants_results.json),
[Tests](../tests/test_historical_constants.py).
Vier neue Tests,364 insgesamt bestanden. FIND-051 ist ein positiver
lokaler Reproduktionsbefund;51 Befundgruppen sind keine Fehlerzählung.
Die50 früheren Registereinträge und sämtliche alten Rechenprofile,
Ergebnisse, Normalisierungen sowie die datierte Übersicht/PDF bleiben erhalten.
Ein Agent, keine unabhängige Begutachtung. Kein neuer Commit/Push.
