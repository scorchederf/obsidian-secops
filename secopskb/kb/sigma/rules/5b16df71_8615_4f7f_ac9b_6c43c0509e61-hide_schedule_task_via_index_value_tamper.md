---
sigma_id: "5b16df71-8615-4f7f-ac9b-6c43c0509e61"
title: "Hide Schedule Task Via Index Value Tamper"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_hide_scheduled_task_via_index_tamper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_hide_scheduled_task_via_index_tamper.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "5b16df71-8615-4f7f-ac9b-6c43c0509e61"
  - "Hide Schedule Task Via Index Value Tamper"
attack_technique_ids:
  - "T1562"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Hide Schedule Task Via Index Value Tamper

Detects when the "index" value of a scheduled task is modified from the registry
Which effectively hides it from any tooling such as "schtasks /query" (Read the referenced link for more information about the effects of this technique)

## Metadata

- Rule ID: 5b16df71-8615-4f7f-ac9b-6c43c0509e61
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-26
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_hide_scheduled_task_via_index_tamper.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562]]

## Detection

```yaml
selection:
  TargetObject|contains|all:
  - \SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree\
  - Index
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Unlikely

## References

- https://blog.qualys.com/vulnerabilities-threat-research/2022/06/20/defending-against-scheduled-task-attacks-in-windows-environments

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_hide_scheduled_task_via_index_tamper.yml)
