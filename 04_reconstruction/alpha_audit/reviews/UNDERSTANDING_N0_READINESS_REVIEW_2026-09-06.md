# N=0-Rechenfall: bedingte Readiness-Bilanz (H006)

Datum: 2026-09-06

Umfang: Vorbereitung eines nicht implementierten Lehr- und Auditfalls aus
der 1982er Formelversion H006, ausschließlich anhand der bereits
quellengeprüften Formelbibliothek und Bildanker. Dies ist weder eine
Massenrechnung noch ein Vergleich mit einem Messwert. H007, H013 und die
1989er Formel werden nicht in diesen Fall eingemischt.

## Ergebnis

Als gut begrenzten Lehrfall wählen wir den in H006 als Elektronmultiplett
bezeichneten Grundzustand x2 bei N=0. Er ist heute
nur als zweistufig vorbereiteter bedingter Test bereit:

1. Stufe A — Auswertung eines quellenprovenierten, gegenüber der
   Rechenauswahl nicht nach Sollmasse gewählten Besetzungsquadrupels:
   möglich, sobald eine Quelle tatsächlich ein n1..n4-Quadrupel für die
   H006-Version und Komponente liefert. Dies prüft dann die bedingte
   Auswertung der Massenanteile. Das heißt nicht automatisch, dass der
   Tabellenwert empirisch unabhängig von der historischen Modellbildung
   wäre.
2. Stufe B — Herleitung dieses Quadrupels aus H006: noch nicht ausführbar.
   Die algorithmische Zielgröße und die vorherige nu_x/vx-Notation sind
   nicht quellenbelegt verbunden; weitere Auswahlpfade dürfen nicht aus
   einer Sollmasse gewählt werden.

Ein tabellarischer Zustand darf Stufe A nur speisen, wenn die Tabelle
explizit die vier Besetzungszahlen meint. Ein H006-Teilchenlabel oder seine
vier Konfigurationsziffern sind kein stiller Ersatz dafür.

## Versionswahl und Kandidatenvergleich

Die Fallversion wird fest auf H006, Die Massenformel nach Burkhard Heim
(1982), IGW-Reproduktion, eingefroren. Ihre zentrale Gleichung lautet:

    M = mu * alpha_mass_plus * (K_aux + G_aux + H_aux + Phi_aux).   (XII)

Sie steht auf H006 Druck 5/PDF 5, Bildanker
07_outputs/source_check_images/1982_massenformel/page-05.png.
mu*alpha+ ist dabei die durch NORM-1982-MASS-MU-ALPHA-PLUS eng gebundene
Produktlesart. Das unparenthesierte alpha_mass_plus ist nicht der frühere
Feinstruktur-Zweig alpha_(+); ebenso ist G_aux nicht der Zählwert G=k+1.

| möglicher Kontext | N=0-Lehrwert | Begrenzung |
| --- | --- | --- |
| H006 x2 / Elektron | H006 schreibt für N=0 unmittelbar f(0)=0; für x2 sogar f=0 für alle erlaubten N. Damit entfallen im bedingten N=0-Test der f-Zusatz und die Gamma-Seite der Gleichung. | Die geprüfte Teilchentabelle gibt kein n1..n4 an. |
| H006 x8 / Proton oder x12 / Delta | ebenfalls Grundzustandsetiketten | Für einen ersten Test ohne den besonderen x2-Kontrollfall mehr Selektions- und Anregungsfragen; auch hier kein belegtes Besetzungsquartett in den geprüften H006-Ankern. |
| H007 / 1989 | besitzt eigene N=0-Ausdrücke | B3--B5 führen über phi, B49 und B50. Das B50-Doppelminus ist allgemein ein offener Signbefund, seine Relevanz für einen konkreten Satz von Quantenzahlen ist jedoch fallweise zu prüfen; unter geeigneten Parametern kann der betreffende U-Anteil auslöschen. H007 bleibt hier lediglich ein anderer Formelstand und wird nicht mit H006 gemischt. |

Die Wahl erfolgt nach Nachvollziehbarkeit, nicht nach Nähe zu einer
bekannten Elektronenmasse.

## Was H006 über x2 und N=0 belegt

H006 Druck 3/PDF 3 wurde vollseitig geprüft; Bild:
07_outputs/source_check_images/1982_massenformel/page-03.png. Die Liste
steht unter Die möglichen Multipletts der Grundzustände und definiert die
allgemeine Schreibweise:

    x_nu (epsilon B, epsilon P, epsilon Q, epsilon kappa)_epsilon C(q0,...,qP).

Dort steht sichtbar:

    x2 (0110)0(0,-1) == (e0, e-).

Die vier Ziffern 0110 sind damit Bestandteile der Konfigurationsnotation
(epsilon B, epsilon P, epsilon Q, epsilon kappa). Sie sind nicht als die
späteren Besetzungszahlen n1,n2,n3,n4 definiert. Die Seite liefert den
Multiplettkontext und Konfigurationsparameter, aber kein einsetzbares
Besetzungsquadrupel.

H006 Druck 8/PDF 8 wurde ebenfalls vollseitig geprüft; Bild:
07_outputs/source_check_images/1982_massenformel/page-08.png. Dort heißt
es, die Resonanzordnung N >= 0 wähle zulässige Quadrupel n_j, 1 <= j <= 4,
aus. Gedruckt ist:

    f(N) = [1-Q(2-k)(1-kappa)]
           [a_vx*N/(N+2) + b_vx*sqrt(N(N-2))].                 (XXV)

Für N=0 setzt der Text f=0 und gibt:

    (n1+Q1)^3 alpha1 + (n2+Q2)^2 alpha2 + (n3+Q3) alpha3
    + exp[(1-2k)(n4+Q4)/(3Q4)] = W_vx.                         (XXVI)

Der Text nennt dies die Beschreibung der n_j und der Masse M0(vx) einer
Multiplettkomponente. Für x2 vermerkt er zusätzlich
Q(2-k)(1-kappa)=1, daher f=0 für alle N>=0, und schließt mit der
modellinternen Aussage, Elektronen seien nach diesem Bild nicht anregbar.
Das ist eine H006-Aussage über dessen Modell, keine moderne
Teilchenphysik-Aussage.

### Minimaler, schon quellenbelegter Preflight für die e--Komponente

Für den engeren Kandidaten e- lässt sich aus derselben Seite bereits ein
kleiner, vollständig quellenlokaler Eingabesatz bilden, ohne irgendeine
Besetzung zu behaupten:

    edition/version = H006 only
    base multiplet = x2, epsilon=+1
    printed configuration = (epsilon B,epsilon P,epsilon Q,epsilon kappa)
                          = (0,1,1,0)
    hence B=0, P=1, Q=1, kappa=0
    component = x=1, printed charge list entry e-
    C=0, N=0

Die Bildseite gibt oberhalb der Tabelle in (II) die Ladungsregel

    2*qx = (P-2x)[1-kappa*Q*(2-k)]
            + epsilon[k-1-(1+kappa)*Q*(2-k)] + C,
    0 <= x <= P, q=|qx|.

Für das in der Tabelle als Meson eingestufte x2 gilt k=1. Einsetzen der
oben abgelesenen Werte ergibt 2*qx=(1-2x)-1=-2x. Somit ist für x=1
qx=-1 und q=1, genau wie die sichtbare Komponentenzeile (0,-1) ausweist;
für x=0 ergibt sich qx=0. Das ist eine direkte algebraische Kontrolle der
gedruckten Konfigurations- und Ladungsangabe, keine Massenauswertung.

Explizit **nicht** vorhanden bleiben n1,n2,n3,n4, W_vx, a_vx, b_vx und
eine aus dem H006-Algorithmus hergeleitete Besetzung. Der Preflight
reduziert daher die Eingabelücke für die e--Komponente, schließt aber
Stufe A oder B noch nicht.

## Stufe A: bedingter Auswertungstest

### Zulässiger Inputvertrag

Eine künftige Stufe A darf nur mit einem extern bereitgestellten,
quellenzitierten Datensatz beginnen, der mindestens enthält:

    version = H006-only
    state/multiplet component = exact printed source label
    N = 0
    k, epsilon, P, Q, kappa, x, qx, q=|qx| = source-specific values
    n1, n2, n3, n4 = explicitly labelled occupation quadruple
    constants_profile = model_1982_igw2003_printed
    alpha-profile = explicitly declared literal-source branch handling

Der Nachweis muss zeigen, dass n_j wirklich das Besetzungsquadrupel der
H006-Auswahlregel ist, nicht eine (epsilon B,epsilon P,epsilon Q,
epsilon kappa)-Kurzschreibweise, Ladungsliste oder Konfigurationsnummer.
Die geprüfte x2-(0110)-Zeile erfüllt diesen Nachweis nicht.

Liegt der Input vor, ist die reine Rechenkette:

    (k,q,P,Q,kappa; n1..n4; historical constants)
      -> eta, t, alpha_mass_plus/minus, eta_qk
      -> alpha1..3, Q1..4
      -> K_aux, G_aux, H_aux, Phi_aux
      -> mu_mass_element
      -> M_1982 = mu*alpha_mass_plus*(K_aux+G_aux+H_aux+Phi_aux).

Die Quellenanker sind H006 Druck 4/PDF 4: (VI)--(X), Druck 5/PDF 5:
(XI)--(XII), sowie HT-F-1982-MU, HT-F-1982-AUX und HT-F-1982-MASS.
s0=1 m und die gedruckten Werte für hbar, c und die gravitative gamma
gehören zum historischen Profil. mu hat dort Masseneinheit; eine
Umrechnung nach MeV/c^2 wäre ein nachgelagerter, getrennt protokollierter
Darstellungsschritt und darf die Eingabewahl nicht beeinflussen.

Aktiv, aber nur mit ihrer engen dokumentierten Reichweite, sind:
NORM-1982-MU-HISTORICAL-CONSTANTS,
NORM-1982-MASS-MU-ALPHA-PLUS,
NORM-1982-AUX-SYMBOL-ROLES,
NORM-1982-AUX-PHI-PRECEDENCE und NORM-1982-ETA-INDEX.
Resolved bedeutet hier eine überprüfte Glyphe, Index- oder
Klammerreichweite, nicht eine globale Herleitung oder vollständige
Ausführbarkeit. Das lange Phi_aux bleibt trotz geklärter lokaler Präzedenz
ein sensitiv zusammengesetzter Term.

Für einen festen N=0-Input sind folgende Punkte nur bedingt inaktiv:

- f ist quellenbedingt null; a_vx und b_vx müssen dafür nicht numerisch
  bestimmt werden.
- Die von H006 offen gelassene Beziehung von F(Gamma), voller Bandbreite,
  N und Q_N=Q(N) wird nicht ausgewertet. Das löst sie nicht, sondern
  beschränkt diesen einzelnen Grundzustandsausdruck.
- W4-Fallverhalten, Dezimal-/99...99-Regel und nu_x/vx-Übergang werden in
  Stufe A nicht benutzt, weil keine Besetzung hergeleitet wird.

Auch die quellenausdrückliche Ausnahme f=0 für x2 löst nicht die separate
N=1-Frage: H006 sagt weiterhin, dass bei N=1 kein Spektralterm vorliegt.
Der vorbereitete Fall setzt N=0 direkt ein und leitet aus der x2-Ausnahme
keinen zusätzlichen Ausschluss oder eine allgemeine N-Regel ab.

Stufe A liefert deshalb eine bedingte Auswertungs- und
Auslöschungsprüfung: Stimmen die Teile der eingefrorenen H006-Formel für
den transparent gegebenen Input überein? Sie ist keine Vorhersage eines
Teilchenzustands oder einer Teilchenmasse.

## Stufe B: von H006 zum Quadrupel — derzeit blockiert

H006 Druck 9/PDF 9 gibt einen Auswahlalgorithmus: Für N=0 ist zunächst
W1=W_vx(1+f(0))=W_vx zu bilden; maximale Kubik-, Quadrat- und
Linearanteile werden nacheinander abgezogen und n_j=K_j-Q_j gesetzt.
Die Seite verlangt ausdrücklich Q=Q(0) der lokalen Komponente, nicht
Q_N=Q(N). Das ist die enge Basis für NORM-1982-SELECTION-QN-Q0-SCOPING,
nicht die Lösung der Resonanz-/Bandbreitenbeziehung.

| benötigter Knoten | gegenwärtiger Status | Wirkung |
| --- | --- | --- |
| W_vx, a_vx, b_vx | Druck 8--9 nutzt die vx-Familie. Frühere Kern-/WVX-Formeln liefern source-local W_nu_x, a_nu_x, b_nu_x. NORM-1982-SELECTION-VX-NUX-SCOPING verbietet ihre Gleichsetzung. | Der Algorithmus kann nicht aus den früheren Formeln gespeist werden, solange keine Alias- oder Tabellenquelle besteht. |
| W4-Fall und Ganzzahlregel | Literalvarianten und die 99...99-Ausnahme sind dokumentiert; Case (c) hat Varianten. | Erst nach unabhängiger Bestimmung der Rohreste aktiv; nie nach Massentreffer auswählen. |
| Zustand-zu-Besetzung | x2 ist ein Konfigurationslabel, kein n_j-Datensatz. | Verhindert die stille Verwendung von 0110 als Besetzung. |
| Gamma / Q_N | H006 erklärt die Beziehung selbst für offen. | Für die N=0-Auswertung nicht numerisch nötig, für Resonanzdeutung weiterhin offen. |

Die schmale N=0-Ausnahme legitimiert Stufe B nicht. Für einen kontrollierten
Test müssen Zielgröße und alle Versions- und Aliasentscheidungen vor dem
numerischen Massenvergleich fixiert sein, ohne sie nach dessen Ergebnis
anzupassen. Bloßes Vorwissen über die Elektronenmasse ist nicht vermeidbar.

## Kalibrierungs- und Zirkularitätsregeln

1. Kein n_j, keine W4-Variante, kein Dezimalmodus und keine nu_x/vx-
   Zuordnung darf anhand einer bekannten Elektronen-, Proton- oder
   Delta-Masse gewählt werden.
2. Die H006-ALPHA-Prüfung hält für die gedruckte positive
   Feinstruktur-Angabe Literal-/Rundungsvarianten getrennt. Ein
   indexgetauschter eta-Fall darf nicht wegen eines gewünschten Endwerts
   ausgewählt werden. alpha_mass_plus ist davon getrennt; Phi_aux benutzt
   dennoch den source-lokalen nackten alpha-Zweig.
3. Historische H006-Konstanten und moderne Konstanten dürfen nicht in
   einer Rechnung gemischt werden.
4. Ein aus einer Tabelle übernommenes Besetzungsquadrupel testet nur
   Stufe A. Es belegt weder die H006-Herleitung aus W/Q(0) noch
   Vorhersagekraft.
5. H007-B50, H013-Lesarten und Buch-II-Konfigurationen sind keine
   Reparatur- oder Parameterquelle für den eingefrorenen H006-Fall.

## Nächste begrenzte Reihenfolge

1. Eine H006-nahe Quelle finden, die für eine konkrete x_vx-Komponente
   n1..n4 ausdrücklich als Besetzung ausweist, einschließlich Version.
2. Dann Stufe A als transparente Teilsummenrechnung starten: Rohinput,
   Normalisierungen, Konstanteprofil und Zwischenwerte ausgeben; nie einen
   Messwert als Auswahlkriterium verwenden.
3. Erst danach Stufe B separat prüfen: vx/nu_x-Brücke, W-Quelle,
   Auswahlalgorithmus und Grenzen unabhängig fixieren.

Damit bleibt x2,N=0 ein sinnvoller Lehrfall: Er isoliert Massenformel und
Auswahlfrage, ohne die offene Gamma- und N>0-Resonanzstruktur als gelöst
auszugeben. Gegenwärtig ist er aber kein eigenständig ausführbarer,
geschweige denn prädiktiver Rechenfall.
