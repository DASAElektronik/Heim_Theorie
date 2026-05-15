# OCR-1982-SELECTION-ALGO Critic Review

## Verdict

critic_ready

## Findings

1. Source page 09 resolves the top-line disagreement in favor of Worker A for this specific glyph: the text reads `Q = Q(0) des x_v verwenden`, not `des x_{vx}`. This is visible in `07_outputs/source_check_images/1982_massenformel/page-09.png` and corresponds to OCR line 396.

2. Source page 09 supports source-local `vx` notation for the repeated family `W_{vx}`, `a_{vx}`, `b_{vx}`, `\Phi_{vx}`, terminal `x_{vx}`, and `M_N(vx)`. OCR renders the subscript family as Greek-nu-like in `07_outputs/extracted_text/Massenformel_nach_B_Heim_1982.txt:395`, `:398`, `:421`, `:428`, and `:429`, but the page image shows the same `vx` family already accepted in the related `HT-F-1982-SELECTION-N` review. This remains source transcription only, not project-wide normalization.

3. Source page 09 / OCR line 417 visibly reads `K < 0`, not `K_4 < 0`, in the sentence `Im Fall (c) ist lnW_4 > 0 und K < 0`. The following line 419 separately prints `K_4 < 0`. The accepted transcription should preserve this visible distinction and not silently normalize line 417 to `K_4 < 0`.

4. Source page 09 resolves the final noun in the Vermerk as `Strukturentitäten`, matching Worker B and OCR line 435. Worker A's `Struktureinheiten` is not accepted.

5. The task queue/source-check line range is incomplete. `TASK_QUEUE.csv` and `SOURCE_CHECK_QUEUE.csv` currently list `395-431`, but the same Vermerk continues through OCR line 435. The source scope should be `395-435`, excluding the next section heading `Grenzen der Resonanzspektren` at line 437 and formula `(XXXII)`.

## Accepted Transcription

Bei numerischer Bestimmung von `W_{vx}`, `a_{vx}`, `b_{vx}` und `\Phi_{vx}` (Quantenzahlenfunktion im Massenspektrum `M`) nicht `Q_N = Q(N)`, sondern `Q = Q(0)` des `x_v` verwenden. Zur Bestimmung der `n_j` wird das Anstiegsprinzip der Konfigurationszonenbesetzungen berücksichtigt. Zunächst für eine Resonanzordnung `N = 0` oder `N \ge 2` die rechte Seite `W_{vx}(1+f(N)) = W_1` numerisch bestimmen. Nach der Auswahlregel die maximale Kubikzahl `K_1^3` feststellen, deren Produkt mit `\alpha_1` noch in `W_1` enthalten ist. Dann `W_1 - \alpha_1K_1^3 = W_2 \ge 0` einsetzen in:

```math
(n_2 + Q_2)^2\alpha_2
+ (n_3 + Q_3)\alpha_3
+ \exp[(1-2k)(n_4+Q_4)/3Q_4]
= W_2
\qquad (XXX).
```

Jetzt maximale Quadratzahl `K_2^2` derart, dass `\alpha_2K_2^2` noch in `W_2` enthalten ist, also `W_2 - \alpha_2K_2^2 = W_3 \ge 0`. Ganz entsprechend in

```math
(n_3 + Q_3)\alpha_3
+ \exp[(1-2k)(n_4+Q_4)/3Q_4]
= W_3
\qquad (XXXI)
```

maximale Zahl `K_3` im Sinne `W_3 - \alpha_3K_3 = W_4 \ge 0` bestimmen.

Für `W_4` drei Möglichkeiten:

```text
(a): W_4 = 0,
(b): 0 < W_4 <= 1,
(c): W_4 > 1.
```

Allgemeiner Fall `(b)`: `lnW_4 <= 0` und `K_4(2k-1) = -3Q_4lnW_4`.

Im Fall `(c)` ist `lnW_4 > 0` und `K < 0`. Dies ist unmöglich, weil stets `n_j+Q_j >= 0` bleiben muß. Wegen `n_4+Q_4 <= (n_3+Q_3)\alpha_3` des Anstiegsprinzips wird dann `K_3` um 1 vermindert und `\alpha_3K_3` zu `K_4 < 0` addiert, so dass ein neuer Wert `K_4 >= 0` entsteht, was `K_3 > 0` voraussetzt; denn im Fall `K_3 = 0` kann diese Dilatation wegen des quadratischen Anstiegs von `j = 2` nicht erfolgen, so dass diese Resonanzordnung `N` für `x_{vx}` nicht existiert (verbotener Term).

Im Fall `(a)` hätte `W_4 -> 0` die Divergenz `K_4 -> infinity` zur Folge, doch ist dies wegen `K_4 <= \alpha_3K_3` unmöglich (zumal es divergierende Selbstpotenziale nicht gibt). Aus diesem Grunde wird im Fall `(a)` der maximale Wert `K_4 = \alpha_3K_3` berechnet. Aus den ermittelten `K_j` folgt `n_j = K_j - Q_j`.

Es ist zwar neben `n_j >= 0` auch `n_j < 0` möglich, doch gilt stets `K_j >= 0`, also `n_j >= -Q_j`. Die so ermittelte Quadrupel `n_j` wird mit `\Phi_{vx}` in das Massenspektrum eingesetzt, was numerisch `M_N(vx)` als Spektralterm des Massenspektrums zu `x_{vx}` liefert.

Vermerk: Die `K_j` sind stets ganzzahlig. Im Fall der Bestimmung von `K_4` treten jedoch regelmäßig Dezimalstellen auf. Im Fall der Dezimalstellen `,99...99` muß die Identität `,99...99 = 1` verwendet werden. Ist dagegen die Folge der Dezimalstellen von diesem Wert verschieden, dann darf nicht aufgerundet werden. Die Dezimalstellen sind abzuschneiden, weil die `K_j` die Anzahlen von Strukturentitäten sind.

## Blockers

None for source-image transcription. This approval does not normalize, derive, implement, or validate the algorithm.

## Required Canonical Changes

- Update `04_reconstruction/formula_library/agent_workspace/TASK_QUEUE.csv` for `OCR-1982-SELECTION-ALGO`: set `source_text_lines` from `395-431` to `395-435`; set `critic_status` to `critic_ready` after integration.
- Update `04_reconstruction/formula_library/SOURCE_CHECK_QUEUE.csv` for `HT-F-1982-SELECTION-ALGO`: set `source_lines` from `395-431` to `395-435`; set `status` to `checked` after canonical integration.
- Update `04_reconstruction/formula_library/formula_catalog.csv` with a `HT-F-1982-SELECTION-ALGO` entry, or otherwise split/append the algorithmic occupation tuple choice and `W_4` cases into the appropriate 1982 selection formula file.
- Add a canonical formula/transcription entry for this block using source image page 09 and OCR lines `395-435`, ending at the Vermerk. Do not include the next heading `Grenzen der Resonanzspektren` or formula `(XXXII)`.

## Risk Notes To Preserve

- `source_checked` here means visible-image transcription only. It is not normalization, derivation, implementation, or validation.
- Preserve the printed line 417 distinction `K < 0`; any later replacement with `K_4 < 0` must be marked as normalization or interpretation, not source transcription.
- Preserve the source-local `vx` glyph family and note that OCR often reads it as Greek-nu-like `νx`.
- Preserve `x_v` in `Q = Q(0) des x_v verwenden`; do not harmonize it to `x_{vx}` during source integration.
- Clean LaTeX can hide source ambiguity around `lnW_4` spacing and the `vx`/`νx` family. Keep visible-glyph notes with the canonical entry.
- The Vermerk decimal rule through OCR line 435 is part of this task's source block and should not be dropped.
