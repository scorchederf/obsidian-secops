---
sigma_id: "df9a0e0e-fedb-4d6c-8668-d765dfc92aa7"
title: "Suspicious Non PowerShell WSMAN COM Provider"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_classic/posh_pc_wsman_com_provider_no_powershell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_wsman_com_provider_no_powershell.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / powershell-classic"
aliases:
  - "df9a0e0e-fedb-4d6c-8668-d765dfc92aa7"
  - "Suspicious Non PowerShell WSMAN COM Provider"
attack_technique_ids:
  - "T1059.001"
  - "T1021.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Non PowerShell WSMAN COM Provider

Detects suspicious use of the WSMAN provider without PowerShell.exe as the host application.

## Metadata

- Rule ID: df9a0e0e-fedb-4d6c-8668-d765dfc92aa7
- Status: test
- Level: medium
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2020-06-24
- Modified: 2025-10-22
- Source Path: rules/windows/powershell/powershell_classic/posh_pc_wsman_com_provider_no_powershell.yml

## Logsource

- product: windows
- service: powershell-classic

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1021-remote_services|T1021.003]]

## Detection

```yaml
selection:
  Data|contains: ProviderName=WSMan
filter_main_ps:
  Data|contains:
  - HostApplication=powershell
  - HostApplication=C:\Windows\System32\WindowsPowerShell\v1.0\powershell
  - HostApplication=C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell
  - HostApplication=C:/Windows/System32/WindowsPowerShell/v1.0/powershell
  - HostApplication=C:/Windows/SysWOW64/WindowsPowerShell/v1.0/powershell
filter_main_host_application_null:
  Data|re: HostId=[a-zA-Z0-9-]{36}\s+EngineVersion=
filter_optional_hexnode:
  Data|contains: HostApplication=C:\Hexnode\Hexnode Agent\Current\HexnodeAgent.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://twitter.com/chadtilbury/status/1275851297770610688
- https://bohops.com/2020/05/12/ws-management-com-another-approach-for-winrm-lateral-movement/
- https://github.com/bohops/WSMan-WinRM

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_wsman_com_provider_no_powershell.yml)
