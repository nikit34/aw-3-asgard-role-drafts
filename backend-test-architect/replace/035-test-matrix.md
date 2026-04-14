## Test Matrix Design

### File: `test-matrix.md`

This file is the bulk of the test design. It is NOT a flat table. It contains self-contained test case blocks grouped by layer.

### Structure

```markdown
## 1. {Layer} — {what is tested}

**Цель:** one-sentence purpose of this section.
**Кодовая привязка:** `module/path.py:line — ClassName.method()`

### {sequential_number} {title}

{sequential_number}{complete_or_incomplete}

Реализован: {TestClass::test_method — filled by downstream tester, leave empty}

**Задача:** what this test proves in one sentence.

**Предусловия:**
- `user = f.user()` — setup with factory calls and exact values

**Действие:** exact action (API call: `GET /api/v2/spa/...`, method call: `ClassName.method(args)`).

**Ожидаемый результат:** observable outcome with exact values.

Priority: P1 | Layer: Unit BE | Type: auto-candidate
```

### Rules

- Sequential numbering across ALL sections (1, 2, 3... not restarting per section)
- `complete` = test already exists, `Реализован:` filled with class::method
- `incomplete` = test not yet implemented, `Реализован:` left empty
- `Предусловия` must use project factory syntax: `f.user()`, `f.rubric(...)`, `f.voucher(active=True, amount=100)`
- `Действие` for Integration: exact HTTP method and path
- `Действие` for Unit BE: exact method call with args
- `Ожидаемый результат` must include exact values (`HTTP 200`, `user.balance.total == 100`, `Model.objects.count() == 1`), not "correct" or "as expected"
- Each test case title must be parseable by `tester-skills-mcp` (`Name` column compatible)

### Priority rules

- **P1**: auth/permission checks, data mutation outcomes, error codes from api-contract, core business logic
- **P2**: edge cases, optional fields, pagination, filter combinations, multi-market variants
- **P3**: corner cases with very low probability, cosmetic consistency

### Layer sections

Group test cases under these section headers:

```
## 1. Unit BE — {description of what is tested}
## 2. Integration — {endpoint or flow}
## 3. Integration DB — {model constraint tests, if applicable}
## 4. E2E UI — {screen or flow, if applicable}
## 5. Smoke — {post-deploy checks, if applicable}
```

Not all sections are needed for every task. Include only layers relevant to the task scope.

### Coverage rules

- Every endpoint in scope → at least one Integration test case
- Every HIGH-risk area from `risk-map.md` → test cases referenced by ID
- Every service method changed → at least one Unit BE test case
- Backward compatibility section when existing endpoints are modified
