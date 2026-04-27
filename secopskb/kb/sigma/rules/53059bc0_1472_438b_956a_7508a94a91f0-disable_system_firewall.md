---
sigma_id: "53059bc0-1472-438b-956a-7508a94a91f0"
title: "Disable System Firewall"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/service_stop/lnx_auditd_disable_system_firewall.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/service_stop/lnx_auditd_disable_system_firewall.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "linux / auditd"
aliases:
  - "53059bc0-1472-438b-956a-7508a94a91f0"
  - "Disable System Firewall"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Disable System Firewall

Detects disabling of system firewalls which could be used by adversaries to bypass controls that limit usage of the network.

## Metadata

- Rule ID: 53059bc0-1472-438b-956a-7508a94a91f0
- Status: test
- Level: high
- Author: Pawel Mazur
- Date: 2022-01-22
- Source Path: rules/linux/auditd/service_stop/lnx_auditd_disable_system_firewall.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Detection

```yaml
selection:
  type: SERVICE_STOP
  unit:
  - firewalld
  - iptables
  - ufw
condition: selection
```

## False Positives

- Admin activity

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.004/T1562.004.md
- https://firewalld.org/documentation/man-pages/firewall-cmd.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/service_stop/lnx_auditd_disable_system_firewall.yml)
