## Larixon Backend Serializer and Mapper Tests

Mandatory when task changes: API contracts, serializer fields, response shapes, pagination payloads, optional fields, or market-specific labels.

### What serializer/mapper tests must prove

- full happy-path serialization and deserialization
- null/absent optional fields handled correctly
- enum/key/choice conversion
- nested object serialization
- pagination fields (count, next, results)
- ID and foreign-key preservation for downstream consumers
- validation rules on input serializers

### Django/DRF patterns

- Test serializers directly: `serializer = MySerializer(instance=obj)` then assert `serializer.data`
- Test input validation: `serializer = MySerializer(data=invalid_data)` then assert `serializer.is_valid()` is False
- For complex nested serializers, build the smallest meaningful instance with a factory
- For XML serializers/renderers: test `render()` output directly

### Real project patterns

Examples from existing codebase (adapt to your task):

- `FacebookFeedAutoSerializer`: added `availability`, fixed `transmission` case
- `FacebookFeedXMLRenderer._to_xml`: structural rendering logic with `attrs` key detection
- Response serializers for API v2 endpoints: field presence, optional fields, nested objects

Example:

```python
class TestFacebookFeedAutoSerializer:
    def test_serializes_availability_field(self):
        advert = baker.prepare("adverts.Advert", availability="in stock")
        serializer = FacebookFeedAutoSerializer(advert)
        assert serializer.data["availability"] == "in stock"

    def test_null_optional_field_excluded(self):
        advert = baker.prepare("adverts.Advert", transmission=None)
        serializer = FacebookFeedAutoSerializer(advert)
        assert "transmission" not in serializer.data
```

### Writing rules

- Build fixture showing the branch clearly (e.g. with and without an optional field)
- Assert exact field values for important business fields
- Keep one mapping concern per test
- Prefer stable literal values in assertions

### Anti-patterns

- asserting only that serialization didn't crash (no field value checks)
- one giant fixture for every test case
- skipping null-handling tests for fields that drive UI state
- mixing serializer validation tests with unrelated business logic tests
