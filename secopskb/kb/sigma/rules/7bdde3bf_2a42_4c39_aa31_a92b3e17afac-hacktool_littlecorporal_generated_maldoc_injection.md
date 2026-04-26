---
sigma_id: "7bdde3bf-2a42-4c39-aa31-a92b3e17afac"
title: "HackTool - LittleCorporal Generated Maldoc Injection"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_hktl_littlecorporal_generated_maldoc.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_hktl_littlecorporal_generated_maldoc.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / process_access"
aliases:
  - "7bdde3bf-2a42-4c39-aa31-a92b3e17afac"
  - "HackTool - LittleCorporal Generated Maldoc Injection"
attack_technique_ids:
  - "T1204.002"
  - "T1055.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - LittleCorporal Generated Maldoc Injection

Detects the process injection of a LittleCorporal generated Maldoc.

## Metadata

- Rule ID: 7bdde3bf-2a42-4c39-aa31-a92b3e17afac
- Status: test
- Level: high
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-08-09
- Modified: 2023-11-28
- Source Path: rules/windows/process_access/proc_access_win_hktl_littlecorporal_generated_maldoc.yml

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]
- [[kb/attack/techniques/T1055-process_injection|T1055.003]]

## Detection

```yaml
selection:
  SourceImage|endswith: \winword.exe
  CallTrace|contains|all:
  - :\Windows\Microsoft.NET\Framework64\v2.
  - UNKNOWN
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/connormcgarr/LittleCorporal

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_hktl_littlecorporal_generated_maldoc.yml)
