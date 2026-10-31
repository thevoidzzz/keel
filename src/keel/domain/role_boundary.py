"""A phrase that exists only in the other role's manual."""

from keel.domain.reply import Reply

OPERATOR_PHRASE = "The night desk books the close before noon."
AUDITOR_PHRASE = "Northline is the sample code."


def quotes_other_role(reply: Reply, role: str) -> bool:
    phrase = _foreign_phrase(role)
    if phrase in reply.answer:
        return True
    return any(phrase in excerpt for excerpt in reply.excerpts)


def _foreign_phrase(role: str) -> str:
    if role == "operator":
        return AUDITOR_PHRASE
    if role == "auditor":
        return OPERATOR_PHRASE
    raise ValueError("unknown role")
