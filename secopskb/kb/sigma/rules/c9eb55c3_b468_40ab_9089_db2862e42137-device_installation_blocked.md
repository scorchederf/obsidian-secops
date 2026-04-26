---
sigma_id: "c9eb55c3-b468-40ab-9089-db2862e42137"
title: "Device Installation Blocked"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_device_installation_blocked.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_device_installation_blocked.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "c9eb55c3-b468-40ab-9089-db2862e42137"
  - "Device Installation Blocked"
attack_technique_ids:
  - "T1200"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Device Installation Blocked

Detects an installation of a device that is forbidden by the system policy

## Metadata

- Rule ID: c9eb55c3-b468-40ab-9089-db2862e42137
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-10-14
- Source Path: rules/windows/builtin/security/win_security_device_installation_blocked.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1200-hardware_additions|T1200]]

## Detection

```yaml
selection:
  EventID: 6423
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/Yamato-Security/EnableWindowsLogSettings/blob/7f6d755d45ac7cc9fc35b0cbf498e6aa4ef19def/ConfiguringSecurityLogAuditPolicies.md
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-6423

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_device_installation_blocked.yml)
