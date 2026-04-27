---
sigma_id: "02773bed-83bf-469f-b7ff-e676e7d78bab"
title: "BloodHound Collection Files"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_bloodhound_collection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_bloodhound_collection.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "02773bed-83bf-469f-b7ff-e676e7d78bab"
  - "BloodHound Collection Files"
attack_technique_ids:
  - "T1087.001"
  - "T1087.002"
  - "T1482"
  - "T1069.001"
  - "T1069.002"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects default file names outputted by the BloodHound collection tool SharpHound

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1087-account_discovery#^t1087001-local-account|T1087.001: Local Account]]
- [[kb/attack/techniques/T1087-account_discovery#^t1087002-domain-account|T1087.002: Domain Account]]
- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482: Domain Trust Discovery]]
- [[kb/attack/techniques/T1069-permission_groups_discovery#^t1069001-local-groups|T1069.001: Local Groups]]
- [[kb/attack/techniques/T1069-permission_groups_discovery#^t1069002-domain-groups|T1069.002: Domain Groups]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

## Detection

```yaml
selection:
  TargetFilename|endswith:
  - BloodHound.zip
  - _computers.json
  - _containers.json
  - _gpos.json
  - _groups.json
  - _ous.json
  - _users.json
filter_optional_ms_winapps:
  Image|endswith: \svchost.exe
  TargetFilename|startswith: C:\Program Files\WindowsApps\Microsoft.
  TargetFilename|endswith: \pocket_containers.json
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Some false positives may arise in some environment and this may require some tuning. Add additional filters or reduce level depending on the level of noise

## References

- https://academy.hackthebox.com/course/preview/active-directory-bloodhound/bloodhound--data-collection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_bloodhound_collection.yml)
