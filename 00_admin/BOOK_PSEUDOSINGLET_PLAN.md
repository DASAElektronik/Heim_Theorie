# Buchinternes N0-Pseudosingulett: Eingaben vor Auswahl

2026-09-06, Etappe30. Ausgang `00180ec`, Branch `normalization-review`.
Fortsetzung des in Etappe29 festgelegten Einzelauftrags.

- [x] H004-Vertrag fuer k=Q=kappa=q=1 und Resonanz N=0 aus der Buchfassung
  festlegen: Q_j, g, eta/eta_qk, alpha_i, A16, Y9 und f mit Quellenstellen.
- [x] Alpha-/xi-/Y-Konventionen und Abhaengigkeiten vor einer numerischen
  Auswahl festlegen; explizite Formeln von gedruckten Naeherungszahlen trennen.
  Keine H006/H010-Programmkonstanten als Buchwerte importieren.
- [x] Direkte Buch-Strukturbedingungen aus G_j und delta_jG_j rekonstruieren;
  nicht pauschal H006-XIII/XXXII uebernehmen.
- [x] Nur bei geschlossenem Vertrag Auswahlzweig, Besetzungen, Rest und
  Strukturgates berechnen; sonst die konkrete Eingabeluecke dokumentieren.
- [x] Unabhaengige Pruefung, proportionale Tests und alte Regressionschecks;
  Bericht, Quellenumfang, Befundregister und Wiedereinstieg sichern/pushen.

Y9=1 nur ausgewiesene Tabellenannahme, kein Fitauftrag. Weitere Y-Faktoren
nur nach expliziter Quellenpruefung. Keine Zielmasse, F_S-Rechnung,
Neuner-Epsilon-Erfindung oder still geaenderte alte Profile/Snapshots.
Die49CSV-Normalisierungen bleiben erhalten. SOURCE_ATTRIBUTION.md gilt.

Root: A16-/W-Anschluss, Gesamtvertrag, eigene Sicht und Integration.
book_derivation: Q_j/g/alpha1/alpha2 und Buch-Kanal-/N0-Zuordnung.
alpha_versions: ausschliesslich buchinterne Alpha-/eta-/xi-/Y-Eingaben.
data_audit: direkte G_j-/delta_jG_j-Strukturbedingungen.
Jeder Agent schreibt nur seine neue BOOK_PSEUDOSINGLET*-Reviewdatei.
Interne Reviews sind keine externen PeerReviews.

Die numerische Profilfestlegung wird hier VOR deren neuer Auswertung
nachgetragen und separat versioniert. Eine Quellenluecke ist ein erlaubter
begrenzter Abschluss, keine pauschale Nichtberechenbarkeit der Theorie.

Profilfestlegung vor Rechnung: `NORM-BOOK-PSEUDOSINGLET.md` und
`book_pseudosinglet_inputs.json` im Alpha-Audit. Primaer105 mit Y3=1,
q,k-Indizes (A2:1,2), mathematische pi/e, goldenes xi, Y9=1; getrennte
Druckwert-Sensitivitaet alpha=0.007297354572. Keine weitere Achse/Fitwahl.
Direkte ungewichtete107-Gates und spaetere107b-sigma-Bandbreite getrennt.
Zum Zeitpunkt dieser Profilfestlegung war noch kein Auswahlergebnis berechnet.

## Abschluss

Plancheckpoint2d53bfc, Eingabecheckpoint05a0bab vor Rechnung,
Rechner-/Test-/Snapshotcheckpoint4213148. Bericht
`06_docs/BOOK_PSEUDOSINGLET_2026-09-06.md`, Quellenumfang in03_notes.
Beide Profile: N_(j)=(14,9,13,7); direkte107/107a-Bandbreite beta3=-10.
107b-Gewichtungsanschluss separat, kein stiller Reparaturalgorithmus.
17neueTests,264gesamt,12Rechenchecks; dreiAgenten/vierReviews,
unabhaengige Struktur- und Numerikbloecke von Root erneut ausgefuehrt.
FIND-040 ist ein bedingter Befund, keine Gesamtwiderlegung oder Masse.
Naechster Einzelauftrag: quellenbelegte Behandlung von Strukturverletzungen
in Buchauswahl/historischer GSTRUC-Routine, Fassungen getrennt halten.
