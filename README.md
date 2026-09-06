# Heims Theorie

Arbeitsordner fuer eine nuechterne Rekonstruktion und Pruefung von Burkhard Heims Theorie.

## Ziel

Wir behandeln Heim nicht als Glaubensfrage, sondern als Audit:

1. Primaerquellen und spaetere Rekonstruktionen sauber trennen.
2. Behauptete Formeln und Rechenschritte reproduzierbar machen.
3. Heims Zahlen mit heutigen Referenzdaten vergleichen.
4. Freie Parameter, Annahmen und unklare Schritte dokumentieren.
5. Nur dann ueber experimentelle Signaturen sprechen, wenn eine formale Rekonstruktion traegt.

## Leitfrage

Kann aus Heims Original- bzw. nahen Quellen eine reproduzierbare, parameterarme Berechnung von Teilcheneigenschaften gewonnen werden, die heutigen Messdaten standhaelt?

## Struktur

- `00_admin/`: TODO, Fortschritt, Entscheidungen, offene Fragen.
- `01_sources/`: Quellenregister und spaeter lokale Kopien/Notizen zu Heim-Texten und Sekundaerliteratur.
- `02_raw_data/`: Referenzdaten aus PDG, NIST/CODATA, HEPData und CERN Open Data.
- `03_notes/`: Lese- und Exzerptnotizen.
- `04_reconstruction/`: Formale Rekonstruktion, Formelbibliothek, Gleichungen, Implementierungen.
- `05_analysis/`: Vergleiche, Fehlerrechnung, Parameterzaehlung.
- `06_docs/`: Unsere laufende Dokumentation und Zusammenfassungen.
- `07_outputs/`: Tabellen, Plots, Reports.
- `scripts/`: Hilfsskripte fuer Datenimport und Auswertung.

## Arbeitsprinzipien

- Primaerquelle vor Kommentar.
- Jede Zahl bekommt Herkunft, Einheit, Unsicherheit und Datum der Quelle.
- Jede Formel bekommt eine eindeutige Referenzstelle.
- Unklare Schritte werden markiert, nicht geglaettet.
- Keine Vermischung von Heim, Heim-Droescher, Ludwiger, Fan-Auslegung und moderner Rekonstruktion.

## Aktueller Arbeitsmodus

Stand 2026-09-06, Etappe 15: Die
[Verstaendnisbilanz](06_docs/UNDERSTANDING_BALANCE_2026-09-06.md) fuehrt den
bisher untersuchten Alpha-/Konfigurations-/Massenformel-Ausschnitt zusammen.
Sie trennt Quellenlesung, Rechnung, physikalische Herleitung und empirische
Pruefung. 26 Befundgruppen sind keine 26 Fehler und keine Gesamtwiderlegung.
Acht Rechenchecks und 98 Tests bestehen; die 49 Normalisierungen bleiben
unveraendert (47 resolved, 2 blocked).

Naechster enger Schritt: Eingabeblatt fuer die e--Komponente des
x2-Multipletts bei N=0 in H006 vorbereiten. Das gedruckte 0110 sind
Konfigurationsmerkmale, nicht die Besetzungszahlen n1..n4. Diese muessen
zuerst fassungstreu belegt werden. Ein gegebenes Tupel auszuwerten ist
von seiner Herleitung durch die Auswahlregel zu unterscheiden. Noch
keine freigegebene Elektronenmassenrechnung und keine moderne
Widerlegungsrecherche.

[Wiedereinstieg](00_admin/RESUME.md),
[Arbeitsfolge](00_admin/UNDERSTANDING_ROADMAP.md),
[N0-Eingabevoraussetzungen](04_reconstruction/alpha_audit/reviews/UNDERSTANDING_N0_READINESS_REVIEW_2026-09-06.md).

## Verlauf: erste neun Etappen

Die folgenden Test-/Befundzahlen und naechsten Schritte sind historisch;
fuer den aktuellen Stand gelten die Bilanz und der Wiedereinstieg oben.

Stand 2026-09-06: Der erste isolierte Alpha-Audit ist ausfuehrbar und unabhaengig
geprueft. [Ergebnisbericht](06_docs/ALPHA_AUDIT_2026-09-06.md),
[Ausfuehren](04_reconstruction/alpha_audit/README.md),
[Wiedereinstieg](00_admin/RESUME.md).

Die zweite Etappe verfolgt die Buchherleitung, trennt offene Annahmen und
prueft Y3-Rueckrechnung sowie Rechenpraezision; insgesamt 23 Tests bestehen.
[Buchbefunde](06_docs/BOOK_TRACE_2026-09-06.md),
[Verstaendnisplan](00_admin/UNDERSTANDING_ROADMAP.md).
Neuere Arbeiten auf Widerlegung zu pruefen ist als spaetere Phase vorgesehen:
zuerst die Herleitung und physikalische Bedeutung verstehen.

Die dritte Etappe reproduziert Heims vorlaeufige Alpha-Naeherung, klaert
die Buch-Indexreihenfolge und dokumentiert einen lokalen Energieordnungs-
widerspruch. [Schrittweise Erklaerung](06_docs/CHARGE_DERIVATION_2026-09-06.md).
33 Tests bestehen; Annahmen und Korrekturkandidaten sind gesondert markiert.

Die vierte Etappe verfolgt Energie, Masse und Wellenlaenge vor(105).
Sie trennt Heims pc von konventioneller Bewegungsenergie sowie h/(mc) von
h/p und zeigt den Einfluss dieser Annahmen auf die Alpha-Gleichung.
[Erklaerung und Quellen](06_docs/ENERGY_KINEMATICS_2026-09-06.md).
44 Tests bestehen; unabhaengige Reviews abgeschlossen. Keine fertig begruendete
Alternativtheorie: Kinematik, Kreisgeometrie und Energiezuordnung bleiben offen.

Die fuenfte Etappe findet Heims eigene Motivation: Lorentz-/Wellenargument
fuer pc sowie die bekannte Alpha-Abweichung und das duale Elektronenbild
fuer die Bindungskorrektur. [Warum-Bilanz](06_docs/AUTHOR_RATIONALE_2026-09-06.md)
trennt Motivation von fehlenden Herleitungsschritten. Exakte Boostdiagnosen
und ein neuer lokaler Matrixdruck-Befund sind unabhaengig geprueft;56 Tests.
Eine auf21.12.1981 datierte Manuskriptfassung liefert einen weiteren
direkten Beleg fuer die Motivation; ihre Unterschiede zur Buchfassung
und die Grenzen der Scan-Provenienz bleiben ausdruecklich dokumentiert.

Die sechste Etappe prueft moegliche Ergaenzungen der Kreiswelle:
[Wellen-Schliessung](06_docs/WAVE_CLOSURE_2026-09-06.md). Das eigene skalare
Ringproblem liefert ganzzahlige Moden, keine automatische Auswahl N1 oder
Heim-H-Eigenloesung. Phase-/Impulsidentifikation und Versionsunterschiede
der A_k bleiben getrennt.69 Tests und drei unabhaengige Reviews; keine
angefittete Verbesserung oder pauschale Widerlegung der Gesamttheorie.

Die siebte Etappe findet eine bedingte quelleninterne Geschwindigkeitsbruecke:
H-Stabilitaet ergibt w=c; fuer den strukturellen Fluss gilt w_f=w.
Die Objekt-/Phasenzuordnung bleibt offen. C=A1*A2 und Y3=1 sind eine
berechenbare Spezialisierung, nicht vollstaendig unabhaengig hergeleitet.
[Bilanz und Erklaerung](06_docs/CYCLIC_FLOW_AND_FINDINGS_2026-09-06.md),
[13 Befundgruppen](04_reconstruction/alpha_audit/FINDING_REGISTER.json).
Das Register enthaelt auch positive Befunde und eigene Diagnosen: keine
Fehlerzaehlung. Naechster Block: L*Delta=k und Auswahlregel (98a).

Die achte Etappe verbindet Konfigurationszahl, Ladung und Alpha in einer
[Zusammenhangskarte](04_reconstruction/alpha_audit/CONFIGURATION_DEPENDENCIES.md).
Die [Auswahlpruefung](06_docs/CONFIGURATION_SELECTION_2026-09-06.md) findet
einen lokalen Umformungskonflikt und u2=1.963489... statt des gedruckten
Bereichs 2..3; globale Maxima und beide Buch-Alpha-Paare bleiben jedoch erhalten.
Die 1989-eta22-Verwendung ist eine separate offene Versionsfrage. 86 Tests,
unabhaengige Reviews und sieben reproduzierte Snapshots; 16 Befundgruppen.
Naechster Querverweis: (79)/(79a) und F/G-Potentialzuordnung.

Die neunte Etappe verfolgt diese Rueckverweise:
[Exponentialkontext](06_docs/EXPONENTIAL_CONTEXT_2026-09-06.md).
Die Abklingrate ist im explizit skalaren Abbild unter a>lambda>0 reproduziert,
einschliesslich Amplitude und Naeherungsfehler. Positive Extremstellen
allein erzwingen diese Parameterwahl nicht; metronische Zusatzregeln bleiben
separat zu pruefen. Die F/G-Potentialzuordnung ist im untersuchten Kontext
weiter spekulativ. 98 Tests, acht Snapshots und 18 Befundgruppen; keine
Gesamtwiderlegung. Naechster Anschluss: Versionsgeltung von 1989 eta22.

## Implementierungsgrenze

Wir bauen zuerst eine Formelbibliothek unter `04_reconstruction/formula_library/`.
Jede Formel bekommt eine ID, Quelle, Status, Abhaengigkeiten, Outputs und Audit-Risiken.
Erst wenn eine Formel `source_checked` und `normalized` ist, soll sie implementiert werden.

Die beiden ALPHA-Bloecke besitzen dafuer explizite Normalisierungsentscheidungen
und den begrenzten Status `audit_implemented`; eine vollstaendige Massenrechnung
bleibt offen.

## Lizenz und Fremdmaterial

Dieses Repository nutzt getrennte Lizenzen:

- Code und Scripts: Apache-2.0, siehe `LICENSE-CODE`.
- Eigene Dokumentation, Rekonstruktions- und Audit-Notizen: CC BY 4.0, siehe `LICENSE-DOCS`.
- Fremdquellen, PDFs, ZIPs, XLSM-Dateien, Scans, OCR-Texte und daraus generierte Bildartefakte sind nicht von diesen Lizenzen umfasst.

Details stehen in `LICENSE` und `THIRD_PARTY_NOTICE.md`.
