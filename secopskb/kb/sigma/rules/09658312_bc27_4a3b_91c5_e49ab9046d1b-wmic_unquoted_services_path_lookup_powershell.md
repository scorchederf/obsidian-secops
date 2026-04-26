---
sigma_id: "09658312-bc27-4a3b-91c5-e49ab9046d1b"
title: "WMIC Unquoted Services Path Lookup - PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_wmi_unquoted_service_search.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_wmi_unquoted_service_search.yml"
build_date: "2026-04-26 14:14:39"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "09658312-bc27-4a3b-91c5-e49ab9046d1b"
  - "WMIC Unquoted Services Path Lookup - PowerShell"
attack_technique_ids:
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# WMIC Unquoted Services Path Lookup - PowerShell

Detects known WMI recon method to look for unquoted service paths, often used by pentest inside of powershell scripts attackers enum scripts

## Metadata

- Rule ID: 09658312-bc27-4a3b-91c5-e49ab9046d1b
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-20
- Modified: 2022-11-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_wmi_unquoted_service_search.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
  - 'Get-WmiObject '
  - 'gwmi '
  ScriptBlockText|contains|all:
  - ' Win32_Service '
  - Name
  - DisplayName
  - PathName
  - StartMode
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/nccgroup/redsnarf/blob/35949b30106ae543dc6f2bc3f1be10c6d9a8d40e/redsnarf.py
- https://github.com/S3cur3Th1sSh1t/Creds/blob/eac23d67f7f90c7fc8e3130587d86158c22aa398/PowershellScripts/jaws-enum.ps1
- https://www.absolomb.com/2018-01-26-Windows-Privilege-Escalation-Guide/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_wmi_unquoted_service_search.yml)
