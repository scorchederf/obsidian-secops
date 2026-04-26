---
sigma_id: "1e75c1cc-c5d4-42aa-ac3d-91b0b68b3b4c"
title: "Arbitrary File Download Via Squirrel.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_squirrel_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_squirrel_download.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "1e75c1cc-c5d4-42aa-ac3d-91b0b68b3b4c"
  - "Arbitrary File Download Via Squirrel.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Arbitrary File Download Via Squirrel.EXE

Detects the usage of the "Squirrel.exe" to download arbitrary files. This binary is part of multiple Electron based software installations (Slack, Teams, Discord, etc.)

## Metadata

- Rule ID: 1e75c1cc-c5d4-42aa-ac3d-91b0b68b3b4c
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Karneades / Markus Neis, Jonhnathan Ribeiro, oscd.community
- Date: 2022-06-09
- Modified: 2023-11-09
- Source Path: rules/windows/process_creation/proc_creation_win_squirrel_download.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
  Image|endswith:
  - \squirrel.exe
  - \update.exe
selection_download_cli:
  CommandLine|contains:
  - ' --download '
  - ' --update '
  - ' --updateRollback='
selection_download_http_keyword:
  CommandLine|contains: http
condition: all of selection_*
```

## False Positives

- Expected FP with some Electron based applications such as (1Clipboard, Beaker Browser, Caret, Discord, GitHub Desktop, etc.)

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Squirrel/
- http://www.hexacorn.com/blog/2019/03/30/sqirrel-packages-manager-as-a-lolbin-a-k-a-many-electron-apps-are-lolbins-by-default/
- http://www.hexacorn.com/blog/2018/08/16/squirrel-as-a-lolbin/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_squirrel_download.yml)
