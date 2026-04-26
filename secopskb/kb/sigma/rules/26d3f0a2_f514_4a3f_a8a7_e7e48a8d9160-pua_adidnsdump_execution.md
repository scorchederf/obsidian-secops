---
sigma_id: "26d3f0a2-f514-4a3f-a8a7-e7e48a8d9160"
title: "PUA - Adidnsdump Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_python_adidnsdump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_python_adidnsdump.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "26d3f0a2-f514-4a3f-a8a7-e7e48a8d9160"
  - "PUA - Adidnsdump Execution"
attack_technique_ids:
  - "T1018"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - Adidnsdump Execution

This tool enables enumeration and exporting of all DNS records in the zone for recon purposes of internal networks Python 3 and python.exe must be installed,
Usee to Query/modify DNS records for Active Directory integrated DNS via LDAP

## Metadata

- Rule ID: 26d3f0a2-f514-4a3f-a8a7-e7e48a8d9160
- Status: test
- Level: low
- Author: frack113
- Date: 2022-01-01
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_python_adidnsdump.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]

## Detection

```yaml
selection:
  Image|endswith: \python.exe
  CommandLine|contains: adidnsdump
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1018/T1018.md#atomic-test-9---remote-system-discovery---adidnsdump

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_python_adidnsdump.yml)
