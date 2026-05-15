# OCR-1982-SELECTION-ALGO Worker A

## Scope

- Formula ID: HT-F-1982-SELECTION-ALGO
- Image pages: 09
- OCR lines: 395-431

## Transcription

Bei numerischer Bestimmung von `W_{vx}`, `a_{vx}`, `b_{vx}` und `\Phi_{vx}` (Quantenzahlenfunktion im
Massenspektrum M) nicht `Q_N = Q(N)`, sondern `Q = Q(0)` des `x_v` verwenden. Zur
Bestimmung der `n_j` wird das Anstiegsprinzip der Konfigurationszonenbesetzungen
berücksichtigt. Zunächst für eine Resonanzordnung `N = 0` oder `N \ge 2` die rechte Seite `W_{vx}`
`(1+f(N)) = W_1` numerisch bestimmen. Nach der Auswahlregel die maximale Kubikzahl
`K_1^3` feststellen, deren Produkt mit `\alpha_1` noch in `W_1` enthalten ist. Dann `W_1 - \alpha_1 K_1^3 = W_2 \ge 0`
einsetzen in:

`(n_2 + Q_2)^2 \alpha_2 + (n_3 + Q_3)\alpha_3 + \exp[(1-2k)(n_4+Q_4)/3Q_4] = W_2           (XXX).`

Jetzt maximale Quadratzahl `K_2^2` derart, dass `\alpha_2 K_2^2` noch in `W_2` enthalten ist, also
`W_2 - \alpha_2 K_2^2 = W_3 \ge 0`. Ganz entsprechend in

`(n_3 + Q_3)\alpha_3 + \exp[(1-2k)(n_4+Q_4)/3Q_4] = W_3                           (XXXI)`

maximale Zahl `K_3` im Sinne `W_3 - \alpha_3 K_3 = W_4 \ge 0` bestimmen.

Für `W_4` drei Möglichkeiten:      `(a): W_4 = 0`,
                                  `(b): 0 < W_4 \le 1`,
                                  `(c): W_4 > 1`.

Allgemeiner Fall `(b): \ln W_4 \le 0` und `K_4(2k-1) = -3Q_4 \ln W_4`.
Im Fall `(c)` ist `\ln W_4 > 0` und `K < 0`. Dies ist unmöglich, weil stets `n_j+Q_j \ge 0` bleiben muß.
Wegen `n_4+Q_4 \le (n_3+Q_3)\alpha_3` des Anstiegsprinzips wird dann `K_3` um 1 vermindert und `\alpha_3 K_3`
zu `K_4 < 0` addiert, so dass ein neuer Wert `K_4 \ge 0` entsteht, was `K_3 > 0` voraussetzt; denn im
Fall `K_3 = 0` kann diese Dilatation wegen des quadratischen Anstiegs von `j = 2` nicht erfolgen,
so dass diese Resonanzordnung `N` für `x_{vx}` nicht existiert (verbotener Term).

Im Fall `(a)` hätte `W_4 \to 0` die Divergenz `K_4 \to \infty` zur Folge, doch ist dies wegen `K_4 \le \alpha_3 K_3`
unmöglich (zumal es divergierende Selbstpotenziale nicht gibt). Aus diesem Grunde wird
im Fall `(a)` der maximale Wert `K_4 = \alpha_3 K_3` berechnet. Aus den ermittelten `K_j` folgt `n_j = K_j -
Q_j`.
Es ist zwar neben `n_j \ge 0` auch `n_j < 0` möglich, doch gilt stets `K_j \ge 0`, also `n_j \ge -Q_j`.
Die so ermittelte Quadrupel `n_j` wird mit `\Phi_{vx}` in das Massenspektrum eingesetzt, was
numerisch `M_N(vx)` als Spektralterm des Massenspektrums zu `x_{vx}` liefert.

Vermerk: Die `K_j` sind stets ganzzahlig. Im Fall der Bestimmung von `K_4` treten jedoch
regelmäßig Dezimalstellen auf. Im Fall der Dezimalstellen `,99...99` muß die Identität
`,99...99 = 1` verwendet werden. Ist dagegen die Folge der Dezimalstellen von diesem Wert
verschieden, dann darf nicht aufgerundet werden. Die Dezimalstellen sind abzuschneiden,
weil die `K_j` die Anzahlen von Struktureinheiten sind.

## Glyph Decisions

| Source position | Worker reading | Confidence | Reason |
|---|---|---:|---|
| p.09, lines 395-398 and 421, 429 | `vx` subscript on `W`, `a`, `b`, `\Phi`, and `x` | 0.63 | The page image reads as `vx`; OCR collapses this to `\nu x`. I kept the source-image shape and flagged the letter as visually confusable. |
| p.09, lines 400 and 405-410 | `K_1^3`, `K_2^2`, `K_3`, `K_4` | 0.98 | OCR flattens these to `K13`, `K22`, and `K3`; the image shows explicit subscript/exponent structure. |
| p.09, line 416 | `\ln W_4` | 0.96 | Image clearly shows the logarithm with a space before `W_4`; OCR joins it as `lnW4`. |
| p.09, lines 428-431 | `K_j`, `n_j`, `\Phi_{vx}` | 0.95 | The index `j` is visible in the page image and is required by the surrounding notation. |

## Ambiguities

- The subscript glyph in `W_{vx}`, `a_{vx}`, `b_{vx}`, `\Phi_{vx}`, and `x_{vx}` is visually close to Greek `\nu`; I did not normalize it.
- The final noun in the Vermerk is slightly soft in the source image; I read it as `Struktureinheiten`.
- The supplied OCR range stops at line 431, while the page image continues the Vermerk paragraph; the continuation here is source-image transcription only.

## OCR Corrections

| OCR text | Image reading | Source page | Text line |
|---|---|---|---|
| `Wνx , aνx , bνx und Φνx` | `W_{vx}, a_{vx}, b_{vx} und \Phi_{vx}` | 09 | 395 |
| `nicht QN = Q(N) , sondern Q = Q(0) des xν verwenden.` | `nicht Q_N = Q(N), sondern Q = Q(0) des x_v verwenden.` | 09 | 396 |
| `Wνx` / `K13` / `W1 - α1K13 = W2 ≥ 0` | `W_{vx}` / `K_1^3` / `W_1 - \alpha_1 K_1^3 = W_2 \ge 0` | 09 | 398-400 |
| `(n2 + Q2)² α2 + (n3 + Q3) α3 + exp[(1-2k)(n4+Q4)/3Q4] = W2` | `(n_2 + Q_2)^2 \alpha_2 + (n_3 + Q_3)\alpha_3 + \exp[(1-2k)(n_4+Q_4)/3Q_4] = W_2` | 09 | 403 |
| `K2²` / `W2 - α2K2² = W3 ≥ 0` | `K_2^2` / `W_2 - \alpha_2 K_2^2 = W_3 \ge 0` | 09 | 405-406 |
| `(n3 + Q3) α3 + exp[(1-2k)(n4+Q4)/3Q4] = W3` | `(n_3 + Q_3)\alpha_3 + \exp[(1-2k)(n_4+Q_4)/3Q_4] = W_3` | 09 | 408 |
| `K3` / `W4` / `lnW4` / `K4(2k-1) = -3Q4lnW4` | `K_3` / `W_4` / `\ln W_4` / `K_4(2k-1) = -3Q_4 \ln W_4` | 09 | 410-416 |
| `xνx` | `x_{vx}` | 09 | 421, 429 |
| `K4 = α3K3 ... nj = Kj - Qj` | `K_4 = \alpha_3 K_3 ... n_j = K_j - Q_j` | 09 | 423-426 |
| `Quadrupel nj ... Φνx ... M_N(vx) ... xνx` | `Quadrupel n_j ... \Phi_{vx} ... M_N(vx) ... x_{vx}` | 09 | 428-429 |
| `Vermerk: Die Kj sind stets ganzzahlig. Im Fall der Bestimmung von K4 treten jedoch` | `Vermerk: Die K_j sind stets ganzzahlig. Im Fall der Bestimmung von K_4 treten jedoch` | 09 | 431 |

## Do Not Integrate Yet

Hold this as a source-image packet only. The page image continues the Vermerk paragraph beyond the supplied OCR span, and the `vx`/`\nu x` glyph family should stay marked ambiguous until the canonical transcription pass.
