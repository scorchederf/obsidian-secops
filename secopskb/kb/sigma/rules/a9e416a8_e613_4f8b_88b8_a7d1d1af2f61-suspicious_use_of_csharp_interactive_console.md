---
sigma_id: "a9e416a8-e613-4f8b-88b8-a7d1d1af2f61"
title: "Suspicious Use of CSharp Interactive Console"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_csi_use_of_csharp_console.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_csi_use_of_csharp_console.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a9e416a8-e613-4f8b-88b8-a7d1d1af2f61"
  - "Suspicious Use of CSharp Interactive Console"
attack_technique_ids:
  - "T1127"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of CSharp interactive console by PowerShell

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

## Detection

```yaml
selection:
  Image|endswith: \csi.exe
  ParentImage|endswith:
  - \powershell.exe
  - \pwsh.exe
  - \powershell_ise.exe
  OriginalFileName: csi.exe
condition: selection
```

## False Positives

- Possible depending on environment. Pair with other factors such as net connections, command-line args, etc.

## References

- https://redcanary.com/blog/detecting-attacks-leveraging-the-net-framework/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_csi_use_of_csharp_console.yml)
