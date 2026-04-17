## Larixon Mobile TD Checklist Additions

### Step Zero: scope guard (mobile vs web)

- [ ] Before generating any TD, verify the feature touches Kotlin (Android) / Swift (iOS) / KMP common code
- [ ] If the feature is implemented **only** in web repositories (`core`, frontend SPA), BLOCK via `/tracker-blocked` with message: "Задача web-only, передать backend-test-architect. Мобильный test-architect не пишет TD для web-only фич." Do not proceed to write TD.
- [ ] If the feature has TODO()-stubs in the mobile repo but no real implementation, BLOCK and reference upstream developer subtask

### `test-strategy.md` (header of the TD)

- [ ] H1 title follows exact format: `TD {QUARTER} | {TASK_KEY} | {YYYY-MM-DD}` (not `MOB-{KEY}. [ROLE] role` — that title is controlled by the ASGARD publisher)
- [ ] **Ссылки** rendered as numbered table `| # | Описание | Ссылка / Значение |` — at minimum: Jira-таск, Тип, Feature-ветка, Целевые платформы, Экран/Flow, Android ViewModel/UseCase, iOS Presenter/Service, Эндпоинты бэкенда, Существующие тесты
- [ ] **Контекст** starts with **Репозитории и стеки** table (separate rows for Android and iOS when both are affected)
- [ ] **Доменные понятия** glossary table present when the feature introduces non-obvious domain terms (CD-4017 pattern) — optional but recommended for bug-TD
- [ ] If Type=Bug: Контекст contains **Архитектура функционала** (numbered steps 1..N with code refs), **Ключевые детали реализации**, **Точки поломки** (Android / iOS / Backend / KMP hypotheses), **Ограничения** table
- [ ] **Скоуп** has explicit Включено / Исключено lists (платформы, экраны, flows)
- [ ] **Out of scope** present and non-empty
- [ ] **Источники** includes `Confluence (правила TD)`, `Confluence (Mobile QA process)`, `Сильные TD (референсы)` with 2-3 related TDs, and separate bullet lists for Android and iOS code files
- [ ] test-strategy.md contains **no test cases** — those belong in test-matrix.md only (one fact lives in one file)

### `test-matrix.md` (body)

- [ ] Per-case self-contained blocks — NO flat `| ID | Scenario | ... |` matrix anywhere
- [ ] Every case has: **Задача**, **Предусловия**, **Действие**, **Ожидаемый результат**, trailing `Priority: P0/P1/P2 | Layer: X | Type: auto-candidate/manual` — the 6 mandatory fields
- [ ] Sequential numbering across ALL sections (1..N); restart per section is forbidden
- [ ] No ID prefixes (`T-`, `UT-`, `IT-`, `E2E-`), no letter suffixes (`17a`), no gaps
- [ ] Each case has markdown checkbox `[ ]` or `[x]` **in the heading** (after `###`), never after list-marker `*`/`-`
- [ ] `[x]` cases have `Реализован: TestClass::testMethodName` (Android) or `TestSpec::"scenario"` / `TestClass.testMethodName` (iOS) below the heading
- [ ] `[ ]` cases with existing close-but-inexact coverage have `Частично покрыт: test_name` line below the heading
- [ ] `[НЕ РЕАЛИЗОВАНО]` plain-text label in heading when production code is not yet written
- [ ] No emoji in headings (⚠️ ✅ ❌ 🔥) — use plain-text labels
- [ ] `Предусловия` use factory syntax (`UserFactory.create()`, `AdvertFactory.create()`) — never abstract descriptions like "valid user" or "mock OpenAI"
- [ ] `Действие` includes exact method call (Unit) or exact UI steps with selectors / accessibility IDs (Integration / E2E). Integration/E2E `Действие` does NOT reference internal class names.
- [ ] `Ожидаемый результат` has exact values (state values, `onNodeWithText(...).assertIsDisplayed()`, `app.buttons["Submit"].exists == true`) — no "correct" / "as expected" / "работает"
- [ ] Parametric cases use table-inside-case (CD-1319 pattern) for 4+ combinations OR Kotest `withData` IDs (STM-65 pattern) for 2-3
- [ ] Each layer section opens with **Цель** + **Кодовая привязка** (with both Android and iOS paths when both are affected)
- [ ] Layer is a single token from the fixed enum: `Unit Android`, `Unit iOS`, `Unit KMP`, `Integration Android`, `Integration iOS`, `E2E UI Android`, `E2E UI iOS`, `Smoke` — no parenthetical role name
- [ ] E2E UI layer is separate from Smoke (both present only when relevant)
- [ ] For cross-platform features: separate sections for Unit Android / Unit iOS / Unit KMP (when shared) / Integration Android / Integration iOS
- [ ] **No `Итого` summary table** at end of test-matrix.md — counts are returned by publish action, not in TD body
- [ ] **No `*Automated by ASGARD*`** or other agent signature in the body
- [ ] **No rework/review notes** ("⚠️ rework v2" sections) — review belongs in Jira comments; version bumps go into test-strategy.md title line as `(vN)`

### `risk-map.md`

- [ ] Main table: `| Риск | Приоритет | Источник | Кейсы | Платформа |` — `Приоритет` matches test-matrix priority (P0/P1/P2), `Источник` labels origin (ТЗ / Побочный эффект / Граничный случай / Регрессия), `Кейсы` references case numbers, `Платформа` = Android / iOS / both
- [ ] Separate tables for **Усилители риска** and **Регрессионные риски** when applicable
- [ ] Total length ≤ 1 page (~60 lines) — no HIGH/MEDIUM/LOW governance sub-documents

### `test-data-strategy.md`

- [ ] Android: `UserFactory.create(...)`, `AdvertFactory.create(...)`, `TestFixtures.loadJson(...)`, MockWebServer dispatcher syntax
- [ ] iOS: `UserFactory.user(...)`, `AdvertFactory.advert(...)`, `URLProtocol` stub or Cuckoo/Mockito-Swift
- [ ] KMP: `commonTest` helpers listed with `expect`/`actual` overrides when needed
- [ ] Feature flags: `FakeFeatureFlags(GDPR_GOOGLE = true)` with market-specific values
- [ ] Multi-market fixtures: one fixture per affected market (`bz`, `tj`, `mn`, `ja`, `pn`, `sl`)
- [ ] No duplication with test-strategy.md or test-matrix.md — one fact per file

### `coverage-targets.md`

- [ ] Per-module table: `Module | Class/Method | Risk | Target Lines | Target Branches | Justification`
- [ ] Modules not touched in feature branch labelled `no change`
- [ ] Coverage tool named: Kover (Android), `xccov` (iOS)
- [ ] No Gradle command strings — CI execution belongs to merge/devops flow, not test-architect

### Confluence publication (not authored by agent)

- [ ] `{toc}` macro is injected by the ASGARD publisher — do not insert it manually in any of the 5 files
- [ ] `## {filename.md}` H2 headers are prepended by the publisher — do not repeat the file name inside the file

### Role assignments (Jira comment)

- [ ] Android Allure project: `https://larixon.testops.cloud/project/69/launches`
- [ ] iOS Allure project: `https://larixon.testops.cloud/project/168/launches`
- [ ] `td-allure-sync` triggered after TD approval
- [ ] Bamboo plan keys (AD-AT / AD-IN / ID-II) appear only in the Источники section of test-strategy.md; tests do not start or trigger Bamboo from within the TD
- [ ] Downstream roles: `unit-tester` (mobile), `integ-tester` (mobile), `manual-tester` (platform). Do NOT redefine manual-tester behavior — only describe what is passed to it via standard platform `060-downstream-guidance.md`
