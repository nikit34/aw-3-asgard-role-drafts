## Larixon Coverage Expectations

### Source of truth

- Prefer the current repo configuration over legacy wording in old docs.
- In the Android repo, coverage is currently wired through `Kover`.
- Older task descriptions or Bamboo labels may still mention `Jacoco`. If you see both, explain the mismatch instead of pretending they are the same thing.

### Working coverage floors

Use these as default target floors unless the repo or task explicitly defines stricter gates:

| Layer | Target floor |
| --- | --- |
| Repository / data source | 85% |
| UseCase / interactor / business rule | 90% |
| ViewModel / presenter state reducer | 80% |
| Mapper / serializer / formatter | 90% |

These are working engineering targets, not a license to write shallow tests. Behavior quality matters more than chasing a number.

### Android coverage workflow

- Confirm whether the touched module applies the Kover plugin.
- When giving local instructions, prefer the actual Gradle task and the report path that exists in the repo.
- Expected local report location: `build/reports/kover/html/index.html`
- Fail-below-threshold: `./gradlew ${MODULE}:koverVerify`
- If the task asks about CI coverage, report whether the Bamboo job label and published artifact URL were actually found, but do not turn direct Bamboo execution into a tester-role requirement.

### iOS coverage workflow

- No confirmed published iOS coverage URL or gate was found in accessible sources.
- Local-only: `xcodebuild test -enableCodeCoverage YES` (not confirmed in CI)
- If the task requires an iOS percentage or CI gate, escalate instead of fabricating one.
- Still expect change-based unit coverage for new business logic, mappers, and presentation state.

### Review rule

When you evaluate coverage for a change:

- start from changed business behavior, not from raw percentages
- check whether all new branches, validation paths, and mapping branches have tests
- call out missing tests even if module-level coverage looks healthy
- call out inflated coverage if tests only assert default values or construction noise

### Reporting format

Always say:

- tool actually used (`Kover`, `Jacoco`, Xcode coverage, or unknown)
- whether the CI report URL is confirmed
- which layer is under-covered
- which exact behaviors are still untested
