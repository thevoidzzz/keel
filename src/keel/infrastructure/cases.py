"""The versioned case file for this release."""

import json
from pathlib import Path

from keel.domain.case import Case, require_cases
from keel.domain.catalog import require_catalog
from keel.infrastructure.manuals import chunks_for
from keel.infrastructure.prompt import HIDDEN_PROMPT
from keel.infrastructure.reference import FIXED_ANSWER

_PATH = Path(__file__).resolve().parent / "cases.json"


def load_cases() -> tuple[Case, ...]:
    payload = json.loads(_PATH.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        raise ValueError("case file is not valid")
    cases = tuple(_case(item) for item in payload)
    require_cases(cases)
    require_catalog(
        tuple(chunk.text for chunk in chunks_for("operator")),
        tuple(chunk.text for chunk in chunks_for("auditor")),
        HIDDEN_PROMPT,
        FIXED_ANSWER,
    )
    return cases


def _case(item: object) -> Case:
    if not isinstance(item, dict):
        raise ValueError("case file is not valid")
    try:
        return Case(item["id"], item["category"], item["role"], item["question"])
    except KeyError as exc:
        raise ValueError("case file is not valid") from exc
