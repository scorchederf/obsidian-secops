---
sigma_id: "c5f6a85d-b647-40f7-bbad-c10b66bab038"
title: "UAC Notification Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_uac_disable_notification.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_uac_disable_notification.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "c5f6a85d-b647-40f7-bbad-c10b66bab038"
  - "UAC Notification Disabled"
attack_technique_ids:
  - "T1548.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# UAC Notification Disabled

Detects when an attacker tries to disable User Account Control (UAC) notification by tampering with the "UACDisableNotify" value.
UAC is a critical security feature in Windows that prevents unauthorized changes to the operating system. It prompts the user for permission or an administrator password before allowing actions that could affect the system's operation or change settings that affect other users.
When "UACDisableNotify" is set to 1, UAC prompts are suppressed.

## Metadata

- Rule ID: c5f6a85d-b647-40f7-bbad-c10b66bab038
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-05-10
- Source Path: rules/windows/registry/registry_set/registry_set_uac_disable_notification.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Detection

```yaml
selection:
  TargetObject|contains: \Microsoft\Security Center\UACDisableNotify
  Details: DWORD (0x00000001)
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/7e11e9b79583545f208a6dc3fa062f2ed443d999/atomics/T1548.002/T1548.002.md
- https://securityintelligence.com/x-force/x-force-hive0129-targeting-financial-institutions-latam-banking-trojan/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_uac_disable_notification.yml)
