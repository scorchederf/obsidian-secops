---
sigma_id: "851c506b-6b7c-4ce2-8802-c703009d03c0"
title: "Winlogon Helper DLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_winlogon_helper_dll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_winlogon_helper_dll.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "851c506b-6b7c-4ce2-8802-c703009d03c0"
  - "Winlogon Helper DLL"
attack_technique_ids:
  - "T1547.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Winlogon Helper DLL

Winlogon.exe is a Windows component responsible for actions at logon/logoff as well as the secure attention sequence (SAS) triggered by Ctrl-Alt-Delete.
Registry entries in HKLM\Software[Wow6432Node]Microsoft\Windows NT\CurrentVersion\Winlogon\ and HKCU\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\ are
used to manage additional helper programs and functionalities that support Winlogon. Malicious modifications to these Registry keys may cause Winlogon to
load and execute malicious DLLs and/or executables.

## Metadata

- Rule ID: 851c506b-6b7c-4ce2-8802-c703009d03c0
- Status: test
- Level: medium
- Author: Timur Zinniatullin, oscd.community
- Date: 2019-10-21
- Modified: 2022-07-07
- Source Path: rules/windows/powershell/powershell_script/posh_ps_winlogon_helper_dll.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.004]]

## Detection

```yaml
selection:
  ScriptBlockText|contains: CurrentVersion\Winlogon
selection2:
  ScriptBlockText|contains:
  - Set-ItemProperty
  - New-Item
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1547.004/T1547.004.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_winlogon_helper_dll.yml)
