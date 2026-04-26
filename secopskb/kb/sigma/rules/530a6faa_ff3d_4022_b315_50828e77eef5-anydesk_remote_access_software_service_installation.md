---
sigma_id: "530a6faa-ff3d-4022-b315-50828e77eef5"
title: "Anydesk Remote Access Software Service Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_install_anydesk.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_anydesk.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / system"
aliases:
  - "530a6faa-ff3d-4022-b315-50828e77eef5"
  - "Anydesk Remote Access Software Service Installation"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Anydesk Remote Access Software Service Installation

Detects the installation of the anydesk software service. Which could be an indication of anydesk abuse if you the software isn't already used.

## Metadata

- Rule ID: 530a6faa-ff3d-4022-b315-50828e77eef5
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2022-08-11
- Modified: 2025-02-24
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_service_install_anydesk.yml

## Logsource

- product: windows
- service: system

## Detection

```yaml
selection_provider:
  Provider_Name: Service Control Manager
  EventID: 7045
selection_service:
- ServiceName|contains|all:
  - AnyDesk
  - Service
- ImagePath|contains: AnyDesk
condition: all of selection_*
```

## False Positives

- Legitimate usage of the anydesk tool

## References

- https://thedfirreport.com/2022/08/08/bumblebee-roasts-its-way-to-domain-admin/
- https://thedfirreport.com/2025/02/24/confluence-exploit-leads-to-lockbit-ransomware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_anydesk.yml)
