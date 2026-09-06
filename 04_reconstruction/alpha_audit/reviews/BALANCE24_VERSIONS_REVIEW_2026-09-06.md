# Etappe 24: versionsgebundene Quellenbilanz

Stand: 2026-09-06. Synthese ausschliesslich aus bereits geprueften
Projektberichten; keine neue PDF-/Webrecherche und keine neue Massenrechnung.

Massgebender Arbeitsgrundsatz ist
[SOURCE_ATTRIBUTION](../../../00_admin/SOURCE_ATTRIBUTION.md): Ein Datum,
Hash oder Zahlentreffer beweist weder Echtheit noch unveraenderte
Ueberlieferung. Lokale Formelbruecken duerfen nicht zu einer
fassungsuebergreifenden Gesamtausgabe zusammengesetzt werden.

## 1. Ergebnis

Die Etappen 16--23 haben vier konkrete, unterschiedlich starke Bruecken
erbracht:

1. **H006-intern, Elektron/N=0:** Der Basisanstieg, die Strukturpotenz und
   der gedruckte Auswahlalgorithmus erzeugen bedingt das Nulltupel
   `n=(0,0,0,0)`; `(0110)` ist nicht dieses Tupel.
2. **H006 gegen H010, derselbe enge N0-Knoten:** `mu`, die Hilfsstruktur bis
   `alpha1/2`, `K+G+H`, `Phi` und der abschliessende Massenkoerper sind bei
   gleich gehaltenen Eingaben algebraisch anschliessbar. Zwei aktive
   Unterschiede verbleiben in `alpha3`.
3. **H004 -- H010 -- H015-Listing:** Genau diese beiden H010-Formen von
   `alpha3` stehen auch in Buch II (98c) und im fotografierten
   FORTRAN-Listing. Dies belegt die Formelgestalt, aber keine vollstaendige
   Programm- oder Editionsidentitaet.
4. **H006 -- H015-Typoskript, Exponent:** Die gruppierte Exponentenform ist
   im Typoskript und in fast allen homologen H006-Wiederholungen belegt.
   Innerhalb der geprueften H006-Kette weicht nur (XIV) ab. Die Ursache ist
   nicht belegt.

Daneben bilden H013/H014(8c) nach ihren eigenen Substitutionen eine direkte
Bruecke zu H007(B8), jeweils mit `2*alpha3=N3`. Diese neuere logarithmische
`N3`-Familie ist jedoch **keine** Herleitung oder Entscheidung der alten
H006/H004/H010-`alpha3`-Terme.

Es gibt daher keine quellenbelegte vollstaendige gemeinsame „1982-Fassung“.
Es gibt nur lokal benannte Uebereinstimmungen, Unterschiede und bedingte
Rekonstruktionsschritte.

## 2. Fassungsmatrix

| Kennung | Quellen- und Datierungsstatus | Belegte lokale Rolle | Nicht daraus ableitbar |
|---|---|---|---|
| **H006** | IGW-Wiedergabe 2002/2003 von *Die Massenformel nach Burkhard Heim (1982)*; wiedergegebener Schluss `gez. (Heim)`, 25.2.1982; kein verifiziertes Urschriftfaksimile | Elektronzuordnung Druck/PDF3; `Q_j,n_j`, `alpha3`, Masse Druck/PDF5; Basis/Strukturpotenz (XV)--(XIX) S.6; N=0 und (XXVI) S.8; Algorithmus S.9; Grenze (XXXV) S.10 | Unveraenderte Autorurschrift, einheitliche Formelgestalt an jeder Wiederholung oder historische Fehlerursache |
| **H010 Pascal/C** | Spaetere statische Transkriptions-/Portdateien; Header berichten Heim-Formeln 17.9.1978, GPROG/Schulz-DESY 1982 sowie Uebertragungen 2001/2006; diese Angaben sind Dateiselbstauskunft | H006-nahe N0-Auswahl und Massenkoerper; Pascal383--384/C807--808 `alpha3`; Pascal520--546/C998--1026 `KGH`, `Phi`, Masse | Originalprogramm, identische Konstanten, identische Rundung, vollstaendige H006- oder „1982“-Fassung |
| **H015-Listing** | Fotografierter Listingausschnitt in heutigem Archivscan; PDF22 zeigt Kommentar 17/03/82 und Compilerkopf `DATE 82.223`; Digitalisierungsdatum ist kein Werkdatum | ISN0021/Zeilen00003710--00003713: beide H010-`ALF3`-Terme; ISN0022/00004100: `AN3=2*ALF3` | Vollstaendiges Originalprogramm, ausgefuehrter historischer Lauf, gleiche Eingaben oder forensisch gesicherte Autorschaft aller Blaetter |
| **H015-Typoskript** | Fotografierte Blaetter 4, 4a, 5, 6, 7 in derselben Scan-Datei; Blatt7 zeigt `(Heim)`/25.2.1982; Blaetter1--3 sind dort nicht als geschlossener Block belegt | Allgemeiner und N0-Exponent auf PDF39/Blatt4 und PDF41/Blatt5 gruppiert; Wiederholungen/Algorithmus PDF42/Blatt6 und Grenze PDF43/Blatt7 schliessen an | Vollstaendige Gleichheit mit H006, roemische H006-Nummerierung, lueckenlose Ueberlieferung oder Ursache der H006-(XIV)-Abweichung |
| **H004** | *Elementarstrukturen der Materie II*, gepruefter Scan der Ausgabe 1996 | Druck271--278: `alpha3=f-qF`, `F=H+G`; freie und laut Text an Elektron/Proton empirisch angepasste Koeffizienten; (98c) liefert die H010/H015-Listing-Gestalt | Datierung der Formel auf 1978 allein aus anderem Werkdatum; parameterfreie Ableitung; vollstaendige Identitaet mit H006/H010 |
| **H007** | IGW-Wiedergabe 2002/2003 eines berichteten Manuskripts 1989; kein Originalfaksimile | Druck12/PDF3 (B8) logarithmisches `N3`; Druck15/PDF6 (B40) `alpha3=N3/2` | Alte H006/H010-`alpha3`-Formel, deren Potenz-/Wurzelentscheidung oder automatisch die Chronologie der Manuskriptfassungen |
| **H013/H014** | Zwei getrennte undatierte, autorbezeichnete Scans; keine Reihenfolge aus Dateinamen, Upload oder Formgestalt | H013 Druck14--17/PDF15--18 und H014 Druck9--12/PDF9--12: (8c), (8c1), (11a); direkte algebraische Vorstufe zu H007(B8) und `2*alpha3=N3` | Datierung gegeneinander/H007; Herleitung des alten `alpha3`; gemeinsame Gesamtfassung ihrer Massen-, Zeit- oder Alpha-Korrekturen |

H015-Listing und H015-Typoskript sind in derselben heutigen PDF gesammelt,
bleiben aber zwei verschiedene Belegarten. Eine Formel im Listing darf nicht
ohne sichtbare Bruecke dem Typoskriptblatt zugeschrieben werden und umgekehrt.

## 3. Konkrete belegte Formelbruecken

### 3.1 H006-interner N0-Pfad

H006 Druck/PDF3 liefert fuer die geladene Elektronkomponente des
`x_2(0110)`-Multipletts `k=P=Q=q=1`, `kappa=0`, `q_x=-1`. Druck/PDF6
reduziert die Strukturpotenz auf `w=1` und definiert (XV) als Basisanstieg
„fuer `n_j=0`“. Druck/PDF8 setzt bei `N=0` `f=0`; Druck/PDF9 erzeugt mit
dem gruppierten Exponenten und der logarithmischen `K4`-Beziehung erneut
`K_j=Q_j` und damit `n_j=0`.

Das ist ein fassungsinterner, nicht nach einer Sollmasse ausgewaehlter Weg.
Ein literal gespeicherter Elektron-Tabellensatz `n1..n4` wurde gleichwohl
nicht gefunden. Details:
[N0_OCCUPATION_SOURCE_REVIEW](N0_OCCUPATION_SOURCE_REVIEW_2026-09-06.md)
und [HISTORICAL_N0](../../../06_docs/HISTORICAL_N0_2026-09-06.md).

### 3.2 H006/H010-Massenkoerper unter engen Bedingungen

Bei gleichem Elektronknoten, gleichem Nulltupel und gleichen Eingaben sind
folgende Koerper algebraisch angeschlossen:

- `mu`, `eta`, `t`, `alpha+/-`, `eta_qk`, `alpha1/2`, `Q_j`;
- H006 `K+G+H` und H010 `kgh`;
- H006 `Phi` und H010 `fig` im geprueften N0-Fall;
- `M=mu*alpha+*(K+G+H+Phi)` und der entsprechende H010-Koerper vor der
  Ausgabeeinheitenumrechnung.

Nicht gleich sind die beiden aktiven `alpha3`-Terme: H006 setzt
`1+sqrt(eta_qk)` mit unter die Potenz und zeigt im zweiten Term ein
Wurzelglyph; H010 setzt den ersten Faktor ausserhalb der Potenz und besitzt
im zweiten Term keine Wurzel. Die genaue historische Radikandweite in H006
bleibt bildlich offen. Diese Aussage gilt nur fuer den geprueften N0-Pfad,
nicht fuer alle Teilchen oder alle Programmzweige. Details:
[HISTORICAL_N0_FORMULA_REVIEW](HISTORICAL_N0_FORMULA_REVIEW_2026-09-06.md).

### 3.3 Herkunft der H010-`alpha3`-Gestalt

H004(98c), Druck275/278, und H015-Listing PDF22/ISN0021 belegen dieselben
zwei charakteristischen Entscheidungen wie H010:

- `1+sqrt(eta_qk)` steht ausserhalb der Potenz `2k+1`;
- `(2*xi*eta_qk)^k` enthaelt keinen Wurzeloperator.

H004 legt die dafuer verwendeten freien `A_i/B_i` ausdruecklich mit Bezug
auf die Empirie von Elektron und Proton fest. Die Buchstelle erklaert damit
die algebraische Herkunft innerhalb dieser Buchfassung; sie macht die
Wahl nicht parameterfrei. H015 zeigt, dass die Codegestalt nicht erst bei
der Pascal-/C-Uebertragung auftaucht. Es folgt weder, dass jeder H010-Zweig
dem fotografierten Listing gleicht, noch wann die Formel erstmals entstand.
Details: [ALPHA3_ORIGIN](../../../06_docs/ALPHA3_ORIGIN_2026-09-06.md) und
[ALPHA3_DESY_CODE_REVIEW](ALPHA3_DESY_CODE_REVIEW_2026-09-06.md).

### 3.4 Auswahl-/Grenzexponent H006 gegen H015

H006(XIV), Druck/PDF6, zeigt linear
`exp[1-2k(n4+Q4)/3Q4]`. H006(XV), (XXVI), (XXVII), (XXIX), (XXX),
(XXXI), (XXXV) setzen dagegen `1-2k` in Klammern. (XXXIV) enthaelt keinen
Exponentialterm. H015-Typoskript setzt sowohl im allgemeinen als auch im
N0-Ausdruck und im Algorithmus die gruppierte Form.

Die N0-Reduktion und die gedruckte logarithmische `K4`-Umkehrung schliessen
an die gruppierte Form an. Damit ist diese Form keine eigene moderne
Erfindung. Trotzdem bleibt (XIV) nur eine lokalisierte Abweichung der
IGW-Wiedergabe; ein Satzfehler, eine Revision oder eine andere Ursache ist
nicht entschieden. Details:
[HISTORICAL_EXPONENTS](../../../06_docs/HISTORICAL_EXPONENTS_2026-09-06.md)
und [HISTORICAL_EXPONENT_REPRINT_REVIEW](HISTORICAL_EXPONENT_REPRINT_REVIEW_2026-09-06.md).

### 3.5 Neue logarithmische N3-Familie

H013/H014(8c) werden nach ihren unmittelbar gedruckten Definitionen
`u=2*pi*e` und `3*omega=4*c` algebraisch zu H007(B8). H013/H014(11a) und
H007(B40) verbinden dies mit `2*alpha3=N3`.

In dieser Formel fehlen aber die fuer H006/H004/H010 charakteristischen
`xi`-Teilausdruecke. Der H007-Rueckverweis uebernimmt `N1/N2`, fuehrt die
weiteren `N_i` jedoch neu ein. Darum ist dies eine positive Bruecke nur
innerhalb der neuen N3-Familie, nicht rueckwaerts zur alten Formel. Details:
[ALPHA3_MANUSCRIPT_ORIGIN_REVIEW](ALPHA3_MANUSCRIPT_ORIGIN_REVIEW_2026-09-06.md).

## 4. Drei verschiedene Alpha-Rollen

Die folgenden Symbole duerfen nicht ineinander umbenannt werden:

| Rolle | Bedeutung in der geprueften Kette | Versionshinweis |
|---|---|---|
| nacktes `alpha` | Feinstrukturkonstante bzw. eingesetzte Kopplungsgroesse innerhalb weiterer Formeln | H006 gibt sie zuvor durch (V) vor; H010 setzt aktiv `1/137.03599976`; H004 verwendet sie in der `alpha3`-Konstruktion |
| `alpha3` | Koeffizient der dritten Konfigurationszone; in alter Form aus `f-qF`, spaeter ueber `N3/2` | H006(IX) weicht von H004(98c)/H010/H015-Listing ab; H007/H013/H014 bilden eine neue logarithmische Familie |
| `alpha+`/`alpha-` | aus `eta,t` gebildete Massenfaktoren; `alpha+` multipliziert den abschliessenden Massenkoerper, `alpha-/alpha+` tritt in `Phi` auf | Nicht das nackte `alpha` und nicht `alpha3`; ihre Formgleichheit im engen H006/H010-N0-Vergleich beseitigt keine `alpha3`- oder Eingabedifferenz |

Ein passender Massenwert kann weder diese Rollen gleichsetzen noch zwischen
Fassungen, Klammern oder Eingabekonstanten entscheiden.

## 5. Was **nicht** zu einer gemeinsamen Fassung verbunden ist

- H006-Titeljahr, H015-Blattdatum, H015-Listingdaten und H010-Headerangaben
  ergeben keine einheitliche chronologische Edition.
- Formgleichheit H004(98c)--H010--H015-Listing beweist nicht die Gleichheit
  des ganzen Programms, der Konstanten, Rundung oder Zustandsauswahl.
- Die H015-Typoskriptblaetter 4--7 vervollstaendigen nicht die fehlenden
  Blaetter1--3 und authentifizieren nicht automatisch die IGW-Wiedergabe.
- Die bedingte H006/H010-N0-Bruecke gilt nicht fuer Resonanzen, andere
  Teilchen oder den unbekannten allgemeinen `Q_N/Gamma`-Zusammenhang.
- H007/H013/H014 duerfen nicht nachtraeglich als Erratum oder Herleitung von
  H006/H004/H010 importiert werden.
- H004s empirisch gewaehlte Koeffizienten duerfen nicht als aus der
  Metronik eindeutig erzwungen ausgegeben werden.
- Kein Formular darf nach Naehe zur Elektronenmasse zur „historisch
  richtigen“ Version erklaert werden.

## 6. Alte Aussagen, die nicht wiederholt werden duerfen

Nach den Etappen 16--23 sind insbesondere folgende Kurzschluesse ueberholt
oder zu stark:

1. **„`(0110)` ist das Elektron-Besetzungstupel.“** Nein: Es ist die
   Multiplett-Konfigurationssignatur; das N0-Tupel wird separat generiert.
2. **„Der H006-Elektronfall ist mangels `n` prinzipiell nicht rechenbar.“**
   Zu stark: Fuer genau diesen N0-Knoten ist `n=(0,0,0,0)` quellenintern
   bedingt geschlossen; ein literal gespeicherter Tabellensatz fehlt.
3. **„H006 und H010 unterscheiden sich nur durch Konstanten oder
   Rundung.“** Falsch: Zwei wertaktive `alpha3`-Formelunterschiede sind
   statisch belegt.
4. **„Die H010-`alpha3`-Form ist erst eine spaete Pascal/C-Aenderung.“**
   Nicht mehr haltbar: H004(98c) und das datumsbezeichnete H015-Listing
   zeigen dieselbe Gestalt. Das datiert dennoch nicht ihren Ursprung.
5. **„Alle H006-Wiederholungen besitzen den ungruppierten Exponenten.“**
   Falsch: In der geprueften Kette weicht nur (XIV) ab; selbst
   (XXVII)/(XXIX) sind hochaufgeloest gruppiert.
6. **„Damit ist ein H006-Druckfehler oder dessen Urheber bewiesen.“** Nein:
   Die lokale Inkonsistenz und die gruppierte Vergleichsfassung sind belegt,
   nicht ihre Entstehungsursache oder ein autorisiertes Erratum.
7. **„H015 ist die vollstaendige authentifizierte 1982-Urschrift bzw. das
   vollstaendige Originalprogramm.“** Nicht belegt: Es ist ein heutiger
   Scan fotografierter, unvollstaendiger Artefakte mit sichtbaren
   Datums-/Zuschreibungsangaben.
8. **„H007/H013/H014 entscheiden die alte alpha3-Klammer oder Wurzel.“**
   Nein: Ihre logarithmische `N3`-Form ist strukturell eine andere Familie.

## 7. Enger Schlussstatus

Die historisch naehere Quellenlage ist heute besser als vor Etappe16:
Besetzung, Massenkoerper, `alpha3`-Gestalt und Auswahl-/Grenzexponent haben
jeweils konkrete lokale Anschluesse. Gerade diese Fortschritte verbieten
aber eine Mischfassung: Jede Rechnung oder Erklaerung muss Quelle,
Formelstand, Eingabekonstanten, Indexkonvention und eigene Normalisierung
separat nennen.

Der belastbare Stand ist deshalb keine restaurierte „1982-Gesamtformel“,
sondern eine **Matrix begrenzter Bruecken mit dokumentierten
Versionsgrenzen**. Eine weitere Zusammenfuehrung braucht eine konkrete
Originalseite, ein autorisiertes Erratum oder eine vollstaendige
Ueberlieferungskette; Formgleichheit und Datumsnaehe allein reichen nicht.
