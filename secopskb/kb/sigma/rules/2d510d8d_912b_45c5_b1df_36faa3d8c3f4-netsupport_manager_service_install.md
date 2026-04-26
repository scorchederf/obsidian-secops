---
sigma_id: "2d510d8d-912b-45c5-b1df-36faa3d8c3f4"
title: "NetSupport Manager Service Install"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_install_netsupport_manager.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_netsupport_manager.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / system"
aliases:
  - "2d510d8d-912b-45c5-b1df-36faa3d8c3f4"
  - "NetSupport Manager Service Install"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# NetSupport Manager Service Install

Detects NetSupport Manager service installation on the target system.

## Metadata

- Rule ID: 2d510d8d-912b-45c5-b1df-36faa3d8c3f4
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-31
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_service_install_netsupport_manager.yml

## Logsource

- product: windows
- service: system

## Detection

```yaml
selection_root:
  Provider_Name: Service Control Manager
  EventID: 7045
selection_service:
- ImagePath|contains: \NetSupport Manager\client32.exe
- ServiceName: Client32
condition: all of selection_*
```

## False Positives

- Legitimate use of the tool

## References

- http://resources.netsupportsoftware.com/resources/manualpdfs/nsm_manual_uk.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_netsupport_manager.yml)
