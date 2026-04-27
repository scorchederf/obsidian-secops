---
sigma_id: "9a4ff3b8-6187-4fd2-8e8b-e0eae1129495"
title: "SysKey Registry Keys Access"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_syskey_registry_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_syskey_registry_access.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "9a4ff3b8-6187-4fd2-8e8b-e0eae1129495"
  - "SysKey Registry Keys Access"
attack_technique_ids:
  - "T1012"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects handle requests and access operations to specific registry keys to calculate the SysKey

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1012-query_registry|T1012: Query Registry]]

## Detection

```yaml
selection:
  EventID:
  - 4656
  - 4663
  ObjectType: key
  ObjectName|endswith:
  - lsa\JD
  - lsa\GBG
  - lsa\Skew1
  - lsa\Data
condition: selection
```

## False Positives

- Unknown

## References

- https://threathunterplaybook.com/hunts/windows/190625-RegKeyAccessSyskey/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_syskey_registry_access.yml)
