## Larixon Web E2E Test Style (Playwright)

### Default rule

Follow the dominant style in `functional_tests/`. Do not introduce a new test framework or folder structure if one already exists. Playwright tests integrate into the existing pytest-based E2E infrastructure.

### Playwright test patterns

- Use `pytest-playwright` fixtures: `page`, `browser`, `context`
- Write tests as pytest functions, not classes (unless the existing code uses classes)
- Use Playwright's auto-waiting — do not add explicit sleeps
- Prefer locators over raw selectors: `page.get_by_role()`, `page.get_by_text()`, `page.get_by_test_id()`
- Use `expect()` from `playwright.sync_api` for assertions

### Naming conventions

- Test files: `test_{feature}.py` or `test_{flow}.py`
- Test functions: `test_{user_action}_{expected_outcome}` — e.g. `test_filter_by_category_shows_filtered_results`
- Keep names descriptive enough to serve as documentation

### Page Object Model

- Use Page Objects for reusable page interactions when the same page is tested in multiple scenarios
- Keep Page Objects thin — locators and simple actions, not business logic
- Store page objects in a `pages/` directory within `functional_tests/`
- Do not create a Page Object for a page tested only once

### Locator strategy

Priority order for locators:

1. `get_by_test_id()` — most stable, preferred when `data-testid` attributes exist
2. `get_by_role()` — semantic, resilient to text changes
3. `get_by_text()` — for user-visible content assertions
4. `get_by_label()` — for form fields
5. CSS selectors — last resort, when semantic locators are unavailable

Never use XPath unless there is no CSS/semantic alternative.

### Assertions

- Use Playwright's `expect()` for auto-retrying assertions:
  - `expect(page.get_by_role("heading")).to_have_text("...")`
  - `expect(page.locator(".item")).to_have_count(3)`
  - `expect(page).to_have_url(re.compile(r"/results/"))`
- For response validation: intercept with `page.route()` or `page.expect_response()`
- Do not use plain `assert` for UI state — it does not auto-retry

### Test data and setup

- Use API calls or direct DB setup for preconditions — do not navigate through UI for test data creation
- Clean up test data after tests when feasible
- Use unique identifiers to avoid collision between parallel test runs

### Flaky test prevention

- Never use `time.sleep()` — use Playwright's auto-waiting or `page.wait_for_selector()`
- Use `expect()` with auto-retry instead of immediate assertions
- Isolate tests — each test should work independently
- Use `browser.new_context()` for test isolation when needed

### Mandatory writing rules

- One test = one user flow or one closely related behavior
- Use real domain data from the task, not generic placeholders
- Keep comments rare — test names should be self-documenting
- Take screenshots on failure: configure in `conftest.py`
- If adding to existing files, extend the existing style cleanly

### Do not

- Add `time.sleep()` anywhere in Playwright tests
- Use raw `page.query_selector()` when Playwright locators are available
- Create complex inheritance hierarchies for page objects
- Test backend logic through the browser when an API test would suffice
- Skip cross-browser testing without documenting why
