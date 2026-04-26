---
sigma_id: "54773c5f-f1cc-4703-9126-2f797d96a69d"
title: "PUA - Advanced Port Scanner Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_advanced_port_scanner.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_advanced_port_scanner.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "54773c5f-f1cc-4703-9126-2f797d96a69d"
  - "PUA - Advanced Port Scanner Execution"
attack_technique_ids:
  - "T1046"
  - "T1135"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - Advanced Port Scanner Execution

Detects the use of Advanced Port Scanner.

## Metadata

- Rule ID: 54773c5f-f1cc-4703-9126-2f797d96a69d
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-12-18
- Modified: 2023-02-07
- Source Path: rules/windows/process_creation/proc_creation_win_pua_advanced_port_scanner.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1046-network_service_discovery|T1046]]
- [[kb/attack/techniques/T1135-network_share_discovery|T1135]]

## Detection

```yaml
selection_img:
- Image|contains: \advanced_port_scanner
- OriginalFileName|contains: advanced_port_scanner
- Description|contains: Advanced Port Scanner
selection_cli:
  CommandLine|contains|all:
  - /portable
  - /lng
condition: 1 of selection_*
```

## False Positives

- Legitimate administrative use
- Tools with similar commandline (very rare)

## References

- https://github.com/3CORESec/MAL-CL/tree/master/Descriptors/Other/Advanced%20Port%20Scanner

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_advanced_port_scanner.yml)
