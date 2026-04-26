---
sigma_id: "f8be3e82-46a3-4e4e-ada5-8e538ae8b9c9"
title: "Credential Dumping Activity By Python Based Tool"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_lsass_python_based_tool.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_lsass_python_based_tool.yml"
build_date: "2026-04-26 15:01:44"
status: "stable"
level: "high"
logsource: "windows / process_access"
aliases:
  - "f8be3e82-46a3-4e4e-ada5-8e538ae8b9c9"
  - "Credential Dumping Activity By Python Based Tool"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Credential Dumping Activity By Python Based Tool

Detects LSASS process access for potential credential dumping by a Python-like tool such as LaZagne or Pypykatz.

## Metadata

- Rule ID: f8be3e82-46a3-4e4e-ada5-8e538ae8b9c9
- Status: stable
- Level: high
- Author: Bhabesh Raj, Jonhnathan Ribeiro
- Date: 2023-11-27
- Modified: 2023-11-29
- Source Path: rules/windows/process_access/proc_access_win_lsass_python_based_tool.yml

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

### Software Tags

- S0349

## Detection

```yaml
selection:
  TargetImage|endswith: \lsass.exe
  CallTrace|contains|all:
  - _ctypes.pyd+
  - :\Windows\System32\KERNELBASE.dll+
  - :\Windows\SYSTEM32\ntdll.dll+
  CallTrace|contains:
  - python27.dll+
  - python3*.dll+
  GrantedAccess: '0x1FFFFF'
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/bh4b3sh/status/1303674603819081728
- https://github.com/skelsec/pypykatz

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_lsass_python_based_tool.yml)
