---
sigma_id: "42d36aa1-3240-4db0-8257-e0118dcdd9cd"
title: "Suspicious Hyper-V Cmdlets"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_hyper_v_condlet.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_hyper_v_condlet.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "42d36aa1-3240-4db0-8257-e0118dcdd9cd"
  - "Suspicious Hyper-V Cmdlets"
attack_technique_ids:
  - "T1564.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Hyper-V Cmdlets

Adversaries may carry out malicious operations using a virtual instance to avoid detection

## Metadata

- Rule ID: 42d36aa1-3240-4db0-8257-e0118dcdd9cd
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-04-09
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_hyper_v_condlet.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.006]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
  - New-VM
  - Set-VMFirmware
  - Start-VM
condition: selection
```

## False Positives

- Legitimate PowerShell scripts

## References

- https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1564.006/T1564.006.md#atomic-test-3---create-and-start-hyper-v-virtual-machine

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_hyper_v_condlet.yml)
