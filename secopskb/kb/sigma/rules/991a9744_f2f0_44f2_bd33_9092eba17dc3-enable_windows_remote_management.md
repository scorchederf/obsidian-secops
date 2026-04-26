---
sigma_id: "991a9744-f2f0-44f2-bd33-9092eba17dc3"
title: "Enable Windows Remote Management"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_enable_psremoting.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_enable_psremoting.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "991a9744-f2f0-44f2-bd33-9092eba17dc3"
  - "Enable Windows Remote Management"
attack_technique_ids:
  - "T1021.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Enable Windows Remote Management

Adversaries may use Valid Accounts to interact with remote systems using Windows Remote Management (WinRM). The adversary may then perform actions as the logged-on user.

## Metadata

- Rule ID: 991a9744-f2f0-44f2-bd33-9092eba17dc3
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-07
- Source Path: rules/windows/powershell/powershell_script/posh_ps_enable_psremoting.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.006]]

## Detection

```yaml
selection_cmdlet:
  ScriptBlockText|contains: 'Enable-PSRemoting '
condition: selection_cmdlet
```

## False Positives

- Legitimate script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1021.006/T1021.006.md#atomic-test-1---enable-windows-remote-management
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enable-psremoting?view=powershell-7.2

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_enable_psremoting.yml)
