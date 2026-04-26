---
sigma_id: "a24e5861-c6ca-4fde-a93c-ba9256feddf0"
title: "Uncommon Process Access Rights For Target Image"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_susp_all_access_uncommon_target.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_susp_all_access_uncommon_target.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "low"
logsource: "windows / process_access"
aliases:
  - "a24e5861-c6ca-4fde-a93c-ba9256feddf0"
  - "Uncommon Process Access Rights For Target Image"
attack_technique_ids:
  - "T1055.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Uncommon Process Access Rights For Target Image

Detects process access request to uncommon target images with a "PROCESS_ALL_ACCESS" access mask.

## Metadata

- Rule ID: a24e5861-c6ca-4fde-a93c-ba9256feddf0
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems), frack113
- Date: 2024-05-27
- Source Path: rules/windows/process_access/proc_access_win_susp_all_access_uncommon_target.yml

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055.011]]

## Detection

```yaml
selection:
  TargetImage|endswith:
  - \calc.exe
  - \calculator.exe
  - \mspaint.exe
  - \notepad.exe
  - \ping.exe
  - \wordpad.exe
  - \write.exe
  GrantedAccess: '0x1FFFFF'
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/windows/win32/procthread/process-security-and-access-rights

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_susp_all_access_uncommon_target.yml)
