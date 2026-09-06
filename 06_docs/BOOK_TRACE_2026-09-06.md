# Alpha-Buchherleitung: zweite Audit-Etappe

Stand: 2026-09-06. Interne Konsistenz, Quellenprovenienz und offene Annahmen;
keine Gesamtbewertung von Heims Physik.

## Ergebnis

Wir koennen mehr von der Herleitung nachvollziehen, aber noch keine
vollstaendig geschlossene Alpha-Theorie rekonstruieren. Wesentliche
Zwischenschritte sind als Annahmen formuliert. Heim benennt insbesondere
den Faktor Y3 als Unsicherheit und setzt ihn fuer seine Zahlenrechnung auf 1.
Eine andere gemeinsame Wahl von Y3 kann die beiden gedruckten Zweigwerte
nicht gleichzeitig herstellen. Der Grund ist bereits die komplementaere
Wurzelidentitaet, kein neuer experimenteller Test.

Ordinaere binary64-Ausloeschung erklaert die Abweichung nicht. Sehr geringe
Dezimalpraezision kann dagegen Fehler gleicher Groessenordnung erzeugen;
ein historischer Rechenweg ist damit weder nachgewiesen noch ausgeschlossen.

## Was die Quellenkette traegt

| Stelle | Inhalt | Erkenntnisstatus |
|---|---|---|
| Band I, Druck247, (28a) | `eta=pi/fourth_root(pi^4+4)`; `eta_1=eta` | Explizite Definition in gepruefter 1998-Ausgabe |
| Band I, Druck247/248, (28)/(29) | Ladungskomponenten und Mittelung ihrer Potentiale | Physikalische Annahmen; nachfolgende Algebra nachvollziehbar |
| Band I, Druck248, (29)/(29a) | `vartheta=5*eta+2*sqrt(eta)+1`; vorlaeufige Alpha-Naeherung | Definition und bedingte Folge, keine voraussetzungsfreie Ableitung |
| Band II, Druck1 | Ungeklaerte Beziehungen mit Y_k versehen; Tabellen mit allen Y_k=1 | Ausdrueckliche Rechenpolitik |
| Band II, Druck301 | Von Proportionalitaet zu `C=A1*A2`; verbleibende Unsicherheit Y3 | Kein belegter Zwang auf Y3=1 |
| Band II, Druck302, (105) | Alpha-Gleichung und A_k in eta_1k; Zahlenbeispiel Y3=1 | Explizite Gleichung, Indexbedeutung nicht hier definiert |

Band I wurde nur an den angegebenen Stellen geprueft. Der Scan ist eine
spaetere, laut Titeltext veraenderte Ausgabe; wir schreiben ihre Formeln
nicht ungeprueft dem urspruenglichen Erscheinungsjahr zu. Die zweiindizierte
eta-Familie und die physikalische Begruendung der Mittelung bleiben offen.

Quellen/Seiten/Abbildungen:
[Band-I-Notiz](../03_notes/EDM1_ALPHA_DEPENDENCIES_2026-09-06.md),
[Band-II-Quellenreview](../04_reconstruction/alpha_audit/reviews/BOOK_DERIVATION_REVIEW_2026-09-06.md).

## Y3-Rueckrechnung: Diagnose, keine Vorhersage

Mit `R0=9*vartheta/(2*pi)^5`, `P=A1*A2` und einem vorgegebenen `d=1/alpha`
lautet die Inversion:

```text
R_required(d) = sqrt(d^2-1)/d^2
Y3_required(d) = (1-R_required(d)/R0)/P
```

Sie verwendet die Buch-(105)-Struktur mit den zwei **expliziten IGW1982-
Indexprofilen**. Damit wird keine vollstaendige, buchautarke numerische
Herleitung behauptet. Zahlen unten: mathematisches pi, 80 Dezimalstellen;
gezeigt sind gerundete Auszuege.

| Zielwert fuer die Rueckrechnung | Y3 mit lokaler 1982-Indexlesart | Y3 mit separater vertauschter Indexvariante |
|---|---:|---:|
| Gedruckt: `1/alpha_plus=137.03596147` | 0.106739226858 | 1.000300562531 |
| Gedruckt: `1/alpha_minus=1.00001363` | 2633.652578318402 | 24681.124579619378 |
| Bereits hinterlegte CODATA2022-Referenz | 0.109286029194 | 1.024167775031 |

Die aus den beiden gedruckten Angaben resultierenden Y3-Intervalle sind
disjunkt, auch unter bedingten Halb-Letzte-Stelle-Rundungsintervallen.
Bei positiver rechter Seite verlangt die gemeinsame Gleichung immer
`alpha_plus^2+alpha_minus^2=1`. Keine alleinige Aenderung der gemeinsamen
rechten Seite kann diese Bedingung entfernen.

Die letzte Tabellenzeile demonstriert nur eine nachtraegliche Kalibrierung.
Der verwendete Referenzwert steht mit Herkunft in `inputs.json`; er ist dort
NIST CODATA2022, nicht ein neuer externer Widerlegungstest. Nach der
Kalibrierung ist Alpha als Testdatum verbraucht. Der andere Zweig ist dann
eine algebraische Folge, noch keine physikalisch bestaetigte Kopplung.

## Welche Rechenfehlerhypothese geprueft wurde

Der direkte Ausdruck `sqrt(B*(1-sqrt(1-2/B)))`, `B=1/(2*R^2)`, verliert bei
kleinem R Stellen. Gegen die stabile Loesung betraegt sein binary64-Fehler
hier etwa `3.2e-14` bzw. `3.3e-13`; der Fehler des gedruckten negativen
Kehrwerts liegt dagegen bei `1.3e-5`.

Die zusaetzlich vorab festgelegten Dezimalversuche mit 8,10,12,16,24 Stellen
sind alle im Ergebnis-JSON enthalten. Bei 8 Stellen treten Fehler um
`1e-5` auf. Daher ist nur **binary64 als Erklaerung dieser Rechnung**
ausgeschlossen, nicht jede historische Rundung, Handrechnung oder
Abschreibvariante. Keine Praezision wurde nach einem passenden Treffer als
historisch zutreffend ausgewaehlt.

## Editions- und Zitatpruefung

Die aktuelle Herausgeberfassung der sogenannten 1989-Massenformel ist
byte-identisch zum lokal auditierten PDF. Sie ist eine IGW-Ueberlieferung
2002/2003 eines berichteten Manuskripts von 1989. Ihre Einleitung nennt ein
nicht mehr auffindbares Programm und nachtraeglich geschaetzte Klammern;
eine spezifische Korrektur fuer B58-B62 wurde in der begrenzten Suche nicht
gefunden. Das belegt keine konkrete Fehlerursache.
[Herausgeber-PDF](https://heim-theory.com/wp-content/uploads/2026/03/F_Erweiterte_Massenformel_nach_Heim-1989.pdf).

Die Messwertzeile laesst sich auf Krueger, Nistler und Weirauch (1999)
zurueckverfolgen: `137.03601144(498)` bedeutet absolute Standardunsicherheit
`4.98e-6`, relative Standardunsicherheit `3.64e-8`. Die IGW-Schreibweise
`+/-3.4e-8` ist nicht diese absolute Unsicherheit. Der Wortlaut des zitierten
populaeren Artikels von 2002 blieb ungeprueft.
[Publisherabstract, Metrologia](https://iopscience.iop.org/article/10.1088/0026-1394/36/2/9/meta).

Eine spaetere Behauptung ueber die exakte Zahlenpaarung einer verbesserten
Formel von 1992 bleibt unbelegt. Die gefundene Publikation Auerbach/von
Ludwiger (1992) druckt andere Werte. Das ist ein Provenienzproblem, keine
allgemeine Widerlegung dieser Arbeiten.
[1992-Publikation im Herausgeberarchiv](https://heim-theory.com/wp-content/uploads/2025/11/Heims-Theory-of-Elementary-Particle-Structures-Auerbach-und-Ludwiger.pdf).

Details, Suchgrenzen und weiterer 2003-Vergleich stehen im
[externen Quellenreview](../04_reconstruction/alpha_audit/reviews/EXTERNAL_SOURCE_REVIEW_2026-09-06.md).

## Umsetzung und naechste Forschungseinheit

Der neue Rechner ist getrennt vom ersten Audit. Die unabhaengige Review
bestaetigt die zentralen Rechnungen und fand einen zusaetzlichen
Decimal-Randfall: Zu lange Eingabewerte konnten bei unzureichender Praezision
auf 1 kollabieren. Die Umsetzung lehnt jetzt nicht exakt darstellbare
Quadrate/Subtraktionen ab; neue Regressionen pruefen Ablehnung und korrekte
Rechnung bei erhoehter Praezision. Bisherige Ergebniszahlen bleiben gleich.

```powershell
py -3.13 scripts/audit_alpha.py --check --verify-sources
py -3.13 scripts/audit_alpha_book.py --check
py -3.13 -m unittest discover -s tests -v
```

[Mathematikreview](../04_reconstruction/alpha_audit/reviews/BOOK_DIAGNOSTICS_MATH_REVIEW_2026-09-06.md),
[Ergebnisdaten](../05_analysis/alpha_book_diagnostics.json),
[Korrektur-/Erweiterungskandidaten](../04_reconstruction/alpha_audit/EXTENSION_CANDIDATES.md).

Ein konkreter Ansatzpunkt ist die **Begruendung der bislang gewaehlten
Mittelung und des Korrelationsfaktors**. Das ist zunaechst eine Forschungsfrage,
keine bereits verbesserte physikalische Theorie. Die naechste Einheit verfolgt
eta-Konfigurationen und diese Annahmen weiter; erst nach einer nachvollziehbaren
Verstaendnisbilanz folgt die gewuenschte Suche nach neueren Gegenbelegen und
Anschlussmoeglichkeiten. Siehe
[Verstaendnisplan](../00_admin/UNDERSTANDING_ROADMAP.md).
