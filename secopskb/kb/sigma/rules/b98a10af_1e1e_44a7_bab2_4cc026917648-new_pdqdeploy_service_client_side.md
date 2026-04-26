---
sigma_id: "b98a10af-1e1e-44a7-bab2-4cc026917648"
title: "New PDQDeploy Service - Client Side"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_install_pdqdeploy_runner.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_pdqdeploy_runner.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / system"
aliases:
  - "b98a10af-1e1e-44a7-bab2-4cc026917648"
  - "New PDQDeploy Service - Client Side"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New PDQDeploy Service - Client Side

Detects PDQDeploy service installation on the target system.
When a package is deployed via PDQDeploy it installs a remote service on the target machine with the name "PDQDeployRunner-X" where "X" is an integer starting from 1

## Metadata

- Rule ID: b98a10af-1e1e-44a7-bab2-4cc026917648
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-22
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_service_install_pdqdeploy_runner.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detection

```yaml
selection_root:
  Provider_Name: Service Control Manager
  EventID: 7045
selection_service:
- ImagePath|contains: PDQDeployRunner-
- ServiceName|startswith: PDQDeployRunner-
condition: all of selection_*
```

## False Positives

- Legitimate use of the tool

## References

- https://documentation.pdq.com/PDQDeploy/13.0.3.0/index.html?windows-services.htm

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_pdqdeploy_runner.yml)
