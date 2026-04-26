---
sigma_id: "ee9ca27c-9bd7-4cee-9b01-6e906be7cae3"
title: "New PDQDeploy Service - Server Side"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_install_pdqdeploy.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_pdqdeploy.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / system"
aliases:
  - "ee9ca27c-9bd7-4cee-9b01-6e906be7cae3"
  - "New PDQDeploy Service - Server Side"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New PDQDeploy Service - Server Side

Detects a PDQDeploy service installation which indicates that PDQDeploy was installed on the machines.
PDQDeploy can be abused by attackers to remotely install packages or execute commands on target machines

## Metadata

- Rule ID: ee9ca27c-9bd7-4cee-9b01-6e906be7cae3
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-22
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_service_install_pdqdeploy.yml

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
- ImagePath|contains: PDQDeployService.exe
- ServiceName:
  - PDQDeploy
  - PDQ Deploy
condition: all of selection_*
```

## False Positives

- Legitimate use of the tool

## References

- https://documentation.pdq.com/PDQDeploy/13.0.3.0/index.html?windows-services.htm

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_pdqdeploy.yml)
