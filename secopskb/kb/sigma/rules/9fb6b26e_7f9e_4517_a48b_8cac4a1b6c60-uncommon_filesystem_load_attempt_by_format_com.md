---
sigma_id: "9fb6b26e-7f9e-4517-a48b-8cac4a1b6c60"
title: "Uncommon FileSystem Load Attempt By Format.com"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_format_uncommon_filesystem_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_format_uncommon_filesystem_load.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9fb6b26e-7f9e-4517-a48b-8cac4a1b6c60"
  - "Uncommon FileSystem Load Attempt By Format.com"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of format.com with an uncommon filesystem selection that could indicate a defense evasion activity in which "format.com" is used to load malicious DLL files or other programs.

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  Image|endswith: \format.com
  CommandLine|contains: '/fs:'
filter_main_known_fs:
  CommandLine|contains:
  - /fs:exFAT
  - /fs:FAT
  - /fs:NTFS
  - /fs:ReFS
  - /fs:UDF
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://twitter.com/0gtweet/status/1477925112561209344
- https://twitter.com/wdormann/status/1478011052130459653?s=20

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_format_uncommon_filesystem_load.yml)
