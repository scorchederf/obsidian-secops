---
sigma_id: "c17d47b7-dcd6-4109-87eb-d1817bd4cbc9"
title: "Windows Credential Guard Registry Tampering Via CommandLine"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_credential_guard_registry_tampering.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_credential_guard_registry_tampering.yml"
build_date: "2026-04-26 15:01:54"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c17d47b7-dcd6-4109-87eb-d1817bd4cbc9"
  - "Windows Credential Guard Registry Tampering Via CommandLine"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Credential Guard Registry Tampering Via CommandLine

Detects attempts to add, modify, or delete Windows Credential Guard related registry keys or values via command line tools such as Reg.exe or PowerShell.
Credential Guard uses virtualization-based security to isolate secrets so that only privileged system software can access them.
Adversaries may disable Credential Guard to gain access to sensitive credentials stored in the system, such as NTLM hashes and Kerberos tickets, which can be used for lateral movement and privilege escalation.
The rule matches suspicious command lines that target DeviceGuard or LSA registry paths and manipulate keys like EnableVirtualizationBasedSecurity, RequirePlatformSecurityFeatures, or LsaCfgFlags.
Such activity may indicate an attempt to disable or tamper with Credential Guard, potentially exposing sensitive credentials for misuse.

## Metadata

- Rule ID: c17d47b7-dcd6-4109-87eb-d1817bd4cbc9
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-12-26
- Source Path: rules/windows/process_creation/proc_creation_win_credential_guard_registry_tampering.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  - \reg.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
  - reg.exe
selection_cli:
  CommandLine|contains:
  - 'add '
  - 'New-ItemProperty '
  - 'Set-ItemProperty '
  - 'si '
  - 'delete '
  - 'del '
  - 'Remove-ItemProperty '
  - 'rp '
selection_key_base:
  CommandLine|contains:
  - \Control\DeviceGuard
  - \Control\LSA
  - Software\Policies\Microsoft\Windows\DeviceGuard
selection_key_specific:
  CommandLine|contains:
  - EnableVirtualizationBasedSecurity
  - RequirePlatformSecurityFeatures
  - LsaCfgFlags
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://woshub.com/disable-credential-guard-windows/
- https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-deviceguard

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_credential_guard_registry_tampering.yml)
