# Eta22 und Delta: der konkrete Buchanschluss

Stand: 2026-09-06. Elfte, abgeschlossene Forschungsetappe ab e50cab8.
Auftrag: den konkreten H013-Zustand (q,k)=(2,2) gegen Heims Buchauswahl
pruefen und dabei seine Begriffe und seinen Gedankengang verstehen.

## Ergebnis vorweg

Der entscheidende Anschluss steht bereits im selben Buch: BandII ordnet
die Delta++-Komponente einem Grundmuster mit q=2 und k=2 zu. Direkt neben
der Grundmusterliste verweist Heim ausdruecklich auf die Erfuellung
seiner Auswahl(98a). Wir muessen diesen Anschluss also nicht mehr durch
eine Gleichsetzung mit dem undatierten Typoskript herstellen.

Damit gewinnt ein bekannter Befund an konkreter Reichweite: Die woertlich
gedruckte detaillierte Schranke vor(98a) laesst dieses Paar nicht zu,
obwohl der behauptete Zahlenbereich und die spaetere Buchliste es zulassen.
Die urspruengliche Positivitaetsbedingung wird von (2,2) hingegen erfuellt.
Das ist ein lokales Problem der gedruckten Herleitung, keine Widerlegung
der Existenz von Delta-Teilchen oder der gesamten Heim-Theorie.

## 1. Wie Heim den Zustand einordnet

In der bisher rekonstruierten Buchkette versucht Heim, interne
Ladungsstrukturen und Konfigurationszahlen mit moeglichen Teilchenmustern
zu verbinden. Dabei sind verschiedene Ebenen auseinanderzuhalten:

1. BandII266/267 fuehrt den Faktor eta_qk fuer die interne Ladungsstruktur
   ein. q ist der Ladungsbetrag in Einheiten der Elementarladung, k eine
   positive ganze Konfigurationszahl. k ist hier nicht die Resonanzordnung N.
2. II268/269 bildet Potentialverhaeltnisse und identifiziert diese
   spekulativ mit Beitraegen einer Strukturbedingung. Daraus beansprucht
   der Text eine Auswahl der q/k-Konfigurationen.
3. II287-289 verbindet weitere Invarianten mit Multipletts, also Gruppen
   zusammengehoeriger Grundmuster mit verschiedenen Ladungskomponenten.
4. II290/291 stellt den Bezug zu bekannten Teilchenmustern her. Das ist
   ein Quellenbeleg fuer Heims Zuordnung, noch kein unabhaengiger Beweis
   fuer die Richtigkeit der zugrunde liegenden Konstruktion.

Gerade deshalb ist wichtig, dass die konkrete Zustandsliste und die
beanspruchte Auswahl mathematisch zusammenpassen. Hier tun die drei
gedruckten Herleitungsebenen das nicht durchgaengig.

## 2. Die direkte Quellenkette, ohne Fassungsmischung

Quelle H004: Elementarstrukturen der Materie2, lokale1996-Ausgabe.
Die tragenden Buchseiten wurden visuell gelesen und unabhaengig von
einem zweiten Leser gegengelesen. Das sind mehrere Lesungen derselben
Primaerquelle, keine voneinander unabhaengigen Quellen. PDF-Folios sind
ab1 gezaehlt.

| Buchstelle | Gelesene Verbindung | Bedeutung fuer (2,2) |
| --- | --- | --- |
| Druck287/PDF293, (100a) | abs(q_x)=q | Eine Ladungskomponente vom Betrag2 bedeutet q=2. |
| Druck288/289, PDF294/295, (101)/(101a) | Quartett12: (k P Q kappa)=(2,3,3,0), Ladungen (+2,+1,0,-1) | Die +2-Komponente besitzt k=2 und q=2. |
| Druck289/PDF295, nach(101a) | Ausdruecklicher Rueckverweis auf Erfuellung von(98a) hinsichtlich k und q<3 | Die Liste wird nicht als Ausnahme von der Auswahl eingefuehrt. |
| Druck291/PDF297, (101b) | Quartett12 wird als Delta++,Delta+,Delta0,Delta- bezeichnet; k=B+1 | Die fragliche Komponente ist Delta++. |
| Druck372/PDF377 | Invarianten Delta++=(1330)0(+2) und separate M_x(N=0)-Tabelle | Erneuter Grundmuster-/N=0-Anker, kein blosser N>0-Resonanzeintrag. |

Zwei leicht verwechselbare Notationen: In (101a) beginnt (2330) mit k.
Im Anhang beginnt (1330) mit der Baryonenziffer B; k=B+1 gibt wieder2.
Das dort ebenfalls gedruckte Massentupel (2,1,5,1) bezeichnet dagegen
Zonenparameter und ist keine Definition von eta22. Auch steht eta22 nicht
woertlich neben Delta++; dieser Familienwert folgt durch Einsetzen der
jetzt verbundenen q/k-Indizes in die vorhandene Definition.

## 3. Welche Schranke besteht der Zustand?

Die definierte Familie ist

    eta(q,k) = [1+(4+k)*q^4/pi^4]^(-1/4).

Fuer (2,2) ergibt sie eta22=0.842423846102092834... . Setze fuer die
Auswahlpruefung a=eta(q,0), e=eta(1,0), x=1/eta(q,k). Mit den gedruckten
V/Q-Definitionen aufII268 gilt

    R = V1+Q1-V2-Q2 = a*(x-D),
    B = (1+sqrt(a))^2/(4*e*a) + sqrt(e) - a/sqrt(e),
    D = (1+sqrt(a))^2/(4*e*a) + sqrt(e)/a - a/sqrt(e),
    u_B(q) = (pi/q)^4*(B^4-1)-4.

B,D,R sind unsere klar deklarierten Hilfsnamen. Q2=sqrt(e) hat in der
Quelle keinen q-Index. Die drei Buchzeilen ergeben verschiedene Tests:

| Ebene aufII269/PDF275 | Unter den gedruckten Identifikationen | Fuer (2,2) |
| --- | --- | --- |
| Urspruengliche F/G-Positivitaet | -R>0, also x<D | erfuellt |
| Danach gedruckte V/Q-Ungleichung | R>0, also x>D | nicht erfuellt |
| Danach gedruckte eta-Schranke | x<B, also k<u_B(q) | nicht erfuellt |

Konkret ergibt die unabhaengige Rechnung

    B_2 = 1.18615355896463710288...
    x   = 1.18705091816549861483...
    D_2 = 1.32005047368182700497...

also B_2 < x < D_2. Entsprechend ist

    u_B(2) = 1.963489198102715361...

und k=2 besteht die strikte B-Schranke nicht. Der Buchtext behauptet
dagegen 2<u_2<3. Mit diesem behaupteten Intervall waere k=2 zulaessig.
Die globalen Maxima k_max=2,q_max=3 in(98a) sind nochmals etwas anderes:
Sie widersprechen (2,2) nicht und bleiben als Maxima auch in unserer
B-Auswertung erhalten. Sie erlauben nicht automatisch jedes Paar im
k/q-Rechteck; etwa (3,2) scheitert schon am gedruckten u_3-Intervall.

Hier liegt keine empfindliche letzte Dezimalstelle vor:
x-B_2=+0.0008973592008615... und u_B(2)-2=-0.0365108018972846... .
Eine unabhaengige Machin-pi-Rechnung mit80/120 Stellen bestaetigt die
Entscheidungen und die vorhandene API samt Snapshot. Der Main hat den
ausfuehrbaren Code im Mathematikreview nochmals separat ausgefuehrt;
maximaler absoluter80/120-Unterschied der19 Groessen kleiner3.50e-80.
Das ist eine Hochpraezisionsgegenpruefung, keine Intervallzertifizierung.

Aus D-B=sqrt(e)*(1/a-1)>0 folgt ausserdem: Die B-Bedingung ist staerker
als die vorgelagerte Positivitaet. (2,2) ist ein konkretes Beispiel, das
die Positivitaet erfuellt, aber B nicht. Wir ersetzen deshalb nicht
eigenmaechtig B durch D: Eine solche Aenderung waere eine zu begruendende
Reparatur, nicht die wortgetreue Rekonstruktion.

## 4. Was die anderen Fassungen hinzufuegen

Die H013/H014-Typoskripte tragen die konkrete N=0-Tabellenbelegung und
den eta22-Konstantenwert ebenfalls, sind aber nicht verlaesslich datiert.
Der Vergleich muss ueber Ladungsbetrag, k und weitere Quantenzahlen
erfolgen, nicht allein ueber aehnliche kleine oder grosse Delta-Glyphen.
Die direkte H004-Kette beseitigt die Notwendigkeit, fuer den vorliegenden
Buchbefund eine Fassungsidentitaet vorauszusetzen.

H013 Druck20a/PDF22 erklaert zudem, warum Heim nicht jede Abweichung von
seiner stufenweisen Anregungsregel(14d) als Nichtexistenz versteht: Er
unterscheidet schrittweise Anregungen von einem einzigen energetischen
Vorgang, etwa einer Resonanz. Das ist eine ausdrueckliche Einschraenkung
dieser anderen Auswahlregel, keine Reparatur der B-Schranke aufII269.
Der Delta-Resonanzblock in H013 TabelleVa Druck52/PDF55 hat N>0, aber
keine q-Spalte. Nicht jede dieser Zeilen ist dadurch als q2 identifiziert.
H014 TabelleI Druck38/PDF41 bestaetigt die N0-Belegung; Main hat auch
diese drei Vollseiten gegengelesen. delta(N) als 0/1-Selektor in H013
ist nochmals eine andere Groesse, keine Teilchenbezeichnung.

H006 PDF3 fuehrt das entsprechende Quartett in der B-Notation auf, aber
die IGW-Wiedergabe versieht es sichtbar mit einer Frage nach der
Denkbarkeit als Grundzustand. Die Urheberschaft dieser redaktionellen
Schicht ist hier nicht gesichert. H007 Druck20/PDF11 verwendet q=2
fuer Delta dagegen ausdruecklich im N>0-Resonanzkontext und nennt dort
unbekannte Funktionen und begrenzte Naeherungen.

Die dazu angegebene IGW-Tabellensammlung KapitelG wurde neu als S006
gesichert: TabelleI enthaelt eine passende N=0-Quantenzahlenbelegung
unter einer o-artigen Bezeichnung; TabelleVb enthaelt explizite
Delta-Resonanzen mit N>0. Das ist kein Freibrief, Grundmuster, Resonanzen
und jede unterschiedliche Benennung physikalisch gleichzusetzen.
N=0 bedeutet auch nicht unbegrenzte Lebensdauer. Quellenlinks, Hashes,
vollstaendig betrachtete Seiten und Grenzen stehen in der Quellennotiz.

## 5. Was damit geklaert ist und was offen bleibt

Neu ist die konkrete Anwendung des bereits bekannten Schrankenproblems
auf einen im selben Buch aufgenommenen Zustand. Die tabellierte Zulassung
ist mit der woertlichen detaillierten B-Bedingung unvereinbar. Das wird
in FIND-016/FIND-019 ergaenzt;
FIND-015 bleibt der zugehoerige lokale Umformungsknoten. Keine neue
unabhaengige Fehlergruppe wird allein aus diesem Anschluss erzeugt.

Nicht geklaert sind die historische Ursache und eine belegte richtige
Fassung dieser Auswahl. Es waere falsch, daraus ein Verbot von eta22
als mathematisch definiertem Faktor in jeder anderen Formel abzuleiten.
Ebenso wenig folgt aus dem Delta-Zustandsanschluss, warum eta22 in der
speziellen Alpha-Korrektur C_prime von H007(B59) vorkommt. Eine konkrete
Zwischenzustandsdynamik oder diese spezielle Herleitung ist nicht belegt.

Der naechste begrenzte Schritt ist deshalb die Rollenpruefung von eta22
in H007(B47)/(B55) samt zugehoerigen Autorenstellen: Definition,
physikalische Bedeutung und begruendete Uebergaenge getrennt aufzeichnen.
Eine wiederkehrende Konstante allein schliesst die B59-Luecke nicht.
Danach folgen B50/Gamma-Q_N und die geplante Verstaendnisbilanz.
Keine erneute ungezielte Suche nach denselben Indizes, kein moderner
Messwertvergleich oder Hardwareausbau in dieser Etappe.

## 6. Reproduktion und dauerhafte Ablage

- Quellenkontext: `03_notes/DELTA_SELECTION_SOURCE_CONTEXT_2026-09-06.md`.
- Drei unabhaengig bearbeitete Reviews unter
  `04_reconstruction/alpha_audit/reviews/`: DELTA_BOOK_SCOPE,
  DELTA_MANUSCRIPT_SOURCE, DELTA_SELECTION_MATH, jeweils2026-09-06.
- Acht vorhandene Rechner, Eingaben und Snapshots bleiben unveraendert.
  Nachpruefbefehle stehen in `scripts/README.md`; der fokussierte Test ist
  `py -3.13 scripts/audit_configuration_selection.py --check --verify-sources`.
- Schlusspruefung erfolgreich: acht Snapshotchecks samt verfuegbaren
  Quellhashchecks, Registervalidator und98 Unittests. Unabhaengige
  Synthesegegenlesung bestaetigt die Mathematik; Praezisierungen zu
  Maxima, Bedingungslogik und derselben Primaerquelle uebernommen.
- Register weiterhin20 Befundgruppen, keine20 Fehler. Die49
  Normalisierungsentscheidungen bleiben unveraendert (47 resolved,2 alte Blocker).

Plan und Wiedereinstieg: `00_admin/DELTA_SELECTION_PLAN.md` und
`00_admin/RESUME.md`. Quellen-PDFs bleiben bewusst ausserhalb von Git;
eigene Notizen und nachvollziehbare Rechnungen werden versioniert gesichert.
