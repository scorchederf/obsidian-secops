---
sigma_id: "d95de845-b83c-4a9a-8a6a-4fc802ebf6c0"
title: "Suspicious Group And Account Reconnaissance Activity Using Net.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_net_groups_and_accounts_recon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_groups_and_accounts_recon.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d95de845-b83c-4a9a-8a6a-4fc802ebf6c0"
  - "Suspicious Group And Account Reconnaissance Activity Using Net.EXE"
attack_technique_ids:
  - "T1087.001"
  - "T1087.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Group And Account Reconnaissance Activity Using Net.EXE

Detects suspicious reconnaissance command line activity on Windows systems using Net.EXE
Check if the user that executed the commands is suspicious (e.g. service accounts, LOCAL_SYSTEM)

## Metadata

- Rule ID: d95de845-b83c-4a9a-8a6a-4fc802ebf6c0
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), omkar72, @svch0st, Nasreddine Bencherchali (Nextron Systems)
- Date: 2019-01-16
- Modified: 2023-03-02
- Source Path: rules/windows/process_creation/proc_creation_win_net_groups_and_accounts_recon.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087.001]]
- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \net.exe
  - \net1.exe
- OriginalFileName:
  - net.exe
  - net1.exe
selection_group_root:
  CommandLine|contains:
  - ' group '
  - ' localgroup '
selection_group_flags:
  CommandLine|contains:
  - domain admins
  - ' administrator'
  - ' administrateur'
  - enterprise admins
  - Exchange Trusted Subsystem
  - Remote Desktop Users
  - Utilisateurs du Bureau à distance
  - Usuarios de escritorio remoto
  - ' /do'
filter_group_add:
  CommandLine|contains: ' /add'
selection_accounts_root:
  CommandLine|contains: ' accounts '
selection_accounts_flags:
  CommandLine|contains: ' /do'
condition: selection_img and ((all of selection_group_* and not filter_group_add)
  or all of selection_accounts_*)
```

## False Positives

- Inventory tool runs
- Administrative activity

## References

- https://redcanary.com/blog/how-one-hospital-thwarted-a-ryuk-ransomware-outbreak/
- https://thedfirreport.com/2020/10/18/ryuk-in-5-hours/
- https://research.nccgroup.com/2022/08/19/back-in-black-unlocking-a-lockbit-3-0-ransomware-attack/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_groups_and_accounts_recon.yml)
