# AW-3 ASGARD Role Drafts

This directory contains project-specific role additions and overrides prepared for Jira `AW-3`:

### Mobile roles (Android/KMP + iOS)

- `test-architect`
- `unit-tester`
- `integ-tester`

### Backend/Web roles (Django/Python + React/Next.js + Playwright)

- `backend-test-architect`
- `backend-unit-tester`
- `frontend-unit-tester`
- `backend-integ-tester`
- `e2e-tester` (directory was `backend-e2e-tester`, renamed to match ASGARD role name)

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
- `backend-e2e-tester` directory renamed to `e2e-tester` to match ASGARD platform role name

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
| `033-test-data-fixtures.md` | replace | Platform has PL/UA/UZ markets; replaced with Larixon markets (bz/tj/mn/ja/pn/sl) |
| `037-multi-market-tests.md` | replace | Platform copy is not aligned with Larixon mobile markets |
| `200-larixon-test-devices.md` | add | Environments, devices, TestOps, emulator/simulator baseline |
| `036-accessibility-tests.md` | extend | Larixon-specific a11y constraints and mobile automation hints |

### Test Architect (mobile)

| Slot | Action | Reason |
| --- | --- | --- |
| `020-test-levels.md` | replace | Mobile-specific layer taxonomy (Unit Android / Unit iOS / Unit KMP / Integration Android / Integration iOS / E2E UI / Smoke) |
| `035-test-matrix.md` | replace | Case-block format with `[ ]`/`[x]` markdown checkboxes and `Реализован:` pytest-like IDs instead of platform flat `T-NNN` matrix |
| `200-larixon-mobile-td.md` | add | Mobile TD output rules: 5 compact non-overlapping files, Step Zero mobile-scope guard (BLOCK for web-only tasks), anti-patterns from MOB-795/MOB-750 |
| `070-checklist.md` | extend | Mobile TD checklist including Step Zero guard and platform-specific conventions |

### Backend Test Architect

| Slot | Action | Reason |
| --- | --- | --- |
| `020-test-levels.md` | replace | 4-level model (Unit BE/Unit FE/Integration/E2E) instead of platform 3-level |
| `035-test-matrix.md` | replace | Case-block format with `[ ]`/`[x]` markdown checkboxes and `Реализован:` pytest IDs; anti-patterns list from MOB-810/MOB-775 |
| `060-downstream-guidance.md` | extend | Added Frontend Unit Tester guidance template |
| `200-larixon-web-td.md` | add | Web TD output rules: 5 compact non-overlapping files, Ссылки/Контекст/Репозитории table, bug-TD Архитектура+Точки поломки pattern, reference TDs |
| `070-checklist.md` | extend | Larixon-specific TD checklist: case-status markers, `[НЕ РЕАЛИЗОВАНО]`, `Частично покрыт:`, publisher-managed `{toc}` |

### Backend Unit Tester

| Slot | Action | Reason |
| --- | --- | --- |
| `011-test-style.md` | add | Python/pytest/Django test style (slot 011 does not exist in manifest, inserted between 010 and 012) |
| `013-test-architect-input.md` | add | Bridge to test-architect downstream guidance: scenario IDs, coverage targets, risk map |
| `034-viewmodel-tests.md` | add | View-logic unit tests: permission predicates, pagination helpers, query param parsing (renumbered from 033 to avoid collision) |
| `200-larixon-web-infra.md` | add | Larixon web/backend infra, repo, CI, TestOps, local execution, test stack, conftest example |
| `020-coverage.md` | replace | pytest-cov coverage expectations with Django layer-specific floors, --cov-fail-under, pragma:no-cover |
| `031-service-tests.md` | replace | Service/business logic/management command tests — pure unit, no DB |
| `032-serializer-tests.md` | replace | DRF serializer/mapper/formatter tests |
| `033-model-tests.md` | replace | Django model methods (Model.__new__ pattern), manager/queryset (exception for DB) |

### Frontend Unit Tester

| Slot | Action | Reason |
| --- | --- | --- |
| `011-test-style.md` | add | React/Next.js test style (slot 011 does not exist in manifest, inserted between 010 and 012) |
| `013-test-architect-input.md` | add | Bridge to test-architect downstream guidance: scenario IDs, coverage targets, risk map |
| `200-larixon-web-frontend-infra.md` | add | Larixon frontend infra, repo, test stack, local execution, reporting |

### Backend Integration Tester

| Slot | Action | Reason |
| --- | --- | --- |
| `013-test-architect-input.md` | add | Bridge to test-architect downstream guidance: scenario IDs, endpoint assignments |
| `037-multi-market-tests.md` | add | Larixon web markets, Django settings, @override_settings snippet (manifest has no slot 037) |
| `200-larixon-web-infra.md` | add | Web integration infra, single-endpoint scope, stands, TestOps, reverse() pattern |
| `033-factories-fixtures.md` | replace | model_bakery replaces factory_boy (changed from extend to replace to avoid contradiction) |

### E2E Tester (renamed from backend-e2e-tester to match ASGARD role name)

| Slot | Action | Reason |
| --- | --- | --- |
| `011-test-style.md` | add | Playwright/pytest test style, framed as full-stack E2E extension of platform API patterns |
| `013-test-architect-input.md` | add | Bridge to test-architect downstream guidance; defers to BLOCK protocol per locked 012 |
| `031-external-services.md` | extend | Larixon-specific external service mocking: Playwright page.route(), backend mocks, market services |
| `200-larixon-web-e2e-infra.md` | add | tester-skills-mcp integration, Allure TestOps, multi-market E2E, reporting rule |
| `020-e2e-infrastructure.md` | replace | Larixon Playwright infra + restored multi-user setup, file org, test isolation |

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

## Fixes after platform slot comparison (2026-04-10)

Compared all 7 role drafts against actual ASGARD platform slots via API. Fixed:

### Blockers (would fail upload)
- `backend-e2e-tester/` renamed to `e2e-tester/` (platform role is `e2e-tester`)
- `backend-unit-tester/replace/011-test-style.md` moved to `add/` (slot 011 not in manifest)
- `frontend-unit-tester/replace/011-test-style.md` moved to `add/` (slot 011 not in manifest)
- `backend-unit-tester/add/033-viewmodel-tests.md` renumbered to `034` (collision with replace/033-model-tests)

### Locked slot conflicts resolved
- **unit-tester/011**: Added note that JUnit 5 is legacy-only, Kotest DescribeSpec preferred for new files
- **integ-tester/013**: Fixed "MEDIUM = 3/5 states" → risk-map controls priority/depth, not state count (5/5 preserved)
- **integ-tester/200**: Added CI-execution disclaimer per locked "write and compile only" rule
- **backend-unit-tester/034**: Rewrote from view/endpoint tests to pure view-logic helpers (locked 010 says views → integ-tester)
- **backend-unit-tester/031,033**: Aligned with no-DB rule; added Model.__new__() pattern, baker.prepare for unit tests
- **backend-test-architect/200**: P0/P1/P2 → P1/P2/P3; "Unit BE with DB" → "Unit BE no DB"; `backend-e2e-tester` → `e2e-tester`
- **backend-integ-tester/200**: Removed scope redefinition; this role tests single-endpoint per locked 010; fixed reverse() per BIT-004
- **backend-integ-tester/033**: Changed from `extend/` to `replace/` (model_bakery can't extend factory_boy slot)
- **e2e-tester/011**: Added framing: Playwright is full-stack E2E extension of API patterns from slot 030
- **e2e-tester/013**: "Proceed without strategy" → BLOCK per locked 012
- **frontend-unit-tester/011**: Removed fireEvent exception (violates locked FUT-006)

### Missing slots created
- `integ-tester/replace/033-test-data-fixtures.md` — Larixon markets (bz/tj/mn) replacing PL/UA/UZ
- `backend-test-architect/replace/020-test-levels.md` — 4-level model with frontend-unit-tester
- `backend-test-architect/replace/035-test-matrix.md` — P1/P2/P3, UTF-* prefix, Реализован convention
- `backend-test-architect/extend/060-downstream-guidance.md` — Frontend Unit Tester guidance template
- `e2e-tester/extend/031-external-services.md` — Playwright and backend mocking for Larixon services

### Content restored from platform
- **backend-unit-tester/020**: Added `# pragma: no cover` acceptable exclusions
- **backend-unit-tester/033**: Added `Model.__new__()` pure-unit technique
- **e2e-tester/020**: Added multi-user setup, test isolation, file organization
- **integ-tester/037**: Fixed locale formats to BCP47 (en-US, ru-RU, mn-MN)

## TD output convention (2026-04-17)

Aligned architect roles (`backend-test-architect`, `test-architect`) with the reference Larixon TDs (STM-65/68/101, CD-4653/1319/4017) and tester-skills-mcp rules. Changes:

- **Case format**: markdown checkbox `[ ]` / `[x]` in the heading (after `###`), never after list marker. `[x]` requires `Реализован: test_file::TestClass::test_method` line below.
- **`Частично покрыт: test_name`** marker for close-but-inexact existing coverage; case stays `[ ]`.
- **`[НЕ РЕАЛИЗОВАНО]`** plain-text label in heading when production code is blocking.
- **6 mandatory case fields**: Задача / Предусловия / Действие / Ожидаемый результат / Priority | Layer | Type. Flat `| ID | Scenario | Test Level | ... |` matrix is rejected.
- **Sequential numbering** across all sections; no `T-`/`UT-`/`IT-`/`E2E-` prefixes, no `17a` suffixes, no gaps.
- **Layer enum** (web): `Unit BE`, `Unit FE`, `Integration`, `Integration DB`, `Integration Contract`, `E2E`, `E2E UI`, `Smoke`.
- **Layer enum** (mobile): `Unit Android`, `Unit iOS`, `Unit KMP`, `Integration Android`, `Integration iOS`, `E2E UI Android`, `E2E UI iOS`, `Smoke`.
- **Risk-map**: compact `Риск | Приоритет | Источник | Кейсы` table (add `Платформа` column for mobile). `Источник` = ТЗ / Побочный эффект / Граничный случай / Регрессия.
- **5-file output model**: each of the 5 files from locked `050-output-format.md` stays compact and non-overlapping. `test-strategy.md` has no cases; `test-matrix.md` has only cases; risks live in `risk-map.md`; data in `test-data-strategy.md`; coverage in `coverage-targets.md`. Cross-reference via `См. test-strategy.md §Контекст`.
- **No `Итого` summary table** in `test-matrix.md` (mcp anti-pattern — counts come from publish action).
- **No agent signatures** (`*Automated by ASGARD*`) or rework narratives (`⚠️ rework v2`) in TD body.
- **No emoji** in headings; use plain-text labels.
- **`{toc}` macro and `## {filename}` headers** are managed by the ASGARD publisher; agents must not insert them manually.
- **Step Zero guard** added to mobile `test-architect`: BLOCK with clear message for web-only tasks, no `НЕПРИМЕНИМО`-style TD body.
- **6 downstream `013-test-architect-input.md`** slots updated to the new format: plain case numbers, layer-section navigation, case status markers, factory-syntax expectations.

### Added scope: `test-architect/` (mobile)

The mobile `test-architect` platform role previously had no project-specific drafts in this repo. Added 4 slots mirroring `backend-test-architect`: `add/200-larixon-mobile-td.md`, `replace/020-test-levels.md`, `replace/035-test-matrix.md`, `extend/070-checklist.md`.

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
