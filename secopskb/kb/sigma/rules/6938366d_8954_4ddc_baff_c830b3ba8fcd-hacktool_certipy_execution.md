---
sigma_id: "6938366d-8954-4ddc-baff-c830b3ba8fcd"
title: "HackTool - Certipy Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_certipy.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_certipy.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "6938366d-8954-4ddc-baff-c830b3ba8fcd"
  - "HackTool - Certipy Execution"
attack_technique_ids:
  - "T1649"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - Certipy Execution

Detects Certipy execution, a tool for Active Directory Certificate Services enumeration and abuse based on PE metadata characteristics and common command line arguments.

## Metadata

- Rule ID: 6938366d-8954-4ddc-baff-c830b3ba8fcd
- Status: test
- Level: high
- Author: pH-T (Nextron Systems), Sittikorn Sangrattanapitak
- Date: 2023-04-17
- Modified: 2024-10-08
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_certipy.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1649-steal_or_forge_authentication_certificates|T1649]]

## Detection

```yaml
selection_img:
- Image|endswith: \Certipy.exe
- OriginalFileName: Certipy.exe
- Description|contains: Certipy
selection_cli_commands:
  CommandLine|contains:
  - ' account '
  - ' auth '
  - ' cert '
  - ' find '
  - ' forge '
  - ' ptt '
  - ' relay '
  - ' req '
  - ' shadow '
  - ' template '
selection_cli_flags:
  CommandLine|contains:
  - ' -bloodhound'
  - ' -ca-pfx '
  - ' -dc-ip '
  - ' -kirbi'
  - ' -old-bloodhound'
  - ' -pfx '
  - ' -target'
  - ' -template'
  - ' -username '
  - ' -vulnerable'
  - auth -pfx
  - shadow auto
  - shadow list
condition: selection_img or all of selection_cli_*
```

## False Positives

- Unlikely

## References

- https://github.com/ly4k/Certipy
- https://research.ifcr.dk/certipy-4-0-esc9-esc10-bloodhound-gui-new-authentication-and-request-methods-and-more-7237d88061f7

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_certipy.yml)
