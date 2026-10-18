# Quellenumfang: früher Konstantensatz

2026-10-18, Etappe41, Ausgang b2c1113.
[Bericht](../06_docs/HISTORICAL_CONSTANTS_2026-10-18.md).

## Tragende fotografische Stellen

H015, lokale Kopie
`01_sources/heim_primary/alpha3_origin/Heim_DESY_1982_Archivscan.pdf`.
SHA256 erneut bestätigt:
`C242599F7AAF68BB8E2F3C7756A24687E86FAD879E4D0E22C00585A32403317F`.
Archivfundort und Überlieferungsgrenzen bleiben wie in
[Etappe18](ALPHA3_ORIGIN_SOURCES_2026-09-06.md). Keine neue externe Quelle.

| Physische PDF-Seite | Vollständig betrachtete Fotoseite / enger Prüfgegenstand |
|---|---|
| 5 | GINIT PAGE1, ISN0006-0023: feste Eingaben und abgeleitete Größen; WRITE/FORMAT bis Zeile00005000 |
| 18 | MAIN-Anfang: Banner H.D.Schulz26/7/82, CALL GINIT vor Teilchen-Schleife |
| 21 | GINIT PAGE2/3: restliche Formatfelder, Matrixfortsetzung und RETURN; keine erneute Konstantenzuweisung im sichtbaren Rest |
| 27 | Ausgabekopf, 17 Konstantenzeilen, Parameter-Matrix und E/MU-Anfang; nur Konstantenzeilen vollständig numerisch geprüft |

Zusätzliche vollständige Fotoseiten zur Navigation/Kontexteinordnung:
PDF2-4,6-13,19-20,28-30. Diese Sichtung ist keine vollständige Prüfung der
dortigen Algorithmen oder Resonanzmassen. Fotografien zeigen teils nur
Ausschnitte zusammenhängender Papierlisten. Die vollständige Fotoseite
ist nicht mit dem vollständigen ursprünglichen Papierblatt gleichzusetzen.
PDF20 hat eine Hand vor Teilen des Listings; die Konstantentranskription
stützt sich auf die freie Sicht aufPDF5.

Datumsaufdrucke: Kommentar17/03/82; Banner26/7/82; Compilerkopf
DATE82.223/09.22.04 bei GINIT. Diese Angaben werden nicht zu einem
einzigen bewiesenen Ausführungsdatum zusammengezogen. Keine forensische
Authentifizierung, keine Ausführung historischer Software.

OCR aus pypdf und pdftotext ist hier extrem lückenhaft. Keine negative
Fundbehauptung aus Volltextsuche abgeleitet. Poppler-Bilder unter
`tmp/pdfs/historical_constants/`, bestehendes `tmp/pdfs/alpha3_desy/desy-21.png`
und `tmp/pdfs/alpha3_origin/desy-20.png`; zusätzlich vollständige JPEGs
unter `tmp/pdfs/structure_handling_fortran/originals/` mit nullbasiertem
Bildindex (004=PDF5,026=PDF27), anhand des Seiteninhalts abgeglichen.
5/27 auch in Originalauflösung nachgelesen.

## Statische spätere Überlieferung

H010-Pascal0.62c: GVALUES, GINIT und Banner neu gelesen, insbesondere
Zeilen141-179,197-215,632-635. Mehrfache Zuweisung: letzte aktiv.
H010-Vergleichstext: Kopf und Konstantenblock neu gelesen. Dort steht
ausdrücklich ein Ausgabelistendatum2002-12-02 und Pascal2006, obwohl
der Programmbanner26/07/82 enthält. Daher kein unveränderter1982-Laufbeleg.
H010-C und H006 nur über die bestehenden Detailreviews verglichen;
keine neue vollständige Quellprüfung dieser Dateien behauptet.

Erneut geprüfte Hashes:

| Datei | SHA256 |
|---|---|
| H006 Massenformel_nach_B_Heim_1982.pdf | F74DA0DAC8496BCD01226F54D88598152D67E1C954943AF61D0EC1811F5527BE |
| H010 Pascal0.62/GPROG0.62c.PAS | 1C1D60DC68F0EB540AA0E061896EF03559E3F57846D1E8A3AA28563694CDC59C |
| H010 C0.66/gprog_0.66.c | 29CBF3EBC197EFC8044C2C34D71AB40DD7C6F6829368A412812C7868A287B7B0 |
| H010 Pascal0.62/comparison GPROGOUT Fortran - Pascal0.62.txt | F30D419B1A753EE59572429484A6CF9C133F5579731E17A052C10938CB87C99B |

Die vollständigen Dateinamen mit Leerzeichen stehen im bestehenden
[H010-Konstantenreview](../04_reconstruction/alpha_audit/reviews/HISTORICAL_N0_CONSTANTS_REVIEW_2026-09-06.md).
Alle Quellkopien unverändert. H00329/H004371 werden aus der unmittelbar
vorhergehenden Etappe40 übernommen; keine erneute Sichtung behauptet.

## Eigener Beitrag

Transkription von17 Ausgabezeilen und den festen GINIT-Eingaben;
unabhängig davon benannte mathematische Nachrechnung in Decimal.
60/90-Stellenkontrolle und separate direkte binary64-Kontrolle von EQ/AMU.
Die historische Ausgabe war vor Rechnung bekannt. Kein blinder Test,
kein Nachweis einer Massenrechnung, kein Peer Review.
