## Larixon Backend Coverage Expectations

### Source of truth

- Prefer the current repo configuration over assumptions.
- Coverage is measured with `pytest-cov` (coverage.py).
- Expected local HTML report: `htmlcov/index.html`

### Working coverage floors

Use these as default target floors unless the repo or task explicitly defines stricter gates:

| Layer | Target floor |
| --- | --- |
| Model / manager / queryset | 85% |
| Service / business rule / use case | 90% |
| View / viewset / API endpoint | 80% |
| Serializer / mapper / formatter | 90% |
| Management command | 80% |

These are working engineering targets, not a license to write shallow tests. Behavior quality matters more than chasing a number.

### Coverage workflow

- Run with coverage: `python -m pytest --cov={app} --cov-report=html`
- Fail-below-threshold: `python -m pytest --cov={app} --cov-fail-under=80`
- Check specific module: `python -m pytest --cov={app}.{module} adverts/tests/test_{module}.py`
- The `htmlcov/index.html` report shows line-by-line coverage
- If CI publishes a coverage artifact, report the actual URL. Do not fabricate one.

### Review rule

When you evaluate coverage for a change:

- start from changed business behavior, not from raw percentages
- check whether all new branches, validation paths, and mapping branches have tests
- call out missing tests even if module-level coverage looks healthy
- call out inflated coverage if tests only assert default values or construction noise

### Reporting format

Always say:

- tool actually used (`pytest-cov`, or other)
- whether the CI report URL is confirmed
- which layer is under-covered
- which exact behaviors are still untested
