---
sigma_id: "727454c0-d851-48b0-8b89-385611ab0704"
title: "Lolbin Unregmp2.exe Use As Proxy"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_unregmp2.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_unregmp2.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "727454c0-d851-48b0-8b89-385611ab0704"
  - "Lolbin Unregmp2.exe Use As Proxy"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Lolbin Unregmp2.exe Use As Proxy

Detect usage of the "unregmp2.exe" binary as a proxy to launch a custom version of "wmpnscfg.exe"

## Metadata

- Rule ID: 727454c0-d851-48b0-8b89-385611ab0704
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-12-29
- Modified: 2024-06-04
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_unregmp2.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \unregmp2.exe
- OriginalFileName: unregmp2.exe
selection_cmd:
  CommandLine|contains|windash: ' /HideWMP'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Unregmp2/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_unregmp2.yml)
