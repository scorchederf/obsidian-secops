---
sigma_id: "06b401f4-107c-4ff9-947f-9ec1e7649f1e"
title: "Potential Arbitrary Command Execution Via FTP.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_ftp_arbitrary_command_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ftp_arbitrary_command_execution.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "06b401f4-107c-4ff9-947f-9ec1e7649f1e"
  - "Potential Arbitrary Command Execution Via FTP.EXE"
attack_technique_ids:
  - "T1059"
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Arbitrary Command Execution Via FTP.EXE

Detects execution of "ftp.exe" script with the "-s" or "/s" flag and any child processes ran by "ftp.exe".

## Metadata

- Rule ID: 06b401f4-107c-4ff9-947f-9ec1e7649f1e
- Status: test
- Level: medium
- Author: Victor Sergeev, oscd.community
- Date: 2020-10-09
- Modified: 2024-04-23
- Source Path: rules/windows/process_creation/proc_creation_win_ftp_arbitrary_command_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]
- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \ftp.exe
selection_child_img:
- Image|endswith: \ftp.exe
- OriginalFileName: ftp.exe
selection_child_cli:
  CommandLine|contains|windash: '-s:'
condition: selection_parent or all of selection_child_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Ftp/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ftp_arbitrary_command_execution.yml)
