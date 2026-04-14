## Larixon Web Test Design Infrastructure

### Scope

- Repository: `https://gitlab.dev.larixon.com/larixon-classifieds/web/core` (local: `~/Core`)
- Feature branch = Jira ticket number (e.g. `CD-4651`). Always analyze the feature branch, not master. If not specified, ask.

### Test layers → downstream routing

| Layer | Covers | Downstream role |
| --- | --- | --- |
| Unit BE | service/serializer/model methods — no HTTP, no DB | `backend-unit-tester` |
| Unit FE | React component/hook/store/mapper in isolation | `frontend-unit-tester` |
| Integration | single-endpoint through Django test client with real DB | `backend-integ-tester` |
| E2E UI | browser-level Playwright against a running stand | `e2e-tester` |

Assign each scenario to exactly one layer. Do not duplicate assertions across layers.

### Prioritization

| Priority | Meaning |
| --- | --- |
| P1 | Critical — blocks business or core user flow |
| P2 | Important — regression risk, significant secondary flow |
| P3 | Supplementary — edge case, cosmetic, nice-to-have |

### Markets

Include market-specific rows when the feature touches locale, currency, or user-facing content:

| Market | Locale | Currency | Notes |
| --- | --- | --- | --- |
| Bazaraki | EN | EUR | GDPR/Google privacy |
| Somon | RU | TJS | Cyrillic content |
| Unegui | MN | MNT | eMongolia integration |
| Jacars | en_JM | JMD | Car-market specific |
| Pin | en_TT | TTD | Trinidad |
| Salanto | EN | EUR | Verify payment currency |

### Content rules for the 5 mandatory files

The platform requires 5 files in `production-documentation/task-{TASK_KEY}/` (locked slot 050). The following rules define what each file must contain for Larixon web projects. ASGARD publishes these files to Confluence — ensure each file is self-contained and readable.

#### `test-strategy.md` — Ссылки + Контекст + Out of scope + Источники

Must include these sections:

1. **Ссылки** — numbered table of all references:

| # | Описание | Ссылка / Значение |
| --- | --- | --- |
| 1 | Jira-таск | URL |
| 2 | Тип | Bug / Feature (Priority) |
| 3 | Endpoint(s) | `METHOD /api/path/` |
| 4 | View / Service | `module/path.py:line — ClassName.method()` |
| ... | Существующие тесты | `module/tests.py — TestClass` |

2. **Контекст** — repo table (`Репозиторий | Роль | Фреймворк | Тестовый стек`), step-by-step architecture with code refs (`module/path.py:line — method()`), data model, key settings
3. **Out of scope** — explicit bulleted list of exclusions
4. **Источники** — links to Jira, Confluence, code, existing tests

#### `test-matrix.md` — test cases grouped by layer

NOT a flat table. Each test case is a self-contained block:

```markdown
### {sequential_number} {title}

{sequential_number}{complete_or_incomplete}

Реализован: {empty in TD — filled by downstream tester}

**Задача:** what this test proves.

**Предусловия:**
- `user = f.user()` — factory calls with exact values

**Действие:** exact HTTP call or method call.

**Ожидаемый результат:** exact values (HTTP 200; `field == value`; `Model.objects.count() == 1`).

Priority: P0-P2 | Layer: Unit BE / Integration / E2E UI | Type: auto-candidate
```

Group cases under numbered layer sections:
```markdown
## 1. Unit BE — {description}
## 2. Integration — {endpoint}
## 3. E2E UI / Smoke
```

Each section starts with **Цель** and **Кодовая привязка**.

#### `risk-map.md` — Риски и приоритеты

Table with case references:

| Риск | Приоритет | Кейсы |
| --- | --- | --- |
| Description of risk | P0-P2 | Integration 4, 5 |

#### `test-data-strategy.md` — factories and fixtures

Use project factory syntax: `f.user()`, `f.rubric(...)`, `f.voucher(active=True, amount=100)`. Include permission matrix (anonymous, owner, non-owner, admin).

#### `coverage-targets.md` — per-module targets

Table: `Module | Class | Risk | Target Lines | Target Branches | Justification`.

### Reference TDs (study before writing)

These TDs follow the team convention:
- [CD-4253 (bug fix, race condition)](https://larixon.atlassian.net/wiki/spaces/itdep/pages/4316823553)
- [CD-4680 (feature, multi-endpoint)](https://larixon.atlassian.net/wiki/spaces/itdep/pages/4315578383)
- [CD-4653 (bug fix, file upload)](https://larixon.atlassian.net/wiki/spaces/itdep/pages/4290707498)

Study these before starting. Your `test-matrix.md` must use the same per-case detail level (Задача/Предусловия/Действие/Ожидаемый) — not a flat matrix table.

TD synced to Allure TestOps web project (`project/1`) via `td-allure-sync`.
