## Larixon TD Checklist Additions

### `test-strategy.md` (header of the TD)

- [ ] H1 title follows exact format: `TD {QUARTER} | {TASK_KEY} | {YYYY-MM-DD}` (not `MOB-{KEY}. [ROLE] role` — that title is controlled by the ASGARD publisher)
- [ ] **Ссылки** rendered as numbered table `| # | Описание | Ссылка / Значение |` — at minimum: Jira-таск, Тип, Feature-ветка, Endpoint, View/Service, Существующие тесты
- [ ] **Контекст** starts with **Репозитории и стеки** table (`Репозиторий | Роль | Фреймворк | Тестовый стек | Сборщик`)
- [ ] **Доменные понятия** glossary table present when the feature introduces non-obvious domain terms (CD-4017 pattern) — optional but recommended for bug-TD
- [ ] If Type=Bug: Контекст also contains **Архитектура функционала** (numbered steps 1..N with code refs), **Ключевые детали реализации**, **Точки поломки** (Frontend/Backend hypotheses), **Ограничения** table
- [ ] **Скоуп** has explicit Включено / Исключено bullet lists
- [ ] **Out of scope** section is present and non-empty
- [ ] **Источники** at bottom includes `Confluence (правила TD)`, `Confluence (Test Design)`, `Confluence (Template for TD)`, `Сильные TD (референсы)` with 2-3 related TDs
- [ ] test-strategy.md contains **no test cases** — those belong in test-matrix.md only (one fact lives in one file)
- [ ] **Репозитории и стеки** lists only repos with active changes on the feature branch — not all platform-configured repos
- [ ] When Репозитории и стеки contains both a `backend` row AND any `frontend-*` row, test-strategy.md includes an **API-контракты (cross-repo)** subsection with `Endpoint | Backend repo | Frontend repo | Статус контракта | api-contract ref` table
- [ ] Every row with `Статус контракта = Расхождение` has at least one matching Integration Contract case in test-matrix.md
- [ ] API-контракты subsection is **absent** when task is single-repo (backend-only or frontend-only) — do not fabricate cross-repo rows

### `test-matrix.md` (body)

- [ ] Per-case self-contained blocks — NO flat `| ID | Scenario | ... |` matrix anywhere
- [ ] Every case has: **Задача**, **Предусловия**, **Действие**, **Ожидаемый результат**, trailing `Priority: P0/P1/P2 | Layer: X | Type: auto-candidate/manual` — the 6 mandatory fields
- [ ] Sequential numbering across ALL sections (1..N); restart per section is forbidden
- [ ] No ID prefixes (`T-`, `UT-`, `IT-`, `E2E-`), no letter suffixes (`17a`), no gaps
- [ ] Each case has markdown checkbox `[ ]` or `[x]` **in the heading** (after `###`), never after list-marker `*`/`-`
- [ ] `[x]` cases have `Реализован: test_file.py::TestClass::test_method` line below the heading
- [ ] `[ ]` cases with existing close-but-inexact coverage have `Частично покрыт: test_name` line below the heading
- [ ] `[НЕ РЕАЛИЗОВАНО]` plain-text label in heading when production code is not yet written
- [ ] No emoji in headings (⚠️ ✅ ❌ 🔥) — use plain-text labels
- [ ] `Предусловия` use factory syntax `f.user(...)`, `f.rubric(...)`, `f.advert(...)` — never abstract descriptions like "Serializer instance", "valid user", "mock: 500 response"
- [ ] `Действие` includes exact HTTP method+path (Integration/E2E) or exact method call with args (Unit BE). Integration/E2E `Действие` does NOT reference internal class names.
- [ ] `Ожидаемый результат` has exact values (HTTP code, field == value, count == N) — no "correct" / "as expected" / "работает"
- [ ] Parametric cases use table-inside-case (CD-1319 pattern) for 4+ combinations OR pytest-parametrize ID list (STM-65 pattern) for 2-3
- [ ] Each layer section opens with **Цель** + **Кодовая привязка** (`module/path.py:line — method()`)
- [ ] Layer is a single token from the fixed enum: `Unit BE`, `Unit FE`, `Integration`, `Integration DB`, `Integration Contract`, `E2E`, `E2E UI`, `Smoke` — no parenthetical role name
- [ ] E2E UI layer is separate from Smoke (both present only when relevant)
- [ ] **No `Итого` summary table** at end of test-matrix.md — counts are returned by publish action, not in TD body
- [ ] **No `*Automated by ASGARD*`** or other agent signature in the body
- [ ] **No rework/review notes** ("⚠️ rework v2" sections) — review belongs in Jira comments; version bumps go into test-strategy.md title line as `(vN)`

### `risk-map.md`

- [ ] Main table: `| Риск | Приоритет | Источник | Кейсы |` — `Приоритет` matches test-matrix priority (P0/P1/P2), `Источник` labels the origin (ТЗ / Побочный эффект / Граничный случай / Регрессия), `Кейсы` references case numbers
- [ ] Separate tables for **Усилители риска** and **Регрессионные риски** when applicable
- [ ] Total length ≤ 1 page (~60 lines) — no governance/HIGH-MEDIUM-LOW sub-documents with narrative

### `test-data-strategy.md`

- [ ] Factory syntax throughout: `f.user()`, `f.voucher(active=True, amount=100)`
- [ ] Permission matrix section: Anonymous / Owner / Other user / Admin → which cases use each
- [ ] Multi-market section when feature touches locale/currency: `@override_settings(SETTINGS_MODULE="settings.bazaraki")` + fixtures per market
- [ ] External mocks enumerated: Firebase, Redis, ClickHouse, default_storage — with patch targets
- [ ] No duplication with test-strategy.md or test-matrix.md — one fact per file

### `coverage-targets.md`

- [ ] Per-module table: `Module | Class/Method | Risk | Target Lines | Target Branches | Justification`
- [ ] Modules not touched in feature branch labelled `no change` (no artificial targets)
- [ ] `# pragma: no cover` candidates listed with justification

### Confluence publication (not authored by agent)

- [ ] `{toc}` macro is injected by the ASGARD publisher — do not insert it manually in any of the 5 files
- [ ] `## {filename.md}` H2 headers are prepended by the publisher — do not repeat the file name inside the file

### Role assignments (Jira comment)

- [ ] Every case has an implicit downstream assignment via its Layer; Jira comment's Downstream Guidance breaks counts by role (backend-unit-tester / backend-integ-tester / frontend-unit-tester / e2e-tester)
- [ ] Allure sync triggered via `td-allure-sync` (project `https://larixon.testops.cloud/project/1/launches`)
