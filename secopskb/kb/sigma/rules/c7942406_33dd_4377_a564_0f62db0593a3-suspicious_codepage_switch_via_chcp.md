---
sigma_id: "c7942406-33dd-4377-a564-0f62db0593a3"
title: "Suspicious CodePage Switch Via CHCP"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_chcp_codepage_switch.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_chcp_codepage_switch.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c7942406-33dd-4377-a564-0f62db0593a3"
  - "Suspicious CodePage Switch Via CHCP"
attack_technique_ids:
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious CodePage Switch Via CHCP

Detects a code page switch in command line or batch scripts to a rare language

## Metadata

- Rule ID: c7942406-33dd-4377-a564-0f62db0593a3
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Jonhnathan Ribeiro, oscd.community
- Date: 2019-10-14
- Modified: 2023-03-07
- Source Path: rules/windows/process_creation/proc_creation_win_chcp_codepage_switch.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection:
  Image|endswith: \chcp.com
  CommandLine|endswith:
  - ' 936'
  - ' 1258'
condition: selection
```

## False Positives

- Administrative activity (adjust code pages according to your organization's region)

## References

- https://learn.microsoft.com/en-us/windows/win32/intl/code-page-identifiers
- https://twitter.com/cglyer/status/1183756892952248325

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_chcp_codepage_switch.yml)
