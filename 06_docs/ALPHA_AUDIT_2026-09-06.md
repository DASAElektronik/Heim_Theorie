# Alpha-Audit 1982 / 1989

Stand: 2026-09-06. Erster abgeschlossener, ausfuehrbarer Auditblock.

Die erfassten Alpha-Gleichungen lassen sich jetzt unabhaengig nachrechnen.
Die dazu gedruckten Zahlen sind untereinander und mit den ausgewerteten
Formeln nicht durchgaengig vereinbar. Fuenf Paar-/Kehrwertpruefungen bleiben
auch unter Rundungsintervallen widerspruechlich. Das problematische
1982-Zahlenpaar steht ebenfalls im visuell geprueften Buchscan.

## Umfang und Quellen

- [1982 IGW-Wiedergabe](../01_sources/heim_primary/Massenformel_nach_B_Heim_1982.pdf),
  PDF-Seiten 3-5: (V), Alpha-Block, (IX).
- [1989 IGW-Wiedergabe](../01_sources/heim_primary/Erweiterte_Massenformel_Nach_Heim_1989.pdf),
  PDF-Seite 3 / Druckseite 12: Fortsetzungsverweis; PDF-Seite 9 / Druckseite 18:
  (B58)-(B62).
- [Elementarstrukturen der Materie 2](../01_sources/heim_primary/Burkhard%20Heim%20-%201996%20-%20Elementarstrukuren%20der%20Materie%202.pdf),
  PDF-Folios 307-309 / Druckseiten 301-303: Gleichung (105) und Zahlenpaar.

Die IGW-Dokumente sind Wiedergaben von 2002/2003. Die Bezeichnungen 1982 und
1989 sind keine alleinigen Nachweise fuer historische Prioritaet jeder Zahl.
PDF-Hashes und URLs sind in
[inputs.json](../04_reconstruction/alpha_audit/inputs.json) festgehalten.
Gedruckte Zahlen bleiben unveraenderte Strings; keine Fremdprogramme oder
Makros wurden ausgefuehrt.

## 1. Interne Zweigbedingung

Beide Alpha-Bloecke haben fuer festgelegte rechte Seite R die Form

```math
a\sqrt{1-a^2}=R,\quad a>0.
```

Mit t=a^2 gilt t^2-t+R^2=0. Fuer die beiden positiven Loesungen folgt daher

```math
a_+^2+a_-^2=1,\qquad a_+a_-=R.
```

Diese notwendige Bedingung ist unabhaengig von eta, pi, Indexwahl und Messdaten.
Sie gilt auch bei einem gemeinsamen Y3-Faktor auf der rechten Seite.

| Gedruckte Daten | Summe der Alpha-Quadrate, Zentralwerte | Vereinbar mit 1 einschliesslich Rundung? |
|---|---:|---|
| 1982: inverse Werte 137,03596147 / 1,00001363 | 1,00002599194107416 | Nein |
| 1989 B62: direkte Alpha-Werte | 1,00002503195114346 | Nein |
| 1989: eingerahmte inverse Werte | 1,00002485195094520 | Nein |

Fuer jede gedruckte Dezimalzahl wird konservativ ein geschlossenes Intervall
von +/- einer halben letzten Dezimalstelle zugelassen. Die Intervallgrenzen
werden nach aussen gerundet. Alle drei Intervalle fuer die Quadratsumme
schliessen 1 aus. Die vollstaendigen Grenzen stehen im
[Ergebnis-JSON](../05_analysis/alpha_audit_results.json).
Diese Druckintervalle sind keine statistischen Messunsicherheiten.

## 2. B62 und seine Kehrwerte

| Gedrucktes Alpha in B62 | Unabhaengig berechneter Kehrwert | Gedruckter Kehrwert |
|---|---:|---:|
| 0.0072973525253328589 | 137,0359999093488152 | 137,03601 |
| 0.999985890199089 | 1,000014110000000291 | 1,0000142 |

Die zulaessigen Druckintervalle der letzten Spalte sind
[137,036005; 137,036015] und [1,00001415; 1,00001425]. Selbst nach
Fortpflanzung der Druckintervalle der direkten Alpha-Zahlen besteht keine
Ueberlappung. Damit liegen zwei weitere Konsistenzverletzungen vor.
Die fuenf Checks sind diagnostische Beziehungen, keine fuenf statistisch
unabhaengigen Experimente.

## 3. Auswertung der Formeln

Mathematisches pi, 80 signifikante Dezimalstellen intern; nachfolgend gekuerzt.
Die 1989-Definition verwendet gemaess ihrem Verweis vor B8 auf (IX) die
Reihenfolge (q,k). Die (k,q)-Alternative ist ein Gegenversuch zur Sensitivitaet.
Die Definition von vartheta steht ausdruecklich in (V), nicht vollstaendig
in (IX); diese Ungenauigkeit der Quellenreferenz bleibt dokumentiert.

| Modell | 1/alpha_plus | Bezug zum gedruckten positiven Kehrwert |
|---|---:|---|
| 1982, woertliche lokale (k,q)-Lesart | 137,049188026664 | Abweichung +0,013226556664 |
| 1982, vorhandene Indexvariante | 137,035960995152 | Abweichung -0,000000474848 |
| 1989, Quellenverweis mit (q,k) | 137,036039529722 | Abweichung +0,000029529722 |
| 1989, (k,q)-Gegenversuch | 137,036279118941 | Abweichung +0,000269118941 |

Auch die 1982-Indexvariante trifft den gedruckten Wert nicht auf dessen
angegebene Genauigkeit: etwa 47,48 Einheiten der letzten Stelle bleiben.
Die bisherige Formulierung, sie "reproduziere" den gedruckten Wert, wurde
daher korrigiert. Der historische Variantenname `printed_alpha_fit_variant`
bleibt fuer Nachvollziehbarkeit bestehen; er behauptet keinen erfolgreichen Fit.

Ein zweites Profil mit gedrucktem pi=3,1415926535 aendert die Ergebnisse nur
geringfuegig und beseitigt keine dieser Abweichungen. Sein Einsatz fuer 1989
ist ein Sensitivitaetstest, keine behauptete historische Konstantenwahl.

## 4. Buchquelle und Faktor Y3

Der Quellenagent und der Hauptagent haben Druckseiten 301-302 im Scan geprueft.
Gleichung (105) enthaelt `1-A1*A2*Y3` und dieselbe linke Seite
`alpha*sqrt(1-alpha^2)`. Die Prosa fuehrt Y3 zur Beruecksichtigung einer
Unsicherheit ein und setzt fuer die anschliessende Zahlenrechnung Y3=1.
Daneben steht dasselbe reziproke Paar wie in der 1982-IGW-Wiedergabe.

Damit ist das Zahlenproblem im lokalen Buchscan selbst sichtbar. Es ist
nicht allein durch die spaetere IGW-Abschrift oder heutige OCR erklaerbar.
Das lokalisiert den Befund genauer, identifiziert aber noch nicht den
urspruenglichen Rechen- oder Druckfehler. Eine beliebige gemeinsame Y3-Wahl
koennte die gegenseitige Zweiginkonsistenz nicht beheben.

Die Herkunft und allgemeine Festlegung von Y3 sowie die gesamte Herleitung
von A1/A2 sind nicht durch diesen engen Test geklaert. Eine parameterfreie
Ableitung wird deshalb nicht behauptet. 1989 ersetzt die rechte Korrektur
durch C'; diese andere Formelversion muss eigenstaendig bleiben.

## 5. Getrennter moderner Vergleich

NIST nennt fuer CODATA 2022 den dimensionslosen Referenzwert
1/alpha=137,035999177 mit Standardunsicherheit 0,000000021.
[NIST-Kompletttabelle](https://physics.nist.gov/cuu/Constants/Table/allascii.txt),
abgerufen am 2026-09-06, Zeile "inverse fine-structure constant".

Die relative Differenz der 1982-Indexvariante betraegt etwa -0,278626 ppm;
die 1989-Lesart ueber den Quellenverweis liegt bei +0,294468 ppm.
Diese Werte sind beschreibende Residuen. Ohne Unsicherheitsmodell fuer die
Theorie und ihre Varianten folgt daraus keine statistische Ausschlusszahl.
Der Messwert ist kein Input der Gleichungen und waehlt keine Variante aus.

## Pruefung und Wiederholung

```powershell
py -3.13 scripts/audit_alpha.py --check --verify-sources
py -3.13 -m unittest discover -s tests -v
```

13 Tests bestanden: unabhaengige Loesungs-/pi-Werte, Grenzfaelle, Rundung,
80/120-Stellen-Konvergenz und Unabhaengigkeit von Referenzwerten.
Die Rechnung benoetigt nur Python >=3.10 mit Standardbibliothek.
Ohne lokale PDFs kann der numerische Audit ohne `--verify-sources` laufen.

[Quellenreview](../04_reconstruction/alpha_audit/reviews/SOURCE_REVIEW_2026-09-06.md)
von GPT-5.6 Terra; [Mathematikreview](../04_reconstruction/alpha_audit/reviews/MATH_REVIEW_2026-09-06.md)
von GPT-6 Astra mit vorab unabhaengig berechneten Referenzzahlen. Der empfohlene
zusaetzliche 1989-Regressionstest wurde nach dieser Review als 13. Test aufgenommen.

## Naechste abgegrenzte Arbeitspakete

1. Buchherleitung um (105) rueckwaerts auf Definitionen von eta, A_k und Y3
   verfolgen; Ausgabe, Errata und moegliche aeltere Rechenblaetter identifizieren.
   Ziel: Ursache lokalisieren, keine willkuerliche Korrektur passend zum Zielwert.
2. B58-B62 mit weiteren belegbaren 1989-Fassungen vergleichen; Quelle des
   Zahlenkastens und des erwaehnten Messwerts von 2002 pruefen.
3. Danach Massenspektrum: fehlende Abhaengigkeiten katalogisieren und die
   getrennten B50-/Gamma-Q_N-Fragen bearbeiten. Der Alpha-Audit allein
   schliesst die Massenrekonstruktion nicht ab.

Wiedereinstieg und Sicherungsstand: [RESUME.md](../00_admin/RESUME.md).
