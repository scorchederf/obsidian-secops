---
sigma_id: "acd74772-5f88-45c7-956b-6a7b36c294d2"
title: "Removal Of SD Value to Hide Schedule Task - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_delete/registry_delete_schtasks_hide_task_via_sd_value_removal.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_delete/registry_delete_schtasks_hide_task_via_sd_value_removal.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / registry_delete"
aliases:
  - "acd74772-5f88-45c7-956b-6a7b36c294d2"
  - "Removal Of SD Value to Hide Schedule Task - Registry"
attack_technique_ids:
  - "T1562"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Removal Of SD Value to Hide Schedule Task - Registry

Remove SD (Security Descriptor) value in \Schedule\TaskCache\Tree registry hive to hide schedule task. This technique is used by Tarrask malware

## Metadata

- Rule ID: acd74772-5f88-45c7-956b-6a7b36c294d2
- Status: test
- Level: medium
- Author: Sittikorn S
- Date: 2022-04-15
- Modified: 2025-10-25
- Source Path: rules/windows/registry/registry_delete/registry_delete_schtasks_hide_task_via_sd_value_removal.yml

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
  - SD
condition: selection
```

## False Positives

- Unknown

## References

- https://www.microsoft.com/security/blog/2022/04/12/tarrask-malware-uses-scheduled-tasks-for-defense-evasion/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_delete/registry_delete_schtasks_hide_task_via_sd_value_removal.yml)
