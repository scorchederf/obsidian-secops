---
sigma_id: "7bdde3bf-2a42-4c39-aa31-a92b3e17afac"
title: "HackTool - LittleCorporal Generated Maldoc Injection"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_hktl_littlecorporal_generated_maldoc.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_hktl_littlecorporal_generated_maldoc.yml"
build_date: "2026-04-27 19:13:51"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the process injection of a LittleCorporal generated Maldoc.

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution#^t1204002-malicious-file|T1204.002: Malicious File]]
- [[kb/attack/techniques/T1055-process_injection#^t1055003-thread-execution-hijacking|T1055.003: Thread Execution Hijacking]]

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
