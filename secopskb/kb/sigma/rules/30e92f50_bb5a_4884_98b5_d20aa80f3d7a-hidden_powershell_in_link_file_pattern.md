---
sigma_id: "30e92f50-bb5a-4884-98b5-d20aa80f3d7a"
title: "Hidden Powershell in Link File Pattern"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_embed_exe_lnk.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_embed_exe_lnk.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "30e92f50-bb5a-4884-98b5-d20aa80f3d7a"
  - "Hidden Powershell in Link File Pattern"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Hidden Powershell in Link File Pattern

Detects events that appear when a user click on a link file with a powershell command in it

## Metadata

- Rule ID: 30e92f50-bb5a-4884-98b5-d20aa80f3d7a
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-02-06
- Source Path: rules/windows/process_creation/proc_creation_win_susp_embed_exe_lnk.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  ParentImage: C:\Windows\explorer.exe
  Image: C:\Windows\System32\cmd.exe
  CommandLine|contains|all:
  - powershell
  - .lnk
condition: selection
```

## False Positives

- Legitimate commands in .lnk files

## References

- https://www.x86matthew.com/view_post?id=embed_exe_lnk

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_embed_exe_lnk.yml)
