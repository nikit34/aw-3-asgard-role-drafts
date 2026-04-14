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

### TD output format

Produce a **single Confluence page** (not multiple files). The page structure must follow the team convention exactly:

```
Ссылки
Контекст
Риски и приоритеты
1. {Layer} — {section title}  (test cases)
2. {Layer} — {section title}  (test cases)
...
Out of scope
Источники
```

Publish to [TDs 2026](https://larixon.atlassian.net/wiki/spaces/itdep/folder/4091674628). Synced to Allure TestOps web project (`project/1`) via `td-allure-sync`. Publication and generation happen in separate chats (generation consumes most context).

**Do NOT** produce separate files (`test-strategy.md`, `test-matrix.md`, `risk-map.md`, `coverage-targets.md`, `test-data-strategy.md`). All content goes into the single TD page following the sections below.

### Section: Ссылки

Numbered table with all references relevant to testing:

| # | Описание | Ссылка / Значение |
| --- | --- | --- |
| 1 | Jira-таск | URL |
| 2 | Тип | Bug / Feature (Priority) |
| 3 | Endpoint(s) | `METHOD /api/path/` |
| 4 | View / Service | `module/path.py:line — ClassName.method()` |
| ... | Существующие тесты (до задачи) | `module/tests.py — TestClass` |

### Section: Контекст

1. **Репозитории и стеки** table: `Репозиторий | Роль | Фреймворк | Тестовый стек | Сборщик`
2. **Архитектура** — step-by-step description of the code flow with precise code references (`module/path.py:line — method()`)
3. **Модель данных** — affected models and fields
4. **Ключевые настройки** — if applicable

### Section: Риски и приоритеты

| Риск | Приоритет | Кейсы |
| --- | --- | --- |
| Description of risk | P0-P2 | Reference to test case IDs below (e.g. "Integration 4, 5") |

### Sections: Test cases by layer

Group test cases under numbered sections by layer. Section title format:
```
1. Unit BE — {description of what is tested}
2. Integration — {endpoint or flow}
3. E2E UI — {screen or flow}
4. Smoke
```

Each section starts with a brief **Цель** and **Кодовая привязка**.

### Section: Out of scope

Explicit bulleted list of what is NOT tested and why.

### Section: Источники

Links to Jira, Confluence (TD template, TD rules, TD flow, reference TDs), code paths, existing tests.

Reference TDs:
- [CD-4253 (bug fix, race condition)](https://larixon.atlassian.net/wiki/spaces/itdep/pages/4316823553)
- [CD-4680 (feature, multi-endpoint)](https://larixon.atlassian.net/wiki/spaces/itdep/pages/4315578383)
- [CD-4653 (bug fix, file upload)](https://larixon.atlassian.net/wiki/spaces/itdep/pages/4290707498)
