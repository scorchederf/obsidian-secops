---
sigma_id: "a16980c2-0c56-4de0-9a79-17971979efdd"
title: "Cmd.EXE Missing Space Characters Execution Anomaly"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_no_space_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_no_space_execution.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a16980c2-0c56-4de0-9a79-17971979efdd"
  - "Cmd.EXE Missing Space Characters Execution Anomaly"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Cmd.EXE Missing Space Characters Execution Anomaly

Detects Windows command lines that miss a space before or after the /c flag when running a command using the cmd.exe.
This could be a sign of obfuscation of a fat finger problem (typo by the developer).

## Metadata

- Rule ID: a16980c2-0c56-4de0-9a79-17971979efdd
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-08-23
- Modified: 2023-03-06
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_no_space_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection1:
  CommandLine|contains:
  - cmd.exe/c
  - \cmd/c
  - '"cmd/c'
  - cmd.exe/k
  - \cmd/k
  - '"cmd/k'
  - cmd.exe/r
  - \cmd/r
  - '"cmd/r'
selection2:
  CommandLine|contains:
  - /cwhoami
  - /cpowershell
  - /cschtasks
  - /cbitsadmin
  - /ccertutil
  - /kwhoami
  - /kpowershell
  - /kschtasks
  - /kbitsadmin
  - /kcertutil
selection3:
  CommandLine|contains:
  - cmd.exe /c
  - cmd /c
  - cmd.exe /k
  - cmd /k
  - cmd.exe /r
  - cmd /r
filter_generic:
  CommandLine|contains:
  - 'cmd.exe /c '
  - 'cmd /c '
  - 'cmd.exe /k '
  - 'cmd /k '
  - 'cmd.exe /r '
  - 'cmd /r '
filter_fp:
- CommandLine|contains: AppData\Local\Programs\Microsoft VS Code\resources\app\node_modules
- CommandLine|endswith: cmd.exe/c .
- CommandLine: cmd.exe /c
condition: 1 of selection* and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://twitter.com/cyb3rops/status/1562072617552678912
- https://ss64.com/nt/cmd.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_no_space_execution.yml)
