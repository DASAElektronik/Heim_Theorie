# Sind die H/G-Grenzen ein gemeinsamer Potentialpfad?

Stand: 2026-09-06. Begrenzte Quellenreview zu H004, EDM II, Druck 267 und
272--274 / PDF 273 und 278--280. Keine Fits und keine Ergaenzung einer nicht
gedruckten Dynamik.

## 1. Kurzantwort

Die Quelle definiert keinen einzigen, gleichzeitig von einem gemeinsamen
Startwert durchlaufenen Potentialpfad fuer alle H/G-Terme. Sie setzt mehrere
getrennte Metronintegrale mit verschiedenen Grenzen an:

```text
H/A1: V_alpha -> V_beta                    in V_(omega),
H/A3: V_epsilon -> V_(rho rho),
G/B1: V_a -> V_b                           in V_(rho rho)(G),
G/B3: V_epsilon -> V_(rho rho),
G/B4: W_a=V_(omega omega) -> W_b=C_k V_(delta delta),
      mit V_epsilon als genanntem Zwischenwert.
```

(98) dient danach dazu, die Endquotienten in `eta_qk`-Form auszudruecken.
Der Text sagt nicht, dass jeder Zwischenpunkt aller Integrale allein durch
denselben laufenden Wert `eta_qk` erzeugt wird.

Unter einer zusaetzlich unterstellten gemeinsamen positiven (98)-Kurve
entstehen Spannungen: Die H-Untergrenzen entspraechen verschiedenen formalen
Startwerten, und `V_beta` liegt als mit `alpha/3` skalierter Zonenanteil
unterhalb des Wertebereichs des unskalierten `V_(omega,epsilon)`. Das ist
ein Einwand gegen diese Zusatzlesart, kein pauschaler Widerspruch der
gedruckten, separat gesetzten Grenzquotienten.

## 2. Quelle und gemeinsame Algebra

Visuell vollstaendig gelesen wurden Druck 267 / PDF 273 sowie Druck 272--274 /
PDF 278--280. Tragende Bilder:

- `tmp/pdfs/eta_configuration/band2-98-273.png`;
- `tmp/pdfs/alpha3_book_origin/edm2-278.png` und `edm2-279.png`;
- `tmp/pdfs/metronic_potential/edm2-pdf280-print274.png`.

Setze nur zur kompakten Quellenalgebra `s=sqrt(eta_qk)` und
`V_epsilon=V_(epsilon epsilon)`. Druck 267 gibt

```text
e_rho=epsilon_+/-*s,
2*e_omega=epsilon_+/-*(1+s),
e_delta=epsilon_+/-*(1-s),
4*pi*epsilon_0*V_xy=e_x*e_y*f(r).
```

Die Potentialbeschreibung wird dort phaenomenologisch genannt. Druck 272
verlangt, die `R3`-Distanz an der Grenze von `j=3` konstant zu halten. Nur
unter dieser Gleichabstandsbedingung kuerzt sich derselbe Faktor `f(r)` in
Quotienten.

Fuer `q>0,k>0` folgt aus der gedruckten eta-Gleichung `0<eta_qk<1`, also
`0<s<1`. Die rohen Komponentenpotentiale haben relativ zu `V_epsilon`:

```text
V_(rho rho)/V_epsilon       = s^2         in (0,1),
V_(omega,epsilon)/V_epsilon = (1+s)/2     in (1/2,1),
V_(omega omega)/V_epsilon   = (1+s)^2/4   in (1/4,1),
V_(delta delta)/V_epsilon   = (1-s)^2     in (0,1).
```

Dies kennzeichnet Komponentenfamilien. Es beweist nicht, dass spaetere
skalierte Grenzen selbst wieder Punkte derselben unskalierten Familie sind.

## 3. H/A1: komponentenbezogen, aber skalierter Zielwert

Druck 272 bezeichnet `V_(omega)` als Potential bezogen auf
`e_omega*epsilon_+`. Druck 273 setzt sein Integral von `V_alpha` nach
`V_beta`; Druck 274 bestimmt

```text
2*V_alpha=V_epsilon,
3*V_beta=alpha*V_(omega,epsilon).
```

`V_beta` wird als der auf die p-Zone `j=3` entfallende Anteil des
`V_omega`-Potentials motiviert; `alpha` wird als Kopplungsfaktor gesetzt.
Die obere Grenze ist daher nicht das volle `V_(omega,epsilon)`, sondern ein
zonen-/korrelationsskalierter Zielwert. Sicher ist

```text
V_beta/V_alpha=alpha*(1+s)/3.
```

Eine durchgehende Parametrisierung `V_(omega,epsilon)(s(t))` folgt daraus
nicht. Bei einer solchen Zusatzlesart waere `V_alpha=V_epsilon/2` gerade der
Randwert `s=0`, fuer endliche `q>0,k>0` also kein (98)-Mitglied. Ferner gilt

```text
V_beta/V_epsilon=alpha*(1+s)/6 < 1/3
```

fuer die als Feinstrukturkonstante gemeinte `0<alpha<1`, waehrend die rohe
omega-epsilon-Kurve fuer `s'>=0` nie unter `1/2` faellt. `V_beta` ist somit
nicht ohne den ausdruecklich gesetzten Faktor `alpha/3` als anderer Punkt
derselben rohen Kurve lesbar.

Belastbar ist: `V_(omega)` benennt die Komponentenart; die Grenzen sind
gesondert gesetzte, teils skalierte Korrelationswerte. Ob die Komponentenart
waehrend jedes diskreten Zwischenschritts streng erhalten bleibt, sagt der
Text nicht.

## 4. H/A3 und G/B3: gleicher Quotient, kein gemeinsamer H-Start

Die `A3`- und `B3`-Integrale besitzen dieselben Grenzen

```text
V_epsilon -> V_(rho rho),
V_(rho rho)/V_epsilon=s^2=eta_qk.
```

Sie koennen quellennah als derselbe Endquotient mit verschiedenen Gewichten
gelesen werden. H004 verlangt aber keinen gemeinsamen zeitlichen Verlauf
mit dem `A1`-Integral.

Auf einer positiven rho-rho-Kurve entspraeche `V_epsilon` dem Wert `s=1`;
der A1-Start entsprach `s=0` in der omega-epsilon-Familie. Beide H-Integrale
beginnen folglich nicht bei demselben `s`. Das passt zur Druckstruktur aus
zwei getrennten Integralen. Eine gleichzeitige Variation aller Komponenten
von einem eta-Anfangszustand waere eine zusaetzliche Annahme.

`s=1` ist zudem der formale `q=0`-Wert, waehrend der H/G-Kontext `q>0`
behandelt. Druck 273 nennt `V_epsilon=const` eine nicht der
`delta_e`-Variation unterworfene Bezugsgroesse. Der untere Wert ist daher
quellennah eine Referenzgrenze, kein belegter interner `q>0`-Zustand.

## 5. G/B1: rho-rho-Familie mit abgeklungenem Ziel

Druck 272 nennt fuer `V_(rho rho)(G)` eine Variation zwischen
`V_(rho rho)` und `V'_(rho rho)(q=1)`. Druck 274 setzt

```text
V_a=V_(rho rho)(q,k),
e*V_b=V'_(rho rho)(q=1),   V'=V(k=1),
V_b/V_a=eta_11/(e*eta_qk).
```

Beide unskalierten Potentiale gehoeren zur rho-rho-Familie. `V_b` ist aber
laut Text das um `e^-1` abgeklungene Potential der Minimalkondensation; die
Annahme wird selbst spekulativ genannt. Es wird nicht behauptet, `V_b` sei
ein durch ganzzahlige `(q',k')` realisierter Rohwert aus (98).

Eine kontinuierliche Kurve koennte formal `s_b^2=e^-1*eta_11` enthalten.
Das bestimmt weder ein diskretes `(q',k')` noch den Abklingpfad. Belegt ist
der gesetzte Endwert, nicht seine Dynamik.

## 6. G/B4: W verbindet verschiedene Komponentenfamilien

Druck 272 definiert `W` als Variation zwischen `V_(omega omega)` und
`V_(delta delta)`. Druck 274 setzt

```text
W_a=V_(omega omega),
W_b=C_k*V_(delta delta),
C_k=2^(k-2).
```

Das Integral wuerde laut Text zunaechst von `W_a` bis `V_epsilon` laufen;
daran schliesse eine weitere Integration bis `W_b` an. H004 beschreibt also
selbst einen zusammengesetzten Weg ueber die Referenz, nicht einen
gleichnamigen Komponentenpfad `V_xy(s)` mit festem `(x,y)`.

Unter (98) sind die Endwerte

```text
W_a/V_epsilon=(1+s)^2/4,
W_b/V_epsilon=2^(k-2)*(1-s)^2,
W_b/W_a=2^k*((1-s)/(1+s))^2.
```

Der letzte Quotient ist die gedruckte Logform. Er folgt aus den Endsetzungen,
obwohl Anfang und Ende verschiedenen Komponentenprodukten angehoeren.

Fuer `k=1,2` liegen sowohl `W_a` als auch `W_b` unter `V_epsilon`. In einem
gewoehnlichen eindimensionalen Potentialwert fuehrte der beschriebene Weg
somit erst auf- und dann abwaerts. Das ist kein algebraischer Widerspruch
eines orientierten oder zusammengesetzten Integrals, zeigt aber, warum `W`
nicht als monotoner gemeinsamer (98)-Komponentenpfad behandelt werden darf.

## 7. Belastbare Lesarten

**Am besten belegt: getrennte Endpunkt-/Korrelationsintegrale.** Jeder Term
hat einen Potentialnamen, eigene Grenzen und einen Faktor `A_i` oder `B_i`.
(98) liefert Komponentenwerte; Zonenanteil, Abklingen und `C_k` liefern
weitere Skalierungen. So entstehen die gedruckten Quotienten ohne erfundene
gemeinsame Zwischenzustaende.

**Nicht belegt: ein gemeinsamer eta-Pfad.** Diese Zusatzlesart verlangte
denselben laufenden `s`-Wert fuer A1 und A3. Ihre Untergrenzen entsprechen
aber `s=0` bzw. `s=1`, und der A1-Zielwert liegt wegen `alpha/3` ausserhalb
der rohen omega-epsilon-Kurve. Ohne weitere Amplituden-/Projektionsvariable
ist diese Lesart nicht geschlossen.

**Moeglich, aber offen: Komponentenpfade mit skalierten Endprojektionen.**
Die Prosa ueber p-Zonenanteil, Abklingen und Zone-4-Anschluss passt zu einer
Hybridlesart, in der `delta_e` innerhalb von Komponentenfamilien wirkt und
die genannten Faktoren Grenzprojektionen darstellen. Eine explizite
Pfadparametrisierung oder Operatorgleichung dafuer fehlt jedoch.

## 8. Abschluss

Quellenfest sind die getrennten Integrale, ihre Endwerte und die daraus
gebildeten Quotienten. Nicht quellenfest sind ein gemeinsamer eta-Start fuer
A1/A3, `V_beta` als unskalierter omega-epsilon-Kurvenpunkt, ein diskreter
(98)-Zustand fuer `V_b` oder ein einheitlicher monotoner W-Pfad.

Die Endpunktlagen diagnostizieren somit eine fehlende Pfaddefinition. Ohne
weitere Operatorquelle begruenden sie keinen pauschalen Widerspruch gegen
die von H004 direkt gesetzten getrennten Endquotienten.
