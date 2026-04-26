---
sigma_id: "d6b5520d-3934-48b4-928c-2aa3f92d6963"
title: "Important Windows Service Terminated With Error"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_terminated_error_important.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_terminated_error_important.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "d6b5520d-3934-48b4-928c-2aa3f92d6963"
  - "Important Windows Service Terminated With Error"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Important Windows Service Terminated With Error

Detects important or interesting Windows services that got terminated for whatever reason

## Metadata

- Rule ID: d6b5520d-3934-48b4-928c-2aa3f92d6963
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-04-14
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_service_terminated_error_important.yml

## Logsource

- product: windows
- service: system

## Detection

```yaml
selection_eid:
  Provider_Name: Service Control Manager
  EventID: 7023
selection_name:
- param1|contains:
  - ' Antivirus'
  - ' Firewall'
  - Application Guard
  - BitLocker Drive Encryption Service
  - Encrypting File System
  - Microsoft Defender
  - Threat Protection
  - Windows Event Log
- Binary|contains:
  - 770069006e0064006500660065006e006400
  - 4500760065006e0074004c006f006700
  - 6d0070007300730076006300
  - 530065006e0073006500
  - '450046005300'
  - '420044004500530056004300'
condition: all of selection_*
```

## False Positives

- Rare false positives could occur since service termination could happen due to multiple reasons

## References

- https://www.microsoft.com/en-us/security/blog/2023/04/11/guidance-for-investigating-attacks-using-cve-2022-21894-the-blacklotus-campaign/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_terminated_error_important.yml)
