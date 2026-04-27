---
sigma_id: "0326c3c8-7803-4a0f-8c5c-368f747f7c3e"
title: "Triple Cross eBPF Rootkit Execve Hijack"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_triple_cross_rootkit_execve_hijack.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_triple_cross_rootkit_execve_hijack.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "0326c3c8-7803-4a0f-8c5c-368f747f7c3e"
  - "Triple Cross eBPF Rootkit Execve Hijack"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Triple Cross eBPF Rootkit Execve Hijack

Detects execution of a the file "execve_hijack" which is used by the Triple Cross rootkit as a way to elevate privileges

## Metadata

- Rule ID: 0326c3c8-7803-4a0f-8c5c-368f747f7c3e
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-05
- Source Path: rules/linux/process_creation/proc_creation_lnx_triple_cross_rootkit_execve_hijack.yml

## Logsource

- category: process_creation
- product: linux

## Detection

```yaml
selection:
  Image|endswith: /sudo
  CommandLine|contains: execve_hijack
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/h3xduck/TripleCross/blob/1f1c3e0958af8ad9f6ebe10ab442e75de33e91de/src/helpers/execve_hijack.c#L275

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_triple_cross_rootkit_execve_hijack.yml)
