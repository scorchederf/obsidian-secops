---
sigma_id: "2a926e6a-4b81-4011-8a96-e36cc8c04302"
title: "PowerShell Scripts Installed as Services - Security"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_powershell_script_installed_as_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_powershell_script_installed_as_service.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "2a926e6a-4b81-4011-8a96-e36cc8c04302"
  - "PowerShell Scripts Installed as Services - Security"
attack_technique_ids:
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Scripts Installed as Services - Security

Detects powershell script installed as a Service

## Metadata

- Rule ID: 2a926e6a-4b81-4011-8a96-e36cc8c04302
- Status: test
- Level: high
- Author: oscd.community, Natalia Shornikova
- Date: 2020-10-06
- Modified: 2022-11-29
- Source Path: rules/windows/builtin/security/win_security_powershell_script_installed_as_service.yml

## Logsource

- definition: The 'System Security Extension' audit subcategory need to be enabled to log the EID 4697
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1569-system_services|T1569.002]]

## Detection

```yaml
selection:
  EventID: 4697
  ServiceFileName|contains:
  - powershell
  - pwsh
condition: selection
```

## False Positives

- Unknown

## References

- https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_powershell_script_installed_as_service.yml)
