---
sigma_id: "7124aebe-4cd7-4ccb-8df0-6d6b93c96795"
title: "Suspicious Kernel Dump Using Dtrace"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dtrace_kernel_dump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dtrace_kernel_dump.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "7124aebe-4cd7-4ccb-8df0-6d6b93c96795"
  - "Suspicious Kernel Dump Using Dtrace"
attack_technique_ids:
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious way to dump the kernel on Windows systems using dtrace.exe, which is available on Windows systems since Windows 10 19H1

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1082-system_information_discovery|T1082: System Information Discovery]]

## Detection

```yaml
selection_plain:
  Image|endswith: \dtrace.exe
  CommandLine|contains: lkd(0)
selection_obfuscated:
  CommandLine|contains|all:
  - syscall:::return
  - lkd(
condition: 1 of selection*
```

## False Positives

- Unknown

## References

- https://twitter.com/0gtweet/status/1474899714290208777?s=12
- https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/dtrace

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dtrace_kernel_dump.yml)
