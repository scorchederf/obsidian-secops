---
sigma_id: "e0b0c2ab-3d52-46d9-8cb7-049dc775fbd1"
title: "Enumeration for Credentials in Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_enumeration_for_credentials_in_registry.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_enumeration_for_credentials_in_registry.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "e0b0c2ab-3d52-46d9-8cb7-049dc775fbd1"
  - "Enumeration for Credentials in Registry"
attack_technique_ids:
  - "T1552.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Enumeration for Credentials in Registry

Adversaries may search the Registry on compromised systems for insecurely stored credentials.
The Windows Registry stores configuration information that can be used by the system or other programs.
Adversaries may query the Registry looking for credentials and passwords that have been stored for use by other programs or services

## Metadata

- Rule ID: e0b0c2ab-3d52-46d9-8cb7-049dc775fbd1
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-12-20
- Modified: 2022-12-25
- Source Path: rules/windows/process_creation/proc_creation_win_reg_enumeration_for_credentials_in_registry.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.002]]

## Detection

```yaml
reg:
  Image|endswith: \reg.exe
  CommandLine|contains|all:
  - ' query '
  - '/t '
  - REG_SZ
  - /s
hive:
- CommandLine|contains|all:
  - '/f '
  - HKLM
- CommandLine|contains|all:
  - '/f '
  - HKCU
- CommandLine|contains: HKCU\Software\SimonTatham\PuTTY\Sessions
condition: reg and hive
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1552.002/T1552.002.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_enumeration_for_credentials_in_registry.yml)
