## Larixon Web Integration Test Infrastructure

### Scope

This role covers integration testing for the Larixon backend/web Django monolith. Integration tests exercise full request/response cycles through the Django test client with real database.

- Repository: `https://gitlab.dev.larixon.com/larixon-classifieds/web/core`
- Local path convention: `~/Core`
- Feature branch convention: branch name matches Jira ticket number (e.g. `CD-4651`)

### CI and ownership

- CI runs through GitLab CI pipelines.
- Integration tests run as part of the CI pipeline after merge. The tester role writes and validates tests locally; CI execution belongs to the automated merge/devops flow.
- Do not instruct the user to manually trigger CI unless the task explicitly asks for CI handoff details.

### Local execution

- Run all tests: `python -m pytest`
- Run integration tests for an app: `python -m pytest adverts/tests/views/`
- Run a specific integration test: `python -m pytest adverts/tests/views/feeds/tests_common.py::FacebookFeedXMLStructureTest`
- Run with verbose output: `python -m pytest -v adverts/tests/views/feeds/`

### Environments

Always name the exact stand when specifying test prerequisites:

- Shared stands: `stand1.dev.larixon.com` through `stand13.dev.larixon.com`
- Market-specific: `bazaraki-master.dev.larixon.com`, `somon-master.dev.larixon.com`, `unegui-master.dev.larixon.com`, `jacars-master.dev.larixon.com`

"dev" or "staging" alone is not enough — always specify the exact stand URL.

### Test management and reporting

- **Allure TestOps** is the primary reporting system (not TestRail):
  - Base URL: `https://larixon.testops.cloud`
  - Web project: `https://larixon.testops.cloud/project/1/launches`
- Do not route this workflow through TestRail.

### Integration test patterns

- Use `APITestCase` with `self.client` for endpoint tests
- Create minimal DB fixtures with factories
- Assert full response cycle: status code, body structure, key field values
- For XML endpoints: parse response content with `ET.fromstring()` and use `find()` / `findall()`
- For paginated endpoints: assert `count`, `next`, `results` structure
- Test with authenticated and unauthenticated users
- Test filter, ordering, and limit parameters

Example (XML feed endpoint):

```python
class TestFacebookFeedXML(APITestCase):
    def test_feed_returns_valid_xml_with_listings(self):
        baker.make("adverts.Advert", is_active=True, _quantity=3)
        response = self.client.get("/api/v2/feeds/property/facebook/")
        self.assertEqual(response.status_code, 200)
        root = ET.fromstring(response.content)
        listings = root.findall(".//listing")
        self.assertEqual(len(listings), 3)

    def test_feed_returns_404_for_unknown_type(self):
        response = self.client.get("/api/v2/feeds/unknown/facebook/")
        self.assertEqual(response.status_code, 404)
```

### Real project examples

- `adverts/tests/views/feeds/tests_common.py` — XML structure, filter conditions, pagination

### Reporting rule

Every integration result must include:

- endpoint(s) and HTTP method(s) tested
- stand URL (if tested against running instance)
- test run artifact path
- factories/fixtures created
