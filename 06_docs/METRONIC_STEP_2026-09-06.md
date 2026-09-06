# Skalierung oder kleiner Schritt? Die konkrete M7-/H/G-Bruecke

2026-09-06, Etappe 21. Ausgang38d89c8, Plancheckpoint94a049c.
Quellen: H003I106-111, H004II271-275; vorige M2/M2a-Lesung als Kontext.
Keine neue Massenrechnung, keine Empiriepruefung und keine Gesamtwiderlegung.

## Ergebnis und Praezisierung gegenueber Etappe 20

Heim fuehrt delta_e in M7 zunaechst als Faktor a*delta ein. In der
Erlaeuterung seiner Exponentialnaeherung wertet er dann jedoch wirklich
einen um delta_e phi verschobenen inneren Funktionswert aus. Ein kleiner
innerer Schritt ist damit im Text **vorhanden**, nicht bloss eine von uns
erdachte Rettungsmoeglichkeit. Es fehlt im geprueften Abschnitt aber die
Herleitung, dass diese Operation gleich dem skalierten M2-Operator ist.

Unsere exakte Gegenrechnung zeigt: Auf allgemeinen skalaren Folgen sind
das verschiedene Operationen. Auch sehr kleines a allein beseitigt ihren
relativen Unterschied nicht. Dies ist der neue, engere Befund FIND-033.
Ein eigenstaendiger fraktionaler Index-/Gitterschritt ist damit weder
definiert noch widerlegt. Heims Absicht einer Naeherung ist belegt;
eine konsistente exakte Operatoridentitaet folgt daraus nicht.

Die H/G-Gleichungen enthalten zudem unveraendert zwei Notationen:
delta_e an den Potentialen, unskaliertes delta an H, G und X. Ein kleiner
Potentialschritt verkleinert den gedruckten X-Schritt daher nicht automatisch.

## 1. Die konkrete Stelle in M7

H003I106/PDF112 wiederholt den M2-Argumentschritt n nach n-1.
I108/PDF114, M5, fordert eine metronische Stammfunktion mit delta Phi=phi.
Auf I109/PDF115, M7, folgen nach delta_e=a*delta und der Kleinheitsannahme
f=exp(phi) und die Auswertung

    delta_e f = exp(phi)-exp(phi-delta_e phi).

Die umgebende Prosa behandelt infinitesimale Approximationen; die daraus
gewonnenen Log-/Exponentialregeln werden mit Naeherungszeichen gedruckt.
Der hier geschriebene Auswertungsschritt ist aber nicht die Wirkung von
a mal derselben Rueckwaertsdifferenz auf f. Mit u=delta phi und U=exp(phi)>0
lauten die beiden Ausdruecke, fuer unseren Vergleich eindeutig benannt,

    L = a*delta exp(phi) = a*U*(1-exp(-u)),
    R = U*(1-exp(-a*u)).

u ist unser Exponentsprung, nicht Heims Ladungszahl q. Fuer 0<a<1,u!=0
gilt R>L, weil 1-exp(-a*u) als Funktion von a streng konkav ist und bei
a=0 verschwindet. Bei a=0,a=1 oder u=0 stimmen die Ausdruecke ueberein.

Ein exakt auswertbarer Zeuge ist exp(phi_n)=4,exp(phi_(n-1))=1,a=1/2:

    L = (4-1)/2 = 3/2,
    R = 4-exp(ln4/2) = 4-2 = 2.

a=1/2 ist kein behauptetes metronisches Kleinheitsregime, sondern ein
Identitaetszeuge. Die Kleinheitsfrage wird gesondert entschieden: Fuer
festes u!=0 und a->0 von oben gilt

    (R-L)/a -> U*(u-1+exp(-u)) > 0,
    (R-L)/abs(L) -> (u-1+exp(-u))/abs(1-exp(-u)) > 0.

Der absolute Unterschied verschwindet, der relative nicht. Bei u=ln4
betraegt der letztere Grenzwert rund0.8483924814931875. Dies ist keine
Unsicherheit einer Teilchenmasse. Wirklich kleines u liefert dagegen
R-L=U*a*(1-a)*u^2/2+O(u^3), eine andere, zu belegende Voraussetzung.

## 2. Was ist damit ueber ein Argumentgitter bekannt?

Die Quelle benutzt phi-delta_e phi als inneres Argument. Sie gibt hier
keine Gleichung phi(n-h)=phi(n)-a*delta phi(n), keine Schrittweite h und
kein Gitter fuer nichtganzzahlige n-h an. Selbst eine solche Gleichung
fuer eine einzelne Funktion waere nicht automatisch ein gemeinsames
Argumentgitter fuer alle Funktionen.

M8 auf I110/PDF116 definiert fuer eine zulaessige neue Variable phi einen
endlichen dividierten Quotienten, nicht pauschal eine infinitesimale
Ableitung. I111/PDF117 begrenzt die verallgemeinerte Kettenregel und
verlangt individuelle Durchfuehrung. Das liefert keinen stillen Beweis
der Gleichheit L=R. Die eng korrekte Aussage lautet daher: Belegte
innere Verschiebung im M7-Naeherungsansatz, aber offene Verbindung zur
zuvor genannten skalaren Operatorwirkung und zur spaeteren Integration.

## 3. Die gemischten H/G-Gleichungen bleiben gemischt

H004II272/273, PDF278/279, druckt

    delta H/H = A1*delta_e V_omega/V_omega
                + A2*delta X/X + A3*delta_e V_rhorho/V_rhorho,
    delta G/G = B1*delta_e V_G/V_G + B2*delta X/X
                + B3*delta_e V_rhorho/V_rhorho + B4*delta_e W/W.

V_G steht hier zur Kuerzung fuer den gedruckten Ausdruck V_(rho rho)(G),
nicht fuer einen neu bestimmten Potentialpfad. Delta_e betrifft laut
Quelle die internen Ladungsfeldkomponenten aus(98), bei festem Radius
und konstantem epsilon. X(nu) ist dagegen eine gesonderte Zaehlerfolge
am Uebergang j=3 nach j=4. Auch die logarithmischen Zeilen behalten
diese Glyphentrennung. Ein delta_e X oder eine gemeinsame Skalengleichung
steht in diesem Abschnitt nicht. Das kleine x in der vorherigen
f(x)-Analyse darf nicht mit dem danach eingefuehrten grossen X verwechselt
werden. Der Potentialstrich fixiert k=1, keine Ableitung.

Heim waehlt auf II275 A2=(2k+1)/2 und B2=k/2. Dasselbe X hat deshalb
verschiedene Gewichte. Die empirische Koeffizientenwahl ist keine neue
Herleitung eines gemeinsamen Schrittparameters.

## 4. Eine exakte bedingte Rekonstruktion statt des Logaustauschs

Wenn wir ZUSAETZLICH ein gemeinsames Rueckwaertsgitter, positive skalare
Nachbarwerte und delta_e=a*delta auf diesem Gitter voraussetzen, folgt
mit r_X=delta X/X, r_i=delta V_i/V_i fuer den H-Zweig

    S_H = A2*r_X+a*(A1*r_1+A3*r_3),
    H_n/H_(n-1) = 1/(1-S_H).

Bei positivem H_(n-1) ist eine positive Fortsetzung genau fuer S_H<1
moeglich. G hat die entsprechende Form mit seinen B-Gewichten und drei
Potentialanteilen. Ueber mehrere Schritte entsteht ein Produkt dieser
Faktoren, nicht ohne Weiteres nur ein Quotient der Endpotentiale.

Mit E(r)=-ln(1-r)-r lautet der ganze Logrest exakt

    delta lnH-A2*delta lnX-a*sum_i A_i*delta lnV_i
      = E(S_H)-A2*E(r_X)-a*sum_i A_i*E(r_i).

Damit werden die linke H-Variation und alle Potentialreste beruecksichtigt.
Aufhebungen sind moeglich; der isolierte X-Rest reicht fuer einen realen
H/G- oder Massenfehler weiterhin nicht. Das gemeinsame Gitter ist eine
offen genannte Zusatzannahme, keine von uns entdeckte Quellenidentitaet.

Eine alternative exakte Konstruktion koennte stattdessen die gedruckte
Loggleichung als Grundansatz setzen. Dann waere der einzelne H-Faktor

    (X_n/X_(n-1))^A2 * product_i (V_i,n/V_i,n-1)^(a*A_i).

Das ist im Allgemeinen nicht 1/(1-S_H). Die zwei Konstruktionen sind
moegliche, voneinander verschiedene mathematische Modelle; keine davon
wird hier als verbesserte oder authentisch vervollstaendigte Heim-Theorie
eingesetzt. Fuer beide fehlen konkrete Potentialpfade, gemeinsame
Indexzuordnung und Anfangswerte. Alte Rechenprofile werden nicht ersetzt.

## 5. Warum Endwerte nicht immer genuegen

Synthetischer Zeuge: X konstant, nur ein Potentialterm aktiv, a=1/2,
A1=1,H0=1. Die beiden Wege V=(1,2,4) und V=(1,3,4) besitzen dieselben
Endwerte. Die exakte additive Differenzgleichung liefert aber

    H2 = 16/9  beziehungsweise  12/7.

Nach der logarithmischen Endpunktregel kaeme fuer beide 2 heraus.
Dies zeigt die benoetigte Zusatzinformation: Anfang und Ende allein
bestimmen die endliche gewichtete Schrittbilanz nicht. Die Wege erfuellen
keine behauptete vollstaendige Heim-Konfiguration und sind keine Datenfits.

Ein zweiter Test haelt alle Potentiale konstant und laesst nur X variieren.
Im Fibonacci-Grenzfall hat der ganze Einzelschritt-Logrest bei k=1 fuer H
das Vorzeichen plus (rund0.1290341), fuer G minus (rund-0.02867056).
Bei G,k=2 verschwindet er exakt, weil B2=1. Eine unbedingte Aussage,
saemtliche Beitraege haetten gleiches Fehlervorzeichen, waere somit falsch.
Diese Tests zeigen ausschliesslich Verhalten der bedingten Rekurrenz.

## Nachpruefung und enger naechster Schritt

Zwei Quellenreviews, eigenstaendige Mathematikreview und Root-Vollseiten-
gegenlesung. Root fuehrte den Reviewcode separat aus: zehn Felder80/120
Stellen, max.relative Abweichung2.550612081569e-80. Zehn neue Tests in
`tests/test_metronic_step.py`,168gesamt; alle zehn alten Snapshot- und
Quellhashchecks bestanden. FIND-033:33Befundgruppen, nicht33Fehler.
Keine alten Rechner, Eingaben, Ergebnissnapshots oder49CSV-Normalisierungen
geaendert. Vorige Befunde erhalten sichtbare Praezisierungsnachtraege.

Naechster neuer Anker: Die Potentialkomponenten aus(98) und H004s
benannte Integrationsgrenzen auf einen gemeinsamen Variationsparameter
pruefen. H003M7/M8/M5 bleiben Anforderungen an dessen Operatorzuordnung,
nicht Anlass fuer eine Wiederholung derselben Suche.
Insbesondere: Was bleibt bei festem k konstant, wodurch variieren dann
die Komponenten aus(98), und wie wird diese Variation an X(nu) gekoppelt?
Erst eine solche Zuordnung oder klar deklarierte eigene Modellannahme
erlaubt das Produkt oben als physikalischen Rechenweg auszuwerten.
Keine identische Quellensuche ohne neuen Anker, kein Massenziel-Fit.

[Quellenumfang und Reviewpfade](../03_notes/METRONIC_STEP_SOURCES_2026-09-06.md).
