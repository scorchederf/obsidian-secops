---
sigma_id: "f35c5d71-b489-4e22-a115-f003df287317"
title: "Potential CobaltStrike Process Patterns"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_cobaltstrike_process_patterns.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_cobaltstrike_process_patterns.yml"
build_date: "2026-04-26 15:01:48"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f35c5d71-b489-4e22-a115-f003df287317"
  - "Potential CobaltStrike Process Patterns"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential CobaltStrike Process Patterns

Detects potential process patterns related to Cobalt Strike beacon activity

## Metadata

- Rule ID: f35c5d71-b489-4e22-a115-f003df287317
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-07-27
- Modified: 2023-03-29
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_cobaltstrike_process_patterns.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_generic_1:
  CommandLine|endswith: cmd.exe /C whoami
  ParentImage|startswith: C:\Temp\
selection_generic_2:
  ParentImage|endswith:
  - \runonce.exe
  - \dllhost.exe
  CommandLine|contains|all:
  - cmd.exe /c echo
  - '> \\\\.\\pipe'
selection_conhost_1:
  ParentCommandLine|contains|all:
  - cmd.exe /C echo
  - ' > \\\\.\\pipe'
  CommandLine|endswith: conhost.exe 0xffffffff -ForceV1
selection_conhost_2:
  ParentCommandLine|endswith: /C whoami
  CommandLine|endswith: conhost.exe 0xffffffff -ForceV1
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://hausec.com/2021/07/26/cobalt-strike-and-tradecraft/
- https://thedfirreport.com/2021/08/29/cobalt-strike-a-defenders-guide/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_cobaltstrike_process_patterns.yml)
