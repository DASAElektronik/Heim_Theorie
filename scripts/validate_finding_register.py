"""Check finding-register metadata only; never execute evidence or assess truth."""

import argparse
from datetime import date
import json
from pathlib import Path, PurePosixPath
import re


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = Path("04_reconstruction/alpha_audit/FINDING_REGISTER.json")
SOURCE_REGISTER_PATH = Path("01_sources/source_register.md")
TOP_FIELDS = frozenset({"schema_version", "updated", "scope", "findings"})
FINDING_FIELDS = frozenset({
    "finding_id", "kind", "claim", "source_ids", "source_locator",
    "assumptions", "scope", "not_established", "evidence_paths",
    "reproduction", "next_check",
})
LIST_FIELDS = frozenset({"source_ids", "evidence_paths"})
KINDS = frozenset({
    "local_contradiction", "conditional_conflict", "source_output_mismatch",
    "open_justification", "version_difference", "source_definition",
    "conditional_bridge", "own_diagnostic", "positive_reproduction",
})


def _nonempty_string(value):
    return isinstance(value, str) and bool(value.strip())


def _keys_error(value, expected, label):
    missing = expected - value.keys()
    extra = value.keys() - expected
    if missing or extra:
        return (f"{label}: fields differ from schema "
                f"(missing={sorted(missing)!r}, extra={sorted(map(str, extra))!r})")
    return None


def read_source_ids(path):
    """Read IDs solely from the first column of source-register table rows."""
    content = Path(path).read_text(encoding="utf-8")
    ids = set(re.findall(r"^\|\s*([A-Z]+[0-9]{3})\s*\|", content, re.MULTILINE))
    if not ids:
        raise ValueError("source register contains no recognized table IDs")
    return ids


def _evidence_error(raw, root):
    # Lexical checks precede normalization: even an internal a/../b is refused.
    if ("\\" in raw or ":" in raw or "\x00" in raw
            or PurePosixPath(raw).is_absolute()
            or ".." in PurePosixPath(raw).parts):
        return "must be a relative path without '..', backslash, colon or NUL"
    try:
        target = (root / raw).resolve()
        if not target.is_relative_to(root):
            return "resolved path leaves the repository root"
        if not target.is_file():
            return "must resolve to an existing file"
    except (OSError, RuntimeError, ValueError) as exc:
        return f"cannot safely resolve file: {exc}"
    return None


def validate_register(document, *, root, source_ids):
    """Return metadata errors; existing evidence does not establish its claims."""
    errors = []
    root = Path(root).resolve()
    if not isinstance(document, dict):
        return ["register: expected an object"]
    key_error = _keys_error(document, TOP_FIELDS, "register")
    if key_error:
        errors.append(key_error)
    if type(document.get("schema_version")) is not int or document["schema_version"] != 1:
        errors.append("schema_version: expected integer 1 (not boolean)")
    updated = document.get("updated")
    try:
        if not isinstance(updated, str) or not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", updated):
            raise ValueError
        date.fromisoformat(updated)
    except ValueError:
        errors.append("updated: expected a valid ISO date YYYY-MM-DD")
    if not _nonempty_string(document.get("scope")):
        errors.append("scope: expected a nonempty string")
    findings = document.get("findings")
    if not isinstance(findings, list) or not findings:
        errors.append("findings: expected a nonempty list")
        return errors

    seen = set()
    for index, row in enumerate(findings):
        label = f"findings[{index}]"
        if not isinstance(row, dict):
            errors.append(f"{label}: expected an object")
            continue
        key_error = _keys_error(row, FINDING_FIELDS, label)
        if key_error:
            errors.append(key_error)
        for field in sorted(FINDING_FIELDS - LIST_FIELDS):
            if not _nonempty_string(row.get(field)):
                errors.append(f"{label}.{field}: expected a nonempty string")

        finding_id = row.get("finding_id")
        if not isinstance(finding_id, str) or not re.fullmatch(r"FIND-(?!000)[0-9]{3}", finding_id):
            errors.append(f"{label}.finding_id: expected FIND-001 through FIND-999")
        elif finding_id in seen:
            errors.append(f"{label}.finding_id: duplicate {finding_id}")
        else:
            seen.add(finding_id)
        if not isinstance(row.get("kind"), str) or row["kind"] not in KINDS:
            errors.append(f"{label}.kind: unknown finding kind")

        for field in sorted(LIST_FIELDS):
            values = row.get(field)
            if not isinstance(values, list) or not values:
                errors.append(f"{label}.{field}: expected a nonempty list")
                continue
            for position, value in enumerate(values):
                item_label = f"{label}.{field}[{position}]"
                if not _nonempty_string(value):
                    errors.append(f"{item_label}: expected a nonempty string")
                elif field == "source_ids":
                    if value not in source_ids:
                        errors.append(f"{item_label}: unknown source ID {value!r}")
                else:
                    problem = _evidence_error(value, root)
                    if problem:
                        errors.append(f"{item_label}: {problem}: {value!r}")
    return errors


def _unique_object(pairs):
    """Reject duplicate JSON keys instead of silently accepting the last one."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def validate_file(root=ROOT):
    """Read only the fixed register and source-register paths below root."""
    root = Path(root)
    try:
        document = json.loads((root / REGISTER_PATH).read_text(encoding="utf-8"),
                              object_pairs_hook=_unique_object)
        source_ids = read_source_ids(root / SOURCE_REGISTER_PATH)
    except (OSError, ValueError) as exc:
        return [f"register input: {exc}"]
    return validate_register(document, root=root, source_ids=source_ids)


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Prueft nur Metadatenintegritaet des festen Befundregisters; "
                    "keine Wahrheitspruefung oder Ausfuehrung von Evidenzpfaden.")
    parser.parse_args(argv)
    errors = validate_file()
    if errors:
        print("FEHLER: Metadatenintegritaet nicht bestaetigt (keine Wahrheitspruefung).")
        for error in errors:
            print(f"- {error}")
        return 1
    print("OK: Metadatenintegritaet bestaetigt; keine Wahrheitspruefung der Befunde.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
