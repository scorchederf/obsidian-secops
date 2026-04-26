---
sigma_id: "9d4548fa-bba0-4e88-bd66-5d5bf516cda0"
title: "Masquerading as Linux Crond Process"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_masquerading_crond.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_masquerading_crond.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "linux / auditd"
aliases:
  - "9d4548fa-bba0-4e88-bd66-5d5bf516cda0"
  - "Masquerading as Linux Crond Process"
attack_technique_ids:
  - "T1036.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Masquerading as Linux Crond Process

Masquerading occurs when the name or location of an executable, legitimate or malicious, is manipulated or abused for the sake of evading defenses and observation.
Several different variations of this technique have been observed.

## Metadata

- Rule ID: 9d4548fa-bba0-4e88-bd66-5d5bf516cda0
- Status: test
- Level: medium
- Author: Timur Zinniatullin, oscd.community
- Date: 2019-10-21
- Modified: 2023-08-22
- Source Path: rules/linux/auditd/execve/lnx_auditd_masquerading_crond.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

## Detection

```yaml
selection:
  type: execve
  a0: cp
  a1: /bin/sh
  a2|endswith: /crond
condition: selection
```

## References

- https://github.com/redcanaryco/atomic-red-team/blob/8a82e9b66a5b4f4bc5b91089e9f24e0544f20ad7/atomics/T1036.003/T1036.003.md#atomic-test-2---masquerading-as-linux-crond-process

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_masquerading_crond.yml)
