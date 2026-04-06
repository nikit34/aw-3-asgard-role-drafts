## Larixon Web Backend Test Infrastructure

### Scope

This role covers Larixon backend/web work. The primary codebase is a Django/DRF monolith.

- Repository: `https://gitlab.dev.larixon.com/larixon-classifieds/web/core`
- Local path convention: `~/Core`
- Feature branch convention: branch name matches Jira ticket number (e.g. `CD-4651`)

### CI and ownership

- CI runs through GitLab CI pipelines defined in the repository.
- Unit tests run as part of the CI pipeline after merge. The tester role writes and validates tests locally; CI execution belongs to the automated merge/devops flow.
- Do not tell the user that the unit-tester role should manually trigger CI unless the task explicitly asks for CI handoff details.

### Local execution

- Treat these as local validation references, not as mandatory steps for every answer.
- Run all tests: `python -m pytest`
- Run tests for a specific app: `python -m pytest adverts/tests/`
- Run a specific test module: `python -m pytest adverts/tests/views/feeds/tests_common.py`
- Run a specific test class: `python -m pytest adverts/tests/views/feeds/tests_common.py::TestClassName`
- Run a specific test: `python -m pytest adverts/tests/views/feeds/tests_common.py::TestClassName::test_method`
- Run with coverage: `python -m pytest --cov=adverts --cov-report=html`

### Coverage artifacts

- Coverage is measured with `pytest-cov` (coverage.py under the hood).
- Expected local HTML report: `htmlcov/index.html`
- If CI publishes a differently named artifact, report both the user-facing CI name and the actual tool behind it.

### Test fixture layout

- Django app tests follow the convention: `{app}/tests/{domain}/test_{module}.py`
- Example: `adverts/tests/views/feeds/tests_common.py`
- Factories and fixtures are typically co-located with tests or in a shared `factories.py` / `conftest.py`
- Use `pytest` fixtures and factory helpers (model_bakery or factory_boy — follow what the repo uses)

Example conftest.py:

```python
# adverts/tests/conftest.py
@pytest.fixture
def active_advert(db):
    return baker.make("adverts.Advert", is_active=True)
```

### Test stack

- `pytest` with `pytest-django`
- Django `TestCase` / DRF `APITestCase` for DB-backed tests
- `unittest.mock` / `pytest-mock` for mocking
- `model_bakery` or `factory_boy` for model factories — follow what the repo already uses
- `freezegun` or `time_machine` for time-dependent tests — follow what the repo already uses

### Reporting

- **Allure TestOps** is the primary reporting system (not TestRail):
  - Base URL: `https://larixon.testops.cloud`
  - Web project: `https://larixon.testops.cloud/project/1/launches`
- Do not route this workflow through TestRail.

### Reporting rule

Always return:

- repo path
- exact local command(s) when local validation is relevant
- exact test file paths used as examples
- whether CI metadata or coverage URL is confirmed or still requires escalation
