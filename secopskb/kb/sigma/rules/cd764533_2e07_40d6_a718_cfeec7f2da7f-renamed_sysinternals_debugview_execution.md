---
sigma_id: "cd764533-2e07-40d6-a718-cfeec7f2da7f"
title: "Renamed SysInternals DebugView Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_sysinternals_debugview.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_sysinternals_debugview.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "cd764533-2e07-40d6-a718-cfeec7f2da7f"
  - "Renamed SysInternals DebugView Execution"
attack_technique_ids:
  - "T1588.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious renamed SysInternals DebugView execution

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1588-obtain_capabilities#^t1588002-tool|T1588.002: Tool]]

## Detection

```yaml
selection:
  Product: Sysinternals DebugView
filter:
  OriginalFileName: Dbgview.exe
  Image|endswith: \Dbgview.exe
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://www.epicturla.com/blog/sysinturla

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_sysinternals_debugview.yml)
