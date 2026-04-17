## Test Matrix Design

### File: `test-matrix.md`

This file is the bulk of the test design. It is **NOT a flat table**. It contains self-contained test case blocks grouped by layer, following the Larixon team convention (see reference TDs in `200-larixon-web-td.md`).

Reject MOB-802-style `| ID | Scenario | Test Level | Priority | ... |` flat matrix — it loses Действие/Ожидаемый specificity and is incompatible with downstream 013 contract.

### Per-case block template

```markdown
### N [ ] {title — describes behavior, not implementation}

Реализован: `test_file.py::TestClass::test_method`
   (omit this line when the case is not yet written)

**Задача:** one sentence — what behavior this proves.

**Предусловия:**
- `rubric = f.rubric(collect_reviews_enabled=True)` — exact factory calls with values
- `advert = f.advert(rubric=rubric, reviews_count=3, avg_rating=4.5)`
- `settings.SETTING_NAME = value` via `override_settings` when applicable

**Действие:** exact call (HTTP or method).
- Integration: `GET /api/v2/spa/advert/{advert.id}/reviews/?sort=rating_high`
- Unit BE: `GetAdvertReviewsInfo(advert_id=advert.id, user_id=None)()`
- E2E UI: step-by-step selectors + clicks

**Ожидаемый результат:** exact observable values.
- HTTP 200; `response.json["count"] == 3`; `response.json["advert"]["lead_id"] is None`
- NOT "correct", "as expected", "работает" — always exact values

Priority: P0 | Layer: Unit BE | Type: auto-candidate
```

### Case status markers

Each case heading carries a markdown checkbox in the heading itself (after `###`), never after a list marker:

- `### N [ ] Title` — case **not yet implemented**. Omit `Реализован:` line.
- `### N [x] Title` — case **implemented**. MUST include `Реализован: test_file.py::TestClass::test_method` line under the heading.
- `### N [ ] Title` with `Частично покрыт: test_name` line below — existing test covers the area but not this exact scenario. Downstream tester still writes a new test; partial coverage is acknowledged in the Jira comment.
- `### N [ ] Title [НЕ РЕАЛИЗОВАНО]` — production code itself is not yet written. No test can be written against nonexistent code. Downstream tester leaves `[ ]`, blocks on the developer, notes in Jira.

**Forbidden combinations:**
- `* [ ]` / `- [ ]` / `* [x]` / `- [x]` — list-marker + checkbox is a Confluence-task anti-pattern. Checkbox goes **only** in the case heading.
- Using `[x]` without `Реализован:` line — checkbox without evidence of the test location.
- Using `Реализован:` with `[ ]` — contradiction; if test exists, checkbox is `[x]`.

### Rules

- **Sequential numbering across ALL sections** (1, 2, 3… — do NOT restart per section). See CD-4653 for a canonical example (cases 1..30 across 4 layers).
- **Hierarchical sub-numbering is OK** inside a section (1.1, 1.2 — see STM-68) but the top-level counter still increments globally. Pick one convention per TD and stick with it.
- No ID prefixes (no `T-`, `UT-`, `IT-`, `E2E-`). No letter suffixes (`17a`). No gaps.
- `Предусловия` MUST use project factory syntax: `f.user()`, `f.rubric(...)`, `f.advert_lead(advert=advert, user_id=user.id)`. Never abstract descriptions like "a valid user", "Serializer instance", "mock: 500 response".
- `Действие` for Integration/E2E: exact external contract (HTTP method + path + query params OR UI step with DOM selector). **Do NOT reference internal class names** — e.g. write `GET /api/v2/spa/advert/{id}/reviews/`, not `AdvertReviewsView.get()`.
- `Действие` for Unit BE: exact method call with arguments (internal class names are OK at Unit level — the unit under test IS the class).
- `Ожидаемый результат` MUST include exact values: `HTTP 200`, `field == value`, `Model.objects.count() == 1`, `response.json["key"] == null`.
- Case title MUST be parseable by `tester-skills-mcp` as a `Name` column entry (single line, ≤120 chars, no Markdown bold/italic).

### Parametric cases

Two acceptable patterns:

**A. pytest-parametrize (2-3 combinations):**

```markdown
### 12 [x] map_review_item: даты "сегодня/вчера/раньше" → корректные ключи date_label

Реализован: `test_advert_reviews_mappers.py::TestMapReviewItem::test_date_label[2026-03-09 10:30:00-Today, 10:30]`,
            `test_date_label[2026-03-08 13:59:00-Yesterday, 13:59]`,
            `test_date_label[2026-03-07 05:03:00-07.03.2026, 05:03]`

**Задача:** проверить форматирование date_label для today / yesterday / older.

**Предусловия:** `freezer.move_to("2026-03-09 15:00")`, 3 `UserReview` с разными `created_at`.

**Действие:** для каждого значения `created_at` вызвать `map_review_item(review, reasons_map={})`.

**Ожидаемый результат:**
- today 10:30 → `"Today, 10:30"`
- yesterday 13:59 → `"Yesterday, 13:59"`
- older → `"07.03.2026, 05:03"`

Priority: P1 | Layer: Unit BE | Type: auto-candidate
```

**B. Table inside the case (CD-1319 pattern — 4+ combinations):**

```markdown
### 1 [ ] Параметрический: смена только account_type (user_type не трогаем)

**Задача:** проверить поведение user_type при смене account_type.

**Предусловия:** пользователь открыт в Django Admin; user_type не изменяется.

**Действие:** в Django Admin сменить account_type на значение из колонки «Новый account_type», сохранить.

| # | Предусловия | Новый account_type | Ожидаемый user_type | Комментарий |
| --- | --- | --- | --- | --- |
| 1 | account_type=business_fixed, user_type=real estate | business_fixed_premium | real estate (сохранился) | Переход внутри allowed |
| 2 | account_type=business_fixed, user_type=default | business | default (сброшен) | Переход из allowed в не-allowed |
| 3 | account_type=business, user_type=default | business_fixed | default (не выставляется) | Переход из не-allowed в allowed |
| 4 | account_type=business, user_type=real estate (legacy) | business_fixed | real estate (сохранился) | Переход из не-allowed в allowed, legacy user_type |

Priority: P0 | Layer: Unit BE | Type: auto-candidate
```

Pattern B keeps the case count low while covering the combinatorial space. Use the `#` column to give each row its own addressable id within the case.

### Priority rules

- **P0**: critical business / core user flow / regression in existing contract / auth/permission checks / data mutation outcomes
- **P1**: important secondary flow / error codes from api-contract / core business logic / i18n ngettext
- **P2**: edge case / optional field / pagination / filter combinations / multi-market variant / cosmetic consistency

Use P0/P1/P2 consistently. Do NOT use P1/P2/P3 — Larixon convention is P0-P2.

### Layer sections

Group test cases under these numbered section headers (skip layers not relevant):

```
## 1. Unit BE — {what is tested}
## 2. Integration — {endpoint or flow}
## 3. Integration DB — {model constraint tests, if applicable}
## 4. Integration Contract — {cross-repo contract checks, if applicable}
## 5. E2E — {headless multi-step flow, if applicable}
## 6. E2E UI — {browser screen / admin page, if applicable}
## 7. Smoke — {post-deploy manual checks, if applicable}
```

Every section opens with:

```markdown
**Цель:** one-sentence purpose of this section.

**Кодовая привязка:** `module/path.py:line — ClassName.method()`
```

### Layer classification

- **Unit BE** — pure Python, no DB, no HTTP. Mock ORM, mock external services. Test service methods, mapper functions, validators.
- **Integration** — single-endpoint through Django test client (`APIClient`, `Client`), real test DB. Test one URL end-to-end including auth, serialization, DB state.
- **Integration DB** — optional; model constraints, migrations, transaction behavior (`transaction=True`, `select_for_update`). Only when the task modifies DB constraints.
- **Integration Contract** — cross-repo contract checks. Use when `test-strategy.md § API-контракты (cross-repo)` has at least one row with `Статус контракта = Расхождение`. One case per diverged endpoint. Assert exact field names, types, nesting, pagination shape against the frontend's expected shape (not just HTTP status). Downstream: `backend-integ-tester`.
- **E2E** — headless multi-step flow across endpoints or API-only end-to-end scenarios. Use when no browser is required.
- **E2E UI** — Playwright-driven browser test with DevTools Network/Console verification. Use for admin screens, critical user flows, bug-reproductions that need real browser. **Distinct from Smoke** — see CD-4653 for the canonical split.
- **Smoke** — manual post-deploy check. 1-5 minimal checks to verify the feature is live.

### Coverage rules

- Every endpoint in scope → at least one Integration case
- Every P0 row in `risk-map.md` → cases referenced by number in the risk table (`Кейсы` column)
- Every service method changed → at least one Unit BE case
- Backward compatibility: when existing endpoints are modified, add explicit regression case under Integration (see CD-4653 case 2.3 "регрессия")
- Cross-repo contract: every `Расхождение` row in `test-strategy.md § API-контракты (cross-repo)` → at least one Integration Contract case asserting the exact expected shape
- For bug-TD: include one E2E UI case that reproduces the original bug path before the fix, and one Smoke manual case after the fix

### Forbidden in `test-matrix.md`

These patterns are rejected — flag them in review:

- Flat-table matrix with columns `| ID | Scenario | Test Level | Priority | ... |` or `| ID | Name | Area | Scenario | Priority | Test Data | Expected Result |` — loses Задача/Действие/Ожидаемый specificity and breaks downstream 013 contract.
- Collapsing Задача/Предусловия/Действие/Ожидаемый into fewer columns — the 6 fields are mandatory per case.
- Emoji in section/case headings (⚠️ ✅ ❌ 🔥 etc.). Use plain-text `[НЕ РЕАЛИЗОВАНО]` label instead.
- ID prefixes (`T-001`, `UT-001`, `IT-001`, `E2E-001`) — use plain sequential numbers.
- Letter suffixes (`17a`) or gaps in numbering.
- `Area` column with internal class names (`PromptBuilder`, `InputSanitizer`). Name the tested behavior, not the internal class.
- `Layer: Unit Tests (backend-unit-tester)` with parenthetical role name. Layer value is a single token from the fixed enum.
- `Итого` summary table or case-count sidebar at the end of the file. Counts are returned via `action_td_publish`, not in the TD body.
- `*Automated by ASGARD*` or any agent signature in the body of `test-matrix.md`.
- Review feedback and rework notes ("⚠️ КРИТИЧЕСКОЕ ИЗМЕНЕНИЕ (rework v2)" sections). Review belongs in Jira/Confluence comments; version bumps go into the title line as `(vN)`.
- Abstract preconditions: `"Serializer instance"`, `"a valid user"`, `"mock: 500 response"`, `"body: {title, category_id: valid}"`. Always factory-syntax with exact values.
