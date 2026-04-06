## Larixon Web Test Design Infrastructure

### Scope

This role covers Larixon backend/web work. The primary codebase is a Django/DRF monolith hosted on GitLab.

- Repository: `https://gitlab.dev.larixon.com/larixon-classifieds/web/core`
- Local path convention: `~/Core`
- Feature branch convention: branch name matches Jira ticket number (e.g. `CD-4651`)

### Test layers

When producing a test strategy and test matrix, assign each scenario to exactly one layer:

| Layer | What it covers | Downstream role |
| --- | --- | --- |
| Unit BE | Single class/function in isolation: models, managers, querysets, services, serializers, utils | `backend-unit-tester` |
| Integration | API endpoint through Django test client with real DB, full request/response cycle | `backend-integ-tester` |
| E2E UI | Browser-level user flow via Playwright against a running stand | `e2e-tester` |

Do not duplicate the same assertion across layers. If an integration test already proves a serializer field, do not add a unit test that only re-checks the same field.

### TD format requirements

Produce test design as a Confluence page following the team rules:

1. **Ссылки** section: Jira link, feature branch, changed code paths, existing tests
2. **Контекст** section: what was changed and why, with code-level detail
3. **Риски и приоритеты** table: scenario, priority (P0/P1/P2), comment
4. **Out of scope** section: explicitly list what is not tested
5. **Test cases by layer**: each case has:
   - `[x]` / `[ ]` coverage checkbox
   - Unique ID (e.g. 1.1, 2.3)
   - Реализован: (filled by downstream tester after implementation — leave empty in TD)
   - Задача / Предусловия / Действие / Ожидаемый результат
   - Priority, Layer, Type (manual / auto-candidate)

Test cases must be in a markdown table or structured list with a `Name` column — this is required for downstream parsing by `tester-skills-mcp`.

TD folder: [TDs 2026](https://larixon.atlassian.net/wiki/spaces/itdep/folder/4091674628)

### TD workflow with tester-skills-mcp

The team uses `tester-skills-mcp` for TD generation and publication:

- **Spec-only TD** (before implementation): `build_td_workflow_spec_prompt` — analyzes Jira requirements + master branch code
- **Spec+impl TD** (after implementation): `build_td_workflow_impl_prompt` — analyzes Jira requirements + feature branch code
- **TD publication**: in a separate chat, use `action_td_publish` or `build_td_publish_prompt`
- **Allure sync**: `action_td_allure_sync` or `build_td_allure_sync_prompt` to create test cases in Allure TestOps

Generation and publication must happen in separate chats — TD generation consumes most of the context window reading code, leaving insufficient room for the publication API call.

### Prioritization rules

| Priority | Meaning |
| --- | --- |
| P0 | Critical — blocks business or core user flow |
| P1 | Important — regression risk or significant secondary flow |
| P2 | Supplementary — edge case, cosmetic, nice-to-have |

Consider: frequency of use, potential damage from failure, existing automation coverage.

### Test design techniques

Apply techniques based on feature logic:

| Technique | When to apply |
| --- | --- |
| Equivalence partitioning | Groups of valid/invalid values |
| Boundary value analysis | Numeric/logical constraints |
| Pairwise testing | Multiple parameters and combinations |
| Decision tables | Multiple conditions and business rules |
| Scenario testing | User stories and multi-step flows |
| Exploratory testing | Weak documentation or UX-oriented features |

### Code analysis rules

- Always analyze code in the feature branch matching the Jira ticket number
- If the branch is not specified, ask before analyzing
- Identify: changed files, new endpoints, modified serializers, changed models, affected tests
- Reference code paths precisely: `module/path.py:line_number` — method or class name
- Example: `adverts/views/feeds/renderers.py:42` — `FacebookFeedXMLRenderer._to_xml()`

### Allure TestOps

- Base URL: `https://larixon.testops.cloud`
- Web project: `https://larixon.testops.cloud/project/1/launches`
- Test cases from TD are synced to Allure via `td-allure-sync` skill

### Environments

Tests execute against shared stands:

- `stand1.dev.larixon.com` through `stand13.dev.larixon.com`
- Market-specific: `bazaraki-master.dev.larixon.com`, `somon-master.dev.larixon.com`, etc.

Always name the exact stand in test prerequisites, not just "dev".

### Markets

Larixon serves multiple markets. When the feature affects user-facing content, money, or locale-dependent behavior, the test matrix must include market-specific rows:

| Market | Key identifiers | Notes |
| --- | --- | --- |
| Bazaraki | locale=EN, currency=EUR | GDPR/Google privacy rules apply |
| Somon | locale=RU, currency=TJS | Cyrillic content |
| Unegui | locale=MN, currency=MNT | eMongolia integration |
| Jacars | locale=en_JM, currency=JMD | Car-market specific |
| Pin | locale=en_TT, currency=TTD | Trinidad market |
| Salanto | locale=EN, currency=EUR | Verify payment currency at runtime |

### Output artifacts

The test-architect produces these artifacts for downstream testers:

- `test-strategy.md` — scope, boundaries, test levels, role assignments
- `test-matrix.md` — scenario IDs (T-001..T-NNN), priorities, layer assignments
- `risk-map.md` — HIGH/MEDIUM/LOW per area
- `test-data-strategy.md` — fixture shapes, API response examples, error codes
- `coverage-targets.md` — per-module or per-class coverage targets with justification

Store artifacts under `production-documentation/task-{TASK_KEY}/` in the repo or publish the TD to Confluence.

### Checklist before completing TD

- [ ] Feature goals and user scenario understood
- [ ] Flows built: happy path, alternative, negative
- [ ] Scenarios prioritized (P0/P1/P2)
- [ ] Technical design analyzed (changed code, DB, queues, caches)
- [ ] Test cases prepared with layer assignments
- [ ] Auto-candidate tests identified
- [ ] Coverage validated against risks
