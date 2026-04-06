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
   - test-data-strategy.md — MockWebServer JSON shapes, market data sets, error codes
   - coverage-targets.md   — screen state coverage, flow coverage targets
```

### What to use

When test-architect artifacts exist, they override your own planning:

| Aspect | Without test-architect | With test-architect |
|--------|----------------------|---------------------|
| Scenario list | You derive from UX spec | Use assigned scenario IDs from test-matrix.md (your rows have `Test Level = Integration`) |
| Screen state coverage | All 5 states for every screen | Use risk-map.md — HIGH = 5/5 states, MEDIUM = 3/5 (Success, Error, Loading) |
| MockWebServer setup | You create from API contracts | Use JSON response definitions from test-data-strategy.md — file names, error codes, pagination shapes |
| What NOT to test | Implicit | Use explicit "out of scope for Integration Tester" boundaries from test-strategy.md |

### Traceability

When following test-architect guidance, include scenario IDs in test names or Allure annotations:

```kotlin
// T-042: CartScreen shows empty state when API returns no items
@Test
fun cartScreen_showsEmptyState_whenApiReturnsNoItems() { ... }
```

For Allure-annotated tests, use the scenario ID in the `@Story` or `@Description` annotation so it maps back to the test matrix.

Reference the scenario IDs in your Jira completion comment so test-architect can verify coverage.

### Conflicts

If test-architect guidance conflicts with what you see in the code (e.g. a screen listed for testing does not exist, test tags from ui-contracts.md differ from what test-architect assumed):

1. Follow what the code and ui-contracts.md actually have — Designer's contracts are the source of truth for tags
2. Post a `/tracker-comment` noting the discrepancy with the specific T-xxx ID
3. Continue with the rest of the plan

### Artifacts not found

If no test-architect artifacts exist for this feature, proceed with your own planning as defined in `015-workflow.md`. This is normal for tasks that skip the test-architect phase.
