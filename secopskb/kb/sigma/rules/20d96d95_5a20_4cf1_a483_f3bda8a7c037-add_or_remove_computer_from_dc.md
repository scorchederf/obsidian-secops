---
sigma_id: "20d96d95-5a20-4cf1-a483-f3bda8a7c037"
title: "Add or Remove Computer from DC"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_add_remove_computer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_add_remove_computer.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "low"
logsource: "windows / security"
aliases:
  - "20d96d95-5a20-4cf1-a483-f3bda8a7c037"
  - "Add or Remove Computer from DC"
attack_technique_ids:
  - "T1207"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Add or Remove Computer from DC

Detects the creation or removal of a computer. Can be used to detect attacks such as DCShadow via the creation of a new SPN.

## Metadata

- Rule ID: 20d96d95-5a20-4cf1-a483-f3bda8a7c037
- Status: test
- Level: low
- Author: frack113
- Date: 2022-10-14
- Source Path: rules/windows/builtin/security/win_security_add_remove_computer.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1207-rogue_domain_controller|T1207]]

## Detection

```yaml
selection:
  EventID:
  - 4741
  - 4743
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/Yamato-Security/EnableWindowsLogSettings/blob/7f6d755d45ac7cc9fc35b0cbf498e6aa4ef19def/ConfiguringSecurityLogAuditPolicies.md
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4741
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4743

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_add_remove_computer.yml)
