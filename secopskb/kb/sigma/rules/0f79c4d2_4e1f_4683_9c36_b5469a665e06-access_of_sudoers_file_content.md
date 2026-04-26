---
sigma_id: "0f79c4d2-4e1f-4683-9c36-b5469a665e06"
title: "Access of Sudoers File Content"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_process_reading_sudoers.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_process_reading_sudoers.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "0f79c4d2-4e1f-4683-9c36-b5469a665e06"
  - "Access of Sudoers File Content"
attack_technique_ids:
  - "T1592.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Access of Sudoers File Content

Detects the execution of a text-based file access or inspection utilities to read the content of /etc/sudoers in order to potentially list all users that have sudo rights.

## Metadata

- Rule ID: 0f79c4d2-4e1f-4683-9c36-b5469a665e06
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-06-20
- Modified: 2025-06-04
- Source Path: rules/linux/process_creation/proc_creation_lnx_susp_process_reading_sudoers.yml

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
  - /ed
  - /egrep
  - /emacs
  - /fgrep
  - /grep
  - /head
  - /less
  - /more
  - /nano
  - /tail
  CommandLine|contains: ' /etc/sudoers'
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/sleventyeleven/linuxprivchecker/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_process_reading_sudoers.yml)
