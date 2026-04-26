---
sigma_id: "043c4b8b-3a54-4780-9682-081cb6b8185c"
title: "Suspicious IIS Module Registration"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_iis_susp_module_registration.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_iis_susp_module_registration.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "043c4b8b-3a54-4780-9682-081cb6b8185c"
  - "Suspicious IIS Module Registration"
attack_technique_ids:
  - "T1505.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious IIS Module Registration

Detects a suspicious IIS module registration as described in Microsoft threat report on IIS backdoors

## Metadata

- Rule ID: 043c4b8b-3a54-4780-9682-081cb6b8185c
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Microsoft (idea)
- Date: 2022-08-04
- Modified: 2023-01-23
- Source Path: rules/windows/process_creation/proc_creation_win_iis_susp_module_registration.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.004]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \w3wp.exe
selection_cli_1:
  CommandLine|contains: appcmd.exe add module
selection_cli_2:
  CommandLine|contains: ' system.enterpriseservices.internal.publish'
  Image|endswith: \powershell.exe
selection_cli_3:
  CommandLine|contains|all:
  - gacutil
  - ' /I'
condition: selection_parent and 1 of selection_cli_*
```

## False Positives

- Administrative activity

## References

- https://www.microsoft.com/security/blog/2022/07/26/malicious-iis-extensions-quietly-open-persistent-backdoors-into-servers/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_iis_susp_module_registration.yml)
