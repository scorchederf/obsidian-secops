---
sigma_id: "71c276aa-49cd-43d2-b920-2dcd3e6962d5"
title: "Service Installed By Unusual Client - System"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_install_sups_unusal_client.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_sups_unusal_client.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "71c276aa-49cd-43d2-b920-2dcd3e6962d5"
  - "Service Installed By Unusual Client - System"
attack_technique_ids:
  - "T1543"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Service Installed By Unusual Client - System

Detects a service installed by a client which has PID 0 or whose parent has PID 0

## Metadata

- Rule ID: 71c276aa-49cd-43d2-b920-2dcd3e6962d5
- Status: test
- Level: high
- Author: Tim Rauch (Nextron Systems), Elastic (idea)
- Date: 2022-09-15
- Modified: 2023-01-04
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_service_install_sups_unusal_client.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543]]

## Detection

```yaml
selection:
  Provider_Name: Service Control Manager
  EventID: 7045
  ProcessId: 0
condition: selection
```

## False Positives

- Unknown

## References

- https://www.elastic.co/guide/en/security/current/windows-service-installed-via-an-unusual-client.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_sups_unusal_client.yml)
