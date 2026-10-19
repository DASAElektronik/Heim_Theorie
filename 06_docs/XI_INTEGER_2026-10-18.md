# Xi: der frühe Ganzzahlquotient erklärt den Korrekturhinweis

2026-10-18, Einheit 47. [Prüfvertrag](../00_admin/XI_INTEGER_PLAN.md),
[Rechner](../scripts/audit_xi_integer.py),
[vollständige zwölf Zeilen](../05_analysis/xi_integer_results.json).

## Ergebnis

Die fotografierte MAIN-Zeile ergibt für Xi Strangeness 0 und Ladungen
(+1, 0). Eine exakte rationale Auswertung derselben Expression ergibt
−2 und (0, −1), entsprechend dem Korrekturblatt. Unter den zwölf
Grundmustern der H006-Tabelle betrifft diese Differenz ausschließlich Xi.
Das erklärt einen konkreten Implementierungsfehler; es bewertet nicht
die gesamte Theorie und liefert noch keine korrigierte Xi-Masse.

## Quellen und Versionsgrenzen

Vollständig visuell geprüft: H017 Archivfotos 48 (MAIN Seite1), 59
(MAIN Seite2), 57 (Korrekturblatt), 103 (GBASE Seite1), H006 PDF2/3
(Symbolik und gesamte Grundmustertabelle), H015 PDF18 (MAIN), PDF24
(GMASS/ETAQK). H017 Fotos 54/77/78 zusätzlich zur Ausgabenavigation
betrachtet; keine Xi-Ausgabe daraus gewonnen. Ihre Tabellen sind nicht
vollständig transkribiert. Alle H017-Originale wurden in Einheit46 gehasht;
Einzelnachweise stehen im [Manifest](../05_analysis/desy_collection_sources.json).

H006 ist eine spätere IGW-Wiedergabe des 1982-Materials, mit redaktionellen
Anmerkungen. Hier dient ausdrücklich seine Tabelle III/IV als Vergleich,
nicht pauschal jede Formel dieser Fassung. H01757 trägt keine erkennbare
Datierung oder Signatur. Es nennt S=−2, Ladungen 0/−1 und eine fehlende
unmittelbare Massenrelevanz von S. Ein direkter Auftrag zur Änderung eines
bestimmten archivierten Programmlaufs ist damit nicht bewiesen.

H017 MAIN trägt 82.205/15.00.44; seine Zeile ISN0030 lautet:

```fortran
ICS=2/(IK*(1+IKAPPA))*(IPG*IEPSP+IQG*IEPSQ)*(IK-1+IKAPPA)
```

H015 PDF18/ISN0032 enthält dieselbe Expression, trotz anderem
Listingstand 82.223/09.22.03. Der Vergleich beweist nur diese lokale
Übereinstimmung. Die Originaldateien und bisherigen Rechenprofile bleiben
unverändert. `IMPLICIT REAL*16 (A-H,J-Z)` lässt die mit I beginnenden
Variablen ganzzahlig; auch das Literal 2 ist ganzzahlig.

Die zugrunde gelegte Sprachregel ist linksassoziative Multiplikation/Division
mit Abschneiden ganzzahliger Quotienten gegen null. Als heutige
Herstellerreferenz: [IBM, Arithmetic](https://www.ibm.com/docs/en/xl-fortran-linux/16.1.0?topic=expressions-arithmetic).
Suchauszug am 2026-10-18 verfügbar; direktes Öffnen lieferte403. Diese
Referenz ersetzt keine Emulation des damaligen System/370-Compilers.

## Exakte Rechnung

H006 PDF3/IV, Zeile x9: B=1, P=1, Q=1, KAPPA=1, EPS=+1;
mit k=B+1 also (2,1,1,1). Daraus ergeben sich EPSP=EPSQ=−1.

| Schritt | Fotografiertes Integerlisting | Eigene rationale Diagnose |
|---|---:|---:|
| Vorfaktor 2/[2(1+1)] | 0 | 1/2 |
| (P·EPSP+Q·EPSQ) | −2 | −2 |
| (k−1+KAPPA) | 2 | 2 |
| CS | 0 | −2 |
| IQX, Reihenfolge IX=1,2 | +1, 0 | 0, −1 |
| KQ=abs(IQX) | 1, 0 | 0, 1 |

Das spätere `CS=QFLOAT(ICS)` kann den bereits verlorenen Bruchteil nicht
wiederherstellen. Die rationale Diagnose ist keine Behauptung über einen
tatsächlich ausgeführten historischen Patch. Die vollständige Expression
kann in dieser geprüften Domain auch durch Multiplikation des Zählers vor
der abschließenden ganzzahligen Division ausgewertet werden: ihr Ergebnis
ist in allen zwölf Fällen ganzzahlig. Keine Aussage über beliebige Inputs
oder Überlaufgrenzen eines Originalcompilers.

Alle zwölf Tabellenzeilen bei EPS=+1 und alle27 Komponenten wurden
geprüft. Elf Zeilen stimmen schon im Integerlisting mit der Tabelle
überein; x9 weicht ab. Die rationale Diagnose stimmt mit allen zwölf
überein. Das Pseudosingulett x3 behält dabei beide tabellierten Komponenten.
Antiteilchen und weitere Zustände sind nicht Teil dieser Rechnung.

## Was folgt für Massen?

H01748/ISN0035 benutzt ICS in der Ladungsrechnung; H01759/ISN0037–0038
bildet IKQ/KQ und ruft in ISN0042 GBASE auf. Dort verwenden
H017103/ISN0017/0019 die Funktion ETAQK(KQ,K) für ALF1/ALF2. Die
Korrektur ändert also den Input eines tatsächlichen Koeffizientenpfads,
nicht nur den Ausdruck einer Überschrift.

H015 PDF24 zeigt zusätzlich eine explizite KQ-Abhängigkeit in GMASS und
ETAQK. Daraus folgt keine bezifferte Massendifferenz und noch kein Beweis,
dass die ungeordnete Menge beider Xi-Massen verändert wird: zunächst
werden die beiden KQ-Werte vertauscht. Für einen Nachweis bloßer
Umordnung müsste ausgeschlossen werden, dass weitere Komponentenlabels
den nachfolgenden Pfad unterscheiden. Das ist ein separater nächster Schritt.

## Reproduktion und Grenze

```powershell
py -3.13 scripts/audit_xi_integer.py --check
py -3.13 -m unittest tests.test_xi_integer
```

Vier neue Tests: Vorzeichen der Ganzzahldivision, unabhängige reduzierte
Xi-Rechnung, zwölf Quellenzeilen und Elektronen-/Domaingrenzen. Der
vollständige bisherige Elektronenrechner wird nicht erweitert oder repariert.
Keine Messmassen, Konstantenfits, neuen F_S-Annahmen oder nachträglich
angepassten Inputs. FIND-055 ergänzt die bestehenden54 Befunde als lokale
Implementierungsdiagnose; diese Anzahl ist keine Anzahl unabhängiger Fehler.

Abschlussprüfung:377 Tests bestanden; Snapshot und Registermetadaten gültig.
H006/H015-SHA256 erneut identisch mit dem Quellenregister; die54 alten
Befundobjekte wurden gegen Git-HEAD verglichen und bleiben unverändert.
