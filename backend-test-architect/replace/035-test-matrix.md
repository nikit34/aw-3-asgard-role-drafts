## Test Case Format

### Individual test case structure

Each test case is a self-contained block inside the layer section. Format:

```
### {sequential_number} {title}

{sequential_number}{status: complete or incomplete}

Реализован: {TestClass::test_method — filled by downstream tester, leave empty in TD}

**Задача:** what this test proves in one sentence.

**Предусловия:**
- bullet list of setup steps with factory calls and exact values

**Действие:** the exact action (API call, method call, user step).

**Ожидаемый результат:** observable outcome with exact values (status codes, field values, DB state).

Priority: P0-P2 | Layer: Unit BE / Integration / E2E UI / Smoke | Type: auto-candidate / manual
```

### Rules

- Sequential numbering across all sections (1, 2, 3... not restarting per section)
- `complete` = test already exists in codebase, `Реализован:` filled with class::method
- `incomplete` = test not yet implemented, `Реализован:` left empty
- `Предусловия` must use project factory syntax: `f.user()`, `f.rubric(...)`, `f.voucher(active=True, amount=100)`
- `Действие` for Integration: exact HTTP method and path (`GET /api/v2/spa/...`)
- `Действие` for Unit BE: exact method call (`ClassName.method(args)`)
- `Ожидаемый результат` must include exact values, not "correct" or "as expected"
- Each test case must have a `Name` column-compatible title for `tester-skills-mcp` parsing

### Priority rules

- **P1**: auth/permission checks, data mutation outcomes, error codes from api-contract, core business logic
- **P2**: edge cases, optional fields, pagination, filter combinations, multi-market variants
- **P3**: corner cases with very low probability, cosmetic consistency

### ID conventions

Test cases use sequential numbers (1, 2, 3...) within the single TD page. Layer prefix conventions for downstream reference:

| Prefix | Layer | Downstream role |
| --- | --- | --- |
| `UT-` | Unit BE | `backend-unit-tester` |
| `UTF-` | Unit FE | `frontend-unit-tester` |
| `IT-` | Integration | `backend-integ-tester` |
| `E2E-` | E2E UI | `e2e-tester` |

These prefixes are used in downstream guidance comments, not in the TD page itself (TD uses sequential numbers).

### Coverage rules

- Every endpoint in scope → at least one Integration test case
- Every HIGH-risk area from Риски table → test cases referenced in the Кейсы column
- Every service method changed → at least one Unit BE test case
- Backward compatibility section when existing endpoints are modified
- `Реализован` column filled only by downstream tester after implementation — leave empty in TD
