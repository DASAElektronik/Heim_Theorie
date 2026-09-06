# Gekoppelte Existenzpruefung des festen Buchmodells

Stand: 2026-09-06. Eigenstaendige mathematische Pruefung ohne Masse,
Sollwertsuche, Epsilon oder Aenderung der Buchinputs. Untersucht wird genau

```text
W = a1*N1^3 + a2*N2^2 + a3*N3 + exp(-N4/3)
```

mit nichtnegativen ganzen `N_j`, den drei strikten direkten Gates

```text
N1^3 > G2(N2),   N2^2 > G3(N3),   N3 > N4,
G2(n)=n(n+1)(2n+1)/6,   G3(n)=n(n+1)/2,
```

und der zweiten Reihe `N1^3>=N2^2>=N3>=1`. Die Formeln und die zwei
unveraenderten Profile stehen in `scripts/audit_book_pseudosinglet.py` und
`04_reconstruction/alpha_audit/book_pseudosinglet_inputs.json`.

## 1. Ergebnis

Unter den unten angegebenen gemeinsamen rationalen Einschliessungen fuer
beide feste Profile existiert **kein** solches Tupel. Der Ausschluss ist
sogar staerker als verlangt: Er benutzt nur Nichtnegativitaet, die ersten
beiden strikten Gates und die Energiegleichung. Die zweite 107-Reihe und
das dritte Gate `N3>N4` koennen die Kandidatenmenge nur weiter verkleinern.

Der Beweis ist kein Test der Buchtheorie insgesamt. Er betrifft genau den
festgelegten Koeffizienten-/W-Pfad und verlangt exakte Gleichheit; ein
ungefaehr passendes Tupel oder die alte greedy-Auswahl wird nicht gesucht.

## 2. Gemeinsame rationale Schranken

Fuer beide Profile genuegen die groben Intervalle

```text
249/250 < a1 < 9969/10000,
1       < a2 < 5063/5000,
0       < a3 < 9787/10000,
141513/50 < W < 2831.
```

Sie enthalten sowohl den `alpha`-Wert aus (105) bei `Y3=1` als auch das
getrennte Profil mit dem gedruckten Alpha-Dezimalwert. Die transzendenten
Ausgangsformeln werden hier nicht durch Dezimalrundung ersetzt: Fuer den
nachfolgenden diskreten Schluss sind nur diese rationalen
Intervallschranken erforderlich. Ihre formelgebundene Intervallpruefung ist
von der rein ganzzahligen Folgerung zu trennen.

Fuer jedes `N4>=0` gilt unabhaengig davon

```text
0 < exp(-N4/3) <= 1.
```

## 3. Vollstaendige Fallzerlegung

### 3.1 `N1>=15`

Schon der erste positive Summand ist zu gross:

```text
a1*N1^3 > (249/250)*15^3 = 3361.5 > 2831 > W.
```

Damit bleibt `N1<=14`.

### 3.2 `N1<=13`

Aus dem ersten Gate folgt `N2<=18`, denn

```text
G2(19)=2470 > 13^3=2197.
```

Aus dem zweiten Gate folgt dann `N3<=24`, denn

```text
G3(25)=325 > 18^2=324.
```

Selbst die gemeinsame Obergrenze aller vier Energieterme ist

```text
2197 + (5063/5000)*18^2 + (9787/10000)*24 + 1
= 2549.5712 < 2830.26 < W.
```

Also ist auch dieser ganze Bereich ausgeschlossen.

### 3.3 `N1=14`, aber `N2>=10`

Mit nur den ersten beiden positiven Summanden folgt

```text
a1*14^3+a2*10^2
> (249/250)*2744+100
= 2833.024 > 2831 > W.
```

Somit muss bei `N1=14` notwendig `N2<=9` gelten.

### 3.4 `N1=14` und `N2<=8`

Das zweite Gate erzwingt `N3<=10`, weil
`G3(11)=66>8^2=64`. Die groesstmoegliche linke Seite bleibt dann unter

```text
(9969/10000)*2744 + (5063/5000)*8^2
+ (9787/10000)*10 + 1
= 2811.087 < 2830.26 < W.
```

### 3.5 `N1=14` und `N2=9`

Das zweite Gate erzwingt `N3<=12`, weil
`G3(13)=91>9^2=81`. Selbst bei `N3=12` und beim maximal moeglichen
Exponentialterm ist

```text
(9969/10000)*2744 + (5063/5000)*81
+ (9787/10000)*12 + 1
= 2830.2586 < 2830.26 < W.
```

Der Sicherheitsabstand der verwendeten rationalen Grenzen betraegt hier
noch `0.0014=7/5000`. Fuer kleinere `N3` wird die linke Seite nur kleiner.
Damit ist auch der letzte Fall ausgeschlossen.

Die Faelle `N1<=13`, `N1=14,N2<=8`, `N1=14,N2=9`,
`N1=14,N2>=10` und `N1>=15` ueberdecken alle nichtnegativen ganzen
`N1,N2`. Es bleibt daher kein Kandidat.

## 4. Selbststaendiger `Fraction`-Kontrollblock

Der folgende Block importiert keinen Projektcode und benutzt keine
Gleitkommazahl. Er prueft die rationalen Rechenschritte und die
vollstaendige Fallabdeckung; die vier Koeffizientenintervalle sind sein
expliziter Eingabevertrag.

```python
from fractions import Fraction as F

a1_lo, a1_hi = F(249, 250), F(9969, 10000)
a2_lo, a2_hi = F(1), F(5063, 5000)
a3_lo, a3_hi = F(0), F(9787, 10000)
W_lo, W_hi = F(141513, 50), F(2831)

def G2(n):
    return F(n * (n + 1) * (2*n + 1), 6)

def G3(n):
    return F(n * (n + 1), 2)

assert 0 < a1_lo < a1_hi < 1
assert 0 < a2_lo < a2_hi
assert 0 <= a3_lo < a3_hi < 1
assert W_lo < W_hi

# N1 >= 15: sicher oberhalb des Budgets.
m_hi_n1 = a1_lo * 15**3 - W_hi
assert m_hi_n1 > 0

# N1 <= 13: Gates geben N2 <= 18 und N3 <= 24.
assert G2(19) > 13**3
assert G3(25) > 18**2
upper_13 = F(1)*13**3 + a2_hi*18**2 + a3_hi*24 + 1
m_lo_n1 = W_lo - upper_13
assert m_lo_n1 > 0

# N1=14 und N2>=10: sicher oberhalb des Budgets.
m_hi_n2 = a1_lo*14**3 + a2_lo*10**2 - W_hi
assert m_hi_n2 > 0

# N1=14, N2<=8: zweites Gate gibt N3<=10; sicher unterhalb.
assert G3(11) > 8**2
upper_8 = a1_hi*14**3 + a2_hi*8**2 + a3_hi*10 + 1
m_lo_n2_8 = W_lo - upper_8
assert m_lo_n2_8 > 0

# Einziger Restfall N2=9: zweites Gate gibt N3<=12.
assert G3(13) > 9**2
upper_9 = a1_hi*14**3 + a2_hi*9**2 + a3_hi*12 + 1
m_lo_n2_9 = W_lo - upper_9
assert m_lo_n2_9 == F(7, 5000) > 0

print({
    "N1>=15 over": m_hi_n1,
    "N1<=13 under": m_lo_n1,
    "N1=14,N2>=10 over": m_hi_n2,
    "N1=14,N2<=8 under": m_lo_n2_8,
    "N1=14,N2=9 under": m_lo_n2_9,
})
```

## 5. Aussagegrenze

Der Schluss ist eine exakte Nicht-Existenz unter dem festgelegten
Gleichungssystem, sobald die gemeinsamen rationalen Koeffizientenintervalle
gegen die unveraenderten Buchformeln zertifiziert sind. Er sagt nicht,
welche Gleichung Heim bei einer Gateverletzung haette aendern wollen, und
liefert keine Ersatzbesetzung. Insbesondere darf er nicht als Beweis gegen
andere Fassungen, andere `Y`-Werte, kollabierte Zonen mit geaendertem
Gleichungssystem oder die gesamte Theorie verallgemeinert werden.
