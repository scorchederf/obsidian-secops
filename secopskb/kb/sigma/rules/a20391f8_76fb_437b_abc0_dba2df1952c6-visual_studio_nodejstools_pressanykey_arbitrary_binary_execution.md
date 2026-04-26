---
sigma_id: "a20391f8-76fb-437b-abc0-dba2df1952c6"
title: "Visual Studio NodejsTools PressAnyKey Arbitrary Binary Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pressanykey_lolbin_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pressanykey_lolbin_execution.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "a20391f8-76fb-437b-abc0-dba2df1952c6"
  - "Visual Studio NodejsTools PressAnyKey Arbitrary Binary Execution"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Visual Studio NodejsTools PressAnyKey Arbitrary Binary Execution

Detects child processes of Microsoft.NodejsTools.PressAnyKey.exe that can be used to execute any other binary

## Metadata

- Rule ID: a20391f8-76fb-437b-abc0-dba2df1952c6
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-01-11
- Modified: 2023-04-11
- Source Path: rules/windows/process_creation/proc_creation_win_pressanykey_lolbin_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  ParentImage|endswith: \Microsoft.NodejsTools.PressAnyKey.exe
condition: selection
```

## False Positives

- Legitimate use by developers as part of NodeJS development with Visual Studio Tools

## References

- https://twitter.com/mrd0x/status/1463526834918854661
- https://gist.github.com/nasbench/a989ce64cefa8081bd50cf6ad8c491b5

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pressanykey_lolbin_execution.yml)
