---
sigma_id: "cd185561-4760-45d6-a63e-a51325112cae"
title: "Live Memory Dump Using Powershell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_memorydump_getstoragediagnosticinfo.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_memorydump_getstoragediagnosticinfo.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "cd185561-4760-45d6-a63e-a51325112cae"
  - "Live Memory Dump Using Powershell"
attack_technique_ids:
  - "T1003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Live Memory Dump Using Powershell

Detects usage of a PowerShell command to dump the live memory of a Windows machine

## Metadata

- Rule ID: cd185561-4760-45d6-a63e-a51325112cae
- Status: test
- Level: high
- Author: Max Altgelt (Nextron Systems)
- Date: 2021-09-21
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_memorydump_getstoragediagnosticinfo.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - Get-StorageDiagnosticInfo
  - -IncludeLiveDump
condition: selection
```

## False Positives

- Diagnostics

## References

- https://learn.microsoft.com/en-us/powershell/module/storage/get-storagediagnosticinfo?view=windowsserver2022-ps

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_memorydump_getstoragediagnosticinfo.yml)
