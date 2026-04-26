---
sigma_id: "ca621ba5-54ab-4035-9942-d378e6fcde3c"
title: "HackTool - HandleKatz LSASS Dumper Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_handlekatz.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_handlekatz.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ca621ba5-54ab-4035-9942-d378e6fcde3c"
  - "HackTool - HandleKatz LSASS Dumper Execution"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - HandleKatz LSASS Dumper Execution

Detects the use of HandleKatz, a tool that demonstrates the usage of cloned handles to Lsass in order to create an obfuscated memory dump of the same

## Metadata

- Rule ID: ca621ba5-54ab-4035-9942-d378e6fcde3c
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-08-18
- Modified: 2024-11-23
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_handlekatz.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection_loader_img:
  Image|endswith: \loader.exe
  CommandLine|contains: '--pid:'
selection_loader_imphash:
  Hashes|contains:
  - IMPHASH=38D9E015591BBFD4929E0D0F47FA0055
  - IMPHASH=0E2216679CA6E1094D63322E3412D650
selection_flags:
  CommandLine|contains|all:
  - '--pid:'
  - '--outfile:'
  CommandLine|contains:
  - .dmp
  - lsass
  - .obf
  - dump
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/codewhitesec/HandleKatz

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_handlekatz.yml)
