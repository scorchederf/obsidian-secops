---
sigma_id: "35f41cd7-c98e-469f-8a02-ec4ba0cc7a7e"
title: "PowerShell Write-EventLog Usage"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_write_eventlog.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_write_eventlog.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "35f41cd7-c98e-469f-8a02-ec4ba0cc7a7e"
  - "PowerShell Write-EventLog Usage"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Write-EventLog Usage

Detects usage of the "Write-EventLog" cmdlet with 'RawData' flag. The cmdlet can be levreage to write malicious payloads to the EventLog and then retrieve them later for later use

## Metadata

- Rule ID: 35f41cd7-c98e-469f-8a02-ec4ba0cc7a7e
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-16
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_write_eventlog.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - Write-EventLog
  - '-RawData '
condition: selection
```

## False Positives

- Legitimate applications writing events via this cmdlet. Investigate alerts to determine if the action is benign

## References

- https://www.blackhillsinfosec.com/windows-event-logs-for-red-teams/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_write_eventlog.yml)
