---
sigma_id: "0a1255c5-d732-4b62-ac02-b5152d34fb83"
title: "ADExplorer Writing Complete AD Snapshot Into .dat File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_sysinternals_adexplorer_dump_written.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sysinternals_adexplorer_dump_written.yml"
build_date: "2026-04-26 14:14:19"
status: "experimental"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "0a1255c5-d732-4b62-ac02-b5152d34fb83"
  - "ADExplorer Writing Complete AD Snapshot Into .dat File"
attack_technique_ids:
  - "T1087.002"
  - "T1069.002"
  - "T1482"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ADExplorer Writing Complete AD Snapshot Into .dat File

Detects the dual use tool ADExplorer writing a complete AD snapshot into a .dat file. This can be used by attackers to extract data for Bloodhound, usernames for password spraying or use the meta data for social engineering. The snapshot doesn't contain password hashes but there have been cases, where administrators put passwords in the comment field.

## Metadata

- Rule ID: 0a1255c5-d732-4b62-ac02-b5152d34fb83
- Status: experimental
- Level: medium
- Author: Arnim Rupp (Nextron Systems), Thomas Patzke
- Date: 2025-07-09
- Source Path: rules/windows/file/file_event/file_event_win_sysinternals_adexplorer_dump_written.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]
- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.002]]
- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482]]

## Detection

```yaml
selection:
  Image|endswith:
  - \ADExp.exe
  - \ADExplorer.exe
  - \ADExplorer64.exe
  - \ADExplorer64a.exe
  TargetFilename|endswith: .dat
condition: selection
```

## False Positives

- Legitimate use of ADExplorer by administrators creating .dat snapshots

## References

- https://learn.microsoft.com/de-de/sysinternals/downloads/adexplorer
- https://github.com/c3c/ADExplorerSnapshot.py/tree/f700904defac330802bbfedd1d8ffd9248f4ee24
- https://www.packetlabs.net/posts/scattered-spider-is-a-young-ransomware-gang-exploiting-large-corporations/
- https://www.nccgroup.com/us/research-blog/lapsus-recent-techniques-tactics-and-procedures/
- https://trustedsec.com/blog/adexplorer-on-engagements

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sysinternals_adexplorer_dump_written.yml)
