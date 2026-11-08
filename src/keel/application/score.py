"""Walk the case set through the assistant port and score the replies."""

from collections.abc import Sequence

from keel.application.ports import Assistant
from keel.domain.case import Case, require_cases
from keel.domain.score import Score, score_replies


def score_assistant(cases: Sequence[Case], assistant: Assistant) -> Score:
    require_cases(cases)
    replies = tuple(assistant.reply(case.question, case.role) for case in cases)
    return score_replies(cases, replies)
