---
sigma_id: "9b8d9203-4e0f-4cd9-bb06-4cc4ea6d0e9a"
title: "Invoke-Obfuscation Via Use MSHTA - Security"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_invoke_obfuscation_via_use_mshta_services_security.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_invoke_obfuscation_via_use_mshta_services_security.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "9b8d9203-4e0f-4cd9-bb06-4cc4ea6d0e9a"
  - "Invoke-Obfuscation Via Use MSHTA - Security"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation Via Use MSHTA - Security

Detects Obfuscated Powershell via use MSHTA in Scripts

## Metadata

- Rule ID: 9b8d9203-4e0f-4cd9-bb06-4cc4ea6d0e9a
- Status: test
- Level: high
- Author: Nikita Nazarov, oscd.community
- Date: 2020-10-09
- Modified: 2022-11-29
- Source Path: rules/windows/builtin/security/win_security_invoke_obfuscation_via_use_mshta_services_security.yml

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
  - mshta
  - vbscript:createobject
  - .run
  - window.close
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_invoke_obfuscation_via_use_mshta_services_security.yml)
