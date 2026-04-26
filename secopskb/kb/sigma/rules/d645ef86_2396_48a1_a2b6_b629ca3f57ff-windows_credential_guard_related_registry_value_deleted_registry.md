---
sigma_id: "d645ef86-2396-48a1-a2b6-b629ca3f57ff"
title: "Windows Credential Guard Related Registry Value Deleted - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_delete/registry_delete_disable_credential_guard.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_delete/registry_delete_disable_credential_guard.yml"
build_date: "2026-04-26 15:01:54"
status: "experimental"
level: "high"
logsource: "windows / registry_delete"
aliases:
  - "d645ef86-2396-48a1-a2b6-b629ca3f57ff"
  - "Windows Credential Guard Related Registry Value Deleted - Registry"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Credential Guard Related Registry Value Deleted - Registry

Detects attempts to disable Windows Credential Guard by deleting registry values. Credential Guard uses virtualization-based security to isolate secrets so that only privileged system software can access them.
Adversaries may disable Credential Guard to gain access to sensitive credentials stored in the system, such as NTLM hashes and Kerberos tickets, which can be used for lateral movement and privilege escalation.

## Metadata

- Rule ID: d645ef86-2396-48a1-a2b6-b629ca3f57ff
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-12-26
- Source Path: rules/windows/registry/registry_delete/registry_delete_disable_credential_guard.yml

## Logsource

- category: registry_delete
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
  - \DeviceGuard\RequirePlatformSecurityFeatures
  - \Lsa\LsaCfgFlags
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/DambergC/SaveFolder/blob/90e945eba80fae85f2d54b4616e05a44ec90c500/Cygate%20Installation%20tool%206.22/Script/OSD/OSDeployment-CredentialGuardDisable.ps1#L50
- https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/configure

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_delete/registry_delete_disable_credential_guard.yml)
