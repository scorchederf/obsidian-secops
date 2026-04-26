---
sigma_id: "843544a7-56e0-4dcc-a44f-5cc266dd97d6"
title: "Meterpreter or Cobalt Strike Getsystem Service Installation - System"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_meterpreter_or_cobaltstrike_getsystem_service_installation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_meterpreter_or_cobaltstrike_getsystem_service_installation.yml"
build_date: "2026-04-26 15:01:46"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "843544a7-56e0-4dcc-a44f-5cc266dd97d6"
  - "Meterpreter or Cobalt Strike Getsystem Service Installation - System"
attack_technique_ids:
  - "T1134.001"
  - "T1134.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Meterpreter or Cobalt Strike Getsystem Service Installation - System

Detects the use of getsystem Meterpreter/Cobalt Strike command by detecting a specific service installation

## Metadata

- Rule ID: 843544a7-56e0-4dcc-a44f-5cc266dd97d6
- Status: test
- Level: high
- Author: Teymur Kheirkhabarov, Ecco, Florian Roth (Nextron Systems)
- Date: 2019-10-26
- Modified: 2023-11-15
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_meterpreter_or_cobaltstrike_getsystem_service_installation.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.001]]
- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.002]]

## Detection

```yaml
selection_id:
  Provider_Name: Service Control Manager
  EventID: 7045
selection_cli_cmd:
  ImagePath|contains|all:
  - /c
  - echo
  - \pipe\
  ImagePath|contains:
  - cmd
  - '%COMSPEC%'
selection_cli_rundll:
  ImagePath|contains|all:
  - rundll32
  - .dll,a
  - '/p:'
selection_cli_share:
  ImagePath|startswith: \\\\127.0.0.1\\ADMIN$\
condition: selection_id and 1 of selection_cli_*
```

## False Positives

- Unlikely

## References

- https://speakerdeck.com/heirhabarov/hunting-for-privilege-escalation-in-windows-environment
- https://blog.cobaltstrike.com/2014/04/02/what-happens-when-i-type-getsystem/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_meterpreter_or_cobaltstrike_getsystem_service_installation.yml)
