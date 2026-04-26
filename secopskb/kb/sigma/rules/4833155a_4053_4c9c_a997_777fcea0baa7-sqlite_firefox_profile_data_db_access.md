---
sigma_id: "4833155a-4053-4c9c-a997-777fcea0baa7"
title: "SQLite Firefox Profile Data DB Access"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sqlite_firefox_gecko_profile_data.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sqlite_firefox_gecko_profile_data.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "4833155a-4053-4c9c-a997-777fcea0baa7"
  - "SQLite Firefox Profile Data DB Access"
attack_technique_ids:
  - "T1539"
  - "T1005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# SQLite Firefox Profile Data DB Access

Detect usage of the "sqlite" binary to query databases in Firefox and other Gecko-based browsers for potential data stealing.

## Metadata

- Rule ID: 4833155a-4053-4c9c-a997-777fcea0baa7
- Status: test
- Level: high
- Author: frack113
- Date: 2022-04-08
- Modified: 2023-01-19
- Source Path: rules/windows/process_creation/proc_creation_win_sqlite_firefox_gecko_profile_data.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1539-steal_web_session_cookie|T1539]]
- [[kb/attack/techniques/T1005-data_from_local_system|T1005]]

## Detection

```yaml
selection_sql:
- Product: SQLite
- Image|endswith:
  - \sqlite.exe
  - \sqlite3.exe
selection_firefox:
  CommandLine|contains:
  - cookies.sqlite
  - places.sqlite
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1539/T1539.md#atomic-test-1---steal-firefox-cookies-windows
- https://blog.cyble.com/2022/04/21/prynt-stealer-a-new-info-stealer-performing-clipper-and-keylogger-activities/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sqlite_firefox_gecko_profile_data.yml)
