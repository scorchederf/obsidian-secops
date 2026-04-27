---
sigma_id: "966315ef-c5e1-4767-ba25-fce9c8de3660"
title: "Suspicious Environment Variable Has Been Registered"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_suspicious_env_variables.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_suspicious_env_variables.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "966315ef-c5e1-4767-ba25-fce9c8de3660"
  - "Suspicious Environment Variable Has Been Registered"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the creation of user-specific or system-wide environment variables via the registry. Which contains suspicious commands and strings

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection_main:
  TargetObject|contains: \Environment\
selection_details:
- Details:
  - powershell
  - pwsh
- Details|contains:
  - \AppData\Local\Temp\
  - C:\Users\Public\
  - TVqQAAMAAAAEAAAA
  - TVpQAAIAAAAEAA8A
  - TVqAAAEAAAAEABAA
  - TVoAAAAAAAAAAAAA
  - TVpTAQEAAAAEAAAA
  - SW52b2tlL
  - ludm9rZS
  - JbnZva2Ut
  - SQBuAHYAbwBrAGUALQ
  - kAbgB2AG8AawBlAC0A
  - JAG4AdgBvAGsAZQAtA
- Details|startswith:
  - SUVY
  - SQBFAF
  - SQBuAH
  - cwBhA
  - aWV4
  - aQBlA
  - R2V0
  - dmFy
  - dgBhA
  - dXNpbm
  - H4sIA
  - Y21k
  - cABhAH
  - Qzpc
  - Yzpc
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://infosec.exchange/@sbousseaden/109542254124022664

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_suspicious_env_variables.yml)
