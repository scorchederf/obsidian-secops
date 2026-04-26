---
sigma_id: "bd8b828d-0dca-48e1-8a63-8a58ecf2644f"
title: "Group Membership Reconnaissance Via Whoami.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_whoami_groups_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_whoami_groups_discovery.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "bd8b828d-0dca-48e1-8a63-8a58ecf2644f"
  - "Group Membership Reconnaissance Via Whoami.EXE"
attack_technique_ids:
  - "T1033"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Group Membership Reconnaissance Via Whoami.EXE

Detects the execution of whoami.exe with the /group command line flag to show group membership for the current user, account type, security identifiers (SID), and attributes.

## Metadata

- Rule ID: bd8b828d-0dca-48e1-8a63-8a58ecf2644f
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-28
- Source Path: rules/windows/process_creation/proc_creation_win_whoami_groups_discovery.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]

## Detection

```yaml
selection_img:
- Image|endswith: \whoami.exe
- OriginalFileName: whoami.exe
selection_cli:
  CommandLine|contains:
  - ' /groups'
  - ' -groups'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/whoami

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_whoami_groups_discovery.yml)
