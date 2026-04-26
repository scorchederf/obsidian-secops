---
sigma_id: "3be619f4-d9ec-4ea8-a173-18fdd01996ab"
title: "Flush Iptables Ufw Chain"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_iptables_flush_ufw.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_iptables_flush_ufw.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "3be619f4-d9ec-4ea8-a173-18fdd01996ab"
  - "Flush Iptables Ufw Chain"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Flush Iptables Ufw Chain

Detect use of iptables to flush all firewall rules, tables and chains and allow all network traffic

## Metadata

- Rule ID: 3be619f4-d9ec-4ea8-a173-18fdd01996ab
- Status: test
- Level: medium
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2023-01-18
- Source Path: rules/linux/process_creation/proc_creation_lnx_iptables_flush_ufw.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Detection

```yaml
selection_img:
  Image|endswith:
  - /iptables
  - /xtables-legacy-multi
  - /iptables-legacy-multi
  - /ip6tables
  - /ip6tables-legacy-multi
selection_params:
  CommandLine|contains:
  - -F
  - -Z
  - -X
selection_ufw:
  CommandLine|contains:
  - ufw-logging-deny
  - ufw-logging-allow
  - ufw6-logging-deny
  - ufw6-logging-allow
condition: all of selection_*
```

## False Positives

- Network administrators

## References

- https://blogs.blackberry.com/
- https://www.cyberciti.biz/tips/linux-iptables-how-to-flush-all-rules.html
- https://twitter.com/Joseliyo_Jstnk/status/1620131033474822144

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_iptables_flush_ufw.yml)
