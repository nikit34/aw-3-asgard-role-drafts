## Larixon Backend Unit Test Style

### Default rule

Follow the dominant style of the touched app/module. Larixon web/core is a Django monolith where conventions may vary between apps. Do not force a universal style across all apps.

### Python / pytest

- Prefer the style already used in the module:
  - `pytest`-style functions with fixtures in newer code
  - `django.test.TestCase` subclasses in legacy areas
  - DRF `APITestCase` for endpoint-touching tests
- Do not convert an entire existing `TestCase`-based file to pytest functions just to add one test.

### Naming conventions

- Test files: `test_{module}.py` or `tests_{module}.py` — follow existing convention in the app
- Test classes: `Test{Subject}{Context}` — e.g. `TestFacebookFeedXMLRendererUnit`
- Test methods: `test_{action}_{condition}_{expected}` — e.g. `test_toplevel_dicts_wrapped_in_listing`
- Keep names descriptive enough to serve as documentation

### Assertions

- Use plain `assert` statements in pytest-style tests
- Use `self.assert*` methods in `TestCase` subclasses
- Use `self.assertEqual`, `self.assertIn`, `self.assertRaises` in Django TestCase
- For DRF: `response.status_code`, `response.data`, `response.json()`
- For XML: `ET.fromstring()` with `find()` / `findall()` assertions

### Mandatory writing rules

- One test = one behavior or one closely related branch
- Use real domain names from the task, not placeholder entities
- Prefer stable factories/builders over giant inline object construction
- Keep comments rare and only for non-obvious setup
- If a module is legacy, extend the legacy style cleanly instead of starting a style war inside one file

### Parametrized tests

- Use `@pytest.mark.parametrize` for data-driven test variations
- Use `parameterized` or `subTest` in `TestCase` classes if that's the existing pattern
- Keep parametrize data readable — one row per scenario, not opaque tuples

### Do not

- Mix pytest assertions and `self.assert*` in the same file
- Rewrite the entire file structure when adding a single regression test
- Use `time.sleep()` in unit tests — use freezegun/time_machine for time-dependent logic
- Import production settings directly — use `@override_settings` for test-specific config
