# AW-3 ASGARD Role Drafts

This directory contains project-specific role additions and overrides prepared for Jira `AW-3`:

### Mobile roles (Android/KMP + iOS)

- `unit-tester`
- `integ-tester`

### Backend/Web roles (Django/Python + Playwright)

- `backend-test-architect`
- `backend-unit-tester`
- `backend-integ-tester`
- `backend-e2e-tester`

The files are organized to mirror the actions requested in the Jira task:

- `add/<slot>.md`
- `replace/<slot>.md`
- `extend/<slot>.md`

## Status

- ASGARD roles inspected on `2026-04-01`: `unit-tester` (Manifest v2, 15 slots), `integ-tester` (Manifest v3, 15 slots)
- Account permission: `viewer` — files need to be uploaded by a user with `write:roles`
- Bamboo plan keys confirmed: `AD-AT`, `AD-IN`, `ID-II`
- Allure TestOps confirmed as reporting system (not TestRail): projects 69 and 168
- Tests run on emulators/simulators — BrowserStack is out of scope
- Playwright is out of scope for mobile roles (separate web flow)
- Tester roles write and validate locally; CI execution belongs to the merge/devops flow
- Backend/web roles use Playwright for E2E, TestOps project 1, GitLab CI

## Scope covered in this package

### Unit Tester

| Slot | Action | Reason |
| --- | --- | --- |
| `013-test-architect-input.md` | add | Bridge to test-architect downstream guidance: scenario IDs, coverage targets, risk map, test data |
| `200-larixon-test-infra.md` | add | Larixon-specific ownership boundaries, local run references, fixture layout, Android+iOS notes |
| `011-test-style.md` | replace | Actual Larixon test style is mixed Android/KMP plus iOS XCTest/Quick, not one pure platform pattern |
| `020-coverage.md` | replace | Current Android repo uses Kover; legacy Jacoco wording exists in old docs |
| `031-repository-tests.md` | replace | Need Larixon examples and iOS-equivalent guidance |
| `032-usecase-tests.md` | replace | Need real Larixon domain examples, including review flow |
| `033-viewmodel-tests.md` | replace | Need Kotest/Turbine/dispatcher patterns from real code plus iOS equivalent |
| `034-mapper-tests.md` | replace | Need real DTO-to-domain examples, including paginated reviews |
| `035-kmp-testing.md` | extend | KMP testing: commonTest vs platform, running, expect/actual mocking |

### Integration Tester

| Slot | Action | Reason |
| --- | --- | --- |
| `013-test-architect-input.md` | add | Bridge to test-architect downstream guidance: scenario IDs, screen/flow assignments, MockWebServer setup |
| `037-multi-market-tests.md` | replace | Platform copy is not aligned with Larixon mobile markets |
| `200-larixon-test-devices.md` | add | Environments, devices, TestOps, emulator/simulator baseline |
| `036-accessibility-tests.md` | extend | Larixon-specific a11y constraints and mobile automation hints |

### Backend Test Architect

| Slot | Action | Reason |
| --- | --- | --- |
| `200-larixon-web-td.md` | add | TD workflow rules, web infra, tester-skills-mcp integration, markets, environments, output artifacts |
| `070-checklist.md` | extend | Larixon-specific TD checklist: Confluence publish, Allure sync, role assignments, mcp parsing |

### Backend Unit Tester

| Slot | Action | Reason |
| --- | --- | --- |
| `013-test-architect-input.md` | add | Bridge to test-architect downstream guidance: scenario IDs, coverage targets, risk map |
| `033-viewmodel-tests.md` | add | Django view/DRF viewset/API endpoint tests (no platform slot, added between 032 and 040) |
| `200-larixon-web-infra.md` | add | Larixon web/backend infra, repo, CI, TestOps, local execution, test stack, conftest example |
| `011-test-style.md` | replace | Python/pytest/Django test style instead of generic platform pattern |
| `020-coverage.md` | replace | pytest-cov coverage expectations with Django layer-specific floors, --cov-fail-under |
| `031-service-tests.md` | replace | Service/business logic/management command tests (was 032-usecase-tests) |
| `032-serializer-tests.md` | replace | DRF serializer/mapper/formatter tests (was 034-mapper-tests) |
| `033-model-tests.md` | replace | Django model/manager/queryset tests (was 031-repository-tests) |

### Backend Integration Tester

| Slot | Action | Reason |
| --- | --- | --- |
| `013-test-architect-input.md` | add | Bridge to test-architect downstream guidance: scenario IDs, endpoint assignments |
| `200-larixon-web-infra.md` | add | Web integration infra, environments, stands, TestOps, execution commands |
| `037-multi-market-tests.md` | replace | Platform copy not aligned with Larixon web markets and Django settings |

### Backend E2E Tester

| Slot | Action | Reason |
| --- | --- | --- |
| `011-test-style.md` | add | Playwright/pytest test style, POM patterns, locator strategy (manifest has no slot 011, inserted between 010 and 012) |
| `013-test-architect-input.md` | add | Bridge to test-architect downstream guidance: scenario IDs, flow assignments |
| `200-larixon-web-e2e-infra.md` | add | tester-skills-mcp integration, Allure TestOps, multi-market E2E, reporting rule |
| `020-e2e-infrastructure.md` | replace | Larixon-specific Playwright infra, repo, stands, environments, CI, local execution |

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

### Web/Backend

- Repo: `https://gitlab.dev.larixon.com/larixon-classifieds/web/core`
- Local path convention: `~/Core`
- Test framework: `pytest` with `pytest-django`
- E2E framework: Playwright (`pytest-playwright`)
- Django/DRF monolith with apps: `adverts`, `locations`, etc.
- Feature branch convention: branch name = Jira ticket number (e.g. `CD-4651`)
- Real test examples from TD:
  - `adverts/tests/views/feeds/tests_common.py` — Facebook feed XML structure tests
  - `adverts/views/feeds/renderers.py` — renderer unit tests
  - `adverts/serializers/feeds/fb.py` — serializer tests
- E2E tests: `functional_tests/` directory
- Markets configured via Django settings files (e.g. `bazaraki.py`, `somon.py`)

### tester-skills-mcp

- Repository: `/Users/permi/tester-skills-mcp`
- TD workflow: `build_td_workflow_spec_prompt`, `build_td_workflow_impl_prompt`
- TD publication: `action_td_publish`, `build_td_publish_prompt` (separate chat)
- Allure sync: `action_td_allure_sync`, `build_td_allure_sync_prompt`
- E2E scan: `action_e2e_functional_scan`, `build_e2e_scan_prompt`
- E2E implementation: `build_e2e_implement_prompt`
- Playwright research: `action_playwright_research`, `build_playwright_research_prompt`
- Playwright implementation: `build_playwright_e2e_implement_prompt`
- TD format requirement: markdown table with `Name` column for downstream parsing

### Shared QA infrastructure

- **Allure TestOps** (primary reporting, not TestRail):
  - Base URL: `https://larixon.testops.cloud`
  - Web project: `https://larixon.testops.cloud/project/1/launches`
  - Android project: `https://larixon.testops.cloud/project/69/launches`
  - iOS project: `https://larixon.testops.cloud/project/168/launches`
- **Bamboo** plan keys:
  - `AD-AT` — Android Automated Tests: `https://bamboo.dev.larixon.com/browse/AD-AT`
  - `AD-IN` — Android Integration: `https://bamboo.dev.larixon.com/browse/AD-IN`
  - `ID-II` — iOS Integration: `https://bamboo.dev.larixon.com/browse/ID-II`
- **Execution**: emulators (Android) and simulators (iOS) — BrowserStack out of scope
- **Playwright**: out of scope (separate web flow)
- Tester roles write and validate locally; CI execution belongs to the merge/devops flow

## Remaining steps

- Upload these files to ASGARD Role Composer as project additions/replacements (requires `write:roles`)
- Verify assembled prompts via "Preview Assembled" in HEIMDALL after upload

## Sources

### Jira

- `AW-3`: `https://larixon.atlassian.net/browse/AW-3`

### Confluence

- Mobile QA process: `https://larixon.atlassian.net/wiki/spaces/It1/pages/3531276289`
- BrowserStack choice: `https://larixon.atlassian.net/wiki/spaces/It1/pages/3493298191`
- Device matrix example: `https://larixon.atlassian.net/wiki/spaces/It1/pages/4071096331`
- TD design rules: `https://larixon.atlassian.net/wiki/spaces/itdep/pages/3591733264`
- Workshop: Claude Code + MCP for QA: `https://larixon.atlassian.net/wiki/spaces/It1/pages/4115759106`
- tester-skills-mcp guide: `https://larixon.atlassian.net/wiki/spaces/It1/pages/4142563459`
- QA Claude Skills catalog: `https://larixon.atlassian.net/wiki/spaces/It1/pages/4209770530`
- TD folder (current): `https://larixon.atlassian.net/wiki/spaces/itdep/folder/4091674628`

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
