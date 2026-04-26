---
sigma_id: "0f017df3-8f5a-414f-ad6b-24aff1128278"
title: "Suspicious Eventlog Clear"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_clear_eventlog.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_clear_eventlog.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "0f017df3-8f5a-414f-ad6b-24aff1128278"
  - "Suspicious Eventlog Clear"
attack_technique_ids:
  - "T1070.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Eventlog Clear

Detects usage of known powershell cmdlets such as "Clear-EventLog" to clear the Windows event logs

## Metadata

- Rule ID: 0f017df3-8f5a-414f-ad6b-24aff1128278
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2022-09-12
- Modified: 2025-10-06
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_clear_eventlog.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.001]]

## Detection

```yaml
selection:
- ScriptBlockText|contains:
  - 'Clear-EventLog '
  - 'Remove-EventLog '
  - 'Limit-EventLog '
  - 'Clear-WinEvent '
- ScriptBlockText|contains|all:
  - Eventing.Reader.EventLogSession
  - ClearLog
- ScriptBlockText|contains|all:
  - Diagnostics.EventLog
  - Clear
condition: selection
```

## False Positives

- Rare need to clear logs before doing something. Sometimes used by installers or cleaner scripts. The script should be investigated to determine if it's legitimate

## References

- https://twitter.com/oroneequalsone/status/1568432028361830402
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.001/T1070.001.md
- https://eqllib.readthedocs.io/en/latest/analytics/5b223758-07d6-4100-9e11-238cfdd0fe97.html
- https://stackoverflow.com/questions/66011412/how-to-clear-a-event-log-in-powershell-7
- https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.eventing.reader.eventlogsession.clearlog?view=windowsdesktop-9.0&viewFallbackFrom=dotnet-plat-ext-5.0#System_Diagnostics_Eventing_Reader_EventLogSession_ClearLog_System_String_
- https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.eventlog.clear

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_clear_eventlog.yml)
