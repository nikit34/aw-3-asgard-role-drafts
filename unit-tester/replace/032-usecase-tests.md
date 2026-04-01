## Larixon UseCase Tests

Use this slot for Android/KMP use cases and for the nearest iOS business-command/interactor equivalent when the project does not expose explicit `UseCase` classes.

### What use case tests must prove

- business validation rules
- correct repository or service interaction
- success result mapping
- error propagation
- branching by input or state

### Strong Larixon examples

- `feature-advert-review/src/test/java/com/larixon/advert/review/domain/usecase/SubmitReviewUseCaseTest.kt`
- `feature-credit-application/domain/src/commonTest/kotlin/com/larixon/creditapplication/domain/usecase/CalculateMonthlyPaymentUseCaseTest.kt`
- `feature-advert-details/domain/src/commonTest/kotlin/com/larixon/advertdetails/domain/usecase/GetAdvertDetailUseCaseTest.kt`

### Writing rules

- Keep the test focused on one business action
- Prefer real domain values over placeholders
- Assert the returned domain result and the important collaboration
- If object construction itself is invalid, test that validation explicitly
- If the use case is a pass-through wrapper with no business behavior, say so and avoid pretending there is meaningful logic

### Review-domain hints for review-feature work

For review features, use case tests should typically cover:

- completed-deal submission with rating
- failed-deal submission without rating
- invalid submission state
- backend error propagation
- tab state or counter recalculation only if it belongs to the business layer

### iOS mapping rule

If the iOS app uses interactors, coordinators, or service commands instead of explicit `UseCase` classes, test the smallest unit that owns the business decision and say that it is the iOS equivalent.

### Anti-patterns

- testing only the constructor
- asserting only that analytics ran while skipping the returned business result
- duplicating repository tests in the use case layer without adding business-value checks
