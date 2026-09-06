# Strukturverletzungen: Buchregel und historische Implementierung

2026-09-06, Etappe31. Ausgang `2ae50af`, Branch `normalization-review`.
Fortsetzung von FIND-040; kein neuer Zahlenvertrag und keine Massenrechnung.

- [x] H004323/328/329/340-342 samt gezieltem Kontext visuell lesen:
  Gibt es eine Pruefung von107/107a waehrend der Auswahl, Ruecksetzen,
  gekoppelte Neuwahl oder explizite G/delta-Umdefinition?
- [x] H015-FORTRAN-GSTRUC mit direkten Callern/Outputs statisch lesen.
  Nur lokale fotografierte Fassung, keine historische Programmausfuehrung.
- [x] H010-Pascal/C-GSTRUC und direkte Daten-/Kontrollfluesse statisch
  vergleichen; abweichende Fassungen nicht als Bucherratum behandeln.
- [x] Positiven Regelbeleg von begrenztem Nichtfund trennen; nur bei
  Bedarf eigene synthetische Kontrollflussdiagnosen, keine heimliche Reparatur.
- [x] Reviews, Quellenumfang, Bericht, Register und Wiedereinstieg sichern;
  alte Rechner/Inputs/Snapshots/49CSV erhalten und relevante Tests pruefen.

Root: eigene Originalseiten-/C/Pascal-Lektuere, Integration und Sicherung.
book_derivation: Buchregeln und G/delta-/Kollapsanschluss.
alpha_versions: fotografiertes FORTRAN-Listing und direkte Caller.
data_audit: unabhaengige C/Pascal-Kontrollflusspruefung.
Agenten schreiben nur ihre neuen STRUCTURE_HANDLING_*-Reviews.
Interne Gegenpruefung ist kein externes PeerReview.

Nicht autorisiert durch diesen Auftrag: Masse/F_S, Y9-/Zielwertfit,
Aenderung des fixierten Buchvertrags, neue Besetzung nach Trefferqualitaet,
allgemeine gekoppelte Ersatzregel oder werkweite Fehlbehauptung aus Nichtfund.
Eine lokale Quellenluecke ist ein erlaubtes Ergebnis. Erst nach dieser
Klaerung ueber eine eigene ausdruecklich getrennte Auswahldiagnose entscheiden.

## Abschluss

Plancheckpoint ec5e5a9; Buch-/Portreviews und acht eigene Tests in0118ae9.
Bericht `06_docs/STRUCTURE_HANDLING_2026-09-06.md`, Quellenumfang in03_notes.
Kein belegter Reparaturpfad fuer den FIND-040-Fall; positive Buchregeln
haben andere Ausloeser. H015-Sonderzweig liest IK4-Vorbestand; H010
integerisiert vorher neu, aber prueft keine aktuellen107-Gates. GLIMIT
enthaelt gewichtete Grenzalgebra, keinen individuellen Strukturfilter.
DreiReviews,36unabhaengigeChecks wiederholt,272Tests und12Rechenchecks.
Naechster Auftrag: eigene gekoppelte Existenzpruefung bei unveraenderten
Buchinputs vorbereiten; zuerst vollstaendige Grenzen/Genauigkeitsvertrag.
