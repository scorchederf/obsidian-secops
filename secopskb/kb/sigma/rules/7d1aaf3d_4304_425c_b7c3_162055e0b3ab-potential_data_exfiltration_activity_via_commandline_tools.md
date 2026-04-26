---
sigma_id: "7d1aaf3d-4304-425c-b7c3-162055e0b3ab"
title: "Potential Data Exfiltration Activity Via CommandLine Tools"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_data_exfiltration_via_cli.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_data_exfiltration_via_cli.yml"
build_date: "2026-04-26 15:01:48"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "7d1aaf3d-4304-425c-b7c3-162055e0b3ab"
  - "Potential Data Exfiltration Activity Via CommandLine Tools"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Data Exfiltration Activity Via CommandLine Tools

Detects the use of various CLI utilities exfiltrating data via web requests

## Metadata

- Rule ID: 7d1aaf3d-4304-425c-b7c3-162055e0b3ab
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-02
- Modified: 2025-10-19
- Source Path: rules/windows/process_creation/proc_creation_win_susp_data_exfiltration_via_cli.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_iwr:
  Image|endswith:
  - \powershell_ise.exe
  - \powershell.exe
  - \pwsh.exe
  - \cmd.exe
  CommandLine|contains:
  - 'curl '
  - Invoke-RestMethod
  - Invoke-WebRequest
  - 'irm '
  - 'iwr '
  - 'wget '
  CommandLine|contains|all:
  - ' -ur'
  - ' -me'
  - ' -b'
  - ' POST '
selection_curl:
  Image|endswith: \curl.exe
  CommandLine|contains: --ur
selection_curl_data:
  CommandLine|contains:
  - ' -d '
  - ' --data '
selection_wget:
  Image|endswith: \wget.exe
  CommandLine|contains:
  - --post-data
  - --post-file
payloads:
- CommandLine|re:
  - net\s+view
  - sc\s+query
- CommandLine|contains:
  - Get-Content
  - GetBytes
  - hostname
  - ifconfig
  - ipconfig
  - netstat
  - nltest
  - qprocess
  - systeminfo
  - tasklist
  - ToBase64String
  - whoami
- CommandLine|contains|all:
  - 'type '
  - ' > '
  - ' C:\'
condition: (selection_iwr or all of selection_curl* or selection_wget) and payloads
```

## False Positives

- Unlikely

## References

- https://www.sentinelone.com/blog/living-off-windows-defender-lockbit-ransomware-sideloads-cobalt-strike-through-microsoft-security-tool/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_data_exfiltration_via_cli.yml)
