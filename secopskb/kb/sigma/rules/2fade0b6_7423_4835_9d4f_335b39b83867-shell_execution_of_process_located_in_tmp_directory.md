---
sigma_id: "2fade0b6-7423-4835-9d4f-335b39b83867"
title: "Shell Execution Of Process Located In Tmp Directory"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_shell_child_process_from_parent_tmp_folder.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_shell_child_process_from_parent_tmp_folder.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "2fade0b6-7423-4835-9d4f-335b39b83867"
  - "Shell Execution Of Process Located In Tmp Directory"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects execution of shells from a parent process located in a temporary (/tmp) directory

## Logsource

- category: process_creation
- product: linux

## Detection

```yaml
selection:
  ParentImage|startswith: /tmp/
  Image|endswith:
  - /bash
  - /csh
  - /dash
  - /fish
  - /ksh
  - /sh
  - /zsh
condition: selection
```

## False Positives

- Unknown

## References

- https://blogs.jpcert.or.jp/en/2023/05/gobrat.html
- https://jstnk9.github.io/jstnk9/research/GobRAT-Malware/
- https://www.virustotal.com/gui/file/60bcd645450e4c846238cf0e7226dc40c84c96eba99f6b2cffcd0ab4a391c8b3/detection
- https://www.virustotal.com/gui/file/3e44c807a25a56f4068b5b8186eee5002eed6f26d665a8b791c472ad154585d1/detection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_shell_child_process_from_parent_tmp_folder.yml)
