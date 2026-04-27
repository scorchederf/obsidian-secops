---
sigma_id: "81a0ecb5-0a41-4ba1-b2ba-c944eb92bfa2"
title: "Add Insecure Download Source To Winget"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_winget_add_insecure_custom_source.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winget_add_insecure_custom_source.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "81a0ecb5-0a41-4ba1-b2ba-c944eb92bfa2"
  - "Add Insecure Download Source To Winget"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects usage of winget to add a new insecure (http) download source.
Winget will not allow the addition of insecure sources, hence this could indicate potential suspicious activity (or typos)

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]

## Detection

```yaml
selection_img:
- Image|endswith: \winget.exe
- OriginalFileName: winget.exe
selection_cli:
  CommandLine|contains|all:
  - 'source '
  - 'add '
  - http://
condition: all of selection_*
```

## False Positives

- False positives might occur if the users are unaware of such control checks

## References

- https://learn.microsoft.com/en-us/windows/package-manager/winget/source
- https://github.com/nasbench/Misc-Research/tree/b9596e8109dcdb16ec353f316678927e507a5b8d/LOLBINs/Winget

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winget_add_insecure_custom_source.yml)
