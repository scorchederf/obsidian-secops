---
sigma_id: "7a922f1b-2635-4d6c-91ef-af228b198ad3"
title: "Invoke-Obfuscation COMPRESS OBFUSCATION - Security"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_invoke_obfuscation_via_compress_services_security.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_invoke_obfuscation_via_compress_services_security.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "7a922f1b-2635-4d6c-91ef-af228b198ad3"
  - "Invoke-Obfuscation COMPRESS OBFUSCATION - Security"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Invoke-Obfuscation COMPRESS OBFUSCATION - Security

Detects Obfuscated Powershell via COMPRESS OBFUSCATION

## Metadata

- Rule ID: 7a922f1b-2635-4d6c-91ef-af228b198ad3
- Status: test
- Level: medium
- Author: Timur Zinniatullin, oscd.community
- Date: 2020-10-18
- Modified: 2022-11-29
- Source Path: rules/windows/builtin/security/win_security_invoke_obfuscation_via_compress_services_security.yml

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
  - new-object
  - text.encoding]::ascii
  - readtoend
  ServiceFileName|contains:
  - system.io.compression.deflatestream
  - system.io.streamreader
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_invoke_obfuscation_via_compress_services_security.yml)
