---
sigma_id: "514e4c3a-c77d-4cde-a00f-046425e2301e"
title: "Abuse of Service Permissions to Hide Services Via Set-Service"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_hide_services_via_set_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_hide_services_via_set_service.yml"
build_date: "2026-04-26 15:01:43"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "514e4c3a-c77d-4cde-a00f-046425e2301e"
  - "Abuse of Service Permissions to Hide Services Via Set-Service"
attack_technique_ids:
  - "T1574.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Abuse of Service Permissions to Hide Services Via Set-Service

Detects usage of the "Set-Service" powershell cmdlet to configure a new SecurityDescriptor that allows a service to be hidden from other utilities such as "sc.exe", "Get-Service"...etc. (Works only in powershell 7)

## Metadata

- Rule ID: 514e4c3a-c77d-4cde-a00f-046425e2301e
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-17
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_hide_services_via_set_service.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.011]]

## Detection

```yaml
selection_img:
- Image|endswith: \pwsh.exe
- OriginalFileName: pwsh.dll
selection_sddl:
  CommandLine|contains|all:
  - 'Set-Service '
  - DCLCWPDTSD
selection_cmdlet:
  CommandLine|contains:
  - '-SecurityDescriptorSddl '
  - '-sd '
condition: all of selection_*
```

## False Positives

- Rare intended use of hidden services

## References

- https://twitter.com/Alh4zr3d/status/1580925761996828672
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-service?view=powershell-7.2

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_hide_services_via_set_service.yml)
