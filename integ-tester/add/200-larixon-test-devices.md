## Larixon Test Devices and Environments

### Environment rule

Always name the exact stand and build you are testing. `dev` is not enough.

### Shared stands

The accessible mobile sources confirm shared stands such as:

- `stand1.dev.larixon.com`
- `stand2.dev.larixon.com`
- `stand3.dev.larixon.com`
- `stand4.dev.larixon.com`
- `stand5.dev.larixon.com`
- `stand6.dev.larixon.com`
- `stand7.dev.larixon.com`
- `stand8.dev.larixon.com`
- `stand9.dev.larixon.com`
- `stand10.dev.larixon.com`
- `stand11.dev.larixon.com`
- `stand12.dev.larixon.com`
- `stand13.dev.larixon.com`

Market-specific entries also exist in mobile configs, for example:

- `bazaraki-master.dev.larixon.com`
- `somon-master.dev.larixon.com`
- `somon1.dev.larixon.com`
- `somon2.dev.larixon.com`
- `somon3.dev.larixon.com`
- `somon4.dev.larixon.com`
- `unegui-master.dev.larixon.com`
- `unegui.dev.larixon.com`
- `unegui1.dev.larixon.com`
- `unegui2.dev.larixon.com`
- `jacars-master.dev.larixon.com`
- `jacars-kuber.dev.larixon.com`

### Device baseline

Use at least one modern and one older-supported device per platform when the task affects real UI behavior:

| Platform | Baseline devices |
| --- | --- |
| Android | `Pixel 6` on Android `14+`, `Samsung Galaxy S21` on Android `12+` |
| iOS | `iPhone 12` on iOS `16+`, `iPhone 14 Pro` on iOS `17+` |

Add a smaller-screen device if the task changes dense layouts, tab bars, badges, long text, or card wrapping.

### Execution preference

- Default to native validation routes that are already available to the team:
  - Android emulator or locally connected device
  - iOS simulator or locally connected device
- For the current mobile ASGARD flow, keep emulator or simulator based validation as the baseline assumption.
- Treat BrowserStack as out of scope for the baseline role unless the owner explicitly asks for cloud-device coverage in this workflow.
- If the task only asks for scenario design, do not force any execution environment at all. Separate scenario design from run orchestration.
- CI-side execution still belongs to the merge or devops flow, not to the tester role itself.

### BrowserStack

- Accessible Confluence sources confirm BrowserStack was selected in a PoC for Larixon mobile testing.
- The same source mentions `2` parallel sessions.
- Credentials were not available in accessible sources.
- Server's `2026-04-01` guidance says not to describe BrowserStack in the current baseline mobile tester skills for now.
- Only bring BrowserStack back if the owner explicitly asks for cloud-device execution in this workflow.

### Test management and reporting

- Allure/TestOps base URL: `https://larixon.testops.cloud`
- Confirmed TestOps launch pages for this workflow:
  - `https://larixon.testops.cloud/project/168/launches`
  - `https://larixon.testops.cloud/project/69/launches`
- Android UI tests already expose Allure metadata such as:
  - `AllureId`
  - `Epic`
  - `Feature`
  - `Story`
- Do not route this workflow through TestRail. Use the confirmed TestOps projects above as the primary reporting entry points.

### Execution commands

- Use these only when the task explicitly needs local execution guidance or reproduction help.
- Android physical/emulator UI run:
  - `./gradlew connectedTjDebugAndroidTest`
- Android managed-device example:
  - `./gradlew allureDeviceDebugAndroidTest`
- iOS simulator example:
  - `xcodebuild test -workspace Larixon.xcworkspace -scheme Bazaraki -destination 'platform=iOS Simulator,name=iPhone 14'`

### Reporting rule

Every integration result must include:

- platform
- market
- stand URL
- device model or emulator/simulator profile
- OS version
- app build
- test run link or artifact path
