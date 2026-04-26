---
sigma_id: "9212f354-7775-4e28-9c9f-8f0a4544e664"
title: "Active Directory Database Snapshot Via ADExplorer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_adexplorer_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_adexplorer_execution.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9212f354-7775-4e28-9c9f-8f0a4544e664"
  - "Active Directory Database Snapshot Via ADExplorer"
attack_technique_ids:
  - "T1087.002"
  - "T1069.002"
  - "T1482"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Active Directory Database Snapshot Via ADExplorer

Detects the execution of Sysinternals ADExplorer with the "-snapshot" flag in order to save a local copy of the active directory database. This can be used by attackers to extract data for Bloodhound, usernames for password spraying or use the meta data for social engineering. The snapshot doesn't contain password hashes but there have been cases, where administrators put passwords in the comment field.

## Metadata

- Rule ID: 9212f354-7775-4e28-9c9f-8f0a4544e664
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-03-14
- Modified: 2025-07-09
- Source Path: rules/windows/process_creation/proc_creation_win_sysinternals_adexplorer_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]
- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.002]]
- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \ADExp.exe
  - \ADExplorer.exe
  - \ADExplorer64.exe
  - \ADExplorer64a.exe
- OriginalFileName: AdExp
- Description: Active Directory Editor
- Product: Sysinternals ADExplorer
selection_cli:
  CommandLine|contains: snapshot
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.documentcloud.org/documents/5743766-Global-Threat-Report-2019.html
- https://learn.microsoft.com/de-de/sysinternals/downloads/adexplorer
- https://github.com/c3c/ADExplorerSnapshot.py/tree/f700904defac330802bbfedd1d8ffd9248f4ee24
- https://www.packetlabs.net/posts/scattered-spider-is-a-young-ransomware-gang-exploiting-large-corporations/
- https://www.nccgroup.com/us/research-blog/lapsus-recent-techniques-tactics-and-procedures/
- https://trustedsec.com/blog/adexplorer-on-engagements

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_adexplorer_execution.yml)
