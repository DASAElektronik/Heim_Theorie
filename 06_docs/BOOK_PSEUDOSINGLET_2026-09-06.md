# Buch-Pseudosingulett: berechenbare Auswahl, nicht bestandener Strukturcheck

2026-09-06, Etappe30, Ausgang `00180ec`. Plancheckpoint `2d53bfc`,
Eingaben vor Auswertung fixiert in `05a0bab`, Rechnercheckpoint `4213148`.
Fortsetzung der [Buch-Auswahlpruefung](BOOK_SELECTION_2026-09-06.md).
Keine Masse, F_S-Rechnung, Y9-Anpassung oder Quellenprogramm-Ausfuehrung.

## Ergebnis

Der vereinbarte Vorwaertspfad laesst sich mit ausschliesslich buchinternen
Formeln und ausdruecklich festgelegten Tabellenannahmen numerisch schliessen.
Beide vorab festgelegten Alpha-Profile liefern

\[
(N_{(1)},N_{(2)},N_{(3)},N_{(4)})=(14,9,13,7),\qquad
(n_1,n_2,n_3,n_4)=(11,6,11,6).
\]

Dieser rechnerisch stabile Auswahlausgang verletzt die unmittelbar aus
(98e), Druck323 und (107)/(107a) rekonstruierte Strukturbedingung:

\[
\delta_2G_2>G_3\quad\Longrightarrow\quad
9^2>\frac{13\cdot14}{2},\quad\text{also }81>91.
\]

Das ist falsch; die zugehoerige Bandbreite ist beta3=-10 statt mindestens1.
Ein konkreter **bedingter buchinterner Konflikt** ist damit erreicht,
nicht bloss ein kuenstliches Hilfsbeispiel wie in Etappe29. Vorausgesetzt
sind die benannten Buchinputs, die gewoehnliche Abschneideregel und die
unveraenderte Anwendung der genannten Strukturdefinitionen auf dasselbe
Pseudosingulett. Der Befund bestimmt nicht, welche Quellenstelle zu
aendern waere, und widerlegt nicht automatisch die gesamte Heim-Theorie.

## 1. Was vor der Rechnung festgelegt wurde

Der vollstaendige [Eingabevertrag](../04_reconstruction/alpha_audit/NORM-BOOK-PSEUDOSINGLET.md)
und die [fixierten Eingaben](../04_reconstruction/alpha_audit/book_pseudosinglet_inputs.json)
stehen im separaten Commit05a0bab, zeitlich vor der ersten neuen Rechnung.
Es wurden nach Sichtung der Ergebnisse keine weiteren Profilachsen ergaenzt.

Primaerquelle ist H004, *Elementarstrukturen der Materie II*, Ausgabe1996.
Der [Quellenumfang](../03_notes/BOOK_PSEUDOSINGLET_SOURCES_2026-09-06.md)
trennt Druck-/PDF-Seiten, eigene Vollsicht und Agentenlekture.

| Eingabe | Buchanker Druck/PDF | Festlegung |
|---|---|---|
| Muster3 | 289/295,(101a);291/297,(101b);330/336 | Pseudosingulett, k=P=Q=kappa=q=1; negative Komponente epsilon=1,qx=-1,C=0 |
| Resonanz | 327/333 | N=0, f(0)=0; nicht n_j=0 |
| Geruestoffsets | 277/283,(98b) | Q_j=(3,3,2,1); N_(j)=n_j+Q_j |
| Eta-Familie | 266-267/272-273,(98) | eta_(q,k)=pi/[pi^4+q^4(4+k)]^(1/4); eta=eta_(1,0) |
| xi und vartheta | 275/281;33/42 | xi=(1+sqrt(5))/2; vartheta=5eta+2sqrt(eta)+1 |
| Alpha-Primarprofil | 302/308,(105)/(105a) | Kleiner positiver Zweig mit Y3=1, A1 aus eta_(1,1), A2 aus eta_(1,2) |
| Alpha-Druckprofil | 302/308 | Separater Input alpha=0.007297354572, keine behauptete exakte105-Loesung |
| Zonenkoeffizienten | 278/284,(98c) | Buchformen fuer alpha1,alpha2,alpha3; keine H006/H010-Substitution |
| A16 | 335/341,(109b) | A16=(pi e)^2[1+alpha(1+6alpha/pi)/(5eta)]Y9; Y9=1 |
| W | 330/336,(108)/(108a);334/340,(109a) | W=g(1+eta11*A16), W1=W bei N=0 |

Die Annahmen Y3=1 und Y9=1 sind durch die Tabellenpolitik der Einfuehrung
Druck1/PDF12 motiviert, nicht hergeleitet und nicht nach Resten angepasst.
Das unindizierte Folgenverhaeltnis Y=xi^2 aus der alpha3-Konstruktion ist
weder Y3 noch Y9. In98c/g wird kein weiterer Y-Faktor ergaenzt.

Die Autorenzuordnung von Muster3 zum Myon ist empirisch; sie wird durch
diese Rechnung nicht als unabhaengige physikalische Herleitung bestaetigt.
Die Konfigurationssignatur (1111) ist kein Besetzungstupel. Ebenso ist
N=0 nicht der Geruestfall n_j=0 des anderen Spinors mit kappa=0.

## 2. Der aktive Rechenweg

Mit eigenen Abkuerzungen d=eta11 und s=sqrt(d) ergibt98c fuer k=q=1:

\[
\alpha_1=(1+s)/2,\quad\alpha_2=1/d,\quad
\alpha_3=1-H_{\rm Korr}-G_{\rm Korr},
\]
\[
H_{\rm Korr}=\frac{\alpha(1+s)\xi^3}{3d^3},\qquad
G_{\rm Korr}=\frac{2\xi d}{e}\left(\frac{1-s}{1+s}\right)^2.
\]

Diese disambiguierenden Namen bezeichnen Heims lokale H/G-Korrekturen,
nicht die Zonenpolynome G_j oder spaetere Massenpolynome.
Die Quelle nennt die vorausgehende Koeffizientenwahl auf275 empirisch
angepasst; korrekte Auswertung ist kein nachtraeglicher Herleitungsbeweis.

Aus der linearen108a und dem aktiven109a-Term folgt w=1+d*A16;
anschliessend g=27alpha1+9alpha2+2alpha3+exp(-1/3) und W=g*w.
Der Pfad benoetigt weder beta noch A26/A31 oder eine numerische
0^0-Vereinbarung fuer die alternative Potenzdarstellung109.
Nicht behauptet wird eine Pruefung der gesamten inaktiven Matrix.

Die Auswahl340-342 maximiert nacheinander den kubischen, quadratischen
und linearen Beitrag. Beide fixierten Profile erreichen 0<W4<1 und
0<W5=-3ln(W4)<alpha3*N_(3). Es greifen weder Saettigung noch Transfer.
Gewoehnliches TRC ergibt N_(4)=floor(W5)=7; die unbestimmte endliche
Neuner-Ausnahme wird nicht durch ein erfundenes Epsilon implementiert.

| Groesse, gerundete Rechenausgabe | Gleichung105, Y3=1 | Alpha-Druckwert |
|---|---:|---:|
| alpha | 0.007297354597567 | 0.007297354572 |
| alpha3 | 0.978658789856464 | 0.978658789931195 |
| A16 | 73.0360701176662 | 73.0360701172790 |
| W1 | 2830.263257668096 | 2830.263257664228 |
| W4 | 0.0784852851812753 | 0.0784852803410499 |
| W5 | 7.63453236505430 | 7.63453255006575 |
| Rest108, links minus rechts | +0.0184866826831298 | +0.0184866875233552 |

Dies sind dimensionslose Rechenausgaben, keine entsprechend genauen
physikalischen Vorhersagen. Der zweite Alpha-Wert ist unsere deklarierte
Druckwert-Sensitivitaet; die Ursache seiner Abweichung von105 ist dadurch
nicht als Rundung erklaert. Kein Profil wurde nach kleinerem Rest gewaehlt.

## 3. Die direkte Strukturpruefung

98e auf278/PDF284 definiert die G_j ohne alpha_j. Druck323/PDF329
schreibt die vier Differenzen ebenfalls ausdruecklich ungewichtet:

\[
G=\left(\frac{N_1^2(N_1+1)^2}{4},
\frac{N_2(N_2+1)(2N_2+1)}6,\frac{N_3(N_3+1)}2,N_4\right),
\quad D=\delta G=(N_1^3,N_2^2,N_3,1).
\]

Hier stehen N1..N4 nur fuer die vier N_(j), nicht fuer Resonanzordnungen.
Gewoehnliche Rueckwaertsdifferenzen bestaetigen die gedruckten
Polynomidentitaeten; dies ersetzt keine allgemeine metronische Axiomatik.

107 auf321/PDF327 fordert D_j>G_(j+1) sowie D_j>=D_(j+1).
107a auf328/PDF334 schreibt fuer den nicht kollabierten Zweig
beta_(j+1)=D_j-G_(j+1)>=1. Die Exaktauswertung des selektierten Tupels ist:

| Uebergang | D_j | G_(j+1) | Bandbreite | Nicht kollabierte Bedingung |
|---|---:|---:|---:|---|
| Zone1 -> Zone2 | 2744 | 285 | 2459 | bestanden |
| Zone2 -> Zone3 | 81 | 91 | -10 | nicht bestanden |
| Zone3 -> Zone4 | 13 | 7 | 6 | bestanden |

Die zweite Reihe 2744>=81>=13>=1 und das Zentrumsgate D1>0 bestehen.
Die eine bestandene Reihe ersetzt die andere nicht. Der Kollapsfall
ist in107a bei beta_j=0 mit G_j->0 und Aenderung der vorigen Besetzung
beschrieben; beta3=-10 ist nicht dieser Rand. Es wird keine nachtraegliche
Kaskade oder andere Besetzung als angebliche Buchvorschrift eingesetzt.
Die numerisch nicht vorgegebenen oberen Grenzen L_j/L_N sind nicht validiert.

## 4. Zwei weitere, davon getrennte Anschlussfragen

### 4.1 spaetere sigma-Bandbreite

107b auf329/PDF335 setzt dagegen beta4=alpha3*N3-N4; auch341 verwendet
den gewichteten Ausdruck. Mit den vorherigen ungewichteten Definitionen
ist das nicht dieselbe Groesse wie beta4=N3-N4:

\[
\beta_{4,\sigma}-\beta_{4,107a}=(\alpha_3-1)N_3.
\]

Im Primarprofil stehen deshalb 5.722564268134... und6 nebeneinander.
H_Korr>0,G_Korr>0 geben hier alpha3<1, also ist die Differenz bei N3=13
streng negativ. Eine entsprechende Umdefinition von G_j oder delta_j
wurde im direkt geprueften Anschluss278 sowie321-330 nicht gefunden.
Die spatere sigma-Anregungsdeutung wird nicht ungeprueft zu einem
allgemeinen N=0-Zustandspraedikat erweitert. Insbesondere werden nicht
alle107-Gates still mit alpha_j gewichtet. Diese lokale Definitionsfrage
ist von der bereits gescheiterten direkten Zone2->3-Bedingung getrennt.

### 4.2 Gleichungsrest und begrenzte Unmoeglichkeit einer N3-Reparatur

Der positive108-Rest entsteht durch floor(W5): exp(-7/3)-W4>0.
Er ist kein Massenfehler. Wie in Etappe29 gilt fuer den realen Logwert
die Umkehrung; Ganzzahlauswahl und exakte Erhaltung sind nicht identisch.

Bei festem N2=9 wuerde die direkte Strukturbedingung
N3(N3+1)/2<81 verlangen, also N3<=12, weil T12=78 und T13=91.
Laesst man N1=14,N2=9 und W unveraendert, braucht die exakte108 bei
N3=12 jedoch den Exponentialwert

\[
W_3-12\alpha_3=W_4+\alpha_3
\approx1.05714407504>1.
\]

Bei kleinerem N3 wird dieser Wert noch groesser. Fuer reelles N4>=0
gilt dagegen exp(-N4/3)<=1. Ein blosses Senken von N3 kann daher unter
diesen festen Vorstufen nicht zugleich die direkte Strukturbedingung
und die exakte Gleichung retten. Das ist keine Unmoeglichkeitsaussage
ueber andere N1/N2, alle Y-Werte oder eine anders begruendete Auswahlregel.
Es wurde keine Nachsuche nach passender Besetzung oder Masse betrieben.

## 5. Absicherung und Grenzen

Der neue [Rechner](../scripts/audit_book_pseudosinglet.py) hat einen
hashgebundenen Eingabevertrag und getrennte Ausgaben fuer Auswahl,
107/107a und107b. Er ist kein allgemeiner Spektrums- oder Massenloeser.
Der [Snapshot](../05_analysis/book_pseudosinglet_results.json) enthaelt
auch Zwischenschritte, Randabstaende und fehlgeschlagene Gates.

- Root: 80/120-Stellenvergleich; unabhaengig: Machin-pi, anderer kleiner
  Alpha-Loeser und eigene Formelimplementierung bei120/160Stellen.
- Root fuehrte den selbstenthaltenen Numerikblock erneut aus:84 benannte
  Decimalfelder gegen Root120, maxabs4.5725614163e-115; exakte Tupel/Gates gleich.
  Die 84Felder enthalten Aliase, nicht84unabhaengige physikalische Befunde.
- Kleinster numerischer Greedyabstand >0.0784, Integerabstand des W5
  >0.3654, Rohwertkappenabstand >5.0880. Kein gerichteter Intervallbeweis
  und keine physikalische Fehlergrenze aus blosser Praezisionsstabilitaet.
- Unabhaengiger exakter Strukturblock:1773Pruefungen, von Root erneut
  ausgefuehrt. Vier Polynomidentitaeten per Koeffizientenvergleich;
  sein synthetisches Testgitter ist kein physikalisches Spektrum.
- 17 neue Tests,264gesamt; zwoelf Ergebnischecks einschliesslich aller
  elf alten Rechnungen bestanden, jeweilige Quellhashes unveraendert.
- Vier Reviewdateien von drei internen Agenten; kein externes PeerReview.
  Alte Rechner, Inputs, Ergebnisse und49CSV-Normalisierungen bleiben erhalten.

Dieser Schritt demonstriert somit einen konkreten Auswahlausgang mit
fehlgeschlagener direkter Buch-Strukturpruefung. Er ist keine unabhaengige
Myonvorhersage, keine Gesamtwiderlegung und keine begruendete Ersatztheorie.

## 6. Naechster Einzelauftrag

Den **Umgang mit Strukturverletzungen in der Auswahl** gezielt klaeren:
Welche gedruckte oder historische Implementierungsregel prueft107 bereits
waehrend der Maximalwahl, setzt Zonen zurueck oder deutet G/delta um?
Ausgangspunkt sind genau die Buchstellen323/328/329/340-342 und die
bereits vorhandenen historischen Auswahlroutinen (z.B. GSTRUC).
Historische Programme nur statisch als getrennte Quellen lesen, nicht
deren Konstanten oder Ergebnisse in den aktuellen Buchvertrag uebernehmen.

Ein fehlender Ruecksprung oder eine abweichende Implementierung ist
getrennt von einem Autorenerratum zu dokumentieren. Keine neue Besetzung
nach Trefferqualitaet suchen, kein Y9-Fit und noch keine Masse/F_S-Rechnung.
Erst danach waere eine eigene explizit deklarierte gekoppelte Auswahl-
diagnose als Erweiterung des Algorithmus sinnvoll zu beurteilen.
