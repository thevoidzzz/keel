"""Score one remote assistant. The check does not call this module."""

import os
import sys
from datetime import date

from keel.domain.errors import AssistantUnavailable
from keel.infrastructure.http_assistant import HttpAssistant
from keel.__main__ import run


def main() -> None:
    url = os.environ.get("KEEL_ASSISTANT_URL", "").strip().rstrip("/")
    if not url:
        raise SystemExit("KEEL_ASSISTANT_URL is required")
    sys.stdout.write(f"ran_on: {date.today().isoformat()}\n")
    try:
        code = run(HttpAssistant(url), url)
    except (AssistantUnavailable, ValueError) as exc:
        raise SystemExit(str(exc)) from None
    if code:
        raise SystemExit(code)


if __name__ == "__main__":
    main()
