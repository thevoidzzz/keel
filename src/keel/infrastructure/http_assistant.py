"""One POST. The answer and the excerpts come back. No key is sent."""

import json
import urllib.error
import urllib.request

from keel.domain.errors import AssistantUnavailable
from keel.domain.reply import Reply


class HttpAssistant:
    def __init__(self, base_url: str, timeout: float = 5.0) -> None:
        self._url = _answers_url(base_url)
        self._timeout = timeout

    def reply(self, question: str, role: str) -> Reply:
        payload = _post(self._url, {"question": question, "role": role}, self._timeout)
        answer = payload.get("answer")
        if not isinstance(answer, str) or answer == "":
            raise AssistantUnavailable("the assistant returned no answer")
        citations = payload.get("citations")
        excerpts: list[str] = []
        if isinstance(citations, list):
            for citation in citations:
                excerpt = citation.get("excerpt") if isinstance(citation, dict) else None
                if isinstance(excerpt, str):
                    excerpts.append(excerpt)
        return Reply(answer, tuple(excerpts))


def _answers_url(base_url: str) -> str:
    return base_url.rstrip("/") + "/v1/answers"


def _post(url: str, body: dict[str, str], timeout: float) -> dict[str, object]:
    request = urllib.request.Request(
        url,
        data=json.dumps(body).encode(),
        headers={"content-type": "application/json", "accept": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode())
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise AssistantUnavailable("the assistant is unavailable") from exc
    if not isinstance(payload, dict):
        raise AssistantUnavailable("the assistant is unavailable")
    return payload
