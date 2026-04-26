---
sigma_id: "2704ab9e-afe2-4854-a3b1-0c0706d03578"
title: "HackTool - Dumpert Process Dumper Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_dumpert.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_dumpert.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "2704ab9e-afe2-4854-a3b1-0c0706d03578"
  - "HackTool - Dumpert Process Dumper Execution"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - Dumpert Process Dumper Execution

Detects the use of Dumpert process dumper, which dumps the lsass.exe process memory

## Metadata

- Rule ID: 2704ab9e-afe2-4854-a3b1-0c0706d03578
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems)
- Date: 2020-02-04
- Modified: 2025-01-22
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_dumpert.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
- Hashes|contains: MD5=09D278F9DE118EF09163C6140255C690
- CommandLine|contains: Dumpert.dll
condition: selection
```

## False Positives

- Very unlikely

## References

- https://github.com/outflanknl/Dumpert
- https://unit42.paloaltonetworks.com/actors-still-exploiting-sharepoint-vulnerability/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_dumpert.yml)
