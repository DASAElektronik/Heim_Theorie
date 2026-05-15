# Formelbibliothek

Ziel: Alle Formeln aus Heim-Quellen und Rekonstruktionen so katalogisieren, dass Herleitung, Provenienz, Status und spaetere Implementierung getrennt bleiben.

## Warum das sinnvoll ist

Die Massenformel ist kein einzelner Ausdruck, sondern ein Netzwerk aus:

- Symboldefinitionen und Quantenzahlen.
- Naturkonstanten und Hilfsfunktionen.
- Auswahlregeln.
- Hauptformeln fuer Massen, Lebensdauern, Feinstrukturkonstante und Neutrinos.
- Spaeteren Korrekturen, Branch-Wahlen und Implementierungsentscheidungen.

Eine Bibliothek verhindert, dass wir beim Rechnen unbemerkt Quellen mischen.

## Struktur

- `formula_catalog.csv`: maschinenlesbarer Index.
- `formulas/`: eine Markdown-Datei pro Formel oder Formelgruppe.
- `symbols/`: Symbol- und Einheitenregister.
- `derivations/`: Notizen zur Herleitung oder zum Beweisstatus.
- `reviews/`: Critic-/Audit-Kommentare zu einzelnen Formeln.
- `normalization/`: Entscheidungsqueue fuer die Uebersetzung von source-gepruefter Transkription in implementierbare Mathematik.
- `agent_workspace/`: Arbeitsbereich fuer parallele OCR-Agenten. Worker-Pakete und Critic-Reviews entstehen dort, bevor etwas in die kanonischen Dateien uebernommen wird.

## Statuswerte

- `raw_ocr`: aus OCR/Text extrahiert, noch nicht gegen Bild/PDF kontrolliert.
- `source_checked`: gegen Quelle geprueft.
- `normalized`: in eine eindeutige moderne Schreibweise gebracht.
- `implemented`: in Code umgesetzt.
- `validated_against_table`: reproduziert eine Heim-nahe Tabelle.
- `rejected_or_ambiguous`: nicht eindeutig oder nicht tragfaehig.

## Provenienzklassen

- `primary`: Heim-Original oder gedruckte Heim-Quelle.
- `near_primary`: Heim-nahe Abschrift, Vortrag, Verlag/IGW-Material.
- `secondary`: spaetere Erklaerung, Rekonstruktion oder Kommentar.
- `implementation`: Excel, C, Pascal, MathCad, Skript.
- `our_inference`: unsere eigene Normalisierung oder Interpretation.

## Agenten-Workflow

Der Agenten-Workflow ist bewusst zweistufig:

1. Worker-Agenten lesen Bilder/OCR und schreiben Vorschlaege nach `agent_workspace/worker_packets/`.
2. Ein Critic prueft diese Vorschlaege gegen Bildquelle und Guardrails in `agent_workspace/critic_reviews/`.
3. Erst danach editiert der Main-Integrator die kanonischen Dateien.

Worker-Ausgaben sind nie selbst `source_checked`.
