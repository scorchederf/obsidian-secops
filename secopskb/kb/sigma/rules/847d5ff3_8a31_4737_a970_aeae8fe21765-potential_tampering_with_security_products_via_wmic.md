---
sigma_id: "847d5ff3-8a31-4737-a970-aeae8fe21765"
title: "Potential Tampering With Security Products Via WMIC"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_uninstall_security_products.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_uninstall_security_products.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "847d5ff3-8a31-4737-a970-aeae8fe21765"
  - "Potential Tampering With Security Products Via WMIC"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential Tampering With Security Products Via WMIC

Detects uninstallation or termination of security products using the WMIC utility

## Metadata

- Rule ID: 847d5ff3-8a31-4737-a970-aeae8fe21765
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-01-30
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_uninstall_security_products.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_cli_1:
  CommandLine|contains|all:
  - wmic
  - 'product where '
  - call
  - uninstall
  - /nointeractive
selection_cli_2:
  CommandLine|contains|all:
  - wmic
  - 'caption like '
  CommandLine|contains:
  - call delete
  - call terminate
selection_cli_3:
  CommandLine|contains|all:
  - 'process '
  - 'where '
  - delete
selection_product:
  CommandLine|contains:
  - '%carbon%'
  - '%cylance%'
  - '%endpoint%'
  - '%eset%'
  - '%malware%'
  - '%Sophos%'
  - '%symantec%'
  - Antivirus
  - 'AVG '
  - Carbon Black
  - CarbonBlack
  - Cb Defense Sensor 64-bit
  - Crowdstrike Sensor
  - 'Cylance '
  - Dell Threat Defense
  - DLP Endpoint
  - Endpoint Detection
  - Endpoint Protection
  - Endpoint Security
  - Endpoint Sensor
  - ESET File Security
  - LogRhythm System Monitor Service
  - Malwarebytes
  - McAfee Agent
  - Microsoft Security Client
  - Sophos Anti-Virus
  - Sophos AutoUpdate
  - Sophos Credential Store
  - Sophos Management Console
  - Sophos Management Database
  - Sophos Management Server
  - Sophos Remote Management System
  - Sophos Update Manager
  - Threat Protection
  - VirusScan
  - Webroot SecureAnywhere
  - Windows Defender
condition: 1 of selection_cli_* and selection_product
```

## False Positives

- Legitimate administration

## References

- https://twitter.com/cglyer/status/1355171195654709249
- https://thedfirreport.com/2021/10/18/icedid-to-xinglocker-ransomware-in-24-hours/
- https://www.mandiant.com/resources/unc2165-shifts-to-evade-sanctions
- https://research.nccgroup.com/2022/08/19/back-in-black-unlocking-a-lockbit-3-0-ransomware-attack/
- https://www.trendmicro.com/en_us/research/23/a/vice-society-ransomware-group-targets-manufacturing-companies.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_uninstall_security_products.yml)
