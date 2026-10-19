# Strukturbehandlung: Quellenumfang und Zuschreibung

2026-09-06, Etappe31. Keine neue Originalquelle importiert oder veraendert.

## Identifizierte lokale Kopien

| Quelle | Datei | SHA256 |
|---|---|---|
| H004, Heim, Elementarstrukturen der Materie II, Ausgabe1996 | `01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf` | `F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849` |
| H015, fotografierte Listings/Typoskript; heutiger Archivscan | `01_sources/heim_primary/alpha3_origin/Heim_DESY_1982_Archivscan.pdf` | `C242599F7AAF68BB8E2F3C7756A24687E86FAD879E4D0E22C00585A32403317F` |
| H010, Archiv | `01_sources/heim_primary/massformula.zip` | `8D29EAE202B9C85D3E2A19203A760E2581680D330A2C3AC601F2D73EB1E00AFE` |
| H010, C0.66 | `01_sources/heim_primary_unpacked_untrusted/massformula/C 0.66/gprog_0.66.c` | `29CBF3EBC197EFC8044C2C34D71AB40DD7C6F6829368A412812C7868A287B7B0` |
| H010, Pascal0.62c | `01_sources/heim_primary_unpacked_untrusted/massformula/Pascal 0.62/GPROG 0.62c.PAS` | `1C1D60DC68F0EB540AA0E061896EF03559E3F57846D1E8A3AA28563694CDC59C` |

Root hat alle fuenf Hashes erneut geprueft. Kopienidentifikation ist keine
historische Authentifizierung. Keine Quellprogramme kompiliert/ausgefuehrt.

## Eigene Root-Lektuere

H004, vollstaendige relevante Druck-/PDF-Seiten:

- 321/327 und323/329: (107), Grundmusterbezug und explizite deltaG.
  Bilder `tmp/pdfs/book_selection_source/edm2-327.png`, `edm2-329.png`.
- 328/334 und329/335: Kollaps/Reset, (107a), gedruckte sigma-Gleichsetzung.
  Bilder `tmp/pdfs/a16_book/edm2-334.png`, `edm2-335.png`.
- 340-342/346-348: Exhaustion, Zone4-Kappe/Transfer und Verbot analoger
  Transfers; anschliessende F_S-Passage nur Kontext, keine F_S-Rechnung.
  Bilder `tmp/pdfs/book_selection_source/edm2-346.png` bis `edm2-348.png`.

Weitere Buchkontextseiten321-330 las der Buchagent. Sie sind nicht als
zusaetzliche neue Root-Sicht behauptet. Die vorherige Eta-/A16-Vertragspruefung
bleibt in Etappe30 belegt; keine neue Konstantenauswahl.

H015, ganze verfuegbare Fotoseiten, nicht behauptete Vollstaendigkeit jedes
darauf teilweise angeschnittenen Papierblatts:

- PDF23: GSTRUC-Seiten1/2, `h015x-23.jpg` und Originalbild022.
- PDF18/4/19: MAIN-Seiten1/2/3 in anderer Reihenfolge als im PDF;
  Originalbilder017/003/018. Caller aufPDF4, Limitfortsetzung aufPDF19.
- PDF22: GBASE-Seite1 und angeschnittener BeginnSeite2, Originalbild021.
- PDF24: GMASS und ETAQK, Originalbild023; nur Kontrollfluss/Verbrauch
  der Werte, keine neue Massen-/Eta-Auswertung.
- PDF14: repraesentative Ausgabe mit IK-/N-Spalten, Originalbild013.
  Keine Einzelmassen transkribiert oder alle Ausgabeseiten validiert.
- PDF5: GINIT, Originalbild004, nur Navigations-/Kontextsicht.

Originalbilder liegen unter
`tmp/pdfs/structure_handling_fortran/originals/h015-NNN.jpg`, NNN ist
hier der nullbasierte Bildindex. Zuordnung zur physischen PDF-Seite wurde
am Inhalt geprueft. Wegen instabiler grosser PNG-Transporte wurden die
lesbaren eingebetteten JPEG-Vollseiten verwendet. OCR war kein Formelbeleg.
Arbeitsbilder sind organisiert, ignoriert und keine Publikationsfreigabe.

H010: Root las C-Kopf/aktive ROUND-Schalter, myround469-499,
GStruc894-979, GMass984-1029, GLimit1032-1117 und direkte Caller1241-1315.
Zusaetzlich Sammlung332-375, Nachvergleich378-406 und Schluss1315-1330,
sowie dateiweite K/n-Zuweisungs-/Caller-Suche. Pascal-Kopf,
GSTRUC452-512, GMASS516-547, GLIMIT550-622 und Caller697-757 gelesen.
Keine neue Validierung der gesamten Matrix- oder Massenformeln.

Beide Readmes im jeweiligen Programmordner vollstaendig gelesen;
Bearbeiterkommentare bleiben Bearbeiterangaben. Hashes:
C-Readme `4A9C58FCAB8009DBC30FB85F5E22AE4F17BB589133EF0B43AA886AC7980DEE39`,
Pascal-Readme `32F3FEA726B772170355622CED2465BE8227A69D85DF9859808D03A5454D9371`.

## Online-Abgleich und Eigenanteil

Die [Archivseite](https://heim-theory.com/archiv/) wurde erneut geoeffnet,
nur als Fundortabgleich. Keine neue Datei und keine moderne Theorie- oder
Empirieaussage daraus in den Befund uebernommen.

Heim zugeschrieben werden die im Buch belegten Struktur-/Kollaps-/
Exhaustionsideen. Das fotografierte Listing bleibt H015; H010 nennt
Schulz/Mueller/Posdzech/leovinus als unterschiedliche Bearbeitungsstufen.
Weder Aehnlichkeit noch ein passendes Ergebnis beweist Editionsidentitaet.
Unsere Leistung ist die statische Kontrollflussrekonstruktion, die
Quellenabgrenzung und die ausdruecklich synthetische Mathematikdiagnose.

Root las drei STRUCTURE_HANDLING_*-Reviews und pruefte den unabhaengigen
36-Kontrollen-Block erneut. Acht neueTests,272gesamt und12bestehende
Snapshotchecks bestanden. Interne Gegenpruefung, kein externesPeerReview.
Alle alten Rechner/Inputs/Snapshots und49CSV-Normalisierungen bleiben gleich.
Plancheckpointec5e5a9, Buch-/Port-/Testcheckpoint0118ae9.
