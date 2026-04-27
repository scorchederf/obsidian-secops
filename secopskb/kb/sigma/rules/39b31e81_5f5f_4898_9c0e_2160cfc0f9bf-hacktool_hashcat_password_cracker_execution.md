---
sigma_id: "39b31e81-5f5f-4898-9c0e-2160cfc0f9bf"
title: "HackTool - Hashcat Password Cracker Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_hashcat.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_hashcat.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "39b31e81-5f5f-4898-9c0e-2160cfc0f9bf"
  - "HackTool - Hashcat Password Cracker Execution"
attack_technique_ids:
  - "T1110.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# HackTool - Hashcat Password Cracker Execution

Execute Hashcat.exe with provided SAM file from registry of Windows and Password list to crack against

## Metadata

- Rule ID: 39b31e81-5f5f-4898-9c0e-2160cfc0f9bf
- Status: test
- Level: high
- Author: frack113
- Date: 2021-12-27
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_hashcat.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1110-brute_force|T1110.002]]

## Detection

```yaml
selection_img:
  Image|endswith: \hashcat.exe
selection_cli:
  CommandLine|contains|all:
  - '-a '
  - '-m 1000 '
  - '-r '
condition: 1 of selection_*
```

## False Positives

- Tools that use similar command line flags and values

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1110.002/T1110.002.md#atomic-test-1---password-cracking-with-hashcat
- https://hashcat.net/wiki/doku.php?id=hashcat

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_hashcat.yml)
