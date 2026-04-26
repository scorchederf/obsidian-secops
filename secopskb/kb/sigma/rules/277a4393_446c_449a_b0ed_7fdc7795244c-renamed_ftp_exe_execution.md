---
sigma_id: "277a4393-446c-449a-b0ed-7fdc7795244c"
title: "Renamed FTP.EXE Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_ftp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_ftp.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "277a4393-446c-449a-b0ed-7fdc7795244c"
  - "Renamed FTP.EXE Execution"
attack_technique_ids:
  - "T1059"
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Renamed FTP.EXE Execution

Detects the execution of a renamed "ftp.exe" binary based on the PE metadata fields

## Metadata

- Rule ID: 277a4393-446c-449a-b0ed-7fdc7795244c
- Status: test
- Level: medium
- Author: Victor Sergeev, oscd.community
- Date: 2020-10-09
- Modified: 2023-02-03
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_ftp.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]
- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection_original:
  OriginalFileName: ftp.exe
filter_img:
  Image|endswith: \ftp.exe
condition: selection_original and not filter_img
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Ftp/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_ftp.yml)
