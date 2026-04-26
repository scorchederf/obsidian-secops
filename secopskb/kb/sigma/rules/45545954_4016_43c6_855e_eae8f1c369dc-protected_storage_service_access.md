---
sigma_id: "45545954-4016-43c6-855e-eae8f1c369dc"
title: "Protected Storage Service Access"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_protected_storage_service_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_protected_storage_service_access.yml"
build_date: "2026-04-26 15:01:50"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "45545954-4016-43c6-855e-eae8f1c369dc"
  - "Protected Storage Service Access"
attack_technique_ids:
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Protected Storage Service Access

Detects access to a protected_storage service over the network. Potential abuse of DPAPI to extract domain backup keys from Domain Controllers

## Metadata

- Rule ID: 45545954-4016-43c6-855e-eae8f1c369dc
- Status: test
- Level: high
- Author: Roberto Rodriguez @Cyb3rWard0g
- Date: 2019-08-10
- Modified: 2021-11-27
- Source Path: rules/windows/builtin/security/win_security_protected_storage_service_access.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Detection

```yaml
selection:
  EventID: 5145
  ShareName|contains: IPC
  RelativeTargetName: protected_storage
condition: selection
```

## False Positives

- Unknown

## References

- https://threathunterplaybook.com/hunts/windows/190620-DomainDPAPIBackupKeyExtraction/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_protected_storage_service_access.yml)
