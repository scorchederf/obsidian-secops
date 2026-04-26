---
sigma_id: "18beca67-ab3e-4ee3-ba7a-a46ca8d7d0cc"
title: "Sysmon Channel Reference Deletion"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_sysmon_channel_reference_deletion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_sysmon_channel_reference_deletion.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "18beca67-ab3e-4ee3-ba7a-a46ca8d7d0cc"
  - "Sysmon Channel Reference Deletion"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Sysmon Channel Reference Deletion

Potential threat actor tampering with Sysmon manifest and eventually disabling it

## Metadata

- Rule ID: 18beca67-ab3e-4ee3-ba7a-a46ca8d7d0cc
- Status: test
- Level: high
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2020-07-14
- Modified: 2025-10-22
- Source Path: rules/windows/builtin/security/win_security_sysmon_channel_reference_deletion.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection1:
  EventID: 4657
  ObjectName|contains:
  - WINEVT\Publishers\{5770385f-c22a-43e0-bf4c-06f5698ffbd9}
  - WINEVT\Channels\Microsoft-Windows-Sysmon/Operational
  ObjectValueName: Enabled
  NewValue: 0
selection2:
  EventID: 4663
  ObjectName|contains:
  - WINEVT\Publishers\{5770385f-c22a-43e0-bf4c-06f5698ffbd9}
  - WINEVT\Channels\Microsoft-Windows-Sysmon/Operational
  AccessMask: '0x10000'
condition: 1 of selection*
```

## False Positives

- Unknown

## References

- https://twitter.com/Flangvik/status/1283054508084473861
- https://twitter.com/SecurityJosh/status/1283027365770276866
- https://securityjosh.github.io/2020/04/23/Mute-Sysmon.html
- https://gist.github.com/Cyb3rWard0g/cf08c38c61f7e46e8404b38201ca01c8

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_sysmon_channel_reference_deletion.yml)
