---
sigma_id: "e6313acd-208c-44fc-a0ff-db85d572e90e"
title: "Network Reconnaissance Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_nslookup_domain_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_nslookup_domain_discovery.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e6313acd-208c-44fc-a0ff-db85d572e90e"
  - "Network Reconnaissance Activity"
attack_technique_ids:
  - "T1087"
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a set of suspicious network related commands often used in recon stages

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087: Account Discovery]]
- [[kb/attack/techniques/T1082-system_information_discovery|T1082: System Information Discovery]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - nslookup
  - _ldap._tcp.dc._msdcs.
condition: selection
```

## False Positives

- False positives depend on scripts and administrative tools used in the monitored environment

## References

- https://thedfirreport.com/2022/02/07/qbot-likes-to-move-it-move-it/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_nslookup_domain_discovery.yml)
