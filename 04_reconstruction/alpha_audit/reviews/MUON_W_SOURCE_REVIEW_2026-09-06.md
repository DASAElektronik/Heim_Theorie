# H006 x3/mu-: W-Quelle, aktive Terme und lokale Definitionsgrenzen

Stand: 2026-09-06. Dies ist eine eng begrenzte, quellenorientierte
Sichtlesung von H006 (*Massenformel nach B. Heim 1982*, lokale
IGW-Wiedergabe), SHA-256
`F74DA0DAC8496BCD01226F54D88598152D67E1C954943AF61D0EC1811F5527BE`.
Geprüft wurden vollständig Druck/PDF 5--8, besonders (IX) sowie
(XV)--(XXVI). Die tragenden Bildanker sind
`tmp/pdfs/n0_alias/h006-05.png` bis `h006-08.png`. Keine Masse,
Besetzung oder numerische Auswertung wird hier bestimmt.

## 1. Eingabekette und was hier vorausgesetzt wird

Die zuvor separat visuell geprüfte H006-(III)-Zeile für
`x3(0111)_0(-1,-1) = (mu-) Pseudosingulett` liefert
`epsilon=+1`, `k=P=Q=kappa=1`, `C=0`; (II) liefert für beide formalen
Komponenten `q_x=-1`, folglich `q=1`. Diese Review prüft nur den
anschließenden W-Block. Die Zusammenziehung der zwei Komponenten zum
Pseudosingulett ist damit nicht neu interpretiert.

Auf Druck/PDF 5 definiert (IX) sichtbar `eta_qk` mit dem Formelrumpf
`pi/[pi^4+(4+k)q^4]^(1/4)`. Für den vorliegenden Wert wird im Folgenden
nur als lokale Abkürzung

```text
d := eta_qk |_(k=1,q=1) = eta_11
```

geschrieben. Das ist **nicht** die unindizierte `eta` der A-Matrix auf
Druck/PDF 7. Die vier Sichtseiten geben keine Gleichung an, welche diese
beiden Symbolformen gleichsetzt.

## 2. Quellnahe Reduktion von w(1), w(2), w und W

Druck/PDF 6 trennt in (XVII) und (XVIII) die zwei Klammern der
Strukturpotenz. Mit den obigen Konfigurationswerten ergibt sich, unter den
in Abschnitt 3 genannten Regularitätsbedingungen,

```text
w(1) = (1-Q)[...] + kappa*Q*eta_qk*A16 = d*A16,

w(2) = (q-1)A21 + (1-P)A22 + C(P,2)[...]
       + kappa(A26 + q*eta_qk^2*A31) + C(Q,3)eta_qk*A32
       + C(P,3)[...]
     = A26 + d^2*A31.
```

Das ist ein Quellenanschluss, keine angenommene Auslöschung: hier sind
gerade `kappa=1`, `P=Q=q=1` ausschlaggebend. Anders als beim früheren
`x2/e-`-Nullfall verschwindet weder der `A16`-Anteil noch der
`A26/A31`-Anteil.

(XIX) schreibt zunächst Potenzen von `w(1)` und `w(2)`. Der direkt
darunter gedruckte Text behandelt die uneigentlichen `0^0`-Fälle als
Strukturpotenz eins und gibt die verschobene Programmform an. Für den
mesonischen Fall `k=1` steht dort ausdrücklich

```text
w_nu_x(k=1) = 1 + w(1) = 1 + d*A16,
W_nu_x = g(q,k) * w_nu_x.                 (XV)
```

Die gedruckte Begründung setzt dabei voraus, dass die betroffene Basis
nicht `-1` wird; sie ersetzt keine allgemeine Behandlung undefinierter
Koeffizienten. `w(2)` bleibt deshalb trotz Exponent null ein relevanter
Definitions-/Regularitätscheck, nicht ein aktiver Summand von `w`.

Auf Druck/PDF 8 sagt der Text für die Resonanzordnung ausdrücklich:
`N=0` mache `f=0`, worauf (XXVI) zur Auswahl der `n_j` folgt. Das ist
eine separate quelleninterne N=0-Aussage. Sie beweist weder einen
Besetzungsvektor noch reduziert sie `W` oder `g` auf eins.

## 3. Sichtbare Koeffizienten und Bedingungen vor Nullauslöschung

Druck/PDF 7 druckt die hier aktiven Zeilen in kompakter Slashnotation:

```text
A16 = (pi e)^2 [1 + alpha(1+6 alpha/pi)/5 eta]
A26 = 2{1 - [pi(e xi alpha)^2 sqrt(eta)]/2}/(e xi^2)
A31 = (pi e alpha)^2 [1 - (pi e)^2(1-beta^2)].
```

Die A16-Zeile enthält keinen expliziten Bruchstrich um `5 eta`.
`/(5*eta)` ist daher die bereits dokumentierte
Denominator-Produkt-Normalisierung, nicht eine neue typografisch
bewiesene Klammer. Die ebenfalls erhaltene linkassoziative Variante
`(/5)*eta` ist eine getrennte Sensitivität. Beide betreffen die aktive
Größe `d*A16`.

Auch bei einem Nullvorfaktor müssen die ausgeklammerten Ausdrücke zuerst
definiert sein. Die auf den geprüften Seiten unmittelbar sichtbaren
Prüfpunkte sind:

| Ort | Reduktion beim muonischen Input | notwendige lokale Prüfung |
|---|---|---|
| (XVII), `(1-Q)[...]` | Vorfaktor `0` | Die darin stehenden `A11..A15` und die `eta_qk`-Divisionen müssen definiert sein. |
| (XVIII), `(q-1)A21`, `(1-P)A22`, `C(P,2)[...]` | jeweils `0` | Insbesondere `A24=2 xi^2/(3 eta)` ist definiert; dann wird der sichtbare Nenner `1+A24(1+q_x)` bei `q_x=-1` zu `1`. |
| (XVIII), `C(Q,3)eta_qk A32` | `0` | Die in `A32` sichtbare unindizierte-`eta`-Division bleibt regulär. |
| (XVIII), `C(P,3)[...]` | `0` | Bei `q=1` sind `3-q=2` und `8-A66^(q(q-1))=8-A66^0=7`; zusätzlich dürfen die eingebetteten A-Zeilen nicht undefiniert sein. Dazu gehört `A36=[1-pi e(xi e)^2(1-beta^2)]^(-1)`, dessen Nenner nicht null sein darf. |
| aktiver Teil | kein Nullvorfaktor | In `A26` müssen `e` und `xi` nicht null sein und der Wurzelausdruck reell/definiert sein; `A31` muss endlich sein. A16 verlangt je nach expliziter Normalisierungslesart insbesondere eine reguläre unindizierte `eta`-Division. |

Damit ist `w(2)=A26+d^2 A31` nur unter diesen lokalen
Definitionsbedingungen eine algebraische Reduktion. Insbesondere ist es
nicht zulässig, `A24`, `A36` oder eine andere eingebettete Division durch
einen äußeren Nullkoeffizienten stillschweigend zu entfernen. Die
unindizierte `eta` der A-Zeilen bleibt von `d=eta_11` getrennt.

## 4. g und die offene alpha3-Wurzellesart

(XV), Druck/PDF 6, definiert `W_nu_x=g(q,k)w_nu_x`; für `n_j=0` enthält
`g` neben den drei `Q_i`-gewichteten `alpha_i` den sichtbaren
Exponentialterm `exp[(1-2k)/3]`. Damit bleibt `alpha3` aus (IX) aktiv
für eine spätere W-/Auswahlrechnung.

Die zweite Klammer in (IX) zeigt die kompakte Quellelementfolge
`(eta_11/(e eta_qk)) (2 sqrt(xi eta_qk))^k`. Für den Zielpunkt ist das
eine Stelle mit `d=eta_11`; diese Sichtlesung legt jedoch weder die alte
Default-Implementierung `sqrt(xi*d)` noch die getrennt zu prüfende
Variante `sqrt(xi)*d` neu fest. Beide gehören als ausdrücklich
vorab benannte Profilachsen in eine Quellenmatrix. Eine Auswahl zwischen
ihnen wäre weder durch die hier gelesene Formel allein noch durch einen
etwaigen späteren Zahlenwert gedeckt.

## 5. Status für einen folgenden, masselosen Auswahltest

Quellengetragen und nur unter den genannten Domains verwendbar ist:

```text
H006, x3/mu-, N=0:
  d = eta_11;
  w1 = d*A16;
  w2 = A26 + d^2*A31;
  w  = 1 + d*A16;
  W  = g(1,1) * (1 + d*A16);
  f  = 0  (aus der ausdruecklichen N=0-Aussage auf p8).
```

Nicht quellenfest bestimmt sind hier eine bevorzugte A16-Slashbindung,
eine bevorzugte alpha3-Wurzelweite, konkrete Konstanten, ein
Besetzungsquadrupel oder eine Teilchenmasse. Die im Plan genannten
`3 x 2 x 2` Profile sind deshalb ein transparentes Rechenangebot unter
erhaltenen Lesarten, keine aus H006 hergeleitete eindeutige Vorhersage.
