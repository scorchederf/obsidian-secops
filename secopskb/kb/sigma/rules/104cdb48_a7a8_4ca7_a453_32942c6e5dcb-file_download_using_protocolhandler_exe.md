---
sigma_id: "104cdb48-a7a8-4ca7-a453-32942c6e5dcb"
title: "File Download Using ProtocolHandler.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_protocolhandler_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_protocolhandler_download.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "104cdb48-a7a8-4ca7-a453-32942c6e5dcb"
  - "File Download Using ProtocolHandler.exe"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File Download Using ProtocolHandler.exe

Detects usage of "ProtocolHandler" to download files. Downloaded files will be located in the cache folder (for example - %LOCALAPPDATA%\Microsoft\Windows\INetCache\IE)

## Metadata

- Rule ID: 104cdb48-a7a8-4ca7-a453-32942c6e5dcb
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-07-13
- Modified: 2023-11-09
- Source Path: rules/windows/process_creation/proc_creation_win_protocolhandler_download.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \protocolhandler.exe
- OriginalFileName: ProtocolHandler.exe
selection_cli:
  CommandLine|contains:
  - ftp://
  - http://
  - https://
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218/T1218.md
- https://lolbas-project.github.io/lolbas/OtherMSBinaries/ProtocolHandler/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_protocolhandler_download.yml)
