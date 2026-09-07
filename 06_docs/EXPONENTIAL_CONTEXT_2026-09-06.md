# Exponentialverlauf und F/G: Was der fruehere Kontext klaert

Stand: 2026-09-06. Neunte Etappe, anschliessend an die Konfigurationsauswahl.
Primaerquelle H004: EDM II, zweite unveraenderte Auflage 1996, lokale
hashgepruefte PDF. Kein moderner Messdatenvergleich und keine Gesamtbewertung.

## Ergebnis in einfachen Worten

Heims Verweis auf einen exponentiell abklingenden Verlauf ist nachvollziehbar:
Aus der gewoehnlich-skalaren Abbildung seiner Formel (79) erhalten wir fuer
grosse Abstaende denselben Exponentenkoeffizienten lambda-a, also die
positive Abklingrate a-lambda, sofern a>lambda>0 gilt. Der genaue
Verlauf ist jedoch keine reine Exponentialfunktion. Wir haben jetzt auch
den konstanten Vorfaktor und den Naeherungsfehler bestimmt.

Zwei andere Schritte sind damit nicht erledigt: Warum muss dieser
Parameterbereich gelten, und warum darf man vier Beitraege der Operator-
Spur mit den vier Potentialverhaeltnissen gleichsetzen? Das erste Argument
traegt im gewoehnlichen skalaren Abbild nicht ohne Zusatzbedingungen;
das zweite nennt Heim selbst spekulativ. Der fruehere Kontext liefert
keine gefundene Konvention, die den Auswahlknoten aus Etappe 8 aufloest.

Das ist ein begrenztes, gemischtes Ergebnis: eine reproduzierte Naeherung,
eine genauer lokalisierte offene Zuordnung und ein bedingter Rechenkonflikt.
Es ist weder ein Beweis aller metronischen Grundlagen noch eine Widerlegung
der gesamten Theorie. Insbesondere ersetzen wir Heims Operatoren nicht
unbemerkt durch gewoehnliche Differentialrechnung.

## 1. Welche Aussagen miteinander verbunden sind

| Quelle (Druck / PDF-Seite, 1-basiert) | Beitrag zur Kette | Pruefstatus |
|---|---|---|
| II 98-100 / 105-107, (58)/(58a) | Weltselektor, K, quadratischer Korrelationsselektor D, Kopplungstensor Q und Spurstruktur | Quellenbelegt; noch keine vier einzeln definierten F/G-Skalare |
| II 175-177 / 181-183, (79) | Reeller Verlauf mit Exponentialfaktor; b=cos(lambda T); Integration entlang mu in R3 | Quelle visuell gelesen; gewoehnlich-skalares Abbild explizit getrennt |
| II 177 / 183, (79a) | Spezialisierung cos K=0, also b=0 | Im skalaren Abbild reproduziert |
| II 178-179 / 184-185, (79b)/(79c) | mu;n -> r bei tau->0, grosse Abstaende, behauptetes exponentielles Nahwirkungsfeld | Rate bedingt reproduziert; Parameterbegruendung gesondert geprueft |
| II 268 / 274 | (58)/(58a) auf die C-Struktur des Ladungsfelds angewendet | Echte Quellenverbindung, keine automatisch normierte Energiegleichheit |
| II 269 / 275 | Exponentialnaeherung erneut; Spur angenaehert durch F2-F1+G2-G1; spekulative F/V- und G/Q-Zuordnung | Einzeldefinitionen/Skalenbruecke im Suchumfang nicht gefunden; alter Richtungskonflikt bleibt |

Die allgemeine Operatorstelle enthaelt auf Druck 98 einen Uebergang zu
Energiedichten mit zusaetzlicher Konstante und R3-Integration. Sie sagt
nicht einfach, die Spur sei bereits eines der dimensionslosen Verhaeltnisse
auf Druck 268. Daraus folgt eine offene Normierungsfrage, nicht allein
schon ein bewiesener Dimensionsfehler.

## 2. Praezise, begrenzte skalare Nachrechnung

Unsere Definition: E=1, mu;n -> r, feste reelle lambda,a,b, und Weglassen
des tensorindizierten Vorfaktors zugunsten H(0)=1. H ist nur unser Name
fuer diese Funktion, nicht die frueher untersuchte H-Elektronenwelle.

Es gelten lambda>0, a>0, -1<b<1 und r>=0. Die Quelle betrachtet im
Extremumsargument einen engeren positiven b-Zweig; b=0 ist (79a), negative
b sind hier eigene mathematische Kontrollen. Die singulaeren Original-
Endpunkte b=+-1 werden nicht durch algebraisches Wegkuerzen zugelassen.
Wenn r eine Laenge ist, sind lambda und a inverse Laengen, b dimensionslos.
Die jetzigen a,b sind NICHT die eta-Abkuerzungen der vorherigen Etappe.

Mit x=lambda*r, w=exp(x) und p=a/(2*lambda) wird die Klammer von (79) zu

    (1+b)/2 * [1+(w-b)^2/(1-b^2)]
      = (w^2-2*b*w+1)/(2*(1-b)).

Damit erhalten wir die elementare Funktion

    H(r) = exp(x) * [(exp(2*x)-2*b*exp(x)+1)/(2*(1-b))]^(-p).

Diese Gleichheit ist exakt fuer die definierte skalare Funktion, nicht als
Nachweis einer exakten skalaren Loesung des metronischen Gesamtsystems.
Die Entwicklung des Operators, seiner Eigenwerte und seiner zugelassenen
Randbedingungen ist damit noch nicht rekonstruiert.

### Asymptote mit kontrollierbarem Fehler

Mit t=exp(-x) ist exakt

    H(r) = [2*(1-b)]^p * exp((lambda-a)*r) * (1-2*b*t+t^2)^(-p).

Fuer feste Parameter und r->infinity folgt deshalb

    H_lead(r) = [2*(1-b)]^p * exp((lambda-a)*r),
    H/H_lead -> 1.

Die Rate lambda-a ist also bestaetigt. H geht genau dann gegen null, wenn
a>lambda gilt. Bei a=lambda bleibt eine positive Grenzamplitude, bei
0<a<lambda waechst H. Das sind unterschiedliche Parameterzweige, keine
numerischen Rundungseffekte.

Der relative Rest ist

    H/H_lead - 1 = (1-2*b*t+t^2)^(-p)-1
                = 2*p*b*t + [-p+2*p*(p+1)*b^2]*t^2 + O(t^3).

Fuer b=0 verschwindet der erste Restterm; dann beginnt der Fehler erst bei
exp(-2*lambda*r). Mit s=2*abs(b)*t+t^2<1 liefert der Mittelwertsatz zudem
die analytische Schranke |Rest| <= p*s/(1-s)^(p+1). Ihre Decimal-Auswertung
ist gerundet; das Programm ist kein Intervallzertifizierer.

Beispiele mit synthetischem lambda=1, a=1.5 (beliebige konsistente Einheit):

| b | x=lambda*r | Relativer Rest H/H_lead-1 |
|---|---:|---:|
| 0.6 | 5 | +0.00607284 (ca. 0.6073 %) |
| 0.6 | 10 | +0.0000408603 (ca. 0.004086 %) |
| 0 | 5 | -0.0000340486 (ca. -0.003405 %) |

Diese Zahlen beschreiben nur Naeherungsfehler unserer Testfunktionen,
keine experimentell bestimmten Felder oder Laengenskalen.

### Warum wir den Vorfaktor nicht als zusaetzlichen Fehler zaehlen

Druck 178 und 269 schreiben die proportionale grosse-r-Form

    exp(x) * [0.5*sqrt((1+b)/(1-b))*(exp(x)-b)^2]^(-p).

Ihre fuehrende Amplitude ist gegenueber dem normierten (79)-Abbild um
(1-b^2)^(-p/2) verschieden. Die Exponentialrate ist aber dieselbe; bei
b=0 stimmt auch der Vorfaktor. Da die Quelle proportional/approximativ
schreibt und auf Druck 269 ausdruecklich eine Amplitude A einfuehrt,
ist die konstante Differenz allein kein belastbarer Fehlerbefund.
Bei einem spaeteren Vergleich absoluter Feldstaerken muesste die
Normierung allerdings explizit festgelegt werden.

## 3. Die Parameterbegruendung ist ein eigener Pruefschritt

Druck 178 bezeichnet A=lambda/a und fordert 0<A<E, woraus es a>lambda
ableitet. Dieses A ist nicht die spaetere Amplitude A auf Druck 269.
Ausserdem verwendet die Quelle alpha zuvor fuer den Realteil eines
Selektors und spaeter fuer die Abklingrate. Wir nennen jenen Realteil hier R.

Im gewoehnlichen skalaren Abbild gilt

    H'/H = lambda - a*R(w),
    R(w) = w*(w-b)/(w^2-2*b*w+1).

Stationaritaet liefert mit A=lambda/a die Quadratik

    (1-A)*w^2 + b*(2*A-1)*w - A = 0.

Positive stationaere Radien allein erzwingen A<1 nicht. Ein exaktes,
ungefittetes Gegenbeispiel in beliebigen konsistenten Einheiten ist

    lambda=1, a=10/11, b=3/5, also A=11/10>1.
    5*w^2-36*w+55=0 -> w=11/5 oder w=5.
    r=ln(11/5)>0 ist ein Maximum; r=ln(5)>0 ist ein Minimum.

Der Verlauf waechst fuer grosse r dennoch mit Rate 1/11. Die Wurzeln und
Vorzeichen sind mit exakten Bruechen geprueft, nicht nur grafisch vermutet.
Dieses Beispiel liegt absichtlich ausserhalb der von Heim behaupteten
abklingenden Teilklasse. Es prueft deren Begruendung aus der blossen
Existenz von Extremstellen; es widerlegt NICHT das Abklingen bei a>lambda.
Eine zusaetzliche Randbedingung H(infinity)=0 wuerde fuer unsere Funktion
genau diesen abklingenden Zweig auswaehlen. Das waere hier eine offen
deklarierte Ergaenzung, keine in der Quelle nachgewiesene Herleitung.

Eine weitere lokale Pruefstelle: Druck 176 hat bei der Substitution
u=(w-b)/sqrt(1-b^2) den Nenner E+u^2; Druck 178 schreibt E-u^2. Gewoehnlich
skalar mit C=b/sqrt(1-b^2) folgt R=u*(u+C)/(1+u^2). Das Minus ist damit
nicht dieselbe skalare Umformung. C=ctg K benoetigt fuer diese positive
Wurzelzuordnung einen entsprechenden sin-K-Zweig. Die Originalseiten
wurden nicht korrigiert; die metronische Bedeutung bleibt zu klaeren.
Auch w=b ist im skalaren Abbild keine Extremstelle von H: dort waere
H'/H=lambda, und fuer 0<b<1 liegt r=ln(b)/lambda ohnehin unter null.

Wir gruppieren diese verbundenen Stellen als einen bedingten lokalen
Extremumsbefund, nicht als mehrere unabhaengige Widerlegungen. Eine
allgemeine metronische Extremwertregel oder ein Erratum kann seine
Reichweite aendern und waere Anlass fuer eine erneute Pruefung.

## 4. Was F und G in der Auswahlstelle tatsaechlich leisten

Im geprueften Rueckverweis definieren (58)/(58a) die Operatoren K, D und
Lambda/L sowie den Kopplungstensor. Druck 268 wendet diese Struktur auf
das Ladungsfeld an. Erst die lokale Passage auf Druck 269 benennt die
vier Summanden F1,F2,G1,G2 fuer eine angenaeherte Spur.

Die gepruefte Kette liefert keine vier separaten Formeln, Randwerte oder
Skalen, aus denen die Gleichsetzung mit V1,V2,Q1,Q2 berechnet werden
koennte. Gleichnamige Fremdfeldselektoren F und Protosimplexzahlen G_j
an anderen Stellen sind ohne explizite Verbindung keine Loesung dieser
Zuordnungsfrage. Der Umfang der erfolglosen Definitionssuche ist im
Quellenreview angegeben; keine Behauptung ueber jeden unveroeffentlichten Text.

Bei der tatsaechlich gedruckten, indexgleichen Zuordnung bleibt

    F2-F1+G2-G1 = V2-V1+Q2-Q1 = -R_VQ.

Positive linke Seite bedeutet R_VQ<0, nicht das auf Druck 269 als naechstes
gedruckte R_VQ>0. Die frueheren Operator-Minuszeichen kehren nicht einfach
die spaeter explizit gedruckten Indizes um. FIND-015 bleibt deshalb im
untersuchten Zusammenhang bestehen. Auch FIND-016 (u2-Zahlenbereich)
und die erhaltenen beiden Buch-Alpha-Paare werden nicht veraendert.

## 5. Reproduzierbarkeit und naechster Anschluss

Neue Dateien: `scripts/audit_exponential_context.py`,
`tests/test_exponential_context.py`,
`05_analysis/exponential_context_diagnostics.json`.
Normalisierung: `NORM-EXPONENTIAL-CONTEXT-001`.

    py -3.13 scripts/audit_exponential_context.py --check --verify-sources
    py -3.13 scripts/validate_finding_register.py
    py -3.13 -m unittest discover -s tests -q

12 neue Tests: exakte Klammeridentitaet, direkte (79)-Auswertung, (79a)
als sech-Spezialfall, drei Grenzregime, Fehlerschranke, Amplitudentrennung,
exaktes Extremumsbeispiel, Ableitung, 80/120-Stellen-Konvergenz und Domaenen.
Unabhaengige Randtests fanden drei Ausloeschungsfehler bei b extrem nahe
an +-1, darunter einen bei sehr kleinem positivem r. Faktorisierte
Auswertung und eine stabile Berechnung von 1-exp(-x) beheben sie. Eigene
Regressionen pruefen 100-stellige Eingaben bei 80 Arbeitsstellen, auch
r=1e-100 gegen eine direkte 220-stellige Vergleichsrechnung. Die regulaeren
Snapshotwerte blieben unveraendert. Das waren Fehler unseres Codes, keine
Heim-Befunde. Alle 98 Tests und acht Snapshotchecks bestehen; alte sieben
Rechner/Inputs/Snapshots wurden nicht geaendert.

Unabhaengige Reviews (jeweils 2026-09-06): EXPONENTIAL_SOURCE,
FG_IDENTIFICATION_SOURCE und EXPONENTIAL_MATH unter
`04_reconstruction/alpha_audit/reviews/`. Alle drei und der abschliessende
Synthesecheck sind abgeschlossen. Unabhaengig wurden 273 Snapshotfelder
gegen eine direkte 140-stellige Originalklammerauswertung geprueft
(groesste absolute Differenz <2.4e-79), ausserdem 32 Randfelder gegen eine
direkte 260-stellige Rechnung (mit max(1,|Referenz|) skalierte Differenz
<3.4e-78). Keine beobachtete offene Beanstandung; keine Garantie fuer alle
moeglichen Parameter oder die Wahrheit der physikalischen Interpretation.
Die sieben alten Rechner/Inputs/Snapshots bleiben unveraendert.

Register: 18 Befundgruppen (keine Fehlerzaehlung), darunter FIND-017 als
positive bedingte Reproduktion und FIND-018 als bedingter Extremumskonflikt.
49 Normalisierungsentscheidungen: 47 resolved, zwei unveraenderte historische
Massenblocker. Plan 838eba0 und Zwischenstand 8e8aa15 sind gepusht;
der Abschluss ist ueber Git und `00_admin/RESUME.md` nachvollziehbar.

Als naechstes bleibt der bereits vorgemerkte Versionsanschluss: Welche
Rolle hat eta22 in der Massenformel-Fassung 1989, und beansprucht diese
ueberhaupt dieselbe Zustandsauswahl? Danach die Abhaengigkeiten B50 und
Gamma/Q_N. Neue offene Operatorfragen werden mit konkretem Pruefanlass
in der Zusammenhangskarte gesichert, nicht durch ungezielte Varianten
oder eine vorzeitige externe Widerlegungssuche ersetzt.
