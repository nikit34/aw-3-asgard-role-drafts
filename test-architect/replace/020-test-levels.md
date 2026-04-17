## Test Levels for Larixon Mobile (Android + iOS)

### Level 1: Unit Android (unit-tester, Android role)

**Scope:** pure Kotlin — no Android Context, no real network, no real DB.

**What to test:**
- Mappers (DTO → domain, domain → UI state) — pure functions, parameterized via Kotest `withData`
- UseCases — business logic with mocked repositories (MockK)
- ViewModels — state transitions and side-effects via Turbine for Flow / StateFlow
- Validators, formatters, i18n ngettext helpers
- Unit KMP common modules (`commonTest`) — multiplatform runner

**Tooling:** JUnit 5 (legacy-only for existing files) / Kotest `DescribeSpec` (preferred for new code) + MockK + Turbine + Kotest multiplatform runner for KMP. Coverage via Kover.

---

### Level 1b: Unit iOS (unit-tester, iOS role)

**Scope:** pure Swift — no UIViewController, no URLSession, no CoreData.

**What to test:**
- Mappers (DTO → domain, domain → view model) — pure functions
- Presenters / ViewModels — state transitions and output subjects with stubs
- Formatters, validators, localization helpers (ngettext equivalents)
- Pure business logic in Services

**Tooling:** XCTest or Quick + Nimble. Swift Package Manager or CocoaPods test target. Coverage via Xcode built-in `xccov`.

---

### Level 2: Integration Android (integ-tester, Android role)

**Scope:** full Android stack — screen rendering, navigation, ViewModel → Repository → MockWebServer. On-process emulator.

**What to test:**
- Compose UI rendering against real ViewModel — via `composeTestRule.setContent {}` + `onNodeWithText/assertIsDisplayed`
- Screen state transitions (loading / empty / error / content) with MockWebServer dispatchers
- Navigation triggers (not animations — visual animation belongs to Manual/E2E)
- Multi-screen flows within one Activity / NavHost
- Multi-market differences via product flavors (`tjDebug`, `mnDebug`, etc.)

**NOT in scope:**
- Full user journeys spanning login + deep flows (that's E2E UI)
- Visual pixel match (that's Manual)

**Tooling:** `connected{Flavor}DebugAndroidTest` + `androidx.compose.ui:ui-test-junit4` + `MockWebServer` + Espresso (legacy). Runs on emulator per Larixon product flavor.

---

### Level 2b: Integration iOS (integ-tester, iOS role)

**Scope:** XCTestCase with UI host, mocked URLSession via protocol stubs, launched on simulator.

**What to test:**
- ViewController / SwiftUI view rendering with test navigation stack
- Screen states triggered by stubbed network responses
- Market-specific targets via Xcode build configurations (`Bazaraki`, `Somon.tj`, `Unegui.mn`, `Jacars`, `Pin.tt`, `Salanto`)

**NOT in scope:**
- Full user journeys across multiple screens with real network (E2E UI)
- Design pixel match (Manual)

**Tooling:** XCTest + XCUIApplication + test target with mocked protocols. Runs on simulator per Larixon market target.

---

### Level 3: E2E UI — Android + iOS (integ-tester, extended)

**Scope:** full app on real emulator/simulator running against a fixture-backed stand or staging. Multi-screen user journey.

**What to test:**
- Complete user journeys (register → search → open advert → call seller → leave review)
- Deep-linking and external intents
- Permission prompts (camera, location, notifications) with `UiDevice.grantRuntimePermission` (Android) / XCUIApplication interruption handling (iOS)
- Bug-reproduction E2E for regression-sensitive paths

**NOT in scope:**
- Single-screen behavior (covered by Integration)
- Pure business logic (covered by Unit)
- Production-data integrity checks (manual)

**Tooling:**
- Android: `UiDevice` + Espresso + Bamboo plan `AD-AT` for CI.
- iOS: XCUIApplication + Bamboo plan `ID-II` for CI.

### Level 4: Smoke — manual

**Scope:** 1-5 minimal post-deploy manual steps on prod-like build. Verifies deploy health, not feature correctness.

**Tooling:** human on real device from the device matrix. Allure TestOps project 69 (Android) / project 168 (iOS).

---

### Boundary decision

Each scenario goes to exactly one layer. When unclear:

1. Can it be tested without Android Context / UIKit? → **Unit**
2. Does it involve UI rendering or single-screen state transitions? → **Integration**
3. Does it need multi-screen navigation with real(ish) network? → **E2E UI**
4. Does it need a real device on prod-like build? → **Smoke / Manual**
5. If still unclear → default to Integration (safest automation coverage)

Avoid duplicating assertions across layers — reference Larixon TDs never repeat an assertion across layers, each test owns its part.
