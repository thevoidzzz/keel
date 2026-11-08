"""Score the reference assistant. Exit with an error when the bar is missed."""

import sys

from keel.application.ports import Assistant
from keel.application.score import score_assistant
from keel.domain.score import format_report, missed
from keel.infrastructure.cases import load_cases
from keel.infrastructure.reference import ReferenceAssistant


def run(assistant: Assistant, name: str) -> int:
    score = score_assistant(load_cases(), assistant)
    sys.stdout.write(format_report(name, score))
    if not missed(score):
        return 0
    for failure in score.failures:
        sys.stdout.write(f"{failure.id} {failure.category}\n")
    return 1


def main() -> None:
    try:
        code = run(ReferenceAssistant(), "reference")
    except ValueError as exc:
        raise SystemExit(str(exc)) from None
    if code:
        raise SystemExit(code)


if __name__ == "__main__":
    main()
