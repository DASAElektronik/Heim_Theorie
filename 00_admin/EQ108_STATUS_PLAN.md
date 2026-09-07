# Quellenvertrag: Gleichung (108) und diskrete Auswahl

2026-09-07, Etappe 37. Ausgang `15d1da3`, Branch `normalization-review`.

## Frage und Grenzen

Ist (108) im Buch als Gleichheit nach Ganzzahlauswahl beansprucht, oder
ist eine begründete diskrete Projektions-/Restregel angegeben? Drei Ebenen
trennen: Näherungsansatz der Koeffizienten/Externzone, Gleichheit innerhalb
dieses Ansatzes, Erhaltung durch den nachgeschalteten Auswahlalgorithmus.
Das gedruckte Gleichheitszeichen allein belegt keinen exakten Feldanspruch;
ein vorhandener Näherungsansatz allein legitimiert keinen beliebigen Rest.

Primärumfang H004 Druck 322-335 sowie 340-347; bei einem konkreten
Anschluss zusätzliche Einzelstellen begründet nachlesen. Root prüft
vollständige Originalseiten und dokumentiert den tatsächlichen Sichtumfang.
Insbesondere TRC-Messbarkeit, Kappe/Transfer, F_S-Einführung und mögliche
Rückkopplung zu W getrennt untersuchen. Ein Nichtfund gilt nur im Umfang.

Keine neue A-/Y-/Massenrechnung, kein nachträglich akzeptierendes Epsilon,
kein erfundener Projektionsalgorithmus und keine Wiederholung der gesamten
(79)-Fehlerrecherche. Alte Rechner, Verträge, Snapshots und Befunde bleiben
historisch erhalten. Kein pauschaler Anspruch, das gesamte Werk zu kennen
oder Heims Absichten beziehungsweise Lebensendwissen nachzuweisen.

## Arbeitsteilung und Sicherung

- Root: Plan, eigene Originallektüre, Quellenbilanz, Integration und Save.
- book_derivation: Einführung (108), upstream-Näherungen und W-Anschluss.
- alpha_versions: Auswahltext und unmittelbarer F_S-Folgeabschnitt.
- data_audit: logische Reichweite alter Restbefunde, keine neuen Fitwerte.

Agenten schreiben zunächst nur neue `EQ108_STATUS_*_REVIEW`-Dateien.
Bericht `06_docs/EQ108_STATUS_2026-09-07.md`, Quellenumfang in `03_notes/`,
Wiedereinstieg und Befundregister. Quellenbefund ist kein neuer unabhängiger
Fehler. Bestehende Regressionsprüfungen; neue Tests nur bei neuem Rechencode.

## Abschluss 2026-09-07

Plancheckpoint `f32f89a`. Root las H004 Druck322-335 und340-347 vollständig
visuell (22 Seiten); Quellenagent zusätzlich321. Ergebnisbericht und
`03_notes/EQ108_STATUS_SOURCES_2026-09-07.md` dokumentieren die Fundstellen.
Drei interne Reviews wurden gelesen und gegengeprüft. Mehrdeutiges kleines
f auf343 ist ausdrücklich keine Grundlage des F_S-Schlusses.

Ergebnis: formale Gleichheit im Näherungsmodell und vorhandene diskrete
Vorschrift, aber im geprüften Anschluss keine ausdrückliche finale
Restgarantie. Messbarkeit334/341 betrifft unterschiedliche Schritte;
F_S fällt unter323 bei fester Besetzungsvariation heraus. FIND-047 ist
ein offener Begründungsanschluss, kein neuer unabhängiger Fehler.

Read-only Regression am2026-09-07:342 bestehende Tests sowie12 alte
Snapshotchecks und5 weitere Zertifikats-/Diagnosechecks bestanden (je
Exit0). Keine neuen Tests, Eingaben, Rechner oder numerischen Snapshots.
H004-SHA256 erneut unverändert. Root prüft Registermetadaten und Staged
Diff vor dem abschließenden Save; finalen Commit über Git bestimmen,
keinen eigenen Commit-Hash in sich selbst eintragen.

Nächster Einzelauftrag: Massenformel98d/e bis112 und F_S-Rolle, zunächst
algebraisch und quellenkritisch ohne neue Massenkalibrierung.
