# Zweite Etappe: Buchherleitung und Quellenvarianten

Beginn: 2026-09-06. Ausgangspunkt: Alpha-Audit, Commit `a2a9e84`.
Der Nutzer bestaetigt weitere Projektarbeit und meldet 24.218 Credits.

## Abschlusskriterien

- [ ] eta-, A_k-, vartheta- und Y3-Abhaengigkeiten von Buch (105) soweit in
  den relevanten Quellenstellen nachvollziehbar dokumentieren.
- [ ] Quellennahe Definition, Annahme und empirische Anpassung unterscheiden.
- [ ] Y3-Rueckrechnung als ausdruecklich nachtraegliche Diagnose berechnen;
  niemals als parameterfreie Vorhersage ausgeben.
- [ ] Numerische Ausloeschung als begrenzte Fehlerhypothese pruefen.
- [ ] 1989-Quellenvarianten/Errata und Nistler-Weirauch-2002-Zitat recherchieren;
  gefundene Belege und erfolglose, begrenzte Suchen getrennt festhalten.
- [ ] Ergebnisse testen, unabhaengig gegenlesen, dokumentieren und sichern.

## Arbeitsteilung

- Quellenagent `book_derivation`: GPT-5.6 Terra high; Buchstellen und Edition.
- Quellenagent `alpha_versions`: GPT-5.6 Sol high; externe Fassungen und Zitate.
- Hauptagent: mathematische Diagnose, Code, Integration und Git-Checkpoints.

Agenten schreiben ausschliesslich getrennte Review-Dateien. Ein zusaetzlicher
Mathematik-Agentenaufruf traf eine Thread-Grenze; die laufenden Quellenauftraege
und lokale Arbeit laufen weiter. Neue mathematische Ergebnisse werden nach
Moeglichkeit von einem verfuegbaren Reviewer geprueft, ohne alte Reviews als
Freigabe fuer neue Berechnungen auszugeben.

## Grenzen

Keine Aenderung der source-literal Alpha-Varianten nach besserem Zahlenfit.
Kein allgemeines Y3-Modell ohne Quellenbasis, keine neue Massenimplementierung.
Eine historische Fehlerursache bleibt offen, wenn Belege fehlen. Der erste
Alpha-Audit bleibt als getrennt reproduzierbarer Befund erhalten.

## Checkpoints

Plan/Wiedereinstieg; danach Diagnosecode und Quellenbefunde; schliesslich
gepruefter Bericht, aktualisierte Provenienz und Fortsetzungsauftrag.
