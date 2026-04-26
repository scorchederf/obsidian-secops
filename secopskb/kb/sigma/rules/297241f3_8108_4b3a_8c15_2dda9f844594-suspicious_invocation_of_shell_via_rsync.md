---
sigma_id: "297241f3-8108-4b3a-8c15-2dda9f844594"
title: "Suspicious Invocation of Shell via Rsync"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_rsync_shell_spawn.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_rsync_shell_spawn.yml"
build_date: "2026-04-26 14:14:36"
status: "experimental"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "297241f3-8108-4b3a-8c15-2dda9f844594"
  - "Suspicious Invocation of Shell via Rsync"
attack_technique_ids:
  - "T1059"
  - "T1203"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Invocation of Shell via Rsync

Detects the execution of a shell as sub process of "rsync" without the expected command line flag "-e" being used, which could be an indication of exploitation as described in CVE-2024-12084. This behavior is commonly associated with attempts to execute arbitrary commands or escalate privileges, potentially leading to unauthorized access or further exploitation.

## Metadata

- Rule ID: 297241f3-8108-4b3a-8c15-2dda9f844594
- Status: experimental
- Level: high
- Author: Florian Roth
- Date: 2025-01-18
- Source Path: rules/linux/process_creation/proc_creation_lnx_rsync_shell_spawn.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]
- [[kb/attack/techniques/T1203-exploitation_for_client_execution|T1203]]

## Detection

```yaml
selection:
  ParentImage|endswith:
  - /rsync
  - /rsyncd
  Image|endswith:
  - /ash
  - /bash
  - /csh
  - /dash
  - /ksh
  - /sh
  - /tcsh
  - /zsh
filter_main_expected:
  CommandLine|contains: ' -e '
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://sysdig.com/blog/detecting-and-mitigating-cve-2024-12084-rsync-remote-code-execution/
- https://gist.github.com/Neo23x0/a20436375a1e26524931dd8ea1a3af10

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_rsync_shell_spawn.yml)
