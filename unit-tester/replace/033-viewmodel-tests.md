## Larixon ViewModel Tests

Use this slot for Android `ViewModel` tests and for the closest iOS presentation-state owner when the module uses `Presenter`, `ViewModel`, or another stateful presentation object.

### What presentation tests must prove

- initial state
- state transitions after user input
- success and error rendering state
- navigation or one-shot events
- saved-state restoration when relevant
- analytics only when it is part of the contract

### Strong Larixon examples

- `feature-advert-review/src/test/java/com/larixon/advert/review/presentation/screen/rating/RatingViewModelTest.kt`
- `feature-credit-application/ui/src/commonTest/kotlin/com/larixon/creditapplication/ui/CreditApplicationViewModelTest.kt`
- `app/src/test/kotlin/com/larixon/presentation/search/NotificationDialogViewModelTest.kt`

### Android rules

- Use a test dispatcher, not real main-thread timing
- Use `Turbine` for flow collection
- Assert the state object, not internal mutable fields
- Verify navigation and analytics only when they are triggered by observable behavior
- Keep `SavedStateHandle` explicit when the screen depends on persisted state

Turbine example with dispatcher setup:

```kotlin
class RatingViewModelTest : DescribeSpec({
    val testDispatcher = UnconfinedTestDispatcher()
    beforeSpec { Dispatchers.setMain(testDispatcher) }
    afterSpec { Dispatchers.resetMain() }

    describe("selecting rating") {
        it("updates state with selected value") {
            vm.state.test {
                awaitItem().selectedRating shouldBe null
                vm.onEvent(RatingEvent.SelectRating(4))
                awaitItem().selectedRating shouldBe 4
                cancelAndIgnoreRemainingEvents()
            }
        }
    }
})
```

### iOS rules

- Test the presentation object, not the rendered view tree
- Assert output state, commands, or callbacks
- If the module is MVP, map this slot to the presenter or coordinator that owns the state transition

```swift
func testLoadingStateTransition() {
    sut.loadReviews()
    XCTAssertTrue(sut.isLoading)
    waitForExpectations(timeout: 1)
    XCTAssertFalse(sut.isLoading)
}
```

### Review-domain behaviors worth testing

- review config load success and failure
- selected rating state
- reason toggle state
- clearing incompatible reasons when rating block changes
- submission success and error
- persisted state for partially filled review flows

### Anti-patterns

- snapshot-style assertions of a whole giant state object when only one field matters
- real delays instead of scheduler control
- mixing navigation, analytics, and state assertions into one unreadable mega-test
