---
sigma_id: "526cc8bc-1cdc-48ad-8b26-f19bff969cec"
title: "Removal Of Index Value to Hide Schedule Task - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_delete/registry_delete_schtasks_hide_task_via_index_value_removal.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_delete/registry_delete_schtasks_hide_task_via_index_value_removal.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / registry_delete"
aliases:
  - "526cc8bc-1cdc-48ad-8b26-f19bff969cec"
  - "Removal Of Index Value to Hide Schedule Task - Registry"
attack_technique_ids:
  - "T1562"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Removal Of Index Value to Hide Schedule Task - Registry

Detects when the "index" value of a scheduled task is removed or deleted from the registry. Which effectively hides it from any tooling such as "schtasks /query"

## Metadata

- Rule ID: 526cc8bc-1cdc-48ad-8b26-f19bff969cec
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-26
- Modified: 2025-10-25
- Source Path: rules/windows/registry/registry_delete/registry_delete_schtasks_hide_task_via_index_value_removal.yml

## Logsource

- category: registry_delete
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
condition: selection
```

## False Positives

- Unknown

## References

- https://blog.qualys.com/vulnerabilities-threat-research/2022/06/20/defending-against-scheduled-task-attacks-in-windows-environments

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_delete/registry_delete_schtasks_hide_task_via_index_value_removal.yml)
