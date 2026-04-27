---
sigma_id: "115fdba9-f017-42e6-84cf-d5573bf2ddf8"
title: "Disable of ETW Trace - Powershell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_etw_trace_evasion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_etw_trace_evasion.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "115fdba9-f017-42e6-84cf-d5573bf2ddf8"
  - "Disable of ETW Trace - Powershell"
attack_technique_ids:
  - "T1070"
  - "T1562.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Disable of ETW Trace - Powershell

Detects usage of powershell cmdlets to disable or remove ETW trace sessions

## Metadata

- Rule ID: 115fdba9-f017-42e6-84cf-d5573bf2ddf8
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-28
- Modified: 2022-11-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_etw_trace_evasion.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562.006]]

## Detection

```yaml
selection_pwsh_remove:
  ScriptBlockText|contains: 'Remove-EtwTraceProvider '
selection_pwsh_set:
  ScriptBlockText|contains|all:
  - 'Set-EtwTraceProvider '
  - '0x11'
condition: 1 of selection*
```

## False Positives

- Unknown

## References

- https://medium.com/palantir/tampering-with-windows-event-tracing-background-offense-and-defense-4be7ac62ac63

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_etw_trace_evasion.yml)
