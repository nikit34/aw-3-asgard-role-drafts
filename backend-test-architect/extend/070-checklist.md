## Larixon TD Checklist Additions

- [ ] TD is a single Confluence page (not separate files)
- [ ] Sections present: Ссылки, Контекст, Риски и приоритеты, test case sections, Out of scope, Источники
- [ ] Each test case has: sequential number, complete/incomplete status, Реализован (empty), Задача/Предусловия/Действие/Ожидаемый, Priority/Layer/Type
- [ ] Риски table references test case IDs in Кейсы column
- [ ] Code references are precise: `module/path.py:line — ClassName.method()`
- [ ] Downstream role assignments specified per layer section
- [ ] Market-specific rows added when feature touches locale/currency/content
- [ ] Allure sync triggered via `td-allure-sync` (separate chat)
- [ ] Test case titles parseable by `tester-skills-mcp` (`Name` column compatible)
