# Vorvertrag: Sättigung im festen z3-Zweig

2026-09-07, Etappe 36. Ausgang `efb812d`, Branch `normalization-review`.
Vor neuer Auswertung gesichert; alte Eingaben, Rechner und Snapshots bleiben.

## Feste Fragestellung

Die vier Zellen aus `decay_sensitivity_inputs.json` bleiben unverändert.
Beide A=1/3-Zellen sind Kontrollen ohne Sättigung; beide A=1/5-Zellen
werden mit der Sättigungsvorschrift von H004 Druck 341 fortgesetzt.
Der 1/5-Fall bleibt unsere Gegenprobe: Insbesondere muss die reelle
Umkehrung -ln(W4)/A zum veränderten Exponentialterm passen. Die im Buch
bereits spezialisierte 1/3-Umkehrung ist nicht unverändert einzusetzen.

- Keine Änderung von a_j, w, Y, g/W, Vorbesetzungen oder A-Auswahl.
- cap=a3*N3; bei raw>cap: t=TRC(cap), N4=t-1 nur falls t>cap,
  sonst N4=t. Kein zusätzlicher Rücksprung oder Transfer.
- TRC-Ausnahme ohne erfundene Messbarkeitsschwelle behandeln: eigene
  Fallanalyse Abschneiden versus mögliche Promotion zum nächsten Integer.
  Keine Gleichsetzung der Gesamt-TRC mit floor und kein pauschales ceil-1.
- Vollständiges Tupel, n_j=N_j-Q_j, direkte 107/107a-Gates und separate
  gewichtete 107b-Größe berichten. Untergrenze n_j>=-Q_j beachten;
  weder negative n_j noch 0<gewichtete Größe<1 automatisch verbieten.
- R=T_A-W_A nach Auswahl direkt und über Externrest erneut auswerten.
  Exaktheit, gewöhnliche Auswahl und physikalische Näherung bleiben getrennt.
- Keine neue Masse, kein empirisches Fehlerbudget oder Parameterfit.
  Der alte vollständige Existenzsatz wird nicht als neuer Fehler gezählt.

## Durchführung

Root liest H004 Druck 321-323,328-330,340-342 vollständig visuell und
erstellt einen neuen, hashgebundenen Diagnoseaufsatz samt Tests.
book_derivation prüft Originalregel und Definitionsgrenzen;
alpha_versions prüft die TRC-/Domänenalgebra;
data_audit rechnet nach Sicherung des Vertrags unabhängig nach.
Agenten schreiben jeweils nur neue SATURATION_*_REVIEW-Dateien.

Neue Ergebnisse: `06_docs/SATURATION_2026-09-07.md` und eigener
Quellenumfang; Registereintrag als Anschlussdiagnose, kein neuer
unabhängiger Theoriefehler. Danach Regression und Git-Sicherung.
