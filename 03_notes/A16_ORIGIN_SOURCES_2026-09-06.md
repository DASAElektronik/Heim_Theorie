# A16-Quellenumfang und Fassungsgrenzen

2026-09-06, Etappe27; keine neue PDF oder fremde Programmausfuehrung.

## Kopien und erneut gepruefte SHA256

| ID | Lokaler Pfad unter Projektwurzel | SHA256 |
|---|---|---|
| H004 | 01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf | F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849 |
| H006 | 01_sources/heim_primary/Massenformel_nach_B_Heim_1982.pdf | F74DA0DAC8496BCD01226F54D88598152D67E1C954943AF61D0EC1811F5527BE |
| H015 | 01_sources/heim_primary/alpha3_origin/Heim_DESY_1982_Archivscan.pdf | C242599F7AAF68BB8E2F3C7756A24687E86FAD879E4D0E22C00585A32403317F |
| H010/C | 01_sources/heim_primary_unpacked_untrusted/massformula/C 0.66/gprog_0.66.c | 29CBF3EBC197EFC8044C2C34D71AB40DD7C6F6829368A412812C7868A287B7B0 |
| H010/Pascal | 01_sources/heim_primary_unpacked_untrusted/massformula/Pascal 0.62/GPROG 0.62c.PAS | 1C1D60DC68F0EB540AA0E061896EF03559E3F57846D1E8A3AA28563694CDC59C |

## Was Root selbst gelesen hat

- H006 Vollseiten Druck/PDF6/7: XV-XIX, A-Matrix-Status und A16/XXIV.
  Bestehende Bilder `tmp/pdfs/n0_alias/h006-06.png`, `h006-07.png`.
  Definitions-/Zahlenvertrag aus Etappe26 erhalten, nicht neu normalisiert.
- H004 Druck330--336/PDF336--342 vollstaendig, einschliesslich
  108/108a, F16-Spinorrolle, Grenzwert,109/109a/109b, Y9 und heuristischem
  Status. Buchreview zusaetzlich Druck325--337/PDF331--343.
- H004 EinfuehrungDruck1/PDF12, Y_k-Tabellenkonvention, sowie folgende
  Druck2/PDF13 als Kontext. Keine pauschale+6-Seitenverschiebung fuer
  den Vorspann: PDF7 ist nicht die gesuchte Einfuehrungsseite.
- H015 PDF21 als Vollseite und Detail der Matrix, GINIT-Seite2,
  ISN0031/00005308. PDF20 als vollstaendige vorhandene Leseansicht und
  Detail des GINIT-Anfangs, Kommentar17/03/82 und Compilerkopf.
  Schatten und abgeschnittener unterer Text der Fotografie begrenzen
  Aussagen zu weiteren Definitionen auf PDF20. Kein Gesamtprogrammnachweis.
  Insbesondere ist die H015-ETA-Zuweisung nicht glyphensicher gelesen;
  H010s Definition wird nicht als H015-Originaltranskription ausgegeben.
- H015 PDF39 als Vollseite und Matrixdetail: A16 explizit alpha/(5eta),
  keinY9. Oben steht4, unten5; Ursache offen. Alte Verweise auf Blatt4
  benannten die obere Ziffer. Aktueller A16-Anker benennt beide Folios
  und den Matrixblock unten. `tmp/pdfs/alpha3_origin/desy-39.png` und
  `tmp/pdfs/a16_archive/h015-p39-a16-typescript-detail.jpg` visuell gelesen.
- H010 Kopf-/Portierungstexte, C-GInit-Kontext ca.579--727 mit ETA-
  Definition und A16:705, Pascal-GINIT-Matrixkontext mit A16:291.
  Reines statisches Lesen; keine Ausfuehrung untrusted Programme.

Die neue Buchreview und Archivreview enthalten ihren jeweiligen
zusaetzlichen Suchumfang. Keine Behauptung, das gesamte Werk oder alle
Archivalien seien auf fehlende Herleitungen durchsucht worden.

## Darstellungs- und Herkunftsgrenzen

H006 bleibt IGW-Wiedergabe2002/2003 eines auf1982 datierten Textes;
H004 ist die vorliegende spaetere Buchausgabe; H015 ein heutiger Scan
fotografierter Listings. Der lokale Hash prueft Identitaet, nicht Echtheit.
H010s Angaben ueber1978/1982/2001/2006 sind Portierungskommentare.
H015s Compiler-VERSION1.3.0(01MAY80) ist kein Formeldatum.
Die explizite lokale A16-Formbruecke ersetzt keine lueckenlose Editionskette.

Der erneute Abruf des [H015-Archivlinks](https://burkhardheim.de/media/f/c57c27a0-3692-5fae-920d-5ba89ad58349)
scheiterte im Web-PDF-Werkzeug an der Dateigroesse96,663,680Byte.
Daraufhin wurde die schon archivierte, hashgepruefte PDF verwendet;
kein angeblich neuer Download oder neuer Primaerquellenfund im Netz.

Arbeitsbilder geordnet unter `tmp/pdfs/a16_book/` und
`tmp/pdfs/a16_archive/`, daneben wiederverwendete alte Bilder. Grosses
PNG wurde vom Bildwerkzeug teils nicht eingelesen; kleinere Detailansichten
und Vollseiten wurden stattdessen geprueft. Keine Quelldatei bearbeitet.
Diese lokalen, von Git ausgeschlossenen Leseansichten sind keine
freigegebenen Veroeffentlichungsabbildungen.

## Enger Schluss

Belegt sind die Nennerklammer im H015-Listing/Typoskript und die Buchform malY9,
die F16->A16-Strukturrolle sowie der vom Buch benannte heuristische
Herleitungsstatus. Eine Herleitung gerade von5,6,(pi*e)^2 oder Y9=1
fehlt im geprueften Buchabschnitt. Das ist kein Nachweis ihrer
Nichtexistenz in saemtlichen Publikationen und keine Gesamtwiderlegung.
