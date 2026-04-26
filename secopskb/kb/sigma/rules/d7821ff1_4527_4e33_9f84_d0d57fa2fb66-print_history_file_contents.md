---
sigma_id: "d7821ff1-4527-4e33-9f84-d0d57fa2fb66"
title: "Print History File Contents"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_history_recon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_history_recon.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "d7821ff1-4527-4e33-9f84-d0d57fa2fb66"
  - "Print History File Contents"
attack_technique_ids:
  - "T1592.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Print History File Contents

Detects events in which someone prints the contents of history files to the commandline or redirects it to a file for reconnaissance

## Metadata

- Rule ID: d7821ff1-4527-4e33-9f84-d0d57fa2fb66
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-06-20
- Modified: 2022-09-15
- Source Path: rules/linux/process_creation/proc_creation_lnx_susp_history_recon.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1592-gather_victim_host_information|T1592.004]]

## Detection

```yaml
selection:
  Image|endswith:
  - /cat
  - /head
  - /tail
  - /more
selection_history:
- CommandLine|contains:
  - /.bash_history
  - /.zsh_history
- CommandLine|endswith:
  - _history
  - .history
  - zhistory
condition: all of selection*
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/sleventyeleven/linuxprivchecker/
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1552.003/T1552.003.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_history_recon.yml)
