"""Failures of a peer. They are not a scored reply."""


class AssistantUnavailable(Exception):
    """The assistant did not return a reply. The gate does not score this."""
