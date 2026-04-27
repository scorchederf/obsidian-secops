---
sigma_id: "044ba588-dff4-4918-9808-3f95e8160606"
title: "Copy .DMP/.DUMP Files From Remote Share Via Cmd.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_copy_dmp_from_share.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_copy_dmp_from_share.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "044ba588-dff4-4918-9808-3f95e8160606"
  - "Copy .DMP/.DUMP Files From Remote Share Via Cmd.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects usage of the copy builtin cmd command to copy files with the ".dmp"/".dump" extension from a remote share

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \cmd.exe
- OriginalFileName: Cmd.Exe
selection_cli:
  CommandLine|contains|all:
  - 'copy '
  - ' \\\\'
  CommandLine|contains:
  - .dmp
  - .dump
  - .hdmp
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2022/09/26/bumblebee-round-two/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_copy_dmp_from_share.yml)
