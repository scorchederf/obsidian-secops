---
sigma_id: "c7746f1c-47d3-43d6-8c45-cd1e54b6b0a2"
title: "Kernel Memory Dump Via LiveKD"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_livekd_kernel_memory_dump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_livekd_kernel_memory_dump.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c7746f1c-47d3-43d6-8c45-cd1e54b6b0a2"
  - "Kernel Memory Dump Via LiveKD"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Kernel Memory Dump Via LiveKD

Detects execution of LiveKD with the "-m" flag to potentially dump the kernel memory

## Metadata

- Rule ID: c7746f1c-47d3-43d6-8c45-cd1e54b6b0a2
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-16
- Modified: 2024-03-13
- Source Path: rules/windows/process_creation/proc_creation_win_sysinternals_livekd_kernel_memory_dump.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith:
  - \livekd.exe
  - \livekd64.exe
- OriginalFileName: livekd.exe
selection_cli:
  CommandLine|contains|windash: ' -m'
condition: all of selection_*
```

## False Positives

- Unlikely in production environment

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/livekd
- https://4sysops.com/archives/creating-a-complete-memory-dump-without-a-blue-screen/
- https://kb.acronis.com/content/60892

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_livekd_kernel_memory_dump.yml)
