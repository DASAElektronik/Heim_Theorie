# Source Check Images

PDF pages exported with `pdftoppm -png -r 180` for manual verification of OCR formulas.

## Sets

- `1982_massenformel/`: pages from `Massenformel_nach_B_Heim_1982.pdf`
- `1989_erweiterte_massenformel/`: pages from `Erweiterte_Massenformel_Nach_Heim_1989.pdf`

## Usage

Use these PNGs to move formula-library entries from `raw_ocr` to `source_checked`.

Rules:

- Do not correct formulas from memory.
- Every correction must cite the image page and the text source line.
- If a symbol is unreadable, mark it `ambiguous` rather than guessing.
- If the PNG export has missing symbol fonts, check the original PDF as the final authority.

