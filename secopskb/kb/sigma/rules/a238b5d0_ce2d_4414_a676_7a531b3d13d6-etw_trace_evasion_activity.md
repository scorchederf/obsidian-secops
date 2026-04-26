---
sigma_id: "a238b5d0-ce2d-4414-a676-7a531b3d13d6"
title: "ETW Trace Evasion Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_etw_trace_evasion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_etw_trace_evasion.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a238b5d0-ce2d-4414-a676-7a531b3d13d6"
  - "ETW Trace Evasion Activity"
attack_technique_ids:
  - "T1070"
  - "T1562.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ETW Trace Evasion Activity

Detects command line activity that tries to clear or disable any ETW trace log which could be a sign of logging evasion.

## Metadata

- Rule ID: a238b5d0-ce2d-4414-a676-7a531b3d13d6
- Status: test
- Level: high
- Author: @neu5ron, Florian Roth (Nextron Systems), Jonhnathan Ribeiro, oscd.community
- Date: 2019-03-22
- Modified: 2022-06-28
- Source Path: rules/windows/process_creation/proc_creation_win_susp_etw_trace_evasion.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562.006]]

## Detection

```yaml
selection_clear_1:
  CommandLine|contains|all:
  - cl
  - /Trace
selection_clear_2:
  CommandLine|contains|all:
  - clear-log
  - /Trace
selection_disable_1:
  CommandLine|contains|all:
  - sl
  - /e:false
selection_disable_2:
  CommandLine|contains|all:
  - set-log
  - /e:false
selection_disable_3:
  CommandLine|contains|all:
  - logman
  - update
  - trace
  - --p
  - -ets
selection_pwsh_remove:
  CommandLine|contains: Remove-EtwTraceProvider
selection_pwsh_set:
  CommandLine|contains|all:
  - Set-EtwTraceProvider
  - '0x11'
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil
- https://abuse.io/lockergoga.txt
- https://medium.com/palantir/tampering-with-windows-event-tracing-background-offense-and-defense-4be7ac62ac63

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_etw_trace_evasion.yml)
