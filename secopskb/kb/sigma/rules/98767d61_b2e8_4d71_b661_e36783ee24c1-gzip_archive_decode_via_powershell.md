---
sigma_id: "98767d61-b2e8-4d71-b661-e36783ee24c1"
title: "Gzip Archive Decode Via PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_decode_gzip.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_decode_gzip.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "98767d61-b2e8-4d71-b661-e36783ee24c1"
  - "Gzip Archive Decode Via PowerShell"
attack_technique_ids:
  - "T1132.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Gzip Archive Decode Via PowerShell

Detects attempts of decoding encoded Gzip archives via PowerShell.

## Metadata

- Rule ID: 98767d61-b2e8-4d71-b661-e36783ee24c1
- Status: test
- Level: medium
- Author: Hieu Tran
- Date: 2023-03-13
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_decode_gzip.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1132-data_encoding|T1132.001]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - GZipStream
  - ::Decompress
condition: selection
```

## False Positives

- Legitimate administrative scripts may use this functionality. Use "ParentImage" in combination with the script names and allowed users and applications to filter legitimate executions

## References

- https://www.zscaler.com/blogs/security-research/onenote-growing-threat-malware-distribution

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_decode_gzip.yml)
