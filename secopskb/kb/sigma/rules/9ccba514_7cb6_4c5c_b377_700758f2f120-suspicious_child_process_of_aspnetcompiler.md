---
sigma_id: "9ccba514-7cb6-4c5c-b377-700758f2f120"
title: "Suspicious Child Process of AspNetCompiler"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_aspnet_compiler_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_aspnet_compiler_susp_child_process.yml"
build_date: "2026-04-27 19:13:56"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects potentially suspicious child processes of "aspnet_compiler.exe".

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

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
