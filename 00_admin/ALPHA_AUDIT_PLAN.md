# Arbeitsplan: Alpha-Audit 1982 / 1989

Beginn: 2026-09-06. Auftrag: Plan ausarbeiten, das Alpha-Problem bearbeiten,
Agenten nach Bedarf einsetzen und wiederholt sichern.

## Ziel und Abschlusskriterien

Die in den lokalen IGW-Wiedergaben erfassten Alpha-Gleichungen und Zahlen
unabhaengig reproduzieren. Jede Variante, Konstantenwahl und Quellenstelle
bleibt sichtbar. Ergebnis ist ein ausfuehrbarer Konsistenz-Audit, keine
Validierung der gesamten Heim-Theorie und keine vollstaendige Massenrechnung.

- [x] Quellenstellen, Dateihashes, gedruckte Zahlen und Indexkonventionen erfasst.
- [x] Algebraische Zweigbedingung hergeleitet und numerisch stabil ausgewertet.
- [x] 1982-Originalablesung und bereits dokumentierte Indexvariante getrennt.
- [x] 1989-B58/B61 ausgewertet, soweit die eta-Zuordnung belegt ist;
      andernfalls Varianten explizit als bedingt ausgewiesen.
- [x] Gedruckte Zweigpaare und Kehrwerte mit Rundungsintervallen geprueft.
- [x] NIST/CODATA-2022-Vergleich separat und ohne Rueckwirkung auf Formeln.
- [x] Sinnvolle automatisierte Tests und unabhaengige mathematische Review.
- [x] Ergebnisbericht, offene Fragen und Wiedereinstieg dokumentiert.
- [x] Arbeitscheckpoints committed und auf den bestehenden Branch gepusht.

Abgeschlossen: ausfuehrbarer Audit, 13 Tests, Quellen- und Mathematikreview.
Der Bericht `06_docs/ALPHA_AUDIT_2026-09-06.md` nennt die verbleibenden
historischen Ursachenfragen. Die Theorie als Ganzes ist nicht abschliessend
beurteilt. Ein zusaetzlicher enger Buchquellencheck bestaetigte das gleiche
gedruckte Zweigpaar und dokumentierte den dort verwendeten Faktor Y3.

## Arbeitspakete und Rollen

| Paket | Verantwortung | Ergebnis |
|---|---|---|
| A: Quellen und Notation | GPT-5.6 Terra, high; Hauptagent liest Gegenstellen | Quellenreview mit Seitenangaben |
| B: Rechner und Referenzdaten | Hauptagent | Python-Standardbibliothek, versionierte Eingaben und Ergebnisse |
| C: Algebra und Gegenpruefung | GPT-6 Astra, high | Unabhaengige Herleitung, Rundungstest, Implementierungsreview |
| D: Integration und Sicherung | Hauptagent | Bericht, Statuspflege, Git-Checkpoints |

Agenten erhalten kleine, frische Auftragskontexte und getrennte Ausgabedateien.
Kein weiterer Agent ohne eine konkrete unabhaengige Teilaufgabe.
Nur der Hauptagent aendert kanonische Formeln und Statusregister.

## Reihenfolge und Checkpoints

1. Plan und Wiedereinstieg sichern.
2. Quellenprofil, eng begrenzte Normalisierungsentscheidung und lauffaehigen
   Alpha-Rechner sichern; noch nicht reviewte Arbeit klar kennzeichnen.
3. Review, Tests, Bericht und finalen Wiedereinstieg sichern.

Nach jedem abgeschlossenen Paket oder wesentlichen Befund Dateien sofort
speichern. Git-Commits verwenden explizite Pfade; Fremdquellen und generierte
PDF-Seiten bleiben gemaess .gitignore lokal. Push auf den vorhandenen Branch
`normalization-review` von `origin`, keine History-Umschreibung.

## Methodische Grenzen

- Quelltext nicht anhand von Zielwerten reparieren.
- Gedruckte Dezimalstellen liefern nur bedingte Rundungsintervalle, keine
  experimentellen oder theoretischen Standardunsicherheiten.
- Hohe Rechenpraezision ist keine Aussage ueber physikalische Genauigkeit.
- `source_checked`, Normalisierung, Implementierung und Validierung trennen.
- Ein Widerspruch zwischen Gleichung und Tabelle lokalisiert ein Problem
  dieser Fassung; seine historische Ursache benoetigt weitere Quellenarbeit.
- B50, Gamma/Q_N, C-Output-Provenienz und Residualtabellenbereinigung sind
  nachfolgende Arbeitspakete, nicht Teil dieses ersten Alpha-Abschlusses.

## Unterbrechungen

Kontingent und Sitzungsfortsetzung sind nicht garantiert. Massgeblich fuer
den Wiedereinstieg ist `00_admin/RESUME.md`, nicht der Chatverlauf. Dort stehen
der letzte gepruefte Stand, offene Arbeit, Befehle und Sicherungsstatus.
