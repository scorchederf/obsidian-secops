---
sigma_id: "087790e3-3287-436c-bccf-cbd0184a7db1"
title: "Potential CommandLine Path Traversal Via Cmd.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_path_traversal.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_path_traversal.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "087790e3-3287-436c-bccf-cbd0184a7db1"
  - "Potential CommandLine Path Traversal Via Cmd.EXE"
attack_technique_ids:
  - "T1059.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential CommandLine Path Traversal Via Cmd.EXE

Detects potential path traversal attempt via cmd.exe. Could indicate possible command/argument confusion/hijacking

## Metadata

- Rule ID: 087790e3-3287-436c-bccf-cbd0184a7db1
- Status: test
- Level: high
- Author: xknow @xknow_infosec, Tim Shelton
- Date: 2020-06-11
- Modified: 2023-03-06
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_path_traversal.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]

## Detection

```yaml
selection_img:
- ParentImage|endswith: \cmd.exe
- Image|endswith: \cmd.exe
- OriginalFileName: cmd.exe
selection_flags:
- ParentCommandLine|contains:
  - /c
  - /k
  - /r
- CommandLine|contains:
  - /c
  - /k
  - /r
selection_path_traversal:
- ParentCommandLine: /../../
- CommandLine|contains: /../../
filter_java:
  CommandLine|contains: \Tasktop\keycloak\bin\/../../jre\bin\java
condition: all of selection_* and not 1 of filter_*
```

## False Positives

- Java tools are known to produce false-positive when loading libraries

## References

- https://hackingiscool.pl/cmdhijack-command-argument-confusion-with-path-traversal-in-cmd-exe/
- https://twitter.com/Oddvarmoe/status/1270633613449723905

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_path_traversal.yml)
