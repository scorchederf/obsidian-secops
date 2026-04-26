---
sigma_id: "4e25af4b-246d-44ea-8563-e42aacab006b"
title: "Potential Xterm Reverse Shell"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_xterm_reverse_shell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_xterm_reverse_shell.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "4e25af4b-246d-44ea-8563-e42aacab006b"
  - "Potential Xterm Reverse Shell"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Xterm Reverse Shell

Detects usage of "xterm" as a potential reverse shell tunnel

## Metadata

- Rule ID: 4e25af4b-246d-44ea-8563-e42aacab006b
- Status: test
- Level: medium
- Author: @d4ns4n_
- Date: 2023-04-24
- Source Path: rules/linux/process_creation/proc_creation_lnx_xterm_reverse_shell.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
  Image|contains: xterm
  CommandLine|contains: -display
  CommandLine|endswith: :1
condition: selection
```

## False Positives

- Unknown

## References

- https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
- https://www.revshells.com/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_xterm_reverse_shell.yml)
