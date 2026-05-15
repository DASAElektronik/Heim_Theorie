# OCR-1982-SELECTION-ALGO Worker b

## Scope

- Formula ID: HT-F-1982-SELECTION-ALGO
- Image pages: 09
- OCR lines: 395-435

## Transcription

Bei numerischer Bestimmung von W_{vx}, a_{vx}, b_{vx} und \Phi_{vx} (Quantenzahlenfunktion im
Massenspektrum M) nicht Q_N = Q(N), sondern Q = Q(0) des x_{vx} verwenden. Zur
Bestimmung der n_j wird das Anstiegsprinzip der Konfigurationszonenbesetzungen
berücksichtigt. Zunächst für eine Resonanzordnung N = 0 oder N \ge 2 die rechte Seite W_{vx}
(1+f(N)) = W_1 numerisch bestimmen. Nach der Auswahlregel die maximale Kubikzahl
K_1^3 feststellen, deren Produkt mit \alpha_1 noch in W_1 enthalten ist. Dann W_1 - \alpha_1K_1^3 = W_2 \ge 0
einsetzen in:

              (n_2 + Q_2)^2 \alpha_2 + (n_3 + Q_3) \alpha_3 + exp[(1-2k)(n_4+Q_4)/3Q_4] = W_2           (XXX).

Jetzt maximale Quadratzahl K_2^2 derart, dass \alpha_2K_2^2 noch in W_2 enthalten ist, also
W_2 - \alpha_2K_2^2 = W_3 \ge 0 . Ganz entsprechend in

              (n_3 + Q_3) \alpha_3 + exp[(1-2k)(n_4+Q_4)/3Q_4] = W_3                           (XXXI)

maximale Zahl K_3 im Sinne W_3 - \alpha_3K_3 = W_4 \ge 0 bestimmen.

Für W_4 drei Möglichkeiten:      (a): W_4 = 0 ,
                                (b): 0 < W_4 \le 1 ,
                                (c): W_4 > 1 .

Allgemeiner Fall (b): lnW_4 \le 0 und K_4(2k-1) = -3Q_4lnW_4 .
Im Fall (c) ist lnW_4 > 0 und K < 0 . Dies ist unmöglich, weil stets n_j+Q_j \ge 0 bleiben muß.
Wegen n_4+Q_4 \le (n_3+Q_3)\alpha_3 des Anstiegsprinzips wird dann K_3 um 1 vermindert und \alpha_3K_3
zu K_4 < 0 addiert, so dass ein neuer Wert K_4 \ge 0 entsteht, was K_3 > 0 voraussetzt; denn im
Fall K_3 = 0 kann diese Dilatation wegen des quadratischen Anstiegs von j = 2 nicht erfolgen,
so dass diese Resonanzordnung N für x_{vx} nicht existiert (verbotener Term).

Im Fall (a) hätte W_4 \to 0 die Divergenz K_4 \to \infty zur Folge, doch ist dies wegen K_4 \le \alpha_3K_3
unmöglich (zumal es divergierende Selbstpotenziale nicht gibt). Aus diesem Grunde wird
im Fall (a) der maximale Wert K_4 = \alpha_3K_3 berechnet. Aus den ermittelten K_j folgt n_j = K_j -
Q_j .
Es ist zwar neben n_j \ge 0 auch n_j < 0 möglich, doch gilt stets K_j \ge 0 , also n_j \ge -Q_j .
Die so ermittelte Quadrupel n_j wird mit \Phi_{vx} in das Massenspektrum eingesetzt, was
numerisch M_N(vx) als Spektralterm des Massenspektrums zu x_{vx} liefert.

Vermerk: Die K_j sind stets ganzzahlig. Im Fall der Bestimmung von K_4 treten jedoch
regelmäßig Dezimalstellen auf. Im Fall der Dezimalstellen ,99... 99 muß die Identität
,99... 99 = 1 verwendet werden. Ist dagegen die Folge der Dezimalstellen von diesem Wert
verschieden, dann darf nicht aufgerundet werden. Die Dezimalstellen sind abzuschneiden,
weil die K_j die Anzahlen von Strukturentitäten sind

## Glyph Decisions

| Source position | Worker reading | Confidence | Reason |
|---|---|---:|---|
| 395-396 | `W_{vx}, a_{vx}, b_{vx}, \Phi_{vx}` | medium | OCR has `ν`; image reads as `vx` in the subscripts. |
| 395-396 | `x_{vx}` | medium | The `x` glyph after `Q(0)` is small and slightly blurred. |
| 399-400 | `W_1`, `K_1^3`, `\alpha_1` | high | Superscript/subscript stack is visible in the page image. |
| 403 | `K_2^2` | high | OCR collapsed the exponent; image shows a quadratic term. |
| 405-410 | `W_2`, `W_3`, `K_3`, `K_4` | high | The stepwise occupation choices are clearly numbered on the page. |
| 416-421 | `K_4(2k-1) = -3Q_4\ln W_4` and `K < 0` | medium | The `K` subscript is not perfectly crisp in the image at line 417. |
| 421, 429 | `x_{vx}` and `M_N(vx)` | medium | The repeated `vx/νx` glyph is close enough to remain ambiguous. |
| 432-435 | decimal-place rule with `,99... 99 = 1` | high | The Vermerk is legible and the section boundary is clear. |

## Ambiguities

- The recurring `vx` versus `νx` glyph in `W`, `a`, `b`, `\Phi`, `x`, and `M_N` is not fully stable in the scan.
- The `K < 0` reading in the `W_4` case (line 417) may hide a subscript, but the scan does not make that fully certain.
- The `x` glyph in `des x_{vx}` and the terminal `x_{vx}` in `M_N(vx)` are close to the OCR's `ν` reading.

## OCR Corrections

| OCR text | Image reading | Source page | Text line |
|---|---|---|---|
| `Wνx , aνx , bνx und Φνx` | `W_{vx}, a_{vx}, b_{vx} und \Phi_{vx}` | 09 | 395-396 |
| `Wνx` | `W_{vx}` | 09 | 398-400 |
| `K13` | `K_1^3` | 09 | 399-400 |
| `W1 - α1K13 = W2 ≥ 0` | `W_1 - \alpha_1K_1^3 = W_2 \ge 0` | 09 | 400 |
| `(n2 + Q2)² α2 + (n3 + Q3) α3 + exp[(1-2k)(n4+Q4)/3Q4] = W2` | `(n_2 + Q_2)^2 \alpha_2 + (n_3 + Q_3) \alpha_3 + exp[(1-2k)(n_4+Q_4)/3Q_4] = W_2` | 09 | 403 |
| `K22` | `K_2^2` | 09 | 405-406 |
| `(n3 + Q3) α3 + exp[(1-2k)(n4+Q4)/3Q4] = W3` | `(n_3 + Q_3) \alpha_3 + exp[(1-2k)(n_4+Q_4)/3Q_4] = W_3` | 09 | 408 |
| `W3 - α3K3 = W4 ≥ 0` | `W_3 - \alpha_3K_3 = W_4 \ge 0` | 09 | 410 |
| `lnW4 ≤ 0 und K4(2k-1) = -3Q4lnW4` | `\ln W_4 \le 0 und K_4(2k-1) = -3Q_4\ln W_4` | 09 | 416 |
| `K < 0` | `K_4 < 0` or `K < 0` (scan ambiguous) | 09 | 417 |
| `so dass diese Resonanzordnung N für xνx nicht existiert` | `so dass diese Resonanzordnung N für x_{vx} nicht existiert` | 09 | 421 |
| `Aus den ermittelten Kj folgt nj = Kj - Qj` | `Aus den ermittelten K_j folgt n_j = K_j - Q_j` | 09 | 425-426 |
| `Die so ermittelte Quadrupel nj wird mit Φνx ... zu xνx liefert` | `Die so ermittelte Quadrupel n_j wird mit \Phi_{vx} ... zu x_{vx} liefert` | 09 | 428-429 |
| `,99... 99 muß die Identität ,99... 99 = 1 verwendet werden` | same, with the comma-leading decimal block preserved | 09 | 432-433 |

## Do Not Integrate Yet

Do not update any canonical formula or queue files from this packet alone. The only remaining blocker is the `vx/νx` glyph family and the `K_4` vs `K` subscript visibility in the W4 case; those should stay marked as ambiguous until critic review.
