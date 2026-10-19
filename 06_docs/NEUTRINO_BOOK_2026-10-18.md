# Buch-Neutrinozustände: begründeter Filter, bedingte Verträglichkeit

2026-10-18, Einheit51. [Vertrag](../00_admin/NEUTRINO_BOOK_PLAN.md).
Anschluss an49/50, keine neue Neutrinomassenrechnung.

## Was sich präzisiert hat

Der in49 als zusätzliche Portentscheidung gegenüber H007 beschriebene
Filter ist im Buch H004 sachlich anschließbar: Dort wird gerade Parität
von P+Q für positive Feldmasse gefordert, und k=2 wird für die diskutierte
freie Strahlung unter einer Erhaltungsannahme ausgeschlossen. Der Filter
ist damit nicht ohne Quellenmotiv. Die gesamte C-Ausgabe ist dadurch
aber noch nicht mit dem Buch oder B65 identisch.

H004 führt außerdem eine konkrete experimentelle Referenz an. Sie
stützt eine historische Verträglichkeitsaussage mit einer Obergrenze,
keinen gemessenen Treffer bei Heims Tabellenwert. Zwischen Heims
Feldkatalyt-Begriff und dem dort begrenzten Massenparameter fehlt im
geprüften Buchabschnitt weiterhin eine quantitative Messgleichung.

## Quellenumfang

H004 Druck351–354/PDF357–360 vollständig visuell gelesen. Zusätzlich
Tabellenanhang Druck376/PDF381 vollständig gelesen. Der Seitenversatz
ist im Anhang anders; deshalb beide Locator angeben. Neue Arbeitsbilder
mit Poppler150dpi; Tabellenanhang aus dem vorhandenen Vollseitenrender.
Unveränderter H004-SHA256:
`f094f56ec81d22d17c21c93ba248705dd79100828b813c72682f6a6605593849`.

M007 ist die auf Druck354/Fußnote5 angegebene Publikation PRL50(1983)474.
Bibliografie und APS-Abstract öffentlich ermittelt. Der Volltext konnte
über die geprüften Publisher-URLs nicht geladen werden; keine Volltext-
oder Methodenprüfung behauptet. Der bei INSPIRE gespeicherte APS-Abstract
erhielt die im Webauszug verlorenen mathematischen Symbole. Einzelnachweis
und Zugriffsgrenze: [Metadaten](../05_analysis/neutrino_book_sources.json).

## Vom leeren Zustand zur eingeschränkten Strahlungsliste

H004351 diskutiert zunächst den hypothetischen neutralen e0-Zustand und
unterscheidet ihn von einer leeren Struktur n_j=−Q_j. Auf352 setzt die
Quelle für die Neutrinointerpretation q_x=0. Sie führt elf mögliche
Strukturen auf; das ist weder die Fünferliste aus H007 noch die aktive
Dreier-Namensliste des C-Ports.

In118a steht `m(nu_x)=mu*alpha_plus*phi_(q=0)`. Die Quelle behauptet,
dass bei leerer Struktur K+H+F verschwinden, der Feldterm aber bleibt.
Auf352 folgt die Positivitätsbedingung P+Q gerade. Auf353 wird der
Ausschluss freier k=2-Strahlung ausdrücklich an die Erhaltung von k
geknüpft; der Text diskutiert Protonenzerfall als möglichen Gegenfall.
Das ist eine bedingte damalige Argumentation, keine hier aktualisierte
Aussage über heutige Experimente.

Unter dieser Einschränkung nennt das Buch freie nu_e, nu_mu und nu_pi.
Es führt außerdem einen additiven beta-Anteil mit Zerlegung in Raumspin-
und Isospinanteil ein. Die Buchbezeichnung nu_pi ist keine Schreibweise
für tau-Neutrino. Auch die elf ursprünglichen Möglichkeiten, die drei
weiter diskutierten Strukturen und die zusätzlichen beta-Komponenten
dürfen nicht als austauschbare Zustandszählungen behandelt werden.

Der C-Filter `k==1 && (P+Q)%2==0` hat damit einen Anschluss an352/353.
Er prüft jedoch selbst nicht q_x=0, und die aktive Namensliste enthält
Elternzustände mit q_x=−1. Zudem verwendet der Port den extrahierten
Eltern-Feldterm. Aus dem Filter allein folgt daher weder die Leerraum-
operation des Buchs noch die B65-Definition aus H007. Die begrenzte
Nichtgleichheit aus50 bleibt unverändert.

## Behauptete Oszillation und Ausdrucksgrenze

118b setzt phi_R=phi_P=B_nu und phi_beta=2B_nu. 118c beschreibt
eine reversible Zerlegung `nu_beta <-> nu_P + nu_R`. Auf354 wird
daraus ein scheinbarer Wechsel zwischen einfacher und doppelter
Feldmasse erläutert. In den geprüften Seiten fehlen eine Zeit-/Längen-
abhängigkeit, Übergangswahrscheinlichkeit und Ankopplung an Präparation
oder Detektion. Das Wort Oszillation allein liefert diese Größen nicht.

Der Anhang376 druckt nu_R=2,003, nu_P=2,03 und nu_beta=4,006 in
der eV-Gruppe. Die beiden ersten Druckwerte sind trotz118b nicht gleich;
der zweite wird hier nicht still zu2,003 korrigiert. Die Werte der übrigen
Gruppe stehen in keV, insbesondere nu(e0)=5,375675, nu_mu=11,28781
und nu_pi=1,441793. Diese Angaben sind transkribierte Buchwerte,
keine in dieser Einheit reproduzierten Ergebnisse oder moderne Massen.

## Der konkrete experimentelle Verweis

Die Fußnote führt zu T.Kirsten, H.Richter und E.Jessberger,
*Rejection of Evidence for Nonzero Neutrino Rest Mass from Double Beta Decay*,
PRL50,474–477(1983), veröffentlicht14.02.1983,
[DOI/Publisher](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.50.474).
Der APS-Abstract beschreibt eine Neubestimmung des Zerfallsratenverhältnisses
von128Te und130Te. Das Ergebnis ist mit verschwindendem untersuchtem
Massen-/Beimischungsparameter vereinbar; unter der dortigen Majorana-
Auswertung wird eine Obergrenze von ungefähr5,6eV bei95% angegeben.
Es handelt sich nicht um die Messung einer positiven Masse von4,006eV.

Rein arithmetisch liegt4,006 unter5,6. Dieser Vergleich wäre nur dann
ein physikalischer Verträglichkeitstest, wenn die beiden Größen samt
Modellannahmen zulässig identifiziert werden können. Eine solche
Überleitungsformel wird auf H004354 nicht geliefert. Heims Formulierung
der Verträglichkeit ist deshalb weder als gemessene Bestätigung noch
umgekehrt allein durch den ablehnenden Artikeltitel als Widerlegung zu
behandeln. Die Publikation richtet sich gegen früher behauptete Evidenz
für eine von null verschiedene Masse; ihre Grenze lässt kleinere Werte zu.

## Konsequenz für die Forschung

Es gibt jetzt einen konkreteren Weg zur Prüfung: H004118a/118b und
die angegebene Feldmasseninterpretation getrennt von H007/B65 behandeln;
die bereits sichtbaren Eingriffe des Ports nicht zur Messdefinition erheben.
Für den historischen Messanschluss fehlen der vollständige M007-Methodenteil
und eine Heim-seitige Gleichung zur experimentellen Größe. Diese Lücke
wird nicht durch einen modernen Grenzwert oder eine Namensänderung ersetzt.

FIND-057 hält Quellenanschluss und Grenze gemeinsam fest. Die bekannte
Portdifferenz wird nicht erneut als unabhängiger Fehler gezählt. Reine
Quellen-/Metadatenprüfung: Rechenstand weiterhin381 erfolgreiche Tests;
keine Veränderung der bisherigen numerischen Ergebnisse.
