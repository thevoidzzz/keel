"""What an assistant returned. The gate does not rewrite either field."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Reply:
    answer: str
    excerpts: tuple[str, ...]
