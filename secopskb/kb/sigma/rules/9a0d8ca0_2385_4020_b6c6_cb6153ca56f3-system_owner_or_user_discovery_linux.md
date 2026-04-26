---
sigma_id: "9a0d8ca0-2385-4020-b6c6-cb6153ca56f3"
title: "System Owner or User Discovery - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_user_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_user_discovery.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "low"
logsource: "linux / auditd"
aliases:
  - "9a0d8ca0-2385-4020-b6c6-cb6153ca56f3"
  - "System Owner or User Discovery - Linux"
attack_technique_ids:
  - "T1033"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Owner or User Discovery - Linux

Detects the execution of host or user discovery utilities such as "whoami", "hostname", "id", etc.
Adversaries may use the information from System Owner/User Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

## Metadata

- Rule ID: 9a0d8ca0-2385-4020-b6c6-cb6153ca56f3
- Status: test
- Level: low
- Author: Timur Zinniatullin, oscd.community
- Date: 2019-10-21
- Modified: 2025-06-04
- Source Path: rules/linux/auditd/execve/lnx_auditd_user_discovery.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]

## Detection

```yaml
selection:
  type: EXECVE
  a0:
  - hostname
  - id
  - last
  - uname
  - users
  - w
  - who
  - whoami
condition: selection
```

## False Positives

- Admin activity

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1033/T1033.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_user_discovery.yml)
