## Larixon Test Devices and Environments

### Environment rule

Always name the exact stand and build you are testing. `dev` is not enough.

### Shared stands

- Shared: `stand1.dev.larixon.com` ... `stand13.dev.larixon.com`

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

- Tests run on local emulators and simulators. This is the confirmed baseline for the current mobile workflow:
  - Android: emulator (e.g. Pixel 6 API 34)
  - iOS: simulator (e.g. iPhone 14, iOS 17)
- BrowserStack is **out of scope** for this workflow.
- If the task only asks for scenario design, do not force any execution environment at all. Separate scenario design from run orchestration.
- CI-side execution (Bamboo) runs tests on emulators automatically after merge. The tester role writes and validates locally; CI execution belongs to the automated merge/devops flow.

### Test management and reporting

- **Allure TestOps** is the primary reporting system (not TestRail):
  - Base URL: `https://larixon.testops.cloud`
  - Android launches: `https://larixon.testops.cloud/project/69/launches`
  - iOS launches: `https://larixon.testops.cloud/project/168/launches`
- Bamboo plan keys for CI test execution:
  - Android Automated Tests: `AD-AT` — `https://bamboo.dev.larixon.com/browse/AD-AT`
  - Android Integration: `AD-IN` — `https://bamboo.dev.larixon.com/browse/AD-IN`
  - iOS Integration: `ID-II` — `https://bamboo.dev.larixon.com/browse/ID-II`
- Android UI tests expose Allure metadata through annotations:
  - `AllureId`, `Epic`, `Feature`, `Story`
- Do not route this workflow through TestRail.

### Execution commands

- Use these only when the task explicitly needs local execution guidance or reproduction help.
- Android physical/emulator UI run:
  - `./gradlew connectedTjDebugAndroidTest`
- Android managed-device example:
  - `./gradlew allureDeviceDebugAndroidTest`
- iOS simulator example:
  - `xcodebuild test -workspace Larixon.xcworkspace -scheme Bazaraki -destination 'platform=iOS Simulator,name=iPhone 14'`
- iOS UI tests for specific market:
  - `xcodebuild test -workspace Larixon.xcworkspace -scheme Somon.tj -destination 'platform=iOS Simulator,name=iPhone 14'`

### Reporting rule

Every integration result must include:

- platform
- market
- stand URL
- device model or emulator/simulator profile
- OS version
- app build
- test run link or artifact path
