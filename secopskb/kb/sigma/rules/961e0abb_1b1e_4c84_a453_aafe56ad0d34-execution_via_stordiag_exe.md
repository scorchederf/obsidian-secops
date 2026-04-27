---
sigma_id: "961e0abb-1b1e-4c84-a453-aafe56ad0d34"
title: "Execution via stordiag.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_stordiag_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_stordiag_susp_child_process.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "961e0abb-1b1e-4c84-a453-aafe56ad0d34"
  - "Execution via stordiag.exe"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of stordiag.exe to execute schtasks.exe systeminfo.exe and fltmc.exe

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detection

```yaml
selection:
  ParentImage|endswith: \stordiag.exe
  Image|endswith:
  - \schtasks.exe
  - \systeminfo.exe
  - \fltmc.exe
filter:
  ParentImage|startswith:
  - c:\windows\system32\
  - c:\windows\syswow64\
condition: selection and not filter
```

## False Positives

- Legitimate usage of stordiag.exe.

## References

- https://strontic.github.io/xcyclopedia/library/stordiag.exe-1F08FC87C373673944F6A7E8B18CD845.html
- https://twitter.com/eral4m/status/1451112385041911809

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_stordiag_susp_child_process.yml)
