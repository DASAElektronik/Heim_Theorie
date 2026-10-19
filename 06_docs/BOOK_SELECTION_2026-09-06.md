# Buch-Auswahl: Besetzungen, Gleichungsrest und Rueckschluss auf A16

2026-09-06, Etappe29. Ausgang `3a779e5`, Plancheckpoint `4da02b3`.
Fortsetzung der [F16-Bestimmtheitspruefung](F16_DETERMINACY_2026-09-06.md).
Keine neue Masse, F_S-Rechnung, Y9-Anpassung oder Autoren-Ersatzformel.

## Ergebnis

Die Buchfassung beschreibt deutlicher als die bisher untersuchten
Kurzfassungen, wie aus vorgegebenem W ganzzahlige Besetzungen entstehen.
Sie liefert im geprueften Abschnitt aber keine zusaetzliche eindeutige
Herleitung von A16. Eine eindeutige Vorwaertsauswahl ist nicht automatisch
eindeutig umkehrbar. Eigene exakte Beispiele belegen diese Unterscheidung
fuer die reduzierte Vorschrift, nicht fuer vollstaendige Heim-Zustaende.

Zugleich muss man zwei Ansprueche auseinanderhalten: eine zulaessige
Besetzung auswaehlen und die vorausgehende Gleichung exakt loesen.
Abschneiden, Saettigung und der Transfer leisten Letzteres bei festen
vorherigen Resten nicht allgemein. Das ist ein bedingter lokaler Befund,
keine Gesamtwiderlegung der Theorie und keine neue Massenabweichung.

## 1. Quellenvertrag und Eingaben

Hauptquelle ist H004, Heim, *Elementarstrukturen der Materie II*,
Ausgabe1996, Druck340-342 / physische PDF346-348. Direkte Anschluesse:
(107) Druck321/PDF327, (107a)328/334, (107b)329/335 und (108)330/336.
[Quellenumfang und Hashes](../03_notes/BOOK_SELECTION_SOURCES_2026-09-06.md)
dokumentieren die Vollsicht und die getrennte H006/H015-Gegenlesung.

Das Buch stellt W sowie die Resonanzgroessen a,b zuerst aus (108)-(110d)
bereit. Die eigentliche Exhaustion beginnt mit W1=W(1+f). Wir schreiben
die Auswahlzahlen wie das Buch als N_(j), nicht wie H006/H015 als K_j.
Die Resonanzordnung N und die vier N_(j) sind verschiedene Groessen.
Erst nach der Auswahl wird n_j=N_(j)-Q_j gesetzt.

Die Rechenrichtung ist:

```text
A16 -> w -> W=g*w -> W1=W*(1+f) -> N_(1), N_(2), N_(3), N_(4) -> n_j
```

Der A16-Anschluss stammt aus (108)/(109a), bereits in Etappe28 geprueft.
Auf340-342 steht keine Rueckiteration zur Bestimmung von A16 und kein
Fixpunktauftrag fuer die Koeffizientenmatrix. Resonanz-a ist nicht alpha3;
im Folgenden verwenden wir fuer den dritten Koeffizienten stets alpha3.

Mit lambda=(2k-1)/(3Q4)>0 lautet (108) im betrachteten reellen Anschluss:

\[
\alpha_1N_{(1)}^3+\alpha_2N_{(2)}^2+\alpha_3N_{(3)}
  +e^{-\lambda N_{(4)}}=W_1.
\]

Die folgende skalare Analyse setzt alpha_i>0 und W1>=0 voraus.
Diese Voraussetzungen geben keine beliebigen positiven Koeffizienten
als gemeinsame physikalische Heim-Parameterfamilie frei.

## 2. Exhaustion bis zum logarithmischen Rest

N_(1) wird bis zum groessten Integer mit alpha1*N_(1)^3<=W1 erhoeht.
Aus W2=W1-alpha1*N_(1)^3 wird analog N_(2) mit quadratischem Beitrag
ausgeschoepft. Es bleiben W3=W2-alpha2*N_(2)^2 und danach

\[
m=N'_{(3)}=\left\lfloor W_3/\alpha_3\right\rfloor,\qquad
r=W_4=W_3-\alpha_3m.
\]

Vor einem etwaigen Transfer ist N_(3)=m. Die Quelle spricht im Ablauf
von positiven ganzen Zahlen; die allgemeine Besetzungsdomaene N_(j)>=0
steht im Kontext Druck322. Der Null-Maximalfall ist unsere entsprechend
deklarierte Domaenenkonvention. Bei positiven Koeffizienten folgt aus
der sukzessiven Maximalwahl exakt 0<=r<alpha3.

Der Druck341 nennt dagegen als Alternativen 0<=W4<=1 und
1<W4<(alpha3*N_(3))_max; der zweite Bereich sei fuer k=2 moeglich.
Wir erhalten diese gedruckte obere Grenze als Quellenangabe. Die engere
Greedy-Folgerung r<alpha3 ist unsere Algebra, keine stille Textkorrektur.

Fuer r>0 setzt Heim W5=x=-ln(r)/lambda. Bei r=0 beschreibt er eine
Divergenz gegen +unendlich; ln(0) ist kein endlicher Rechenschritt.

## 3. Was die vierte Auswahl tatsaechlich vorschreibt

TRC schneidet Dezimalstellen ab, mit einer ausdruecklichen Ausnahme fuer
eine endliche Neunerfolge bis unterhalb der Messbarkeitsschranke.
Die Quelle gibt dafuer keine numerische Schwelle an. Unendlich 0.999...=1
und eine endliche Promotion sind mathematisch nicht dasselbe. Wir
implementieren deshalb weder ein frei erfundenes Epsilon noch pauschal
TRC=floor. Die unten benannten Floor-Faelle sind der gewoehnliche Zweig.

| Fall | Buchregel auf Druck341/PDF347 | Zu trennende Frage |
|---|---|---|
| r=0 oder x>alpha3*m | N_(4)=TRC(alpha3*m); nur bei TRC(alpha3*m)>alpha3*m anschliessend minus1 | Endliche Kappe statt exakter logarithmischer Umkehrung |
| 0<r<=1 und 0<=x<=alpha3*m | N_(4)=TRC(x) | Ganzzahligkeit erhaelt die reelle Gleichung nur in Sonderfaellen |
| r>1, also x<0; Quelle: k=2 und besetzte Zone3 | Transfer aus Zone3, danach N_(4)=TRC(W6) | Nichtnegativitaet, Rohwertkappe und Erhaltung sind getrennte Anforderungen |

Die bedingte Minus1-Regel verbindet Heim ausdruecklich mit beta4=1 aus
(107a). Sie ist keine allgemeine Vorschrift ceil(alpha3*m)-1.

### Transfer: gesicherter erster Schritt und deklarierte Fortsetzung

Der erste Schritt verwendet ausdruecklich den alten Wert m=N'_(3):

\[
u_1=W_6=x+\alpha_3m,\qquad N_{(3)}=m-1.
\]

Das Buch beschreibt danach absteigende Zugaben und druckt eine Summe
ueber mu mit Term N'_(3)+1-mu. Explizite untere/obere Summengrenzen
fehlen. Die naheliegende kumulative Rekonstruktion nach h Schritten ist

\[
u_h=x+\alpha_3\sum_{s=1}^{h}(m+1-s)
    =x+\alpha_3\bigl(hm-h(h-1)/2\bigr),\qquad N_{(3)}=m-h.
\]

Diese geschlossene Mehrschrittform ist **unsere deklarierte Lesart**,
nicht eine vollstaendig ausgeschriebene Autoren-Implementierung.
Die Quelle verlangt gleichzeitig u_h>=0, u_h<=alpha3*(m-h) und m-h>=0.
Erst danach folgt N_(4)=TRC(u_h). Insbesondere darf man die Rohwertkappe
nicht durch eine Pruefung allein des abgeschnittenen Wertes ersetzen.

Schon fuer h=1 sind beide Rohwertbedingungen genau aequivalent zu
-alpha3*m<=x<=-alpha3 bei m>=1. Nichtnegativitaet allein genuegt nicht.
Die Bemerkung, im Allgemeinen genuege ein Schritt, ist keine Garantie.
Wenn Nichtnegativitaet nur durch negatives N_(3) erreichbar waere, nennt
Heim den Term verboten. Ein allgemeiner Ausweg bei anderer Gateverletzung,
erneute Logarithmierung eines geaenderten W4, Aenderung von W1 oder ein
Ruecksprung zu N_(1)/N_(2) ist hier nicht ausformuliert.

Druck342 begruendet den speziellen Transfer3->4 durch den linearen
Charakter von G4 und delta3G3. Analoge Transfers2->3 oder1->2 schliesst
der Text wegen weiterer niedrigerer Potenzterme aus. Das erklaert Heims
angegebene Motivation; es beweist noch keine Gleichungserhaltung.

### Zusaetzlicher Randanschluss: beta4

(107) fordert delta_jG_j>G_(j+1) und delta_jG_j>=delta_(j+1)G_(j+1).
(107a) verlangt beta_j>=1, mit einem gesonderten Kollapsfall beta_j=0,
G_j=0 und Aenderung der vorigen Besetzung. (107b) schreibt
beta4=alpha3*N_(3)-N_(4)>0. Diese Bedingungen sind staerker als die
blosse nichtstrikte Rohwertkappe im Auswahltext.

Eigener Randtest: Ist alpha3*m=2, r=0 und TRC gewoehnliches Floor, so
liefert die gedruckte Kappe N_(4)=2 und beta4=0. Die bedingte Minus1-Regel
greift nicht, weil floor(2)>2 falsch ist. Das verlangt einen gesonderten
Anschluss an den Kollapsfall, bevor der Zustand akzeptiert werden kann.
Es ist kein nachgewiesener realer Teilchenfall oder globaler Widerspruch.
Auch eine echte Neuner-Promotion verlangt eine eigene Grenzpruefung.

## 4. Eigene exakte Restdiagnose

Wir halten W3 und alpha3 fest, also auch die vorausgehenden N_(1),N_(2),
und pruefen den Fehler links minus rechts:

\[
R=\alpha_3N_{(3)}+e^{-\lambda N_{(4)}}-W_3.
\]

**Gewoehnliches Abschneiden:** Bei N_(3)=m, j=floor(x)>=0 und
theta=x-j in [0,1) gilt

\[
R=e^{-\lambda j}-r=r(e^{\lambda\theta}-1)\ge0.
\]

Gleichheit gilt genau bei ganzzahligem x. Bei einer echten endlichen
Promotion j>x ist das Vorzeichen dagegen negativ. Die Floor-Aussage
ist deshalb keine Fehlergarantie fuer jede moegliche TRC-Konvention.

**Saettigung:** Bei r=0 und endlichem N_(4) bleibt R>0. Bei r>0,
x>alpha3*m und einem gekappten j<=alpha3*m<x ebenfalls. Das betrifft
das gewaehlte m, nicht ohne Zusatzargument alle anderen Besetzungen.

**Transfer:** Fuer r>1, h>=1 und ein akzeptiertes j=N_(4)>=0 gilt
unabhaengig von der Summenlesart:

\[
R=e^{-\lambda j}-r-\alpha_3h
 \le1-r-\alpha_3h<0.
\]

Bei festem W3 gibt es in diesem Fall sogar kein ganzzahliges N_(3)>=0
mit reellem N_(4)>=0, das die Restgleichung erfuellt: Fuer N_(3)<=m
waere der benoetigte Exponentialterm mindestens r>1; fuer N_(3)>=m+1
waere er wegen r<alpha3 negativ. Das schliesst weder andere vorherige
Besetzungen noch eine separat begruendete diskrete Projektionsregel aus.

Ein akzeptierter **synthetischer** Erstschritt zeigt den Unterschied:
alpha3=2, m=4, lambda=1/15, r=3/2 ergibt
1<u1=8-15*ln(3/2)<2. Somit N_(3)=3, N_(4)=1, Rohwertkappe6 und
beta4=5. Trotzdem R=exp(-1/15)-7/2<0. Das ist kein vollstaendiger
Heim-Zustand und kein Nachweis aller Bedingungen(107)/(107a).

Die Restargumente erweitern FIND-035 um den direkt geprueften Buchvertrag;
sie sind keine zusaetzliche unabhaengige Zaehlliste desselben Fehlers.

## 5. Was das fuer A16 bedeutet

Im aktiven Buch-Pseudosingulett k=Q=kappa=q=1 gilt nach der vorausgehenden
Grenzwertapproximation W=g(1+d*A16), d=eta_qk>0. Bei festem f>-1 sei
G=g(1+f)>0. Das ist ein lokaler Anschluss, keine Freigabe von A16 als
global beliebigem physikalischen Parameter.

Bleiben die ersten drei Greedywerte fest, sei ihre Beitragssumme S.
Dann ist r(A)=G(1+d*A)-S. Die gewoehnliche, ungesaettigte Auswahl
N_(4)=j entspricht

\[
e^{-\lambda(j+1)}<r(A)\le e^{-\lambda j}.
\]

Somit ergibt sich ein **Intervall**, nicht automatisch ein Einzelwert:

\[
\frac{S+e^{-\lambda(j+1)}-G}{Gd}<A
\le\frac{S+e^{-\lambda j}-G}{Gd}.
\]

Es ist mit der Zelle gleicher N_(1)..N_(3), der Rohwertkappe und allen
weiteren Bedingungen zu schneiden; es kann dadurch eingeengt oder leer
werden. Wir haben nicht bewiesen, dass ein ganzes solches Intervall im
vollstaendigen Heim-Modell physikalisch erlaubt ist.

Exakter eigener Zwei-Eingaben-Test, keine Buchkonstanten:
alpha=(1,2,1), lambda=1/3, W1=151/4 beziehungsweise189/5. Beide ergeben
N_(1)..N_(4)=(3,2,2,0), bei S=37 und r=3/4 beziehungsweise4/5.
Beide Logwerte liegen sicher zwischen0 und1, die Rohwertkappe2 haelt;
beta4=2. Die Gleichungsreste sind aber 1/4 beziehungsweise1/5.
Mit der rein synthetischen affinen Beziehung W1=2+A werden auch zwei
verschiedene A-Eingaben demselben Tupel zugeordnet. Weitere(107)-Gates
oder Teilchenzuordnungen werden fuer diesen Zeugen nicht behauptet.

Ein unabhaengig festes vollstaendiges Tupel **plus exakt geforderte**
Gleichung(108) koennte dagegen A eindeutig bestimmen: In obiger Notation
waere A=(S+exp(-lambda*j)-G)/(G*d). Dies ist gerade nicht schon durch
Abschneiden bewiesen. Formel(109b) mit festem Y9 bleibt berechenbar;
es wurde kein neues Y9 bestimmt oder nach einem kleineren Rest gewaehlt.

## 6. Begrenzter Fassungsvergleich

H006 Druck/PDF9 und H015 physische PDF42 haben dieselbe lokale
logarithmische Umkehrung und drei W4-Faelle. Sie nennen den reellen
Logwert unmittelbar K4; im negativen Fall beschreiben sie einen K3-
Rueckschritt und eine Addition alpha3*K3 ohne expliziten Vor-/Nachindex.
Das Buch bezeichnet dagegen W5/W6, nennt den alten N'_(3) im ersten
Schritt, die absteigende Fortsetzung und die Rohwertkappe. Auch die
Saettigung bei endlichem x oberhalb der Kappe wird dort ausgeschrieben.

Das sind hilfreiche Praezisierungen **der Buchfassung**. Ohne weiteren
Editionsbeleg sind sie keine rueckwirkend autorisierte Korrektur der
Kurzfassungen. H006/H015 nennen zudem N=0 oder N>=2 sowie Q(0), waehrend
der Buchabschnitt N>=0 nennt. Gleiche Strukturideen erlauben weder einen
vollstaendigen Symbol-/Parametertransfer noch eine gemischte Zahlenfassung.

## 7. Reproduktion, Reichweite und Folgeauftrag

- 13 neue rationale/Intervalltests in `tests/test_book_selection.py`;
  deren allgemeine Log-/Exp-Helfer stammen aus den Etappe25-Tests.
  Kein Produktionssolver und keine vollstaendige TRC-Implementierung.
- Unabhaengiger selbstenthaltener Mathematik-Reviewblock: 37 rationale
  Pruefungen, von Root erneut ausgefuehrt. Drei interne Reviews insgesamt;
  kein externes PeerReview. Quellenaussagen, unsere Lesart und eigene
  skalare Zeugen sind getrennt.
- Vollsuite247Tests und elf alte Ergebnis-/Quellchecks erneut bestanden;
  Resultate im Wiedereinstieg. Keine Aenderung an
  alten Rechnern, Eingaben, Snapshots oder49CSV-Normalisierungen.
- FIND-039 buendelt den neuen Buchanschluss und seine Grenzen;
  die Anzahl der Befundgruppen ist keine Anzahl widerlegter Aussagen.

**Naechster Einzelauftrag:** einen buchinternen Eingabevertrag fuer das
aktive Pseudosingulett bei N=0 aufstellen. Vor einer neuen Auswahlrechnung
muessen k,Q,kappa,q, Q_j, g, eta/eta_qk, alpha_i, A16, Y9 und f aus
derselben Buchfassung mit eindeutigen Quellenstellen festliegen.
Y9=1 nur als ausgewiesene Tabellenannahme; keine Uebernahme der H006-
Zahlenprofile oder H010-Programmkonstanten als angebliche Buchwerte.
Erst bei geschlossenem Vertrag den erreichten Zweig und seine Struktur-
und Restbedingungen pruefen, weiterhin ohne Masse/F_S oder Zielwertfit.
Eine konkrete Eingabeluecke ist ein zulaessiges begrenztes Ergebnis.

Offen bleiben unabhaengig davon die TRC-Messschwelle, der vollstaendige
Mehrschritt-/Gatefehlerablauf, der Kollapsanschluss und die physikalische
Begruendung einer von exakter(108)-Erhaltung unterschiedenen Auswahl.
Sie werden nicht still durch eigene Reparaturen geschlossen.
