---
sigma_id: "8e4cf0e5-aa5d-4dc3-beff-dc26917744a9"
title: "Tap Driver Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_install_tap_driver.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_tap_driver.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / system"
aliases:
  - "8e4cf0e5-aa5d-4dc3-beff-dc26917744a9"
  - "Tap Driver Installation"
attack_technique_ids:
  - "T1048"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Tap Driver Installation

Well-known TAP software installation. Possible preparation for data exfiltration using tunnelling techniques

## Metadata

- Rule ID: 8e4cf0e5-aa5d-4dc3-beff-dc26917744a9
- Status: test
- Level: medium
- Author: Daniil Yugoslavskiy, Ian Davis, oscd.community
- Date: 2019-10-24
- Modified: 2022-12-25
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_service_install_tap_driver.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048]]

## Detection

```yaml
selection:
  Provider_Name: Service Control Manager
  EventID: 7045
  ImagePath|contains: tap0901
condition: selection
```

## False Positives

- Legitimate OpenVPN TAP installation

## References

- https://community.openvpn.net/openvpn/wiki/ManagingWindowsTAPDrivers

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_tap_driver.yml)
