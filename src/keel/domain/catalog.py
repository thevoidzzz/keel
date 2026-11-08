"""The manuals and the prompt have to keep their signals apart, or there is no rate."""

from collections.abc import Sequence

from keel.domain.hidden_prompt import SENTINEL
from keel.domain.plant import TOKEN
from keel.domain.role_boundary import AUDITOR_PHRASE, OPERATOR_PHRASE


def require_catalog(
    operator_texts: Sequence[str],
    auditor_texts: Sequence[str],
    prompt: str,
    fixed_answer: str,
) -> None:
    if prompt == "" or fixed_answer == "":
        raise ValueError("catalog is not valid")
    _only_in(OPERATOR_PHRASE, operator_texts, auditor_texts, prompt, fixed_answer)
    _only_in(AUDITOR_PHRASE, auditor_texts, operator_texts, prompt, fixed_answer)
    if sum(TOKEN in text for text in operator_texts) != 1:
        raise ValueError("token is not only in the planted chunk")
    if any(TOKEN in text for text in auditor_texts) or TOKEN in prompt or TOKEN in fixed_answer:
        raise ValueError("token is not only in the planted chunk")
    manuals = (*operator_texts, *auditor_texts)
    if SENTINEL not in prompt or any(SENTINEL in text for text in manuals) or SENTINEL in fixed_answer:
        raise ValueError("sentinel is not only in the prompt")


def _only_in(
    phrase: str,
    allowed: Sequence[str],
    other_manual: Sequence[str],
    prompt: str,
    fixed_answer: str,
) -> None:
    if not any(phrase in text for text in allowed):
        raise ValueError("role phrase is missing from its manual")
    if any(phrase in text for text in other_manual) or phrase in prompt or phrase in fixed_answer:
        raise ValueError("role phrase is in the wrong manual")
