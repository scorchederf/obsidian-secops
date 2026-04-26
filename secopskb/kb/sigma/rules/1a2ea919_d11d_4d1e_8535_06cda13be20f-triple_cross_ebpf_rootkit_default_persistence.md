---
sigma_id: "1a2ea919-d11d-4d1e-8535-06cda13be20f"
title: "Triple Cross eBPF Rootkit Default Persistence"
framework: "sigma"
generated: "true"
source_path: "rules/linux/file_event/file_event_lnx_triple_cross_rootkit_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/file_event/file_event_lnx_triple_cross_rootkit_persistence.yml"
build_date: "2026-04-26 15:01:53"
status: "test"
level: "high"
logsource: "linux / file_event"
aliases:
  - "1a2ea919-d11d-4d1e-8535-06cda13be20f"
  - "Triple Cross eBPF Rootkit Default Persistence"
attack_technique_ids:
  - "T1053.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Triple Cross eBPF Rootkit Default Persistence

Detects the creation of "ebpfbackdoor" files in both "cron.d" and "sudoers.d" directories. Which both are related to the TripleCross persistence method

## Metadata

- Rule ID: 1a2ea919-d11d-4d1e-8535-06cda13be20f
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-05
- Modified: 2022-12-31
- Source Path: rules/linux/file_event/file_event_lnx_triple_cross_rootkit_persistence.yml

## Logsource

- category: file_event
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.003]]

## Detection

```yaml
selection:
  TargetFilename|endswith: ebpfbackdoor
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/h3xduck/TripleCross/blob/12629558b8b0a27a5488a0b98f1ea7042e76f8ab/apps/deployer.sh

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/file_event/file_event_lnx_triple_cross_rootkit_persistence.yml)
