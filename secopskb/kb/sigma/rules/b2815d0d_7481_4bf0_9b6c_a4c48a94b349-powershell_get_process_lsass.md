---
sigma_id: "b2815d0d-7481-4bf0-9b6c-a4c48a94b349"
title: "PowerShell Get-Process LSASS"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_getprocess_lsass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_getprocess_lsass.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b2815d0d-7481-4bf0-9b6c-a4c48a94b349"
  - "PowerShell Get-Process LSASS"
attack_technique_ids:
  - "T1552.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Get-Process LSASS

Detects a "Get-Process" cmdlet and it's aliases on lsass process, which is in almost all cases a sign of malicious activity

## Metadata

- Rule ID: b2815d0d-7481-4bf0-9b6c-a4c48a94b349
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-04-23
- Modified: 2023-01-05
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_getprocess_lsass.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.004]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - Get-Process lsas
  - ps lsas
  - gps lsas
condition: selection
```

## False Positives

- Unknown

## References

- https://web.archive.org/web/20220205033028/https://twitter.com/PythonResponder/status/1385064506049630211

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_getprocess_lsass.yml)
