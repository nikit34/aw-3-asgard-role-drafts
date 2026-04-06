## Larixon Multi-Market Web Tests

Replace any platform-level assumptions about other market sets. Larixon web currently serves these real markets:

| Market | Key identifiers | Locale | Currency | Mandatory notes |
| --- | --- | --- | --- | --- |
| Bazaraki | `bazaraki` | `EN` | `EUR` | GDPR/Google privacy rules apply; primary market |
| Somon | `somon` | `RU` | `TJS` | Cyrillic content is common; dedicated Somon stands exist |
| Unegui | `unegui` | `MN` | `MNT` | eMongolia integration |
| Jacars | `jacars` | `en_JM` | `JMD` | Car-market wording and Jamaica locale |
| Pin | `pin` | `en_TT` | `TTD` | Trinidad market |
| Salanto | `salanto` | `EN` | `EUR` | Verify payment-side currency at runtime if flow depends on it |

### Selection rule

- For any user-facing money, locale, or content-sensitive endpoint, test at least three markets:
  - Bazaraki (EUR, English)
  - Somon (TJS, Russian/Cyrillic)
  - Unegui (MNT, Mongolian)
- Add the most affected business market on top of that baseline if the task is market-specific.
- If the task changes a market-only flow, you must include the owning market even if it falls outside the default three-market baseline.

### Market-specific flows

- **Bazaraki**: GDPR-related consent, Google privacy checks, country value "Cyprus" (Latin C, not Cyrillic)
- **Unegui**: eMongolia auth or toggles
- **Somon**: Cyrillic text in user-generated content, Russian labels
- **Jacars**, **Pin**: validate localized labels and currency formatting

### Django settings per market

- Market-specific configuration lives in settings files: `config/settings/{market}.py`
- Use `@override_settings` to switch market context in tests when needed
- For feed tests: market affects `COUNTRY`, locale, currency, and feature flags

Stands and environments: see `200-larixon-web-infra.md`

Example:

```python
from django.test import override_settings

@override_settings(COUNTRY="CY", LANGUAGE_CODE="en", CURRENCY="EUR")
class TestBazarakiFeed(APITestCase):
    def test_feed_uses_eur_currency(self):
        ...
```

### Reporting rule

Always state:

- tested market(s)
- locale-sensitive assertions made
- market-specific branches intentionally skipped and why
