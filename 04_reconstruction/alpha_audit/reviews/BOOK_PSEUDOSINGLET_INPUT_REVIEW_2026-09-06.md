# Buchinterner Eingabevertrag fuer das N=0-Pseudosingulett

Stand: 2026-09-06, Etappe 30, Ausgang `00180ec`. Diese Review legt vor
einer Zahlenrechnung fest, welche dimensionslosen Eingaben die vorliegende
Buchfassung H004 selbst verlangt. Sie berechnet weder eine Masse noch eine
Besetzung und importiert keine Konstantentabelle aus H006, H010 oder H015.

## 1. Quelle und Sichtumfang

Quelle ist Burkhard Heim, *Elementarstrukturen der Materie II*, vorliegende
Ausgabe 1996, lokale Datei
`01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf`,
SHA-256
`F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.
Der Hash identifiziert die lokale Kopie, nicht die Echtheit eines
Papieroriginals.

Nach vollstaendig gelesener PDF-Skill-Anleitung wurden die tragenden
Vollseiten visuell geprueft:

- Einfuehrung Druck 1 / PDF 12 (`Y_k`-Tabellenkonvention);
- Druck 33 / PDF 42 (unindiziertes `vartheta`);
- Druck 251 / PDF 257, (96b) (`2*xi=1+sqrt(5)`);
- Druck 266--267 / PDF 272--273, (98) (`eta`, `eta_qk`, `vartheta_qk`);
- Druck 271--278 / PDF 277--284, (98b)/(98c) (`alpha_j`, `Q_j`, `xi`);
- Druck 288--291 / PDF 294--297, (101)--(101b) (Pseudosingulettmuster);
- Druck 300--302 / PDF 306--308, (105) (`Y3`, `A1`, `A2`, `alpha`);
- Druck 325, 330--336 / PDF 331, 336--342, (108)--(109b)
  (`g`, Strukturpotenz, `A16`, `Y9`).

OCR und bestehende Reviews dienten nur der Navigation. Neue eigene Bilder
liegen unter `tmp/pdfs/book_pseudosinglet_input/`; weitere verwendete
Vollseiten unter `tmp/pdfs/eta_configuration/`, `alpha3_book_origin/`,
`correlation_chain/` und `a16_book/`.

## 2. Ergebnis: primaerer Buchvertrag

Fuer eine spaetere, getrennte Zahlenrechnung ist folgendes Profil
quellennah und vor dem Ergebnis festlegbar:

```text
Profilname: H004_BOOK_105_Y3_1_Y9_1

Zustand: nu=3, (k,P,Q,kappa)=(1,1,1,1), q=1,
         gedruckt epsilon*q_x=-1, N=0
pi,e: mathematische Konstanten
xi: (1+sqrt(5))/2
eta: eta_(1,0)
d: eigener Alias d := eta_(1,1), kein Buchsymbol
eta12: eta_(1,2)
Y3: 1 in (105)
alpha: kleiner positiver Zweig der unverkuerzten Gleichung (105)
Y9: 1 gemaess der ausdruecklichen Tabellenanhang-Konvention
```

`Y3=1` und `Y9=1` sind dabei zwei getrennt zu protokollierende
Spezialisierungen. Sie werden nicht voneinander hergeleitet und nicht nach
einem kleinen Gleichungsrest gewaehlt. Das Profil ist eine durch das Buch
selbst verwendete numerische Spezialisierung, keine Herleitung der
Unsicherheitsfaktoren.

Als optionale, getrennte Eingabesensitivitaet ist zulaessig:

```text
Profilname: H004_PRINTED_ALPHA
wie oben, aber alpha := 0.007297354572 aus Druck 302.
```

Dieses zweite Profil benutzt genau den gedruckten Alpha-Dezimalwert. Es
darf nicht zugleich als numerisch neu geloester (105)-Zweig ausgegeben und
nicht mit dem ebenfalls gedruckten gerundeten Kehrwert vermischt werden.
Die Differenz beider Profile waere eine Druckwertsensitivitaet, keine
alternative physikalische Loesung. Ob die Abweichung durch Rundung oder
eine andere Ursache entstand, wird nicht unterstellt.

## 3. Zustandsdaten und ihre Grenzen

Druck 288 / PDF 294 definiert die kompakte Form

```text
(nu)(k P Q kappa) epsilon*C (epsilon*q_x)_0^P.             (101)
```

Druck 289 / PDF 295 listet das Muster 3 als
`(3)(1111)0(-1)`. Druck 290--291 / PDF 296--297 identifiziert Muster 3
heuristisch mit dem negativ geladenen Pseudosingulett. Druck 332 / PDF 338
nennt fuer dieses Pseudosingulett nochmals `k=1`, `q=1`, `Q=1` und
`kappa=1`. Damit sind die fuer den Strukturterm aktiven Betragsdaten

```text
k=P=Q=kappa=q=1,  epsilon*q_x=-1
```

buchintern belegt. Aus dem gedruckten Produkt `epsilon*C=0` wird hier
nicht unnoetig ein einzelnes `epsilon` rekonstruiert. Deshalb wird auch
der letzte Eintrag glyphentreu als Produkt `epsilon*q_x=-1` festgehalten;
eine spaetere Formel, in der `q_x` einzeln aktiv waere, braeuchte zusaetzlich
eine explizite Wahl von `epsilon`. Im betrachteten `A16`-Kanal ist nur
`q=abs(q_x)=1` aktiv. Die Resonanzordnung `N=0` ist nicht die Musterziffer
`nu=3` und nicht eine der vier Besetzungen `N_(j)`.

Aus Druck 327 / PDF 333 folgt fuer `N=0` `f(0)=0`. Das bestimmt noch kein
Besetzungstupel `N_(1)..N_(4)` und keine Masse. Insbesondere ordnet Druck
330 / PDF 336 die Interpretation `n_j=0` ausdruecklich dem anderen
`k=1,Q=1`-Spinor mit `kappa=0` zu; sie darf nicht auf das aktive
Pseudosingulett mit `kappa=1` uebertragen werden.

## 4. Drei verschiedene eta-Groessen

Druck 266--267 / PDF 272--273 gibt

```text
eta_qk * fourth_root(pi^4 + q^4*(4+k)) = pi,               (98)
eta_q0 = eta_q,
eta_(1,0) = eta.
```

Damit sind innerhalb derselben Buchfassung exakt definiert:

```text
eta      = eta_(1,0) = pi/fourth_root(pi^4+4),
eta_11   = eta_(1,1) = pi/fourth_root(pi^4+5),
eta_12   = eta_(1,2) = pi/fourth_root(pi^4+6).
```

Die Indexreihenfolge ist in (98) `eta_(q,k)`. Deshalb ist das `eta_(1,k)`
in (105) fuer `k=1,2` gerade `eta_11` beziehungsweise `eta_12`. Eine alte
H006-Indexkonvention darf hier nicht daruebergelegt werden.

Der Alias `d=eta_11` ist nur eine lesbare Rekonstruktionsabkuerzung fuer
den aktiven Zustand `q=k=1`. Er ist nicht in H004 gedruckt. Insbesondere
gilt nicht `eta=d`: Das unindizierte `eta` in `vartheta` und `A16` ist
`eta_(1,0)`, waehrend der aeussere Pseudosingulettfaktor `eta_qk=d=eta_11`
ist.

Druck 33 / PDF 42 wiederholt

```text
vartheta = 5*eta + 2*sqrt(eta) + 1.
```

Druck 267 definiert analog `vartheta_qk`. Gleichung (105) druckt jedoch
unindiziertes `vartheta`; deshalb wird dort nicht `vartheta_11` eingesetzt.

## 5. Alpha: Abhaengigkeitskette von (105)

Druck 302 / PDF 308 schreibt

```text
(2*pi)^5*alpha*sqrt(1-alpha^2)
    = 9*vartheta*(1-A1*A2*Y3),                              (105)

(1+sqrt(eta_(1,k)))*A_k
    = (1-sqrt(eta_(1,k)))*sqrt(eta_(1,k)),  alpha>0.
```

Also sind `A1` und `A2` ohne neuen Zahleninput aus `eta_11` und `eta_12`
bestimmt. Die Seite setzt fuer ihre anschliessende numerische Loesung
ausdruecklich `Y3=1`. Beide dort resultierenden Kopplungswerte sind
positiv; die Quelle identifiziert anschliessend den kleinen Zweig
`alpha_(+)` mit `alpha`. Das folgt nicht aus `alpha>0` allein. Das primaere
Profil loest genau diese unverkuerzte Gleichung; es importiert weder einen
modernen Alpha-Wert noch den rechten Ausdruck eines alten H006-Rechners.

Der Text fuehrt `Y3` als Unsicherheitsfaktor des Korrelationsschlusses ein.
`Y3=1` ist daher eine deklarierte Spezialisierung, kein unabhaengiger
Beweis fuer den Faktor. Die auf Druck 302 ebenfalls gedruckten Dezimalwerte
sind Ausgaben dieser Darstellung und keine zusaetzlichen exakten Konstanten.

## 6. xi und der nicht indizierte Grossbuchstabe Y

Druck 251 / PDF 257, (96b), und Druck 275 / PDF 281 geben

```text
2*xi = 1+sqrt(5).
```

Auf Druck 273--275 bezeichnet hingegen

```text
Y = X(z+1)/X(z-1)
```

ein Folgenverhaeltnis. Aus der Rekursion `X_v=X_(v-1)+X_(v-2)` und dem
angenommenen grossen Grenzindex setzt der Text `Y=xi^2`. Dieses
**unindizierte** `Y` ist weder der Unsicherheitsfaktor `Y3` noch `Y9`.
Nach der Substitution erscheint es in (98c) nicht mehr als freier Input.

Fuer das Profil wird deshalb der exakte Buchwert
`xi=(1+sqrt(5))/2` verwendet, nicht eine Dezimalzahl aus H006/H010.
Die Rekursions-/Grenzwertannahme und die empirische Wahl der vorherigen
`A_i/B_i` bleiben Quellenannahmen; der exakte Wert von `xi` macht sie nicht
zu einer voraussetzungslosen Ableitung.

## 7. `alpha_1`, `alpha_2`, `alpha_3` und `g`

Druck 271 und (98c) auf Druck 278 / PDF 284 liefern

```text
alpha1 = (1+sqrt(eta_qk))/2,
alpha2 = 1/eta_qk,
k*alpha3 = exp(k-1)-k*q*(H+G),
3*H = alpha*(1+sqrt(eta_qk))
      *(xi/eta_qk^2)^(2*k+1)*eta_qk^3,
e*eta_qk*G = eta_11*(2*xi*eta_qk)^k
             *((1-sqrt(eta_qk))/(1+sqrt(eta_qk)))^2.        (98c)
```

Hier sind `alpha1..alpha3` Zonenkoeffizienten; das nackte `alpha` in `H`
ist die Kopplungskonstante aus (105). Fuer `k=q=1` ist in allen
`eta_qk`-Stellen `eta_11` einzusetzen. Das `e` in (98c) ist die
Eulersche Zahl, wie die Buchprosa zu den Grenzwerten `pi,e,xi` bestaetigt.

Druck 277 / PDF 283, (98b), gibt mit `s=k^2+1`

```text
Q1=3*2^(s-2), Q2=2^s-1,
Q3=2^s+2*(-1)^k, Q4=2^(s-1)-1.
```

Fuer `k=1` folgt daher `(Q1,Q2,Q3,Q4)=(3,3,2,1)`. Diese `Q_j` sind
Geruestbesetzungen und nicht die einzelne Spinorzahl `Q=1` aus (101).

Druck 325 und (108) auf Druck 330 / PDF 336 definieren

```text
g(k,q) = alpha1*Q1^3 + alpha2*Q2^2 + alpha3*Q3
         + exp(-(2*k-1)/3).
```

In `alpha1..alpha3` und `g` steht nach (98c) kein `Y_k`-Unsicherheitsfaktor.
Das zuvor auftretende unindizierte Folgenverhaeltnis `Y` ist bereits durch
`xi^2` spezialisiert. Fuer diese Kette sind deshalb keine weiteren
`Y1`, `Y2` oder sonstigen Tabellenfaktoren einzufuehren.

## 8. `A16`, `Y9` und der aktive Strukturkanal

Druck 335 / PDF 341, (109b), druckt eindeutig

```text
A16 = (pi*e)^2
      *[1 + alpha/(5*eta)*(1+6*alpha/pi)]*Y9.
```

Das eta im Nenner ist unindiziert, also nicht `d=eta_11`. Der Faktor
`Y9` multipliziert die gesamte Klammer. Druck 335 sagt zugleich, dass die
`A_im` nicht explizit hergeleitet seien und mit empirischen
Grundzustandsdaten heuristisch auf `pi,e,xi,alpha,beta` zurueckgefuehrt
wuerden.

Die Einfuehrung, Druck 1 / PDF 12, ordnet die `Y_k` ungeklärten
mathematischen Beziehungen zu und sagt ausdruecklich, fuer die theoretischen
numerischen Daten des Tabellenanhangs seien **alle** `Y_k=1` unterstellt.
Das traegt die Profilwahl `Y9=1`, nicht aber eine allgemeine Behauptung
`Y9` sei hergeleitet oder immer eins.

Fuer das Pseudosingulett setzt Druck 332 / PDF 338

```text
X6=kappa*eta_qk*F16,
underline(w1)=(1-Q)*sum_(i=1)^5 X_i + Q*X6.
```

Im Grenzbereich wird `F16` zu `A16`. Mit `k=Q=kappa=q=1` folgt daher

```text
underline(w1)=eta_11*A16,
w=1+underline(w1)=1+eta_11*A16,
W=g*(1+eta_11*A16).
```

Damit sind in diesem reduzierten Kanal alle anderen `A_im` und ihre
`Y_k` inaktiv. Auch `beta` wird fuer dieses `W` nicht benoetigt. Das ist
eine algebraische Kanalreduktion der gedruckten Formeln, keine Behauptung,
die gesamte Koeffizientenmatrix oder die Besetzungsauswahl sei bestimmt.

## 9. Quellenstatus und verbleibende Grenze

Das dimensionslose Konstantenprofil bis einschliesslich `W` ist numerisch
geschlossen, **wenn** `Y3=1` aus der Rechnung auf Druck 302 und `Y9=1`
aus der Tabellenanhang-Konvention vorab angenommen werden. Das macht den
gesamten Zustand noch nicht auswahlseitig geschlossen. Ohne `Y3` bleibt
`alpha` in (105), ohne `Y9` bleibt `A16` und damit `W` parametrisch. Es
waere unzulaessig, einen der beiden Faktoren nach einem kleineren Rest oder
einer passenden Masse zu waehlen.

Es liegt kein buchinterner Formelkonflikt zwischen `eta`, `eta_11` und
`eta_12` vor; der Konflikt entsteht erst durch eine unmarkierte
Gleichsetzung oder den Import einer anderen Indexfassung. Ebenso sind
`Y=xi^2`, `Y3` und `Y9` keine austauschbaren Schreibweisen.

Die Zahlenkette ist trotz ihrer Auswertbarkeit keine unabhaengige
Vorhersage aller Eingaben: Druck 275 nennt die Koeffizientenwahl fuer
`alpha3` optimal an Elektron/Proton angepasst, und Druck 335 nennt die
`A_im`-Bestimmung heuristisch und auf empirischen Grundzustandsdaten
beruhend. Das ist eine belegte Quellenklassifikation, keine neue
physikalische Widerlegung.

Nicht Gegenstand und weiterhin offen sind das Besetzungstupel
`N_(1)..N_(4)`, die Kompatibilitaet aller Auswahlgates, eine Masse sowie
die physikalische Herleitung der heuristischen `A16`-Form. Der hier
festgelegte Inputvertrag darf fuer diese spaeteren Schritte verwendet
werden, ohne H006/H010-Konstanten oder ein gewuenschtes Ergebnis
einzuschmuggeln.
