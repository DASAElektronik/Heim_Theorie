# HT-F-1982-MU: 1982 Mass Element

## Formula

Source-checked transcription from page image:

```math
\mu =
\sqrt[4]{\pi}
\sqrt[3]{3 \pi \gamma \hbar s_0}
\sqrt{\frac{\hbar}{3 c \gamma}}
s_0^{-1},
\qquad s_0 = 1\ \mathrm{m}
```

## Source

- Provenance: `near_primary`
- File: `07_outputs/extracted_text/Massenformel_nach_B_Heim_1982.txt`
- Lines: 150-164
- Source image: `07_outputs/source_check_images/1982_massenformel/page-04.png`
- Original label: `(VI)`
- Source heading: `abgeleitete Naturkonstante (Massenelement)`

## Source Constants In Same Block

```text
hbar = h / 2 pi = 1.0545887e-34 J s
c = 2.99792458e8 m s^-1
gamma = 6.6732e-11 N m^2 kg^-2
epsilon0 = 8.8542e-12 A s V^-1 m^-1
mu0 = 1.2566e-6 A^-1 s V m^-1
R_ = (mu0 / epsilon0)^(1/2) = 376.73037659 V A^-1
```

## Dependencies

- `hbar`
- `c`
- `gamma`
- `pi`
- `s0`

## Outputs

- `mu`, the mass element. This is not the muon.

## Current Status

`source_checked`

## Audit Notes

- The OCR line is damaged, but the page image is readable enough for this transcription.
- Dimensional check: the expression reduces to mass units (`kg`) when `s0` has length units.
- Using the printed 1982/IGW constants gives approximately `mu = 2.259021874e-31 kg`, or `0.126721834 MeV/c^2` using a modern kg-to-MeV conversion. This derived value is for sanity checking only, not a source value.
- This is central because every 1982 mass scales with `mu * alpha_plus`.

## Risks

- The document is an IGW 2003 transcription/introduction of Heim's 1982 programming manuscript, not an independently verified facsimile of Heim's original notation.
- Historical constants differ from modern constants and from later C/Pascal/XLSM implementations.
- The printed formula uses the gravitational constant symbol `gamma`; do not confuse it with other `G`/`gamma` symbols in later code.
