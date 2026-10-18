# Heims Theorie

Arbeitsordner fuer eine nuechterne Rekonstruktion und Pruefung von Burkhard Heims Theorie.

## Ziel

Wir behandeln Heim nicht als Glaubensfrage, sondern als Audit:

1. Primaerquellen und spaetere Rekonstruktionen sauber trennen.
2. Behauptete Formeln und Rechenschritte reproduzierbar machen.
3. Heims Zahlen mit heutigen Referenzdaten vergleichen.
4. Freie Parameter, Annahmen und unklare Schritte dokumentieren.
5. Nur dann ueber experimentelle Signaturen sprechen, wenn eine formale Rekonstruktion traegt.

## Leitfrage

Kann aus Heims Original- bzw. nahen Quellen eine reproduzierbare, parameterarme Berechnung von Teilcheneigenschaften gewonnen werden, die heutigen Messdaten standhaelt?

## Struktur

- `00_admin/`: TODO, Fortschritt, Entscheidungen, offene Fragen.
- `01_sources/`: Quellenregister und spaeter lokale Kopien/Notizen zu Heim-Texten und Sekundaerliteratur.
- `02_raw_data/`: Referenzdaten aus PDG, NIST/CODATA, HEPData und CERN Open Data.
- `03_notes/`: Lese- und Exzerptnotizen.
- `04_reconstruction/`: Formale Rekonstruktion, Formelbibliothek, Gleichungen, Implementierungen.
- `05_analysis/`: Vergleiche, Fehlerrechnung, Parameterzaehlung.
- `06_docs/`: Unsere laufende Dokumentation und Zusammenfassungen.
- `07_outputs/`: Tabellen, Plots, Reports.
- `scripts/`: Hilfsskripte fuer Datenimport und Auswertung.

## Arbeitsprinzipien

- Primaerquelle vor Kommentar.
- Jede Zahl bekommt Herkunft, Einheit, Unsicherheit und Datum der Quelle.
- Jede Formel bekommt eine eindeutige Referenzstelle.
- Unklare Schritte werden markiert, nicht geglaettet.
- Keine Vermischung von Heim, Heim-Droescher, Ludwiger, Fan-Auslegung und moderner Rekonstruktion.
- Heims belegte Grundideen bleiben ihm zugeschrieben; unsere Rekonstruktion
  und eigene Erweiterungen werden nach dem [Zuschreibungsgrundsatz](00_admin/SOURCE_ATTRIBUTION.md) getrennt ausgewiesen.

## Aktueller Arbeitsmodus

[Grafischer Überblick als PDF](output/pdf/Heim_Audit_Ueberblick_2026-10-18.pdf)
und [drei Grafiken mit Erläuterungen](07_outputs/figures/README.md)
fassen die Etappen39/40 zusammen. Die PDF ist eine datierte Übersicht;
die vollständigen Quellen- und Rechendetails stehen in den Berichten.

Stand 2026-10-18, Etappe50:
[B65 und C-Feldextraktion algebraisch getrennt](06_docs/NEUTRINO_FIELD_BRIDGE_2026-10-18.md):
Eine quellenbelegte Gleichheit zweier Zustände bleibt im projizierten Port
nicht erhalten. Keine Massenziele eingesetzt; B50 bleibt allgemein offen.
56 Befunde,381 Tests bestanden.

Vorheriger Stand, Etappe49:
[Neutrino-Größen und Port-Zuordnung](06_docs/NEUTRINO_OBSERVABLE_2026-10-18.md):
H007 nennt fünf mögliche Feldzustände; C0.66 verwendet aktiv andere
e-/mu-/tau-Deskriptoren und einen zusätzlichen Speicherfilter. Seine
mu-/tau-Feldgrößen sind algebraisch gleich, sofern beide ausgewertet werden.
Die Zuordnung zu einer Messgröße bleibt offen. Keine neuen Messresiduen;
55 Befunde,377 Tests im unveränderten Rechenstand.

Vorheriger Stand, Etappe48:
[Xi-Folgen und spätere Übertragungen](06_docs/XI_DOWNSTREAM_2026-10-18.md):
Zusätzliche QX-Terme fallen für Xi weg; bei wohldefinierter Auswertung
werden die beiden Massenpfade nur umgeordnet. Ein alter IK4-Vorbestand
verhindert eine pauschale Aussage über jeden Originallauf. Pascal/C
vermeiden den frühen Divisionsverlust bereits.55 Befunde,377 Tests
im unveränderten Rechenstand.

Vorheriger Stand, Etappe47:
[Xi-Integerfehler eingegrenzt](06_docs/XI_INTEGER_2026-10-18.md):
Die vorgezogene Division ergibt0 statt1/2; nur Xi weicht unter zwölf
Grundmustern von der CS-/Ladungstabelle ab. KQ-Eingaben werden vertauscht;
Massenfolgen noch separat zu prüfen.55 Befunde,377 Tests bestanden.

Vorheriger Stand, Etappe46:
[DESY-Bestand nach Dokumenten getrennt](06_docs/DESY_COLLECTION_2026-10-18.md):
127 Fotos gehasht, fünf Formelblätter H015 zugeordnet. Programmfassungen
unterscheiden sich; ein Xi-Korrekturblatt eröffnet eine konkrete Integerprüfung.
54 Befunde, zuletzt373 Tests. [Git-Synchronisierung](00_admin/GIT_SYNC.md):
Push wieder möglich, Pull durch lokale FETCH_HEAD-Schreibsperre begrenzt.

Vorheriger Stand, Etappe45:
[Begrenzte Archivprüfung](06_docs/FS_ARCHIVE_2026-10-18.md): zusätzlicher
1995er Überblick gesichert; Kalibrierung weiter offen. DESY-Seiteninventar
für gezielte Fortsetzung, keine neue Anpassung.54 Befunde;373 Tests im
zuletzt geprüften Rechenstand.

Vorheriger Stand, Etappe44:
[Früher Beleg des Alpha-/Beta-Zahlenpaars](06_docs/ALPHA_LITERAL_ORIGIN_2026-10-18.md).
Ein auf21.12.1981 datiertes Manuskript druckt genau die H015-Eingabewerte.
Die Herkunft ist damit enger belegt; die gemeinsame mathematische Herleitung
bleibt inkonsistent. Der positive Elektronen-Reproduktionstest bleibt erhalten.
373 Tests bestanden. Weiter: konkrete F_S-/Kalibrierungsprovenienz.

## Verlauf: Etappe43

Stand 2026-10-18, Etappe 43:
[Versionsbilanz des Elektronfalls](06_docs/ELECTRON_VERSIONS_2026-10-18.md).
H015-H010-Unterschied durch Skala und Umrechnung nahezu vollständig erklärt;
der dimensionslose Term bleibt nahezu gleich. H006-Lesart und korrigierter
H004-Anhang bleiben eigene Verträge. Weiter: Herkunft der Alpha-Eingabe,
danach bei fehlender Spur F_S-/Kalibrierungsprovenienz.

## Verlauf: Etappe42

Stand 2026-10-18, Etappe 42:
[Elektronen-Grundzustand im fotografierten Programm](06_docs/H015_ELECTRON_2026-10-18.md).
Mit dem eigenen H015-Konstantensatz ergeben sich die gedruckten Besetzungen
und0.5110032557257554 MeV gegenüber0.51100326 im Ausdruck, innerhalb
der angenommenen Druckrundung. Der letzte Ganzzahlschritt ist analytisch
abgesichert; keine historische Compileremulation oder unabhängige physikalische
Vorhersage behauptet.369 Tests bestanden; alte Ergebnisse erhalten.
Weiter: Versionsbilanz desselben Elektronfalls über H006/H015/H010/H004.

## Verlauf: Etappe41

Stand 2026-10-18, Etappe 41:
[Fotografierter Konstantensatz und Ausgabe](06_docs/HISTORICAL_CONSTANTS_2026-10-18.md).
Alle17 geprüften Initialisierungszeilen des H015-FORTRAN-Ausdrucks lassen
sich innerhalb der Druckrundung reproduzieren. Darunter sind feste Eingaben;
ALFA/BETA werden als Kehrwerte zugewiesen, nicht dort aus105 berechnet.
Der Konstantensatz unterscheidet sich vom korrigierten Buchanhang.
Dessen kleine Ladungsabweichung und vollständige Kalibrierung bleiben offen.
364 Tests bestanden; bisherige Profile und datierte Grafiken erhalten.
Weiter: Elektron-N0-Zweig dieses H015-Stands gegen seinen Ausdruck prüfen.

## Verlauf: Etappe40

Stand 2026-10-18, Etappe 40:
[Konstantenkorrektur und Elektronenanker](06_docs/CONSTANTS_ANCHOR_2026-10-18.md).
H004349/371 beschreibt ausdrücklich die Rückrechnung aus gemessener Masse
und Ladung. Der spätere Elektronentreffer ist damit kein unabhängiger Test.
Massenskaleninversion rekonstruiert; c/epsilon0/mu0 bei Druckrundung vereinbar.
Die bedingte29-Editionsbrücke liefert eine kleine Ladungsabweichung zur
Tabelle, keine empirische Widerlegung.360Tests bestanden.
Weiter: originalen Konstantensatz und frühe29-/Tabellenfassung belegen;
vollständige historische Kalibrierung bleibt offen.

## Verlauf: Etappe39

Stand 2026-10-18, Etappe 39: [F_S-Provenienz](06_docs/FS_PROVENANCE_2026-10-18.md).
Die 17 Komponenten sind über101a/b nachgezählt; historische Massen und
Fehler aus PDG1974 als Referenzkandidaten erfasst. Die genaue ursprüngliche
F_S-Eingabeliste bleibt offen. Y41-44=1 ist durch die allgemeine
Tabellenannahme der Einführung belegt, keine unabhängige Deduktion.
Weiter: Konstantenkorrektur nach115 und Elektronenanker des Vermerks371.

## Verlauf: Etappe38

Stand2026-09-07, Etappe38: [Massenformelkette](06_docs/MASS_CHAIN_2026-09-07.md).
Die Zerlegung4sum(alpha_jG_j)=K+F+H und der Übergang von98d/e zu112
über97/phi sind exakt algebraisch bestätigt. Die FunktionF_S wird dagegen
aus empirischen Massen bestimmt und dann durch einen gemeinsamen Ansatz
beschrieben. Keine neue Masse oder Parameterwahl;354Tests bestanden.
Weiter: Provenienz der17 F_S-Punkte und Y41-44-Festlegung.

## Verlauf: Etappe37

Stand 2026-09-07, Etappe 37:
[(108)-Status](06_docs/EQ108_STATUS_2026-09-07.md). H004 druckt (108) als
formale Selektorgleichheit, verbindet den Externterm aber nur
näherungsweise mit (79b)/(79c). Eine diskrete Auswahlregel ist vorhanden;
im eng geprüften Anschluss wurde aber keine finale Restgarantie oder
Kompensation für (108) gefunden. Das ist ein Quellenstatus, kein neuer
unabhängiger Fehler und keine Gesamtwiderlegung.

Grenzwert-/Unsicherheitsaussagen für `F_im`, Koeffizienten und `Y_k` sind
keine allgemeine Toleranz der beiden Seiten von (108). Bei festem Zustand
bleibt `delta F_S=0`; die empirische `F_S`-Bestimmung wird nicht zur
Restreparatur verwendet. Keine neue Masse, Empirie, Eingabe oder
Parameterwahl; die49 Normalisierungs-CSV-Zeilen bleiben unverändert.
FIND-047 bezeichnet 47 Befundgruppen, nicht47 Fehler. Weiter:
Massenformelkette (98d/e)->(112) und `F_S` quellengetreu rekonstruieren,
ohne Kalibrierung oder Zielwertfit.
[Wiedereinstieg](00_admin/RESUME.md), [Arbeitsfolge](00_admin/UNDERSTANDING_ROADMAP.md).

## Verlauf: Etappe 36

[Sättigungsregel](06_docs/SATURATION_2026-09-07.md): Eigene Anwendung auf
den festen1/5-Gegenprobefall ergibt robust `N=(14,10,1,0)`. Direkte
Strukturgates und separate positive Sigma-Größe bestehen; die feste
Skalargleichung bleibt unerfüllt. Keine Massenabweichung daraus abgeleitet.

## Verlauf: Etappe 35

[A-Sensitivitaet](06_docs/DECAY_SENSITIVITY_2026-09-06.md): Vier vorab
festgelegte Zellen vergleichen `A(k=1)=1/3` mit der eigenen
z3-Sensitivitaet `1/5`; Externterm und g/W werden gemeinsam geaendert.
`1/5` erreicht die Sattigungsgrenze, ohne erfundene Fortsetzung. Frische
Integer-/Realpruefungen finden keine exakte Loesung mit direkten
nichtkollabierten Gates. 331Tests,45 Befundgruppen; keine Masse oder
neue Heim-Fassung.

## Verlauf: Etappe 34

[Xi-Ursprung](06_docs/XI_ORIGIN_2026-09-06.md): Heims (96b)-Wert folgt
bedingt aus einer Fibonacci-artigen Folgenklasse. Die eigene exakte
Fehlerhuelle bestaetigt deren schnelle Konvergenz fuer positive Startwerte,
ist aber keine physikalische Externfehlerschranke. Fuer Sigma fordert Heim
denselben Selektor ausdruecklich nicht; die spaetere Wahl der5 bleibt
Heuristik. 12 neue Tests,316 insgesamt; alte Ergebnisse erhalten.

## Verlauf: Etappe 33

Stand 2026-09-06, Etappe 33:
[Externzonennaeherung](06_docs/EXTERNAL_APPROXIMATION_2026-09-06.md).
Heims Nullpunkt- und Geruestnormierung sind explizit; die Wahl A(1)=1/3
wird auf S. 325 heuristisch motiviert. Eine quantitative r-/nu-/N4- und
Fehlerbruecke wurde im geprueften Anschluss nicht gefunden.

Eigene Fehlerrechnung beruecksichtigt Besetzung, Geruest und Nullpunkt auf
beiden Seiten von (108). Kein physikalisches Fehlerbudget erfunden, keine
korrigierte Besetzung oder Gesamtwiderlegung behauptet. 16 neue Tests,
304 insgesamt; 12 alte Ergebnischecks und Zertifikate bestanden.
Naechster enger Auftrag: (96b)-Motivation der A-Auswahl, gegebenenfalls
separat vorab festgelegte Sensitivitaet ohne Rest-/Massenfit.
[Wiedereinstieg](00_admin/RESUME.md), [Arbeitsfolge](00_admin/UNDERSTANDING_ROADMAP.md).

## Verlauf: Etappe 32

Stand2026-09-06, Etappe32: [Gekoppelte Existenz](06_docs/COUPLED_EXISTENCE_2026-09-06.md).
Fuer beide unveraenderten Buchprofile gibt es keine Besetzung, die gleichzeitig
die direkten ungewichteten107-Gates undexakte108 erfuellt (nichtkollabierter
Zweig). Fuenf vollstaendigeFaelle und rationaleIntervallzertifikate,keinFit.
Das iststaerkerals einFehlerdereinzelnenGreedy-Ausgabe,aberkeineGesamtwiderlegung.

16neueTests,288gesamt,12alteSnapshotchecksplusZertifikatscheck,dreiReviews.
HistorischeFrage zuHeimsKenntnis/Lebensendstandbleibtausdruecklichoffen.
NaechsterSchritt: Externzonennaeherung79b/79c ->322/323 ->g/108 samt
gemeinsamerNormalisierung/Fehlergrenze;keineMasse/Y-Fits.
[Wiedereinstieg](00_admin/RESUME.md), [Arbeitsfolge](00_admin/UNDERSTANDING_ROADMAP.md).

## Verlauf: Etappe 31

Stand2026-09-06, Etappe31: [Strukturbehandlung](06_docs/STRUCTURE_HANDLING_2026-09-06.md).
Die gezielte Buch-/Programmpruefung liefert keine belegte Reparatur des
Buchfalls mit beta3=-10. Kollaps bei beta=0 und Sondertransfer3->4 haben
andere Ausloeser. H015/H010-Auswahlroutinen pruefen die direkten107-Gates
nicht; Programmfassungen, Vorbestandfehler und Warnmeldungen bleiben getrennt.
GLIMIT hat verwandte Grenzalgebra, ersetzt aber keinen Einzelzustandstest.

AchtneueTests,272gesamt,12Checks und dreiinterneReviews. KeineMasse/Fitwahl,
alteRechnungen/49CSV erhalten. NaechsterSchritt: eigene gekoppelte
Existenzpruefung beiunveraendertenBuchinputs, zuerst Grenzen/Genauigkeit.
[Wiedereinstieg](00_admin/RESUME.md), [Arbeitsfolge](00_admin/UNDERSTANDING_ROADMAP.md).

## Verlauf: Etappe 30

Stand2026-09-06, Etappe30: [Buch-Pseudosingulett](06_docs/BOOK_PSEUDOSINGLET_2026-09-06.md).
Zwei vor der Rechnung fixierte Buchprofile liefern N_(j)=(14,9,13,7).
Dieser Auswahlausgang verletzt die direkte Strukturbedingung107/107a:
81>91 ist falsch. Der Befund gilt unter dem benannten Buchvertrag,
nicht als Gesamtwiderlegung oder berechnete Myonmasse.
Spaetere sigma-Gewichtung und der Gleichungsrest bleiben getrennte Fragen.

17neueTests,264gesamt,12Rechenchecks; vier interneReviews von dreiAgenten.
Alte Rechnungen und49CSV-Normalisierungen erhalten. Naechster Schritt:
quellenbelegte Behandlung solcher Strukturverletzungen in Buchauswahl und
historischen GSTRUC-Routinen, ohne Konstantenmischung oder Y9-Fitwahl.
[Wiedereinstieg](00_admin/RESUME.md), [Arbeitsfolge](00_admin/UNDERSTANDING_ROADMAP.md).

## Verlauf: Etappe 29

Stand2026-09-06, Etappe29: [Buch-Auswahl](06_docs/BOOK_SELECTION_2026-09-06.md).
Heims Buchvorschrift trennt W5/W6, TRC, Saettigung und Transfer deutlicher
als die Kurzfassungen. Die Vorwaertsauswahl liefert keine zusaetzliche
eindeutige A16-Herleitung und erhaelt die feste Gleichung nicht allgemein.
Eigene skalare Zeugen sind keine vollstaendigen Heim-Teilchenzustaende;
keine neue Masse oder Gesamtwiderlegung.

13neueTests,247gesamt,elfbestehendeChecks; drei interneReviews.
Alte Rechnungen erhalten. Naechster Schritt: buchinterner Eingabevertrag
des aktiven N0-Pseudosinguletts; keine Konstantenmischung oder Y9-Fitwahl.
[Wiedereinstieg](00_admin/RESUME.md), [Arbeitsfolge](00_admin/UNDERSTANDING_ROADMAP.md).

## Verlauf: Etappe 28

Stand2026-09-06, Etappe28: [F16-Bestimmtheit](06_docs/F16_DETERMINACY_2026-09-06.md).
Die Quellenbedingungen bestimmen Rolle und Grenzcharakter, nicht eindeutig
den Zahlenwert A16. Heim benennt die Deduktion in der Einfuehrung selbst
als offenen Auftrag. Berechnung aus109b bei festemY9 bleibt moeglich;
Herleitung und quantitative Naeherungsgenauigkeit sind davon verschieden.
Eigene reduzierte Beispiele sind keine metronischen Heim-Loesungen.

Zehn neueTests,234gesamt,elf bestehendeChecks; drei interneReviews.
Alte Rechnungen erhalten. Naechster Schritt: Buch-Auswahl/Exhaustion340-342,
quellengetrennt vonH006/H015 und ohne neue Masse oder Y9-Anpassung.
[Wiedereinstieg](00_admin/RESUME.md), [Arbeitsfolge](00_admin/UNDERSTANDING_ROADMAP.md).

## Verlauf: Etappe 27

Stand2026-09-06, Etappe27: [A16-Quellenpruefung](06_docs/A16_ORIGIN_2026-09-06.md).
Die Nennerklammer /(5eta) steht im fotografierten FORTRAN und im Buch.
Das Buch fuehrt zusaetzlich Y9 und nennt die Koeffizienten heuristisch
aus empirischen Grundzustandsdaten gewonnen, nicht explizit hergeleitet.
Y9=1 ist dort Tabellenannahme, kein Beweis oder neuer Fitparameter.

Zehn neue Tests,224gesamt,elf bestehende Snapshotchecks bestanden;
drei interne Reviews. Alte Rechnungen unveraendert. Naechster Auftrag:
F16/A16-Bestimmtheit anhand konkreter Quellenbedingungen, keine Masse.
[Wiedereinstieg](00_admin/RESUME.md), [Arbeitsfolge](00_admin/UNDERSTANDING_ROADMAP.md).

## Verlauf: Etappe 26

Stand 2026-09-06, Etappe 26: Der
[Myon-Eingabe-/Auswahlaudit](06_docs/MUON_SELECTION_2026-09-06.md) verbindet
H006x3 mit W und der Ganzzahlregel. Alle zwoelf vorab festen Profile
erreichen(b), K1..3=(14,9,3). Die A16-Slashbindung aendert K4=0 bzw.1;
beide Lesarten hinterlassen einen positiven Gleichungsrest. Keine Masse,
eindeutige Autorenfassung oder Gesamtwiderlegung daraus abgeleitet.

15 neue Tests, 214 insgesamt, elf Snapshotchecks und Quellenkontrollen.
Drei interne Reviews, unabhaengige Hochpraezisionsrechnung; alte Profile
erhalten. 36 Befundgruppen, nicht36 Fehler. Naechster Einzelauftrag:
A16 in fotografiertem H015/angeschlossenem Buch historisch klaeren;
H010-Programme setzen /(5eta), sind aber kein Autoren-Erratum fuer H006.
[Wiedereinstieg](00_admin/RESUME.md), [Arbeitsfolge](00_admin/UNDERSTANDING_ROADMAP.md).

## Verlauf: Etappe 25

Stand 2026-09-06, Etappe 25: Die
[K4/W4-Pruefung](06_docs/K4_W4_SELECTION_2026-09-06.md) trennt Heims
Zaehl-/Sonderfallvorschriften von der exakten Restgleichung. Bei festen
positiven Eingaben ist der reelle Logschritt korrekt; Abschneiden,
Nullrest-Saettigung und W4>1-Rueckschritt erhalten die Gleichung nicht allgemein.
Die Regeln stehen auch im fotografierten H015-Typoskript. Das widerlegt
nicht pauschal eine eigenstaendige diskrete Deutung oder die gesamte Theorie.

FIND-035 ist ein bedingter Befund, keine neue Teilchenmasse oder
Massenfehlergrenze. Drei Reviews, 14 neue Tests, 199 insgesamt sowie
zehn alte Rechen-/Quellchecks bestanden; alte Profile bleiben erhalten.
Naechster vorab benannter Kandidat: H006x3/mu-,N0, zunaechst Komponenten-,
W- und Auswahlvertrag aus der Quelle, noch keine Masse.
[Wiedereinstieg](00_admin/RESUME.md), [Arbeitsfolge](00_admin/UNDERSTANDING_ROADMAP.md).

## Verlauf: Etappe 24

Stand 2026-09-06, Etappe 24: Die
[aktualisierte Verstaendnisbilanz](06_docs/UNDERSTANDING_BALANCE_STAGE24_2026-09-06.md)
fuehrt Etappen 16-23 zusammen. Ein enger H006-N0-Pfad und ein deklarierter
H010-Ausgabevergleich sind reproduzierbar; die zwei untersuchten H010-alpha3-
Termformen haben einen Buch-/Listingbeleg. Das ist keine vollstaendige
physikalische Herleitung oder gemeinsame historische Gesamtfassung.
Drei Reviews trennen Fassungsbruecken, alle 34 Befundgruppen und naechsten Auftrag.
Zehn alte Rechen-/Quellchecks und 185 Tests bestehen; Rechner, Eingaben,
Tests, Snapshots, Register und 49 Normalisierungen sind unveraendert.

Naechster Schritt: H006 S.9, K4/W4-Sonderfaelle und Ganzzahlregel auf
Gleichungserhalt, Rest und Strukturbedingungen pruefen. H015 PDF42 getrennt
vergleichen; keine neue Massenzahl oder still geaenderte Formel.
[Wiedereinstieg](00_admin/RESUME.md), [Arbeitsfolge](00_admin/UNDERSTANDING_ROADMAP.md).

## Verlauf: Etappe 23

Der
[historische Exponentenvergleich](06_docs/HISTORICAL_EXPONENTS_2026-09-06.md)
belegt dieselbe gruppierte Form in der allgemeinen Auswahlregel und im
N0-Fall des fotografierten H015-Typoskripts. In der geprueften H006-Kette
weicht nur XIV ab. FIND-027 bleibt deshalb ein lokaler Befund zur
IGW-Wiedergabe; keine pauschale Zuschreibung an die Heim-Urschrift.
Basisanstieg und Logarithmusschritt passen zur gruppierten Form, ohne
Formelwahl nach Massentreffer. Fehlerursache und autorisiertes Erratum offen.

Die [Potentialpfadpruefung](06_docs/POTENTIAL_PATHS_2026-09-06.md) und
[Operatorpruefung](06_docs/METRONIC_STEP_2026-09-06.md) bleiben mit ihren
Voraussetzungen erhalten: getrennte H/G-Kanaele sind belegt, ihre
Zwischenpfade und Operatorzuordnung nicht rekonstruiert.
Zehn Rechenchecks und 185 Tests bestehen. FIND-027 wurde praezisiert,
keine neue Gruppe hinzugefuegt: 34 Befundgruppen sind keine 34 Fehler.
Alte Rechner, Eingaben, Snapshots und 49 CSV-Normalisierungen unveraendert.
Keine neue empirische Bestaetigung oder Gesamtwiderlegung.

Naechster Schritt: Verstaendnis-/Versionsbilanz Etappen16-23 zusammenfuehren,
belegte Anschluesse und verbleibende Herleitungsluecken trennen.
H/G-Pfade erst bei neuer konkreter Kanal-/Operatordefinition wieder aufnehmen.
[Wiedereinstieg](00_admin/RESUME.md), [Arbeitsfolge](00_admin/UNDERSTANDING_ROADMAP.md).

## Verstaendnisbilanz der Etappe 15

Die
[Verstaendnisbilanz](06_docs/UNDERSTANDING_BALANCE_2026-09-06.md) fuehrt den
bisher untersuchten Alpha-/Konfigurations-/Massenformel-Ausschnitt zusammen.
Sie trennt Quellenlesung, Rechnung, physikalische Herleitung und empirische
Pruefung. 26 Befundgruppen sind keine 26 Fehler und keine Gesamtwiderlegung.
Acht Rechenchecks und 98 Tests bestehen; die 49 Normalisierungen bleiben
unveraendert (47 resolved, 2 blocked).

Der damals vorbereitete Schritt war ein Eingabeblatt fuer die e--Komponente des
x2-Multipletts bei N=0 in H006. Das gedruckte 0110 sind
Konfigurationsmerkmale, nicht die Besetzungszahlen n1..n4. Ein gegebenes Tupel auszuwerten ist
von seiner Herleitung durch die Auswahlregel zu unterscheiden. Die damalige
Eingabeluecke ist durch Etappe 16 fuer den engen N0-Pfad geschlossen,
nicht fuer die allgemeine Massen- oder Resonanzrechnung.

[Wiedereinstieg](00_admin/RESUME.md),
[Arbeitsfolge](00_admin/UNDERSTANDING_ROADMAP.md),
[N0-Eingabevoraussetzungen](04_reconstruction/alpha_audit/reviews/UNDERSTANDING_N0_READINESS_REVIEW_2026-09-06.md).

## Verlauf: erste neun Etappen

Die folgenden Test-/Befundzahlen und naechsten Schritte sind historisch;
fuer den aktuellen Stand gelten die Bilanz und der Wiedereinstieg oben.

Stand 2026-09-06: Der erste isolierte Alpha-Audit ist ausfuehrbar und unabhaengig
geprueft. [Ergebnisbericht](06_docs/ALPHA_AUDIT_2026-09-06.md),
[Ausfuehren](04_reconstruction/alpha_audit/README.md),
[Wiedereinstieg](00_admin/RESUME.md).

Die zweite Etappe verfolgt die Buchherleitung, trennt offene Annahmen und
prueft Y3-Rueckrechnung sowie Rechenpraezision; insgesamt 23 Tests bestehen.
[Buchbefunde](06_docs/BOOK_TRACE_2026-09-06.md),
[Verstaendnisplan](00_admin/UNDERSTANDING_ROADMAP.md).
Neuere Arbeiten auf Widerlegung zu pruefen ist als spaetere Phase vorgesehen:
zuerst die Herleitung und physikalische Bedeutung verstehen.

Die dritte Etappe reproduziert Heims vorlaeufige Alpha-Naeherung, klaert
die Buch-Indexreihenfolge und dokumentiert einen lokalen Energieordnungs-
widerspruch. [Schrittweise Erklaerung](06_docs/CHARGE_DERIVATION_2026-09-06.md).
33 Tests bestehen; Annahmen und Korrekturkandidaten sind gesondert markiert.

Die vierte Etappe verfolgt Energie, Masse und Wellenlaenge vor(105).
Sie trennt Heims pc von konventioneller Bewegungsenergie sowie h/(mc) von
h/p und zeigt den Einfluss dieser Annahmen auf die Alpha-Gleichung.
[Erklaerung und Quellen](06_docs/ENERGY_KINEMATICS_2026-09-06.md).
44 Tests bestehen; unabhaengige Reviews abgeschlossen. Keine fertig begruendete
Alternativtheorie: Kinematik, Kreisgeometrie und Energiezuordnung bleiben offen.

Die fuenfte Etappe findet Heims eigene Motivation: Lorentz-/Wellenargument
fuer pc sowie die bekannte Alpha-Abweichung und das duale Elektronenbild
fuer die Bindungskorrektur. [Warum-Bilanz](06_docs/AUTHOR_RATIONALE_2026-09-06.md)
trennt Motivation von fehlenden Herleitungsschritten. Exakte Boostdiagnosen
und ein neuer lokaler Matrixdruck-Befund sind unabhaengig geprueft;56 Tests.
Eine auf21.12.1981 datierte Manuskriptfassung liefert einen weiteren
direkten Beleg fuer die Motivation; ihre Unterschiede zur Buchfassung
und die Grenzen der Scan-Provenienz bleiben ausdruecklich dokumentiert.

Die sechste Etappe prueft moegliche Ergaenzungen der Kreiswelle:
[Wellen-Schliessung](06_docs/WAVE_CLOSURE_2026-09-06.md). Das eigene skalare
Ringproblem liefert ganzzahlige Moden, keine automatische Auswahl N1 oder
Heim-H-Eigenloesung. Phase-/Impulsidentifikation und Versionsunterschiede
der A_k bleiben getrennt.69 Tests und drei unabhaengige Reviews; keine
angefittete Verbesserung oder pauschale Widerlegung der Gesamttheorie.

Die siebte Etappe findet eine bedingte quelleninterne Geschwindigkeitsbruecke:
H-Stabilitaet ergibt w=c; fuer den strukturellen Fluss gilt w_f=w.
Die Objekt-/Phasenzuordnung bleibt offen. C=A1*A2 und Y3=1 sind eine
berechenbare Spezialisierung, nicht vollstaendig unabhaengig hergeleitet.
[Bilanz und Erklaerung](06_docs/CYCLIC_FLOW_AND_FINDINGS_2026-09-06.md),
[13 Befundgruppen](04_reconstruction/alpha_audit/FINDING_REGISTER.json).
Das Register enthaelt auch positive Befunde und eigene Diagnosen: keine
Fehlerzaehlung. Naechster Block: L*Delta=k und Auswahlregel (98a).

Die achte Etappe verbindet Konfigurationszahl, Ladung und Alpha in einer
[Zusammenhangskarte](04_reconstruction/alpha_audit/CONFIGURATION_DEPENDENCIES.md).
Die [Auswahlpruefung](06_docs/CONFIGURATION_SELECTION_2026-09-06.md) findet
einen lokalen Umformungskonflikt und u2=1.963489... statt des gedruckten
Bereichs 2..3; globale Maxima und beide Buch-Alpha-Paare bleiben jedoch erhalten.
Die 1989-eta22-Verwendung ist eine separate offene Versionsfrage. 86 Tests,
unabhaengige Reviews und sieben reproduzierte Snapshots; 16 Befundgruppen.
Naechster Querverweis: (79)/(79a) und F/G-Potentialzuordnung.

Die neunte Etappe verfolgt diese Rueckverweise:
[Exponentialkontext](06_docs/EXPONENTIAL_CONTEXT_2026-09-06.md).
Die Abklingrate ist im explizit skalaren Abbild unter a>lambda>0 reproduziert,
einschliesslich Amplitude und Naeherungsfehler. Positive Extremstellen
allein erzwingen diese Parameterwahl nicht; metronische Zusatzregeln bleiben
separat zu pruefen. Die F/G-Potentialzuordnung ist im untersuchten Kontext
weiter spekulativ. 98 Tests, acht Snapshots und 18 Befundgruppen; keine
Gesamtwiderlegung. Naechster Anschluss: Versionsgeltung von 1989 eta22.

## Implementierungsgrenze

Wir bauen zuerst eine Formelbibliothek unter `04_reconstruction/formula_library/`.
Jede Formel bekommt eine ID, Quelle, Status, Abhaengigkeiten, Outputs und Audit-Risiken.
Erst wenn eine Formel `source_checked` und `normalized` ist, soll sie implementiert werden.

Die beiden ALPHA-Bloecke besitzen dafuer explizite Normalisierungsentscheidungen
und den begrenzten Status `audit_implemented`; eine vollstaendige Massenrechnung
bleibt offen.

## Lizenz und Fremdmaterial

Dieses Repository nutzt getrennte Lizenzen:

- Code und Scripts: Apache-2.0, siehe `LICENSE-CODE`.
- Eigene Dokumentation, Rekonstruktions- und Audit-Notizen: CC BY 4.0, siehe `LICENSE-DOCS`.
- Fremdquellen, PDFs, ZIPs, XLSM-Dateien, Scans, OCR-Texte und daraus generierte Bildartefakte sind nicht von diesen Lizenzen umfasst.

Details stehen in `LICENSE` und `THIRD_PARTY_NOTICE.md`.
