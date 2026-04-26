---
sigma_id: "022eaba8-f0bf-4dd9-9217-4604b0bb3bb0"
title: "HackTool - Wmiexec Default Powershell Command"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_wmiexec_default_powershell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_wmiexec_default_powershell.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "022eaba8-f0bf-4dd9-9217-4604b0bb3bb0"
  - "HackTool - Wmiexec Default Powershell Command"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - Wmiexec Default Powershell Command

Detects the execution of PowerShell with a specific flag sequence that is used by the Wmiexec script

## Metadata

- Rule ID: 022eaba8-f0bf-4dd9-9217-4604b0bb3bb0
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-03-08
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_wmiexec_default_powershell.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  CommandLine|contains: -NoP -NoL -sta -NonI -W Hidden -Exec Bypass -Enc
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/fortra/impacket/blob/f4b848fa27654ca95bc0f4c73dbba8b9c2c9f30a/examples/wmiexec.py

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_wmiexec_default_powershell.yml)
