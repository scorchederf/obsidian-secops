---
sigma_id: "1a31b18a-f00c-4061-9900-f735b96c99fc"
title: "Remote Access Tool Services Have Been Installed - System"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_install_remote_access_software.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_remote_access_software.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / system"
aliases:
  - "1a31b18a-f00c-4061-9900-f735b96c99fc"
  - "Remote Access Tool Services Have Been Installed - System"
attack_technique_ids:
  - "T1543.003"
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool Services Have Been Installed - System

Detects service installation of different remote access tools software. These software are often abused by threat actors to perform

## Metadata

- Rule ID: 1a31b18a-f00c-4061-9900-f735b96c99fc
- Status: test
- Level: medium
- Author: Connor Martin, Nasreddine Bencherchali
- Date: 2022-12-23
- Modified: 2023-06-22
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_service_install_remote_access_software.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]
- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Detection

```yaml
selection:
  Provider_Name: Service Control Manager
  EventID:
  - 7045
  - 7036
  ServiceName|contains:
  - AmmyyAdmin
  - Atera
  - BASupportExpressSrvcUpdater
  - BASupportExpressStandaloneService
  - chromoting
  - GoToAssist
  - GoToMyPC
  - jumpcloud
  - LMIGuardianSvc
  - LogMeIn
  - monblanking
  - Parsec
  - RManService
  - RPCPerformanceService
  - RPCService
  - SplashtopRemoteService
  - SSUService
  - TeamViewer
  - TightVNC
  - vncserver
  - Zoho
condition: selection
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/misbehaving-rats/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_remote_access_software.yml)
