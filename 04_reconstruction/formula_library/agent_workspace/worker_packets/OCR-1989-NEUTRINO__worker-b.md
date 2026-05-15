# HT-F-1989-NEUTRINO OCR Check Packet

verdict: ready

image pages used:
- `07_outputs/source_check_images/1989_erweiterte_massenformel/page-09.png`
- `07_outputs/source_check_images/1989_erweiterte_massenformel/page-10.png`

accepted source-visible transcription for context:
```text
4. Die Massen der Neutrinozustände:

Wird angenommen, dass im Zentralbereich einer Elementarstruktur eine euklidische Metrik
herrscht, dass also keinerlei Strukturelement vorhanden ist, dann bedeutet das: L(n) = - Q_n.
Das heißt nach (B15), dass es auch keine ponderable Masse M_0 gibt. Nach (B16) bis (B21)
hat dies zur folge, dass auch die übrigen Strukturzonen einer euklidischen Metrik genügen
müssen. In (B3) ist dann

n = - Q_n, m = - Q_m, p = - Q_p und σ = - Q_σ (B63)
zu setzen, woraus folgt:
G + F + S = ϕ (B64)

Nach (B49) bleibt trotz σ + Q_σ = 0 i.a. ϕ ≠ 0, und auch Φ ≠ 0 wird von den unteren
Schranken der n, m, p, σ nicht berührt. Wenn Φ + ϕ ≠ 0, wegen P > 0 oder Q > 0, dann
liefert (B3) trotz (B63) eine von Null verschiedene Feldmasse. Diese ist nicht als ponderable
Korpuskel interpretierbar, sondern stellt nach Heim eine Art „Spinpotenz“ dar, die als ein
„Feldkatalyt“ Transmutationen von Elementarkorpuskeln ermöglicht oder bei ihren
Reaktions- und Zerfallsprozessen die Gültigkeit bestimmter Erhaltungsprinzipien
(Drehimpuls) erzwingt. Dieses Verhalten ist denjenigen Eigenschaften adäquat, welche aus
empirischen Gründen eine Neutrinodefinition erforderlich machten.

Setzt man gemäß (B3) für die Neutrinomasse ganz allgemein

M_ν = µα_+ (Φ + φ_0) (B65)

wobei φ_0 die Beziehung (B49) auf die unteren Schranken von n, m, p, σ bezieht, dann zeigt
sich, dass M_ν nur von den Quantenzahlen k, κ, P und Q bestimmt wird.

Für M_ν(kPQκ) > 0 ergeben sich die folgenden Möglichkeiten:

M_ν (1110) = M_ν (1111) und M_ν (1200) im mesonischen Bereich
und M_ν (2110) sowie M_ν (2111) im barionischen Bereich.

Außerdem gibt es noch ein Neutrino, welches nur den Drehimpuls Q = 1 überträgt und
vom β-Übergang gefordert wird. Für dieses Neutrino gibt es nur die zwei Möglichkeiten:

M_ν (2010) oder M_ν (1010).

Da im Fall (2010) M_ν < 0 werden würde, bleibt M_ν (1010) als Möglichkeit für das β-
Neutrino. Mit i = 1,...,5 lauten die möglichen Neutrino-Zustände ν_i:

für k = 1: ν_1(1010), ν_2(1110), ν_3(1200),
für k = 2: ν_4(2110), ν_5(2111).

Für jedes ν_i existiert die spiegelsymmetrische Antistruktur \bar{ν}_i. Aus (B3) lassen sich mit
den möglichen von Null verschiedenen Quantenzahlen die Neutrinomassen bestimmen.

Die Rechenergebnisse sind in Tabelle II zusammengestellt. Die Massen sind in Elektronenvolt
angegeben.

Das empirische β-Neutrino kann durch ν_1 und das empirische µ-Neutrino durch ν_2
interpretiert werden. Es kann vorerst noch nicht entschieden werden, ob die übrigen Neutrinos
ebenfalls in der Natur realisiert sind oder ob es sich dabei nur um nicht wirkliche logische
Möglichkeiten handelt.
```

OCR corrections vs current formula file:
- `M_nu` should be `M_ν`.
- `mu * alpha_plus` should be the source glyph sequence `µα_+` / `μ α_+`, not ASCII-expanded text.
- `Phi + phi0` should be `Φ + φ_0`.
- `phi` in B64 should stay as the source lower-case phi glyph, not be rewritten to plain text.
- `νi`, `ν1`..`ν5` should be `ν_i`, `ν_1`..`ν_5`.
- `β-Neutrino` and `β-Übergang` are Greek beta in the source, not `ß`.
- `Antistruktur νi` should be `Antistruktur \bar{ν}_i`.
- source coverage must extend from `491-552` to `491-554` because the final interpretation sentence continues through line 554.

unresolved glyph / notation risks:
- `ν` vs `v` in `M_ν`, `ν_i`, and the antistruktur notation.
- `φ_0` vs `ϕ_0` in the B65 factor and the related B64/B49 prose.
- `β` glyph versus OCR confusion with `ß`.
- state tuple ordering must remain `1010`, `1110`, `1200`, `2110`, `2111`; do not reorder by interpretation.
- the final paragraph is Heim's empirical identification, not a modern neutrino-physics validation.

implementation implications:
- Keep this as a source-fidelity packet only.
- Do not normalize away the source glyph choices in downstream reconstruction until the canonical formula entry is updated separately.
