---
sigma_id: "df1f26d3-bea7-4700-9ea2-ad3e990cf90e"
title: "Node Process Executions"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_node_adobe_creative_cloud_abuse.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_node_adobe_creative_cloud_abuse.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "df1f26d3-bea7-4700-9ea2-ad3e990cf90e"
  - "Node Process Executions"
attack_technique_ids:
  - "T1127"
  - "T1059.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Node Process Executions

Detects the execution of other scripts using the Node executable packaged with Adobe Creative Cloud

## Metadata

- Rule ID: df1f26d3-bea7-4700-9ea2-ad3e990cf90e
- Status: test
- Level: medium
- Author: Max Altgelt (Nextron Systems)
- Date: 2022-04-06
- Source Path: rules/windows/process_creation/proc_creation_win_node_adobe_creative_cloud_abuse.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.007]]

## Detection

```yaml
selection:
  Image|endswith: \Adobe Creative Cloud Experience\libs\node.exe
filter:
  CommandLine|contains: Adobe Creative Cloud Experience\js
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://twitter.com/mttaggart/status/1511804863293784064

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_node_adobe_creative_cloud_abuse.yml)
