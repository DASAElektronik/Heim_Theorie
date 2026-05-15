# OCR-1989-NEUTRINO Critic Review

verdict: `critic_ready`

## Accepted Source-Visible Transcription

Use readable subscript notation in canonical text (`M_ν`, `ν_i`, `α_+`, `φ_0`) while preserving the source glyphs. The source prints these compactly; do not normalize them to ASCII names.

```text
n = - Q_n,     m = - Q_m,     p = - Q_p     und     σ = - Q_σ        (B63)

G + F + S = φ                                                        (B64)

Setzt man gemäß (B3) für die Neutrinomasse ganz allgemein

M_ν = µα_+ (Φ + φ_0)                                                (B65)

wobei φ_0 die Beziehung (B49) auf die unteren Schranken von n, m, p, σ bezieht,
dann zeigt sich, dass M_ν nur von den Quantenzahlen k, κ, P und Q bestimmt wird.
```

For the positive-mass possibilities and state list, keep the source order:

```text
Für M_ν(kPQκ) > 0 ergeben sich die folgenden Möglichkeiten:

M_ν(1110) = M_ν(1111) und M_ν(1200) im mesonischen Bereich
und M_ν(2110) sowie M_ν(2111) im barionischen Bereich.

Außerdem gibt es noch ein Neutrino, welches nur den Drehimpuls Q = 1 überträgt und
vom β-Übergang gefordert wird. Für dieses Neutrino gibt es nur die zwei Möglichkeiten:

M_ν(2010) oder M_ν(1010).

Da im Fall (2010) M_ν < 0 werden würde, bleibt M_ν(1010) als Möglichkeit für das
β-Neutrino. Mit i = 1,...,5 lauten die möglichen Neutrino-Zustände ν_i:

für k = 1: ν_1(1010), ν_2(1110), ν_3(1200),
für k = 2: ν_4(2110), ν_5(2111).
```

Antistructure line:

```text
Für jedes ν_i existiert die spiegelsymmetrische Antistruktur \bar{ν}_i. Aus (B3)
lassen sich mit den möglichen von Null verschiedenen Quantenzahlen die Neutrinomassen
bestimmen.
```

Final interpretation paragraph through OCR line 554:

```text
Das empirische β-Neutrino kann durch ν_1 und das empirische µ-Neutrino durch ν_2
interpretiert werden. Es kann vorerst noch nicht entschieden werden, ob die übrigen
Neutrinos ebenfalls in der Natur realisiert sind oder ob es sich dabei nur um nicht
wirkliche logische Möglichkeiten handelt.
```

## Required Canonical Edits

- Change source line coverage from `491-552` to `491-554`.
- Replace the ASCII raw formula `M_nu = mu * alpha_plus * (Phi + phi0)` with `M_ν = µα_+ (Φ + φ_0)`.
- Record B63 as `n = - Q_n`, `m = - Q_m`, `p = - Q_p`, `σ = - Q_σ`.
- Record B64 as `G + F + S = φ`.
- Use Greek beta in `β-Übergang` and `β-Neutrino`; the OCR `ß` is incorrect.
- Add the exact state list and order: `ν_1(1010)`, `ν_2(1110)`, `ν_3(1200)`, `ν_4(2110)`, `ν_5(2111)`.
- Add the barred antistructure notation `\bar{ν}_i`.
- Keep Heim's final interpretation as historical/source interpretation, separate from any modern neutrino validation.

## Unresolved Normalization Risks

- `M_ν`/`ν_i` is the preferred readable canonical form; compact `Mν`/`νi` is source-like but easier to misread as unsubscripted text.
- `φ` versus `ϕ` may vary by font/OCR; use `φ` consistently here unless a wider catalog convention requires `ϕ`.
- `µ` versus Greek `μ` is a typography normalization issue; source-visible text uses `µ`.
- Juxtaposition in `µα_+` is source-visible multiplication; do not expand to `mu * alpha_plus` in source transcription.
- Barred `\bar{ν}_i` must not be flattened to plain `ν_i`.

## Implementation Red Flags

- Do not edit canonical formula, catalog, or queue files as part of this critic packet.
- Do not collapse the `β` glyph to German `ß`.
- Do not reorder states by later interpretation; preserve source order and grouping by `k = 1` and `k = 2`.
- Do not present the final paragraph as modern empirical validation of Heim neutrino masses.
