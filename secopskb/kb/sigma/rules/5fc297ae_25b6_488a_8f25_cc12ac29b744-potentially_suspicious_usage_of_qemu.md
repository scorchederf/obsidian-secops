---
sigma_id: "5fc297ae-25b6-488a-8f25-cc12ac29b744"
title: "Potentially Suspicious Usage Of Qemu"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_qemu_suspicious_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_qemu_suspicious_execution.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "5fc297ae-25b6-488a-8f25-cc12ac29b744"
  - "Potentially Suspicious Usage Of Qemu"
attack_technique_ids:
  - "T1090"
  - "T1572"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Usage Of Qemu

Detects potentially suspicious execution of the Qemu utility in a Windows environment.
Threat actors have leveraged this utility and this technique for achieving network access as reported by Kaspersky.

## Metadata

- Rule ID: 5fc297ae-25b6-488a-8f25-cc12ac29b744
- Status: test
- Level: medium
- Author: Muhammad Faisal (@faisalusuf), Hunter Juhan (@threatHNTR)
- Date: 2024-06-03
- Source Path: rules/windows/process_creation/proc_creation_win_qemu_suspicious_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090]]
- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - -m 1M
  - -m 2M
  - -m 3M
  CommandLine|contains|all:
  - restrict=off
  - '-netdev '
  - connect=
  - -nographic
filter_main_normal_usecase:
  CommandLine|contains:
  - ' -cdrom '
  - ' type=virt '
  - ' -blockdev '
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://securelist.com/network-tunneling-with-qemu/111803/
- https://www.qemu.org/docs/master/system/invocation.html#hxtool-5

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_qemu_suspicious_execution.yml)
