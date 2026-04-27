---
sigma_id: "40b19fa6-d835-400c-b301-41f3a2baacaf"
title: "VolumeShadowCopy Symlink Creation Via Mklink"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_mklink_shadow_copies_access_symlink.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_mklink_shadow_copies_access_symlink.yml"
build_date: "2026-04-26 17:03:23"
status: "stable"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "40b19fa6-d835-400c-b301-41f3a2baacaf"
  - "VolumeShadowCopy Symlink Creation Via Mklink"
attack_technique_ids:
  - "T1003.002"
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# VolumeShadowCopy Symlink Creation Via Mklink

Shadow Copies storage symbolic link creation using operating systems utilities

## Metadata

- Rule ID: 40b19fa6-d835-400c-b301-41f3a2baacaf
- Status: stable
- Level: high
- Author: Teymur Kheirkhabarov, oscd.community
- Date: 2019-10-22
- Modified: 2023-03-06
- Source Path: rules/windows/process_creation/proc_creation_win_cmd_mklink_shadow_copies_access_symlink.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - mklink
  - HarddiskVolumeShadowCopy
condition: selection
```

## False Positives

- Legitimate administrator working with shadow copies, access for backup purposes

## References

- https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-windows-environment

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_mklink_shadow_copies_access_symlink.yml)
