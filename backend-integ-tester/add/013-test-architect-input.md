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
   - test-data-strategy.md — factory definitions (project `f.user()`, `f.rubric()` syntax), permission matrix, external mocks
   - coverage-targets.md   — endpoint coverage, flow coverage targets
```

### What to use

When test-architect artifacts exist, they override your own planning:

| Aspect | Without test-architect | With test-architect |
|--------|----------------------|---------------------|
| Scenario list | You derive from API spec | Use cases grouped under `## N. Integration — ...`, `## N. Integration DB — ...`, `## N. Integration Contract — ...` sections of test-matrix.md (your layers). `Integration Contract` cases correspond to `Расхождение` rows in `test-strategy.md § API-контракты (cross-repo)` — assert exact field names, types, nesting, and pagination shape against the frontend's expected shape, not just HTTP status |
| Coverage scope | All endpoints touched by the change | Use `Приоритет` from risk-map.md — P0 exhaustive, P1 happy + error, P2 smoke only |
| Test data setup | You create from models | Use factory calls from test-data-strategy.md |
| What NOT to test | Implicit | Use explicit "out of scope for Integration Tester" boundaries from test-strategy.md |

### Case status markers

Each case in `test-matrix.md` carries a markdown checkbox in its heading:

- `### N [ ] Title` — case not yet written. Write it. Under the heading add `Реализован: test_file.py::TestClass::test_method` after implementing, flip to `[x]` in your commit.
- `### N [x] Title` — case already exists; the `Реализован:` line points to the existing pytest ID. Read/review — do not duplicate.
- `Частично покрыт: test_name` — partial-coverage existing test. Treat as `[ ]` for planning; your new test must cover the exact scenario. Acknowledge the partial test in your Jira comment.
- `[НЕ РЕАЛИЗОВАНО]` label in a case heading — production code is not implemented yet, tests are blocked. Leave `[ ]`, do not write tests against nonexistent code, note in Jira.

### Traceability

When following test-architect guidance, reference the case number in test names or comments:

```python
# Case 42: GET /api/v2/feeds/{id}/ returns valid XML with correct listing count
def test_property_feed_listing_count_equals_advert_count(self):
    ...
```

Reference case numbers in your Jira completion comment so test-architect can verify coverage.

### Conflicts

If test-architect guidance conflicts with what you see in the code (e.g. an endpoint listed for testing does not exist, or the response shape differs from what was assumed):

1. Follow what the code actually has — do not test phantom endpoints
2. Post a `/tracker-comment` noting the discrepancy with the specific case number
3. Continue with the rest of the plan

### Artifacts not found

If no test-architect artifacts exist for this feature, proceed with your own planning as defined in `015-workflow.md`. This is normal for tasks that skip the test-architect phase.
