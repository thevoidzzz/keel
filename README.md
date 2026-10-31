# Keel

Release gate for a grounded internal assistant. A change cannot ship if the assistant follows a planted instruction, crosses a role boundary, or leaks its hidden prompt.

## Tests

GitHub Actions runs `pytest` on pull requests and on pushes to `main`. The job installs no model client and uses no API key.

```bash
pip install -e ".[dev]"
pytest
```

## Contributing

Open a pull request against `main`. The `test` check has to pass before merge.

Architecture and decisions live in `docs/architecture/` and `docs/adr/`.
