## Larixon Mobile Test Design — Output Rules

Platform slot `050-output-format.md` (locked) mandates 5 files in `production-documentation/task-{TASK_KEY}/`. This slot defines what each file must contain so the Confluence-published TD reads coherently and each file stays compact.

**Anti-reference:** MOB-802 / MOB-795 / MOB-750 multi-document format with separate `downstream-guidance.md`, `rework v2 critical change` narratives, governance promises and boundary matrices. The 5 files go to git per locked 050, but each file stays compact and focused per the templates below. Do not produce cross-document rules, boundary matrices, block lists, or governance promises.

### Output model: 5 compact non-overlapping files

Goal: 5 files with no content duplication. Each fact lives in exactly one file. Cross-reference via `См. test-strategy.md §Контекст` if another file needs to point at it. Do **not** merge everything into `test-strategy.md` or produce stubs — the ASGARD publisher reads all 5 and composes the Confluence page.

- `test-strategy.md` — Ссылки (table), Репозитории/стеки, Контекст, [Архитектура+Точки поломки+Ограничения for bugs], Scope, Out of scope, Источники. **No test cases.**
- `test-matrix.md` — every test case (case-block format from slot `035-test-matrix.md`). **Only cases.**
- `risk-map.md` — compact `Риск | Приоритет | Источник | Кейсы | Платформа` table + Усилители + Регрессия. **Only risks.**
- `test-data-strategy.md` — factories, fixtures, feature-flag setups, multi-market data. **Only data.**
- `coverage-targets.md` — per-module targets table (Kover for Android, xccov for iOS). **Only coverage numbers.**

The ASGARD publisher composes the Confluence page by prepending `## {filename}` H2 headers to each file's content and injecting `{toc}` at the top. **Do not insert `{toc}` manually** and do **not** repeat the file name inside the file body.

The Confluence page title is set by the publisher as `MOB-{KEY}. [ROLE] role` — we do **not** control it. The title you author inside `test-strategy.md` (`TD {QUARTER} | {KEY} | {date}`) is the content heading, separate from the Confluence page title.

### Step Zero: mobile scope guard

Before starting any TD, verify the feature actually touches mobile code (Kotlin / Swift / KMP common). Check:

1. Is there a real change in `classifieds-android-app` or `classifieds-ios-app` beyond TODO()-stubs?
2. Are there `@Composable` screens, ViewModels, UseCases, or iOS views/presenters being added or modified?
3. Does the Jira parent task ux-spec include native platforms, or is it flagged as web-only (e.g. "Нативные приложения — вне скоупа")?

If the answer to all three is NO — the feature is web-only:
- BLOCK via `/tracker-blocked` with message: `"Задача web-only по ux-spec — мобильный TD неприменим. Задача должна быть отменена или переназначена на backend-test-architect."`
- Do NOT write a TD with `НЕПРИМЕНИМО` sections, `Что тестировать = НИЧЕГО`, or rework narratives in the body. The block goes into Jira, not into TD files.
- Do NOT redefine behavior of other roles (`manual-tester`, `product`) — only describe what is blocked.

### Scope

- Android repo: `/Users/permi/classifieds-android-app`
- iOS repo: `/Users/permi/classifieds-ios-app`
- Feature branch = Jira ticket (e.g. `MOB-780`, `AT-243`). Analyze the **feature branch**, not `master`. If branch not specified — BLOCK and ask.

### Test layers → downstream routing

| Layer | Covers | Downstream role |
| --- | --- | --- |
| Unit Android | Kotlin pure logic — mappers, usecases, viewmodels | `unit-tester` (Android) |
| Unit iOS | Swift pure logic — mappers, usecases, presenters | `unit-tester` (iOS) |
| Unit KMP / common | shared business logic in `commonTest` | `unit-tester` (KMP) |
| Integration Android | Compose / Espresso test rule + MockWebServer on emulator | `integ-tester` (Android) |
| Integration iOS | XCTest with stubbed URLSession on simulator | `integ-tester` (iOS) |
| E2E UI Android | full-app user journey on emulator | `integ-tester` (Android, E2E mode) |
| E2E UI iOS | full-app user journey on simulator | `integ-tester` (iOS, E2E mode) |
| Smoke | manual post-deploy check | manual tester |

**E2E UI is distinct from Smoke**: E2E UI = automated full-app journey; Smoke = manual post-deploy verification. Each scenario goes to exactly one layer. See CD-4653 for the canonical split.

### Prioritization

| Priority | Meaning |
| --- | --- |
| P0 | Critical business flow / crash path / auth / regression in public contract |
| P1 | Important secondary flow / error state / empty state / i18n plurals |
| P2 | Edge case / rare input / cosmetic spacing / accessibility |

Use P0/P1/P2 consistently.

### Markets (product flavors / iOS targets)

| Market | Android flavor | iOS target | Locale | Currency | Notes |
| --- | --- | --- | --- | --- | --- |
| Bazaraki | `bz` | `Bazaraki` | en-CY | EUR | `GDPR_GOOGLE` enabled |
| Somon.tj | `tj` | `Somon.tj` | tg-TJ | TJS | — |
| Unegui.mn | `mn` | `Unegui.mn` | mn-MN | MNT | `EMONGOLIA_ENABLED` |
| Jacars | `ja` | `Jacars` | en-JM | JMD | — |
| Pin.tt | `pn` | `Pin.tt` | en-TT | TTD | — |
| Salanto | `sl` | `Salanto` | en-CY | EUR | — |

Include market-specific rows when behavior differs per locale / currency / feature flag.

---

## File content templates

### `test-strategy.md` — header of the TD

Sections in this exact order:

```markdown
# TD {QUARTER} | {TASK_KEY} | {YYYY-MM-DD}

## Ссылки

| # | Описание | Ссылка / Значение |
| --- | --- | --- |
| 1 | Jira-таск | https://larixon.atlassian.net/browse/{TASK_KEY} |
| 2 | Тип | Bug (Priority: High) / Feature / Enhancement |
| 3 | Feature-ветка | `{TASK_KEY}` |
| 4 | Целевые платформы | Android / iOS / both |
| 5 | Экран / Flow | `AdvertReviewsScreen` / `Seller cabinet` |
| 6 | Android: ViewModel / UseCase | `feature-advert-reviews/.../RatingViewModel.kt` |
| 7 | iOS: Presenter / Service | `Larixon/AdvertReviews/.../RatingPresenter.swift` |
| 8 | Эндпоинты (бэкенд) | `GET /api/v2/apps/adverts/{id}/reviews/` |
| 9 | Существующие тесты (до задачи) | `RatingViewModelTest` / `RatingPresenterSpec` или `— отсутствуют` |
| ... | ... | ... |

## Контекст

### Репозитории и стеки

| Репозиторий | Роль | Фреймворк | Тестовый стек | Сборщик |
| --- | --- | --- | --- | --- |
| `classifieds-android-app` | Android app | Kotlin + Compose + KMP | JUnit 5 / Kotest / MockK / Turbine / Kover | Gradle |
| `classifieds-ios-app` | iOS app | Swift + UIKit + SwiftUI | XCTest / Quick / Nimble | CocoaPods |

### {краткое описание фичи, 1-3 абзаца}

Для bug-TD (Type=Bug) секция Контекст обязательно содержит дополнительно:

- **Архитектура функционала** — пронумерованные шаги потока (1..N) с точными ссылками на код (`module/file.kt:line — ClassName.method()`)
- **Ключевые детали реализации** — поля DTO / маппер / ViewModel state / feature flag (bullet list)
- **Точки поломки** — гипотезы где именно ломается, с разделением по платформе (Android / iOS / Backend / shared KMP)
- **Ограничения** — таблица `Параметр | Значение | Статус`, где Статус = Подтверждено кодом / [УТОЧНИТЬ]

### Скоуп

- **Включено:** что тестируем (платформы, экраны, flows)
- **Исключено:** что не тестируем (например, другие платформы, миграции на Compose, отдельные задачи)

## Out of scope

- {явный список исключений}

## Источники

- Jira: {url}
- Confluence (правила TD): https://larixon.atlassian.net/wiki/spaces/itdep/pages/3591733264
- Confluence (Mobile QA process): https://larixon.atlassian.net/wiki/spaces/It1/pages/3531276289
- **Сильные TD (референсы):** {2-3 related TDs this was built from}
- Кодовые файлы Android: {bullet list}
- Кодовые файлы iOS: {bullet list}
- Feature-ветка: `{TASK_KEY}`
```

### `test-matrix.md` — the body of the TD

See slot `035-test-matrix.md` for the full format. Summary:

- Per-case self-contained blocks, NOT a flat `| ID | Scenario | Test Level | ... |` table (reject platform default and MOB-795 / MOB-775 format)
- Sequential numbering across ALL sections (1, 2, 3…); no prefixes (`T-`, `UT-`, `IT-`, `E2E-`), no suffixes (`17a`), no gaps
- Each case: **Задача / Предусловия / Действие / Ожидаемый результат / Priority | Layer | Type** — the 6 mandatory fields
- Markdown checkbox `[ ]` / `[x]` in the case heading (after `###`), never after list marker
- `Реализован: TestClass::testMethodName` (Android) or `TestSpec::"scenario"` / `TestClass.testMethodName` (iOS) under the heading for `[x]` cases
- `Частично покрыт: test_name` marker for close-but-inexact coverage
- `[НЕ РЕАЛИЗОВАНО]` plain-text label in heading when production code is not yet written
- Parametric cases: table-inside-case (CD-1319 pattern) for 4+ combinations OR Kotest `withData` IDs (STM-65 pattern) for 2-3

### `risk-map.md` — compact risk→cases table

```markdown
| Риск | Приоритет | Источник | Кейсы | Платформа |
| --- | --- | --- | --- | --- |
| Крэш экрана отзывов при пустом avg_rating | P0 | ТЗ | 4, 28, 52 | Android + iOS |
| Регрессия: сортировка "recent" больше не дефолт | P0 | Регрессия | 25, 54 | Android + iOS |
| Локализация label ngettext для mn-MN | P1 | Граничный случай | 7, 31 | Android |

## Усилители риска

- {list of amplifiers that bumped a risk one level up — e.g. "затрагивает KMP common module", "новый depending module"}

## Регрессионные риски

- {existing flows or contracts that could break}
```

`Приоритет` matches the `Priority` of the referenced cases in `test-matrix.md`. `Источник` labels origin (ТЗ / Побочный эффект / Граничный случай / Регрессия). `Кейсы` uses case numbers only.

Keep total length ≤ 1 page (~60 lines) — no governance/HIGH-MEDIUM-LOW sub-documents with multi-section narrative (MOB-802 anti-pattern).

### `test-data-strategy.md` — fixtures + permission matrix

- Android: `UserFactory.create(...)`, `AdvertFactory.create(reviewsCount = 3)`, `TestFixtures.loadJson("advert_reviews.json")`, `MockWebServer.enqueue(MockResponse())`
- iOS: `UserFactory.user()`, `AdvertFactory.advert(reviewsCount: 3)`, stub of `URLProtocol` returning bundled JSON
- KMP `commonTest`: `expect`/`actual` test helpers in `commonTest` with platform-specific overrides if needed
- Feature flags: `FakeFeatureFlags(GDPR_GOOGLE = true)` per market
- Multi-market fixtures: one fixture per market with expected locale-formatted copies

### `coverage-targets.md` — per-module targets

| Module | Class / Method | Risk | Target Lines | Target Branches | Justification |
| --- | --- | --- | --- | --- | --- |
| `feature-advert-reviews/data` | `AdvertReviewsMapper.toDomain` | HIGH | 100% | 100% | Pure function — exhaustive coverage |
| `feature-advert-reviews/domain` | `SubmitReviewUseCase.invoke` | HIGH | ≥ 90% | ≥ 85% | Critical path + validation branches |
| `feature-advert-reviews/presentation` | `RatingViewModel.submitPressed` | MEDIUM | ≥ 80% | ≥ 75% | State machine |

Modules not modified in the feature branch → `no change`. Coverage measured via Kover (Android) / `xccov` (iOS).

---

## Test case format

Every case in `test-matrix.md` MUST follow the exact shape specified in slot `035-test-matrix.md`: Задача / Предусловия / Действие / Ожидаемый результат / `Priority | Layer | Type`, with markdown checkbox `[ ]` / `[x]` in the case heading and `Реализован:` line below for `[x]` cases.

Factory / fixture references:
- Android unit: `UserFactory.create()`, `AdvertFactory.create()`, MockK `every { ... } returns ...`
- iOS unit: `UserFactory.user()`, `AdvertFactory.advert()`, `stub(sut) { ... }` with Cuckoo/Mockito-Swift
- Integration Android: `composeTestRule.setContent { }` + `onNodeWithText(...)` + MockWebServer dispatcher
- Integration iOS: `XCUIApplication().launch()` + `app.buttons["Submit"].tap()`
- E2E Android: `UiDevice.getInstance(InstrumentationRegistry.getInstrumentation())` + permission grant
- E2E iOS: `XCUIApplication` + interruption monitor

### Layer section headers

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

Skip layers not relevant to task scope. Android-only or iOS-only features keep only relevant platform sections.

Every section opens with **Цель** + **Кодовая привязка** (with both Android and iOS paths when both are affected).

---

## Reference TDs

Team-canonical human TDs to match verbatim (web, but structural rules transfer 1:1 to mobile):

- [STM-68 (feature, reviews page endpoint)](https://larixon.atlassian.net/wiki/spaces/It1/pages/4222976017)
- [STM-65 (feature, listings + new ordering)](https://larixon.atlassian.net/wiki/spaces/It1/pages/4219404307)
- [STM-101 (feature, settings-driven field)](https://larixon.atlassian.net/wiki/spaces/It1/pages/4317675552)
- [CD-4653 (bug, file upload, multi-layer, E2E UI vs Smoke split)](https://larixon.atlassian.net/wiki/spaces/It1/pages/4290707498)
- [CD-1319 (bug, parametric table-inside-case)](https://larixon.atlassian.net/wiki/spaces/It1/pages/4326391810)
- [CD-4017 (bug, multi-layer, Доменные понятия + Источник column)](https://larixon.atlassian.net/wiki/spaces/It1/pages/4320985141)

**Anti-reference:** MOB-802 multi-document AI format with `test-strategy.md §3.1-§3.7 rules`, `downstream-guidance.md`, `cross-role boundary matrix`, `block list of 12 dependencies`, `governance promise`. Do not produce these documents.

---

## Language

- Jira comment follows English platform template (locked slot 050).
- All 5 output files use **Russian field names**: Задача, Предусловия, Действие, Ожидаемый результат, Ссылки, Контекст, Риски и приоритеты, Out of scope, Источники, Итого.
- Case titles may mix Russian and English code identifiers naturally: `avg_rating=null → крэш экрана`.

## Downstream sync

- Android TDs → Allure TestOps project `https://larixon.testops.cloud/project/69/launches` via `td-allure-sync`
- iOS TDs → Allure TestOps project `https://larixon.testops.cloud/project/168/launches` via `td-allure-sync`
- CI execution: Bamboo plans `AD-AT` / `AD-IN` (Android), `ID-II` (iOS) — triggered by merge/devops flow, NOT by test-architect
