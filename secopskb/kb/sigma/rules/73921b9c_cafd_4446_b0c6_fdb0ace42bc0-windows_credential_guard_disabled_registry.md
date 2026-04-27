---
sigma_id: "73921b9c-cafd-4446-b0c6-fdb0ace42bc0"
title: "Windows Credential Guard Disabled - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_credential_guard_disabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_credential_guard_disabled.yml"
build_date: "2026-04-26 17:03:24"
status: "experimental"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "73921b9c-cafd-4446-b0c6-fdb0ace42bc0"
  - "Windows Credential Guard Disabled - Registry"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Windows Credential Guard Disabled - Registry

Detects attempts to disable Windows Credential Guard by setting registry values to 0. Credential Guard uses virtualization-based security to isolate secrets so that only privileged system software can access them.
Adversaries may disable Credential Guard to gain access to sensitive credentials stored in the system, such as NTLM hashes and Kerberos tickets, which can be used for lateral movement and privilege escalation.

## Metadata

- Rule ID: 73921b9c-cafd-4446-b0c6-fdb0ace42bc0
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-12-26
- Source Path: rules/windows/registry/registry_set/registry_set_credential_guard_disabled.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  TargetObject|endswith:
  - \DeviceGuard\EnableVirtualizationBasedSecurity
  - \DeviceGuard\LsaCfgFlags
  - \Lsa\LsaCfgFlags
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Unlikely

## References

- https://woshub.com/disable-credential-guard-windows/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_credential_guard_disabled.yml)
