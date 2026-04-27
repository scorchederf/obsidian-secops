---
sigma_id: "ee5e119b-1f75-4b34-add8-3be976961e39"
title: "Conhost.exe CommandLine Path Traversal"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_conhost_path_traversal.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_conhost_path_traversal.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ee5e119b-1f75-4b34-add8-3be976961e39"
  - "Conhost.exe CommandLine Path Traversal"
attack_technique_ids:
  - "T1059.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

detects the usage of path traversal in conhost.exe indicating possible command/argument confusion/hijacking

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]

## Detection

```yaml
selection:
  ParentCommandLine|contains: conhost
  CommandLine|contains: /../../
condition: selection
```

## False Positives

- Unlikely

## References

- https://pentestlab.blog/2020/07/06/indirect-command-execution/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_conhost_path_traversal.yml)
