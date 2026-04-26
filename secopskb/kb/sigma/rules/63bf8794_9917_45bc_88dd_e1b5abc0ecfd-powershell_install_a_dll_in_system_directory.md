---
sigma_id: "63bf8794-9917-45bc-88dd-e1b5abc0ecfd"
title: "Powershell Install a DLL in System Directory"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_copy_item_system_directory.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_copy_item_system_directory.yml"
build_date: "2026-04-26 15:01:50"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "63bf8794-9917-45bc-88dd-e1b5abc0ecfd"
  - "Powershell Install a DLL in System Directory"
attack_technique_ids:
  - "T1556.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Powershell Install a DLL in System Directory

Uses PowerShell to install/copy a file into a system directory such as "System32" or "SysWOW64"

## Metadata

- Rule ID: 63bf8794-9917-45bc-88dd-e1b5abc0ecfd
- Status: test
- Level: high
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-12-27
- Modified: 2024-01-22
- Source Path: rules/windows/powershell/powershell_script/posh_ps_copy_item_system_directory.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1556-modify_authentication_process|T1556.002]]

## Detection

```yaml
selection:
  ScriptBlockText|re: (Copy-Item|cpi) .{2,128} -Destination .{1,32}\\Windows\\(System32|SysWOW64)
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1556.002/T1556.002.md#atomic-test-1---install-and-register-password-filter-dll

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_copy_item_system_directory.yml)
