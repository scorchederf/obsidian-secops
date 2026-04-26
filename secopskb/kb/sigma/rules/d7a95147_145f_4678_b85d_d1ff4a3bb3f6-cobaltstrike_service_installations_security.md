---
sigma_id: "d7a95147-145f-4678-b85d-d1ff4a3bb3f6"
title: "CobaltStrike Service Installations - Security"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_cobaltstrike_service_installs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_cobaltstrike_service_installs.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "d7a95147-145f-4678-b85d-d1ff4a3bb3f6"
  - "CobaltStrike Service Installations - Security"
attack_technique_ids:
  - "T1021.002"
  - "T1543.003"
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CobaltStrike Service Installations - Security

Detects known malicious service installs that appear in cases in which a Cobalt Strike beacon elevates privileges or lateral movement

## Metadata

- Rule ID: d7a95147-145f-4678-b85d-d1ff4a3bb3f6
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Wojciech Lesicki
- Date: 2021-05-26
- Modified: 2022-11-27
- Source Path: rules/windows/builtin/security/win_security_cobaltstrike_service_installs.yml

## Logsource

- definition: The 'System Security Extension' audit subcategory need to be enabled to log the EID 4697
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]
- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]
- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Detection

```yaml
event_id:
  EventID: 4697
selection1:
  ServiceFileName|contains|all:
  - ADMIN$
  - .exe
selection2:
  ServiceFileName|contains|all:
  - '%COMSPEC%'
  - start
  - powershell
selection3:
  ServiceFileName|contains: powershell -nop -w hidden -encodedcommand
selection4:
  ServiceFileName|base64offset|contains: 'IEX (New-Object Net.Webclient).DownloadString(''http://127.0.0.1:'
condition: event_id and 1 of selection*
```

## False Positives

- Unknown

## References

- https://www.sans.org/webcasts/119395
- https://www.crowdstrike.com/blog/getting-the-bacon-from-cobalt-strike-beacon/
- https://thedfirreport.com/2021/08/29/cobalt-strike-a-defenders-guide/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_cobaltstrike_service_installs.yml)
