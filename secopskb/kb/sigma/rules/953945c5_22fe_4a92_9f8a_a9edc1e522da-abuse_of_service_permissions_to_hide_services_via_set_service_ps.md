---
sigma_id: "953945c5-22fe-4a92-9f8a-a9edc1e522da"
title: "Abuse of Service Permissions to Hide Services Via Set-Service - PS"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_using_set_service_to_hide_services.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_using_set_service_to_hide_services.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "953945c5-22fe-4a92-9f8a-a9edc1e522da"
  - "Abuse of Service Permissions to Hide Services Via Set-Service - PS"
attack_technique_ids:
  - "T1574.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects usage of the "Set-Service" powershell cmdlet to configure a new SecurityDescriptor that allows a service to be hidden from other utilities such as "sc.exe", "Get-Service"...etc. (Works only in powershell 7)

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574011-services-registry-permissions-weakness|T1574.011: Services Registry Permissions Weakness]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - 'Set-Service '
  - DCLCWPDTSD
  ScriptBlockText|contains:
  - '-SecurityDescriptorSddl '
  - '-sd '
condition: selection
```

## False Positives

- Rare intended use of hidden services
- Rare FP could occur due to the non linearity of the ScriptBlockText log

## References

- https://twitter.com/Alh4zr3d/status/1580925761996828672
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-service?view=powershell-7.2

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_using_set_service_to_hide_services.yml)
