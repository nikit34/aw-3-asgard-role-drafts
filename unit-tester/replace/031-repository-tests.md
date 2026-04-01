## Larixon Repository Tests

Use this slot for Android/KMP repositories and for the closest iOS data-layer equivalent if the iOS module does not use the word `Repository`.

### What repository tests must prove

- request parameters are forwarded correctly
- correct local or remote source is used
- DTO or entity mapping is applied correctly
- errors are translated or propagated intentionally
- pagination or cursor data is preserved
- market- or feature-specific flags change behavior only where expected

### Android examples

- `app/src/test/kotlin/com/larixon/repository/payments/PaymentsRepositoryTest.kt`
- `app/src/test/kotlin/tj/somon/somontj/model/repository/categories/RemoteCategoryRepositoryTest.kt`
- `app/src/test/kotlin/tj/somon/somontj/domain/favorites/searches/RemoteSearchRepositoryTest.kt`

### Review-domain examples useful for AW-3

- `feature-advert-reviews/data/src/commonTest/kotlin/com/larixon/advertreviews/data/remote/mapper/AdvertReviewsMapperTest.kt`

Even when a review list module is mapper-heavy, still test the contract at the data boundary:

- count and next-page URL
- review card fields
- null rating vs non-null rating
- optional controls like bottom actions

### iOS mapping rule

If iOS code has no explicit `Repository` abstraction, map this slot to the class that owns the same boundary:

- API client
- service
- gateway
- store
- remote provider

Say that you are testing a `repository-equivalent` instead of inventing a repository that does not exist.

### Fixture rules

- Build the smallest meaningful DTO or entity
- Inline only fields that matter for the behavior under test
- Reuse a local factory helper if the file already has one
- Keep names market- and domain-specific where that changes behavior

### Anti-patterns

- asserting only that a mock was called, without checking returned behavior
- hiding all fields behind giant fixture helpers until the test intent is unreadable
- mixing mapper verification and unrelated business rules into the same repository case
