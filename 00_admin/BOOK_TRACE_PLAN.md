# Zweite Etappe: Buchherleitung und Quellenvarianten

Beginn: 2026-09-06. Ausgangspunkt: Alpha-Audit, Commit `a2a9e84`.
Der Nutzer bestaetigt weitere Projektarbeit und meldet 24.218 Credits.

Erweiterung des Auftrags: Der Nutzer erlaubt ausdruecklich, uebersehene Fehler
oder Zusammenhaenge zu suchen und daraus eigene Verbesserungen der Theorie
zu entwickeln. Originalquellen bleiben erhalten; neue Modelle erhalten eine
eigene Version und werden als unsere Rekonstruktion/Erweiterung ausgewiesen.

Weitere Nutzerpraezisierung: Neuere Arbeiten koennen die Theorie widerlegen
oder Ansatzpunkte liefern. Diese externe physikalische Bewertung soll aber
erst nach der Verstaendnis-/Rekonstruktionsphase erfolgen. Aktuelle Quellen-
und Editionsrecherche dient nur der zuverlaessigen Rekonstruktion. Bereits
erfasste moderne Referenzen bleiben Vergleiche, kein Gesamturteil.

Verstaendnis wird nicht einfach behauptet: Fuer den jeweils untersuchten
Theorieteil muessen Begriffe, Annahmen, Herleitung, Parameter, Zweigwahl und
messbare Bedeutung nachvollziehbar sein; verbleibende Luecken werden sichtbar
gelassen. Vor der breiten Widerlegungsrecherche folgt eine gemeinsame Bilanz.

## Abschlusskriterien

- [x] eta-, A_k-, vartheta- und Y3-Abhaengigkeiten von Buch (105) soweit in
  den relevanten Quellenstellen nachvollziehbar dokumentieren.
- [x] Quellennahe Definition, Annahme und empirische Anpassung unterscheiden.
- [x] Y3-Rueckrechnung als ausdruecklich nachtraegliche Diagnose berechnen;
  niemals als parameterfreie Vorhersage ausgeben.
- [x] Numerische Ausloeschung als begrenzte Fehlerhypothese pruefen.
- [x] 1989-Quellenvarianten/Errata und Nistler-Weirauch-2002-Zitat recherchieren;
  gefundene Belege und erfolglose, begrenzte Suchen getrennt festhalten.
- [x] Ergebnisse testen, unabhaengig gegenlesen, dokumentieren und sichern.
- [x] Aus Befunden konkrete Korrektur-/Erweiterungskandidaten ableiten und
  ihren pruefbaren Mehrwert sowie zusaetzliche Freiheitsgrade benennen.

## Arbeitsteilung

- Quellenagent `book_derivation`: GPT-5.6 Terra high; Buchstellen und Edition.
- Quellenagent `alpha_versions`: GPT-5.6 Sol high; externe Fassungen und Zitate.
- Hauptagent: mathematische Diagnose, Code, Integration und Git-Checkpoints.

Agenten schreiben ausschliesslich getrennte Review-Dateien. Ein zusaetzlicher
Mathematik-Agentenaufruf traf eine Thread-Grenze; die laufenden Quellenauftraege
und lokale Arbeit laufen weiter. Neue mathematische Ergebnisse werden nach
Moeglichkeit von einem verfuegbaren Reviewer geprueft, ohne alte Reviews als
Freigabe fuer neue Berechnungen auszugeben.

Abschluss: derselbe Buchreviewer pruefte die neue Diagnose unabhaengig,
fand einen generischen Praezisionsrandfall und bestaetigte dessen Korrektur.
23 Tests bestehen. Begrenzte Etappe abgeschlossen; fehlende eta-Indexbruecke
und physikalische Schliessung sind Ergebnisse, keine erledigten Herleitungen.
Bericht: `06_docs/BOOK_TRACE_2026-09-06.md`.

## Grenzen

Keine Aenderung der source-literal Alpha-Varianten nach besserem Zahlenfit.
Kein allgemeines Y3-Modell ohne Quellenbasis, keine neue Massenimplementierung.
Eine historische Fehlerursache bleibt offen, wenn Belege fehlen. Der erste
Alpha-Audit bleibt als getrennt reproduzierbarer Befund erhalten.

## Eigene Verbesserungen

Zulaessige Ergebnisse sind auch eine korrigierte Rechnung oder eine neue
Modellvariante. Unterscheiden: Druckkorrektur, Rechenkorrektur, geaenderte
physikalische Annahme. Jede Variante dokumentiert Motiv, Gleichung, Parameter,
Validierungsdaten und einen Test, den die Anpassung nicht bereits erzwungen hat.
Ein nachtraeglicher Y3-Wert ist zunaechst eine Diagnose oder Kalibrierung;
zwei mit zwei Parametern passende Werte allein sind noch kein Erkenntnisgewinn.
Negative Ergebnisse werden ebenso versioniert wie aussichtsreiche Varianten.

## Checkpoints

Plan/Wiedereinstieg; danach Diagnosecode und Quellenbefunde; schliesslich
gepruefter Bericht, aktualisierte Provenienz und Fortsetzungsauftrag.
