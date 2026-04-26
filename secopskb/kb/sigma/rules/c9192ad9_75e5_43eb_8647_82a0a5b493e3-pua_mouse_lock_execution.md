---
sigma_id: "c9192ad9-75e5-43eb-8647-82a0a5b493e3"
title: "PUA - Mouse Lock Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_mouselock_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_mouselock_execution.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c9192ad9-75e5-43eb-8647-82a0a5b493e3"
  - "PUA - Mouse Lock Execution"
attack_technique_ids:
  - "T1056.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - Mouse Lock Execution

In Kaspersky's 2020 Incident Response Analyst Report they listed legitimate tool "Mouse Lock" as being used for both credential access and collection in security incidents.

## Metadata

- Rule ID: c9192ad9-75e5-43eb-8647-82a0a5b493e3
- Status: test
- Level: medium
- Author: Cian Heasley
- Date: 2020-08-13
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_pua_mouselock_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1056-input_capture|T1056.002]]

## Detection

```yaml
selection:
- Product|contains: Mouse Lock
- Company|contains: Misc314
- CommandLine|contains: Mouse Lock_
condition: selection
```

## False Positives

- Legitimate uses of Mouse Lock software

## References

- https://github.com/klsecservices/Publications/blob/657deb6a6eb6e00669afd40173f425fb49682eaa/Incident-Response-Analyst-Report-2020.pdf
- https://sourceforge.net/projects/mouselock/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_mouselock_execution.yml)
