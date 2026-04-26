---
sigma_id: "c8b00925-926c-47e3-beea-298fd563728e"
title: "Remote Access Tool Services Have Been Installed - Security"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_service_install_remote_access_software.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_service_install_remote_access_software.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "c8b00925-926c-47e3-beea-298fd563728e"
  - "Remote Access Tool Services Have Been Installed - Security"
attack_technique_ids:
  - "T1543.003"
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool Services Have Been Installed - Security

Detects service installation of different remote access tools software. These software are often abused by threat actors to perform

## Metadata

- Rule ID: c8b00925-926c-47e3-beea-298fd563728e
- Status: test
- Level: medium
- Author: Connor Martin, Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-12-23
- Modified: 2024-12-07
- Source Path: rules/windows/builtin/security/win_security_service_install_remote_access_software.yml

## Logsource

- definition: The 'System Security Extension' audit subcategory need to be enabled to log the EID 4697
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]
- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Detection

```yaml
selection:
  EventID: 4697
  ServiceName|contains:
  - AmmyyAdmin
  - AnyDesk
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

- The rule doesn't look for anything suspicious so false positives are expected. If you use one of the tools mentioned, comment it out

## References

- https://redcanary.com/blog/misbehaving-rats/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_service_install_remote_access_software.yml)
