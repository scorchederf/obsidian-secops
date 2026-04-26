---
sigma_id: "100ef69e-3327-481c-8e5c-6d80d9507556"
title: "Important Windows Eventlog Cleared"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/microsoft_windows_eventlog/win_system_susp_eventlog_cleared.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_eventlog/win_system_susp_eventlog_cleared.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "100ef69e-3327-481c-8e5c-6d80d9507556"
  - "Important Windows Eventlog Cleared"
attack_technique_ids:
  - "T1070.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Important Windows Eventlog Cleared

Detects the clearing of one of the Windows Core Eventlogs. e.g. caused by "wevtutil cl" command execution

## Metadata

- Rule ID: 100ef69e-3327-481c-8e5c-6d80d9507556
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Tim Shelton, Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-05-17
- Modified: 2023-11-15
- Source Path: rules/windows/builtin/system/microsoft_windows_eventlog/win_system_susp_eventlog_cleared.yml

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
  Channel:
  - Microsoft-Windows-PowerShell/Operational
  - Microsoft-Windows-Sysmon/Operational
  - PowerShellCore/Operational
  - Security
  - System
  - Windows PowerShell
condition: selection
```

## False Positives

- Rollout of log collection agents (the setup routine often includes a reset of the local Eventlog)
- System provisioning (system reset before the golden image creation)

## References

- https://twitter.com/deviouspolack/status/832535435960209408
- https://www.hybrid-analysis.com/sample/027cc450ef5f8c5f653329641ec1fed91f694e0d229928963b30f6b0d7d3a745?environmentId=100

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_eventlog/win_system_susp_eventlog_cleared.yml)
