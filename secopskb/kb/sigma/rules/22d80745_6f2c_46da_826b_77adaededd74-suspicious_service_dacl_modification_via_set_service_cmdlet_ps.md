---
sigma_id: "22d80745-6f2c-46da-826b-77adaededd74"
title: "Suspicious Service DACL Modification Via Set-Service Cmdlet - PS"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_service_dacl_modification_set_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_service_dacl_modification_set_service.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "22d80745-6f2c-46da-826b-77adaededd74"
  - "Suspicious Service DACL Modification Via Set-Service Cmdlet - PS"
attack_technique_ids:
  - "T1574.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Service DACL Modification Via Set-Service Cmdlet - PS

Detects usage of the "Set-Service" powershell cmdlet to configure a new SecurityDescriptor that allows a service to be hidden from other utilities such as "sc.exe", "Get-Service"...etc. (Works only in powershell 7)

## Metadata

- Rule ID: 22d80745-6f2c-46da-826b-77adaededd74
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-24
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_service_dacl_modification_set_service.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.011]]

## Detection

```yaml
selection_sddl_flag:
  ScriptBlockText|contains:
  - '-SecurityDescriptorSddl '
  - '-sd '
selection_set_service:
  ScriptBlockText|contains|all:
  - 'Set-Service '
  - D;;
  ScriptBlockText|contains:
  - ;;;IU
  - ;;;SU
  - ;;;BA
  - ;;;SY
  - ;;;WD
condition: all of selection_*
```

## False Positives

- Rare intended use of hidden services
- Rare FP could occur due to the non linearity of the ScriptBlockText log

## References

- https://twitter.com/Alh4zr3d/status/1580925761996828672
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-service?view=powershell-7.2

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_service_dacl_modification_set_service.yml)
