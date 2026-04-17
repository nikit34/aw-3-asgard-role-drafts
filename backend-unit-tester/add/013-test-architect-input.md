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
   - test-data-strategy.md — factory definitions, permission matrix, external mocks
   - coverage-targets.md   — per-module coverage numbers with justification
```

### What to use

When test-architect artifacts exist, they override your own planning:

| Aspect | Without test-architect | With test-architect |
|--------|----------------------|---------------------|
| Scenario list | You derive from feature scope | Use cases grouped under `## N. Unit BE — ...` section of test-matrix.md (your layer) |
| Coverage targets | Default floors from `020-coverage.md` | Use per-module targets from coverage-targets.md |
| Risk-based depth | You assess yourself | Use `Приоритет` from risk-map.md — P0 rows exhaustive, P1 targeted, P2 minimal |
| What NOT to test | Implicit | Use explicit "out of scope for Unit Tester" boundaries from test-strategy.md |

### Case status markers

Each case in `test-matrix.md` carries a markdown checkbox in its heading:

- `### N [ ] Title` — case not yet written. Write it. Under the heading add `Реализован: test_file.py::TestClass::test_method` after implementing, flip to `[x]` in your commit.
- `### N [x] Title` — case already exists; the `Реализован:` line points to the existing pytest ID. Read/review — do not duplicate.
- `Частично покрыт: test_name` — partial-coverage existing test. Treat as `[ ]` for planning; your new test must cover the exact scenario. Acknowledge the partial test in your Jira comment.
- `[НЕ РЕАЛИЗОВАНО]` label in a case heading — production code is not implemented yet, tests are blocked. Leave `[ ]`, do not write tests against nonexistent code, note in Jira.

### Traceability

When following test-architect guidance, reference the case number in test names or comments:

```python
# Case 12: Service returns validation error when quantity is zero
def test_add_to_cart_returns_validation_error_when_quantity_is_zero(self):
    ...
```

Reference case numbers in your Jira completion comment so test-architect can verify coverage.

### Conflicts

If test-architect guidance conflicts with what you see in the code (e.g. a class listed for testing does not exist, or coverage target is unreachable):

1. Follow what the code actually has — do not test phantom classes
2. Post a `/tracker-comment` noting the discrepancy with the specific case number
3. Continue with the rest of the plan

### Artifacts not found

If no test-architect artifacts exist for this feature, proceed with your own planning as defined in `015-workflow.md`. This is normal for tasks that skip the test-architect phase.
