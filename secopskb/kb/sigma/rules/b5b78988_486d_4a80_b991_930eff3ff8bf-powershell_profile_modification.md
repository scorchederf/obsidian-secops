---
sigma_id: "b5b78988-486d-4a80-b991-930eff3ff8bf"
title: "PowerShell Profile Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_powershell_profile.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_powershell_profile.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "b5b78988-486d-4a80-b991-930eff3ff8bf"
  - "PowerShell Profile Modification"
attack_technique_ids:
  - "T1546.013"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Profile Modification

Detects the creation or modification of a powershell profile which could indicate suspicious activity as the profile can be used as a mean of persistence

## Metadata

- Rule ID: b5b78988-486d-4a80-b991-930eff3ff8bf
- Status: test
- Level: medium
- Author: HieuTT35, Nasreddine Bencherchali (Nextron Systems)
- Date: 2019-10-24
- Modified: 2023-10-23
- Source Path: rules/windows/file/file_event/file_event_win_susp_powershell_profile.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.013]]

## Detection

```yaml
selection:
  TargetFilename|endswith:
  - \Microsoft.PowerShell_profile.ps1
  - \PowerShell\profile.ps1
  - \Program Files\PowerShell\7-preview\profile.ps1
  - \Program Files\PowerShell\7\profile.ps1
  - \Windows\System32\WindowsPowerShell\v1.0\profile.ps1
  - \WindowsPowerShell\profile.ps1
condition: selection
```

## False Positives

- System administrator creating Powershell profile manually

## References

- https://www.welivesecurity.com/2019/05/29/turla-powershell-usage/
- https://persistence-info.github.io/Data/powershellprofile.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_powershell_profile.yml)
