---
sigma_id: "02b64f1b-3f33-4e67-aede-ef3b0a5a8fcf"
title: "Potential COM Objects Download Cradles Usage - Process Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_download_com_cradles.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_download_com_cradles.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "02b64f1b-3f33-4e67-aede-ef3b0a5a8fcf"
  - "Potential COM Objects Download Cradles Usage - Process Creation"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential COM Objects Download Cradles Usage - Process Creation

Detects usage of COM objects that can be abused to download files in PowerShell by CLSID

## Metadata

- Rule ID: 02b64f1b-3f33-4e67-aede-ef3b0a5a8fcf
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-12-25
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_download_com_cradles.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection_1:
  CommandLine|contains: '[Type]::GetTypeFromCLSID('
selection_2:
  CommandLine|contains:
  - 0002DF01-0000-0000-C000-000000000046
  - F6D90F16-9C73-11D3-B32E-00C04F990BB4
  - F5078F35-C551-11D3-89B9-0000F81FE221
  - 88d96a0a-f192-11d4-a65f-0040963251e5
  - AFBA6B42-5692-48EA-8141-DC517DCF0EF1
  - AFB40FFD-B609-40A3-9828-F88BBE11E4E3
  - 88d96a0b-f192-11d4-a65f-0040963251e5
  - 2087c2f4-2cef-4953-a8ab-66779b670495
  - 000209FF-0000-0000-C000-000000000046
  - 00024500-0000-0000-C000-000000000046
condition: all of selection_*
```

## False Positives

- Legitimate use of the library

## References

- https://learn.microsoft.com/en-us/dotnet/api/system.type.gettypefromclsid?view=net-7.0
- https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=57

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_download_com_cradles.yml)
