# Neutrino-Größen: Quellenbegriff und C-Ausgabe sind getrennte Verträge

2026-10-18, Einheit 49, [Prüfvertrag](../00_admin/NEUTRINO_OBSERVABLE_PLAN.md).
Statischer Quellenvergleich; keine neuen Teilchenmassen oder Messdaten.

## Ergebnis

H016 bezeichnet seine Neutrinozustände ausdrücklich weder als Ruhemassen
noch als freie photonartige Feldenergie. H007 erläutert eine verwandte
Feldgröße bei leerer Zonenbesetzung und nennt fünf mögliche Zustände.
Eine direkte experimentelle Messvorschrift ist in den hier geprüften
Abschnitten nicht angegeben. Eine Zahl in eV allein schließt diese Lücke
nicht. Die Quelle darf dadurch weder gegen passende Messdaten bestätigt
noch gegen unpassende Messgrößen widerlegt werden.

H010 C0.66 ersetzt die fünf Namen im aktiven Präprozessorzweig durch
eigene e-/μ-/τ-Bezeichnungen. Seine Speicherbedingung und seine
Feldgrößenberechnung sind weitere Entscheidungen. Sie sind keine
unveränderte Wiedergabe der fünf H007-Zustände. Zudem sind die aktiven
μ-/τ-Feldgrößen im betrachteten Code algebraisch gleich, sofern beide
berechnet und gespeichert werden. Dies ist eine Aussage über diese
Implementierung, keine berechnete Naturvorhersage.

## Quellenumfang

- H016 PDF9, interne Seite8, erneut vollständig visuell gelesen. Der
  Grundtext trägt1995; spätere Bearbeitungsspuren sind bereits in45
  getrennt dokumentiert. Verlangt werden leere Zonen und verschwindender
  elektrischer Ladungszustand im Bereich k=1. Der Ausdruck Feldkatalyt
  wird ausdrücklich metaphorisch eingeführt.
- H007 PDF1 (Deckblatt),9/10 (Druck18/19) vollständig visuell gelesen.
  Deckblatt: Redaktion nach einem1989-Manuskript, IGW2002; Seitenkopf2003.
  Die physikalische Realisierung der zusätzlichen Zustände bleibt im
  Text ausdrücklich unentschieden.
- H010 C0.66 statisch: Zeilen126–173 Namensdeskriptoren und `#if 0`,
  984–1028 GMASS, 1241–1303 Aufrufe und beide Speicherfilter;
  `gprogin.dat` vollständig auf Datensatzbereich und Zustände gelesen.
  Kein Fremdprogramm gestartet. Ausgabe einer älteren C-Fassung nicht
  als Ausführung dieses Codes behandelt.

H007 SHA256: `0e2f646d784152fb008944f58e1b8e709a416b65265d2fb75d3cc44c88ff8a40`.
H016 SHA256: `a2acd1ac9ce0e2d1974216b04f1c701c3395321955dd990588e46080faaf103d`.
C-Dateihash und relativer Pfad stehen im [Bericht48](XI_DOWNSTREAM_2026-10-18.md).

## Definition in H007

B63 setzt die vier Besetzungsgrößen auf die negativen Gerüstwerte:
`n=-Qn, m=-Qm, p=-Qp, sigma=-Qsigma`. Das ist kein gewöhnlicher
besetzter Grundzustand N=0. Die Quelle erhält in B65

`M_nu = mu * alpha_plus * (Phi + varphi_0)`.

`varphi_0` bezieht B49 auf die unteren Schranken. Die Aussage lautet
Feldmasse ohne ponderable Korpuskel, mit einer Interpretation über
übertragene Quanteneigenschaften und Erhaltungsprinzipien. Im selben
Abschnitt stehen mögliche empirische Zuordnungen für beta- und
mu-Neutrino; diese Interpretation ersetzt keine Messgleichung.

Die nachfolgende Tabelle gibt die Quelle wieder. Sie identifiziert die
Indizes1–5 nicht mit heutigen Masseneigenzuständen oder Flavorindizes.

| H007-Zustand | k,P,Q,KAPPA | Quellenaussage | C-Speicherfilter würde zulassen? |
|---|---|---|---|
| nu1 | 1,0,1,0 | mögliche beta-Neutrino-Interpretation | nein: P+Q ungerade |
| nu2 | 1,1,1,0 | mögliche mu-Neutrino-Interpretation; gleicher Quellwert auch1111 | ja |
| nu3 | 1,2,0,0 | mögliche weitere Realisierung offen | ja |
| nu4 | 2,1,1,0 | mögliche weitere Realisierung offen | nein: k ungleich1 |
| nu5 | 2,1,1,1 | mögliche weitere Realisierung offen | nein: k ungleich1 |

Die letzte Spalte ist nur die Auswertung der Bedingung
`k == 1 && (P+Q)%2 == 0`, kein Nachweis eines Programmlaufs oder der
Erreichbarkeit jeder anderen Programmstelle. H016s enger Bereich k=1
beweist seinerseits nicht die zusätzliche Paritätsbedingung des C-Codes.

## Was C0.66 tatsächlich auswählt

Die fünf Deskriptoren `neutrino1` bis `neutrino5` stehen in Zeilen161–166
unter `#if 0` und sind damit in dieser Datei ausgeschaltet. Der aktive
`#else`-Zweig enthält:

| Aktiver Name | Deskriptor | Bedeutung im Code |
|---|---|---|
| e-neutrino | `1110#100#1` | Feldgröße des neutralen1110-Elternzustands |
| mu-neutrino | `1111#1-10#1` | Feldgröße eines1111-Elternzustands mit QX=−1 |
| tau-neutrino | `1111#1-10#1@2` | derselbe Elternzustand, Anregungskennzeichen2 |

Der Name e-neutrino liegt damit auf dem Tupel der H007-Zeile nu2,
nicht auf nu1. Der Code kommentiert diese Liste als Versuch einer
anderen Neutrinodefinition. Das QX im Deskriptor gehört zum ausgewerteten
Elternzustand; es beweist keine elektrische Ladung des damit benannten
Neutrinos. Gerade diese Überleitung ist zu begründen.

Auch eine aktive Namensliste garantiert keine Ausgabe: Die lokale
`gprogin.dat` wählt zunächst nur Datensatz1 (Pi-Zustand). Die weiteren
Datensätze einschließlich nue1 stehen zwar in der Datei, liegen aber
außerhalb dieses eingestellten Bereichs. Für eine Reproduktion muss der
konkrete Start-/Endbereich als Eingabe festgehalten werden. Diese Datei
wurde nicht verändert; daraus wird kein früherer tatsächlicher Lauf abgeleitet.

## Berechnete Feldgröße und die μ-/τ-Gleichheit

GMASS berechnet zunächst FIG im regulären Elternzustand und setzt dann

```text
fik = fig - 4*kq*alfm/alfp
am_field = amu*fakMeV*alfp*fik
```

Der Code wertet dafür nicht einfach erneut die vollständige H007-Formel
bei allen vier unteren Schranken aus. Die Gleichsetzung des extrahierten
Terms mit B65 verlangt einen eigenen Fassungs-/Formelvergleich. Der
1982-nahe Port und H007/B49/B65 sind nicht allein wegen ähnlicher
Symbolnamen identisch.

Eine engere Folgerung ist schon jetzt möglich: In der statisch gelesenen
FIG-Zeile kommt die variable Zonenbesetzung nur im Faktor
`1 + Q*(1-kappa)*(2-k)*n1/q1` vor. Für beide aktiven μ-/τ-Deskriptoren
ist KAPPA=1; der Faktor wird1. Alle übrigen FIG-Eingaben und die
Subtraktion für FIK sind bei diesen beiden Deskriptoren gleich. Daher
bleibt `am_field` bei den unterschiedlichen N-Werten gleich, soweit
die Auswertung wohldefiniert ist. Die gesamte Elternmasse `am` enthält
zusätzlich KGH und ist von dieser Aussage ausdrücklich nicht erfasst.

Das erklärt, warum die drei aktiven Namen nicht schon drei unabhängige
Neutrino-Massenvorhersagen begründen. Es wurde weder eine Masse angepasst
noch ein experimenteller Wert zum Ableiten dieser Gleichheit verwendet.

## Offene Messbrücke und nächster konkreter Vertrag

Vor einem Messvergleich fehlen im geprüften Ausschnitt mindestens die
Definition der beobachteten Größe, die Zuordnung der Quellzustände zu
den experimentell präparierten/detektierten Zuständen und eine Gleichung,
die die Feldgröße auf das jeweilige Messergebnis abbildet. Die bloße
Umbenennung eines Deskriptors liefert diese Verbindung nicht. Dies ist
ein begrenzter Quellenbefund, kein werkweiter Nichtexistenzbeweis.

Nächster prüfbarer Schritt: B49/B65 vollständig gegen den C-Ausdruck
FIK bei den deklarierten unteren Schranken vergleichen. Erst diese
interne Gleichheitsfrage lösen; anschließend gezielt nach einer
Messgrößenzuordnung im Originaltext suchen. Keine moderne Residualtabelle
und kein willkürlich gewählter Ersatzvertrag. Bestehende55 Befunde und
377 Tests bleiben unverändert; diese Einheit ergänzt zunächst den
Quellen-/Zuordnungsbericht, ohne eine weitere Fehlerzählung anzulegen.
