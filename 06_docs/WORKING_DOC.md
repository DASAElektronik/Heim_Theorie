# Arbeitsdokumentation

## Ausgangslage

Wir untersuchen Burkhard Heims Theorie nicht als Gesamtweltbild, sondern mit einem begrenzten Audit. Die erste belastbare Frage lautet, ob die Massenformel formal und numerisch reproduzierbar ist.

## Warum keine LHC-Rohdaten am Anfang?

Ein Teilchenbeschleuniger oder Detektor-Rohdaten sind erst relevant, wenn die Theorie eine neue experimentelle Signatur liefert. Fuer die erste Pruefung reichen PDG/NIST-Referenzwerte und Heims eigene Tabellen.

## Aktueller Stand 2026-09-06

Etappe5: `AUTHOR_RATIONALE_2026-09-06.md` dokumentiert gefundene eigene
Motivationen Heims und die Grenzen der Ableitung. pc, Forminvarianz und
Skalarinvarianz getrennt; bekannte Alpha-Abweichung und duale Kreiswelle
bereits an EDM2 Druck276/277 belegt. Exakte eigene Diagnosen,56 Tests,
lokalen p21-Matrixdruckkonflikt separat dokumentiert. Naechster Einstieg:
ein explizites Wellen-/Randwertproblem hinter dem H-Grundzustandsansatz.
Neu gefundenes Manuskript1981 belegt den Motivations-/Formelkern bereits
in einer frueher datierten Fassung; erwogenes A=4C/freie Integrationskonstante
und Y bleiben als noch nicht normalisierte Versionsunterschiede kenntlich.
Die nachfolgenden Etappen sind Verlauf, kein jeweils aktueller Auftrag.

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
