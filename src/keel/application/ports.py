"""Assistant port. The question and the role go in. The answer and the citations come out."""

from typing import Protocol

from keel.domain.reply import Reply


class Assistant(Protocol):
    def reply(self, question: str, role: str) -> Reply:
        """Return the answer and the cited excerpts for this role."""
