---
sigma_id: "f8748f2c-89dc-4d95-afb0-5a2dfdbad332"
title: "SAM Registry Hive Handle Request"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_sam_registry_hive_handle_request.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_sam_registry_hive_handle_request.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "f8748f2c-89dc-4d95-afb0-5a2dfdbad332"
  - "SAM Registry Hive Handle Request"
attack_technique_ids:
  - "T1012"
  - "T1552.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects handles requested to SAM registry hive

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1012-query_registry|T1012: Query Registry]]
- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552002-credentials-in-registry|T1552.002: Credentials in Registry]]

## Detection

```yaml
selection:
  EventID: 4656
  ObjectType: Key
  ObjectName|endswith: \SAM
condition: selection
```

## False Positives

- Unknown

## References

- https://threathunterplaybook.com/hunts/windows/190725-SAMRegistryHiveHandleRequest/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_sam_registry_hive_handle_request.yml)
