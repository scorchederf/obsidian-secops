---
sigma_id: "b7216a7d-687e-4c8d-82b1-3080b2ad961f"
title: "Modify Group Policy Settings - ScriptBlockLogging"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_modify_group_policy_settings.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_modify_group_policy_settings.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "b7216a7d-687e-4c8d-82b1-3080b2ad961f"
  - "Modify Group Policy Settings - ScriptBlockLogging"
attack_technique_ids:
  - "T1484.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Modify Group Policy Settings - ScriptBlockLogging

Detect malicious GPO modifications can be used to implement many other malicious behaviors.

## Metadata

- Rule ID: b7216a7d-687e-4c8d-82b1-3080b2ad961f
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-08-19
- Source Path: rules/windows/powershell/powershell_script/posh_ps_modify_group_policy_settings.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1484-domain_or_tenant_policy_modification|T1484.001]]

## Detection

```yaml
selection_path:
  ScriptBlockText|contains: \SOFTWARE\Policies\Microsoft\Windows\System
selection_key:
  ScriptBlockText|contains:
  - GroupPolicyRefreshTimeDC
  - GroupPolicyRefreshTimeOffsetDC
  - GroupPolicyRefreshTime
  - GroupPolicyRefreshTimeOffset
  - EnableSmartScreen
  - ShellSmartScreenLevel
condition: all of selection_*
```

## False Positives

- Legitimate use

## References

- https://github.com/redcanaryco/atomic-red-team/blob/40b77d63808dd4f4eafb83949805636735a1fd15/atomics/T1484.001/T1484.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_modify_group_policy_settings.yml)
