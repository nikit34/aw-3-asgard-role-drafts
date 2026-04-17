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
   - risk-map.md        — compact `| Риск | Приоритет | Источник | Кейсы | Платформа |` table
   - test-data-strategy.md — MockWebServer JSON shapes (Android), URLProtocol stubs (iOS), market data sets, error codes
   - coverage-targets.md   — screen state coverage, flow coverage targets
```

### What to use

When test-architect artifacts exist, they override your own planning:

| Aspect | Without test-architect | With test-architect |
|--------|----------------------|---------------------|
| Scenario list | You derive from UX spec | Use cases grouped under `## N. Integration Android — ...`, `## N. Integration iOS — ...`, `## N. E2E UI Android — ...`, `## N. E2E UI iOS — ...` sections of test-matrix.md (your layers) |
| Screen state coverage | All 5 states for every screen | Use `Приоритет` from risk-map.md to prioritize testing order — P0 rows first. All screens still require 5/5 states per platform rules; priority determines test depth and assertion granularity, not state count. |
| MockWebServer / URLProtocol setup | You create from API contracts | Use JSON response definitions from test-data-strategy.md — file names, error codes, pagination shapes |
| What NOT to test | Implicit | Use explicit "out of scope for Integration Tester" boundaries from test-strategy.md |

### Case status markers

Each case in `test-matrix.md` carries a markdown checkbox in its heading:

- `### N [ ] Title` — case not yet written. Write it. Under the heading add `Реализован: TestClass::testMethodName` (Android) or `TestSpec::"scenario description"` / `TestClass.testMethodName` (iOS) after implementing, flip to `[x]` in your commit.
- `### N [x] Title` — case already exists; the `Реализован:` line points to the existing test ID. Read/review — do not duplicate.
- `Частично покрыт: test_name` — partial-coverage existing test. Treat as `[ ]` for planning; your new test must cover the exact scenario. Acknowledge the partial test in your Jira comment.
- `[НЕ РЕАЛИЗОВАНО]` label in a case heading — production code is not implemented yet, tests are blocked. Leave `[ ]`, do not write tests against nonexistent code, note in Jira.

### Traceability

When following test-architect guidance, reference the case number in test names or Allure annotations:

```kotlin
// Case 42: CartScreen shows empty state when API returns no items
@Test
fun cartScreen_showsEmptyState_whenApiReturnsNoItems() { ... }
```

```swift
// Case 42: CartScreen shows empty state when API returns no items
func test_cartScreen_showsEmptyState_whenApiReturnsNoItems() { ... }
```

For Allure-annotated tests, use the case number in the `@Story` or `@Description` annotation so it maps back to the test matrix.

Reference case numbers in your Jira completion comment so test-architect can verify coverage.

### Conflicts

If test-architect guidance conflicts with what you see in the code (e.g. a screen listed for testing does not exist, test tags from ui-contracts.md differ from what test-architect assumed):

1. Follow what the code and ui-contracts.md actually have — Designer's contracts are the source of truth for tags
2. Post a `/tracker-comment` noting the discrepancy with the specific case number
3. Continue with the rest of the plan

### Artifacts not found

If no test-architect artifacts exist for this feature, proceed with your own planning as defined in `015-workflow.md`. This is normal for tasks that skip the test-architect phase.
