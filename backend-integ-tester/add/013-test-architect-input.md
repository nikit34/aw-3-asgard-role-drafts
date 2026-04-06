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
   - test-strategy.md   — scope, boundaries, test levels
   - test-matrix.md     — scenario IDs (T-001..T-NNN), priorities, assignments
   - risk-map.md        — HIGH/MEDIUM/LOW per area
   - test-data-strategy.md — test DB fixtures, API response shapes, error codes
   - coverage-targets.md   — endpoint coverage, flow coverage targets
```

### What to use

When test-architect artifacts exist, they override your own planning:

| Aspect | Without test-architect | With test-architect |
|--------|----------------------|---------------------|
| Scenario list | You derive from API spec | Use assigned scenario IDs from test-matrix.md (your rows have `Test Level = Integration`) |
| Coverage scope | All endpoints touched by the change | Use risk-map.md — HIGH = exhaustive, MEDIUM = happy + error, LOW = smoke only |
| Test data setup | You create from models and fixtures | Use fixture definitions from test-data-strategy.md |
| What NOT to test | Implicit | Use explicit "out of scope for Integration Tester" boundaries from test-strategy.md |

### Traceability

When following test-architect guidance, include scenario IDs in test names or comments:

```python
# T-042: GET /api/v2/feeds/{id}/ returns valid XML with correct listing count
def test_property_feed_listing_count_equals_advert_count(self):
    ...
```

Reference the scenario IDs in your Jira completion comment so test-architect can verify coverage.

### Conflicts

If test-architect guidance conflicts with what you see in the code (e.g. an endpoint listed for testing does not exist, or the response shape differs from what was assumed):

1. Follow what the code actually has — do not test phantom endpoints
2. Post a `/tracker-comment` noting the discrepancy with the specific T-xxx ID
3. Continue with the rest of the plan

### Artifacts not found

If no test-architect artifacts exist for this feature, proceed with your own planning as defined in `015-workflow.md`. This is normal for tasks that skip the test-architect phase.
