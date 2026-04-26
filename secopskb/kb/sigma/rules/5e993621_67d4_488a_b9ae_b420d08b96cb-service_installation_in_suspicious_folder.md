---
sigma_id: "5e993621-67d4-488a-b9ae-b420d08b96cb"
title: "Service Installation in Suspicious Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_susp_service_installation_folder.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_susp_service_installation_folder.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / system"
aliases:
  - "5e993621-67d4-488a-b9ae-b420d08b96cb"
  - "Service Installation in Suspicious Folder"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Service Installation in Suspicious Folder

Detects service installation in suspicious folder appdata

## Metadata

- Rule ID: 5e993621-67d4-488a-b9ae-b420d08b96cb
- Status: test
- Level: medium
- Author: pH-T (Nextron Systems)
- Date: 2022-03-18
- Modified: 2024-01-18
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_susp_service_installation_folder.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detection

```yaml
selection:
  Provider_Name: Service Control Manager
  EventID: 7045
  ImagePath|contains:
  - \AppData\
  - \\\\127.0.0.1
  - \\\\localhost
filter_optional_zoom:
  ServiceName: Zoom Sharing Service
  ImagePath|contains: :\Program Files\Common Files\Zoom\Support\CptService.exe
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_susp_service_installation_folder.yml)
