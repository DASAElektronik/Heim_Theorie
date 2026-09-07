# Massenformel (98d/e) bis (112): was algebraisch trägt

2026-09-07, Etappe38. Ausgang `06952db`, Plancheckpoint `427868c`.
Fortsetzung der [Quellenstatusprüfung](EQ108_STATUS_2026-09-07.md).

## Ergebnis

Die untersuchte Umformung ist algebraisch korrekt: Heims Zerlegung
`4*sum(alpha_j*G_j)=K+F+H` geht exakt auf. Mit der bereits in (97)
definierten Massenskala und der Zusammenfassung `phi` folgt daraus (112).
Es ist eine Umgruppierung derselben Massenformel, keine zusätzliche
Herleitung der Besetzungen oder des empirisch bestimmten Beitrags `F_S`.

Ein anfänglicher Verdacht auf unterschiedliche Ziffern im K-Term wurde
am vergrößerten Original verworfen. Es steht an beiden Stellen `3*Q2`.
In dieser Kette wurde kein neuer algebraischer Fehler nachgewiesen.

## 1. Die Bezeichnungen auseinanderhalten

H004 Druck277/(98b) definiert `N_(j)=n_j+Q_j`. Auf Druck344/(112b)
führt Heim dagegen drei Koeffizienten mit den ähnlichen Namen
`N1,N2,N3` ein. Für die folgende Darstellung benennen wir nur diese um:

```text
x_j := N_(j) = n_j+Q_j,
c1 := alpha1, c2 := 2*alpha2/3, c3 := 2*alpha3.
```

`x_j` sind die Zonenbesetzungen, `c_j` die Koeffizienten. Das einzelne
`N` in `M(N)` bezeichnet wiederum die Resonanzordnung. Diese eigene
Notationshilfe ändert keine Quellenformel. Auch die `F,H` aus (112a)
sind nicht die gleichnamigen Hilfsgrößen aus der älteren (98c)-Kette.

## 2. Ausgangsformel und Massenskala

Mit der eigenen Abkürzung `r=alpha_-/alpha_+`, für `alpha_+!=0`, steht
auf H004 Druck278:

```text
M = mu_+ * [sum_(j=1)^4 alpha_j*G_j + (1-r)*F_S + q*r].   (98d)
```

Die anschließenden Zonenfunktionen lauten:

```text
G1 = x1^2*(1+x1)^2/4,
G2 = x2*(2*x2^2+3*x2+1)/6,
G3 = x3*(1+x3)/2,
G4 = x4.                                                  (98e)
```

(98c) setzt `alpha4=1`. Bereits Druck253/(97) definiert

```text
mu_+ = 4*mu*alpha_+,
mu_S = (1-r)*mu_+.
```

Somit ist der Faktor4 beim Übergang zu (112) weder eine neue Näherung
noch ein zusätzlicher Anpassungsparameter. Er folgt durch Einsetzen
dieser früheren Skalenrelation. Deren eigene physikalische Herleitung
oder numerischer Wert wird dadurch allerdings nicht erneut bewiesen.

## 3. Warum K, F und H entstehen

Zur kurzen Darstellung definieren wir ein eigenes Hilfspolynom
`Pcal(u)`; es ist nicht Heims Quantenzahl `P`:

```text
Pcal(u) = c1*u1^2*(1+u1)^2
        + c2*u2*(2*u2^2+3*u2+1)
        + c3*u3*(1+u3) + 4*u4.
```

Dann folgt aus (98e) unmittelbar `4*sum(alpha_j*G_j)=Pcal(n+Q)`.
Beim Ausmultiplizieren ordnet Heim auf Druck343-344 die Terme so:

| Anteil | Algebraische Bedeutung | Quellenbezeichnung |
|---|---|---|
| `K=Pcal(Q)` | Nur Gerüstgrößen `Q_j`; bei festem Zustand konstant | Gerüstanteil |
| `F=Pcal(n)` | Nur die veränderlichen kleinen Besetzungen `n_j` | Besetzungsanteil |
| `H=Pcal(n+Q)-Pcal(n)-Pcal(Q)` | Gemischte Produkte aus `n_j` und `Q_j` | Gemischter Anteil |

Der explizit gedruckte Mischterm lautet mit unserer c-Notation:

```text
H = 2*n1*Q1*[1+3*(n1+Q1+n1*Q1)+2*(n1^2+Q1^2)]*c1
  + 6*n2*Q2*(1+n2+Q2)*c2
  + 2*n3*Q3*c3.                                           (112a)
```

Wir haben diese konkrete Form mit der Differenz der ausmultiplizierten
Polynome verglichen, nicht H lediglich als den benötigten Rest definiert.
Alle Koeffizienten stimmen überein. Beispielsweise liefert die kubische
Zone2 genau `6*c2*n2*Q2*(1+n2+Q2)`. In Zone4 gibt es keinen Mischterm,
weil `4*(n4+Q4)=4*n4+4*Q4` schon linear zerfällt.

Damit gilt identisch:

```text
4*sum_(j=1)^4 alpha_j*G_j = K+F+H.
```

Die Identität benötigt weder Ganzzahligkeit noch eine bestimmte
Teilchenauswahl; sie gilt auch für reelle Argumente. Das ist ihre
algebraische Stärke und zugleich ihre Grenze: Sie entscheidet nicht,
welche Werte physikalisch zugelassen sind. Insbesondere ist `H` hier
ein Kreuzterm der Umformung, nicht allein dadurch ein neu bewiesenes
Wechselwirkungsgesetz.

Zwei hilfreiche Randfälle:

- Bei allen `n_j=0` verschwinden `F,H`; es bleibt das Gerüst `K`.
  Dies ist nicht mit Resonanzordnung `N=0` gleichzusetzen.
- Beim algebraisch leeren Besetzungstupel `x_j=0`, also `n_j=-Q_j`,
  gilt `K+F+H=0`. Die Einzelanteile können sich also aufheben;
  wir erklären sie nicht pauschal zu einzeln positiven Massen.

## 4. Die Zusammenfassung phi und Formel (112)

Heim setzt auf Druck343

```text
phi = 4*(1-r)*F_S + 4*q*r.
```

Damit wird (98d), ohne weitere Näherung in diesem Umformungsschritt,

```text
M = mu*alpha_+ * [4*sum(alpha_j*G_j) + phi]
  = mu*alpha_+ * [K+F+H+phi].                            (112)
```

Der Faktor `alpha_+` steht vor der gesamten Klammer. `phi` fasst den
F_S-Anteil und den Ladungsbeitrag zusammen; es ist nicht bloß ein anderer
Name für `F_S`. Unter dem dimensionslosen Klammeransatz trägt `mu` die
Masseneinheit. Es wurde hier kein Zahlenwert für eine Teilchenmasse erzeugt.

## 5. Was an F_S empirisch bestimmt wird

Der Text direkt nach (98e), Druck278, nennt die Beschreibung noch
unvollständig und führt sowohl die Bestimmung von `F_S` als auch die
Auswahl der Besetzungen als weitere Aufgaben an. Auf Druck342 wird nach
der Besetzungsauswahl zunächst aus zugeordneten Messmassen bestimmt:

```text
mu_S*F_S = M_emp - mu_+*[sum(alpha_j*G_j)+q*r].
```

Für `mu_S!=0` lässt sich daraus `F_S` ausrechnen. Das Einsetzen desselben
Wertes in (98d) liefert definitionsgemäß wieder `M_emp`; dieser einzelne
Rückweg wäre für sich kein unabhängiger Vorhersagetest. Bei `mu_S=0`
bestimmt diese Gleichung `F_S` überhaupt nicht. Der zweite Fall ist hier
nur eine algebraische Randprüfung, keine behauptete physikalische Wahl.

Die Quelle nennt17 verfügbare Punkte aus Komponenten der Multipletts
`v=1` bis `v=10`, mit Ausschluss von `e0` in `v=2`. Gesucht wird ein
Funktionsverlauf, der diese Punkte trifft und für `e0,v=11,v=12`
plausible Werte liefert. Das ist eine klare Unterscheidung zwischen
Rekonstruktion der verwendeten Daten und Extrapolation. Wir haben die17
Werte weder neu zusammengestellt noch einen Fit gerechnet; die Zahl
und Zuordnung sind Angaben der Quelle.

Der vorgeschlagene Ausdruck auf Druck343 lautet:

```text
4*(1-r)*F_S = A_v*F1*Fq*F_kappa/F2 + B_v*(P+Q),
phi = A_v*F1*Fq*F_kappa/F2 + B_v*(P+Q) + 4*q*r.          (111)
```

Die Hilfsfunktionen verwenden Zustandsquantenzahlen und bereits
eingeführte Größen; (111a/b) enthält außerdem `Y41` im Zusatz von `F2`,
`Y42` im `q*eta^2*(k-1)`-Term von `Fq`, `Y43` im Zusatz von `F_kappa`
und `Y44` bei `B_v`. Daraus folgt nicht, dass vier unabhängige freie
Fitparameter nachgewiesen wären. Ihre Werte und Herkunft sind eine
gesonderte Quellenfrage, keine Wahlmöglichkeit dieses Audits.

Die vorgeschlagene Funktionsform ist mehr als17 einzeln eingesetzte
Konstanten: Sie verlangt eine gemeinsame Beschreibung verschiedener
Zustände. Ob und wie gut sie die Daten tatsächlich reproduziert und ob
sie neue Zustände korrekt vorhersagt, ist mit der hier bestätigten
Algebra aber noch nicht geprüft.

## 6. Abgrenzung zur vorigen Restfrage und zur Quellenkontrolle

Auf Druck323 gilt für die definierte Besetzungsvariation `delta F_S=0`.
Die wirksame Rolle von `F_S` in der Masse widerspricht seinem Wegfall
in dieser Variation nicht. Die neue algebraische Gleichheit repariert
deshalb keinen alten (108)-Rest bei unveränderten Eingaben. Eine
physikalische Fehlerfortpflanzung bleibt ein eigener Auftrag.

Zwei Leseverdachte wurden am Detailbild verworfen, nicht als Befunde
weitergeführt: Auf344 steht in beiden K-Zeilen `3*Q2`; auf342 steht
bei `B_v` `xi^(-2)`, nicht `xi^(kappa-2)`. Die zweite Grundform entspricht
der nachfolgenden (111b)-Form bei `Y44=1`. Das ist eine bedingte
algebraische Übereinstimmung, keine neue Festlegung von Y44.
Der mehrdeutige kleine-f-Satz auf343 bleibt für unsere Schlüsse unbenutzt.

## 7. Prüfung und nächster begrenzter Auftrag

Zwölf neue [Regressionstests](../tests/test_mass_chain.py) prüfen
koeffizientenweise die vier Polynomzerlegungen, rationale Kontrollfälle,
Skalen-/phi-Umformung und Randfälle. Der unabhängig erstellte
[Algebrablock](../04_reconstruction/alpha_audit/reviews/MASS_CHAIN_ALGEBRA_REVIEW_2026-09-07.md)
bestand bei Root erneut1841 exakte Kontrollen. Die künstliche2-statt3-
Mutation ist darin nur eine Empfindlichkeitsprobe des Checks, keine Quelle.

Die vollständige Quellenbilanz steht in
[MASS_CHAIN_SOURCES](../03_notes/MASS_CHAIN_SOURCES_2026-09-07.md).
Originalsicht und interne Gegenreviews sind kein externes Peer Review;
Testzahlen sind keine Anzahl unabhängiger Experimente. Alte Eingaben,
Rechner, Ergebnisse und49 Normalisierungs-CSV-Zeilen bleiben erhalten.

FIND-048 dokumentiert eine positive bedingte Reproduktion, keinen neuen
Fehler. Als nächster Einzelauftrag bietet sich die Quellenprovenienz des
F_S-Ansatzes an: Wo sind die17 verwendeten Massenwerte, ihre damaligen
Quellen und die Y41-44-Festlegung dokumentiert? Zunächst nur Belege und
Eingaberollen erfassen, keine nachträgliche Kalibrierung oder moderne
Messdatenbewertung.
