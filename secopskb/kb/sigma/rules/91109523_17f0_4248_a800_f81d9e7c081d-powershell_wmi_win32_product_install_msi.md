---
sigma_id: "91109523-17f0-4248-a800-f81d9e7c081d"
title: "PowerShell WMI Win32_Product Install MSI"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_win32_product_install_msi.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_win32_product_install_msi.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "91109523-17f0-4248-a800-f81d9e7c081d"
  - "PowerShell WMI Win32_Product Install MSI"
attack_technique_ids:
  - "T1218.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell WMI Win32_Product Install MSI

Detects the execution of an MSI file using PowerShell and the WMI Win32_Product class

## Metadata

- Rule ID: 91109523-17f0-4248-a800-f81d9e7c081d
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-04-24
- Source Path: rules/windows/powershell/powershell_script/posh_ps_win32_product_install_msi.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.007]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - 'Invoke-CimMethod '
  - '-ClassName '
  - 'Win32_Product '
  - '-MethodName '
  - .msi
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218.007/T1218.007.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_win32_product_install_msi.yml)
