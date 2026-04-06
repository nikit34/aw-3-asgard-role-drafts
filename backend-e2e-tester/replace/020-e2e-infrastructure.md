## Larixon Web E2E Infrastructure

### Scope

This role covers browser-level E2E testing for the Larixon web platform using Playwright. Tests verify complete user flows in a real browser against a running stand.

- Repository: `https://gitlab.dev.larixon.com/larixon-classifieds/web/core`
- Local path convention: `~/Core`
- Feature branch convention: branch name matches Jira ticket number (e.g. `CD-4651`)
- Existing E2E tests: `functional_tests/` directory (pytest-based)
- Playwright tests: being introduced alongside existing functional tests

### CI and ownership

- CI runs through GitLab CI pipelines.
- E2E tests run as part of the CI pipeline. The tester role writes and validates tests locally; CI execution belongs to the automated merge/devops flow.
- Do not instruct the user to manually trigger CI unless the task explicitly asks for it.

### Environments

E2E tests execute against shared stands. Always name the exact stand:

- Shared stands: `stand1.dev.larixon.com` through `stand13.dev.larixon.com`
- Market-specific: `bazaraki-master.dev.larixon.com`, `somon-master.dev.larixon.com`, etc.

### Playwright setup

- Framework: Playwright for Python (`playwright` + `pytest-playwright`)
- Browser: Chromium by default, Firefox and WebKit for cross-browser validation
- Base URL: configured per-stand (e.g. `https://bazaraki-master.dev.larixon.com`)

### Local execution

- Install Playwright browsers: `playwright install`
- Run all E2E tests: `python -m pytest functional_tests/`
- Run Playwright tests: `python -m pytest functional_tests/ -k playwright`
- Run with headed browser: `python -m pytest functional_tests/ --headed`
- Run specific test: `python -m pytest functional_tests/test_feeds.py::test_name`
- Run against specific stand: `BASE_URL=https://stand5.dev.larixon.com python -m pytest functional_tests/`
