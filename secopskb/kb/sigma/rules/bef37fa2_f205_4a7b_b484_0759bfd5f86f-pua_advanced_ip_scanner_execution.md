---
sigma_id: "bef37fa2-f205-4a7b-b484-0759bfd5f86f"
title: "PUA - Advanced IP Scanner Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_advanced_ip_scanner.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_advanced_ip_scanner.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "bef37fa2-f205-4a7b-b484-0759bfd5f86f"
  - "PUA - Advanced IP Scanner Execution"
attack_technique_ids:
  - "T1046"
  - "T1135"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - Advanced IP Scanner Execution

Detects the use of Advanced IP Scanner. Seems to be a popular tool for ransomware groups.

## Metadata

- Rule ID: bef37fa2-f205-4a7b-b484-0759bfd5f86f
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), @ROxPinTeddy
- Date: 2020-05-12
- Modified: 2023-02-07
- Source Path: rules/windows/process_creation/proc_creation_win_pua_advanced_ip_scanner.yml

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
- Image|contains: \advanced_ip_scanner
- OriginalFileName|contains: advanced_ip_scanner
- Description|contains: Advanced IP Scanner
selection_cli:
  CommandLine|contains|all:
  - /portable
  - /lng
condition: 1 of selection_*
```

## False Positives

- Legitimate administrative use

## References

- https://news.sophos.com/en-us/2019/12/09/snatch-ransomware-reboots-pcs-into-safe-mode-to-bypass-protection/
- https://www.fireeye.com/blog/threat-research/2020/05/tactics-techniques-procedures-associated-with-maze-ransomware-incidents.html
- https://labs.f-secure.com/blog/prelude-to-ransomware-systembc
- https://assets.documentcloud.org/documents/20444693/fbi-pin-egregor-ransomware-bc-01062021.pdf
- https://thedfirreport.com/2021/01/18/all-that-for-a-coinminer
- https://github.com/3CORESec/MAL-CL/tree/master/Descriptors/Other/Advanced%20IP%20Scanner

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_advanced_ip_scanner.yml)
