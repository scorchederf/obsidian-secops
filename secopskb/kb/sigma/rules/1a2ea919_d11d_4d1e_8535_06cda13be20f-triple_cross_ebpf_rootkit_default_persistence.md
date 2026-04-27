---
sigma_id: "1a2ea919-d11d-4d1e-8535-06cda13be20f"
title: "Triple Cross eBPF Rootkit Default Persistence"
framework: "sigma"
generated: "true"
source_path: "rules/linux/file_event/file_event_lnx_triple_cross_rootkit_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/file_event/file_event_lnx_triple_cross_rootkit_persistence.yml"
build_date: "2026-04-27 19:13:57"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the creation of "ebpfbackdoor" files in both "cron.d" and "sudoers.d" directories. Which both are related to the TripleCross persistence method

## Logsource

- category: file_event
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job#^t1053003-cron|T1053.003: Cron]]

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
