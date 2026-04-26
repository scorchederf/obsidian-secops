---
sigma_id: "0f0450f3-8b47-441e-a31b-15a91dc243e2"
title: "Potential DLL File Download Via PowerShell Invoke-WebRequest"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_download_dll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_download_dll.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "0f0450f3-8b47-441e-a31b-15a91dc243e2"
  - "Potential DLL File Download Via PowerShell Invoke-WebRequest"
attack_technique_ids:
  - "T1059.001"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential DLL File Download Via PowerShell Invoke-WebRequest

Detects potential DLL files being downloaded using the PowerShell Invoke-WebRequest or Invoke-RestMethod cmdlets.

## Metadata

- Rule ID: 0f0450f3-8b47-441e-a31b-15a91dc243e2
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Hieu Tran
- Date: 2023-03-13
- Modified: 2025-07-18
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_download_dll.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - 'Invoke-RestMethod '
  - 'Invoke-WebRequest '
  - 'IRM '
  - 'IWR '
  CommandLine|contains|all:
  - http
  - OutFile
  - .dll
condition: selection
```

## False Positives

- Unknown

## References

- https://www.zscaler.com/blogs/security-research/onenote-growing-threat-malware-distribution

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_download_dll.yml)
