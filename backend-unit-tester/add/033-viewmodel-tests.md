## Larixon Backend View and API Endpoint Tests

Use this slot for Django views, DRF viewsets, API endpoints, and any module that handles HTTP request/response.

### What view tests must prove

- correct HTTP status code for success and error cases
- response body structure and key field values
- authentication and permission enforcement
- query parameter and filter behavior
- pagination response format and correctness
- content negotiation (JSON, XML) when applicable

### Django/DRF patterns

- Use `APITestCase` or `TestCase` with `self.client`
- Authenticate with `self.client.force_authenticate(user)` or `self.client.force_login(user)`
- Test both authenticated and unauthenticated access
- For XML endpoints (feeds): parse with `ET.fromstring()` and assert structure with `find()` / `findall()`

### What this layer covers vs integration

View tests at the unit level focus on response correctness with controlled DB state. Full integration tests (real multi-service flows, external dependencies) belong in `backend-integ-tester`.

### Writing rules

- Set up minimal DB state needed for the endpoint
- Assert response status, key body fields, and edge-case behavior
- Use parametrize for multiple filter/query combinations
- Test error responses explicitly: 400, 403, 404, 409 as applicable

### Real project patterns

- Feed endpoints: test XML structure, listing count, nested element absence
- API v2 endpoints: test JSON response shape, pagination, filter parameters
- List endpoints: test ordering, limit, offset behavior

### Anti-patterns

- asserting only status 200 without checking response body
- testing the same serializer output that is already tested in `032-serializer-tests`
- skipping permission tests for authenticated-only endpoints
- using `json.loads(response.content)` when `response.data` or `response.json()` is available

Example (DRF viewset + XML endpoint):

```python
class TestFacebookFeedView(APITestCase):
    def test_returns_valid_xml(self):
        response = self.client.get("/api/v2/feeds/property/facebook/")
        self.assertEqual(response.status_code, 200)
        root = ET.fromstring(response.content)
        self.assertIsNotNone(root.find(".//listing"))

    def test_unauthenticated_returns_403(self):
        self.client.logout()
        response = self.client.get("/api/v2/feeds/property/facebook/")
        self.assertEqual(response.status_code, 403)
```
