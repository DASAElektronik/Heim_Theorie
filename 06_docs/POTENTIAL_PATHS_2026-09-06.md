# Potentialpfade: gekoppelte Komponenten, getrennte Integrationsbeitraege

2026-09-06, Etappe 22. Ausgang 377d5e5, Plancheckpoint 79cf5d0.
Enger Umfang: H004 (98), Parameterkontext und H/G-Grenzen II272-274.
Keine neue Teilchenrechnung, empirische Pruefung oder Theoriereparatur.

## Ergebnis

Die vier fuer H/G verwendeten Komponentenpotentiale sind unter festen
gemeinsamen Faktoren nicht unabhaengig: Sie liegen algebraisch auf einer
eindimensionalen Kurve. Die gedruckten Integrationsgrenzen lassen sich
aber nicht als gleichzeitige Anfangs- und Endwerte dieser unveraenderten
Kurve lesen. Schon die zwei H-Untergrenzen verlangen verschiedene Punkte.

Das widerlegt eine von uns gepruefte ZUSATZLESART, nicht unmittelbar
Heims Konstruktion: Das Buch schreibt getrennte Integrale und verwendet
gewichtete Zonenanteile, abgeklungene Referenzwerte und sogar einen Wechsel
zwischen Komponentenarten. Diese Lesart erklaert die Endquotienten besser
als ein einziger unveraenderter Komponentenpfad. Eine Zuordnung der
Zwischenwerte zum metronischen Operator ist damit weiterhin nicht geliefert.

FIND-034 wird deshalb als offene Herleitungsfrage dokumentiert, nicht als
neuer unbedingter Widerspruch oder berechneter Massenfehler.

## 1. Welche Groessen sind gekoppelt?

H004 II266/267, PDF272/273, definiert

    eta_qk = [1+(4+k)*q^4/pi^4]^(-1/4),
    s = sqrt(eta_qk) = [1+(4+k)*q^4/pi^4]^(-1/8).

s ist unsere Kurzbezeichnung, keine neue freie physikalische Variable.
Bei endlichem q>0,k>0 gilt 0<s<1. s=1 ist der formale q=0-Wert;
s=0 wird bei festem k nur im Grenzabschluss erreicht. Fuer die folgende
Algebra erweitern wir bewusst auf 0<=s<=1. Diese groessere Vergleichsmenge
ist keine Erlaubnis, q kontinuierlich als physikalische Ladung zu veraendern.

II263/264 beschreibt k als konstante Konfigurationszahl. II272/273 haelt
den Radius und epsilon fest. Wenn ausserdem q festliegt, sind s und die
folgenden skalaren Komponentenwerte bestimmt. Die geprueften Seiten
definieren q nicht als Laufvariable von delta_e. Auch ein Vergleich von
V(k=1) und V(k=2) ist noch keine Schrittfolge in k.

Mit dem Potentialgesetz 4*pi*epsilon0*V_xy=e_x*e_y*f(r), gemeinsamem
Radius/Faktor und gleichem positiven epsilon-Zweig setzen wir P=V_epsilon>0.
Aus den Komponenten von (98) folgen dann genau diese vier normierten Paare:

| Eigene Kurzform | Komponentenpotential / P | Wert im erweiterten Abschluss |
|---|---|---|
| U(s) | V_(omega,epsilon)/P=(1+s)/2 | 1/2 bis 1 |
| R(s) | V_(rho,rho)/P=s^2 | 0 bis 1 |
| O(s) | V_(omega,omega)/P=(1+s)^2/4 | 1/4 bis 1 |
| D(s) | V_(delta,delta)/P=(1-s)^2 | 0 bis 1 |

R ist hier kein Radius, D kein Differenzoperator. Die exakten Bindungen

    O=U^2,   R=(2U-1)^2,   D=4*(1-U)^2

lassen keine unabhaengige Aenderung nur einer dieser vier Komponenten zu.
U,R,O sind streng steigend, D streng fallend. Ein festgehaltener Wert
einer Komponente legt auf diesem Intervall auch die anderen fest.

Dies gilt fuer die vier genannten Paare, nicht pauschal fuer jedes V im
Buch. Die externen Referenzpotentiale V_RR und V_ee aus II268 haben einen
gesonderten q^2-Kontext. Insbesondere V_ee nicht mit internem V_(rho,rho)
verwechseln. Auch die e_C-Komponente von (98) ist hier nicht erforderlich.

## 2. Warum kein gemeinsamer unveraenderter H-Start existiert

Zusaetzliche Pruefannahme: Beide H-Integrale sollten gleichzeitig mit
denselben r,epsilon und demselben s0 auf der obigen Kurve beginnen.
Dann fordern die auf II274 gesetzten Untergrenzen

    V_alpha=P/2: U(s0)=1/2, also s0=0,
    V_epsilon=P: R(s0)=1,   also s0=1.

Beides ist unvereinbar, selbst im erweiterten Abschluss. Noch bevor eine
physikalische Schrittweite gewaehlt wird, scheitert diese gemeinsame
unskalierte Startdeutung. Daraus folgt aber kein Widerspruch zweier
getrennter Integrale mit unterschiedlichen Referenzgrenzen.

Auch der obere A1-Wert ist nicht einfach ein anderer U-Punkt: Das Buch
setzt V_beta=alpha*V_(omega,epsilon)/3 als gekoppelten Zonenanteil. Bei
der ausdruecklichen Vergleichsannahme 0<alpha<1 gilt fuer jedes sf in[0,1]

    0 < V_beta/P = alpha*U(sf)/3 <= alpha/3 < 1/2 <= U(s).

V_beta liegt damit ausserhalb der ungewichteten U-Kurve. Das ist kein
entdeckter Zahlenfehler des Faktors alpha/3: Gerade dieser zusaetzliche
Kopplungs-/Zonenfaktor wird im Buch gesetzt. Offen ist sein Anschluss an
eine durchgehende Variationsvariable, nicht seine blosse Existenz.

## 3. Was der Text stattdessen tatsaechlich integriert

H004 II273 schreibt getrennte Metronintegrale mit eigenen Grenzen;
II274 ergaenzt Zonenanteil, Abklingen und Anschlussfaktor:

| Beitrag | Gedruckte Grenzen / Rolle |
|---|---|
| H, A1 | P/2 nach alpha*V_(omega,epsilon)/3; gewichteter Zonenanteil |
| H/G, A3/B3 | P nach V_(rho,rho); unveraenderte Referenz P |
| G, B1 | V_(rho,rho)(q,k) nach V_(rho,rho)(1,1)/e; gesetztes Abklingen |
| G, B4 | V_(omega,omega) ueber P nach 2^(k-2)*V_(delta,delta) |

Beim letzten Beitrag wird die Komponentenart gewechselt; W ist nicht
einfach O(s) an zwei Stellen. Fuer k=1,2 und 0<s<1 liegen beide W-Endwerte
unter P. Der beschriebene Weg ueber P ist also im skalaren Potentialwert
zuerst auf- und dann absteigend. Ein zusammengesetztes orientiertes
Integral kann dies beschreiben; daraus entsteht kein weiterer Widerspruch.

Die schon geprueften Endquotienten bleiben algebraisch erhalten. Aus ihnen
folgen jedoch keine eindeutigen Zwischenwerte, keine identische Schrittzahl
fuer alle Kanaele und keine physikalische Kopplung an X(nu). Wir setzen
auch Referenzwerte P oder abgeklungene Werte nicht ohne Beleg mit realisierten
internen Ladungszustaenden gleich.

## 4. Auch gekoppelte endliche Schritte brauchen einen Verlauf

Fuer einen rein mathematischen gemeinsamen Komponentenpfad mit aktuellem s
und vorigem t gilt exakt, solange die jeweiligen Nenner definiert sind,

    delta U=(s-t)/2,       delta R=(s+t)*(s-t),
    r_U=delta U/U=(s-t)/(1+s),
    r_R=delta R/R=(s^2-t^2)/s^2,
    r_O=2*r_U-r_U^2.

Die quadratischen Terme sind Teil der endlichen Differenz, keine Rundung.
Unsere bisherigen beliebigen Potentialzeugen werden dadurch nicht zu
Quellenpfaden; wir ergaenzen jetzt einen staerker eingeschraenkten Zeugen.

Nur im eigenen gemeinsamen-Gitter-Modell der Etappe21 setzen wir k=1,
a=1/10, X konstant, H0=1 und S=a*(r_U-3*r_R). Die positive Rekurrenz
H_neu/H_alt=1/(1-S) liefert fuer die zwei s-Wege

    (1/2,3/4,1): H_end=16800/21659,
    (1/2,7/8,1): H_end=98000/123261.

Die Endkomponenten sind gleich, die Schrittprodukte verschieden. Im
alternativen log-additiven Grundansatz waere dagegen fuer beide
H_end^10=1/48. Die Rechnungen waehlen keinen richtigen Weg aus: konstantes
X ist hier kein positiver Fibonacci-Pfad, die s-Werte sind keine belegten
diskreten Teilchenkonfigurationen, und a ist keine eingesetzte Metronenskala.
Am Endpunkt s=1 gilt D=0; die hier aktiven U/R und H bleiben positiv.
Es wird kein G- oder lnD-Verlauf gerechnet.

## 5. Was fehlt fuer eine physikalisch verwendbare Neuberechnung?

Der H/G-Ausschnitt hat nun eine konkrete Verstaendnisgrenze:

- Definition jedes Integrationskanals jenseits seines Endquotienten;
- Wirkung von delta_e auf diese Kanalvariable und passender Summationsoperator;
- Zuordnung und gegebenenfalls Reihenfolge der Schritte relativ zu X(nu);
- Anfangswerte und ein gemeinsames Fehlerbudget des vollstaendigen Ausdrucks.

Eine positive Hilfsinterpolation zwischen den getrennten Endwerten kann
man leicht selbst konstruieren. Das beweist ihre mathematische Moeglichkeit,
aber nicht ihre Herkunft aus Heims Theorie. Wir erfinden keine solche
Interpolation als Eingabe fuer Teilchenmassen. Die exakte Schrittgleichung
aus Etappe21 bleibt deshalb ein bedingtes Pruefwerkzeug, kein Ersatzrechner.

Diese Quellenrunde ist damit abgeschlossen. Fuer denselben H/G-Pfad wird
erst bei einer konkreten neuen Definition oder identifizierten Parallel-
herleitung weitergesucht. Naechster bereits vorgemerkter, unabhaengiger
Quellenanker: H015 PDF39/41 gegen H006 XIV/XXVI, um eine historische
Exponentenabweichung quellengetreu einzuordnen. Breite moderne Empirie bleibt
nach der vom Nutzer gewuenschten Rekonstruktion; kein neuer Fit.

## Nachpruefung und Sicherung

Zwei Quellenreviews, unabhaengige Mathematikreview und Root-Vollseitenpruefung.
Root hat den gesamten eigenstaendigen Fraction-Block gelesen und erneut
erfolgreich ausgefuehrt. Zehn neue Tests in `tests/test_potential_paths.py`,
178 insgesamt; alle zehn alten Rechenchecks samt Quellhashes bestanden.
Die neuen Zeugen sind rational exakt, eine neue Dezimalpraezisionsstudie
ist fuer sie nicht erforderlich. Mit FIND-034 sind es 34 Befundgruppen,
nicht 34 Fehler. Alte Rechner, Inputs, Ergebnissnapshots und die 49
CSV-Normalisierungen bleiben unveraendert.

[Quellenumfang und Reviewpfade](../03_notes/POTENTIAL_PATH_SOURCES_2026-09-06.md).
