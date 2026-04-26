---
sigma_id: "1b2ae822-6fe1-43ba-aa7c-d1a3b3d1d5f2"
title: "Service Installation with Suspicious Folder Pattern"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_susp_service_installation_folder_pattern.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_susp_service_installation_folder_pattern.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "1b2ae822-6fe1-43ba-aa7c-d1a3b3d1d5f2"
  - "Service Installation with Suspicious Folder Pattern"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Service Installation with Suspicious Folder Pattern

Detects service installation with suspicious folder patterns

## Metadata

- Rule ID: 1b2ae822-6fe1-43ba-aa7c-d1a3b3d1d5f2
- Status: test
- Level: high
- Author: pH-T (Nextron Systems)
- Date: 2022-03-18
- Modified: 2022-03-24
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_susp_service_installation_folder_pattern.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detection

```yaml
selection_eid:
  Provider_Name: Service Control Manager
  EventID: 7045
selection_img_paths:
- ImagePath|re: ^[Cc]:\\[Pp]rogram[Dd]ata\\.{1,9}\.exe
- ImagePath|re: ^[Cc]:\\.{1,9}\.exe
condition: all of selection_*
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_susp_service_installation_folder_pattern.yml)
