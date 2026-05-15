# OCR-1982-SELECTION-N Worker b

## Scope

- Formula ID: HT-F-1982-SELECTION-N
- Image pages: 8
- OCR lines: 357-388

## Transcription

Die Resonanzordnung \(N \ge 0\) (positiv ganzzahlig) wählt die zugelassenen Quadrupel \(n_j\) mit
\(1 \le j \le 4\) aus. Mit der Kürzung

\[
f(N) = [1 - Q(2 - k)(1 - \kappa)]
\bigl[a_{vx}\, N/(N+2) + b_{vx}\, \sqrt{N(N-2)}\bigr]
\tag{XXV}
\]

folgt, dass die unbekannte Funktion \(F(\Gamma)=0\) für alle \(N \ne 1\) bleibt (rechte Seite ist reell).
Im Fall \(N = 0\) wird \(f = 0\), so dass

\[
(n_1 + Q_1)^3 \alpha_1 + (n_2 + Q_2)^2 \alpha_2 + (n_3 + Q_3)\alpha_3
+ \exp[(1-2k)(n_4+Q_4)/3Q_4] = W_{vx}\; (\mathrm{XXVI})
\]

die \(n_j\) des Zustandes \(x_{vx}\) und damit die Masse \(M_0(vx)\) der Komponente \(x\) des Multipletts
\(x_v\) beschreibt. Die \(N \ge 2\) ordnen \(x_{vx}\) ein Spektrum von Besetzungsparameterquadrupeln und
damit nach der Massenformel Resonanzmassen \(M_N(vx)\) zu (für jede Komponente \(x_{vx}\) also
ein Massenspektrum). Im Fall \(N = 1\) kein Spektralterm. Hier ist nicht \(f(N) \ge 0\), \(f(1)\) ist
komplex.

Realteil:

\[
(n_1+Q_1)^3 \alpha_1 + (n_2+Q_2)^2 \alpha_2 + (n_3+Q_3)\alpha_3 + \exp[(1-2k)(n_4+Q_4)/3Q_4]
= W_{vx}\{1+[1-Q(2-k)(1-\kappa)]a_{vx}/3\}
\tag{XVII}
\]

Imaginärteil:

\[
F(\Gamma) = W_{vx}[1-Q(2-k)(1-\kappa)]b_{vx}.
\tag{XXVIII}
\]

Die \(n_j\) und \(F(\Gamma)\) stehen mit \(N\) in irgendeiner Beziehung zu den vollen Bandbreiten \(\Gamma\).
Auch muß es einen Zusammenhang \(Q_N = Q(N)\) zwischen doppelter Spinquantenzahl \(Q\) und
\(N\) geben. Wie könnten diese Zusammenhänge beschaffen sein?

Wird \(N = 1\) ausgeschlossen, dann \(F = 0\), und reelle Beziehung:

\[
(n_1 + Q_1)^3 \alpha_1 + (n_2 + Q_2)^2 \alpha_2 + (n_3 + Q_3) \alpha_3 + + \exp[(1-2k)(n_4+Q_4)/3Q_4]
= W_{vx}(1+f) (\mathrm{XXIX})
\]

diskutieren. Im allgemeinen \(f > 0\) für \(N \ge 2\) und \(f = 0\) für \(N = 0\). Im Falle des Multipletts
\(x_2\) jedoch \(f = 0\) für alle \(N \ge 0\), weil hier allein \(Q(2-k)(1-\kappa)=1\) ist. Elektronen sind nach
diesem Bild nicht anregbar!

## Glyph Decisions

| Source position | Worker reading | Confidence | Reason |
|---|---|---:|---|
| p. 8, OCR line 360 | `b_{vx}\sqrt{N(N-2)}` | 0.98 | The radical bar visibly spans `N(N-2)` on the image. |
| p. 8, OCR line 365 | `W_{vx}` | 0.97 | The page-visible subscript is `vx`; OCR flattened it to `νx`. |
| p. 8, OCR line 373-374 | `W_{vx}` and `a_{vx}` | 0.97 | Both subscripts are visible in the real-part line. |
| p. 8, OCR line 376 | `W_{vx}` and `b_{vx}` | 0.97 | Both subscripts are visible in the imaginary-part line. |
| p. 8, OCR line 384 | `+ + \exp[...]` as printed | 0.74 | The page shows a doubled plus cluster before the exponential term; do not collapse it without a separate source check. |

## Ambiguities

- The `+ +` before `\exp[(1-2k)(n_4+Q_4)/3Q_4]` on the last displayed relation is visually present on the page, but it is not clear whether this is intentional typesetting or a line-wrap artifact.
- `F(Γ)=0` / `f(1) ist komplex.` are clear in the OCR span, but the surrounding prose is tightly set and should not be normalized.
- The `W_{vx}` notation is easy to flatten in OCR; keep the page-visible subscript form as the source reading.

## OCR Corrections

| OCR text | Image reading | Source page | Text line |
|---|---|---|---|
| `bνx     N ( N − 2) ]` | `b_{vx}\sqrt{N(N-2)}]` | 8 | 360 |
| `Wνx (XXVI)` | `W_{vx} (XXVI)` | 8 | 365 |
| `Wνx{1+[1-Q(2-k)(1-κ)]aνx/3}` | `W_{vx}\{1+[1-Q(2-k)(1-\kappa)]a_{vx}/3\}` | 8 | 373-374 |
| `Wνx[1-Q(2-k)(1-κ)]bνx.` | `W_{vx}[1-Q(2-k)(1-\kappa)]b_{vx}.` | 8 | 376 |
| `+ + exp[(1-2k)(n4+Q4)/3Q4]` | `+ + \exp[(1-2k)(n_4+Q_4)/3Q_4]` | 8 | 384 |

## Do Not Integrate Yet

Do not update canonical formula files from this packet alone. The last displayed relation has a visible doubled-plus cluster before the exponential term, so that line should stay under source-check review until a separate integration pass confirms the intended typesetting.
