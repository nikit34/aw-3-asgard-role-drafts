## Larixon Unit Test Style

### Default rule

Larixon is mixed. Follow the dominant style of the touched module instead of forcing one universal format across the whole repo.

### Android and KMP

- Prefer the style already used in the module:
  - Kotest `DescribeSpec` is common in feature modules
  - JUnit-style test classes still exist in legacy app modules
- Common tools in the current Android repo:
  - `JUnit 5`
  - `Kotest`
  - `MockK`
  - `Turbine`
- Use sentence-style `it("...")` inside Kotest specs.
- Use `action_condition_expectedResult` naming in JUnit-style classes when the file already follows that convention.

Minimal Kotest example (dominant style in feature modules):

```kotlin
class ReviewConfigMapperTest : DescribeSpec({
    describe("map") {
        it("maps rating to domain model") {
            val result = mapper.map(dto)
            result.rating shouldBe 4
        }
        it("returns null when rating is absent") {
            val result = mapper.map(dtoWithoutRating)
            result.rating shouldBe null
        }
    }
})
```
- Assert behavior, state, and important collaboration. Do not assert implementation noise.
- When coroutines or flows are involved, use the test dispatcher and `Turbine` instead of sleeps.

### iOS

- Default to `XCTestCase` in existing legacy areas.
- Use `Quick` and `Nimble` only where the current target already uses them.
- Do not convert an existing XCTest-only test file to Quick just to add one more case.
- Keep one assertion vocabulary per file.

Minimal XCTestCase example:

```swift
func testAuthorizationReturnsToken() {
    let result = sut.authorize(credentials: validCredentials)
    XCTAssertNotNil(result.token)
    XCTAssertEqual(result.expiresIn, 3600)
}
```

### Assertions and doubles

- Android:
  - `shouldBe`
  - `shouldBeInstanceOf`
  - `coEvery`
  - `coVerify`
- iOS:
  - `XCTAssert*`
  - `expect(...)` only in Quick/Nimble files

### Good Larixon examples

- Android ViewModel style:
  - `feature-advert-review/.../RatingViewModelTest.kt`
- Android use case style:
  - `feature-advert-review/.../SubmitReviewUseCaseTest.kt`
- Android mapper style:
  - `feature-advert-review/.../ReviewConfigMapperTest.kt`
- iOS Quick style:
  - `LarixonTests/LocalizationSpec.swift`
- iOS XCTest style:
  - `LarixonTests/API/APIAuthorizationTest.swift`

### Mandatory writing rules

- One test = one behavior or one closely related branch
- Use real domain names from the task, not placeholder entities
- Prefer stable factories/builders over giant inline object graphs
- Keep comments rare and only for non-obvious setup
- If a module is legacy, extend the legacy style cleanly instead of starting a style war inside one file

### Do not

- Invent Android-only guidance for iOS work
- Mix Quick/Nimble and raw XCTest assertions in the same iOS file
- Rewrite the entire file structure when adding a single regression test
- Use sleeps where the repo already has dispatcher- or state-based synchronization
