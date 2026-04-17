## Larixon Web Test Design — Output Rules

Platform slot `050-output-format.md` (locked) mandates 5 files in `production-documentation/task-{TASK_KEY}/`. This slot defines the **content rules** each file must follow so the Confluence-published TD reads coherently and each file stays compact.

### Output model: 5 compact non-overlapping files

Goal: 5 files with no content duplication. Each fact lives in exactly one file. Cross-reference via `См. test-strategy.md §Контекст` if another file needs to point at it. Do **not** try to merge everything into `test-strategy.md` or produce stubs — the ASGARD publisher reads all 5 and composes the Confluence page.

- `test-strategy.md` — Ссылки (table), Репозитории/стеки, Контекст, [Архитектура+Точки поломки+Ограничения for bugs], Scope, Out of scope, Источники. **No test cases.**
- `test-matrix.md` — every test case (case-block format from slot `035-test-matrix.md`). **Only cases.**
- `risk-map.md` — compact `Риск | Приоритет | Источник | Кейсы` table + Усилители + Регрессия. **Only risks.**
- `test-data-strategy.md` — factories, permission matrix, external mocks, multi-market fixtures. **Only data.**
- `coverage-targets.md` — per-module targets table. **Only coverage numbers.**

The ASGARD publisher composes the Confluence page by prepending `## {filename}` H2 headers to each file's content and injecting `{toc}` at the top. **Do not insert `{toc}` manually** and do **not** repeat the file name inside the file body.

The Confluence page title is set by the publisher as `MOB-{KEY}. [ROLE] role` — we do **not** control it. The title you author inside `test-strategy.md` (`TD {QUARTER} | {KEY} | {date}`) is the content heading, separate from the Confluence page title.

### Scope

- Primary repository: `https://gitlab.dev.larixon.com/larixon-classifieds/web/core` (local: `~/Core`)
- Additional repositories are available via platform `/api/repos` config when the task is cross-repo (e.g. backend `core` + SPA frontend).
- Feature branch = Jira ticket (e.g. `CD-4651`, `STM-68`). Analyze the **feature branch**, not `develop`/`master`. If branch not specified — BLOCK and ask.

### Phase 1.5: Enumerate repos with active changes

Before writing `test-strategy.md`, enumerate which platform-configured repos actually have changes for this feature. Do NOT list all platform repos — only those the task touches.

1. From `architecture.md` (upstream from `architect`) or Jira description, identify candidate repos. Common candidates:
   - `core` — Django backend, and Jinja2/jQuery frontend-legacy embedded in same repo
   - `front-test` — React/Vite SPA frontend (when task touches SPA desktop / mobile-web)
2. For each candidate, check the feature branch diff:
   ```
   git -C {repo_path} diff {default_branch}...{TASK_KEY} --name-only
   ```
   Empty diff → the repo is NOT in scope for this TD (skip it).
3. Role resolution is fixed by platform convention — do NOT re-detect from `package.json`/`manage.py`:

| Repo path | Role(s) possible |
| --- | --- |
| `core/` — Django + Django Ninja / DRF parts | `backend` |
| `core/` — Jinja2 templates + jQuery parts | `frontend-legacy` (only when task modifies these) |
| `front-test/` or SPA repos | `frontend-spa` (React + Vite) |

4. Document ACTIVE repos only in the **Репозитории и стеки** table inside `test-strategy.md § Контекст`. A monorepo (`core`) can appear twice — once per role when both parts are touched.

### Test layers → downstream routing

| Layer | Covers | Downstream role |
| --- | --- | --- |
| Unit BE | service / serializer / model method — no HTTP, no DB | `backend-unit-tester` |
| Unit FE | React component / hook / store / mapper in isolation | `frontend-unit-tester` |
| Integration | single-endpoint through Django test client with real DB | `backend-integ-tester` |
| Integration DB | model constraint / migration behavior (optional, when applicable) | `backend-integ-tester` |
| Integration Contract | cross-repo endpoint contract verification (backend ↔ frontend-* both in scope) | `backend-integ-tester` |
| E2E | headless multi-step flow across endpoints, no browser | `e2e-tester` |
| E2E UI | browser-level Playwright against a running stand | `e2e-tester` |
| Smoke | post-deploy manual check | manual |

**E2E UI is a separate layer from Smoke**: E2E UI = browser automation with DevTools Network/Console checks; Smoke = manual post-deploy acceptance. Each scenario goes to exactly one layer. See CD-4653 for the canonical split.

**`Integration Contract` is triggered only when Репозитории и стеки contains both a `backend` and any `frontend-*` row** — see "API-контракты (cross-repo)" section below.

### Prioritization

| Priority | Meaning |
| --- | --- |
| P0 | Critical business flow / regression in existing contract |
| P1 | Important — significant secondary flow, error codes |
| P2 | Edge case, boundary, multi-market variant |

Use P0/P1/P2 (not P1/P2/P3) — matches the reference Larixon TDs.

### Markets

Include market-specific rows when the feature touches locale, currency, or user-facing content.

| Market | Locale | Currency | Notes |
| --- | --- | --- | --- |
| Bazaraki | EN | EUR | GDPR / Google privacy |
| Somon | RU | TJS | Cyrillic content |
| Unegui | MN | MNT | eMongolia integration |
| Jacars | en_JM | JMD | Car-market specific |
| Pin | en_TT | TTD | Trinidad |
| Salanto | EN | EUR | Verify payment currency |

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
| 4 | Endpoint | `METHOD /api/path/` |
| 5 | View / Service | `module/path.py:line — ClassName.method()` |
| 6 | DTO / Serializer | `module/path.py — SchemaName` |
| 7 | Форма / Модель | `module/path.py:line — FormName` |
| 8 | Существующие тесты (до задачи) | `module/tests.py::TestClass` или `— отсутствуют` |
| ... | ... | ... |

## Контекст

### Репозитории и стеки

List only repos where the feature branch has actual changes (see Phase 1.5 above).

| Репозиторий | Роль | Фреймворк | Тестовый стек | Сборщик |
| --- | --- | --- | --- | --- |
| `~/Core` (backend part) | backend | Django + Django Ninja / DRF | pytest + pytest-django + model_bakery | — |
| `~/Core` (frontend-legacy part) | frontend-legacy | Jinja2 + jQuery | pytest (server-side templates) | — |
| `~/front-test` | frontend-spa | React + Vite | Vitest + RTL | Vite |

### API-контракты (cross-repo) — required when backend + frontend-* both present

Include this subsection ONLY when Репозитории и стеки contains both a `backend` row AND at least one `frontend-*` row. Skip it entirely otherwise.

Source of truth is `api-contract.md` from upstream `architect`. For each endpoint the feature touches:

1. In the backend repo — find the schema/serializer/view handler on the feature branch
2. In the frontend repo(s) — grep for the URL pattern or API-client method call
3. Compare actual request/response shape against `api-contract.md` spec
4. Label `Статус контракта` as one of:
   - `Совпадает` — backend and frontend agree with api-contract.md
   - `Расхождение: {short reason}` — one side differs; describe the drift
   - `Не покрыт` — frontend does not call this endpoint (backend-only change)

| Endpoint | Backend repo | Frontend repo | Статус контракта | api-contract ref |
| --- | --- | --- | --- | --- |
| `GET /api/v2/spa/advert/{id}/` | `~/Core` | `~/front-test` | Совпадает | `api-contract.md §3.2` |
| `POST /api/v2/spa/generate-description/` | `~/Core` | `~/front-test` | Расхождение: frontend ожидает `result`, backend возвращает `generated_description` | `api-contract.md §4.1` |
| `GET /api/v2/spa/form-config/` | `~/Core` | — | Не покрыт — frontend не использует | — |

For every row with `Расхождение` → add at least one case under `## N. Integration Contract — {endpoint}` in `test-matrix.md` (downstream to `backend-integ-tester`).

### {краткое описание фичи, 1-3 абзаца}

Для bug-TD (Type=Bug) секция Контекст обязательно содержит дополнительно:

- **Архитектура функционала** — пронумерованные шаги потока (1..N) с точными ссылками на код (`module/path.py:line — method()`)
- **Ключевые детали реализации** — поля формы / валидация / обработка файлов / ветвления (bullet list)
- **Точки поломки** — гипотезы где именно ломается, с разделением Frontend / Backend
- **Ограничения** — таблица `Параметр | Значение | Статус`, где Статус = Подтверждено кодом / [УТОЧНИТЬ]

### Скоуп

- **Включено:** что тестируем
- **Исключено:** что не тестируем (смежные экраны, миграции данных, отдельные задачи)

## Out of scope

- {явный список исключений}

## Источники

- Jira: {url}
- Confluence (правила TD): https://larixon.atlassian.net/wiki/spaces/itdep/pages/3591733264
- Confluence (Test Design): https://larixon.atlassian.net/wiki/spaces/It1/pages/3493691537
- Confluence (Template for TD): https://larixon.atlassian.net/wiki/spaces/It1/pages/3582230529
- **Сильные TD (референсы):** {2-3 related TDs this was built from}
- Кодовые файлы (ветка {TASK_KEY}): {bullet list}
- Feature-ветка: `{TASK_KEY}`
```

### `test-matrix.md` — the body of the TD

See slot `035-test-matrix.md` for the full format. Summary:

- Per-case self-contained blocks, NOT a flat `| ID | Scenario | Test Level | ... |` table (reject MOB-795 / MOB-775 format)
- Sequential numbering across ALL sections (1, 2, 3…); no prefixes (`T-`, `UT-`, `IT-`), no suffixes (`17a`), no gaps
- Each case: **Задача / Предусловия / Действие / Ожидаемый результат / Priority | Layer | Type** — the 6 mandatory fields
- Markdown checkbox `[ ]` / `[x]` in the case heading (after `###`), never after list marker
- `Реализован: test_file.py::TestClass::test_method` under the heading for `[x]` cases
- `Частично покрыт: test_name` marker for close-but-inexact coverage
- `[НЕ РЕАЛИЗОВАНО]` plain-text label in heading when production code is not yet written
- Parametric cases: table-inside-case (CD-1319 pattern) for 4+ combinations OR pytest-parametrize ID list (STM-65 pattern) for 2-3

### `risk-map.md` — compact risk→cases table

```markdown
| Риск | Приоритет | Источник | Кейсы |
| --- | --- | --- | --- |
| Отправка сообщения с фото полностью заблокирована | P0 | ТЗ | 1, 11, 20, 29 |
| Регрессия: отправка текста без фото перестала работать | P0 | Регрессия | 5, 13, 21, 28 |
| Кириллица в имени файла ломает сохранение | P1 | Граничный случай | 17 |

## Усилители риска (применённые)

- {list of amplifiers that bumped a risk one level up — e.g. "затрагивает multipart/form-data", "сессия модератора"}

## Регрессионные риски

- {existing contracts or endpoints that could break}
```

`Приоритет` matches the `Priority` of the referenced cases in `test-matrix.md`. `Источник` labels origin (ТЗ / Побочный эффект / Граничный случай / Регрессия). `Кейсы` uses case numbers only — no layer prefix (cases have unique global numbers).

Do **not** produce HIGH/MEDIUM/LOW governance sub-documents with narrative (MOB-802 pattern). Keep the whole file ≤ 1 page (~60 lines).

### `test-data-strategy.md` — factories + permission matrix

- Project factory syntax: `f.user()`, `f.rubric(collect_reviews_enabled=True)`, `f.advert(avg_rating=4.5, reviews_count=47)`, `f.advert_lead(advert=advert, user_id=user.id)`
- Permission matrix table: Anonymous / Owner / Other user / Admin — each row lists which cases use it
- Multi-market fixtures: `@override_settings(SETTINGS_MODULE="settings.bazaraki")` and reference Django settings file per market
- MonkeyPatch for settings: `settings.REVIEW_COMMENT_MAX_SYMBOLS = 0` via `override_settings` in Integration
- External mocks: Firebase / Redis / ClickHouse — list what to patch and how

### `coverage-targets.md` — per-module targets

| Module | Class / Method | Risk | Target Lines | Target Branches | Justification |
| --- | --- | --- | --- | --- | --- |
| `reviews/services/advert_reviews_app/advert_info.py` | `GetAdvertReviewsInfo.__call__` | HIGH | ≥ 90% | ≥ 85% | Ветки по `collect_reviews_enabled`, `reviews_count`, `user_id` critical for 404-vs-200 |
| `reviews/mappers/advert_reviews.py` | `map_review_item`, `map_reviews_summary_item` | HIGH | 100% | 100% | Pure functions — exhaustive coverage |

Modules not modified in the feature branch → `no change` (no artificial targets).

---

## Test case format (canonical Larixon)

Every case in `test-matrix.md` MUST follow this exact shape (see slot `035-test-matrix.md` for the complete rules):

```markdown
### N [ ] {Title — describes behavior, no T- prefix}

Реализован: `test_file.py::TestClass::test_method`
   (omit this line when the case is [ ] not yet written)

**Задача:** one-sentence purpose (what this proves).

**Предусловия:**
- `user = f.user(account_type="business_fixed", user_type=2)` — with exact factory values
- `advert = f.advert(avg_rating=4.5, reviews_count=47)`
- `settings.REVIEW_COMMENT_MAX_SYMBOLS = 2000` (default) — via `override_settings`

**Действие:** exact call.
- Integration: `GET /api/v2/spa/advert/{advert_id}/reviews/?sort=rating_high`
- Unit BE: `GetAdvertReviewsInfo(advert_id=advert.id, user_id=None)()`
- E2E UI: step-by-step with selectors (`textarea[name=text]`, `input[type=file][name=files]`)

**Ожидаемый результат:** exact observable values.
- HTTP 200
- `response.json["advert"]["lead_id"] is None`
- `StaffMessages.objects.filter(staff=operator, user=target_user).exists() == True`
- Do NOT use "correct", "as expected", "работает"

Priority: P0 | Layer: Unit BE | Type: auto-candidate
```

### Parametric cases — table inside the case (CD-1319 pattern)

When a case verifies 4+ input combinations:

```markdown
### 1 [ ] Параметрический: смена account_type

**Задача:** проверить поведение user_type при смене account_type.

**Предусловия:** пользователь открыт в Django Admin; user_type не изменяется.

**Действие:** сменить account_type на значение из колонки «Новый account_type», сохранить.

| # | Предусловия | Новый account_type | Ожидаемый user_type | Комментарий |
| --- | --- | --- | --- | --- |
| 1 | account_type=business_fixed, user_type=real estate | business_fixed_premium | real estate (сохранился) | Переход внутри allowed |
| 2 | account_type=business_fixed, user_type=default | business | default (сброшен) | Переход из allowed в не-allowed |
| ... | ... | ... | ... | ... |

Priority: P0 | Layer: Unit BE | Type: auto-candidate
```

### Layer section structure

Each layer section opens with `Цель` + `Кодовая привязка`:

```markdown
## 1. Unit BE — GetAdvertReviewsInfo.__call__

**Цель:** проверить логику выбора lead_id и валидации `collect_reviews_enabled`, `reviews_count`.
**Кодовая привязка:** `reviews/services/advert_reviews_app/advert_info.py@GetAdvertReviewsInfo.__call__`

### 1 [ ] advert_id не существует → 404
...
```

Layer section headers (use only those relevant to the task):

```
## 1. Unit BE — {description}
## 2. Integration — {endpoint or flow}
## 3. Integration DB — {model constraint tests, if applicable}
## 4. Integration Contract — {cross-repo contract checks, if applicable}
## 5. E2E — {headless multi-step flow, if applicable}
## 6. E2E UI — {browser screen / admin page, if applicable}
## 7. Smoke — {post-deploy manual check, if applicable}
```

### Case status convention

- `### N [ ] Title` — case not yet written; `Реализован:` line omitted
- `### N [x] Title` + `Реализован: test_file.py::TestClass::test_method` — case already exists
- `### N [ ] Title` + `Частично покрыт: test_name` — existing test covers the area but not this exact scenario; downstream tester still writes a new test
- `### N [ ] Title [НЕ РЕАЛИЗОВАНО]` — production code is not yet written; tester cannot write tests against nonexistent code; leave as blocked

For fresh feature branches before tests are written, all cases = `[ ]`. Do NOT fabricate pytest IDs.

---

## Reference TDs (MUST study before writing)

These are the team-canonical TDs. Match their structure verbatim:

- [STM-68 (feature, reviews page endpoint)](https://larixon.atlassian.net/wiki/spaces/It1/pages/4222976017)
- [STM-65 (feature, listings + new ordering)](https://larixon.atlassian.net/wiki/spaces/It1/pages/4219404307)
- [STM-101 (feature, settings-driven field)](https://larixon.atlassian.net/wiki/spaces/It1/pages/4317675552)
- [CD-4653 (bug, file upload, multi-layer, E2E UI vs Smoke split)](https://larixon.atlassian.net/wiki/spaces/It1/pages/4290707498)
- [CD-1319 (bug, Django admin, parametric table-inside-case)](https://larixon.atlassian.net/wiki/spaces/It1/pages/4326391810)
- [CD-4017 (bug, multi-layer, Доменные понятия + Поток бага + Источник column)](https://larixon.atlassian.net/wiki/spaces/It1/pages/4320985141)

**Anti-reference (do NOT follow):**

- MOB-802 multi-document format (coverage-targets.md / risk-map.md / test-strategy.md / downstream-guidance.md as separate governance documents). The 5 files are committed to git per locked 050, but each file must stand alone and be compact per the templates above.

---

## Language

- The Jira comment follows the English platform template (locked slot 050).
- All 5 output files use **Russian field names**: Задача, Предусловия, Действие, Ожидаемый результат, Ссылки, Контекст, Риски и приоритеты, Out of scope, Источники.
- Case titles may mix Russian and English code identifiers naturally: `advert_id не существует → 404`.

## Downstream sync

- TD synced to Allure TestOps web project (`https://larixon.testops.cloud/project/1/launches`) via `td-allure-sync`.
- Each case's Реализован field maps to Allure test case automation status.
