# Potentialgrenzen hinter den H/G-Logarithmen in H004

Stand: 2026-09-06. Enger Quellenvergleich zu EDM II Druck 272--275
(PDF 278--281), mit dem unmittelbar benoetigten (98) auf Druck 267 /
PDF 273 und den Operationsregeln EDM I Druck 103--104 und 109.

## 1. Ergebnis

Die vier in EDM II Druck 274 gedruckten Logarithmusargumente lassen sich
vollstaendig als Quotienten der dort genannten Potentialgrenzen
rekonstruieren:

```text
C_H = alpha/3 * (1+sqrt(eta_qk)),
V_{rho rho}/V_epsilon = eta_qk,
V_b/V_a = eta_11/(e*eta_qk),
W_b/W_a = 2^k*((1-sqrt(eta_qk))/(1+sqrt(eta_qk)))^2.
```

`C_H` ist hier nur eine eindeutige Kurzbezeichnung dieser Review; das Buch
nennt dieses erste Argument nicht `C`. Es darf insbesondere nicht mit dem
auf derselben Seite definierten Proportionalitaetsfaktor `C_k` verwechselt
werden.

Die Quotienten folgen durch gewoehnliche Algebra **nachdem** Heims
Potentialansatz, seine Grenzwahlen und die Ladungsfeldkomponenten aus (98)
eingesetzt sind. Die vorgelagerte Umwandlung der Metronintegrale in
Logarithmen ist keine gewoehnliche Differentialrechnung: Band I definiert
Rueckwaertsdifferenzen und Teleskopsummen exakt, uebertraegt die
Logarithmus-/Exponentialregel auf die skalierte Variation aber nur
approximativ fuer einen kleinen Schritt. Genau an dieser Operatorstufe
bleibt die Buchherleitung bedingt.

## 2. Quellen und Pruefart

Visuell gelesen wurden:

- H004, *Elementarstrukturen der Materie II*, Druck 267 / PDF 273, (98),
  sowie Druck 272--275 / PDF 278--281;
- H003, *Elementarstrukturen der Materie I*, Druck 103 / PDF 109,
  Druck 104 / PDF 110 und Druck 109 / PDF 115, Regeln M2, M2a und M7.

Tragende Bilder sind
`tmp/pdfs/eta_configuration/band2-98-273.png`,
`tmp/pdfs/alpha3_book_origin/edm2-278.png` bis `edm2-281.png` sowie
`tmp/pdfs/metronic_potential/edm1-pdf110-print104.png` und
`edm1-pdf115-print109.png`. OCR diente nicht als Formelquelle.

## 3. Gemeinsame Potential- und Ladungsbasis

H004 Druck 267 nennt die Beschreibung ausdruecklich phaenomenologisch und
setzt bei festgehaltener Distanz `r` im physischen `R3`

```text
4*pi*epsilon_0*V_xy = e_x*e_y*f(r).                 (P)
```

Bei Quotienten derselben Distanz kuerzen sich daher `4*pi*epsilon_0` und
`f(r)`. Benutzt werden aus (98), mit `s=sqrt(eta_qk)`,

```text
e_rho   = epsilon_+- * s,
2*e_omega = epsilon_+- * (1+s),
e_delta = epsilon_+- * (1-s),
eta_qk*[pi^4+q^4(4+k)]^(1/4) = pi.
```

Die Passage setzt `q>0` fuer ein extern erscheinendes Ladungsfeld und
`k>0` fuer die interne Konfiguration voraus. `rho` bezeichnet in den
Komponenten und Potentialindizes das reduzierte Ladungsfeld; es ist nicht
der Chargeparameter `q`. Fuer die vier Quotienten ist
keine zusaetzliche Gleichsetzung `q=|q_x|` noetig oder in diesem Abschnitt
angegeben. Nur der Zaehler des dritten Quotienten wird ausdruecklich auf
`q=1,k=1` spezialisiert und ist deshalb `eta_11`.

H004 Druck 273 erklaert ferner, dass `epsilon_+-` von der metronischen
Variation nicht erfasst werde und
`V_{epsilon epsilon}=V_epsilon=const` als Bezugsgroesse diene. Das ist die
Referenz fuer die folgenden Potentialquotienten.

## 4. Die vier Argumente aus ihren Grenzen

### 4.1 `alpha(1+s)/3`

Der zu `A1` gehoerende H-Anteil laeuft von der griechisch bezeichneten
Grenze `V_alpha` nach `V_beta`. H004 Druck 274 setzt

```text
2*V_alpha = V_epsilon,
3*V_beta  = alpha*V_{omega,epsilon}.
```

Die zweite Setzung wird mit drei massiven Zonen bis `j=3` und der
Feinstrukturkonstante als Kopplungskonstante motiviert. Aus (P) und (98):

```text
V_{omega,epsilon}/V_epsilon
  = (e_omega*epsilon)/(epsilon^2)
  = (1+s)/2.

V_beta/V_alpha
  = [alpha*V_{omega,epsilon}/3]/[V_epsilon/2]
  = alpha*(1+s)/3.
```

Damit ist das erste Argument quellenseitig ein Grenzquotient. Seine
Grenzwahl, insbesondere `3*V_beta=alpha*V_{omega,epsilon}`, ist eine
physikalische Setzung des Textes, keine Folge aus (98) allein.

### 4.2 `eta_qk`

Die zu `A3` und `B3` gehoerenden Integrale laufen von `V_epsilon` nach
`V_{rho rho}`. Wegen (P) und `e_rho=epsilon_+-*s` gilt

```text
V_{rho rho}/V_epsilon = e_rho^2/epsilon_+-^2 = s^2 = eta_qk.
```

Dies ist der Ursprung beider gedruckter Terme `ln eta_qk`.

### 4.3 `eta_11/(e*eta_qk)`

Beim ersten G-Anteil sind die Grenzen mit **lateinischem** Index
`V_a,V_b` bezeichnet; sie sind nicht `V_alpha,V_beta`. Druck 274 setzt

```text
V_a = V_{rho rho}(q,k),
e*V_b = V'_{rho rho}(q=1).
```

Druck 272 definiert den Strich nur als Indexierung
`V'=V(k=1)`, nicht als Ableitung. Daher ist der Zaehler der zweite Zeile
das Potential fuer `(q,k)=(1,1)`. Der Faktor `e` ist hier die Basis des
natuerlichen Logarithmus aus der expliziten Abklingannahme `e^-1`, keine
elektrische Ladung. Mit (P):

```text
V_b/V_a = [V_{rho rho}(1,1)/e]/V_{rho rho}(q,k)
          = eta_11/(e*eta_qk).
```

Die Abklingannahme fuer `V_b` bezeichnet der Text selbst als spekulativ.

### 4.4 `2^k*((1-s)/(1+s))^2`

Fuer den zu `B4` gehoerenden G-Anteil setzt Druck 274

```text
W_a = V_{omega omega},
W_b = C_k*V_{delta delta},
C_k = 2^(k-2).
```

Das Buch gewinnt `C_k` zuvor aus seiner Zone-4-Anschlussrechnung. Ferner
beschreibt es den Weg als zwei Teilintegrationen von `W_a` bis
`V_epsilon` und von `V_epsilon` bis `W_b`. Im Gesamtquotienten faellt die
Zwischenreferenz algebraisch weg. Aus (98):

```text
e_delta/e_omega = 2*(1-s)/(1+s),

W_b/W_a
  = 2^(k-2)*(e_delta/e_omega)^2
  = 2^k*((1-s)/(1+s))^2.
```

Der Faktor `2^k` kommt damit aus **beiden** Quellen: `2^(k-2)` aus der
gesetzten Anschlussproportion und `2^2` aus dem in (98) gedruckten
`2*e_omega=epsilon_+-*(1+s)`.

## 5. Untere Grenzkorrektur und Logarithmusnaeherung

Diese beiden Schritte muessen getrennt bleiben.

1. **Exakte diskrete Indexregel.** H003 M2 definiert
   `delta phi(n)=phi(n)-phi(n-1)`. M2a gibt daher exakt
   `sum_(n=n1)^n2 delta phi(n)=phi(n2)-phi(n1-1)`. Das erklaert auch H004
   Druck 273: die Metronintegration ueber die Ziffern `z` bis `z+1`
   liefert `ln X(z+1)-ln X(z-1)` und damit das dortige
   `Y=X(z+1)/X(z-1)`.
2. **Potential-Untergrenze: Textanweisung, aber offener Schrittindex.**
   H004 Druck 274 fordert bei den Potentialintegralen ausdruecklich, zur
   unteren Grenze die metronische Variation des betreffenden Potentials zu
   addieren. M2a zeigt, was fuer eine exakte Kompensation noetig waere: Soll
   statt `F(b)-F(a-1)` der Wert `F(b)-F(a)` entstehen, muss die Summe beim
   Nachfolger `a+1` beginnen; dort gilt
   `F(a+1)=F(a)+delta F(a+1)`. H004 versieht sein addiertes `delta_e V`
   jedoch nicht mit einem diskreten Schrittindex. Deshalb darf die Prosa
   nicht ohne weiteres als `V_a+delta V(a)` und auch nicht als vollstaendig
   bewiesene `a -> a+1`-Regel gelesen werden. Die danach **gedruckten**
   Logformen verwenden gleichwohl die benannten Endpotentiale; aus diesen
   Endwerten folgt die Quotientenalgebra in Abschnitt 4. Keiner der Faktoren
   `alpha/3`, `eta`, `e^-1` oder `2^k` stammt aus einer von uns ergaenzten
   Indexwahl.
3. **Nur approximativer Logarithmusschritt.** H003 M7 sagt fuer eine mit
   `0<|delta_e|<<1` skalierte Variation ausdruecklich
   `delta_e phi approx phi*delta_e ln(phi)` und beschreibt dies als
   approximativen Zugang. H004 Druck 272 ordnet seine Variation
   entsprechend der Groessenordnung `sqrt(tau)` zu. Deshalb darf die
   Uebertragung vom Potentialvariationsausdruck auf die gedruckten
   Logarithmen nicht als exakte Regel gewoehnlicher Analysis ausgegeben
   werden.

Die Teleskopregel ist damit quellenintern klar. Die genaue indizierte
Umsetzung der H004-Untergrenzenanweisung und die Gueltigkeit der
Logarithmusnaeherung fuer jeden konkreten Potentialpfad werden auf Druck
272--274 jedoch nicht separat vorgefuehrt.

## 6. Von den Logformen zu H und G

Druck 275 sagt zunaechst, `A_i` und `B_r` koennten frei vorgegeben werden,
und waehlt dann als an Elektron- und Protonempirie optimal angepasste Werte

```text
A1=B1=B4=1,  2*A2=2*k+1,  2*B2=B3=k,  A3=1-4*k.
```

Eine Glyphengrenze bleibt: Vor dem ersten G-Logarithmus druckt Seite 274
`B'_1`, waehrend der Variationsansatz auf Seite 273 und die Wahl auf Seite
275 `B1` ohne Strich verwenden. Eine gesonderte Definition von `B'_1` oder
die Gleichung `B'_1=B1` steht in diesem unmittelbaren Abschnitt nicht. Die
Endform von G entspricht der Spezialisierung des Exponenten auf 1; die
Review behandelt den Strich deshalb nicht als neuen, unabhaengig bestimmten
Koeffizienten, vermerkt ihn aber als lokale Satz-/Definitionsluecke.

Mit den vier oben rekonstruierten Logarithmusargumenten und
`ln H-A2 ln Y`, `ln G-B2 ln Y` ergibt gewoehnliche Exponentenalgebra die
auf Druck 275 gedruckten Formen

```text
H = alpha/3*(1+s)*(sqrt(Y)/eta_qk^2)^(2*k+1)*eta_qk^3,

G = eta_11/(e*eta_qk)*(2*eta_qk*sqrt(Y))^k
    *((1-s)/(1+s))^2.
```

Diese Schlussumformung ist algebraisch. Die Exponenten selbst sind jedoch
die empirisch gewaehlten `A_i,B_i`; weder (98) noch die Potentialquotienten
erzwingen sie.

## 7. Verbleibender enger Blocker

Die Quelle liefert eine geschlossene **bedingte** Argumentkette:
Potentialgrenzen plus (98) erklaeren alle vier Quotienten, die gewaehlten
`A_i,B_i` erklaeren ihre Potenzen. Nicht geliefert wird auf diesen Seiten
ein vom Metronenkalkuel unabhaengiger Beweis,

- dass die phaenomenologischen Potentialgrenzen eindeutig sind,
- dass die M7-Kleinheitsnaeherung fuer jeden verwendeten Quotienten mit
  kontrolliertem Fehler gilt, oder
- dass gerade die empirisch angepassten `A_i,B_i` aus einer Operatorregel
  folgen.

Die Quotientenalgebra schliesst daher die Herkunft der sichtbaren
H004/H010-Formelargumente, nicht die metronische oder physikalische
Rechtfertigung aller davor gesetzten Regeln.
