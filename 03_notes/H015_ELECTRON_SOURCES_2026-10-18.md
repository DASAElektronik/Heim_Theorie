# Quellenumfang: H015-Elektron im Grundzustand

2026-10-18, Etappe42. Ein Agent, keine neue externe Quelle.
[Bericht](../06_docs/H015_ELECTRON_2026-10-18.md),
[vorher festgelegter Rechenvertrag](../00_admin/H015_ELECTRON_PLAN.md).

## Quelle und geprüfter Umfang

Lokale H015-Kopie:
`01_sources/heim_primary/alpha3_origin/Heim_DESY_1982_Archivscan.pdf`.
SHA256 mit dem neuen Rechner erneut bestätigt:
`C242599F7AAF68BB8E2F3C7756A24687E86FAD879E4D0E22C00585A32403317F`.
Fundort, Archivierung und Datierungsgrenzen siehe
[bestehende Archivnotiz](ALPHA3_ORIGIN_SOURCES_2026-09-06.md).
Der Hash identifiziert die Datei; keine forensische Echtheitsfeststellung.

| Physische PDF-Seiten | Vollständig betrachtete Fotoseiten / tragende Stellen |
|---|---|
| 18,4 | MAIN: Eingaben, EPS-/CS-/Ladungszuordnung, IX-Schleife; Aufrufe von GINIT/GBASE/GSTRUC/GMASS; N=0 vor den Resonanzfällen; FORMAT300 |
| 5,21 | GINIT: fester Konstantensatz, AMU und ALFP/ALFM; Matrixdefinitionen, Nenner A36/A41, Ausgabeformate |
| 22,7 | GBASE: IS und Q1..4, ALF1..3, GKQ, TEMP1/2-Zweige, WGX; begrenzte Reduktion für K=PG=QG=1,KAPPA=0 |
| 23 | GSTRUC: FN und erste drei Ganzzahlen, W4-Verzweigungen, log-Schritt, Ausgabe K/n; GOTO2 überspringt den nur im W4>1-Zweig stehenden Transfer |
| 24 | GMASS: KGH, FIG und AM=AMU*FAKMEV*ALFP*(KGH+FIG); ETAQK einschließlich lokalem PI-Literal |
| 27 | E-Multiplettkopf, geladene E-Zeile und K/n-Ausgabe; der benachbarte neutrale Fall und Myon werden nicht gerechnet |

Zusätzlich vollständig zur Navigation/Kontexteinordnung betrachtet:
PDF2,3,6,8,19,25,26. Keine neue Detailprüfung aller dortigen Routinen,
Jobdaten oder Warnhinweise behauptet. Die Fotografien können Teile eines
Papierblatts abschneiden; vollständige Fotoseite bedeutet nicht vollständiges
Papieroriginal. Kein Beleg einer lückenlosen historischen Ausführungsakte.

Lesebilder: vorhandene H015-JPEGs unter
`tmp/pdfs/structure_handling_fortran/originals/`, nullbasiert (023=PDF24).
Bei Detailausschnitten zuerst EXIF-Orientierung angewendet und dann
beschnitten, keine inhaltliche Retusche. Ausschnitte MAIN/GBASE/GSTRUC/
GMASS/E-Ausgabe unter `tmp/pdfs/h015_electron/`. Die tragenden Aussagen
beruhen auf visueller Sicht; OCR wurde nicht als Abwesenheitsbeweis benutzt.

## Konkrete Ablesungen

- E-Kopf: K=1, PG=1, QG=1, KAPPA=0; geladene Zeile CS=0,KQ=1,
  EPS=1,QX=-1,N=0. K=(3,3,2,1), n=(0,0,0,0).
- Elektronenwert `0.51100326Q+00` unter `AM(MEV)`; MAIN verwendet
  Q17.8. Vergleich als gerundete Massenenergie, nicht als Messung.
- ETAQK: `PI/(KQ**4*(4.Q0+K)+PI**4)**0.25Q0`.
  Damit hier Nenner PI^4+5; GINIT-ETA hat PI^4+4.
- GSTRUC: `REST=QFLOAT(2*IK-1)/QFLOAT(3*IQ4)`,
  `TEMP=-QLOG(W4)/REST`, `IK4=IQINT(TEMP)`, `GOTO 2`;
  Label2 weist `IN4=IK4-IQ4` zu. Kein Epsilon-Zuschlag sichtbar.
- GBASE-ALF3 erneut gegen das Foto gelesen; die frühere Transkription
  in `ALPHA3_DESY_CODE_REVIEW_2026-09-06.md` stimmt im benötigten Block.
  Keine H006-/H010-Formel oder Konstanten daraus übernommen.
- GMASS-FIG: Produkt plus zwei additive Terme; der Faktor mit N1/Q1
  wird erst nach Auswahl zu1. Reduzierte Produktform und algebraisch
  zusammengefasste Form getrennt gegengerechnet.

## Eigene Rekonstruktion und Grenzen

Die ausgewertete Formel, das eingegrenzte Auswahlverfahren und Decimal-
Rechnung sind eigene Beiträge. Die achtstellige Ausgabe war vor Rechnung
bekannt. Der letzte Ganzzahlschritt verwendet die exakte Identität
W4=exp(-1/3), nicht eine nachträgliche Wahl anhand der Masse.
Das ist keine Wiederholung des SYSTEM/370-Compilers oder seiner REAL*16-
Bibliothek. Matrix und Resonanzpfade werden nicht vollständig ausgeführt;
benötigte Zweigreduktionen und relevante Nenner sind gesondert geprüft.

Vorherige Berichte Etappen17/18/41 dienen zur Einordnung. H004, H006 und
H010 wurden in dieser Etappe nicht erneut vollständig quellengeprüft.
Kein neuer Vergleich mit experimentellen Referenzdaten, keine Kalibrierung.
