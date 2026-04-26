---
sigma_id: "904e8e61-8edf-4350-b59c-b905fc8e810c"
title: "Security Software Discovery Via Powershell Script"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_get_process_security_software_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_get_process_security_software_discovery.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "904e8e61-8edf-4350-b59c-b905fc8e810c"
  - "Security Software Discovery Via Powershell Script"
attack_technique_ids:
  - "T1518.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Security Software Discovery Via Powershell Script

Detects calls to "get-process" where the output is piped to a "where-object" filter to search for security solution processes.
Adversaries may attempt to get a listing of security software, configurations, defensive tools, and sensors that are installed on a system or in a cloud environment. This may include things such as firewall rules and anti-virus

## Metadata

- Rule ID: 904e8e61-8edf-4350-b59c-b905fc8e810c
- Status: test
- Level: medium
- Author: frack113, Anish Bogati, Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-12-16
- Modified: 2023-10-24
- Source Path: rules/windows/powershell/powershell_script/posh_ps_get_process_security_software_discovery.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1518-software_discovery|T1518.001]]

## Detection

```yaml
selection_cmdlet:
  ScriptBlockText|contains:
  - get-process | \?
  - get-process | where
  - gps | \?
  - gps | where
selection_field:
  ScriptBlockText|contains:
  - Company -like
  - Description -like
  - Name -like
  - Path -like
  - Product -like
selection_keywords:
  ScriptBlockText|contains:
  - \*avira\*
  - \*carbonblack\*
  - \*cylance\*
  - \*defender\*
  - \*kaspersky\*
  - \*malware\*
  - \*sentinel\*
  - \*symantec\*
  - \*virus\*
condition: all of selection_*
```

## False Positives

- False positives might occur due to the nature of the ScriptBlock being ingested as a big blob. Initial tuning is required.
- As the "selection_cmdlet" is common in scripts the matching engine might slow down the search. Change into regex or a more accurate string to avoid heavy resource consumption if experienced

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1518.001/T1518.001.md#atomic-test-2---security-software-discovery---powershell

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_get_process_security_software_discovery.yml)
