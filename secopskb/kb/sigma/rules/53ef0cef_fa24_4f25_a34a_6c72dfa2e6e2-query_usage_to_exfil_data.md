---
sigma_id: "53ef0cef-fa24-4f25-a34a-6c72dfa2e6e2"
title: "Query Usage To Exfil Data"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_query_session_exfil.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_query_session_exfil.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "53ef0cef-fa24-4f25-a34a-6c72dfa2e6e2"
  - "Query Usage To Exfil Data"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Query Usage To Exfil Data

Detects usage of "query.exe" a system binary to exfil information such as "sessions" and "processes" for later use

## Metadata

- Rule ID: 53ef0cef-fa24-4f25-a34a-6c72dfa2e6e2
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-01
- Modified: 2023-01-19
- Source Path: rules/windows/process_creation/proc_creation_win_query_session_exfil.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  Image|endswith: :\Windows\System32\query.exe
  CommandLine|contains:
  - session >
  - process >
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/MichalKoczwara/status/1553634816016498688

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_query_session_exfil.yml)
