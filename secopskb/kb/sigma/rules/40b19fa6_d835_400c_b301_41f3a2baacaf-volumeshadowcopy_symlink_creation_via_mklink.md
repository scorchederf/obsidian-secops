---
sigma_id: "40b19fa6-d835-400c-b301-41f3a2baacaf"
title: "VolumeShadowCopy Symlink Creation Via Mklink"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cmd_mklink_shadow_copies_access_symlink.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cmd_mklink_shadow_copies_access_symlink.yml"
build_date: "2026-04-27 19:13:58"
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

Shadow Copies storage symbolic link creation using operating systems utilities

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]
- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]

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
