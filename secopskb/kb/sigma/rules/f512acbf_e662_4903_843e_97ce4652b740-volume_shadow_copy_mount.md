---
sigma_id: "f512acbf-e662-4903-843e-97ce4652b740"
title: "Volume Shadow Copy Mount"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/microsoft_windows_ntfs/win_system_volume_shadow_copy_mount.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_ntfs/win_system_volume_shadow_copy_mount.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "low"
logsource: "windows / system"
aliases:
  - "f512acbf-e662-4903-843e-97ce4652b740"
  - "Volume Shadow Copy Mount"
attack_technique_ids:
  - "T1003.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Volume Shadow Copy Mount

Detects volume shadow copy mount via Windows event log

## Metadata

- Rule ID: f512acbf-e662-4903-843e-97ce4652b740
- Status: test
- Level: low
- Author: Roberto Rodriguez @Cyb3rWard0g, Open Threat Research (OTR)
- Date: 2020-10-20
- Modified: 2022-12-25
- Source Path: rules/windows/builtin/system/microsoft_windows_ntfs/win_system_volume_shadow_copy_mount.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]

## Detection

```yaml
selection:
  Provider_Name: Microsoft-Windows-Ntfs
  EventID: 98
  DeviceName|contains: HarddiskVolumeShadowCopy
condition: selection
```

## False Positives

- Legitimate use of volume shadow copy mounts (backups maybe).

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1003.002/T1003.002.md#atomic-test-3---esentutlexe-sam-copy

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_ntfs/win_system_volume_shadow_copy_mount.yml)
