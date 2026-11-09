"""The codespace keeps the default image. The try command is the reference assistant."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_the_codespace_keeps_the_default_image() -> None:
    config = json.loads((ROOT / ".devcontainer" / "devcontainer.json").read_text(encoding="utf-8"))
    assert set(config) == {"name", "hostRequirements", "features", "postCreateCommand"}
    assert config["name"] == "Keel"
    assert config["hostRequirements"] == {"cpus": 2}
    assert config["features"] == {
        "ghcr.io/devcontainers/features/python:1": {"version": "3.12", "installTools": False}
    }
    assert config["postCreateCommand"] == "python -m pip install --user -e '.[dev]'"


def test_the_readme_try_runs_the_reference_assistant() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "Create a codespace on the 2-core machine." in readme
    assert "default image" in readme
    assert "Delete the codespace when you finish." in readme
    assert "```bash\npython -m keel\n```" in readme
    lowered = readme.lower()
    for needle in ("openai", "anthropic", "render.com", "railway.app", "fly.dev"):
        assert needle not in lowered


def test_the_architecture_records_the_default_image() -> None:
    text = (ROOT / "docs" / "architecture" / "ARCHITECTURE.md").read_text(encoding="utf-8")
    assert "imagen Linux por defecto" in text
    assert "2 núcleos" in text
    assert "No hay prebuild." in text
