---
sigma_id: "e9faba72-4974-4ab2-a4c5-46e25ad59e9b"
title: "VSSAudit Security Event Source Registration"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_vssaudit_secevent_source_registration.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_vssaudit_secevent_source_registration.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "informational"
logsource: "windows / security"
aliases:
  - "e9faba72-4974-4ab2-a4c5-46e25ad59e9b"
  - "VSSAudit Security Event Source Registration"
attack_technique_ids:
  - "T1003.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# VSSAudit Security Event Source Registration

Detects the registration of the security event source VSSAudit. It would usually trigger when volume shadow copy operations happen.

## Metadata

- Rule ID: e9faba72-4974-4ab2-a4c5-46e25ad59e9b
- Status: test
- Level: informational
- Author: Roberto Rodriguez @Cyb3rWard0g, Open Threat Research (OTR)
- Date: 2020-10-20
- Modified: 2022-04-28
- Source Path: rules/windows/builtin/security/win_security_vssaudit_secevent_source_registration.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]

## Detection

```yaml
selection:
  AuditSourceName: VSSAudit
  EventID:
  - 4904
  - 4905
condition: selection
```

## False Positives

- Legitimate use of VSSVC. Maybe backup operations. It would usually be done by C:\Windows\System32\VSSVC.exe.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1003.002/T1003.002.md#atomic-test-3---esentutlexe-sam-copy

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_vssaudit_secevent_source_registration.yml)
