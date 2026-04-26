---
sigma_id: "85cce894-dd8b-4427-a958-5cc47a4dc9b9"
title: "Remote Utilities Host Service Install"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_install_remote_utilities.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_remote_utilities.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / system"
aliases:
  - "85cce894-dd8b-4427-a958-5cc47a4dc9b9"
  - "Remote Utilities Host Service Install"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Utilities Host Service Install

Detects Remote Utilities Host service installation on the target system.

## Metadata

- Rule ID: 85cce894-dd8b-4427-a958-5cc47a4dc9b9
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-31
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_service_install_remote_utilities.yml

## Logsource

- product: windows
- service: system

## Detection

```yaml
selection_root:
  Provider_Name: Service Control Manager
  EventID: 7045
selection_service:
- ImagePath|contains|all:
  - \rutserv.exe
  - -service
- ServiceName: Remote Utilities - Host
condition: all of selection_*
```

## False Positives

- Legitimate use of the tool

## References

- https://www.remoteutilities.com/support/kb/host-service-won-t-start/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_remote_utilities.yml)
