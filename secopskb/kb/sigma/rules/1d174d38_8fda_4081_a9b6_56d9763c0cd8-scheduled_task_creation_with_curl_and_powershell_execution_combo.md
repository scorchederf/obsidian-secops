---
sigma_id: "1d174d38-8fda-4081-a9b6-56d9763c0cd8"
title: "Scheduled Task Creation with Curl and PowerShell Execution Combo"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_curl_and_powershell_combo.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_curl_and_powershell_combo.yml"
build_date: "2026-04-26 14:14:35"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "1d174d38-8fda-4081-a9b6-56d9763c0cd8"
  - "Scheduled Task Creation with Curl and PowerShell Execution Combo"
attack_technique_ids:
  - "T1053.005"
  - "T1218"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Scheduled Task Creation with Curl and PowerShell Execution Combo

Detects the creation of a scheduled task using schtasks.exe, potentially in combination with curl for downloading payloads and PowerShell for executing them.
This facilitates executing malicious payloads or connecting with C&C server persistently without dropping the malware sample on the host.

## Metadata

- Rule ID: 1d174d38-8fda-4081-a9b6-56d9763c0cd8
- Status: experimental
- Level: medium
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-02-05
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_curl_and_powershell_combo.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection_img:
  Image|endswith: \schtasks.exe
  CommandLine|contains|windash: ' /create '
selection_curl:
  CommandLine|contains|all:
  - 'curl '
  - http
  - -o
selection_powershell:
  CommandLine|contains: powershell
condition: all of selection_*
```

## False Positives

- Legitimate use of schtasks for administrative purposes.
- Automation scripts combining curl and PowerShell in controlled environments.

## References

- https://tria.ge/241015-l98snsyeje/behavioral2

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_curl_and_powershell_combo.yml)
