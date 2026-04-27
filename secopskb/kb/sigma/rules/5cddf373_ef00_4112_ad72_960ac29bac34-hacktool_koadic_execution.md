---
sigma_id: "5cddf373-ef00-4112-ad72-960ac29bac34"
title: "HackTool - Koadic Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_koadic.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_koadic.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "5cddf373-ef00-4112-ad72-960ac29bac34"
  - "HackTool - Koadic Execution"
attack_technique_ids:
  - "T1059.003"
  - "T1059.005"
  - "T1059.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects command line parameters used by Koadic hack tool

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059005-visual-basic|T1059.005: Visual Basic]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059007-javascript|T1059.007: JavaScript]]

## Detection

```yaml
selection_img:
- Image|endswith: \cmd.exe
- OriginalFileName: Cmd.Exe
selection_cli:
  CommandLine|contains|all:
  - /q
  - /c
  - chcp
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://unit42.paloaltonetworks.com/unit42-sofacy-groups-parallel-attacks/
- https://github.com/offsecginger/koadic/blob/457f9a3ff394c989cdb4c599ab90eb34fb2c762c/data/stager/js/stdlib.js
- https://blog.f-secure.com/hunting-for-koadic-a-com-based-rootkit/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_koadic.yml)
