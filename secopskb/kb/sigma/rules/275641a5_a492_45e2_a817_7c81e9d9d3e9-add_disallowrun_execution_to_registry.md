---
sigma_id: "275641a5-a492-45e2-a817-7c81e9d9d3e9"
title: "Add DisallowRun Execution to Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_disallowrun_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disallowrun_execution.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "275641a5-a492-45e2-a817-7c81e9d9d3e9"
  - "Add DisallowRun Execution to Registry"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Add DisallowRun Execution to Registry

Detect set DisallowRun to 1 to prevent user running specific computer program

## Metadata

- Rule ID: 275641a5-a492-45e2-a817-7c81e9d9d3e9
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-08-19
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_disallowrun_execution.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|endswith: Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun
  Details: DWORD (0x00000001)
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/40b77d63808dd4f4eafb83949805636735a1fd15/atomics/T1112/T1112.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disallowrun_execution.yml)
