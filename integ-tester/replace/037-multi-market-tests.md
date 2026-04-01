## Larixon Multi-Market Mobile Tests

Replace any platform-level assumptions about other market sets. Larixon mobile currently spans these real markets:

| Market | Android flavor | iOS target | Locale | Currency | Mandatory notes |
| --- | --- | --- | --- | --- | --- |
| Bazaraki | `bz` | `Bazaraki` | `EN_us` | `EUR` | `GDPR_GOOGLE` is enabled for this market |
| Somon | `tj` | `Somon.tj` | `RU_ru` | `TJS` | Cyrillic content is common; dedicated Somon stands exist |
| Unegui | `mn` | `Unegui.mn` | `MN_mn` | `MNT` | `EMONGOLIA_ENABLED` is enabled for this market |
| Jacars | `ja` | `Jacars` | `en_JM` | `JMD` | Car-market wording and Jamaica locale |
| Pin | `pn` | `Pin.tt` | `en_TT` | `TTD` | Trinidad market |
| Salanto | `sl` | `Salanto` | `EN_us` | `EUR` | Verify payment-side currency at runtime if flow depends on it |

### Selection rule

- For any user-facing money, locale, or copy-sensitive UI, run at least three markets:
  - `bz`
  - `tj`
  - `mn`
- Add the most affected business market on top of that baseline if the task is market-specific.
- If the task changes a market-only flow, you must include the owning market even if it falls outside the default three-market baseline.
- Prefer native validation paths already available to the team first. Do not silently assume BrowserStack or another cloud-device lab unless the task or owner explicitly puts it in scope.

### Market-specific flows

- `bz`:
  - GDPR-related consent and Google privacy checks are market-specific
- `mn`:
  - eMongolia-related auth or toggles are market-specific
- `tj`, `ja`, `pn`:
  - validate localized labels, formatting, and navigation text instead of assuming one English fallback

### Review-feature expectations

For review-related work, verify across multiple markets:

- badge counter visibility and hidden state
- pending vs completed filter counts
- pending card actions:
  - rate
  - mark as no-deal
  - hide
- completed review rendering:
  - rating
  - tags
  - optional comment
- deep link opening:
  - `lc://profile/reviews`
- advert title/context click-through
- pagination
- empty state text and layout

### Platform mapping rule

- Android:
  - use real flavors from Gradle
- iOS:
  - use real market target and `AppCustomization` values
- If one platform is not in scope for the current sprint, say that clearly and avoid pretending the validation was cross-platform

### Reporting rule

Always state:

- tested market(s)
- platform(s)
- locale-sensitive assertions
- market-specific branches that were intentionally skipped
