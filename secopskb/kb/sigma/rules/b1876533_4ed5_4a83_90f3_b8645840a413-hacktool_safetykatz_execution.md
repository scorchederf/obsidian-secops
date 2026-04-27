---
sigma_id: "b1876533-4ed5-4a83-90f3-b8645840a413"
title: "HackTool - SafetyKatz Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_safetykatz.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_safetykatz.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "b1876533-4ed5-4a83-90f3-b8645840a413"
  - "HackTool - SafetyKatz Execution"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of the hacktool SafetyKatz via PE information and default Image name

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Detection

```yaml
selection:
- Image|endswith: \SafetyKatz.exe
- OriginalFileName: SafetyKatz.exe
- Description: SafetyKatz
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/GhostPack/SafetyKatz

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_safetykatz.yml)
