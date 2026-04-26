---
sigma_id: "80b708f3-d034-40e4-a6c8-d23b7a7db3d1"
title: "Invoke-Obfuscation Via Stdin - Security"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_invoke_obfuscation_via_stdin_services_security.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_invoke_obfuscation_via_stdin_services_security.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "80b708f3-d034-40e4-a6c8-d23b7a7db3d1"
  - "Invoke-Obfuscation Via Stdin - Security"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation Via Stdin - Security

Detects Obfuscated Powershell via Stdin in Scripts

## Metadata

- Rule ID: 80b708f3-d034-40e4-a6c8-d23b7a7db3d1
- Status: test
- Level: high
- Author: Nikita Nazarov, oscd.community
- Date: 2020-10-12
- Modified: 2022-11-29
- Source Path: rules/windows/builtin/security/win_security_invoke_obfuscation_via_stdin_services_security.yml

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
  - set
  - '&&'
  ServiceFileName|contains:
  - environment
  - invoke
  - ${input)
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_invoke_obfuscation_via_stdin_services_security.yml)
