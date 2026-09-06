# Dritte Etappe: Ladungsmittelung und Konfigurationen verstehen

Beginn: 2026-09-06; Ausgangscommit `c100fbe`.
Nutzerauftrag: mit Heim weiterarbeiten. Ziel ist Lernen und oeffentlich
nachvollziehbare Erkenntnis, nicht ein vorgegebenes positives Resultat.
Eigene Verbesserungen sind erlaubt, Quellen und neue Annahmen bleiben getrennt.

## Begrenzte Ergebnisse dieser Etappe

- [x] Einfach/zweiindiziertes eta und k-Konfigurationen an expliziten
  Quellenstellen rueckverfolgen; Indexluecken nicht durch Fit schliessen.
- [x] BandI(27b)-(29a) in heutiger Notation schrittweise rekonstruieren,
  Ladungszeichen/Einheiten und Mittelungsannahmen offenlegen.
- [x] BandII-Korrelationsschluss vor(105) als Definition, Annahme oder
  algebraische Folge klassifizieren.
- [x] Mittels einer klar als unsere Diagnose markierten Gewichtungsfamilie
  zeigen, welche Aussage die Wahl des gleichen Mittelwerts hinzufuegt.
- [x] Begrenzte Diagnostik reproduzierbar testen und unabhaengig reviewen.
- [x] Verstaendliche Erklaerung, Annahmenkarte und Wiedereinstieg sichern.

Abschluss: 33 Tests; drei Quellen-/Mathematikauftraege und zusaetzliche
Energieordnungs-Gegenpruefung abgeschlossen. Buch-Indexdefinition gefunden,
Mittelungsrechnung reproduziert, Energieordnungs-Konflikt dokumentiert.
Die physikalische Begruendung der Annahmen ist damit nicht abgeschlossen.

## Arbeitsteilung

- `book_derivation`: eta-Konfigurationen, eigene Review-Datei.
- `alpha_versions`: Korrelationskette, eigene Review-Datei.
- Hauptagent: Ladungsmittelung, Mathematik, Erklaerung und Integration.

Die Quellenagenten arbeiten ausschliesslich in ihren benannten Review-Dateien.
Keine Fremdprogramme/Makros, keine Aenderung historischer Quellwerte.
Kein Wechsel zur breiten modernen Widerlegungs- oder Hardwareentwicklung.

## Annahmen fuer die eigene Diagnose

Eine variable Gewichtung lambda ersetzt probeweise die gleiche Mittelung
der zwei in der Quelle bereits ausgewaehlten Potentiale. Das ist kein aus
Heim hergeleiteter freier Parameter und kein verbessertes physikalisches
Modell. Es dient dazu, logische Unterbestimmtheit sichtbar zu machen.
Keine Anpassung von lambda an einen Messwert, kein Vermischen mit Y3.

## Sicherung

Plan-Checkpoint, danach Quellen-/Rechencheckpoint, schliesslich gepruefter
Bericht und Fortsetzungsauftrag. Eigene Quellen-/Annahmenentscheidungen
werden dokumentiert, auch wenn keine physikalische Schliessung gelingt.
