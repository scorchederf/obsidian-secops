---
sigma_id: "0f9c21f1-6a73-4b0e-9809-cb562cb8d981"
title: "Potential Privilege Escalation via Service Permissions Weakness"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_registry_privilege_escalation_via_service_key.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_privilege_escalation_via_service_key.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "0f9c21f1-6a73-4b0e-9809-cb562cb8d981"
  - "Potential Privilege Escalation via Service Permissions Weakness"
attack_technique_ids:
  - "T1574.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Privilege Escalation via Service Permissions Weakness

Detect modification of services configuration (ImagePath, FailureCommand and ServiceDLL) in registry by processes with Medium integrity level

## Metadata

- Rule ID: 0f9c21f1-6a73-4b0e-9809-cb562cb8d981
- Status: test
- Level: high
- Author: Teymur Kheirkhabarov
- Date: 2019-10-26
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_registry_privilege_escalation_via_service_key.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.011]]

## Detection

```yaml
selection:
  IntegrityLevel:
  - Medium
  - S-1-16-8192
  CommandLine|contains|all:
  - ControlSet
  - services
  CommandLine|contains:
  - \ImagePath
  - \FailureCommand
  - \ServiceDll
condition: selection
```

## False Positives

- Unknown

## References

- https://speakerdeck.com/heirhabarov/hunting-for-privilege-escalation-in-windows-environment
- https://pentestlab.blog/2017/03/31/insecure-registry-permissions/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_privilege_escalation_via_service_key.yml)
