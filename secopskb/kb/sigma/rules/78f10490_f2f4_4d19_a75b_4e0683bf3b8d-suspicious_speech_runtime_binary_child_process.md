---
sigma_id: "78f10490-f2f4-4d19-a75b-4e0683bf3b8d"
title: "Suspicious Speech Runtime Binary Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_speechruntime_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_speechruntime_child_process.yml"
build_date: "2026-04-26 17:03:23"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "78f10490-f2f4-4d19-a75b-4e0683bf3b8d"
  - "Suspicious Speech Runtime Binary Child Process"
attack_technique_ids:
  - "T1021.003"
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Speech Runtime Binary Child Process

Detects suspicious Speech Runtime Binary Execution by monitoring its child processes.
Child processes spawned by SpeechRuntime.exe could indicate an attempt for lateral movement via COM & DCOM hijacking.

## Metadata

- Rule ID: 78f10490-f2f4-4d19-a75b-4e0683bf3b8d
- Status: experimental
- Level: high
- Author: andrewdanis
- Date: 2025-10-23
- Source Path: rules/windows/process_creation/proc_creation_win_speechruntime_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.003]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  ParentImage|endswith: \SpeechRuntime.exe
condition: selection
```

## False Positives

- Unlikely.

## References

- https://github.com/rtecCyberSec/SpeechRuntimeMove

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_speechruntime_child_process.yml)
