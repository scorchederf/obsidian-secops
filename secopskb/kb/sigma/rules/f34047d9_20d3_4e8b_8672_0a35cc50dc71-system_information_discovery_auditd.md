---
sigma_id: "f34047d9-20d3-4e8b-8672-0a35cc50dc71"
title: "System Information Discovery - Auditd"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/lnx_auditd_system_info_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/lnx_auditd_system_info_discovery.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "low"
logsource: "linux / auditd"
aliases:
  - "f34047d9-20d3-4e8b-8672-0a35cc50dc71"
  - "System Information Discovery - Auditd"
attack_technique_ids:
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Information Discovery - Auditd

Detects System Information Discovery commands

## Metadata

- Rule ID: f34047d9-20d3-4e8b-8672-0a35cc50dc71
- Status: test
- Level: low
- Author: Pawel Mazur
- Date: 2021-09-03
- Modified: 2023-03-06
- Source Path: rules/linux/auditd/lnx_auditd_system_info_discovery.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Detection

```yaml
selection_1:
  type: PATH
  name:
  - /etc/lsb-release
  - /etc/redhat-release
  - /etc/issue
selection_2:
  type: EXECVE
  a0:
  - uname
  - uptime
  - lsmod
  - hostname
  - env
selection_3:
  type: EXECVE
  a0: grep
  a1|contains:
  - vbox
  - vm
  - xen
  - virtio
  - hv
selection_4:
  type: EXECVE
  a0: kmod
  a1: list
condition: 1 of selection_*
```

## False Positives

- Likely

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f296668303c29d3f4c07e42bdd2b28d8dd6625f9/atomics/T1082/T1082.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/lnx_auditd_system_info_discovery.yml)
