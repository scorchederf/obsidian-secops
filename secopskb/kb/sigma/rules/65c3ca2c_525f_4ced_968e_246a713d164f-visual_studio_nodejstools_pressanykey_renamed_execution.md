---
sigma_id: "65c3ca2c-525f-4ced-968e-246a713d164f"
title: "Visual Studio NodejsTools PressAnyKey Renamed Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_pressanykey.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_pressanykey.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "65c3ca2c-525f-4ced-968e-246a713d164f"
  - "Visual Studio NodejsTools PressAnyKey Renamed Execution"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Visual Studio NodejsTools PressAnyKey Renamed Execution

Detects renamed execution of "Microsoft.NodejsTools.PressAnyKey.exe", which can be abused as a LOLBIN to execute arbitrary binaries

## Metadata

- Rule ID: 65c3ca2c-525f-4ced-968e-246a713d164f
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Florian Roth (Nextron Systems)
- Date: 2023-04-11
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_pressanykey.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  OriginalFileName: Microsoft.NodejsTools.PressAnyKey.exe
filter_main_legit_name:
  Image|endswith: \Microsoft.NodejsTools.PressAnyKey.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://twitter.com/mrd0x/status/1463526834918854661
- https://gist.github.com/nasbench/a989ce64cefa8081bd50cf6ad8c491b5

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_pressanykey.yml)
