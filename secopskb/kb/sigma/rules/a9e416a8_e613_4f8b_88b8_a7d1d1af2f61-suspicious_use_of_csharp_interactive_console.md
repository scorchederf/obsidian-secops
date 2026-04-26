---
sigma_id: "a9e416a8-e613-4f8b-88b8-a7d1d1af2f61"
title: "Suspicious Use of CSharp Interactive Console"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_csi_use_of_csharp_console.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_csi_use_of_csharp_console.yml"
build_date: "2026-04-26 15:01:52"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Use of CSharp Interactive Console

Detects the execution of CSharp interactive console by PowerShell

## Metadata

- Rule ID: a9e416a8-e613-4f8b-88b8-a7d1d1af2f61
- Status: test
- Level: high
- Author: Michael R. (@nahamike01)
- Date: 2020-03-08
- Modified: 2022-07-14
- Source Path: rules/windows/process_creation/proc_creation_win_csi_use_of_csharp_console.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

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
