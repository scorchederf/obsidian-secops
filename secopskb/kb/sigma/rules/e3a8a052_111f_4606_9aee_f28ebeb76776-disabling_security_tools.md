---
sigma_id: "e3a8a052-111f-4606-9aee-f28ebeb76776"
title: "Disabling Security Tools"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_security_tools_disabling.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_security_tools_disabling.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "e3a8a052-111f-4606-9aee-f28ebeb76776"
  - "Disabling Security Tools"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Disabling Security Tools

Detects disabling security tools

## Metadata

- Rule ID: e3a8a052-111f-4606-9aee-f28ebeb76776
- Status: test
- Level: medium
- Author: Ömer Günal, Alejandro Ortuno, oscd.community
- Date: 2020-06-17
- Modified: 2022-10-09
- Source Path: rules/linux/process_creation/proc_creation_lnx_security_tools_disabling.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Detection

```yaml
selection_iptables_1:
  Image|endswith: /service
  CommandLine|contains|all:
  - iptables
  - stop
selection_iptables_2:
  Image|endswith: /service
  CommandLine|contains|all:
  - ip6tables
  - stop
selection_iptables_3:
  Image|endswith: /chkconfig
  CommandLine|contains|all:
  - iptables
  - stop
selection_iptables_4:
  Image|endswith: /chkconfig
  CommandLine|contains|all:
  - ip6tables
  - stop
selection_firewall_1:
  Image|endswith: /systemctl
  CommandLine|contains|all:
  - firewalld
  - stop
selection_firewall_2:
  Image|endswith: /systemctl
  CommandLine|contains|all:
  - firewalld
  - disable
selection_carbonblack_1:
  Image|endswith: /service
  CommandLine|contains|all:
  - cbdaemon
  - stop
selection_carbonblack_2:
  Image|endswith: /chkconfig
  CommandLine|contains|all:
  - cbdaemon
  - 'off'
selection_carbonblack_3:
  Image|endswith: /systemctl
  CommandLine|contains|all:
  - cbdaemon
  - stop
selection_carbonblack_4:
  Image|endswith: /systemctl
  CommandLine|contains|all:
  - cbdaemon
  - disable
selection_selinux:
  Image|endswith: /setenforce
  CommandLine|contains: '0'
selection_crowdstrike_1:
  Image|endswith: /systemctl
  CommandLine|contains|all:
  - stop
  - falcon-sensor
selection_crowdstrike_2:
  Image|endswith: /systemctl
  CommandLine|contains|all:
  - disable
  - falcon-sensor
condition: 1 of selection*
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.004/T1562.004.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_security_tools_disabling.yml)
