---
sigma_id: "e96253b8-6b3b-4f90-9e59-3b24b99cf9b4"
title: "HackTool - KrbRelay Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_krbrelay.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_krbrelay.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e96253b8-6b3b-4f90-9e59-3b24b99cf9b4"
  - "HackTool - KrbRelay Execution"
attack_technique_ids:
  - "T1558.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - KrbRelay Execution

Detects the use of KrbRelay, a Kerberos relaying tool

## Metadata

- Rule ID: e96253b8-6b3b-4f90-9e59-3b24b99cf9b4
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-04-27
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_krbrelay.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.003]]

## Detection

```yaml
selection_img:
- Image|endswith: \KrbRelay.exe
- OriginalFileName: KrbRelay.exe
selection_cli_1:
  CommandLine|contains|all:
  - ' -spn '
  - ' -clsid '
  - ' -rbcd '
selection_cli_2:
  CommandLine|contains|all:
  - shadowcred
  - clsid
  - spn
selection_cli_3:
  CommandLine|contains|all:
  - 'spn '
  - 'session '
  - 'clsid '
condition: 1 of selection_*
```

## False Positives

- Unlikely

## References

- https://github.com/cube0x0/KrbRelay

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_krbrelay.yml)
