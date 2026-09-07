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
