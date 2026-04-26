---
sigma_id: "c0239255-822c-4630-b7f1-35362bcb8f44"
title: "Triple Cross eBPF Rootkit Default LockFile"
framework: "sigma"
generated: "true"
source_path: "rules/linux/file_event/file_event_lnx_triple_cross_rootkit_lock_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/file_event/file_event_lnx_triple_cross_rootkit_lock_file.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "linux / file_event"
aliases:
  - "c0239255-822c-4630-b7f1-35362bcb8f44"
  - "Triple Cross eBPF Rootkit Default LockFile"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Triple Cross eBPF Rootkit Default LockFile

Detects the creation of the file "rootlog" which is used by the TripleCross rootkit as a way to check if the backdoor is already running.

## Metadata

- Rule ID: c0239255-822c-4630-b7f1-35362bcb8f44
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-05
- Modified: 2022-12-31
- Source Path: rules/linux/file_event/file_event_lnx_triple_cross_rootkit_lock_file.yml

## Logsource

- category: file_event
- product: linux

## Detection

```yaml
selection:
  TargetFilename: /tmp/rootlog
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/h3xduck/TripleCross/blob/1f1c3e0958af8ad9f6ebe10ab442e75de33e91de/src/helpers/execve_hijack.c#L33

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/file_event/file_event_lnx_triple_cross_rootkit_lock_file.yml)
