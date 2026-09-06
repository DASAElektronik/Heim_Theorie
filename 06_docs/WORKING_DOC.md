# Arbeitsdokumentation

## Ausgangslage

Wir untersuchen Burkhard Heims Theorie nicht als Gesamtweltbild, sondern mit einem begrenzten Audit. Die erste belastbare Frage lautet, ob die Massenformel formal und numerisch reproduzierbar ist.

## Warum keine LHC-Rohdaten am Anfang?

Ein Teilchenbeschleuniger oder Detektor-Rohdaten sind erst relevant, wenn die Theorie eine neue experimentelle Signatur liefert. Fuer die erste Pruefung reichen PDG/NIST-Referenzwerte und Heims eigene Tabellen.

## Aktueller Stand 2026-09-06

Die vierte Etappe ist in `ENERGY_KINEMATICS_2026-09-06.md` erklaert.
44 Tests bestehen. Quellenanker fuer pc, Transversalmasse, deBroglie,
Compton-artige Laenge und photonische/Elektronen-Kreiswelle sind getrennt.
Neue ungefittete Diagnosen bestimmen keine Messwerte und validieren die Physik
nicht. Naechster Einstieg: A_-, invariante Form/Skalar und operative Energie-
bilanz, dann Kreisgeometrie/Wellenzuordnung. Etappen1-3 unten sind Verlauf.

Die dritte Etappe ist in `CHARGE_DERIVATION_2026-09-06.md` erklaert.
33 Tests bestehen; Buch-Indexbruecke geschlossen, vorlaeufige Alpha-Naeherung
reproduziert, Mittelungs-/Korrelationsannahmen getrennt und neuer lokaler
Energieordnungs-Konflikt dokumentiert. Naechster aktueller Einstieg sind
die Energie-/Masse-/Wellenlaengenbegriffe vor(105). Die folgenden Angaben
zu Etappe1/2 bleiben als Verlauf erhalten.

Der erste isolierte Alpha-Audit ist implementiert, mit 13 Tests geprueft und
unabhaengig reviewt. Ergebnis: `ALPHA_AUDIT_2026-09-06.md`.
Die zweite Etappe ist in `BOOK_TRACE_2026-09-06.md` dokumentiert: Buchstellen,
offene Annahmen, ex-post Y3-Diagnose und Quellenprovenienz. 23 Tests insgesamt,
Mathematikreview samt behobenem Praezisionsrandfall abgeschlossen.
Naechster Einstieg: eta-Konfigurationen, Ladungsmittelung und Korrelationsschluss;
Details und Rechenbefehle stehen in `../00_admin/RESUME.md`.

## Urspruenglicher Arbeitsschritt (historische Planung)

Die Dateien zur Massenformel aus dem Heim-Archiv identifizieren, lokal erfassen und eine erste Quellentabelle erstellen:

- `Massenformel_nach_B_Heim_1982.pdf`
- `Erweiterte_Massenformel_Nach_Heim_1989.pdf`
- `Heim_1989_Massenformel_0.4.xlsm`
- `massformula89.zip`
- relevante Abschnitte aus `Elementarstrukturen der Materie`

Danach: Werte extrahieren und gegen PDG/NIST stellen.
