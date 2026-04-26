---
sigma_id: "f6ecd1cf-19b8-4488-97f6-00f0924991a3"
title: "PUA - Nmap/Zenmap Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_nmap_zenmap.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_nmap_zenmap.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "f6ecd1cf-19b8-4488-97f6-00f0924991a3"
  - "PUA - Nmap/Zenmap Execution"
attack_technique_ids:
  - "T1046"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - Nmap/Zenmap Execution

Detects usage of namp/zenmap. Adversaries may attempt to get a listing of services running on remote hosts, including those that may be vulnerable to remote software exploitation

## Metadata

- Rule ID: f6ecd1cf-19b8-4488-97f6-00f0924991a3
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-12-10
- Modified: 2023-12-11
- Source Path: rules/windows/process_creation/proc_creation_win_pua_nmap_zenmap.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1046-network_service_discovery|T1046]]

## Detection

```yaml
selection:
- Image|endswith:
  - \nmap.exe
  - \zennmap.exe
- OriginalFileName:
  - nmap.exe
  - zennmap.exe
condition: selection
```

## False Positives

- Legitimate administrator activity

## References

- https://nmap.org/
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1046/T1046.md#atomic-test-3---port-scan-nmap-for-windows

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_nmap_zenmap.yml)
