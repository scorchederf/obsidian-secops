---
sigma_id: "fb4e2211-6d08-426b-8e6f-0d4a161e3b1d"
title: "Clfs.SYS Loaded By Process Located In a Potential Suspicious Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_clfs_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_clfs_load.yml"
build_date: "2026-04-26 14:14:22"
status: "experimental"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "fb4e2211-6d08-426b-8e6f-0d4a161e3b1d"
  - "Clfs.SYS Loaded By Process Located In a Potential Suspicious Location"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Clfs.SYS Loaded By Process Located In a Potential Suspicious Location

Detects Clfs.sys being loaded by a process running from a potentially suspicious location. Clfs.sys is loaded as part of many CVEs exploits that targets Common Log File.

## Metadata

- Rule ID: fb4e2211-6d08-426b-8e6f-0d4a161e3b1d
- Status: experimental
- Level: medium
- Author: X__Junior
- Date: 2025-01-20
- Source Path: rules/windows/image_load/image_load_clfs_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_dll:
  ImageLoaded|endswith: \clfs.sys
selection_folders_1:
  Image|contains:
  - :\Perflogs\
  - :\Users\Public\
  - \Temporary Internet
  - \Windows\Temp\
selection_folders_2:
- Image|contains|all:
  - :\Users\
  - \Favorites\
- Image|contains|all:
  - :\Users\
  - \Favourites\
- Image|contains|all:
  - :\Users\
  - \Contacts\
- Image|contains|all:
  - :\Users\
  - \Pictures\
condition: selection_dll and 1 of selection_folders_*
```

## False Positives

- Unknown

## References

- https://ssd-disclosure.com/ssd-advisory-common-log-file-system-clfs-driver-pe/
- https://x.com/Threatlabz/status/1879956781360976155

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_clfs_load.yml)
