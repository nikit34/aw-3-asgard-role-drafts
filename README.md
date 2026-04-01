# AW-3 ASGARD Role Drafts

This directory contains project-specific role additions and overrides prepared for Jira `AW-3`:

- `unit-tester`
- `integ-tester`

The files are organized to mirror the actions requested in the Jira task:

- `add/<slot>.md`
- `replace/<slot>.md`
- `extend/<slot>.md`

## Status

- ASGARD roles inspected on `2026-04-01`: `unit-tester`, `integ-tester`
- Available account permission: `viewer`
- Direct write attempt to ASGARD roles API failed with `403` and `required: write:roles`
- Final Role Composer preview for the project-composed roles cannot be generated until these drafts are uploaded as project additions/replacements in HEIMDALL
- Slack review on `2026-04-01` clarified that tester roles should not directly trigger Bamboo. They should design coverage, write tests, validate locally when possible, and hand off CI execution to the existing merge or devops flow.
- Server guidance from the same day clarified two more boundaries for the current mobile flow:
  - `Playwright` belongs to a separate web flow, not to the default mobile app tester skills
  - `BrowserStack` should not be described as a baseline runner for the current mobile tester skills

## Scope covered in this package

### Unit Tester

| Slot | Action | Reason |
| --- | --- | --- |
| `200-larixon-test-infra.md` | add | Larixon-specific ownership boundaries, local run references, fixture layout, Android+iOS notes |
| `011-test-style.md` | replace | Actual Larixon test style is mixed Android/KMP plus iOS XCTest/Quick, not one pure platform pattern |
| `020-coverage.md` | replace | Current Android repo uses Kover; legacy Jacoco wording exists in old docs |
| `031-repository-tests.md` | replace | Need Larixon examples and iOS-equivalent guidance |
| `032-usecase-tests.md` | replace | Need real Larixon domain examples, including review flow |
| `033-viewmodel-tests.md` | replace | Need Kotest/Turbine/dispatcher patterns from real code plus iOS equivalent |
| `034-mapper-tests.md` | replace | Need real DTO-to-domain examples, including paginated reviews |

### Integration Tester

| Slot | Action | Reason |
| --- | --- | --- |
| `037-multi-market-tests.md` | replace | Platform copy is not aligned with Larixon mobile markets |
| `200-larixon-test-devices.md` | add | Need environments, devices, TestOps notes, and native-first validation guidance for the current mobile flow |
| `036-accessibility-tests.md` | extend | Need Larixon-specific a11y constraints and mobile automation hints |
| `210-playwright-web-tests.md` | add | Optional separate-flow placeholder for confirmed web or hybrid work; intentionally excluded from the mobile baseline |

## Confirmed inputs used for the drafts

### Android

- Repo: `/Users/permi/classifieds-android-app`
- Current test stack in `CLAUDE.md` and Gradle:
  - `JUnit 5`
  - `Kotest`
  - `MockK`
  - `Turbine`
  - `Espresso`
  - `Allure`
  - `Kover`
- Real review-domain tests exist:
  - `feature-advert-review/.../RatingViewModelTest.kt`
  - `feature-advert-review/.../SubmitReviewUseCaseTest.kt`
  - `feature-advert-review/.../ReviewConfigMapperTest.kt`
  - `feature-advert-reviews/.../AdvertReviewsMapperTest.kt`
- Product flavors confirmed from Gradle:
  - `tj`
  - `mn`
  - `bz`
  - `ja`
  - `pn`
  - `sl`
- Market-specific flags confirmed:
  - `GDPR_GOOGLE` is enabled for `bz`
  - `EMONGOLIA_ENABLED` is enabled for `mn`
- Android UI tests already publish Allure metadata through annotations and `allure.properties`

### iOS

- Repo: `/Users/permi/classifieds-ios-app`
- Current unit/UI stack confirmed from `Podfile` and tests:
  - unit tests: `XCTestCase`, `Quick`, `Nimble`
  - UI tests: `XCTest`, `XCUIApplication`
  - Allure helpers in `LarixonUITests/Helpers/AllureXCTestExtensions.swift`
- Market targets confirmed from `AppCustomization.swift` files:
  - `Bazaraki`
  - `Somon.tj`
  - `Unegui.mn`
  - `Jacars`
  - `Pin.tt`
  - `Salanto`
- Locale and timezone values were taken from market `AppCustomization.swift` files, not guessed

### Shared QA infrastructure

- Allure/TestOps base URL: `https://larixon.testops.cloud`
- Default project reference found in `tester-skills-mcp`: `project/135`
- Confluence sources confirm:
  - Android builds are in Bamboo
  - iOS builds are often assembled manually or via Fastlane in current accessible process docs
  - BrowserStack was selected in a PoC, but credentials are not available in current sources
- Slack clarification from `2026-04-01`:
  - tester roles are not expected to start Bamboo jobs directly
  - CI and build execution should stay in the existing automated or devops-controlled flow
  - BrowserStack vs emulator or simulator still needs explicit owner confirmation for this workflow
  - Server clarified that `Playwright` is for web and should stay outside the current mobile app flow
  - Server also said not to describe those web-specific checks inside the current mobile tester skills for now

## Known gaps that still need owner confirmation

- BrowserStack should be treated as out of scope for the current baseline mobile tester skills unless the owner explicitly reintroduces cloud-device coverage
- BrowserStack credentials were not found
- A confirmed Playwright web repo/base URLs were not found, and Playwright should stay outside the mobile baseline because Server described it as a separate web flow
- Exact Bamboo plan keys can be added later as handoff metadata, but they are not required for the base tester-role behavior clarified in Slack
- Final ASGARD composed preview cannot be checked until someone uploads these overrides with `write:roles`

## Sources

### Jira

- `AW-3`: `https://larixon.atlassian.net/browse/AW-3`

### Confluence

- Mobile QA process: `https://larixon.atlassian.net/wiki/spaces/It1/pages/3531276289`
- BrowserStack choice: `https://larixon.atlassian.net/wiki/spaces/It1/pages/3493298191`
- Device matrix example: `https://larixon.atlassian.net/wiki/spaces/It1/pages/4071096331`

### Android code

- `/Users/permi/classifieds-android-app/CLAUDE.md`
- `/Users/permi/classifieds-android-app/gradle/libs.versions.toml`
- `/Users/permi/classifieds-android-app/app/build.gradle`
- `/Users/permi/classifieds-android-app/app/src/androidTest/resources/allure.properties`
- `/Users/permi/classifieds-android-app/feature-advert-review/src/test/java/com/larixon/advert/review/presentation/screen/rating/RatingViewModelTest.kt`
- `/Users/permi/classifieds-android-app/feature-advert-review/src/test/java/com/larixon/advert/review/domain/usecase/SubmitReviewUseCaseTest.kt`
- `/Users/permi/classifieds-android-app/feature-advert-review/src/test/java/com/larixon/advert/review/data/mapper/ReviewConfigMapperTest.kt`
- `/Users/permi/classifieds-android-app/feature-advert-reviews/data/src/commonTest/kotlin/com/larixon/advertreviews/data/remote/mapper/AdvertReviewsMapperTest.kt`
- `/Users/permi/classifieds-android-app/app/src/androidTest/kotlin/tj/somon/somontj/test/e2e/PinAuthorizationTest.kt`

### iOS code

- `/Users/permi/classifieds-ios-app/Podfile`
- `/Users/permi/classifieds-ios-app/LarixonTests/LocalizationSpec.swift`
- `/Users/permi/classifieds-ios-app/LarixonTests/API/APIAuthorizationTest.swift`
- `/Users/permi/classifieds-ios-app/LarixonUITests/Fixtures/BaseUITestCase.swift`
- `/Users/permi/classifieds-ios-app/LarixonUITests/Helpers/AllureXCTestExtensions.swift`
- `/Users/permi/classifieds-ios-app/LarixonUITests/Tests/Navigation/TabBarTests.swift`
- `/Users/permi/classifieds-ios-app/Larixon/Bazaraki/AppCustomization.swift`
- `/Users/permi/classifieds-ios-app/Larixon/Somon.tj/AppCustomization.swift`
- `/Users/permi/classifieds-ios-app/Larixon/Unegui.mn/AppCustomization.swift`
- `/Users/permi/classifieds-ios-app/Larixon/Jacars/AppCustomization.swift`
- `/Users/permi/classifieds-ios-app/Larixon/Pin.tt/AppCustomization.swift`
- `/Users/permi/classifieds-ios-app/Larixon/Salanto/AppCustomization.swift`
