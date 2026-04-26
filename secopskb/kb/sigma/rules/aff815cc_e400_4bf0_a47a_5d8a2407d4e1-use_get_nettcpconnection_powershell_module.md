---
sigma_id: "aff815cc-e400-4bf0-a47a-5d8a2407d4e1"
title: "Use Get-NetTCPConnection - PowerShell Module"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_module/posh_pm_susp_get_nettcpconnection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_susp_get_nettcpconnection.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "low"
logsource: "windows / ps_module"
aliases:
  - "aff815cc-e400-4bf0-a47a-5d8a2407d4e1"
  - "Use Get-NetTCPConnection - PowerShell Module"
attack_technique_ids:
  - "T1049"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Use Get-NetTCPConnection - PowerShell Module

Adversaries may attempt to get a listing of network connections to or from the compromised system they are currently accessing or from remote systems by querying for information over the network.

## Metadata

- Rule ID: aff815cc-e400-4bf0-a47a-5d8a2407d4e1
- Status: test
- Level: low
- Author: frack113
- Date: 2021-12-10
- Modified: 2022-12-02
- Source Path: rules/windows/powershell/powershell_module/posh_pm_susp_get_nettcpconnection.yml

## Logsource

- category: ps_module
- definition: 0ad03ef1-f21b-4a79-8ce8-e6900c54b65b
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1049-system_network_connections_discovery|T1049]]

## Detection

```yaml
selection:
  ContextInfo|contains: Get-NetTCPConnection
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1049/T1049.md#atomic-test-2---system-network-connections-discovery-with-powershell

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_module/posh_pm_susp_get_nettcpconnection.yml)
