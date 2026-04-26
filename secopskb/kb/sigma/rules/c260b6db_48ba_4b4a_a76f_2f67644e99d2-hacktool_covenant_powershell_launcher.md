---
sigma_id: "c260b6db-48ba-4b4a-a76f-2f67644e99d2"
title: "HackTool - Covenant PowerShell Launcher"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_covenant.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_covenant.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c260b6db-48ba-4b4a-a76f-2f67644e99d2"
  - "HackTool - Covenant PowerShell Launcher"
attack_technique_ids:
  - "T1059.001"
  - "T1564.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - Covenant PowerShell Launcher

Detects suspicious command lines used in Covenant luanchers

## Metadata

- Rule ID: c260b6db-48ba-4b4a-a76f-2f67644e99d2
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Jonhnathan Ribeiro, oscd.community
- Date: 2020-06-04
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_covenant.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1564-hide_artifacts|T1564.003]]

## Detection

```yaml
selection_1:
  CommandLine|contains|all:
  - -Sta
  - -Nop
  - -Window
  - Hidden
  CommandLine|contains:
  - -Command
  - -EncodedCommand
selection_2:
  CommandLine|contains:
  - 'sv o (New-Object IO.MemorySteam);sv d '
  - mshta file.hta
  - GruntHTTP
  - -EncodedCommand cwB2ACAAbwAgA
condition: 1 of selection_*
```

## References

- https://posts.specterops.io/covenant-v0-5-eee0507b85ba

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_covenant.yml)
