---
sigma_id: "ca387a8e-1c84-4da3-9993-028b45342d30"
title: "PUA - SoftPerfect Netscan Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_netscan.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_netscan.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ca387a8e-1c84-4da3-9993-028b45342d30"
  - "PUA - SoftPerfect Netscan Execution"
attack_technique_ids:
  - "T1046"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - SoftPerfect Netscan Execution

Detects usage of SoftPerfect's "netscan.exe". An application for scanning networks.
It is actively used in-the-wild by threat actors to inspect and understand the network architecture of a victim.

## Metadata

- Rule ID: ca387a8e-1c84-4da3-9993-028b45342d30
- Status: test
- Level: medium
- Author: @d4ns4n_ (Wuerth-Phoenix)
- Date: 2024-04-25
- Source Path: rules/windows/process_creation/proc_creation_win_pua_netscan.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1046-network_service_discovery|T1046]]

## Detection

```yaml
selection:
- Image|endswith: \netscan.exe
- Product: Network Scanner
- Description: Application for scanning networks
condition: selection
```

## False Positives

- Legitimate administrator activity

## References

- https://www.protect.airbus.com/blog/uncovering-cyber-intruders-netscan/
- https://secjoes-reports.s3.eu-central-1.amazonaws.com/Sockbot%2Bin%2BGoLand.pdf
- https://www.sentinelone.com/labs/black-basta-ransomware-attacks-deploy-custom-edr-evasion-tools-tied-to-fin7-threat-actor/
- https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/yanluowang-ransomware-attacks-continue
- https://research.nccgroup.com/2022/07/13/climbing-mount-everest-black-byte-bytes-back/
- https://www.bleepingcomputer.com/news/security/microsoft-exchange-servers-hacked-to-deploy-hive-ransomware/
- https://www.softperfect.com/products/networkscanner/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_netscan.yml)
