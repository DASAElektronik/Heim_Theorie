# External source review: alpha versions and comparison value

Date of review and access: **2026-09-06**. This is a bounded source-discovery
review, not a numerical repair of the alpha formulas. Search-result snippets were
used only to locate documents; findings below are based on opened pages/PDFs or
explicitly labelled metadata/abstract mirrors.

## Executive findings

1. The document conventionally called the "1989 extended mass formula" is not
   an extant 1989 primary report. The accessible item identifies itself as a
   Forschungskreis/IGW reconstruction from 2002 (in a 2003 compilation), "nach
   einem Manuskript von Burkhard Heim." It says the 57-page report was sent to
   MBB/DASA in 1989, that the associated program could no longer be found, and
   that missing brackets in long equations were corrected by "best estimates."
   No alpha-specific erratum for B58-B62 and no independent alternate edition of
   those equations was located.
2. The experimental number in the IGW text is traceable to the PTB neutron
   experiment, whose authors were **Eckhard Krueger, Wolfgang Nistler, and
   Winfried Weirauch**, not only Nistler and Weirauch. The rounded central value
   `137.0360114` matches the 1999 re-evaluation, but the printed
   `+/- 3.4e-8` does **not** reproduce that paper's uncertainty as an absolute
   standard uncertainty and does not exactly reproduce its relative uncertainty.
3. The claimed "better formula, 1992" pair `137.0360085` / `1.000026627` was
   not found in a 1992 primary source. The located 1992 journal article prints
   instead `137.035976` / `1.0000266`. A 2003 IGW derivation prints
   `137.0359895` / `1.000026627`. Thus the exact claimed pair remains an
   unsupported later-version assertion and must not be merged into either the
   1982 or 1989 model.

## 1. B58-B62: provenance, re-host, and absence of an alpha erratum

### Verified

The currently served PDF is:

- *Die erweiterte Massenformel nach Burkhard Heim (1989). Nach einem Manuskript
  von Burkhard Heim*, Forschungskreis Heimsche Theorie, IGW Innsbruck 2002,
  embedded in *Einfuehrung in die Heimsche Massenformel*, copyright IGW 2003,
  printed pp. 10-20 (PDF pp. 1-11).
- Current URL:
  <https://heim-theory.com/wp-content/uploads/2026/03/F_Erweiterte_Massenformel_nach_Heim-1989.pdf>
- Editor/archive context:
  <https://heim-theory.com/massenformel-alter-arbeitskreis/> and
  <https://heim-theory.com/archiv/>

The introductory page states that a 57-page report with the new formulas and
results was sent to MBB/DASA in 1989. It also states that the corresponding
program was no longer findable and that some missing brackets in the long
manuscript equations had been supplied by best estimates during later
reprogramming. This is a general transmission warning; it does not name B58-B62
or issue an alpha-specific correction.

The current PDF still prints, on printed p. 18, the same B58-B62 chain and
numbers audited locally:

- B62: `alpha(+) = 0.0072973525253328589` and
  `alpha(-) = 0.999985890199089`;
- following reciprocal line: `137.03601` and `1.0000142`;
- experimental comparison attributed to "Nistler & Weirauch 2002":
  `137.0360114 +/- 3.4e-8`.

The former URL
<https://heim-theory.com/wp-content/uploads/2016/02/Erweiterte_Massenformel_Nach_Heim_1989.pdf>
returned "file does not exist" on 2026-09-06. The new URL returned 58,788 bytes,
SHA-256
`0E2F646D784152FB008944F58E1B8E709A416B65265D2FB75D3CC44C88FF8A40`.
That hash and size are identical to the project's previously acquired local copy
from the former URL. The 2026 URL is therefore a byte-identical re-host of the
audited PDF, not an alternate B58-B62 edition.

The site's present historical note distinguishes "Massenformel A" and
"Massenformel B" and expressly says that the dating of mathematical content is
not settled merely by the reported 1989 dispatch. That editorial caution is
consistent with treating this PDF as a later near-primary transmission, not an
unchanged 1989 publication.

### Not found / bounded negative result

No document explicitly labelled erratum, corrigendum, corrected B58-B62, or an
alternate numerical printing of B58-B62 was found in targeted searches of
`heim-theory.com` and `burkhardheim.de`. Searches covered the exact equation
labels, both B62 long decimals, both rounded reciprocals, the title variants,
and German terms `Errata`, `Korrektur`, `Auflage`, and `Klammern`. The editor
archive exposes the same re-hosted PDF. This negative result does not prove that
the reported 1989 MBB/DASA manuscript or private calculation sheets do not
exist; it means they were not publicly located in the searched author/editor
archives.

## 2. What "Nistler & Weirauch 2002" actually points toward

### Bibliographic chain

The IGW bibliography gives:

- Wolfgang Nistler and Winfried Weirauch, "Mit Neutronen zur
  Feinstrukturkonstanten," *Physik in unserer Zeit* **33** (2002), issue 1,
  pp. 10-15. Editor-hosted bibliography:
  <https://heim-theory.com/wp-content/uploads/2026/03/H_Literaturverzeichnis.pdf>

The journal is a Wiley-VCH publication (print ISSN 0031-9252, online ISSN
1521-3943): <https://onlinelibrary.wiley.com/journal/15213943>. A directly
readable copy or article record for the 2002 item was not located during this
bounded search, so its exact wording and uncertainty notation could not be
checked.

PTB's institutional history identifies all three experimenters as PTB
physicists and lists both the 1996 PTB report and the 2002 popular article:

- PTB, "Feinstrukturkonstante neutronisch gemessen," in *PTB-Mitteilungen*
  **123** (2013), issue 4, p. 33:
  <https://oar.ptb.de/files/download/681c516953218de84f08e5e8>.

The original/refined journal record behind the central value is:

- E. Krueger, W. Nistler, W. Weirauch, "Re-evaluation of a precise measurement
  of h/m_n," *Metrologia* **36** (1999), issue 2, pp. 147-148,
  DOI <https://doi.org/10.1088/0026-1394/36/2/9>.

Publisher-deposited Crossref metadata confirms the title, three authors,
journal, volume, issue, pages, and April 1999 publication date:
<https://api.crossref.org/works/10.1088%2F0026-1394%2F36%2F2%2F9>.
The normal browser interface reported an automated-access block, but the
publisher's own abstract endpoint was directly retrieved on 2026-09-06:
<https://iopscience.iop.org/article/10.1088/0026-1394/36/2/9/meta>.
Its HTML identifies IOP Publishing as publisher, all three authors' institution
as PTB, the online date `1999/04/01`, and gives the abstract results as

- `h/m_n = 3.956033285(287)e-7 m^2 s^-1`, relative standard uncertainty
  `7.26e-8`;
- `alpha^-1 = 137.03601144(498)`, relative standard uncertainty `3.64e-8`;
- uncertainties are one-standard-deviation estimates.

This is the immediate publisher-hosted source for the exact value and
uncertainty used in this review. A ResearchGate page reproduces the same
abstract, but it is an unconfirmed secondary abstract copy and is not relied on
as proof:
<https://www.researchgate.net/publication/231004274_Re-evaluation_of_a_precise_measurement_of_hmn>.
The quoted parenthetical uncertainty means an absolute standard uncertainty of
`0.00000498` (`4.98e-6`) on `alpha^-1`; its relative value is `3.64e-8`.

The earlier final-result paper was:

- E. Krueger, W. Nistler, W. Weirauch, "Determination of the fine-structure
  constant by a precise measurement of h/m_n: the final result,"
  *Metrologia* **35** (1998), issue 3, pp. 203-209,
  DOI <https://doi.org/10.1088/0026-1394/35/3/9>, reporting in its abstract
  `alpha^-1 = 137.03601062(503)` and relative uncertainty `3.67e-8`.

As an independent institutional check, the NIST-hosted CODATA 1998 adjustment
reviews the PTB experiment and cites the 1999 re-evaluation. Using its own
consistent constants/lattice-spacing treatment it obtains
`alpha^-1 = 137.0360119(51)` with relative standard uncertainty `3.7e-8` for
the PTB route (Eq. 284):
<https://physics.nist.gov/cuu/pdf/CODATA_RMP2000.pdf>.

### Consequence for the IGW comparison line

The IGW central number `137.0360114` is the 1999 re-evaluated central value
rounded from `137.03601144`. But `+/- 3.4e-8`, if read as an absolute
uncertainty as printed, is about 146 times smaller than the paper's absolute
standard uncertainty `4.98e-6`. If intended as a relative uncertainty, it still
does not equal the paper's `3.64e-8` (nor the 1998 result's `3.67e-8`). The
accessible evidence therefore does not support using the IGW `+/- 3.4e-8` as
the original experimental uncertainty. Whether that notation originated in the
unread 2002 popular article or in the IGW transcription was not resolved.

## 3. Claimed 1992 pair

### Located 1992 publication: different numbers

The identifiable 1992 publication is:

- T. Auerbach and Illobrand von Ludwiger, "Heim's Theory of Elementary
  Particle Structures," *Journal of Scientific Exploration* **6** (1992),
  no. 3, pp. 217-231. Editor/author-group hosted reproduction:
  <https://heim-theory.com/wp-content/uploads/2025/11/Heims-Theory-of-Elementary-Particle-Structures-Auerbach-und-Ludwiger.pdf>.
  The journal's current site identifies its archives as open access:
  <https://journalofscientificexploration.org/>.

On the PDF's section "The Fine Structure Constant" (PDF p. 9; original page
numbering is suppressed in this reproduction), the numerical lines are visibly
`alpha+ = 1/137.035976` and `alpha- = 1/1.0000266`. They do not contain either
`137.0360085` or the full `1.000026627`.

### Later related texts

The English IGW 2003 overview, currently at
<https://heim-theory.com/wp-content/uploads/2016/02/Heims_Mass_Formula_1982.pdf>,
contains the bracketed assertion: "A better formula, 1992, yields" the exact
pair `1/137.0360085` and `1/1.000026627`. It supplies no title, equation,
author, page, or archival identifier for that supposed 1992 formula. This is the
same unsupported claim registered as `EXT-ALPHA-1992-001`.

The separate IGW derivation by I. von Ludwiger and K. Gruener,
*Zur Herleitung der Heimschen Massenformel* (2003 compilation), Eq. (8.23),
prints `alpha(+)^-1 = 137.0359895` and
`alpha(-)^-1 = 1.000026627`, then says a still further corrected formula was
given by Heim in his 1989 mass formula but that its theoretical development had
not been supplied and still had to be found in his papers:
<https://heim-theory.com/wp-content/uploads/2026/03/D_Zur_Herleitung_Der_Heimschen_Massenformel.pdf>.
This locates the seven-digit negative number in a 2003 editor text, but not in a
1992 primary source, and it pairs it with a different positive value.

### Not found / bounded negative result

Exact-string searches for `137.0360085`, `137,0360085`, `1.000026627`, and
`1,000026627` were run across `heim-theory.com`, `burkhardheim.de`, the Journal
of Scientific Exploration site, and the broader web, combined with Heim,
Auerbach, von Ludwiger, alpha, and 1992. The exact positive value led back to
the IGW 2003 overview and later secondary repetitions. No underlying 1992 Heim
manuscript, equation page, calculation sheet, erratum, or other primary item was
located. The 1992 journal article found through author/editor and journal
records contradicts the exact-number attribution rather than substantiating it.

## Audit disposition

- Keep B58-B62 as the **IGW 2002/2003 transmission of a reported 1989
  manuscript**, not as a verified facsimile of the 1989 report.
- Preserve the internal B62/reciprocal discrepancies; no sourced erratum was
  found that authorizes changing any printed number.
- Replace any unqualified label "Nistler & Weirauch 2002 measurement" with a
  note that the underlying PTB experiment and 1999 re-evaluation were by
  **Krueger, Nistler, and Weirauch**. Treat the IGW uncertainty notation as
  unverified/mis-scaled, not as an experimental tolerance for the theory.
- Retain `EXT-ALPHA-1992-001` as `needs_primary_source`. Record that the located
  1992 article reports different rounded values and that the exact negative
  number is only located in a 2003 IGW derivation with a different positive
  partner. No speculative replacement is warranted.
