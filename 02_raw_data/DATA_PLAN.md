# Datenplan

## Welche Daten zaehlen hier als Rohdaten?

Im engeren Sinn gibt es zwei Klassen:

1. Heim-Rohmaterial: Originaltexte, Tabellen, Arbeitsdateien und Implementierungen zur Massenformel.
2. Vergleichsdaten: heutige Mess- und Referenzwerte aus PDG, NIST/CODATA und ggf. HEPData/CERN.

## Was wir in Phase 1 lokal brauchen

- Heim-Massenformel-Dokumente und Tabellen.
- PDG/NIST-Referenzwerte fuer eine kleine Teilchenauswahl.
- Ein Extraktionsprotokoll: jede Zahl mit Quelle, Einheit, Unsicherheit, Abrufdatum.

## Was wir in Phase 1 nicht brauchen

- Petabyte-grosse CERN-Open-Data-Datensaetze.
- Komplette HEPData-Spiegelung.
- Nicht zitierfaehige Forumstexte als Belege.

## Datenqualitaetsregeln

- Rohdateien bleiben unveraendert.
- Abgeleitete Tabellen kommen nach `05_analysis/` oder `07_outputs/`.
- Jede manuelle Extraktion bekommt eine Notiz in `03_notes/`.
- Makro-Dateien und ZIPs werden als untrusted behandelt.

