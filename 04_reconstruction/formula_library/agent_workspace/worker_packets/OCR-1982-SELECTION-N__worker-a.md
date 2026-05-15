# OCR-1982-SELECTION-N Worker a

## Scope

- Formula ID: HT-F-1982-SELECTION-N
- Image pages: 8
- OCR lines: 357-388

## Transcription

Source page 8, coefficient block:

```text
A_{51} = (2\alpha + 1)^2
A_{52} = 6\alpha/\eta^2
A_{53} = (\xi/\eta)^3
A_{54} = \alpha(\beta-\alpha)\sqrt{3/2}

A_{55} = \xi^2
A_{56} = (\xi/\eta)^4
A_{61} = \pi\xi(2\beta-\alpha)/12\beta
A_{62} = \pi^2(\beta-2\alpha)/12

A_{63} = (\sqrt{\eta})/9
A_{64} = \pi/3\eta
A_{65} = \pi/3\xi
A_{66} = \xi\eta
```

Text and formulas from the selection block:

```text
Die Resonanzordnung N \ge 0 (positiv ganzzahlig) wählt die zugelassenen Quadrupel n_j mit
1 \le j \le 4 aus. Mit der Kürzung

f(N) = [1 - Q(2 - k)(1 - \kappa)]\left[a_{\nu x}\frac{N}{N+2} + b_{\nu x}\sqrt{N(N-2)}\right] \tag{XXV}

folgt, dass die unbekannte Funktion F(\Gamma) = 0 für alle N \neq 1 bleibt (rechte Seite ist reell).
Im Fall N = 0 wird f = 0, so dass

(n_1 + Q_1)^3 \alpha_1 + (n_2 + Q_2)^2 \alpha_2 + (n_3 + Q_3)\alpha_3 + \exp[(1-2k)(n_4+Q_4)/3Q_4] = W_{\nu x} \tag{XXVI}

die n_j des Zustandes x_{\nu x} und damit die Masse M_0(\nu x) der Komponente x des Multipletts
x_{\nu} beschreibt. Die N \ge 2 ordnen x_{\nu x} ein Spektrum von Besetzungsparameterquadrupeln und
damit nach der Massenformel Resonanzmassen M_N(\nu x) zu (für jede Komponente x_{\nu x} also
ein Massenspektrum). Im Fall N = 1 kein Spektralterm. Hier ist nicht f(N) \ge 0, f(1) ist
komplex.

Realteil:      (n_1+Q_1)^3 \alpha_1 + (n_2+Q_2)^2 \alpha_2 + (n_3+Q_3) \alpha_3 + \exp[(1-2k)(n_4+Q_4)/3Q_4] =
                       W_{\nu x}\{1+[1-Q(2-k)(1-\kappa)]a_{\nu x}/3\}                              (XVII)

Imaginärteil: F(\Gamma) = W_{\nu x}[1-Q(2-k)(1-\kappa)]b_{\nu x}.                                         (XXVIII)

Die n_j und F(\Gamma) stehen mit N in irgendeiner Beziehung zu den vollen Bandbreiten \Gamma .
Auch muß es einen Zusammenhang Q_N = Q(N) zwischen doppelter Spinquantenzahl Q und
N geben. Wie könnten diese Zusammenhänge beschaffen sein?

Wird N = 1 ausgeschlossen, dann F = 0 , und reelle Beziehung:

(n_1 + Q_1)^3 \alpha_1 + (n_2 + Q_2)^2 \alpha_2 + (n_3 + Q_3) \alpha_3 + + \exp[(1-2k)(n_4+Q_4)/3Q_4] = W_{\nu x} (1+f)(XXIX)

diskutieren. Im allgemeinen f > 0 für N \ge 2 und f = 0 für N = 0. Im Falle des Multipletts
x_2 jedoch f = 0 für alle N \ge 0, weil hier allein Q(2-k)(1-\kappa) = 1 ist. Elektronen sind nach
diesem Bild nicht anregbar!
```

## Glyph Decisions

| Source position | Worker reading | Confidence | Reason |
|---|---|---:|---|
| p. 8, line 360 | `\sqrt{N(N-2)}` on the `b_{\nu x}` term | 0.98 | The radical is visible in the page image; OCR flattened it to plain `N(N-2)`. |
| p. 8, line 365 | `M_0(\nu x)` and `W_{\nu x}` | 0.97 | The subscripts are compact but visible in the source image. |
| p. 8, line 369 | `M_N(\nu x)` | 0.96 | The subscript on `M` is present in the image even though OCR dropped it. |
| p. 8, line 373-374 | `W_{\nu x}\{1+[1-Q(2-k)(1-\kappa)]a_{\nu x}/3\}` | 0.95 | The brace and division are clear in the scan; OCR spacing obscures them. |
| p. 8, line 376 | `W_{\nu x}[1-Q(2-k)(1-\kappa)]b_{\nu x}` | 0.95 | The source shows the full subscripts and bracketed factor. |
| p. 8, line 384 | `+ + \exp[...]` | 0.84 | The page visibly contains a doubled plus before `exp`; do not normalize it away. |
| p. 8, coefficient block | `A_{61} = \pi\xi(2\beta-\alpha)/12\beta` | 0.80 | The inline slash grouping is tight; preserve the source form rather than rewriting the denominator. |

## Ambiguities

- The `b_{\nu x}\sqrt{N(N-2)}` term is the main OCR correction on line 360; keep the radical explicit.
- The `+ + \exp[...]` in the XXIX line appears as a source-level doubled plus. It should be preserved in transcription, but it is not safe to canonicalize from OCR alone.
- The coefficient line `A_{61} = \pi\xi(2\beta-\alpha)/12\beta` is densely set, so the slash grouping is easy to over-read. Keep the source ordering and do not rewrite it into a normalized denominator form.
- Subscripts in `n_j`, `x_{\nu x}`, `M_0(\nu x)`, `M_N(\nu x)`, and `W_{\nu x}` are visually compact and should stay marked as source text rather than inferred notation.

## OCR Corrections

| OCR text | Image reading | Source page | Text line |
|---|---|---|---|
| `f(N) = [1 - Q(2 - k)(1 - κ)][aνx N/(N+2) + bνx     N ( N − 2) ]` | `f(N) = [1 - Q(2 - k)(1 - \kappa)]\left[a_{\nu x}\frac{N}{N+2} + b_{\nu x}\sqrt{N(N-2)}\right]` | 8 | 360 |
| `... = Wνx (XXVI)` | `... = W_{\nu x} \tag{XXVI}` | 8 | 365 |
| `M0(νx)` | `M_0(\nu x)` | 8 | 367 |
| `MN(νx)` | `M_N(\nu x)` | 8 | 369 |
| `Realteil: ... = Wνx{1+[1-Q(2-k)(1-κ)]aνx/3}` | `Realteil: ... = W_{\nu x}\{1+[1-Q(2-k)(1-\kappa)]a_{\nu x}/3\}` | 8 | 373-374 |
| `Imaginärteil: F(Γ) = Wνx[1-Q(2-k)(1-κ)]bνx.` | `Imaginärteil: F(\Gamma) = W_{\nu x}[1-Q(2-k)(1-\kappa)]b_{\nu x}.` | 8 | 376 |
| `(n1 + Q1)3α1 + (n2 + Q2)² α2 + (n3 + Q3) α3 + + exp[(1-2k)(n4+Q4)/3Q4] = Wνx (1+f)(XXIX)` | `(n_1 + Q_1)^3\alpha_1 + (n_2 + Q_2)^2\alpha_2 + (n_3 + Q_3)\alpha_3 + + \exp[(1-2k)(n_4+Q_4)/3Q_4] = W_{\nu x}(1+f)(XXIX)` | 8 | 384 |
| `A61 = πξ(2β - α)/12β` | `A_{61} = \pi\xi(2\beta-\alpha)/12\beta` | 8 | page 8 coefficient block |

## Do Not Integrate Yet

Do not promote this packet into canonical formula files yet. The selection block has one visible doubled-plus source typo and several densely packed subscript/slash groupings that should stay source-faithful until a second image-only pass confirms the intended line breaks and binding.
