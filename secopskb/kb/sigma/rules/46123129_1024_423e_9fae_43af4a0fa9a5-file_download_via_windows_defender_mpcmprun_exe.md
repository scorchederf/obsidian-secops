---
sigma_id: "46123129-1024-423e-9fae-43af4a0fa9a5"
title: "File Download Via Windows Defender MpCmpRun.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mpcmdrun_download_arbitrary_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mpcmdrun_download_arbitrary_file.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "46123129-1024-423e-9fae-43af4a0fa9a5"
  - "File Download Via Windows Defender MpCmpRun.EXE"
attack_technique_ids:
  - "T1218"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File Download Via Windows Defender MpCmpRun.EXE

Detects the use of Windows Defender MpCmdRun.EXE to download files

## Metadata

- Rule ID: 46123129-1024-423e-9fae-43af4a0fa9a5
- Status: test
- Level: high
- Author: Matthew Matchen
- Date: 2020-09-04
- Modified: 2023-11-09
- Source Path: rules/windows/process_creation/proc_creation_win_mpcmdrun_download_arbitrary_file.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection_img:
- OriginalFileName: MpCmdRun.exe
- Image|endswith: \MpCmdRun.exe
- CommandLine|contains: MpCmdRun.exe
- Description: Microsoft Malware Protection Command Line Utility
selection_cli:
  CommandLine|contains|all:
  - DownloadFile
  - url
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://web.archive.org/web/20200903194959/https://twitter.com/djmtshepana/status/1301608169496612866
- https://lolbas-project.github.io/lolbas/Binaries/MpCmdRun/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mpcmdrun_download_arbitrary_file.yml)
