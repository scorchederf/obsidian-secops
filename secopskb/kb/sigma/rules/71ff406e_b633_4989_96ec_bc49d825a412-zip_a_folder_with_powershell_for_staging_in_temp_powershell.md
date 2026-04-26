---
sigma_id: "71ff406e-b633-4989-96ec-bc49d825a412"
title: "Zip A Folder With PowerShell For Staging In Temp - PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_classic/posh_pc_susp_zip_compress.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_susp_zip_compress.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / powershell-classic"
aliases:
  - "71ff406e-b633-4989-96ec-bc49d825a412"
  - "Zip A Folder With PowerShell For Staging In Temp - PowerShell"
attack_technique_ids:
  - "T1074.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Zip A Folder With PowerShell For Staging In Temp - PowerShell

Detects PowerShell scripts that make use of the "Compress-Archive" Cmdlet in order to compress folders and files where the output is stored in a potentially suspicious location that is used often by malware for exfiltration.
An adversary might compress data (e.g., sensitive documents) that is collected prior to exfiltration in order to make it portable and minimize the amount of data sent over the network.

## Metadata

- Rule ID: 71ff406e-b633-4989-96ec-bc49d825a412
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), frack113
- Date: 2021-07-20
- Modified: 2023-12-18
- Source Path: rules/windows/powershell/powershell_classic/posh_pc_susp_zip_compress.yml

## Logsource

- product: windows
- service: powershell-classic

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1074-data_staged|T1074.001]]

## Detection

```yaml
selection:
  Data|contains:
  - Compress-Archive -Path*-DestinationPath $env:TEMP
  - Compress-Archive -Path*-DestinationPath*\AppData\Local\Temp\
  - Compress-Archive -Path*-DestinationPath*:\Windows\Temp\
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1074.001/T1074.001.md
- https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-347a

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_susp_zip_compress.yml)
