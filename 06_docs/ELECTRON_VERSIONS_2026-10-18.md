# Vier Fassungen desselben Elektronenfalls

Nachtrag Etappe44: [H0111981 enthält exakt das H015-Alpha/Beta-Paar](ALPHA_LITERAL_ORIGIN_2026-10-18.md). Früher Zahlenbeleg gefunden; gemeinsame Herleitung damit nicht bestätigt. Die folgende Rechnung bleibt unverändert.

2026-10-18, Etappe43, Ausgang f241ee1.
[Vertrag](../00_admin/ELECTRON_VERSIONS_PLAN.md).

Die bisher reproduzierten Elektronenwerte gehören zu verschiedenen
Rechenverträgen. Der Unterschied zwischen fotografiertem H015 und späterem
H010 lässt sich jetzt vollständig in Massenskala, dimensionslosen Term
und Einheitenumrechnung zerlegen. Das erklärt eine Versionsdifferenz;
es ist keine Bewertung gegenüber heutigen Messdaten.

## Welche Ergebnisse stehen tatsächlich nebeneinander?

| Fassung | Eigene Rekonstruktion | Was wurde dafür festgelegt? | Grenze |
|---|---|---|---|
| H006, IGW-Wiedergabe | 9.07801746451643e-31 kg im Hauptprofil | Wörtliche lokale Alpha-Indexlesart; a3-Potenz-/Wurzelprofil; expliziter XXVI-N0-Weg; mathematisches pi/e, gedrucktes xi | Bedingte eigene Lesart; XIV/XXVI- und Alpha-Fragen bleiben. Kein gesicherter originaler Programmlauf |
| H015, fotografiertes FORTRAN | 9.109531267255284e-31 kg;0.5110032557257554 MeV | Gedruckte Eingaben und aktive Formeln; a3 mit einfachem(1+s), ohne Wurzel im zweiten Term; letzter Integer analytisch | Passt zu0.51100326 im Foto. Kein bitgenauer Compilerlauf und keine geklärte Herkunft aller Inputs |
| H010, spätere Pascal/C-Fassung | 9.10938089197690e-31 kg;0.5109988467032001 MeV | Aktive spätere Konstanten, mathematisches pi/e und goldenes xi; dieselbe hier benötigte a3-Form wieH015 | Passt zum gespeicherten späteren Ausdruck. Exakter Quellcode-/Executable-/Aufrufnachweis fehlt |
| H004, korrigierter Buchanhang | Keine neue vollständige numerische Reproduktion | Empirische Elektronenmasse und Ladung als Rückrechnungsanker; korrigierte Endkonstanten und eigenes Buchmodell | Originaler D_e-/Inputvertrag fehlt. H015-Zustand darf nicht stillschweigend eingesetzt werden |

H006 ist eine spätere Wiedergabe mit der Bezeichnung1982; H010 überliefert
ältere Banner. Beides datiert nicht automatisch jede Formel oder Ausgabe.
Die Bildbelege in H015 schließen einzelne Überlieferungslücken, nicht die
gesamte historische Fassungskette.

Die H006-MeV-Zahl des alten Vergleichs benutzte ausdrücklich den H010-
Umrechnungsfaktor für beide Vergleichsspalten. Sie war keine neu entdeckte
H006-Ausgabe. Deshalb zeigt die erste Zeile hier ausschließlich kg.

## Die Eingaberollen unterscheiden sich

| Rolle | H006-Rekonstruktion | H015 | H010 | H004-Korrektur |
|---|---|---|---|---|
| Nacktes alpha | Aus festgehaltener Formel-/Indexlesart gerechnet | 1/137.03602725 fest | 1/137.03599976 fest; CODATA1998-Kommentar | Gedruckte105-Zahl137.03596147; eigene alte Diagnose bleibt |
| beta | Zugehöriger gerechneter Zweig | 1/1.00001411 fest | 1/1.00001411 fest | Eigenes gedrucktes Paar; nicht aus H015 importieren |
| hbar | 1.0545887e-34 | 1.0545887e-34 | 1.054571596e-34 | Endtabelle druckt h=6.626173e-34, nicht hbar |
| gamma | 6.6732e-11 | 6.6732e-11 | 6.6733198e-11 | 6.672131e-11 als korrigierter Endwert |
| MeV/kg | Im alten Hauptprofil keine eigene historische Umrechnung | 5.609545e29 | 5.6095892e29 | Nicht für eine neue Rechnung ergänzt |
| Elektronenmasse als Anker | Kein Massenziel im eigenen Rechner | Nicht als direkte GMASS-Eingabe; frühere Auswahlgeschichte offen | Nicht als direkte GMASS-Eingabe; spätere Parameterherkunft gesondert | Rückrechnung aus empirischem m_e ausdrücklich beschrieben |

H010 ist kein durchgehend aus CODATA übernommener Konstantensatz:
Die aktive gamma-Zeile trägt den Kommentar "theory W.Droescher(2002)".
Dieser Kommentar ist eine Herkunftsbehauptung der Datei, keine hier
geprüfte unabhängige Herleitung. Im Pascal stehen ältere Werte davor und
werden überschrieben. Dort ist auch das H015-Alpha als alte Sch-Zuweisung
erhalten; das Foto bestätigt diesen Zahlenstand direkt.

Ein universeller empirischer Konstanteneingang ist nicht automatisch ein
frei angepasster Parameter. Umgekehrt beweist ein fehlendes m_e-Argument
im letzten Rechenschritt keine Unabhängigkeit der vorgelagerten Kalibrierung.
Diese Rollen müssen anhand von Herkunft und Festlegung getrennt werden.

## Quantitative H015–H010-Zerlegung

Setze D=alpha_plus*(KGH+FIG), M_kg=mu*D und M_MeV=f*M_kg.
Beide unveränderten Endpunkte liefern:

```text
D_H015 = 4.032511314470189
D_H010 = 4.032511314749317
```

Das Verhältnis H010/H015 zerfällt in drei Faktoren. Die folgende Spalte
ist jeweils (Faktor-1)*10^6; diese gewöhnlichen ppm-Zahlen werden nicht
einfach addiert, sondern ihre Faktoren multipliziert.

| Faktor | Relative Änderung H015 -> H010, ppm |
|---|---:|
| Massenskala mu | -16.5075352963 |
| Dimensionsloser Term D | +0.0000692195 |
| Umrechnung f | +7.8794269410 |
| Gesamte Masse in kg | -16.5074660779 |
| Gesamter Zahlenwert in MeV | -8.6281692063 |

Die dimensionale Skala folgt unabhängig aus

```text
mu_H010/mu_H015 = (pi_H010/pi_H015)^(7/12)
                  *(hbar_H010/hbar_H015)^(5/6)
                  *(gamma_H010/gamma_H015)^(-1/6),
```

weil c und s0 gleich bleiben. Die logarithmischen Skalenbeiträge sind
pi:+0.0000166729, hbar:-13.5156473035 und gamma:-2.9920409165
in10^6*log(Faktor). Nur diese Logarithmen addieren sich exakt und ohne
Abhängigkeit von der Reihenfolge. Die nahezu unveränderte D-Zahl gilt
für diese beiden Endpunkte; sie ist keine allgemeine Sensitivitätsgarantie.

Die H006–H010-Formeldifferenz ist wesentlich größer und wurde bereits
in Etappe17 mit64 vorab fixierten Kombinationen geprüft. Dort dominiert
die andere a3-Potenzklammer. Dies wird nicht mit dem hier untersuchten
H015–H010-Konstantenwechsel vermischt.

## Was folgt für einen unabhängigen Test?

Mehrere passende Ausdrücke derselben Elektronenrechnung sind keine
mehreren unabhängigen Vorhersagen. H004 nennt m_e ausdrücklich als Anker.
Bei H015/H010 bleibt zwar der lokale Massenalgorithmus nachvollziehbar,
aber die ursprüngliche Auswahl-/Kalibrierungsgeschichte der Eingaben
entscheidet über die weitergehende Vorhersagebehauptung.

Ein anderer Teilchenname reicht dafür ebenfalls nicht aus: Die17
F_S-Komponenten umfassen bereits mehrere bekannte Massen. Die genaue
ursprüngliche Arbeitstabelle und die gemeinsamen Funktionsannahmen
müssen bekannt sein, bevor ein davon unabhängiger Testfall benannt wird.

## Verzweigungsentscheidung

1. **H015 -> H010:** lokale Zahlenabweichung durch feste Endpunktfaktoren
   erklärt. Weitere Anpassung oder Variantenraster bringt hier keinen Nutzen.
2. **H015 -> korrigierter H004-Anhang:** ohne originalen D_e-/Inputvertrag
   ist eine neue Rückrechnung nicht eindeutig. Diese numerische Spur bleibt
   offen; kein Ersatzprofil wird passend gemacht.
3. **Nächste konkrete Quellenspur:** Herkunft des H015-ALFA-Literals
   137.03602725 und sein Verhältnis zu früheren Ladungs-/Alphaformeln.
   Falls keine tragende Herkunft greifbar ist, zurück zur Frage der
   unabhängigen Eingaben und zur F_S-/Kalibrierungsprovenienz wechseln.

## Quellen und Reproduzierbarkeit

Diese Etappe synthetisiert die quellengeprüften Berichte
[H006/H010](HISTORICAL_N0_2026-09-06.md),
[Konstantenanker](CONSTANTS_ANCHOR_2026-10-18.md),
[H015-Konstanten](HISTORICAL_CONSTANTS_2026-10-18.md) und
[H015-Elektron](H015_ELECTRON_2026-10-18.md).
Keine neue Original-PDF-Lektüre in dieser Etappe behauptet.
Pascal GVALUES/GINIT Zeilen141-215 erneut statisch gelesen;
Suchumfang der konkreten Alpha-Zahl: lokale PAS/pas/c/txt/md-Dateien
im massformula-Archiv, ausdrücklich mit eingeschlossenen ignorierten Dateien.
Der Treffer ist eine spätere Wiederholung, noch kein Herleitungsbeleg.

Eigene neue [Faktordiagnose](../scripts/audit_electron_versions.py) und
[Ergebnisse](../05_analysis/electron_versions_results.json):
`py -3.13 -B scripts/audit_electron_versions.py --check`.
90/110-Stellen-Ausgaben stimmen bei16 signifikanten Stellen überein;
Skalen-, Produkt- und Logidentitäten unter1e-65 geprüft.
Alte H006/H010/H015-Ergebnisse frisch nachgerechnet und unverändert.
FIND-053 ist eine eigene Versionsdiagnose, kein empirischer Fehlerbefund.
