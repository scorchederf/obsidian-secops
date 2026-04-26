---
sigma_id: "30bcce26-51c5-49f2-99c8-7b59e3af36c7"
title: "Execution Of Script Located In Potentially Suspicious Directory"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_shell_script_exec_from_susp_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_shell_script_exec_from_susp_location.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "30bcce26-51c5-49f2-99c8-7b59e3af36c7"
  - "Execution Of Script Located In Potentially Suspicious Directory"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Execution Of Script Located In Potentially Suspicious Directory

Detects executions of scripts located in potentially suspicious locations such as "/tmp" via a shell such as "bash", "sh", etc.

## Metadata

- Rule ID: 30bcce26-51c5-49f2-99c8-7b59e3af36c7
- Status: test
- Level: medium
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2023-06-02
- Source Path: rules/linux/process_creation/proc_creation_lnx_susp_shell_script_exec_from_susp_location.yml

## Logsource

- category: process_creation
- product: linux

## Detection

```yaml
selection_img:
  Image|endswith:
  - /bash
  - /csh
  - /dash
  - /fish
  - /ksh
  - /sh
  - /zsh
selection_flag:
  CommandLine|contains: ' -c '
selection_paths:
  CommandLine|contains: /tmp/
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://blogs.jpcert.or.jp/en/2023/05/gobrat.html
- https://jstnk9.github.io/jstnk9/research/GobRAT-Malware/
- https://www.virustotal.com/gui/file/60bcd645450e4c846238cf0e7226dc40c84c96eba99f6b2cffcd0ab4a391c8b3/detection
- https://www.virustotal.com/gui/file/3e44c807a25a56f4068b5b8186eee5002eed6f26d665a8b791c472ad154585d1/detection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_shell_script_exec_from_susp_location.yml)
