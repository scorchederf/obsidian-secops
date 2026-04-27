---
sigma_id: "023c654f-8f16-44d9-bb2b-00ff36a62af9"
title: "Python Function Execution Security Warning Disabled In Excel"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_registry_office_disable_python_security_warnings.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_office_disable_python_security_warnings.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "023c654f-8f16-44d9-bb2b-00ff36a62af9"
  - "Python Function Execution Security Warning Disabled In Excel"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Python Function Execution Security Warning Disabled In Excel

Detects changes to the registry value "PythonFunctionWarnings" that would prevent any warnings or alerts from showing when Python functions are about to be executed.
Threat actors could run malicious code through the new Microsoft Excel feature that allows Python to run within the spreadsheet.

## Metadata

- Rule ID: 023c654f-8f16-44d9-bb2b-00ff36a62af9
- Status: test
- Level: high
- Author: @Kostastsale
- Date: 2023-08-22
- Source Path: rules/windows/process_creation/proc_creation_win_registry_office_disable_python_security_warnings.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - \Microsoft\Office\
  - \Excel\Security
  - PythonFunctionWarnings
  CommandLine|contains: ' 0'
condition: selection
```

## False Positives

- Unknown

## References

- https://support.microsoft.com/en-us/office/data-security-and-python-in-excel-33cc88a4-4a87-485e-9ff9-f35958278327

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_office_disable_python_security_warnings.yml)
