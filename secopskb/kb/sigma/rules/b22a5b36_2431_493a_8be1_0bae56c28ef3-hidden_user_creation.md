---
sigma_id: "b22a5b36-2431-493a-8be1-0bae56c28ef3"
title: "Hidden User Creation"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_create_hidden_account.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_create_hidden_account.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "b22a5b36-2431-493a-8be1-0bae56c28ef3"
  - "Hidden User Creation"
attack_technique_ids:
  - "T1564.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Hidden User Creation

Detects creation of a hidden user account on macOS (UserID < 500) or with IsHidden option

## Metadata

- Rule ID: b22a5b36-2431-493a-8be1-0bae56c28ef3
- Status: test
- Level: medium
- Author: Daniil Yugoslavskiy, oscd.community
- Date: 2020-10-10
- Modified: 2021-11-27
- Source Path: rules/macos/process_creation/proc_creation_macos_create_hidden_account.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.002]]

## Detection

```yaml
dscl_create:
  Image|endswith: /dscl
  CommandLine|contains: create
id_below_500:
  CommandLine|contains: UniqueID
  CommandLine|re: ([0-9]|[1-9][0-9]|[1-4][0-9]{2})
ishidden_option_declaration:
  CommandLine|contains: IsHidden
ishidden_option_confirmation:
  CommandLine|contains:
  - 'true'
  - 'yes'
  - '1'
condition: dscl_create and id_below_500 or dscl_create and (ishidden_option_declaration
  and ishidden_option_confirmation)
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1564.002/T1564.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_create_hidden_account.yml)
