---
sigma_id: "17e53739-a1fc-4a62-b1b9-87711c2d5e44"
title: "Python Function Execution Security Warning Disabled In Excel - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_office_disable_python_security_warnings.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_disable_python_security_warnings.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "17e53739-a1fc-4a62-b1b9-87711c2d5e44"
  - "Python Function Execution Security Warning Disabled In Excel - Registry"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Python Function Execution Security Warning Disabled In Excel - Registry

Detects changes to the registry value "PythonFunctionWarnings" that would prevent any warnings or alerts from showing when Python functions are about to be executed.
Threat actors could run malicious code through the new Microsoft Excel feature that allows Python to run within the spreadsheet.

## Metadata

- Rule ID: 17e53739-a1fc-4a62-b1b9-87711c2d5e44
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), @Kostastsale
- Date: 2024-08-23
- Source Path: rules/windows/registry/registry_set/registry_set_office_disable_python_security_warnings.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  TargetObject|contains: \Microsoft\Office\
  TargetObject|endswith: \Excel\Security\PythonFunctionWarnings
  Details: DWORD (0x00000001)
condition: selection
```

## False Positives

- Unknown

## References

- https://support.microsoft.com/en-us/office/data-security-and-python-in-excel-33cc88a4-4a87-485e-9ff9-f35958278327

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_disable_python_security_warnings.yml)
