---
sigma_id: "dcf2db1f-f091-425b-a821-c05875b8925a"
title: "Invoke-Obfuscation VAR+ Launcher - Security"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_invoke_obfuscation_var_services_security.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_invoke_obfuscation_var_services_security.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "dcf2db1f-f091-425b-a821-c05875b8925a"
  - "Invoke-Obfuscation VAR+ Launcher - Security"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation VAR+ Launcher - Security

Detects Obfuscated use of Environment Variables to execute PowerShell

## Metadata

- Rule ID: dcf2db1f-f091-425b-a821-c05875b8925a
- Status: test
- Level: high
- Author: Jonathan Cheong, oscd.community
- Date: 2020-10-15
- Modified: 2022-11-29
- Source Path: rules/windows/builtin/security/win_security_invoke_obfuscation_var_services_security.yml

## Logsource

- definition: The 'System Security Extension' audit subcategory need to be enabled to log the EID 4697
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  EventID: 4697
  ServiceFileName|contains|all:
  - cmd
  - '"set'
  - -f
  ServiceFileName|contains:
  - /c
  - /r
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_invoke_obfuscation_var_services_security.yml)
