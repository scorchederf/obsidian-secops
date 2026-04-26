---
sigma_id: "f8748f2c-89dc-4d95-afb0-5a2dfdbad332"
title: "SAM Registry Hive Handle Request"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_sam_registry_hive_handle_request.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_sam_registry_hive_handle_request.yml"
build_date: "2026-04-26 17:03:22"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# SAM Registry Hive Handle Request

Detects handles requested to SAM registry hive

## Metadata

- Rule ID: f8748f2c-89dc-4d95-afb0-5a2dfdbad332
- Status: test
- Level: high
- Author: Roberto Rodriguez @Cyb3rWard0g
- Date: 2019-08-12
- Modified: 2021-11-27
- Source Path: rules/windows/builtin/security/win_security_sam_registry_hive_handle_request.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1012-query_registry|T1012]]
- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.002]]

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
