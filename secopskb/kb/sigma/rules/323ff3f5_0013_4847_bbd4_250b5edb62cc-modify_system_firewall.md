---
sigma_id: "323ff3f5-0013-4847-bbd4-250b5edb62cc"
title: "Modify System Firewall"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_modify_system_firewall.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_modify_system_firewall.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "linux / auditd"
aliases:
  - "323ff3f5-0013-4847-bbd4-250b5edb62cc"
  - "Modify System Firewall"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Modify System Firewall

Detects the removal of system firewall rules. Adversaries may only delete or modify a specific system firewall rule to bypass controls limiting network usage or access.
Detection rules that match only on the disabling of firewalls will miss this.

## Metadata

- Rule ID: 323ff3f5-0013-4847-bbd4-250b5edb62cc
- Status: test
- Level: medium
- Author: IAI
- Date: 2023-03-06
- Modified: 2025-10-12
- Source Path: rules/linux/auditd/execve/lnx_auditd_modify_system_firewall.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Detection

```yaml
selection1:
  type: EXECVE
  a0: iptables
  a1|contains: DROP
selection2:
  type: EXECVE
  a0: firewall-cmd
  a1|contains: remove
selection3:
  type: EXECVE
  a0: ufw
  a1|contains: delete
selection4:
  type: EXECVE
  a0: nft
  a1|contains:
  - delete
  - flush
condition: 1 of selection*
```

## False Positives

- Legitimate admin activity

## References

- https://www.trendmicro.com/en_us/research/22/c/cyclops-blink-sets-sights-on-asus-routers--.html
- https://blog.aquasec.com/container-security-tnt-container-attack
- https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/configuring_and_managing_networking/getting-started-with-nftables_configuring-and-managing-networking

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_modify_system_firewall.yml)
