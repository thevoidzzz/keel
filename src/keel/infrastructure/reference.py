"""Deterministic assistant. It cites the role's manual and does not read the question."""

from keel.domain.reply import Reply
from keel.infrastructure.manuals import chunks_for

FIXED_ANSWER = "See the cited passage."


class ReferenceAssistant:
    def reply(self, question: str, role: str) -> Reply:
        # The question does not choose the excerpts. Every chunk of the role comes back.
        return Reply(FIXED_ANSWER, tuple(chunk.text for chunk in chunks_for(role)))
