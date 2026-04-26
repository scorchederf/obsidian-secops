---
sigma_id: "502b42de-4306-40b4-9596-6f590c81f073"
title: "Local Accounts Discovery"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_local_system_owner_account_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_local_system_owner_account_discovery.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "502b42de-4306-40b4-9596-6f590c81f073"
  - "Local Accounts Discovery"
attack_technique_ids:
  - "T1033"
  - "T1087.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Local Accounts Discovery

Local accounts, System Owner/User discovery using operating systems utilities

## Metadata

- Rule ID: 502b42de-4306-40b4-9596-6f590c81f073
- Status: test
- Level: low
- Author: Timur Zinniatullin, Daniil Yugoslavskiy, oscd.community
- Date: 2019-10-21
- Modified: 2025-10-20
- Source Path: rules/windows/process_creation/proc_creation_win_susp_local_system_owner_account_discovery.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]
- [[kb/attack/techniques/T1087-account_discovery|T1087.001]]

## Detection

```yaml
selection_other_img:
- Image|endswith:
  - \whoami.exe
  - \quser.exe
  - \qwinsta.exe
- OriginalFileName:
  - whoami.exe
  - quser.exe
  - qwinsta.exe
selection_other_wmi:
  Image|endswith: \wmic.exe
  CommandLine|contains|all:
  - useraccount
  - get
selection_other_cmdkey:
  Image|endswith: \cmdkey.exe
  CommandLine|contains: ' /l'
selection_cmd:
  Image|endswith: \cmd.exe
  CommandLine|contains|all:
  - ' /c'
  - 'dir '
  - \Users\
filter_cmd:
  CommandLine|contains: ' rmdir '
selection_net:
  Image|endswith:
  - \net.exe
  - \net1.exe
  CommandLine|contains: user
filter_net:
  CommandLine|contains:
  - /domain
  - /add
  - /delete
  - /active
  - /expires
  - /passwordreq
  - /scriptpath
  - /times
  - /workstations
condition: (selection_cmd and not filter_cmd) or (selection_net and not filter_net)
  or 1 of selection_other_*
```

## False Positives

- Legitimate administrator or user enumerates local users for legitimate reason

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1033/T1033.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_local_system_owner_account_discovery.yml)
