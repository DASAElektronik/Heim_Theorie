# Quellenumfang: F_S-Provenienz

2026-10-18, Etappe 39. [Bericht](../06_docs/FS_PROVENANCE_2026-10-18.md).

## H004: bestehende lokale Primärquelle

Burkhard Heim, Elementarstrukturen der Materie 2; lokale Ausgabe mit
Gesamtherstellung 1996, Copyright 1984, Manuskripteinreichung 20.3.1981.
Datei `01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf`.
SHA256 am2026-10-18 erneut bestätigt:
`F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.

Vollständig visuell gelesene Seiten in dieser Etappe:

| Druckseite / physische PDF-Seite | Gegenstand |
|---|---|
| Impressum /4 | Drei unterschiedliche Datierungsangaben |
| Einführung 1-3 /12-14 | Y_k=1 für Tabellen, offener Deduktionsauftrag |
| 288-291 /294-297 | Pseudosingulett, Ladungen,101a/b, Teilchenzuordnung |
| 335-336 /341-342 | Heuristische A_im, Grundzustände,1974-Verweis im Resonanzkontext |
| 339 /345 | A41-65 aus 1974-Daten für Resonanzspektrum |
| 342-343 /348-349 | 17 Punkte, Ausschlüsse,111a/b und Y41-44 |
| 355 /361 | 1974-Anpassung versus1976-1982-Bestätigung laut Autor, Fußnote6 |
| Tabellenanhang 371-376 /376-381 | Rechenvermerk, Grundmassen, Resonanzen, weitere Ausgaben |

Das sind20 vollständige Seiten. Die ersten Seiten von Einführung,
Kapitel5 und Tabellenanhang haben keine sichtbare Seitenziffer; ihre
Druckposition wurde über Nachbarseiten bestimmt. Insbesondere gilt
im Tabellenanhang PDF=Druck+5, nicht der vorherige Abstand+6.

Arbeitsbilder unter `tmp/pdfs/fs_provenance/edm2-NNN.png`, ausgenommen
348-349: bestehende Bilder `tmp/pdfs/eq108_status/edm2-348.png` und 349.
Poppler-Renderings; OCR/Pypdf dienten zur Navigation. Die komplette
Originalsicht ersetzt die OCR-Lesung an den tragenden Stellen.

## M006: historische PDG-Referenz, neu importiert

Particle Data Group / V.Chaloupka et al., Review of Particle Properties,
Physics Letters 50B, Nr. 1, April 1974.

- [Offizielles Archiv-PDF](https://pdg.lbl.gov/rpp-archive/files/Physics-Letters-B-1974-v50.pdf)
- [Offizielle Publikationsliste,1974-Zeile](https://pdg.lbl.gov/2025/list_of_RPP_publications.html)
- Abruf2026-10-18;17,532,813 Bytes;215 physische PDF-Seiten.
- Lokale Datei: `01_sources/mainstream_reference/PDG_1974_Review_of_Particle_Properties.pdf`.
- SHA256: `DB7321F5EBD037B5FBD59B802341EA8F27585451C56F924EC77C2DEA84F7530F`.

Vollsicht PDF 2-3 (Titel/Einführung), PDF 20-22 (Stable Particle Table,
Druck 1-3), PDF 24 (Druck 5, Tabellenfußnoten), insgesamt6 Seiten.
Arbeitsbilder `tmp/pdfs/fs_provenance/pdg-NNN.png`.
Die Massen, Fehler und ausdrücklich angegebenen massenbezogenen
S-Faktoren wurden am Bild transkribiert. Tabellenkopf, Sammelbezeichnungen
und Fußnoten mitgelesen; keine Fehlerskalierung ein zweites Mal angewandt.
Fußnote f betrifft historische Spin-/Paritätszuordnungen von Xi/Omega,
nicht die hier transkribierte Massenspalte. Keine moderne Bewertung.

Web-PDF-Lesen scheiterte an der Größenbegrenzung; PowerShell-Download
an TLS-Authentifizierung. Der anschließende Python-urllib-Abruf mit
normaler Zertifikatsprüfung gelang. Keine Zertifikatsprüfung deaktiviert.
PDF lokal geöffnet und mit Poppler gerendert. Fremd-PDF bleibt gemäß
bestehender Gitignore-Regel lokal; Quelle und Hash werden dokumentiert.

## Reichweite und eigene Zuschreibung

Heim zuzuschreiben:101a/b-Zuordnung,17-Punkte-Angabe, heuristische
F_S-Form und Y=1-Annahme. PDG zuzuschreiben: historische Zusammenstellung
der Messwerte; die experimentellen Einzelarbeiten sind damit nicht
vollständig nachverfolgt. Unser Beitrag: Verbindung dieser Quellen,
Nachzählung, Transkription und Trennung von Datenrolle und Nachweisgrenze.

Die 1974-Verweise auf 336/339/355 sind keine ausdrücklich zeilenweise
F_S-Eingabeliste. Die neue Tabelle ist ein historischer Referenzkandidat,
kein freigegebener Ersatz für alte Inputdateien. Nicht geprüft:
Originalarbeitsnotizen zu F_S, alle Buchauflagen, vollständige PDG-Listings,
spätere1976-1982-Daten, Konstantenkorrektur nach 115 oder neue Massenausgabe.
Die Quellenprüfung erfolgte durch einen Agenten. Kein neues unabhängiges
Review behauptet; bestehende Reviews wurden nur als Ausgangspunkt benutzt.
