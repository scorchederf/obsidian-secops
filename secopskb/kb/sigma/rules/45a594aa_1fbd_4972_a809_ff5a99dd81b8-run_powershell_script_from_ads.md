---
sigma_id: "45a594aa-1fbd-4972-a809-ff5a99dd81b8"
title: "Run PowerShell Script from ADS"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_run_script_from_ads.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_run_script_from_ads.yml"
build_date: "2026-04-26 14:14:35"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Run PowerShell Script from ADS

Detects PowerShell script execution from Alternate Data Stream (ADS)

## Metadata

- Rule ID: 45a594aa-1fbd-4972-a809-ff5a99dd81b8
- Status: test
- Level: high
- Author: Sergey Soldatov, Kaspersky Lab, oscd.community
- Date: 2019-10-30
- Modified: 2022-07-14
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_run_script_from_ads.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

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
