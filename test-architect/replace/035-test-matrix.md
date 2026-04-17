## Test Matrix Design

### File: `test-matrix.md`

This file is the bulk of the test design. It is **NOT a flat table**. It contains self-contained test case blocks grouped by layer, following the Larixon team convention used for web TDs — adapted for mobile (Android + iOS). See reference TDs in `200-larixon-mobile-td.md`.

Reject the default platform `| ID | Scenario | Test Level | Priority | ... |` flat matrix and the MOB-802 multi-document format (`coverage-targets.md`, `risk-map.md` as separate governance docs). Every test scenario lives as a self-contained block with Задача/Предусловия/Действие/Ожидаемый.

### Per-case block template

```markdown
### N [ ] {title — describes behavior, not implementation}

Реализован: `TestClass::testMethodName` (Android)  |  `TestSpec::"scenario description"` (iOS Quick/Nimble)  |  `TestClass.testMethodName` (iOS XCTest)
   (omit this line when the case is not yet written)

**Задача:** one sentence — what behavior this proves.

**Предусловия:**
- `val user = UserFactory.create(profile = Profile.business)` (Android) / `let user = UserFactory.business()` (iOS) — exact factory calls
- `MockWebServer.enqueue(MockResponse().setBody(fixture("advert_reviews_summary.json")))` when integration
- feature flag: `FakeFeatureFlags(GDPR_GOOGLE = true)` for `bz` market

**Действие:** exact call.
- Unit: `AdvertReviewsViewModel(repo).loadReviews(advertId = 42)` (Android) / `sut.loadReviews(advertId: 42)` (iOS)
- Integration: navigate to screen via test rule `composeTestRule.setContent { AdvertReviewsScreen(...) }` + interact with nodes
- E2E UI: `UiDevice` / `XCUIApplication` steps against an installed app on emulator/simulator

**Ожидаемый результат:** exact observable values.
- `state.reviews.size == 3`
- `state.averageRating == 4.5f`
- `composeTestRule.onNodeWithText("5 reviews").assertIsDisplayed()`
- NOT "correct", "as expected", "работает" — always exact values

Priority: P0 | Layer: Unit Android | Type: auto-candidate
```

### Case status markers

Each case heading carries a markdown checkbox in the heading itself (after `###`), never after a list marker:

- `### N [ ] Title` — case **not yet implemented**. Omit `Реализован:` line.
- `### N [x] Title` — case **implemented**. MUST include `Реализован: TestClass::testMethodName` (or iOS equivalent) line under the heading.
- `### N [ ] Title` with `Частично покрыт: test_name` line below — existing test covers the area but not this exact scenario. Downstream tester still writes a new test; partial coverage is acknowledged in the Jira comment.
- `### N [ ] Title [НЕ РЕАЛИЗОВАНО]` — production code itself is not yet written. No test can be written against nonexistent code. Downstream tester leaves `[ ]`, blocks on the developer, notes in Jira.

**Forbidden combinations:**
- `* [ ]` / `- [ ]` / `* [x]` / `- [x]` — list-marker + checkbox is a Confluence-task anti-pattern. Checkbox goes **only** in the case heading.
- Using `[x]` without `Реализован:` line — checkbox without evidence of the test location.
- Using `Реализован:` with `[ ]` — contradiction; if test exists, checkbox is `[x]`.

### Rules

- **Sequential numbering across ALL sections** (1, 2, 3…). See CD-4653 for a canonical example (cases 1..30 across 4 layers).
- **Hierarchical sub-numbering** (1.1, 1.2) is OK inside a section but the top-level counter still increments globally.
- No ID prefixes (no `T-`, `UT-`, `IT-`, `E2E-`). No letter suffixes (`17a`). No gaps.
- `Предусловия` MUST use project factory / fixture syntax — never abstract descriptions like "a valid user" or "mock OpenAI".
- `Действие` for Integration/E2E: exact external contract (UI steps with accessibility IDs, emulator interactions, screen navigation). **Do NOT reference internal class names** in Integration/E2E — write the user-observable action.
- `Действие` for Unit: exact method call with arguments (internal class names are OK at Unit level — the unit under test IS the class).
- `Ожидаемый результат` MUST include exact values and assertions. No "correct".
- Case title MUST be parseable by `tester-skills-mcp` as `Name` column (single line, ≤120 chars, no Markdown formatting).

### Parametric cases

Two acceptable patterns:

**A. Kotest `withData` / iOS Quick `context` (2-3 combinations):**

```markdown
### 12 [x] map_review_date_label: today/yesterday/older → корректный формат

Реализован: `AdvertReviewMapperTest::"today 10:30 → Today, 10:30"`,
            `AdvertReviewMapperTest::"yesterday 13:59 → Yesterday, 13:59"`,
            `AdvertReviewMapperTest::"older → 07.03.2026, 05:03"`

**Задача:** проверить date_label для today / yesterday / older.

**Предусловия:** `TimeProvider.freezeAt("2026-03-09T15:00")`, 3 `UserReview` с разными `createdAt`.

**Действие:** для каждого `createdAt` вызвать `ReviewMapper.toItem(review)`.

**Ожидаемый результат:**
- today 10:30 → `"Today, 10:30"`
- yesterday 13:59 → `"Yesterday, 13:59"`
- older → `"07.03.2026, 05:03"`

Priority: P1 | Layer: Unit Android | Type: auto-candidate
```

**B. Table inside the case (CD-1319 pattern — 4+ combinations):**

```markdown
### 1 [ ] Параметрический: показ блока reviews_summary при разных условиях

**Задача:** проверить логику показа reviews_summary в карточке.

**Предусловия:** экран `AdvertCardScreen` с моком эндпоинта `GET /api/v2/apps/adverts/{id}/`.

**Действие:** для каждого набора входов замокать API-ответ, открыть экран, считать видимость блока.

| # | collect_reviews_enabled | avg_rating | reviews_count | Ожидаемый результат |
| --- | --- | --- | --- | --- |
| 1 | true | 4.5 | 3 | блок виден, текст "4.5 (3 reviews)" |
| 2 | true | null | 3 | блок скрыт (no rating) |
| 3 | true | 4.5 | 0 | блок скрыт (no reviews) |
| 4 | false | 4.5 | 3 | блок скрыт (disabled by rubric) |

Priority: P0 | Layer: Integration Android | Type: auto-candidate
```

### Priority rules

- **P0**: critical user flow / regression in public contract / crash path / auth flow
- **P1**: important secondary flow / error/empty state / i18n plurals / market-specific copy
- **P2**: edge case / rare input combination / cosmetic spacing / accessibility

Use P0/P1/P2 (Larixon convention).

### Layer sections

Group test cases under these numbered section headers (skip layers not relevant to the task):

```
## 1. Unit Android — {description}
## 2. Unit iOS — {description}
## 3. Unit KMP — {shared business logic, if applicable}
## 4. Integration Android — {screen / flow}
## 5. Integration iOS — {screen / flow}
## 6. E2E UI Android — {full journey, if applicable}
## 7. E2E UI iOS — {full journey, if applicable}
## 8. Smoke — {post-deploy manual check}
```

When a task is Android-only or iOS-only, keep only the relevant platform sections. For KMP-shared logic, prefer `Unit KMP` + platform-specific integration layers.

Every section opens with:

```markdown
**Цель:** one-sentence purpose of this section.

**Кодовая привязка:**
- Android: `feature-advert-reviews/data/src/commonMain/kotlin/com/larixon/.../AdvertReviewsMapper.kt@toDomain`
- iOS: `Larixon/AdvertReviews/Data/Mappers/AdvertReviewsMapper.swift@toDomain`
```

### Layer classification

- **Unit Android** — pure Kotlin/JUnit 5 / Kotest / MockK. No Context, no UI. Test Mappers, UseCases, ViewModels (state transitions via Turbine).
- **Unit iOS** — pure Swift XCTest or Quick/Nimble. No UIViewController. Test Mappers, UseCases, Presenters.
- **Unit KMP** — `commonTest` source set with Kotest multiplatform runner; test pure business logic shared between Android and iOS.
- **Integration Android** — Compose UI tests (`composeTestRule`) or Espresso against in-process emulator, with `MockWebServer` for network.
- **Integration iOS** — XCUITest or `XCTestCase` with UI host, mock URLSession via protocol stubs.
- **E2E UI Android** / **E2E UI iOS** — full app on real emulator/simulator running against staging or fixture-backed stand; Android `UiDevice` / iOS `XCUIApplication`. Distinct from Smoke.
- **Smoke** — manual post-deploy check on prod-like build; 1-5 minimal steps.

### Coverage rules

- Every screen in scope → at least one Integration case (Android or iOS or both depending on scope)
- Every shared UseCase/Mapper touched → at least one Unit (KMP or platform-specific) case
- Every P0 row in `risk-map.md` → cases referenced by number in the risk table (`Кейсы` column)
- Multi-market behavior: parametric case or per-market cases when locale/currency/feature-flag differs (`bz`, `tj`, `mn`, `ja`, `pn`, `sl`)
- For bug-TD: include E2E UI case reproducing the bug path + Smoke manual case after fix

### Forbidden in `test-matrix.md`

These patterns are rejected — flag them in review:

- Flat-table matrix with columns `| ID | Scenario | Test Level | Priority | ... |` or `| ID | Name | Area | Scenario | Priority | Test Data | Expected Result |` — loses Задача/Действие/Ожидаемый specificity and breaks downstream 013 contract.
- Collapsing Задача/Предусловия/Действие/Ожидаемый into fewer columns — the 6 fields are mandatory per case.
- Emoji in section/case headings (⚠️ ✅ ❌ 🔥 etc.). Use plain-text `[НЕ РЕАЛИЗОВАНО]` label instead.
- ID prefixes (`T-001`, `UT-001`, `IT-001`, `E2E-001`) — use plain sequential numbers.
- Letter suffixes (`17a`) or gaps in numbering.
- `Area` column with internal class names. Name the tested behavior, not the internal class.
- `Layer: Unit Tests (unit-tester)` with parenthetical role name. Layer value is a single token from the fixed enum.
- `Итого` summary table or case-count sidebar at the end of the file. Counts are returned via the publish action, not in the TD body.
- `*Automated by ASGARD*` or any agent signature in the body of `test-matrix.md`.
- Review feedback and rework notes ("⚠️ КРИТИЧЕСКОЕ ИЗМЕНЕНИЕ (rework v2)" sections). Review belongs in Jira/Confluence comments; version bumps go into the title line as `(vN)`.
- Abstract preconditions: `"valid user"`, `"mock OpenAI"`, `"Composable with default state"`. Always factory-syntax with exact values.
