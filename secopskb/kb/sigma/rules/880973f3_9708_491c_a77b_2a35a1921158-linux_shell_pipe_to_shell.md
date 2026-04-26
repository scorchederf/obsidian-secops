---
sigma_id: "880973f3-9708-491c-a77b-2a35a1921158"
title: "Linux Shell Pipe to Shell"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_pipe_shell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_pipe_shell.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "880973f3-9708-491c-a77b-2a35a1921158"
  - "Linux Shell Pipe to Shell"
attack_technique_ids:
  - "T1140"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Linux Shell Pipe to Shell

Detects suspicious process command line that starts with a shell that executes something and finally gets piped into another shell

## Metadata

- Rule ID: 880973f3-9708-491c-a77b-2a35a1921158
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-03-14
- Modified: 2022-07-26
- Source Path: rules/linux/process_creation/proc_creation_lnx_susp_pipe_shell.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140]]

## Detection

```yaml
selection:
  CommandLine|startswith:
  - 'sh -c '
  - 'bash -c '
selection_exec:
- CommandLine|contains:
  - '| bash '
  - '| sh '
  - '|bash '
  - '|sh '
- CommandLine|endswith:
  - '| bash'
  - '| sh'
  - '|bash'
  - ' |sh'
condition: all of selection*
```

## False Positives

- Legitimate software that uses these patterns

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_pipe_shell.yml)
