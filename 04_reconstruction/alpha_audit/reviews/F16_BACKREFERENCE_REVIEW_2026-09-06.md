# F16/A16: Rueckverweise und Bestimmtheitsstatus in H004

Stand: 2026-09-06. Enge Quellenpruefung von Heim,
*Elementarstrukturen der Materie II* (vorliegende Ausgabe 1996). Keine
Massenrechnung, kein Fit und kein fassungsuebergreifender Ersatz.

## 1. Enges Ergebnis

Die gepruefte Buchkette legt die **Rolle** von `F16` und den Grenzuebergang
zu `A16` fest, aber kein Operator-/Randwertproblem, das den Zahlenwert von
`A16` unabhaengig eindeutig erzeugt:

```text
metronische R3-Funktion F16(mu)
  -> geforderte Konvergenz fuer mu -> unendlich / tau -> 0
  -> endlicher reeller Grenzwert A16
  -> Strukturterm X6 = kappa*eta_qk*F16
  -> Grenzterm kappa*Q*eta_qk*A16 in underline(w1).
```

Die Quelle sagt selbst, die Form der `F_im` koenne vorlaeufig nicht
deduziert werden. Auf Druck 335 wird daraus ausdruecklich gefolgert, dass
auch `A_im` und `A66` nicht explizit hergeleitet sind. Die anschliessende
A16-Formel wird als Teil einer heuristischen, an empirischen
Grundzustandsdaten orientierten Koeffizientenbestimmung eingefuehrt.

Das bedeutet nicht, dass `A16` in jeder denkbaren erweiterten Rechnung ein
freier Parameter bleiben muss. Eine unabhaengig vollstaendig bestimmte
Auswahlgleichung koennte eine bestimmte Koeffizientenkombination und in
einem isolierenden Sonderfall auch `A16` algebraisch festlegen. Eine solche
unabhaengige Isolierung oder ein vollstaendiges Randwertproblem fuer `F16`
ist in der hier verfolgten Quellenkette jedoch nicht gegeben.

## 2. Direkte Definitionen auf Druck 330--334

### Druck 330 / PDF 336

Nach (108)/(108a) bezeichnet das Buch `w=W/g` als Strukturpotenz und nennt
die Zerlegung in den dort unterstrichenen Hilfsgroessen

```text
w = 1 + (2-k)underline(w1) + (k-1)underline(w2)
```

einen heuristischen Ansatz. Dieselbe Seite fuehrt danach die verschobenen,
nicht unterstrichenen Buchvariablen durch
`w1=k-1+underline(w1)` und `w2=2-k+underline(w2)` ein und schreibt damit
die Potenzform (109) vor. Diese beiden Notationsebenen werden hier nicht
gleichgesetzt. Danach werden die Strukturbeitraege durch die
Quantenzahlen aus (101a) und durch metronische `R3`-Funktionen der
Selektoren beschrieben. Das Buch schreibt sinngemaess

```text
F_im(mu_s) = phi_im;mu
```

und sagt, dass diese Funktionen von den Metronenziffern `mu_s` der
`R3`-Dimensionen abhaengen und die betrachtete Struktur im `R3`
wiedergeben. Der Nullpunkt der `mu_s` wird durch das Korrelationszentrum
der internen Kondensorfluesse festgelegt.

Das ist eine Variablen-/Ursprungsfestlegung. Es ist auf der Seite keine
explizite Differenz-, Differential- oder Eigenwertgleichung fuer
`phi_im`/`F_im`, kein Funktionswert `F_im(0)` und keine Normierung von
`F16` angegeben.

### Druck 331--332 / PDF 337--338

Druck 331 sagt passagescharf:

- die Form der `F_im` koenne „vorlaeufig nicht deduziert“ werden;
- akzeptiere man ihre Existenz, muessten sie fuer divergierende
  `mu_s -> unendlich` gegen konstante endliche Schranken konvergieren.

Die Seiten bauen anschliessend die skalaren und spinoriellen Summanden aus
den `F_im` und den Musterdaten auf. Fuer den hier interessierenden Term gilt
auf Druck 332:

```text
X6 = kappa*eta_qk*F16,
underline(w1) = (1-Q)*sum_(i=1)^5 X_i + Q*X6.
```

`X6` wird dem Pseudosingulett zugeordnet. Damit sind Index, Vorfaktor und
Strukturrolle von `F16` bestimmt; die Funktion selbst wird dadurch nicht
berechnet.

### Druck 333--334 / PDF 339--340

Auf Druck 333 werden weitere `Z_r`-Terme wiederholt mit vorsichtigen
Formulierungen wie „sollte“, „waere“, „vorgeschlagen“ und „denkbar“
aufgebaut; die Gesamtheit wird als durch (101a) „mehr spekulativ gegeben“
bezeichnet.

Druck 334 setzt fuer den dritten Gueltigkeitsbereich die Grenzrelationen

```text
lim_(tau->0) F_im = lim_(mu->infinity) phi_im;mu = A_im = const < infinity,
lim_(tau->0) F = A = const < infinity.
```

Die Quelle behauptet, diese Relationen seien in der beobachtbaren
`R3`-Umgebung jenseits `j=3` in sehr guter Naeherung erfuellt, sofern die
`A_im` und `A` richtig bestimmt seien. Sie setzt anschliessend

```text
A = A66
```

„aus Gruenden der spaeteren Vereinfachung“.

Das liefert Existenz, Endlichkeit, Realitaetsziel und eine Identifikation
zweier Grenzsymbole. Es gibt keinen Zahlenwert fuer `A16`, keinen
Funktionsverlauf, keine Konvergenzrate und keinen unabhaengigen
Normierungswert. Insbesondere bestimmt die Gleichsetzung `A=A66` den
gemeinsamen Wert nicht.

## 3. Direkte Selbsteinordnung auf Druck 335 / PDF 341

Nach der Matrixdarstellung von `A_im` sagt der Text:

- `A_im=A_im*` und `A66=A66*`: Selbstkonjugation der skalaren Eintraege,
  also Realitaet; daraus wird hier keine Matrix-Hermitizitaet abgeleitet;
- `F_im` seien bislang nicht explizit herzuleiten gewesen;
- daher gelte dies auch fuer `A_im` und `A66`;
- unter Verwendung von (101b) und empirischen Grundzustandsdaten koenne
  man die Koeffizienten **heuristisch numerisch** auf `pi`, `e`, `xi` und
  die Kopplungskonstanten `alpha`, `beta` aus (105a) zurueckfuehren;
- dabei traeten Unsicherheitsfaktoren `Y_k` auf.

Die A16-Zeile folgt in genau diesem System:

```text
A16 = (pi*e)^2 * [1 + alpha/(5*eta)*(1+6*alpha/pi)] * Y9.
```

Auf dieser Seite wird keiner der Faktoren `(pi*e)^2`, `1/5`, `6/pi`,
`eta^(-1)` oder `Y9` aus einem Operator oder aus Randdaten von `F16`
entwickelt.

## 4. Status der tatsaechlich benannten Rueckverweise

| Rueckverweis | Fundstelle | Was er liefert | Was er fuer F16/A16 nicht liefert |
|---|---|---|---|
| (98), (98a) | Druck 267--269 / PDF 273--275 | Definitionen interner Ladungskomponenten, `eta_qk`, Potentialverhaeltnisse und die als spekulativ eingeordnete Begrenzung `k_max=2`, `q_max=3` | Keine Gleichung fuer `F16(mu)`, keinen Grenzwert `A16` |
| (101a) | Druck 289 / PDF 295 | Liste der zulaessigen Grundmuster/Quantenzahlkennzeichnungen | Keine Funktions- oder Randbedingung fuer `F16` |
| (101b) | Druck 291 / PDF 297 | Ausdruecklich empirisches Interpretationsschema der Muster als Teilchenfamilien, darunter das Pseudosingulett | Empirische Zuordnung ist kein Operator, der den Grenzwert berechnet |
| (105a) | Druck 302 / PDF 308 | Bezeichnungen `alpha_(+)=alpha`, `alpha_(-)=beta` und die Naeherung `beta ~= 137 alpha` nach der vorherigen Korrelationsrechnung | Liefert Einsatzkonstanten fuer die heuristische A-Matrix, aber keine F16-Dynamik |

(96) auf Druck 245 / PDF 251 definiert die Protosimplexladung als
ganzzahliges Vielfaches einer Einheitskondensation und fuehrt die
Konfigurationskennziffern weiter. Es ist ein upstream-Begriffsanker fuer die
Musterkonstruktion, wird im geprueften F16-Abschnitt aber **nicht** als
direkte Bestimmungsgleichung fuer `F16` oder `A16` angefuehrt. Aus (96)
allein folgt kein numerischer Matrixeintrag `A16`.

## 5. Was (108) bedingt leisten kann

(108) verknuepft das Polynom in den Besetzungszahlen und den
Exponentialterm mit

```text
W(vx)*(1+f(N)),   W(vx)=g(k,q)*w(vx).
```

Das ist eine echte algebraische Auswahlbeziehung. Sind Besetzungen,
`f(N)`, `g`, die uebrigen Strukturbeitraege und eine unabhaengige linke
beziehungsweise rechte Zielgroesse fest, kann die Gleichung Kombinationen
der `A_im` einschraenken. Im Pseudosingulett kann der A16-Anteil dadurch in
einer entsprechend vollstaendig spezifizierten Sonderrechnung isolierbar
werden.

Die Buchseiten 330--335 geben jedoch weder ein unabhaengiges vollstaendiges
Datenset fuer eine solche Isolierung noch den Verlauf von `F16` an. Die
spaetere Nutzung empirischer Grundzustandsdaten ist deshalb als
Kalibrierung/heuristische Bestimmung zu beschreiben, nicht als bereits
vorher geschlossenes Randwertproblem. Umgekehrt darf aus diesem lokalen
Befund nicht gefolgert werden, jede Nutzung von (108) sei unbestimmt.

## 6. Staerkster interne Statusanker und naechste Quellenfrage

Die Einfuehrung, Druck 2--3 / PDF 13--14, benennt als „noch nicht geloestes
Problem“ gerade die Deduktion der metronischen `R3`-Strukturfunktionen,
deren endliche reelle Grenzwerte fuer `tau->0` die Elemente der
Koeffizientenmatrix (110d) ergeben. Der Satz beginnt am Ende von Druck 2
mit „Das noch nicht geloeste Problem besteht darin, aus einer
strukturellen“ und wird auf Druck 3 mit „Untersuchung ...“ fortgesetzt.
Erst durch diese Deduktion, so der Text, wuerden (109)--(111) ihren eher
heuristischen Charakter verlieren.

Dieser Autorhinweis bestaetigt den lokalen Befund staerker als eine
indirekte Suche nach einem vermeintlichen, nicht zitierten Operator. Ein
enger sinnvoller Folgeauftrag waere daher nicht eine erneute Suche nach
der bereits als offen bezeichneten expliziten `F16`-Form, sondern:

```text
Pruefen, ob (108) fuer einen quellenfest gewaehlten Pseudosingulett-
Grundzustand alle Groessen ausser A16 unabhaengig festlegt, oder ob die
verwendete Zielgroesse/Grundzustandsmasse selbst der empirische Input ist.
```

Das waere ein Bestimmtheitscheck der Auswahlgleichung, keine nachtraeglich
unterstellte Herleitung der metronischen Funktion.

## 7. Pruefumfang und Grenze

Vollstaendig visuell geprueft wurden fuer diesen Auftrag:

- H004 Druck 330--335 / PDF 336--341;
- (98)/(98a): Druck 267--269 / PDF 273--275;
- (101a)/(101b): Druck 289--291 / PDF 295--297;
- (105a): Druck 302--303 / PDF 308--309;
- (96)/(96a): Druck 245--246 / PDF 251--252;
- Einfuehrung Druck 2--3 / PDF 13--14.

Tragende Bildanker liegen unter `tmp/pdfs/a16_book/`,
`tmp/pdfs/f16_constraints/` und `tmp/pdfs/f16_backrefs/`. OCR wurde nur zur
Navigation benutzt. Die Aussage „kein bestimmender Operator gefunden“ ist
auf diese explizite Rueckverweiskette begrenzt; sie ist keine
werkweite Nichtexistenzbehauptung.
