---
sigma_id: "2e65275c-8288-4ab4-aeb7-6274f58b6b20"
title: "Procdump Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_procdump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_procdump.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "2e65275c-8288-4ab4-aeb7-6274f58b6b20"
  - "Procdump Execution"
attack_technique_ids:
  - "T1036"
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Procdump Execution

Detects usage of the SysInternals Procdump utility

## Metadata

- Rule ID: 2e65275c-8288-4ab4-aeb7-6274f58b6b20
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2021-08-16
- Modified: 2023-02-28
- Source Path: rules/windows/process_creation/proc_creation_win_sysinternals_procdump.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
  Image|endswith:
  - \procdump.exe
  - \procdump64.exe
condition: selection
```

## False Positives

- Legitimate use of procdump by a developer or administrator

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/procdump

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_procdump.yml)
