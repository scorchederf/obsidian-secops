---
sigma_id: "4fd6b1c7-19b8-4488-97f6-00f0924991a3"
title: "PUA - NimScan Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_nimscan.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_nimscan.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "4fd6b1c7-19b8-4488-97f6-00f0924991a3"
  - "PUA - NimScan Execution"
attack_technique_ids:
  - "T1046"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - NimScan Execution

Detects usage of NimScan, a portscanner utility.
In early 2025, adversaries were observed using this utility to scan for open ports on remote hosts in a compromised environment.
This rule identifies the execution of NimScan based on the process image name and specific hash values associated with different versions of the tool.

## Metadata

- Rule ID: 4fd6b1c7-19b8-4488-97f6-00f0924991a3
- Status: test
- Level: medium
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-02-05
- Source Path: rules/windows/process_creation/proc_creation_win_pua_nimscan.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1046-network_service_discovery|T1046]]

## Detection

```yaml
selection:
- Image|endswith: \NimScan.exe
- Hashes|contains:
  - IMPHASH=41BB1C7571B3A724EB83A1D2B96DBB8C
  - IMPHASH=B1B6ADACB172795480179EFD18A29549
  - IMPHASH=0D1F896DC7642AD8384F9042F30279C2
condition: selection
```

## False Positives

- Legitimate administrator activity

## References

- https://x.com/cyberfeeddigest/status/1887041526397587859
- https://github.com/elddy/NimScan

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_nimscan.yml)
