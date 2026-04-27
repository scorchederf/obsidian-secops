---
sigma_id: "b2815d0d-7481-4bf0-9b6c-a4c48a94b349"
title: "PowerShell Get-Process LSASS"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_getprocess_lsass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_getprocess_lsass.yml"
build_date: "2026-04-27 19:13:55"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a "Get-Process" cmdlet and it's aliases on lsass process, which is in almost all cases a sign of malicious activity

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552004-private-keys|T1552.004: Private Keys]]

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
