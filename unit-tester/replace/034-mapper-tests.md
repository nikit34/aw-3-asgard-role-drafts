## Larixon Mapper Tests

Mapper tests are mandatory when the task changes API contracts, DTO shape, pagination payloads, optional fields, or market-specific labels.

### Strong Larixon examples

- `feature-advert-review/src/test/java/com/larixon/advert/review/data/mapper/ReviewConfigMapperTest.kt`
- `feature-advert-reviews/data/src/commonTest/kotlin/com/larixon/advertreviews/data/remote/mapper/AdvertReviewsMapperTest.kt`
- `feature-credit-application/data/src/commonTest/kotlin/com/larixon/creditapplication/data/CreditApplicationRequestMapperTest.kt`
- `feature-advert-details/data/src/commonTest/kotlin/com/larixon/advertdetails/data/remote/mapper/AdvertDetailMapperTest.kt`

### What mapper tests must prove

- full happy-path mapping
- null or absent optional fields
- enum or key conversion
- nested object mapping
- pagination fields such as `count`, `next`, `bottom controls`
- preservation of IDs needed by the next layer

### Review-domain expectations

Example for review payloads (adapt to your task domain). For review list and review configuration payloads, test at least:

- pending and completed review card fields
- null rating vs numeric rating
- tags and optional comments
- advert metadata used for context click-through
- next-page URL preservation
- action controls that may be absent

### iOS mapping rule

Apply the same standard to iOS serializers, adapters, formatters, and model transformers. If a mapper is hidden behind a service, test the transformation behavior explicitly and name the responsible type.

### Writing rules

- Build DTO fixtures that show the branch clearly
- Assert exact field values for important business fields
- Keep one mapping concern per test
- Prefer stable literal values that make branch mistakes obvious

### Anti-patterns

- asserting only that mapping did not crash
- using one giant fixture for every case when a tiny DTO would show the branch faster
- skipping null-handling tests for fields that drive UI state
