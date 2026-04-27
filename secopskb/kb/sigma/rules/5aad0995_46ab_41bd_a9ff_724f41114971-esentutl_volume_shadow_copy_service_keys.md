---
sigma_id: "5aad0995-46ab-41bd-a9ff-724f41114971"
title: "Esentutl Volume Shadow Copy Service Keys"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_esentutl_volume_shadow_copy_service_keys.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_esentutl_volume_shadow_copy_service_keys.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / registry_event"
aliases:
  - "5aad0995-46ab-41bd-a9ff-724f41114971"
  - "Esentutl Volume Shadow Copy Service Keys"
attack_technique_ids:
  - "T1003.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the volume shadow copy service initialization and processing via esentutl. Registry keys such as HKLM\\System\\CurrentControlSet\\Services\\VSS\\Diag\\VolSnap\\Volume are captured.

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]

## Detection

```yaml
selection:
  TargetObject|contains: System\CurrentControlSet\Services\VSS
  Image|endswith: esentutl.exe
filter:
  TargetObject|contains: System\CurrentControlSet\Services\VSS\Start
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1003.002/T1003.002.md#atomic-test-3---esentutlexe-sam-copy

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_esentutl_volume_shadow_copy_service_keys.yml)
