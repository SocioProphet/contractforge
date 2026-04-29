#!/usr/bin/env python3
"""Validate ContractForge obligation examples against schema."""

from __future__ import annotations

from pathlib import Path
import json

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "obligation.schema.json"
EXAMPLE_DIR = ROOT / "examples" / "obligations"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    schema = load_json(SCHEMA)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    examples = sorted(EXAMPLE_DIR.glob("*.example.json"))
    if not examples:
        print(f"No obligation examples found under {EXAMPLE_DIR.relative_to(ROOT)}")
        return 1

    failures = []
    for example_path in examples:
        example = load_json(example_path)
        errors = sorted(validator.iter_errors(example), key=lambda error: list(error.path))
        if errors:
            for error in errors:
                location = ".".join(str(part) for part in error.path) or "<root>"
                failures.append(f"{example_path.relative_to(ROOT)} {location}: {error.message}")
        else:
            print(f"ok: {example_path.relative_to(ROOT)} validates against {SCHEMA.relative_to(ROOT)}")

        mapping = example.get("policyMapping", {})
        if not mapping.get("policyFamily") or not mapping.get("policyId"):
            failures.append(f"{example_path.relative_to(ROOT)}: missing policy mapping reference")

        if not example.get("evidenceRefs"):
            failures.append(f"{example_path.relative_to(ROOT)}: missing evidenceRefs")

    if failures:
        print("Obligation examples failed validation:")
        for failure in failures:
            print(f" - {failure}")
        return 1

    print("Obligation examples validate against schema.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
