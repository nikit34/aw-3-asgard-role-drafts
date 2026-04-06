## Larixon Factory and Fixture Additions

### Factory library

- Use `model_bakery` (`baker.make`, `baker.prepare`) — this is the library used in the repo
- If `factory_boy` is found in specific apps, follow that app's convention
- Do not introduce a new factory library

### Shared fixtures

- App-level shared fixtures live in `{app}/tests/conftest.py`
- Cross-app fixtures (if any) live in a top-level `conftest.py`
- Use `@pytest.fixture` for pytest-style tests, `setUp()` for `TestCase` subclasses

### Writing rules

- Build the smallest meaningful model instance
- Inline only fields relevant to the behavior under test
- Use `baker.make` for DB-persisted instances, `baker.prepare` for in-memory only
- Keep factory names domain-specific: `active_advert`, `expired_advert`, not `advert1`, `advert2`
