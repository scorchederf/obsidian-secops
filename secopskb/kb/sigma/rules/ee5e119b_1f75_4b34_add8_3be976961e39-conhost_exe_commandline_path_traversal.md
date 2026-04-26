---
sigma_id: "ee5e119b-1f75-4b34-add8-3be976961e39"
title: "Conhost.exe CommandLine Path Traversal"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_conhost_path_traversal.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_conhost_path_traversal.yml"
build_date: "2026-04-26 15:01:44"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Conhost.exe CommandLine Path Traversal

detects the usage of path traversal in conhost.exe indicating possible command/argument confusion/hijacking

## Metadata

- Rule ID: ee5e119b-1f75-4b34-add8-3be976961e39
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-14
- Source Path: rules/windows/process_creation/proc_creation_win_conhost_path_traversal.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]

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
