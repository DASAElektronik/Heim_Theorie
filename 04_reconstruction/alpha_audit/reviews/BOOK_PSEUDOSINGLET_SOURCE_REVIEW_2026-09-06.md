# H004 Pseudosingulett: Buch-Eingabevertrag (ohne Massenrechnung)

Stand: 2026-09-06. Eng begrenzte visuelle Quellenlesung von Heim,
*Elementarstrukturen der Materie II* (1996), lokale Datei
`01_sources/heim_primary/Burkhard Heim - 1996 - Elementarstrukuren der Materie 2.pdf`,
SHA-256 `F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.
Gelesen wurden die vollständigen Druckseiten 263--264 / PDF 269--270,
277--278 / PDF 283--284, 288--289 / PDF 294--295, 325--332 / PDF 331--338
und 342 / PDF 348. Die Sichtbilder liegen unter
`tmp/pdfs/book_pseudosinglet/edm2-269.png`, `-270.png`, `-283.png`,
`-284.png`, `-294.png`, `-295.png`, `-331.png` bis `-338.png`, und
`-348.png`. OCR diente nur als Locator. Keine H006/H010-Eingaben,
Massenrechnung, Zielwertwahl oder Neuner-Epsilon wurden verwendet.

## Ergebnis

Für den **Buchkanal** des Pseudosinguletts liefert die Quelle die Signatur
`k=1, Q=1, kappa=1, q=1` und die algebraischen Gerüstbesetzungen. Sie
identifiziert den Resonanzgrundzustand als `N=0`, bestimmt aber dadurch
**nicht** automatisch das konkrete P4-Quadrupel `n_j(0)` des aktiven
Pseudosinguletts. Insbesondere ist `n_j=0` im Text die separate
Gerüstinterpretation des anderen `k=1, Q=1`-Spinors mit `kappa=0`.
Ein quellenreiner weiterer Fall benötigt für den bereits festgelegten
V6-Kanal noch die durch die Buch-Erschöpfung gewonnenen `N_(j)`.

## 1. Kanal: was der Text explizit auswählt

Die Multipletliste (101a), Druck 289 / PDF 295, führt für `k=1` unter
anderem den Skalar `(1)(1000)0(0)` und die beiden Spinordoubletts
`(2)(1110)0(0,-1)` und `(3)(1111)0(-1)` auf. Die Folgeseiten behandeln das Grundmuster
als empirisch zuordenbare Möglichkeit; sie sind keine Auswahlrechnung für
ein bestimmtes Teilchen.

Die für den Vertrag entscheidende Klarstellung steht bei (108)/(108a),
Druck 330 / PDF 336:

```text
bei k=1: Skalarterme Q=0 und zwei Spinorterme Q=1;
der Spinor mit kappa=0 muss als n_j=0 interpretiert werden,
der andere Spinorterm ist das Pseudosingulett mit kappa=1 und q=1.
```

Damit ist `k=Q=kappa=q=1` für das Pseudosingulett quellenbelegt. Die
Gleichsetzung `n_j=0` mit diesem aktiven Kanal wäre dagegen eine
Verwechslung: Sie gehört dort ausdrücklich zum `kappa=0`-Spinor.
Der Text nennt das Pseudosingulett auf Druck 332 / PDF 338 zudem
`(1111)0(-1)`; dies ist die notationsnahe Kennzeichnung, kein durch diese
Lesung aufgelöster Ersatz für alle Quantenzahlen anderer Formelstränge.

## 2. Gerüstbesetzungen Q_j und alpha_j

(98b), Druck 277 / PDF 283, definiert für `j<=4` bzw. `(n,m,p,sigma)`

```text
N_(j)(t) = n_j(t) + Q_j,
Q_n = 3*2^(s-2),   Q_m = 2^s-1,
Q_p = 2^s+2(-1)^k,   Q_sigma = 2^(s-1)-1,
s = k^2+1 = const(t).
```

Somit folgt für den **gegebenen** Kanal `k=1` rein algebraisch

```text
(Q_n,Q_m,Q_p,Q_sigma) = (3,3,2,1).
```

Der vorausgehende Text (Druck 263--264 / PDF 269--270) nennt `Q_j` die
zeitlich konstanten Protosimplexbesetzungen eines `k`-fachen
konfigurativen Gerüsts. Er motiviert deren Bestimmung teilweise über die
Empirie von Elektron und Proton. Das ist eine Autorenmotivation, nicht
eine hier nachgewiesene unabhängige Herleitung.

(98c), Druck 278 / PDF 284, gibt die Koeffizienten und den Hilfsterm an:

```text
2 alpha_1 = 1 + sqrt(eta_qk),   alpha_2 eta_qk = 1,
k alpha_3 = e^(k-1) - k q F,   alpha_4 = 1,
F = H + G,
3H = alpha(1+sqrt(eta_qk)) (xi/eta_qk^2)^(2k+1) eta_qk^3,
e eta_qk G = eta_11(2 xi eta_qk)^k
             ((1-sqrt(eta_qk))/(1+sqrt(eta_qk)))^2.
```

Unter `k=q=1` und derselben Indexeinsetzung `eta_qk=eta_11` folgt
formal `alpha_1=(1+sqrt(eta_11))/2`, `alpha_2=1/eta_11`,
`alpha_3=1-F`, `alpha_4=1`. Die Seite definiert `F=H+G` samt seinen
Ausdrücken; ob und wie diese Konstruktion physikalisch hergeleitet ist,
ist eine andere Frage und wird hier nicht behauptet.

## 3. w, W und der einzelne Pseudosingulett-Beitrag

Für den Resonanzrahmen setzt (108), Druck 330 / PDF 336,

```text
alpha_1 N_(1)^3 + alpha_2 N_(2)^2 + alpha_3 N_(3)
 + exp[-(2k-1)N_(4)/(3Q_4)] = W(vx)[1+f(N)],
W(vx)=g(k,q) w(vx),
g(k,q)=alpha_1 Q_1^3+alpha_2 Q_2^2+alpha_3 Q_3+exp[-(2k-1)/3],
f(N>=0)>=0, delta_N f>0.
```

Die unmittelbar vorausgehende Resonanzdarstellung, Druck 327 / PDF 333,
setzt `F=1+f(N)` mit `f(0)=0` (und `f(N)>0` für `N>0`). Damit ist `N=0`
ein Resonanzgrundzustand und (108) hat den Faktor `1+f(0)=1`. Druck
326--329 / PDF 332--335 beschreibt diesen Punkt als
V6-Gitterpunkt mit einem ihm komplementären P4-Quadrupel `n_j(0)` und
trennt ihn von V7-Verschiebungen für `N>0`.

Die Strukturpotenz wird ausdrücklich als heuristischer Ansatz behandelt,

```text
w = 1 + (2-k) underline(w_1) + (k-1) underline(w_2),
underline(w_k)(n_j=0)=0.                         (108a)
```

Für `k=1` reduziert sich diese **Algebra** zu `w=1+underline(w_1)`.
Druck 331--332 / PDF 337--338 bestimmt dafür

```text
X_6 = kappa eta_qk F_16,
underline(w_1) = (1-Q) sum_(i=1)^5 X_i + Q X_6.
```

Für die Buchsignatur `Q=kappa=q=k=1` folgt daher
`underline(w_1)=eta_11 F_16` und `w=1+eta_11 F_16`, sofern in dieser
Einsetzung `eta_qk=eta_11` verwendet wird. Das ist eine direkte
Substitution, keine Bestimmung von `F_16`; die unmittelbar anschließende
Seite sagt, die Form der metronischen Funktionen `F_im` könne vorläufig
nicht deduziert werden und fordert nur einen endlichen Grenzwert
(Druck 331 / PDF 337).

## 4. Was N=0 gerade nicht liefert

Die Symbolschichten sind im Buch verschieden:

* `N=0` bezeichnet den Resonanzgrundzustand/V6-Fall.
* `N_(j)=n_j+Q_j` sind die vier zonalen Besetzungen.
* `n_j=0` bezeichnet auf Druck 325 / PDF 331 die zeitlich konstante
  Gerüststruktur und auf Druck 330 / PDF 336 speziell den `kappa=0`-
  Spinor, nicht den aktiven Pseudosingulett-Spinor.

Nach dem Erschöpfungsverfahren werden erst die `N_(j)` gewonnen; daraus
folgen die komplementären P4-Rasterpunkte
`n_j=N_(j)-Q_j` zu V6-Punkten `N=0` oder zu V7-Verschiebungen `N>0`
(Druck 342 / PDF 348). Diese Reihenfolge belegt: Die Resonanzzahl allein
setzt weder `N_(j)=Q_j` noch `n_j=0` und bestimmt kein konkretes
Quadrupel. Das Buch nennt zwar für einen V6-Punkt eine eindeutige
Zuordnung zu einem `n_j`-Quadrupel (Druck 326 / PDF 332). Die im aktuellen
Arbeitsvertrag festgelegte V6-Kanalsignatur ersetzt jedoch nicht die noch
fehlende quellengetreue Erschöpfung zu seinem numerischen P4-Quadrupel.

## 5. Minimaler quellenreiner Eingabevertrag und offene Teile

Für eine spätere **bedingte** Buchauswertung ist damit quellengetragen:

```text
Kanal:       k=1, Q=1, kappa=1, q=1  (Pseudosingulett)
Resonanz:    N=0, daher f(0)=0 und V6 statt V7
Gerüst:      (Q_1,Q_2,Q_3,Q_4)=(3,3,2,1)
Koeffiz.:    alpha_j aus (98c), nach explizit gewähltem eta_qk-Profil
Potenz:      W=g*w; w=1+eta_11 F_16 unter obiger Indexeinsetzung
```

Offen bleiben ohne zusätzliche, quellengetreue Selektion: das konkrete
P4-Quadrupel `n_j(0)` bzw. `N_(j)`, eine spezifische Form von `F_16`,
ein vollständig gewähltes eta-Profil und jede Zuordnung zu einem gemessenen
Teilchen. Auch der auf Druck 342 beginnende `F_S`-Abschnitt verweist für
seine Bestimmung ausdrücklich auf vorhandene empirische Massedaten; er
wurde deshalb weder als Eingang noch als stiller Kalibrierungsschritt
verwendet.

## Scope

Dies ist eine Quellenrekonstruktion, keine Massenrechnung und keine
Vorhersage. Die hier gezogenen Reduktionen sind als algebraische
Konsequenzen der ausdrücklich gesetzten Kanalwerte markiert; sie ersetzen
weder die offene Auswahl der metronischen Funktionen noch den Buch-
Erschöpfungsschritt.
