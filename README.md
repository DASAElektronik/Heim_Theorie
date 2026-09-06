# Heims Theorie

Arbeitsordner fuer eine nuechterne Rekonstruktion und Pruefung von Burkhard Heims Theorie.

## Ziel

Wir behandeln Heim nicht als Glaubensfrage, sondern als Audit:

1. Primaerquellen und spaetere Rekonstruktionen sauber trennen.
2. Behauptete Formeln und Rechenschritte reproduzierbar machen.
3. Heims Zahlen mit heutigen Referenzdaten vergleichen.
4. Freie Parameter, Annahmen und unklare Schritte dokumentieren.
5. Nur dann ueber experimentelle Signaturen sprechen, wenn eine formale Rekonstruktion traegt.

## Leitfrage

Kann aus Heims Original- bzw. nahen Quellen eine reproduzierbare, parameterarme Berechnung von Teilcheneigenschaften gewonnen werden, die heutigen Messdaten standhaelt?

## Struktur

- `00_admin/`: TODO, Fortschritt, Entscheidungen, offene Fragen.
- `01_sources/`: Quellenregister und spaeter lokale Kopien/Notizen zu Heim-Texten und Sekundaerliteratur.
- `02_raw_data/`: Referenzdaten aus PDG, NIST/CODATA, HEPData und CERN Open Data.
- `03_notes/`: Lese- und Exzerptnotizen.
- `04_reconstruction/`: Formale Rekonstruktion, Formelbibliothek, Gleichungen, Implementierungen.
- `05_analysis/`: Vergleiche, Fehlerrechnung, Parameterzaehlung.
- `06_docs/`: Unsere laufende Dokumentation und Zusammenfassungen.
- `07_outputs/`: Tabellen, Plots, Reports.
- `scripts/`: Hilfsskripte fuer Datenimport und Auswertung.

## Arbeitsprinzipien

- Primaerquelle vor Kommentar.
- Jede Zahl bekommt Herkunft, Einheit, Unsicherheit und Datum der Quelle.
- Jede Formel bekommt eine eindeutige Referenzstelle.
- Unklare Schritte werden markiert, nicht geglaettet.
- Keine Vermischung von Heim, Heim-Droescher, Ludwiger, Fan-Auslegung und moderner Rekonstruktion.

## Aktueller Arbeitsmodus

Stand 2026-09-06: Der erste isolierte Alpha-Audit ist ausfuehrbar und unabhaengig
geprueft. [Ergebnisbericht](06_docs/ALPHA_AUDIT_2026-09-06.md),
[Ausfuehren](04_reconstruction/alpha_audit/README.md),
[Wiedereinstieg](00_admin/RESUME.md).

Die zweite Etappe verfolgt die Buchherleitung, trennt offene Annahmen und
prueft Y3-Rueckrechnung sowie Rechenpraezision; insgesamt 23 Tests bestehen.
[Buchbefunde](06_docs/BOOK_TRACE_2026-09-06.md),
[Verstaendnisplan](00_admin/UNDERSTANDING_ROADMAP.md).
Neuere Arbeiten auf Widerlegung zu pruefen ist als spaetere Phase vorgesehen:
zuerst die Herleitung und physikalische Bedeutung verstehen.

Die dritte Etappe reproduziert Heims vorlaeufige Alpha-Naeherung, klaert
die Buch-Indexreihenfolge und dokumentiert einen lokalen Energieordnungs-
widerspruch. [Schrittweise Erklaerung](06_docs/CHARGE_DERIVATION_2026-09-06.md).
33 Tests bestehen; Annahmen und Korrekturkandidaten sind gesondert markiert.

Wir bauen zuerst eine Formelbibliothek unter `04_reconstruction/formula_library/`.
Jede Formel bekommt eine ID, Quelle, Status, Abhaengigkeiten, Outputs und Audit-Risiken.
Erst wenn eine Formel `source_checked` und `normalized` ist, soll sie implementiert werden.

Die beiden ALPHA-Bloecke besitzen dafuer explizite Normalisierungsentscheidungen
und den begrenzten Status `audit_implemented`; eine vollstaendige Massenrechnung
bleibt offen.

## Lizenz und Fremdmaterial

Dieses Repository nutzt getrennte Lizenzen:

- Code und Scripts: Apache-2.0, siehe `LICENSE-CODE`.
- Eigene Dokumentation, Rekonstruktions- und Audit-Notizen: CC BY 4.0, siehe `LICENSE-DOCS`.
- Fremdquellen, PDFs, ZIPs, XLSM-Dateien, Scans, OCR-Texte und daraus generierte Bildartefakte sind nicht von diesen Lizenzen umfasst.

Details stehen in `LICENSE` und `THIRD_PARTY_NOTICE.md`.
