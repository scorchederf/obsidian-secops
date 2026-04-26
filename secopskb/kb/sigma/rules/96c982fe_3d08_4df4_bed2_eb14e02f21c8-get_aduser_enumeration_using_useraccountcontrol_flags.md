---
sigma_id: "96c982fe-3d08-4df4-bed2-eb14e02f21c8"
title: "Get-ADUser Enumeration Using UserAccountControl Flags"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_as_rep_roasting.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_as_rep_roasting.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "96c982fe-3d08-4df4-bed2-eb14e02f21c8"
  - "Get-ADUser Enumeration Using UserAccountControl Flags"
attack_technique_ids:
  - "T1033"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Get-ADUser Enumeration Using UserAccountControl Flags

Detects AS-REP roasting is an attack that is often-overlooked. It is not very common as you have to explicitly set accounts that do not require pre-authentication.

## Metadata

- Rule ID: 96c982fe-3d08-4df4-bed2-eb14e02f21c8
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-03-17
- Source Path: rules/windows/powershell/powershell_script/posh_ps_as_rep_roasting.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - Get-ADUser
  - -Filter
  - useraccountcontrol
  - -band
  - '4194304'
condition: selection
```

## False Positives

- Legitimate PowerShell scripts

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1069.002/T1069.002.md#atomic-test-11---get-aduser-enumeration-using-useraccountcontrol-flags-as-rep-roasting
- https://shellgeek.com/useraccountcontrol-flags-to-manipulate-properties/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_as_rep_roasting.yml)
