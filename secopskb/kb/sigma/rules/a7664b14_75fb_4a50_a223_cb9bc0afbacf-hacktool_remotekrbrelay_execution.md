---
sigma_id: "a7664b14-75fb-4a50-a223-cb9bc0afbacf"
title: "HackTool - RemoteKrbRelay Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_krbrelay_remote.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_krbrelay_remote.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a7664b14-75fb-4a50-a223-cb9bc0afbacf"
  - "HackTool - RemoteKrbRelay Execution"
attack_technique_ids:
  - "T1558.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - RemoteKrbRelay Execution

Detects the use of RemoteKrbRelay, a Kerberos relaying tool via CommandLine flags and PE metadata.

## Metadata

- Rule ID: a7664b14-75fb-4a50-a223-cb9bc0afbacf
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-06-27
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_krbrelay_remote.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558.003]]

## Detection

```yaml
selection_img:
- Image|endswith: \RemoteKrbRelay.exe
- OriginalFileName: RemoteKrbRelay.exe
selection_cli_required:
  CommandLine|contains|all:
  - ' -clsid '
  - ' -target '
  - ' -victim '
selection_cli_attack_smb:
  CommandLine|contains|all:
  - '-smb '
  - '--smbkeyword '
  CommandLine|contains:
  - interactive
  - secrets
  - service-add
selection_cli_attack_rbcd_main:
  CommandLine|contains: '-rbcd '
selection_cli_attack_rbcd_options:
  CommandLine|contains:
  - '-cn '
  - '--computername '
selection_cli_attack_changepass:
  CommandLine|contains: '-chp '
  CommandLine|contains|all:
  - '-chpPass '
  - '-chpUser '
selection_cli_attack_addgrpname:
  CommandLine|contains|all:
  - '-addgroupmember '
  - '-group '
  - '-groupuser '
condition: selection_img or selection_cli_required or all of selection_cli_attack_rbcd_*
  or selection_cli_attack_changepass or selection_cli_attack_addgrpname or selection_cli_attack_smb
```

## False Positives

- Unlikely

## References

- https://github.com/CICADA8-Research/RemoteKrbRelay

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_krbrelay_remote.yml)
