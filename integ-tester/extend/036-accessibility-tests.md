## Larixon Accessibility Additions

Add these Larixon-specific rules on top of the platform accessibility guidance.

### Directionality

- Current Larixon mobile markets in accessible sources are left-to-right.
- Do not create RTL acceptance criteria unless the task explicitly introduces an RTL language.

### Touch targets

- Android interactive controls should meet at least `48dp`.
- iOS interactive controls should meet at least `44pt`.
- This is especially important for:
  - icon-only buttons (action icons, toggles, hide/show controls)
  - rating controls
  - compact list rows with embedded actions
  - tab/filter chips

Android Compose check:

```kotlin
composeRule.onNodeWithTag("action_icon")
    .assertHeightIsAtLeast(48.dp)
    .assertWidthIsAtLeast(48.dp)
```

iOS check:

```swift
// Verify minimum 44pt touch target
let button = app.buttons["hideReview"]
XCTAssertGreaterThanOrEqual(button.frame.height, 44)
```

### Localized text checks

For UI that ships to multiple markets, verify that localized copy:

- is not clipped
- is not ellipsized in a broken way
- still leaves room for badges, counters, or action icons

Use at least `RU`, `MN`, and `EN` market variants when the task changes dense UI.

### Stable automation hooks

- Prefer stable semantics or accessibility identifiers for important controls.
- Decorative icons must not become separately focusable if the parent row is the real action.
- Badge counters should be announced meaningfully, for example as `2 pending reviews`, not as a bare number.

### Native screen reader passes

For high-risk UI changes, request at least one manual assistive-tech pass:

- TalkBack on Android
- VoiceOver on iOS

If manual a11y validation was not done, say that clearly in the result.
