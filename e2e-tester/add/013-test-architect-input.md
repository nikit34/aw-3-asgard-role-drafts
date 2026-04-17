## Test Architect Upstream Input

After completing Step Zero and before planning your test suite (Phase 2), check whether a Test Architect has already produced a test strategy for this feature.

### Discovery

```
1. From the Jira task, identify the parent story key ({PARENT_KEY})
2. Search for test-architect artifacts:
   find production-documentation/ -path "*/test-matrix.md" | head -5
3. The artifacts live under one of:
   - production-documentation/task-{TA_TASK_KEY}/   (test-architect subtask key)
   - production-documentation/{PARENT_KEY}-*/        (parent story folder)
4. If found, read ALL of:
   - test-strategy.md   — Ссылки, Контекст, Репозитории/стеки, Out of scope, Источники
   - test-matrix.md     — self-contained case blocks grouped by layer; each case has sequential number and checkbox marker
   - risk-map.md        — compact `| Риск | Приоритет | Источник | Кейсы |` table
   - test-data-strategy.md — test data, user accounts, preconditions, external mocks (`page.route()` patterns)
   - coverage-targets.md   — flow coverage targets
```

### What to use

When test-architect artifacts exist, they override your own planning:

| Aspect | Without test-architect | With test-architect |
|--------|----------------------|---------------------|
| Which user flows to test | You decide from requirements | Use "E2E Tester Guidance" section from test-strategy.md |
| Scenario list | You derive from UX spec | Use cases grouped under `## N. E2E — ...` and `## N. E2E UI — ...` sections of test-matrix.md (your layers) |
| Risk-based depth | You assess yourself | Use `Приоритет` from risk-map.md — P0 full flow + edge cases, P1 happy + main error, P2 smoke only |
| Test data | You create yourself | Use precondition definitions from test-data-strategy.md |
| Multi-market matrix | You identify from UI | Use market-specific parametric cases from test-matrix.md |
| What NOT to test | Implicit | Use explicit "out of scope for E2E Tester" boundaries from test-strategy.md |

### Case status markers

Each case in `test-matrix.md` carries a markdown checkbox in its heading:

- `### N [ ] Title` — case not yet written. Write it. Under the heading add `Реализован: tests/e2e/spec.py::TestClass::test_method` after implementing, flip to `[x]` in your commit.
- `### N [x] Title` — case already exists; the `Реализован:` line points to the existing test ID. Read/review — do not duplicate.
- `Частично покрыт: test_name` — partial-coverage existing test. Treat as `[ ]` for planning; your new test must cover the exact scenario. Acknowledge the partial test in your Jira comment.
- `[НЕ РЕАЛИЗОВАНО]` label in a case heading — production code is not implemented yet, tests are blocked. Leave `[ ]`, do not write tests against nonexistent code, note in Jira.

### Traceability

When following test-architect guidance, reference the case number in test names:

```python
# Case 101: User can filter adverts by category and see correct results
def test_filter_adverts_by_category(page):
    ...
```

Reference case numbers in your Jira completion comment so test-architect can verify coverage.

### Conflicts

If test-architect guidance conflicts with what you see in the UI (e.g. a flow listed for testing does not exist, or the page structure differs):

1. Follow what the actual UI has — do not test phantom flows
2. Post a `/tracker-comment` noting the discrepancy with the specific case number
3. Continue with the rest of the plan

### Artifacts not found

If no test-architect artifacts exist for this feature, follow the blocking protocol defined in `012-step-zero.md`: BLOCK via `/tracker-blocked` mentioning Test Architect. Do not proceed without upstream test strategy.
