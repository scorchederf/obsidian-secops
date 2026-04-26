---
sigma_id: "51719bf5-e4fd-4e44-8ba8-b830e7ac0731"
title: "Creation Of A Local User Account"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_create_account.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_create_account.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "low"
logsource: "macos / process_creation"
aliases:
  - "51719bf5-e4fd-4e44-8ba8-b830e7ac0731"
  - "Creation Of A Local User Account"
attack_technique_ids:
  - "T1136.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Creation Of A Local User Account

Detects the creation of a new user account. Such accounts may be used for persistence that do not require persistent remote access tools to be deployed on the system.

## Metadata

- Rule ID: 51719bf5-e4fd-4e44-8ba8-b830e7ac0731
- Status: test
- Level: low
- Author: Alejandro Ortuno, oscd.community
- Date: 2020-10-06
- Modified: 2023-02-18
- Source Path: rules/macos/process_creation/proc_creation_macos_create_account.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1136-create_account|T1136.001]]

## Detection

```yaml
selection_dscl:
  Image|endswith: /dscl
  CommandLine|contains: create
selection_sysadminctl:
  Image|endswith: /sysadminctl
  CommandLine|contains: addUser
condition: 1 of selection_*
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1136.001/T1136.001.md
- https://ss64.com/osx/sysadminctl.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_create_account.yml)
