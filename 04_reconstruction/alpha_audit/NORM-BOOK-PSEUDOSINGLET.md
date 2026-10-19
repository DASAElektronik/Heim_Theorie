# NORM-BOOK-PSEUDOSINGLET: vorab festgelegter bedingter Buchvertrag

2026-09-06, Etappe30. Dieser Vertrag und seine JSON-Eingaben werden VOR
der neuen numerischen Auswahl versioniert. Keine Massenrechnung.

## 1. Quellenwahl und Grenzen

Ausschliesslich H004, vorliegende Ausgabe1996 von *Elementarstrukturen
der Materie II*. Hash/Datei stehen in `book_pseudosinglet_inputs.json`.
Keine H006-/H010-Formeln, Programmkonstanten oder alten Zahlenprofile
als unmarkierte Buchwerte. Bestehende Profile bleiben unveraendert.

Quellenwahl ist nicht die Behauptung einer vollstaendigen Herleitung.
Y3=Y9=1 ist eine bedingte Spezialisierung nach der Tabellenpolitik der
Einfuehrung Druck1/PDF12. Die A/B-Wahl vor98c und A16 bleiben heuristisch.
Physikalische Unsicherheit und numerische Rechengenauigkeit sind getrennt.

## 2. Konfiguration, Offsets und Resonanz

Grundmuster3 in101a, Druck289/PDF295: (1111)0(-1).
101b, Druck291/PDF297, ordnet es dem Myon-Pseudosingulett zu; diese
empirische Autorenidentifikation wird nicht neu physikalisch hergeleitet.
Aktiver Anschluss: k=P=Q=kappa=q=1, epsilon=1,C=0,qx=-1.
Resonanz N=0; dies setzt f(0)=0 (327/PDF333), NICHT die vier n_j=0.

98b, Druck277/PDF283: s=k^2+1,
Q_j=(3*2^(s-2),2^s-1,2^s+2*(-1)^k,2^(s-1)-1)=(3,3,2,1).
N_(j)=n_j+Q_j; die n_j werden erst nach der Exhaustion bestimmt.

## 3. Reine Zahlen und zwei getrennte Alpha-Eingaben

Mathematisches pi, e=exp(1), xi=(1+sqrt(5))/2. Die xi-Grenzsetzung
steht explizit auf275/PDF281; kein gedruckter H006-xi-Dezimalwert.
Eta-Familie aus266-267/PDF272-273 und98:

```text
eta(q,k) = pi/[pi^4+q^4*(4+k)]^(1/4),
eta = eta(1,0), d = eta(1,1), t = eta(1,2),
vartheta = 5*eta+2*sqrt(eta)+1 (33/PDF42).
```

d,t sind nur unsere eindeutigen Aliase. Index1 ist q, Index2 ist k.
eta!=d; der formale k=0-Marker bezeichnet hier das externe Feld,
nicht eine intern zugelassene Konfigurationszahl des Teilchens.

Primaerprofil `book_eq105_y3_1`,105/105a auf302/PDF308:

```text
A1 = sqrt(d)*(1-sqrt(d))/(1+sqrt(d)),
A2 = sqrt(t)*(1-sqrt(t))/(1+sqrt(t)),
Ralpha = 9*vartheta*(1-A1*A2*Y3)/(2*pi)^5,
alpha*sqrt(1-alpha^2)=Ralpha; alpha ist der kleine positive Zweig.
```

Separat vorab benanntes Profil `book_printed_alpha_sensitivity`:
alpha=0.007297354572, genau die gedruckte Dezimalzahl von302/PDF308.
Alle anderen aktiven Formeln/Eingaben bleiben gleich. Dieser Dezimalwert
wird nicht gleichzeitig als exakte Loesung105 behauptet. Kein Uebernehmen
des gedruckten Kehrwerts oder einer heutigen Messkonstante; kein Fit.
Das zweite Profil ist unsere deklarierte Druckwert-Sensitivitaet, nicht
ein zweiter Nachweis des historisch tatsaechlich benutzten Rechenablaufs.

## 4. Aktive Buchkoeffizienten und W

98c, Druck278/PDF284, mit s_d=sqrt(d), r_d=(1-s_d)/(1+s_d):

```text
alpha1=(1+s_d)/2, alpha2=1/d,
H_Korr=alpha*(1+s_d)*xi^3/(3*d^3),
G_Korr=2*xi*d/e*r_d^2,
alpha3=1-H_Korr-G_Korr, alpha4=1.
```

H_Korr/G_Korr sind eigene disambiguierende Namen, keine G_j-Zonenpolynome
und keine spaeteren Massenpolynome. Es werden keine Y_k an98c ergaenzt.

109b, Druck335/PDF341:
`A16=(pi*e)^2*(1+alpha/(5*eta)*(1+6*alpha/pi))*Y9`.
109a334/PDF340 und die lineare108a330/PDF336 liefern im aktiven Kanal
`w=1+d*A16`. Wir benutzen hier NICHT eine numerische 0^0-Vereinbarung
fuer die alternative Potenzform109. beta, A26/A31 und andere Y-Faktoren
sind keine operativen Eingaben dieses reduzierten linearen Pfads.
Damit wird nicht die gesamte Matrix109b oder jeder inaktive Ausdruck
dieser alternativen Darstellung als getrennt geprueft behauptet.

108, Druck330/PDF336:
`g=27*alpha1+9*alpha2+2*alpha3+exp(-1/3)`, `W=g*w`, `W1=W` bei f(0)=0.
Vor Exhaustion alle Radikanden/Nenner und positive alpha_i,W1 pruefen.

## 5. Auswahl und gesonderte Strukturdiagnose

Aus340-342/PDF346-348 sukzessive groesste nichtnegative Integer in
kubischer, quadratischer und linearer Zone; Rest r=W4. Fuer0<r<=1:
W5=-3*ln(r); nur bei0<=W5<=alpha3*N_(3) gewoehnliches Abschneiden.
Eine nicht spezifizierte Neuner-Promotion wird nicht implementiert.
Andere Zweige werden gemeldet und verlangen einen separaten Vertrag.
Ausgabe: N_(j), n_j, Auswahlmargen und Rest von108 links minus rechts.

107/107a werden direkt aus98e278/PDF284 und den expliziten Differenzen
auf323/PDF329 ausgewertet, NICHT aus H006-XIII/XXXII:

```text
G=(N1^2*(N1+1)^2/4, N2*(N2+1)*(2*N2+1)/6, N3*(N3+1)/2, N4),
D=(N1^3, N2^2, N3, 1),
B2=D1-G2, B3=D2-G3, B4=D3-G4; nicht kollabiert jeweils>=1,
D1>=D2, D2>=D3, D3>=D4; Zentrum D1>0.
```

Separat steht auf329/PDF335,(107b),
`B4_sigma=alpha3*N3-N4>0`. Dessen Unterschied zur vorigen B4 ist
`(alpha3-1)*N3`. Keine Umdefinition der ganzen107-Reihe wird daraus
erfunden. Auch `>0`, `>=1` und Ganzzahligkeit sind hier getrennte Fragen.
Die sigma-Anregungsdeutung wird nicht ungeprueft auf N=0 verallgemeinert.
Obere endliche Grenzen L_j/L_N und Kollapsdynamik werden nicht erfunden.
Es wird kein geschlossenes widerspruchsfreies Gesamt-Zustandspraedikat
behauptet; diese Eingaben schliessen nur den benannten Vorwaertspfad.

Numerik: Root80/120 Dezimalstellen, unabh. Gegenrechnung mit eigener
Formelimplementierung. Keine gerichtete Intervallgarantie aus blosser
Praezisionsstabilitaet; numerische Marge ist keine physikalische Fehlerschranke.
