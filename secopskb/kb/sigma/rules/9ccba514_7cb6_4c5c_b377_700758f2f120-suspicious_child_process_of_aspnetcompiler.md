---
sigma_id: "9ccba514-7cb6-4c5c-b377-700758f2f120"
title: "Suspicious Child Process of AspNetCompiler"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_aspnet_compiler_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_aspnet_compiler_susp_child_process.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9ccba514-7cb6-4c5c-b377-700758f2f120"
  - "Suspicious Child Process of AspNetCompiler"
attack_technique_ids:
  - "T1127"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Child Process of AspNetCompiler

Detects potentially suspicious child processes of "aspnet_compiler.exe".

## Metadata

- Rule ID: 9ccba514-7cb6-4c5c-b377-700758f2f120
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-14
- Source Path: rules/windows/process_creation/proc_creation_win_aspnet_compiler_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \aspnet_compiler.exe
selection_child:
- Image|endswith:
  - \calc.exe
  - \notepad.exe
- Image|contains:
  - \Users\Public\
  - \AppData\Local\Temp\
  - \AppData\Local\Roaming\
  - :\Temp\
  - :\Windows\Temp\
  - :\Windows\System32\Tasks\
  - :\Windows\Tasks\
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Aspnet_Compiler/
- https://ijustwannared.team/2020/08/01/the-curious-case-of-aspnet_compiler-exe/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_aspnet_compiler_susp_child_process.yml)
