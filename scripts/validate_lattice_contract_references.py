#!/usr/bin/env python3
"""Validate ContractForge Lattice platform asset contract-reference fixtures."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate(path: Path) -> None:
    doc = json.loads(path.read_text(encoding="utf-8"))
    require(doc.get("apiVersion") == "contractforge.socioprophet.dev/v1", "apiVersion mismatch")
    require(doc.get("kind") == "ContractReferencedAssetFixture", "kind mismatch")
    asset = doc.get("asset")
    require(isinstance(asset, dict), "asset must be an object")
    require(asset.get("sourceRecordKind") == "PlatformAssetRecord", "sourceRecordKind mismatch")
    require(isinstance(asset.get("assetId"), str) and asset["assetId"], "assetId is required")
    require(isinstance(asset.get("contractSubjectClass"), str) and asset["contractSubjectClass"], "contractSubjectClass is required")
    require(isinstance(asset.get("permittedUseSurfaces"), list), "permittedUseSurfaces must be a list")
    require(isinstance(doc.get("contractQuestions"), list) and doc["contractQuestions"], "contractQuestions must be non-empty")


def main(argv: list[str] | None = None) -> int:
    paths = [Path(arg) for arg in (argv if argv is not None else sys.argv[1:])]
    if not paths:
        paths = sorted(Path("examples/lattice").glob("*.json"))
    failed = False
    for path in paths:
        try:
            validate(path)
            print(f"PASS {path}")
        except Exception as exc:  # noqa: BLE001
            failed = True
            print(f"FAIL {path}: {exc}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
