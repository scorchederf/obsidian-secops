---
sigma_id: "85a8e5ba-bd03-4bfb-bbfa-a4409a8f8b98"
title: "Folder Compress To Potentially Suspicious Output Via Compress-Archive Cmdlet"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_zip_compress.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_zip_compress.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "85a8e5ba-bd03-4bfb-bbfa-a4409a8f8b98"
  - "Folder Compress To Potentially Suspicious Output Via Compress-Archive Cmdlet"
attack_technique_ids:
  - "T1074.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Folder Compress To Potentially Suspicious Output Via Compress-Archive Cmdlet

Detects PowerShell scripts that make use of the "Compress-Archive" Cmdlet in order to compress folders and files where the output is stored in a potentially suspicious location that is used often by malware for exfiltration.
An adversary might compress data (e.g., sensitive documents) that is collected prior to exfiltration in order to make it portable and minimize the amount of data sent over the network.

## Metadata

- Rule ID: 85a8e5ba-bd03-4bfb-bbfa-a4409a8f8b98
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), frack113
- Date: 2021-07-20
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_zip_compress.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1074-data_staged|T1074.001]]

## Detection

```yaml
selection:
  CommandLine|contains:
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_zip_compress.yml)
