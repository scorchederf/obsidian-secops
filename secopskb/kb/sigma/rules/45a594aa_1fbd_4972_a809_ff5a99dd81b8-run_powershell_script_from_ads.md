---
sigma_id: "45a594aa-1fbd-4972-a809-ff5a99dd81b8"
title: "Run PowerShell Script from ADS"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_run_script_from_ads.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_run_script_from_ads.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "45a594aa-1fbd-4972-a809-ff5a99dd81b8"
  - "Run PowerShell Script from ADS"
attack_technique_ids:
  - "T1564.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects PowerShell script execution from Alternate Data Stream (ADS)

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]

## Detection

```yaml
selection:
  ParentImage|endswith:
  - \powershell.exe
  - \pwsh.exe
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  CommandLine|contains|all:
  - Get-Content
  - -Stream
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/p0shkatz/Get-ADS/blob/1c3a3562e713c254edce1995a7d9879c687c7473/Get-ADS.ps1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_run_script_from_ads.yml)
