---
sigma_id: "ecbc5e16-58e0-4521-9c60-eb9a7ea4ad34"
title: "Meterpreter or Cobalt Strike Getsystem Service Installation - Security"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_meterpreter_or_cobaltstrike_getsystem_service_install.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_meterpreter_or_cobaltstrike_getsystem_service_install.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "ecbc5e16-58e0-4521-9c60-eb9a7ea4ad34"
  - "Meterpreter or Cobalt Strike Getsystem Service Installation - Security"
attack_technique_ids:
  - "T1134.001"
  - "T1134.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Meterpreter or Cobalt Strike Getsystem Service Installation - Security

Detects the use of getsystem Meterpreter/Cobalt Strike command by detecting a specific service installation

## Metadata

- Rule ID: ecbc5e16-58e0-4521-9c60-eb9a7ea4ad34
- Status: test
- Level: high
- Author: Teymur Kheirkhabarov, Ecco, Florian Roth (Nextron Systems)
- Date: 2019-10-26
- Modified: 2023-11-15
- Source Path: rules/windows/builtin/security/win_security_meterpreter_or_cobaltstrike_getsystem_service_install.yml

## Logsource

- definition: The 'System Security Extension' audit subcategory need to be enabled to log the EID 4697
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.001]]
- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.002]]

## Detection

```yaml
selection_eid:
  EventID: 4697
selection_cli_cmd:
  ServiceFileName|contains|all:
  - /c
  - echo
  - \pipe\
  ServiceFileName|contains:
  - cmd
  - '%COMSPEC%'
selection_cli_rundll:
  ServiceFileName|contains|all:
  - rundll32
  - .dll,a
  - '/p:'
selection_cli_share:
  ServiceFileName|startswith: \\\\127.0.0.1\\ADMIN$\
condition: selection_eid and 1 of selection_cli_*
```

## False Positives

- Unlikely

## References

- https://speakerdeck.com/heirhabarov/hunting-for-privilege-escalation-in-windows-environment
- https://blog.cobaltstrike.com/2014/04/02/what-happens-when-i-type-getsystem/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_meterpreter_or_cobaltstrike_getsystem_service_install.yml)
