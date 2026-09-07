# F16/A16: Welche Bedingungen bestimmen den Grenzwert?

2026-09-06, Etappe28. Ausgang `1fcf209`, Plancheckpoint `c153e02`.
Fortsetzung von [Etappe27](A16_ORIGIN_2026-09-06.md). Keine neue Masse,
keine Anpassung von Y9, keine neue Autorenformel.

## Ergebnis

Die direkt geprueften Buchbedingungen legen die Rolle und den verlangten
Grenzcharakter von F16 fest, aber liefern keine eindeutige Herleitung
des Zahlenwerts A16. Das ist enger als die Aussage, A16 sei unberechenbar:
Die anschliessende heuristische Formel (109b) bestimmt A16 bei festen
Eingaben und festem Y9 durchaus. Auch die Auswahlgleichung (108) koennte
A16 festlegen, wenn ihre uebrigen Groessen unabhaengig bestimmt waeren.

Zusaetzlich ist eine zweite Frage offen: Wie schnell erreicht die unbekannte
F16 ihren Grenzwert? Im gelesenen Abschnitt wird eine sehr gute endliche
Naeherung behauptet, aber keine quantitative Fehlerschranke angegeben.
Grenzwertwert, Herleitung und Naeherungsgenauigkeit sind getrennte Fragen.

## 1. Bedingungen statt blosser Symbolsuche

Primaerquelle ist H004, Heim, *Elementarstrukturen der Materie II*,
vorliegende Ausgabe1996. Druckseiten und physische PDF-Seiten werden
getrennt angegeben. Die folgende Einordnung ist unsere Rekonstruktion
der Originalaussagen, keine nachtraegliche Axiomatik Heims.

| Quellenforderung | Fundstelle Druck/PDF | Was folgt fuer A16? |
|---|---|---|
| F_im sind metronische R3-Funktionen von Selektoren und haengen von den drei mu_s ab | 330/336 | Funktionsrolle und Argumente, keine explizite F16-Funktionsgleichung |
| Der mu_s-Ursprung ist das in R3 projizierte Korrelationszentrum | 330-331/336-337 | Koordinatenursprung, **kein** angegebener Wert F16(0) |
| F_im konvergieren bei divergierenden Metronenziffern gegen konstante endliche Grenzen | 331/337,334/340 | Existenz-/Grenzforderung, kein Zahlenwert oder Konvergenztempo |
| Grenzwerte sind reell; A_im=A_im* | 334-335/340-341 | Realitaet, keine Normierung oder Groesse von A16 |
| X6=kappa*eta_qk*F16 ist der Spinorbeitrag | 332/338 | Multiplikativer Anschluss; X6 ist dort nicht unabhaengig numerisch vorgegeben |
| Gerueststrukturen n_j=0 haben unterstrichenes w_k=0 | 325/331,330/336 | Bedingung an Strukturpotenz; im k=1-Spinor mit kappa=0 ist der F16-Beitrag schon ausgeschaltet |
| f(0)=0, f(N)>0 fuer N>0 und delta_N f>0 | 327/333,330/336 | Bedingungen an die **Resonanzfunktion f**, nicht automatisch an F16 |

Die Metronenziffern mu_s, die Besetzungen n_j beziehungsweise N_(j) und
die Resonanzordnung N sind verschiedene Groessen. Insbesondere ist
N=0 nicht dasselbe wie n_j=0 oder mu_s=0. Die drei Argumentindizes s=1,2,3
sind keine dritte Potenz der Funktion. Wir schreiben deshalb bei Bedarf
F_im(mu_1,mu_2,mu_3), ohne einen neuen Operator einzufuehren.

Die Quelle verbindet auf S.333/334 grosse raeumliche Abstaende relativ
zur Metronlaenge mit der infinitesimalen Naeherung tau gegen null.
Sie schreibt die Limesrelationen fuer die allgemeine F_im-Familie;
F16 ist als deren Eintrag erfasst, nicht durch eine zusaetzliche eigene
F16-Randgleichung. Ein bestimmter dreidimensionaler Annaeherungspfad
oder ein Fehlerbudget wird hier nicht spezifiziert. Wir variieren tau
und mu nicht als unabhaengig freigegebene physikalische Parameter.

Die Selbstkonjugation der Eintraege darf nicht in eine zusaetzliche
Symmetrie A_im=A_mi umgedeutet werden: Die Matrix ist hier vom Typ3,6.
Auch die vereinfachende Setzung A=A66 auf S.334 bedeutet nicht A16=A66.
Die Antiteilchen-/Ladungssymmetrie im Nachbarkontext S.332/333 gibt dort
keinen numerischen Normierungswert fuer den F16-Beitrag an.

Das ist auch mit Heims ausdruecklichem Forschungsauftrag vereinbar:
In der Einfuehrung S.2-3/PDF13-14 bezeichnet er die Deduktion gerade
der metronischen R3-Strukturfunktionen als noch ungeloest. Ihre Grenzen
sollten die Koeffizientenmatrix(110d) liefern und damit den Beziehungen
(109)-(111) ihren heuristischen Charakter nehmen. Auf S.340/PDF346
fasst(110d) die Koeffizienten aus(109b), darunter A16, mit den weiteren
aus(110c) zusammen. Die Einfuehrung meint somit einen konkret
angeschlossenen Herleitungsauftrag, nicht nur einen allgemeinen Vorbehalt.
Sie beweist nicht, dass in spaeteren Arbeiten keine Loesung gefunden wurde.

## 2. Warum der Geruestfall den Myonkoeffizienten nicht kalibriert

Heim unterscheidet auf S.330 fuer k=1 zwei Spinorrollen Q=1:
kappa=0 wird als Geruest interpretiert; kappa=1,q=1 bezeichnet das
Pseudosingulett. Mit d=eta_qk gilt im betrachteten Anschluss

\[
\underline w_1=\kappa QdF_{16}\quad(Q=1),\qquad
w=1+\underline w_1\quad(k=1).
\]

Bei kappa=0 liefert das fuer jedes endliche F16 bereits w=1. Die
Geruestforderung misst dann F16 nicht. Im anderen Fall kappa=Q=q=k=1
bleibt der Beitrag aktiv und nach Grenzwertsubstitution gilt

\[
w=1+dA_{16},\qquad W=g(1+dA_{16}).
\]

Das ist die lokale Buchrolle; die fruehere H006-Signatur wird nicht
mit der Buchsignatur gleichgesetzt. Wir beweisen damit keine beliebige
F16-Aenderung als Loesung aller anderen Heim-Gleichungen.

## 3. Ein exakter Test der reduzierten Grenzforderung

**Eigene mathematische Diagnose, keine Heim-Loesung:** Fuer einen
gewoehnlichen skalaren Folgenindex m=0,1,... betrachten wir

\[
h_a(m)=a+\frac{1}{m+1},\qquad a\in\{1,2\}.
\]

Beide Folgen sind positiv und endlich, besitzen einen konstanten reellen
Grenzwert und haben sogar denselben Rest 1/(m+1). Ihre Grenzwerte sind
dennoch verschieden. Die Konvergenz folgt aus diesem expliziten Rest:
Fuer jedes epsilon>0 ist er bei m+1>1/epsilon kleiner als epsilon.
Mit demselben festen Faktor c erfuellen beide x_a(m)=c*h_a(m).

Damit folgt aus **genau** Realitaet, Endlichkeit, Konvergenz und einem
linearen Anschluss ohne vorgegebenen Ausgangswert keine eindeutige Zahl.
Weder der Folgenindex noch diese Funktionen sind als Heims metronische
R3-Selektoren ausgewiesen. Der Zeuge beweist keine Nicht-Eindeutigkeit
des vollstaendigen, noch nicht rekonstruierten metronischen Problems.

Selbst eine zusaetzlich erfundene Bedingung h(0)=0 wuerde allein nicht
helfen: h_a(m)=a*m/(m+1) hat denselben Nullwert und verschiedene Grenzen.
Das ist nur ein staerkeres eigenes Gegenbeispiel; F16(0)=0 steht hier
gerade **nicht** in der Quelle und wird nicht als Modellannahme eingesetzt.

## 4. Welche weitere Angabe A16 tatsaechlich festlegen koennte

Die Auswahlgleichung (108) darf nicht unterschlagen werden. Unsere
Abkuerzung T108 bezeichne ihre vollstaendige linke Seite mit den N_(j),
nicht eine Lebensdauer. Im oben festgelegten aktiven k=1-Fall gilt nach
Grenzwertsubstitution

\[
T_{108}=g(1+dA_{16})(1+f).
\]

Bei **unabhaengig gegebenen** T108,g,d,f mit g,d>0 und f!=-1 folgt
algebraisch eindeutig

\[
A_{16}=\frac{T_{108}/[g(1+f)]-1}{d}.
\]

Denn die Differenz der rechten Seiten zu A und A' ist
g*d*(1+f)*(A-A'), bei A!=A' also nicht null. Dies ist eine bedingte
positive Bestimmtheit; weitere Bereichs-/Strukturbedingungen sind
dadurch noch nicht bewiesen. Mit f=-1 waere die Inversion unzulaessig.

Auf S.327 beschreibt Heim gerade den beabsichtigten Weg, w und f auf
die Grundmuster zurueckzufuehren und damit die Besetzungen auszuwaehlen.
S.340/PDF346 bestaetigt die Rechenrichtung: Aus(108)-(110d) werden
W,a,b und damit der Generator berechnet; anschliessend beginnt die
Exhaustion zur Bestimmung der Besetzungszahlen.
Sind die N_(j) erst aus W(A16) zu bestimmen, ist T108 keine unabhaengige
Eingabe. Dann muss das gekoppelte Problem geloest werden. Umstellen
allein beweist weder seine Eindeutigkeit noch einen freien Parameter.
Wir setzen keine Besetzungs-/Messwerte ein und behaupten keinen
historisch nachgewiesenen Rueckwaertsfit.

Die Alternative in (109b), naemlich A16 aus Heims heuristischer Formel
bei festem Y9 auszurechnen, bleibt eine konkrete Rechenvorschrift.
Sie ist nur nicht schon durch das reduzierte Grenzargument hergeleitet.

## 5. Warum ein grosser Abstand noch keine Fehlerzahl liefert

S.334 behauptet eine Abweichung weit unter der Messbarkeitsgrenze,
sofern die A_im richtig bestimmt sind. Eine Rate ist dort nicht angegeben.
Als **eigene skalare** Demonstration betrachten wir bei festen a,b,L>0

\[
h_L(m)=a+\frac{bL}{L+m}.
\]

Jede einzelne Funktion mit festem L konvergiert gegen a. Fuer
0<epsilon<b gilt jedoch genau

\[
|h_L(m)-a|\le\epsilon
\quad\Longleftrightarrow\quad
m\ge L(b/\epsilon-1).
\]

Ohne Kenntnis oder Schranke der Skala L folgt kein gemeinsamer endlicher
Schwellwert fuer diese Familie: Zu jedem noch so grossen m>0 liefert
das Familienmitglied L=m einen Rest b/2. Dabei wird fuer verschiedene m
eine andere Funktion gewaehlt; wir bestreiten **nicht** die Konvergenz
einer einzelnen Funktion bei festem L.

L ist keine eingefuehrte Heim-Konstante. Das Beispiel zeigt nur, welche
Information die blosse Grenzexistenz nicht liefert. Es beweist weder,
dass Heims tatsaechliche F16 langsam konvergiert, noch dass seine
Naeherung experimentell falsch ist. Dafuer braeuchte es die wirkliche
Funktion oder eine begruendete Restabschaetzung und einen Quellenanschluss
an die betreffende Messgroesse.

## 6. Quellenabschluss und Nachpruefung

Direkte Rueckverweise werden in der Quellenreview mit ihren genauen
Seiten aufgefuehrt. (101a)/(101b) liefern Grundmuster und empirische
Teilchenzuordnung; (105)/(105a) die dort verwendeten Kopplungen. Das ist
keine zusaetzliche F16-Normierung. (98) auf S.267/PDF273 gibt den
eta-/Ladungsanschluss, (98a) auf S.269/PDF275 eine bedingte k/q-Auswahl,
aber keine F16-Dynamik. Die bereits dokumentierten offenen
Alpha-Befunde werden hier weder neu untersucht noch ueberschrieben.

Zehn neue exakte Fraction-Tests pruefen die eigenen reduzierten Zeugen,
Restschranken, Schalter und bedingte Inversion. Die allgemeine Begruendung
steht oben; endliche Teststichproben ersetzen keinen Konvergenzbeweis.
Root fuehrte zudem den unabhaengigen Mathematikreviewblock erneut aus:
52 exakte Kontrollfaelle bestanden. Drei interne Reviews, kein externes
Peer Review. Kein neuer Massenrechner oder Dezimalsnapshot.

Gesamtsuite234Tests und alle elf bestehenden Snapshotchecks samt den
jeweiligen Quellhashkontrollen bestanden. Alte Rechner, Inputs, Snapshots
und49CSV-Normalisierungen bleiben unveraendert.

Quellenumfang/Hash: [F16_DETERMINACY_SOURCES](../03_notes/F16_DETERMINACY_SOURCES_2026-09-06.md).
Der Befund wird als **FIND-038, open_justification** gefuehrt, nicht als
neuer Rechenfehler und nicht als globale Widerlegung.

## 7. Naechster Einzelauftrag

F16 wird nicht ohne neuen Quellenanker erneut auf dieselbe fehlende
Herleitung durchsucht. Stattdessen folgt die **Buch-Auswahl/Exhaustion
auf Druck340-342/PDF346-348**: Wie werden die schon eingesetzten W-Werte
in Besetzungen ueberfuehrt, welche TRC-/Transferregeln gelten, und
welche Bedingungen kommen dabei wirklich hinzu? Erst die getrennte
Rekonstruktion darf mit H006/H015 und deren alten Restbefunden verglichen
werden. Keine stillschweigende Editionsgleichheit, keine neue Masse,
keine Y9-Wahl nach Output. Der auf S.342 beginnende F_S-Anschluss
bleibt ein spaeterer eigener Auftrag.
