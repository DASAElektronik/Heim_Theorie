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

Stand 2026-09-06, Etappe 35:
[A-Sensitivitaet](06_docs/DECAY_SENSITIVITY_2026-09-06.md).
Vier vorab festgelegte Zellen vergleichen Heims heuristische Buchwahl
`A(k=1)=1/3` mit der eigenen z3-Sensitivitaet `A(k=1)=1/5`, jeweils fuer
beide alten Buch-Alpha-Profile. Externterm und Geruestreferenz `g/W`
werden gemeinsam geaendert; alle uebrigen Groessen bleiben innerhalb des
jeweiligen Alpha-Profils fest.

Bei `1/3` bleibt die ordinary-floor-Ausgabe `(14,9,13,7)` mit direkter
Bandbreite `(2459,-10,6)`. Bei `1/5` erreicht die Vorwaertsauswahl
`(N1,N2,N3)=(14,10,1)`, aber der reelle vierte Wert liegt oberhalb der
Strukturkappe: Sattigungsgrenze, keine erfundene `N4`-Ausgabe. Eine frische
endliche Suche findet in keiner der vier Zellen eine exakte Loesung mit
den direkten nichtkollabierten Gates; die enge vorab deklarierte und die
volle reelle `0<=N4<N3`-Diagnose werden getrennt berichtet. Keine Masse,
kein A-/Y-/Restfit und keine neue Heim-Fassung. 15 neue Tests,331 insgesamt;
45 Befundgruppen, nicht45 Fehler. Weiter: die gedruckte Buch-Sattigungsregel
im erreichten z3-Zweig anwenden und ihren Gleichungserhalt separat pruefen.
[Wiedereinstieg](00_admin/RESUME.md), [Arbeitsfolge](00_admin/UNDERSTANDING_ROADMAP.md).

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
