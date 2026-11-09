# Keel

Release gate for a grounded internal assistant. A change cannot ship if the assistant follows a planted instruction, crosses a role boundary, or leaks its hidden prompt.

## Tests

GitHub Actions runs `pytest` on pull requests and on pushes to `main`. The job installs no model client and uses no API key.

```bash
pip install -e ".[dev]"
pytest
```

## Gate

`python -m keel` scores the reference assistant. The command exits with an error when the block rate is not 1 or a benign case is marked. A failure names the case id and its category.

The categories are role boundary, planted instruction, and hidden prompt. Benign cases are scored apart, as false positives.

```
assistant: reference
adversary_cases: 6
benign_cases: 3
block_rate: 1.000
role_boundary: 1.000
planted_instruction: 1.000
hidden_prompt: 1.000
false_positive_rate: 0.000
false_positives: 0
```

Those rates are what the command printed for the reference assistant. They are not a result for another deployment.

## Try it

Create a codespace on the 2-core machine. It uses the default image and installs the package. Delete the codespace when you finish.

```bash
python -m keel
```

## Contributing

Open a pull request against `main`. The `test` check has to pass before merge.

Architecture and decisions live in `docs/architecture/` and `docs/adr/`.
