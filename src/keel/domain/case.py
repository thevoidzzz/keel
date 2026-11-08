"""One hand-written case. Signals stay in the manuals and the prompt, not on the row."""

from collections.abc import Sequence
from dataclasses import dataclass

from keel.domain.hidden_prompt import SENTINEL
from keel.domain.plant import TOKEN

ROLE_BOUNDARY = "role_boundary"
PLANTED_INSTRUCTION = "planted_instruction"
HIDDEN_PROMPT = "hidden_prompt"
BENIGN = "benign"
ADVERSARY_CATEGORIES = (ROLE_BOUNDARY, PLANTED_INSTRUCTION, HIDDEN_PROMPT)
ROLES = frozenset({"operator", "auditor"})


@dataclass(frozen=True, slots=True)
class Case:
    id: str
    category: str
    role: str
    question: str


def require_cases(cases: Sequence[Case]) -> None:
    """A set with an empty side, a repeated id, or a foreign label has no rate."""

    seen: set[str] = set()
    for case in cases:
        if case.id == "":
            raise ValueError("case id is empty")
        if case.id in seen:
            raise ValueError("duplicate id")
        seen.add(case.id)
        if case.category not in (*ADVERSARY_CATEGORIES, BENIGN):
            raise ValueError("unknown category")
        if case.role not in ROLES:
            raise ValueError("unknown role")
        if case.question == "":
            raise ValueError("question is empty")
        if case.category == PLANTED_INSTRUCTION and TOKEN in case.question:
            raise ValueError("planted question contains the token")
        if case.category == HIDDEN_PROMPT and SENTINEL in case.question:
            raise ValueError("prompt question contains the sentinel")
    adversary = [case for case in cases if case.category in ADVERSARY_CATEGORIES]
    benign = [case for case in cases if case.category == BENIGN]
    if not adversary:
        raise ValueError("adversary set is empty")
    if not benign:
        raise ValueError("benign set is empty")
    # Each printed category needs a denominator.
    for category in ADVERSARY_CATEGORIES:
        if not any(case.category == category for case in cases):
            raise ValueError("category has no cases")
