---
sigma_id: "b3ad3c0f-c949-47a1-a30e-b0491ccae876"
title: "Uncommon Connection to Active Directory Web Services"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_adws_unusual_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_adws_unusual_connection.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "b3ad3c0f-c949-47a1-a30e-b0491ccae876"
  - "Uncommon Connection to Active Directory Web Services"
attack_technique_ids:
  - "T1087"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Uncommon Connection to Active Directory Web Services

Detects uncommon network connections to the Active Directory Web Services (ADWS) from processes not typically associated with ADWS management.

## Metadata

- Rule ID: b3ad3c0f-c949-47a1-a30e-b0491ccae876
- Status: test
- Level: medium
- Author: @kostastsale
- Date: 2024-01-26
- Source Path: rules/windows/network_connection/net_connection_win_adws_unusual_connection.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087]]

## Detection

```yaml
selection:
  Initiated: true
  DestinationPort: 9389
filter_main_dsac:
  Image: C:\Windows\system32\dsac.exe
filter_main_ms_monitoring_agent:
  Image: C:\Program Files\Microsoft Monitoring Agent\
filter_main_powershell:
  Image|startswith:
  - C:\Program Files\PowerShell\7\pwsh.exe
  - C:\Program Files\PowerShell\7-preview\pwsh.ex
  - C:\Windows\System32\WindowsPowerShell\
  - C:\Windows\SysWOW64\WindowsPowerShell\
condition: selection and not 1 of filter_main_*
```

## False Positives

- ADWS is used by a number of legitimate applications that need to interact with Active Directory. These applications should be added to the allow-listing to avoid false positives.

## References

- https://medium.com/falconforce/soaphound-tool-to-collect-active-directory-data-via-adws-165aca78288c
- https://github.com/FalconForceTeam/FalconFriday/blob/a9219dfcfd89836f34660223f47d766982bdce46/Discovery/ADWS_Connection_from_Unexpected_Binary-Win.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_adws_unusual_connection.yml)
