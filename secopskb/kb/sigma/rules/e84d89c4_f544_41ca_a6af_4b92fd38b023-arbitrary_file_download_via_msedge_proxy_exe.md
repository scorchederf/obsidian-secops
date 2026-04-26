---
sigma_id: "e84d89c4-f544-41ca-a6af-4b92fd38b023"
title: "Arbitrary File Download Via MSEDGE_PROXY.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_msedge_proxy_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msedge_proxy_download.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "e84d89c4-f544-41ca-a6af-4b92fd38b023"
  - "Arbitrary File Download Via MSEDGE_PROXY.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Arbitrary File Download Via MSEDGE_PROXY.EXE

Detects usage of "msedge_proxy.exe" to download arbitrary files

## Metadata

- Rule ID: e84d89c4-f544-41ca-a6af-4b92fd38b023
- Status: test
- Level: medium
- Author: Swachchhanda Shrawan Poudel
- Date: 2023-11-09
- Source Path: rules/windows/process_creation/proc_creation_win_msedge_proxy_download.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \msedge_proxy.exe
- OriginalFileName: msedge_proxy.exe
selection_cli:
  CommandLine|contains:
  - http://
  - https://
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/msedge_proxy/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msedge_proxy_download.yml)
