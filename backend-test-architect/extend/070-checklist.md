## Larixon TD Checklist Additions

- [ ] `test-strategy.md` contains: Ссылки (numbered table), Контекст (architecture with code refs), Out of scope, Источники
- [ ] `test-matrix.md` uses per-case blocks (Задача/Предусловия/Действие/Ожидаемый), NOT flat table rows
- [ ] `risk-map.md` has Кейсы column referencing test case IDs from `test-matrix.md`
- [ ] Code references are precise: `module/path.py:line — ClassName.method()`
- [ ] Предусловия use factory syntax: `f.user()`, `f.rubric(...)`, not abstract descriptions
- [ ] Ожидаемый результат has exact values (`HTTP 200`, `field == value`), not "correct" or "as expected"
- [ ] Market-specific rows added when feature touches locale/currency/content
- [ ] Downstream role assignments specified per layer section
- [ ] Test case titles parseable by `tester-skills-mcp` (`Name` column compatible)
- [ ] Allure sync triggered via `td-allure-sync`
