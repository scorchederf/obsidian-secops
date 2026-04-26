---
sigma_id: "7e8f2d3b-9c1a-4f67-b9e8-8d9006e0e51f"
title: "PowerShell Web Access Feature Enabled Via DISM"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dism_enable_powershell_web_access_feature.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dism_enable_powershell_web_access_feature.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "7e8f2d3b-9c1a-4f67-b9e8-8d9006e0e51f"
  - "PowerShell Web Access Feature Enabled Via DISM"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PowerShell Web Access Feature Enabled Via DISM

Detects the use of DISM to enable the PowerShell Web Access feature, which could be used for remote access and potential abuse

## Metadata

- Rule ID: 7e8f2d3b-9c1a-4f67-b9e8-8d9006e0e51f
- Status: test
- Level: high
- Author: Michael Haag
- Date: 2024-09-03
- Source Path: rules/windows/process_creation/proc_creation_win_dism_enable_powershell_web_access_feature.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection_img:
- Image|endswith: \dism.exe
- OriginalFileName: DISM.EXE
selection_cli:
  CommandLine|contains|all:
  - WindowsPowerShellWebAccess
  - /online
  - /enable-feature
condition: all of selection_*
```

## False Positives

- Legitimate PowerShell Web Access installations by administrators

## References

- https://docs.microsoft.com/en-us/powershell/module/dism/enable-windowsoptionalfeature
- https://www.cisa.gov/news-events/cybersecurity-advisories/aa24-241a
- https://gist.github.com/MHaggis/7e67b659af9148fa593cf2402edebb41

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dism_enable_powershell_web_access_feature.yml)
