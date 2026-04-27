---
sigma_id: "e3fdf743-f05b-4051-990a-b66919be1743"
title: "Change User Account Associated with the FAX Service"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_fax_change_service_user.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_fax_change_service_user.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "e3fdf743-f05b-4051-990a-b66919be1743"
  - "Change User Account Associated with the FAX Service"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detect change of the user account associated with the FAX service to avoid the escalation problem.

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Detection

```yaml
selection:
  TargetObject: HKLM\System\CurrentControlSet\Services\Fax\ObjectName
filter:
  Details|contains: NetworkService
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://twitter.com/dottor_morte/status/1544652325570191361
- https://raw.githubusercontent.com/RiccardoAncarani/talks/master/F-Secure/unorthodox-lateral-movement.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_fax_change_service_user.yml)
