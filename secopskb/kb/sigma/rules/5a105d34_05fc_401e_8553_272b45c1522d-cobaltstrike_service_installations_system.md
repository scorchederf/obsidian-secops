---
sigma_id: "5a105d34-05fc-401e-8553-272b45c1522d"
title: "CobaltStrike Service Installations - System"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_cobaltstrike_service_installs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_cobaltstrike_service_installs.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "critical"
logsource: "windows / system"
aliases:
  - "5a105d34-05fc-401e-8553-272b45c1522d"
  - "CobaltStrike Service Installations - System"
attack_technique_ids:
  - "T1021.002"
  - "T1543.003"
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CobaltStrike Service Installations - System

Detects known malicious service installs that appear in cases in which a Cobalt Strike beacon elevates privileges or lateral movement

## Metadata

- Rule ID: 5a105d34-05fc-401e-8553-272b45c1522d
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems), Wojciech Lesicki
- Date: 2021-05-26
- Modified: 2022-11-27
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_cobaltstrike_service_installs.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]
- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]
- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Detection

```yaml
selection_id:
  Provider_Name: Service Control Manager
  EventID: 7045
selection1:
  ImagePath|contains|all:
  - ADMIN$
  - .exe
selection2:
  ImagePath|contains|all:
  - '%COMSPEC%'
  - start
  - powershell
selection3:
  ImagePath|contains: powershell -nop -w hidden -encodedcommand
selection4:
  ImagePath|base64offset|contains: 'IEX (New-Object Net.Webclient).DownloadString(''http://127.0.0.1:'
condition: selection_id and (selection1 or selection2 or selection3 or selection4)
```

## False Positives

- Unknown

## References

- https://www.sans.org/webcasts/119395
- https://www.crowdstrike.com/blog/getting-the-bacon-from-cobalt-strike-beacon/
- https://thedfirreport.com/2021/08/29/cobalt-strike-a-defenders-guide/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_cobaltstrike_service_installs.yml)
