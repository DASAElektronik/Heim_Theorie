# TODO

## Aktueller Einstieg (2026-09-06)

- [x] Isolierten Alpha-Audit 1982/1989 implementieren, testen und gegenlesen.
- [x] Gedruckte Zweig-/Kehrwertangaben unter Rundung pruefen; Bericht erstellt.
- [x] Buch (105) eng gegenpruefen; Y3=1-Spezialisierung dokumentieren.
- [ ] Buchherleitung von eta/A_k/Y3 und historische Ursachenfrage verfolgen.
- [ ] 1989 B58-B62 mit weiteren belegbaren Fassungen und Errata abgleichen.
- [ ] Danach fehlende Massenabhaengigkeiten sowie B50 und Gamma/Q_N bearbeiten.

Massgeblicher Wiedereinstieg: `RESUME.md`. Die folgenden Phasenlisten sind
die urspruengliche Projektplanung und nicht der aktuelle Detailstatus.

## Phase 1: Quellenbasis

- [ ] Vollstaendige Quellenliste aus `01_sources/source_register.md` pruefen.
- [ ] Entscheiden, welche PDFs lokal gesichert werden sollen.
- [ ] Bibliographische Metadaten fuer Heim-Hauptwerke erfassen.
- [ ] Quellen nach Typ markieren: Primaerquelle, Uebersetzung, Sekundaerquelle, spaetere Erweiterung, Kritik.
- [ ] Lizenz-/Copyright-Status fuer lokale Kopien dokumentieren.

## Phase 2: Zielmodell

- [ ] Eingrenzen: zuerst Massenformel, nicht Gesamttheorie.
- [ ] Tabelle der zu vergleichenden Teilchen definieren.
- [ ] Heims behauptete Vorhersagewerte erfassen.
- [ ] Heutige PDG/NIST-Werte mit Unsicherheiten erfassen.
- [ ] Freie Parameter der Rekonstruktion zaehlen.

## Phase 3: Rekonstruktion

- [ ] Formelbibliothek in `04_reconstruction/formula_library/` gegen PDF-Bilder pruefen.
- [ ] Fuer jede Formel aus `formula_catalog.csv` mindestens eine Einzelformel-Datei anlegen.
- [ ] Alle Symbole aus `symbols/symbol_register.csv` disambiguieren.
- [ ] `04_reconstruction/PARAMETER_BOOK.md` mit konkreten Quellenstellen fuellen.
- [ ] Erste Model Card fuer `model_1982_from_text` anlegen.
- [ ] Notation aus Heim-Quellen in moderne Symbole uebersetzen.
- [ ] Formelketten fuer Elektron, Myon, Tau, Proton, Neutron identifizieren.
- [ ] Minimalen Rechenweg als Pseudocode formulieren.
- [ ] Erste Implementierung in `04_reconstruction/mass_formula/` anlegen.
- [ ] Rechenergebnisse gegen Originaltabellen vergleichen.

## Phase 4: Bewertung

- [ ] Abweichungen zu heutigen Referenzdaten berechnen.
- [ ] Pruefen, welche Werte echte Vorhersagen waren und welche schon bekannt waren.
- [ ] Sensitivitaet gegen Parameterwahl untersuchen.
- [ ] Konflikte mit Standardmodell, QFT, Lorentz-Invarianz und bekannten Symmetrien sammeln.
- [ ] Zwischenbericht in `06_docs/` schreiben.
