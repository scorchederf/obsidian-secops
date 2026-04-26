---
sigma_id: "725a9768-0f5e-4cb3-aec2-bc5719c6831a"
title: "Suspicious Where Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_where_browser_data_recon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_where_browser_data_recon.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "725a9768-0f5e-4cb3-aec2-bc5719c6831a"
  - "Suspicious Where Execution"
attack_technique_ids:
  - "T1217"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Where Execution

Adversaries may enumerate browser bookmarks to learn more about compromised hosts.
Browser bookmarks may reveal personal information about users (ex: banking sites, interests, social media, etc.) as well as details about
internal network resources such as servers, tools/dashboards, or other related infrastructure.

## Metadata

- Rule ID: 725a9768-0f5e-4cb3-aec2-bc5719c6831a
- Status: test
- Level: low
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-12-13
- Modified: 2022-06-29
- Source Path: rules/windows/process_creation/proc_creation_win_where_browser_data_recon.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1217-browser_information_discovery|T1217]]

## Detection

```yaml
where_exe:
- Image|endswith: \where.exe
- OriginalFileName: where.exe
where_opt:
  CommandLine|contains:
  - places.sqlite
  - cookies.sqlite
  - formhistory.sqlite
  - logins.json
  - key4.db
  - key3.db
  - sessionstore.jsonlz4
  - History
  - Bookmarks
  - Cookies
  - Login Data
condition: all of where_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1217/T1217.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_where_browser_data_recon.yml)
