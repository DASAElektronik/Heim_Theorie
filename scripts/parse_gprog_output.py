import csv
import re
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT = (
    PROJECT_ROOT
    / "01_sources"
    / "heim_primary_unpacked_untrusted"
    / "massformula"
    / "C 0.66"
    / "output_plus_neutrino.txt"
)
OUTPUT = PROJECT_ROOT / "05_analysis" / "gprog_066_output_plus_neutrino.csv"

LINE_RE = re.compile(
    r"^\s*(?P<name>[^=]+?)\s*=\s*(?P<desc>\S+)\s*=\s*ref=\s*"
    r"(?P<ref>-?\d+(?:\.\d+)?(?:e[+-]?\d+)?)\s+comp=\s*"
    r"(?P<comp>-?\d+(?:\.\d+)?(?:e[+-]?\d+)?)\s*=\s*diff\[%\]=\s*"
    r"(?P<diff>-?\d+(?:\.\d+)?(?:e[+-]?\d+)?)%"
)


def main() -> None:
    rows = []
    for line in INPUT.read_text(encoding="utf-8", errors="replace").splitlines():
        match = LINE_RE.match(line)
        if match:
            rows.append(
                {
                    "name": match.group("name").strip(),
                    "descriptor": match.group("desc"),
                    "reference_mass_mev": match.group("ref"),
                    "computed_mass_mev": match.group("comp"),
                    "diff_percent_reported": match.group("diff"),
                    "source": "massformula/C 0.66/output_plus_neutrino.txt",
                    "source_class": "secondary_implementation_output",
                }
            )

    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "name",
                "descriptor",
                "reference_mass_mev",
                "computed_mass_mev",
                "diff_percent_reported",
                "source",
                "source_class",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    main()

