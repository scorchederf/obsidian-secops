---
sigma_id: "9f107a84-532c-41af-b005-8d12a607639f"
title: "Potentially Suspicious Cabinet File Expansion"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_expand_cabinet_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_expand_cabinet_files.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9f107a84-532c-41af-b005-8d12a607639f"
  - "Potentially Suspicious Cabinet File Expansion"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Cabinet File Expansion

Detects the expansion or decompression of cabinet files from potentially suspicious or uncommon locations, e.g. seen in Iranian MeteorExpress related attacks

## Metadata

- Rule ID: 9f107a84-532c-41af-b005-8d12a607639f
- Status: test
- Level: medium
- Author: Bhabesh Raj, X__Junior (Nextron Systems)
- Date: 2021-07-30
- Modified: 2024-11-13
- Source Path: rules/windows/process_creation/proc_creation_win_expand_cabinet_files.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_cmd:
  Image|endswith: \expand.exe
  CommandLine|contains|windash: '-F:'
selection_folders_1:
  CommandLine|contains:
  - :\Perflogs\
  - :\ProgramData
  - :\Users\Public\
  - :\Windows\Temp\
  - \Admin$\
  - \AppData\Local\Temp\
  - \AppData\Roaming\
  - \C$\
  - \Temporary Internet
selection_folders_2:
- CommandLine|contains|all:
  - :\Users\
  - \Favorites\
- CommandLine|contains|all:
  - :\Users\
  - \Favourites\
- CommandLine|contains|all:
  - :\Users\
  - \Contacts\
filter_optional_dell:
  ParentImage: C:\Program Files (x86)\Dell\UpdateService\ServiceShell.exe
  CommandLine|contains: C:\ProgramData\Dell\UpdateService\Temp\
condition: selection_cmd and 1 of selection_folders_* and not 1 of filter_optional_*
```

## False Positives

- System administrator Usage

## References

- https://labs.sentinelone.com/meteorexpress-mysterious-wiper-paralyzes-iranian-trains-with-epic-troll
- https://blog.malwarebytes.com/threat-intelligence/2021/08/new-variant-of-konni-malware-used-in-campaign-targetting-russia/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_expand_cabinet_files.yml)
