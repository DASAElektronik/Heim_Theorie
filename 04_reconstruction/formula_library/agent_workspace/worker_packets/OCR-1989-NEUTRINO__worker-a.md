# OCR-1989-NEUTRINO Worker a

## Scope

- Formula ID: `HT-F-1989-NEUTRINO`
- Source images: `07_outputs/source_check_images/1989_erweiterte_massenformel/page-09.png`; `07_outputs/source_check_images/1989_erweiterte_massenformel/page-10.png`
- OCR source: `07_outputs/extracted_text/Erweiterte_Massenformel_Nach_Heim_1989.txt` lines 491-554
- Existing formula file checked: `04_reconstruction/formula_library/formulas/HT-F-1989-NEUTRINO.md`

## Verdict

ready

## Accepted Source-Visible Transcription

```text
4. Die Massen der Neutrinozustände:

Wird angenommen, dass im Zentralbereich einer Elementarstruktur eine euklidische Metrik
herrscht, dass also keinerlei Strukturelement vorhanden ist, dann bedeutet das: L(n) = - Qn.
Das heißt nach (B15), dass es auch keine ponderable Masse M0 gibt. Nach (B16) bis (B21)
hat dies zur folge, dass auch die übrigen Strukturzonen einer euklidischen Metrik genügen
müssen. In (B3) ist dann

n = - Qn,    m = - Qm,    p = - Qp    und    σ = - Qσ    (B63)
zu setzen, woraus folgt:
G + F + S = φ    (B64)

Nach (B49) bleibt trotz σ + Qσ = 0 i.a. φ ≠ 0, und auch Φ ≠ 0 wird von den unteren
Schranken der n, m, p, σ nicht berührt. Wenn Φ + φ ≠ 0, wegen P > 0 oder Q > 0, dann
liefert (B3) trotz (B63) eine von Null verschiedene Feldmasse. Diese ist nicht als ponderable
Korpuskel interpretierbar, sondern stellt nach Heim eine Art „Spinpotenz“ dar, die als ein
„Feldkatalyt“ Transmutationen von Elementarkorpuskeln ermöglicht oder bei ihren
Reaktions- und Zerfallsprozessen die Gültigkeit bestimmter Erhaltungsprinzipien
(Drehimpuls) erzwingt. Dieses Verhalten ist denjenigen Eigenschaften adäquat, welche aus
empirischen Gründen eine Neutrinodefinition erforderlich machten.

Setzt man gemäß (B3) für die Neutrinomasse ganz allgemein

Mν = µα+ (Φ + φ_0)    (B65)

wobei φ_0 die Beziehung (B49) auf die unteren Schranken von n, m, p, σ bezieht, dann zeigt
sich, dass Mν nur von den Quantenzahlen k, κ, P und Q bestimmt wird.

Für Mν(kPQκ) > 0 ergeben sich die folgenden Möglichkeiten:

Mν(1110) = Mν(1111) und Mν(1200) im mesonischen Bereich
und Mν(2110) sowie Mν(2111) im barionischen Bereich.

Außerdem gibt es noch ein Neutrino, welches nur den Drehimpuls Q = 1 überträgt und
vom β-Übergang gefordert wird. Für dieses Neutrino gibt es nur die zwei Möglichkeiten:

Mν(2010) oder Mν(1010).

Da im Fall (2010) Mν < 0 werden würde, bleibt Mν(1010) als Möglichkeit für das β-
Neutrino. Mit i = 1,...,5 lauten die möglichen Neutrino-Zustände νi:

für k = 1: ν1(1010), ν2(1110), ν3(1200),
für k = 2: ν4(2110), ν5(2111).

Für jedes νi existiert die spiegelsymmetrische Antistruktur \bar{ν}_i. Aus (B3) lassen sich mit
den möglichen von Null verschiedenen Quantenzahlen die Neutrinomassen bestimmen.

Die Rechenergebnisse sind in Tabelle II zusammengestellt. Die Massen sind in Elektronenvolt
angegeben.

Das empirische β-Neutrino kann durch ν1 und das empirische µ-Neutrino durch ν2
interpretiert werden. Es kann vorerst noch nicht entschieden werden, ob die übrigen Neutrinos
ebenfalls in der Natur realisiert sind oder ob es sich dabei nur um nicht wirkliche logische
Möglichkeiten handelt.
```

## OCR Corrections vs Current Formula File

- Extend the source range in the formula file from `491-552` to `491-554`.
- Replace the flattened raw OCR formula `M_nu = mu * alpha_plus * (Phi + phi0)` with the source-visible `Mν = µα+ (Φ + φ_0)`.
- Keep the state list explicitly as `ν1(1010), ν2(1110), ν3(1200), ν4(2110), ν5(2111)`; the current file only summarizes this loosely.
- Keep the antistructure as `\bar{ν}_i`; do not flatten it to plain `v_i` or omit the bar.
- Preserve the `β`-Neutrino wording in the interpretation paragraph; the current OCR-derived file should not keep `ß` here.
- Preserve `β-Übergang`, not a generalized or normalized alternative.
- Record the ordering exactly as written in source: `k = 1` yields `ν1` through `ν3`; `k = 2` yields `ν4` and `ν5`.

## Unresolved Glyph / Notation Risks

- `ν` vs Latin `v` in `Mν`, `νi`, and `\bar{ν}_i`.
- `φ_0` vs `φ0` for the lower-bound term in `(B65)`.
- `β` glyph vs OCR `ß` in the beta-transition / beta-neutrino lines.
- `µα+` may be read as juxtaposition, not an explicit multiplication chain; do not normalize it away without a separate canonical decision.
- The state tuple ordering is fixed in source, but the compact typography leaves room for OCR reordering if reprocessed mechanically.
- The interpretation paragraph is a historical Heim claim about an internal neutrino definition, not a modern neutrino-physics validation.

## Implementation Implications

- Treat this as a source-check correction packet only.
- Do not reinterpret the passage into modern neutrino mass language.
- Do not update canonical formula or queue files from this packet.
