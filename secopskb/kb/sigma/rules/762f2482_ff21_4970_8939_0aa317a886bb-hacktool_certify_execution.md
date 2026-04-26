---
sigma_id: "762f2482-ff21-4970-8939-0aa317a886bb"
title: "HackTool - Certify Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_certify.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_certify.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "762f2482-ff21-4970-8939-0aa317a886bb"
  - "HackTool - Certify Execution"
attack_technique_ids:
  - "T1649"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - Certify Execution

Detects Certify a tool for Active Directory certificate abuse based on PE metadata characteristics and common command line arguments.

## Metadata

- Rule ID: 762f2482-ff21-4970-8939-0aa317a886bb
- Status: test
- Level: high
- Author: pH-T (Nextron Systems)
- Date: 2023-04-17
- Modified: 2023-04-25
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_certify.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1649-steal_or_forge_authentication_certificates|T1649]]

## Detection

```yaml
selection_img:
- Image|endswith: \Certify.exe
- OriginalFileName: Certify.exe
- Description|contains: Certify
selection_cli_commands:
  CommandLine|contains:
  - '.exe cas '
  - '.exe find '
  - '.exe pkiobjects '
  - '.exe request '
  - '.exe download '
selection_cli_options:
  CommandLine|contains:
  - ' /vulnerable'
  - ' /template:'
  - ' /altname:'
  - ' /domain:'
  - ' /path:'
  - ' /ca:'
condition: selection_img or all of selection_cli_*
```

## False Positives

- Unknown

## References

- https://github.com/GhostPack/Certify

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_certify.yml)
