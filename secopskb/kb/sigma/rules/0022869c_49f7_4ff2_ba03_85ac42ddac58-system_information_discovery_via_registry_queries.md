---
sigma_id: "0022869c-49f7-4ff2-ba03-85ac42ddac58"
title: "System Information Discovery via Registry Queries"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_discovery_via_reg_queries.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_discovery_via_reg_queries.yml"
build_date: "2026-04-26 14:14:37"
status: "experimental"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "0022869c-49f7-4ff2-ba03-85ac42ddac58"
  - "System Information Discovery via Registry Queries"
attack_technique_ids:
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Information Discovery via Registry Queries

Detects attempts to query system information directly from the Windows Registry.

## Metadata

- Rule ID: 0022869c-49f7-4ff2-ba03-85ac42ddac58
- Status: experimental
- Level: low
- Author: lazarg
- Date: 2025-06-12
- Modified: 2025-10-25
- Source Path: rules/windows/process_creation/proc_creation_win_discovery_via_reg_queries.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Detection

```yaml
selection_cmd_reg:
  Image|endswith: \reg.exe
  CommandLine|contains: query
  CommandLine|contains|windash: -v
selection_cmd_powershell:
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  CommandLine|contains:
  - Get-ItemPropertyValue
  - gpv
selection_keys:
  CommandLine|contains:
  - \SOFTWARE\Microsoft\Windows Defender
  - \SOFTWARE\Microsoft\Windows NT\CurrentVersion
  - \SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall
  - \SYSTEM\CurrentControlSet\Control\TimeZoneInformation
  - \SYSTEM\CurrentControlSet\Services
condition: 1 of selection_cmd_* and selection_keys
```

## False Positives

- Unlikely

## Simulation

### System Information Discovery

- atomic_guid: 66703791-c902-4560-8770-42b8a91f7667
- name: System Information Discovery
- technique: T1010
- type: atomic-red-team

### Discover OS Product Name via Registry

- atomic_guid: be3b5fe3-a575-4fb8-83f6-ad4a68dd5ce7
- name: Discover OS Product Name via Registry
- technique: T1082
- type: atomic-red-team

### Discover OS Build Number via Registry

- atomic_guid: acfcd709-0013-4f1e-b9ee-bc1e7bafaaec
- name: Discover OS Build Number via Registry
- technique: T1082
- type: atomic-red-team

## References

- https://cert.gov.ua/article/6277849
- https://github.com/redcanaryco/atomic-red-team/blob/75fa21076dcefa348a7521403cdd6bfc4e88623c/atomics/T1082/T1082.md
- https://github.com/redcanaryco/atomic-red-team/blob/75fa21076dcefa348a7521403cdd6bfc4e88623c/atomics/T1124/T1124.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_discovery_via_reg_queries.yml)
