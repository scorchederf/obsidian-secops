---
sigma_id: "66a4d409-451b-4151-94f4-a55d559c49b0"
title: "PowerShell Deleted Mounted Share"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_mounted_share_deletion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_mounted_share_deletion.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "66a4d409-451b-4151-94f4-a55d559c49b0"
  - "PowerShell Deleted Mounted Share"
attack_technique_ids:
  - "T1070.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Deleted Mounted Share

Detects when when a mounted share is removed. Adversaries may remove share connections that are no longer useful in order to clean up traces of their operation

## Metadata

- Rule ID: 66a4d409-451b-4151-94f4-a55d559c49b0
- Status: test
- Level: medium
- Author: oscd.community, @redcanary, Zach Stanford @svch0st
- Date: 2020-10-08
- Modified: 2025-10-07
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_mounted_share_deletion.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.005]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
  - Remove-SmbShare
  - Remove-FileShare
filter_main_module_load:
  ScriptBlockText|contains|all:
  - FileShare.cdxml
  - Microsoft.PowerShell.Core\Export-ModuleMember
  - ROOT/Microsoft/Windows/Storage/MSFT_FileShare
  - ObjectModelWrapper
  - Cmdletization.MethodParameter
condition: selection and not 1 of filter_main_*
```

## False Positives

- Administrators or Power users may remove their shares via cmd line

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.005/T1070.005.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_mounted_share_deletion.yml)
