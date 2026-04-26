---
sigma_id: "a62b37e0-45d3-48d9-a517-90c1a1b0186b"
title: "Eventlog Cleared"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/microsoft_windows_eventlog/win_system_eventlog_cleared.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_eventlog/win_system_eventlog_cleared.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / system"
aliases:
  - "a62b37e0-45d3-48d9-a517-90c1a1b0186b"
  - "Eventlog Cleared"
attack_technique_ids:
  - "T1070.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Eventlog Cleared

One of the Windows Eventlogs has been cleared. e.g. caused by "wevtutil cl" command execution

## Metadata

- Rule ID: a62b37e0-45d3-48d9-a517-90c1a1b0186b
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2017-01-10
- Modified: 2023-11-15
- Source Path: rules/windows/builtin/system/microsoft_windows_eventlog/win_system_eventlog_cleared.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.001]]

## Detection

```yaml
selection:
  EventID: 104
  Provider_Name: Microsoft-Windows-Eventlog
filter_main_covered:
  Channel:
  - Microsoft-Windows-PowerShell/Operational
  - Microsoft-Windows-Sysmon/Operational
  - PowerShellCore/Operational
  - Security
  - System
  - Windows PowerShell
condition: selection and not 1 of filter_main_*
```

## False Positives

- Rollout of log collection agents (the setup routine often includes a reset of the local Eventlog)
- System provisioning (system reset before the golden image creation)

## References

- https://twitter.com/deviouspolack/status/832535435960209408
- https://www.hybrid-analysis.com/sample/027cc450ef5f8c5f653329641ec1fed91f694e0d229928963b30f6b0d7d3a745?environmentId=100

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_eventlog/win_system_eventlog_cleared.yml)
