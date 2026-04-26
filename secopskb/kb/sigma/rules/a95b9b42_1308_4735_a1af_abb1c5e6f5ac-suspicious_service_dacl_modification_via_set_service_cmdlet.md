---
sigma_id: "a95b9b42-1308-4735-a1af-abb1c5e6f5ac"
title: "Suspicious Service DACL Modification Via Set-Service Cmdlet"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_service_dacl_modification_set_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_service_dacl_modification_set_service.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a95b9b42-1308-4735-a1af-abb1c5e6f5ac"
  - "Suspicious Service DACL Modification Via Set-Service Cmdlet"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Service DACL Modification Via Set-Service Cmdlet

Detects suspicious DACL modifications via the "Set-Service" cmdlet using the "SecurityDescriptorSddl" flag (Only available with PowerShell 7) that can be used to hide services or make them unstopable

## Metadata

- Rule ID: a95b9b42-1308-4735-a1af-abb1c5e6f5ac
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-18
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_service_dacl_modification_set_service.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detection

```yaml
selection_img:
- Image|endswith: \pwsh.exe
- OriginalFileName: pwsh.dll
selection_sddl_flag:
  CommandLine|contains:
  - '-SecurityDescriptorSddl '
  - '-sd '
selection_set_service:
  CommandLine|contains|all:
  - 'Set-Service '
  - D;;
  CommandLine|contains:
  - ;;;IU
  - ;;;SU
  - ;;;BA
  - ;;;SY
  - ;;;WD
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.sans.org/blog/red-team-tactics-hiding-windows-services/
- https://learn.microsoft.com/pt-br/windows/win32/secauthz/sid-strings

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_service_dacl_modification_set_service.yml)
