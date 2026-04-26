---
sigma_id: "6a50f16c-3b7b-42d1-b081-0fdd3ba70a73"
title: "User Added To Root/Sudoers Group Using Usermod"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_usermod_susp_group.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_usermod_susp_group.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "6a50f16c-3b7b-42d1-b081-0fdd3ba70a73"
  - "User Added To Root/Sudoers Group Using Usermod"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# User Added To Root/Sudoers Group Using Usermod

Detects usage of the "usermod" binary to add users add users to the root or suoders groups

## Metadata

- Rule ID: 6a50f16c-3b7b-42d1-b081-0fdd3ba70a73
- Status: test
- Level: medium
- Author: TuanLe (GTSC)
- Date: 2022-12-21
- Source Path: rules/linux/process_creation/proc_creation_lnx_usermod_susp_group.yml

## Logsource

- category: process_creation
- product: linux

## Detection

```yaml
selection:
  Image|endswith: /usermod
  CommandLine|contains:
  - -aG root
  - -aG sudoers
condition: selection
```

## False Positives

- Legitimate administrator activities

## References

- https://pberba.github.io/security/2021/11/23/linux-threat-hunting-for-persistence-account-creation-manipulation/
- https://www.configserverfirewall.com/ubuntu-linux/ubuntu-add-user-to-root-group/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_usermod_susp_group.yml)
