## Larixon Web E2E Project Additions

### tester-skills-mcp integration

The team uses `tester-skills-mcp` for E2E workflow:

- **Coverage scan**: `action_e2e_functional_scan` — scans `functional_tests/`, matches against TD, identifies gaps
- **Playwright research**: `action_playwright_research` — smoke-check, locator collection, snapshot analysis
- **E2E implementation**: `build_playwright_e2e_implement_prompt` — implements Playwright tests from TD
- **Functional implementation**: `build_e2e_implement_prompt` — implements pytest E2E tests from TD

Workflow:
1. Run `action_e2e_functional_scan` to identify existing coverage and new scenarios
2. Run `action_playwright_research` for UI context and locator discovery
3. Use `build_playwright_e2e_implement_prompt` for implementation

### Test management and reporting

- **Allure TestOps** is the primary reporting system (not TestRail):
  - Base URL: `https://larixon.testops.cloud`
  - Web project: `https://larixon.testops.cloud/project/1/launches`
- TD cases are synced to Allure via `td-allure-sync` skill
- Do not route through TestRail.

### Multi-market E2E

For user-facing flows affected by locale, currency, or market-specific features:

- Test at minimum: Bazaraki (EN/EUR), Somon (RU/TJS), Unegui (MN/MNT)
- Switch market by changing the base URL to the market-specific stand
- Verify Cyrillic content rendering on Somon stand
- Verify currency display on market-appropriate stands

### Reporting rule

Every E2E result must include:

- stand URL tested against
- browser(s) used
- market(s) tested
- test run link or artifact path
- flaky risks identified
- whether CI metadata is confirmed or still requires escalation
