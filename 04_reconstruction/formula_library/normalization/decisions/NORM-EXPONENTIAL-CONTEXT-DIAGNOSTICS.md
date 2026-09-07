# NORM-EXPONENTIAL-CONTEXT-001

Stand: 2026-09-06. Isolierte skalare Kontextdiagnose zu EDM2 Druck 175-179
(79)-(79c) und Wiederverwendung auf Druck 269. Keine Metronenrechnung.

## Explizite Abbildung, nicht stillschweigende Operatorgleichheit

Wir setzen E=1, mu;n -> r, halten lambda,a,b als reelle Skalare fest und
normieren den vom Tensorvorfaktor getrennten Verlauf auf H(0)=1.
Die elementare Funktion aus der skalaren rechten Seite von (79) ist

    H(r) = exp(lambda*r) *
           [(exp(2*lambda*r)-2*b*exp(lambda*r)+1)/(2*(1-b))]^(-p),
    p = a/(2*lambda).

Dies ist exakt als gewoehnliche Funktion, nicht als nachgewiesene Loesung
des vollstaendigen metronischen Operatorproblems. Die Diagnose beweist
keine K-, F/G- oder V/Q-Zuordnung. H ist unsere Bezeichnung, keine Heim-
H-Elektronenwelle. lambda und a sind nicht die eta-Konstanten von Etappe 8.

## Domaene und getrennte Aussagen

lambda>0, a>0, -1<b<1, r>=0. Die Quelle waehlt im Extremumsargument einen
engeren positiven b-Zweig; b=0 gehoert zu (79a). Negative b sind eigene
Kontrollfaelle innerhalb der reellen skalaren Funktion. b=+-1 und lambda=0
sind ausgeschlossen, keine Fortsetzung durch algebraisches Wegkuerzen.
Bei r als Laenge haben lambda und a die Einheit inverse Laenge, b und p
sind dimensionslos. Zahlenbeispiele setzen eine beliebige konsistente
Laengeneinheit, keine physikalisch gemessenen Parameter oder Fits.

1. Exakte skalare Funktion und fuehrende Asymptote mit Amplitude getrennt.
2. Rate lambda-a ist reproduzierbar. Abklingen erfordert a>lambda; Gleichheit
   und a<lambda werden als getrennte Kontrollen zugelassen, nicht der
   behaupteten abklingenden Quellenloesung untergeschoben.
3. Druck 178/269 ist proportional/asymptotisch notiert. Seine abweichende
   konstante Amplitude ist kein Beweis eines Fehlers bei freiem Vorfaktor A.
4. Positive stationaere Radien erzwingen im skalaren Abbild nicht a>lambda.
   Ein exaktes rationales Gegenbeispiel hat zwei solche Radien, aber waechst
   asymptotisch. Dies widerlegt keine nicht rekonstruierte metronische Regel.

## Rechen- und Pruefgrenzen

`scripts/audit_exponential_context.py`, eigener Snapshot und 12 neue Tests.
Decimal 40-200 Stellen, Konvergenz 80/120; exakte Fraction-Zertifikate fuer
Klammeridentitaet und Extremumsgegenbeispiel. Stabile Faktorisierung mit
t=exp(-lambda*r), d=(1-t)^2+2*(1-b)*t vermeidet grosse positive Exponenten
und die Ausloeschung nahe b=1,r=0. Kein Anspruch auf beliebig extreme
Parameterwerte oder Intervallzertifizierung der Decimal-Auswertung.

Drei unabhaengig gefundene eigene Ausloeschungsdefekte sind korrigiert:
1-b^2 als (1-b)*(1+b), Selektorzaehler als (1-t)+(1-b)*t und stabiles
1-exp(-x) per kleiner-x-Taylorreihe (sonst direkte Differenz). Tests fuer
100-stellige +-0.99...-Eingaben bei 80 Arbeitsstellen sowie r=1e-100;
letzterer gegen eine direkte 220-stellige Vergleichsauswertung.

Analytische Fehlerschranke folgt aus dem Mittelwertsatz: fuer
s=2*abs(b)*t+t^2<1 gilt |H/H_lead-1| <= p*s/(1-s)^(p+1).
Ohne diese Bedingung wird keine Schranke ausgegeben. Auch die numerische
Auswertung dieser analytischen Schranke ist gerundet, kein Intervallbeweis.

Vorhandene sieben Rechner, Eingaben, Snapshots und Originaltranskriptionen
bleiben unveraendert. Der Formelkatalog bleibt bei zwei isolierten Alpha-
Audits und wird nicht zum vollstaendigen Massenrechner hochgestuft.
Unabhaengiger Quell-/Mathematikreview und Synthesecheck sind abgeschlossen:
273 Snapshotfelder und 32 empfindliche Randfelder separat nachgerechnet,
98 Gesamttests. Nachweise im Etappenbericht und EXPONENTIAL_MATH-Review.
