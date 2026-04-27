---
sigma_id: "4a5f5a5e-ac01-474b-9b4e-d61298c9df1d"
title: "PowerShell as a Service in Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_powershell_as_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_powershell_as_service.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "4a5f5a5e-ac01-474b-9b4e-d61298c9df1d"
  - "PowerShell as a Service in Registry"
attack_technique_ids:
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects that a powershell code is written to the registry as a service.

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]

## Detection

```yaml
selection:
  TargetObject|contains: \Services\
  TargetObject|endswith: \ImagePath
  Details|contains:
  - powershell
  - pwsh
condition: selection
```

## False Positives

- Unknown

## References

- https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_powershell_as_service.yml)
