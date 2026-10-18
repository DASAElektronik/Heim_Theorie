# Xi-Folgeprüfung: bedingte Umordnung und spätere Übertragungen

2026-10-18, Einheit 48, Ausgang decbb36. Anschluss an
[Einheit47](XI_INTEGER_2026-10-18.md), keine neue Masse berechnet.

## Was sich weiter eingrenzen lässt

Für k=2, PG=QG=1, KAPPA=1 verschwinden die ausdrücklich
vorzeichenabhängigen QX-Terme in GBASE. Unter der Voraussetzung einer
endlichen, wohldefinierten und vom alten Speicherzustand unabhängigen
Auswertung hängen die beiden Xi-Massenpfade damit nur noch über KQ
von der Komponente ab. Die Korrektur tauscht KQ=(1,0) gegen (0,1).
Dann werden die beiden Pfade umgeordnet; ihre ungeordnete Ergebnismenge
bleibt gleich. Das ist eine bedingte Folgerung aus dem Programm, keine
Reproduktion der beiden historischen Xi-Massen.

Der Vorbehalt ist konkret: In H015 GSTRUC kann der Zweig W4>1 einen
IK4-Vorbestand verwenden (bereits FIND-041). Eine universelle Aussage
über den tatsächlich ausgeführten, sequenziellen Originaljob folgt daher
nicht allein aus der Formelabhängigkeit. Weder Eintritt dieses Zweigs
für Xi noch sein tatsächlicher Vorbestand wurden hier bestimmt.

## Gelesener Datenfluss

H015 PDF7,22,23,24 vollständig visuell gelesen: GBASE beide Listingseiten,
GSTRUC beide Listingseiten, GMASS/ETAQK. H01518 MAIN bereits in47.
Die PDF-Seiten können mehrere fotografierte Listingseiten enthalten.
Hash unverändert gemäß47. Nur dieser Programmstand trägt die folgende
Abhängigkeitsprüfung; keine automatische Übertragung aller Details auf H017.

| Stelle in H015 | Explizite Abhängigkeit | Reduktion für Xi |
|---|---|---|
| GBASE ISN0038, TEMP2 | QX im Summanden mit binom(PG,2) | binom(1,2)=0 |
| GBASE ISN0038, TEMP2 | weitere QX-Terme mit binom(PG,3) | binom(1,3)=0 |
| GBASE ISN0044, AQ | QX·(3−QX)·(K−1)·(1−KAPPA) | 1−KAPPA=0 |
| GBASE übrige Zuweisungen | KQ und feste Multipletparameter | keine direkte IX/X/CS-Abhängigkeit gefunden |
| GSTRUC | Koeffizienten, WG, N und Strukturgrößen | keine direkte QX/CS/IX/X-Abhängigkeit; Vorbestandsvorbehalt |
| GMASS/ETAQK | KQ, feste Multipletparameter, Strukturgrößen | keine direkte QX/CS/IX/X-Abhängigkeit gefunden |

COMMON-Deklarationen enthalten auch ungenutzte Variablen; entscheidend
sind die ausgeführten rechten Seiten und Sprünge. Die Kürzung von
Nullfaktoren setzt voraus, dass die mitgerechneten Ausdrücke definiert
sind; keine Rechtfertigung von 0·undefiniert. Die KQ-abhängigen Koeffizienten
bleiben erhalten und können sich zwischen neutraler und geladener
Komponente unterscheiden. Eine bloße Überschriftenkorrektur mit sonst
unveränderten Zeilen ist deshalb ebenfalls nicht nachgewiesen.

Für einen vollständigen historischen Nachweis wären getrennte Quellen-
und Ausführungsverträge für beide Xi-Komponenten nötig: Zustandskopf,
N, W4-Zweig, IK4-Vorbestand oder dessen sichere Überschreibung, Ausdruck
und genaue Programmfassung. Ohne diesen Beleg bleibt die bedingte
Umordnung die belastbare Aussage. Kein freies Massenanpassen.

## Spätere Übertragungen vermeiden diesen Divisionsverlust

H010 lokal statisch gelesen, keine fremden Programme ausgeführt:

- Pascal `massformula/Pascal 0.62/GPROG 0.62c.PAS`, Zeilen682–704,
  besonders689: `round(2/(k*(1+kappa))*...)`. In Free Pascal liefert `/`
  auch bei Integeroperanden ein reelles Ergebnis; Ganzzahldivision wäre
  `div`. [Herstellerreferenz, Abschnitt12.8.1](https://docs.freepascal.org/docs-html/3.0.0/ref/refsu46.html),
  am2026-10-18 direkt gelesen. Die äußerlich ähnliche Zeile hat deshalb
  hier andere Divisionssemantik als das FORTRAN-Listing.
- C `massformula/C 0.66/gprog_0.66.c`, Zeilen1212–1230, besonders1215:
  der Vorfaktor verwendet ausdrücklich `2.0` und `1.0+kappa`.
  Die Division verliert den Faktor1/2 daher ebenfalls nicht.

Die Pascal-Datei nennt im Kopf eine Übertragung vom12.03.2006. Ihr
Kommentar Zeilen30–34 schreibt einen Strangeness-Hinweis H.D.Schulz zu
und verweist auf die Ausgabebezeichnung xi; die ausgeschriebene Bezeichnung
weicht vom Foto ab. Das ist spätere Zuschreibung, keine Signatur oder
Datierung des H01757-Originalblatts und kein Nachweis, wann der Fehler
erstmals behoben wurde. Der fortbestehende Warnkommentar beweist nicht,
dass dieselbe Integerdivision im Pascal-Code weiter fehlschlägt.

Die Rundungs-/Kosinusregeln, Konstanten und Strukturregeln der Ports
unterscheiden sich zusätzlich. Die lokale Verbesserung ist keine
Bestätigung einer insgesamt originalgetreuen Übertragung.

SHA256 der statisch gelesenen H010-Dateien, relativ zu
`01_sources/heim_primary_unpacked_untrusted/`:

| Datei | SHA256 |
|---|---|
| massformula/Pascal 0.62/GPROG 0.62c.PAS | 1c1d60dc68f0eb540aa0e061896ef03559e3f57846d1e8a3aa28563694cdc59c |
| massformula/C 0.66/gprog_0.66.c | 29cbf3ebc197efc8044c2c34d71ab40dd7c6f6829368a412812c7868a287b7b0 |

## Entscheidung am Verzweigungspunkt

Der neue Xi-Hinweis ist bis zur lokalen Ursache und bedingten
Massenumordnung verfolgt. Die Vorbestandsgrenze ist ein Anschluss an
FIND-041, kein zweiter neu gezählter Fehler.55 Befunde bleiben bestehen.
Keine Änderung am Rechner, keine Wiederholung der bereits erfolgreichen
377 Tests für diesen reinen Quellen-/Abhängigkeitsbericht erforderlich.

Numerische Xi-Fortsetzung erst mit dem genannten Zustands-/Ausdruckbeleg.
Der nächste unabhängige Verständniszweig ist die bereits vorgemerkte
Messgrößenzuordnung der Neutrino-Zustände aus H016, vor einer externen
Bewertung. Die ursprüngliche F_S-Arbeitstabelle bleibt weiterhin offen.
