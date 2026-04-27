---
sigma_id: "24c77512-782b-448a-8950-eddb0785fc71"
title: "SQLite Chromium Profile Data DB Access"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sqlite_chromium_profile_data.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sqlite_chromium_profile_data.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "24c77512-782b-448a-8950-eddb0785fc71"
  - "SQLite Chromium Profile Data DB Access"
attack_technique_ids:
  - "T1539"
  - "T1555.003"
  - "T1005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detect usage of the "sqlite" binary to query databases in Chromium-based browsers for potential data stealing.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1539-steal_web_session_cookie|T1539: Steal Web Session Cookie]]
- [[kb/attack/techniques/T1555-credentials_from_password_stores#^t1555003-credentials-from-web-browsers|T1555.003: Credentials from Web Browsers]]
- [[kb/attack/techniques/T1005-data_from_local_system|T1005: Data from Local System]]

## Detection

```yaml
selection_sql:
- Product: SQLite
- Image|endswith:
  - \sqlite.exe
  - \sqlite3.exe
selection_chromium:
  CommandLine|contains:
  - \User Data\
  - \Opera Software\
  - \ChromiumViewer\
selection_data:
  CommandLine|contains:
  - Login Data
  - Cookies
  - Web Data
  - History
  - Bookmarks
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/84d9edaaaa2c5511144521b0e4af726d1c7276ce/atomics/T1539/T1539.md#atomic-test-2---steal-chrome-cookies-windows
- https://blog.cyble.com/2022/04/21/prynt-stealer-a-new-info-stealer-performing-clipper-and-keylogger-activities/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sqlite_chromium_profile_data.yml)
