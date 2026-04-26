---
sigma_id: "22236d75-d5a0-4287-bf06-c93b1770860f"
title: "Triple Cross eBPF Rootkit Install Commands"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_triple_cross_rootkit_install.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_triple_cross_rootkit_install.yml"
build_date: "2026-04-26 15:01:53"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "22236d75-d5a0-4287-bf06-c93b1770860f"
  - "Triple Cross eBPF Rootkit Install Commands"
attack_technique_ids:
  - "T1014"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Triple Cross eBPF Rootkit Install Commands

Detects default install commands of the Triple Cross eBPF rootkit based on the "deployer.sh" script

## Metadata

- Rule ID: 22236d75-d5a0-4287-bf06-c93b1770860f
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-05
- Source Path: rules/linux/process_creation/proc_creation_lnx_triple_cross_rootkit_install.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1014-rootkit|T1014]]

## Detection

```yaml
selection:
  Image|endswith: /sudo
  CommandLine|contains|all:
  - ' tc '
  - ' enp0s3 '
  CommandLine|contains:
  - ' qdisc '
  - ' filter '
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/h3xduck/TripleCross/blob/1f1c3e0958af8ad9f6ebe10ab442e75de33e91de/apps/deployer.sh

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_triple_cross_rootkit_install.yml)
