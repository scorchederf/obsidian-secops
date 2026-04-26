---
sigma_id: "0c718a5e-4284-4fb9-b4d9-b9a50b3a1974"
title: "Invoke-Obfuscation STDIN+ Launcher - Security"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_invoke_obfuscation_stdin_services_security.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_invoke_obfuscation_stdin_services_security.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "0c718a5e-4284-4fb9-b4d9-b9a50b3a1974"
  - "Invoke-Obfuscation STDIN+ Launcher - Security"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation STDIN+ Launcher - Security

Detects Obfuscated use of stdin to execute PowerShell

## Metadata

- Rule ID: 0c718a5e-4284-4fb9-b4d9-b9a50b3a1974
- Status: test
- Level: high
- Author: Jonathan Cheong, oscd.community
- Date: 2020-10-15
- Modified: 2022-11-29
- Source Path: rules/windows/builtin/security/win_security_invoke_obfuscation_stdin_services_security.yml

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
  - powershell
selection2:
  ServiceFileName|contains:
  - ${input}
  - noexit
selection3:
  ServiceFileName|contains:
  - ' /c '
  - ' /r '
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_invoke_obfuscation_stdin_services_security.yml)
