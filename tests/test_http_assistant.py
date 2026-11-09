"""A remote assistant is a POST. The check never calls it."""

import json
import socket
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread

import pytest

from keel.__main__ import main as check_main
from keel.domain.errors import AssistantUnavailable
from keel.infrastructure.http_assistant import HttpAssistant
from keel.remote import main as remote_main


class _Peer(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
        length = int(self.headers.get("content-length", "0"))
        body = json.loads(self.rfile.read(length))
        self.server.bodies.append((body, self.headers.get("authorization")))  # type: ignore[attr-defined]
        data = json.dumps(self.server.payload).encode()  # type: ignore[attr-defined]
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, format: str, *args: object) -> None:
        return


def _serve(payload: dict[str, object]) -> tuple[ThreadingHTTPServer, str]:
    server = ThreadingHTTPServer(("127.0.0.1", 0), _Peer)
    server.payload = payload  # type: ignore[attr-defined]
    server.bodies = []  # type: ignore[attr-defined]
    Thread(target=server.serve_forever, daemon=True).start()
    return server, f"http://127.0.0.1:{server.server_address[1]}"


def test_an_excerpt_is_the_reply() -> None:
    server, url = _serve(
        {
            "answer": "See the cited passage.",
            "citations": [{"excerpt": "Northline is the sample code."}],
        }
    )
    try:
        reply = HttpAssistant(url).reply("Where is the close?", "operator")
    finally:
        server.shutdown()
    assert reply.answer == "See the cited passage."
    assert reply.excerpts == ("Northline is the sample code.",)
    body, authorization = server.bodies[0]
    assert body == {"question": "Where is the close?", "role": "operator"}
    assert authorization is None


def test_a_missing_answer_is_not_scored() -> None:
    server, url = _serve({"answer": None, "refused": True, "citations": []})
    try:
        with pytest.raises(AssistantUnavailable, match="no answer"):
            HttpAssistant(url).reply("Where is the close?", "operator")
    finally:
        server.shutdown()


def test_a_silent_peer_is_unavailable() -> None:
    with pytest.raises(AssistantUnavailable, match="unavailable"):
        HttpAssistant(_closed_url()).reply("Where is the close?", "operator")


def _closed_url() -> str:
    probe = socket.socket()
    probe.bind(("127.0.0.1", 0))
    port = probe.getsockname()[1]
    probe.close()
    return f"http://127.0.0.1:{port}"


def test_the_check_ignores_the_assistant_url(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("KEEL_ASSISTANT_URL", _closed_url())
    check_main()


def test_the_remote_run_names_the_url_and_the_day(capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch) -> None:
    server, url = _serve({"answer": "See the cited passage.", "citations": []})
    monkeypatch.setenv("KEEL_ASSISTANT_URL", url)
    try:
        try:
            remote_main()
        except SystemExit:
            pass
    finally:
        server.shutdown()
    text = capsys.readouterr().out
    assert text.startswith("ran_on: ")
    assert len(text.splitlines()[0]) == len("ran_on: 2026-11-09")
    assert f"assistant: {url}" in text
    assert "Where is the close?" not in text


def test_the_remote_run_requires_the_url(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("KEEL_ASSISTANT_URL", raising=False)
    with pytest.raises(SystemExit, match="KEEL_ASSISTANT_URL is required"):
        remote_main()
