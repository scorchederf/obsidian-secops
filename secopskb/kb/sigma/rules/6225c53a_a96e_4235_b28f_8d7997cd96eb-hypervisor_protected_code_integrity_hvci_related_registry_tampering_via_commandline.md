---
sigma_id: "6225c53a-a96e-4235-b28f-8d7997cd96eb"
title: "Hypervisor-protected Code Integrity (HVCI) Related Registry Tampering Via CommandLine"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hvci_registry_tampering.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hvci_registry_tampering.yml"
build_date: "2026-04-26 17:03:19"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "6225c53a-a96e-4235-b28f-8d7997cd96eb"
  - "Hypervisor-protected Code Integrity (HVCI) Related Registry Tampering Via CommandLine"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Hypervisor-protected Code Integrity (HVCI) Related Registry Tampering Via CommandLine

Detects the tampering of Hypervisor-protected Code Integrity (HVCI) related registry values via command line tool reg.exe.
HVCI uses virtualization-based security to protect code integrity by ensuring that only trusted code can run in kernel mode.
Adversaries may tamper with HVCI to load malicious or unsigned drivers, which can be used to escalate privileges, maintain persistence, or evade security mechanisms.

## Metadata

- Rule ID: 6225c53a-a96e-4235-b28f-8d7997cd96eb
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2026-01-26
- Source Path: rules/windows/process_creation/proc_creation_win_hvci_registry_tampering.yml

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
selection_cli_base:
  CommandLine|contains: \DeviceGuard
selection_cli_key:
  CommandLine|contains:
  - EnableVirtualizationBasedSecurity
  - HypervisorEnforcedCodeIntegrity
condition: all of selection_*
```

## False Positives

- Legitimate system administration tasks that require disabling HVCI for troubleshooting purposes when certain drivers or applications are incompatible with it.

## Simulation

### Disable Hypervisor-Enforced Code Integrity (HVCI)

- Atomic Test: [[kb/atomic/tests/70bd71e6_eba4_4e00_92f7_617911dbe020-disable_hypervisor_enforced_code_integrity_hvci|70bd71e6-eba4-4e00-92f7-617911dbe020]]
- atomic_guid: 70bd71e6-eba4-4e00-92f7-617911dbe020
- name: Disable Hypervisor-Enforced Code Integrity (HVCI)
- technique: T1562.001
- type: atomic-red-team

## References

- https://www.sophos.com/en-us/blog/sharpening-the-knife-gold-blades-strategic-evolution
- https://learn.microsoft.com/en-us/windows/security/hardware-security/enable-virtualization-based-protection-of-code-integrity

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hvci_registry_tampering.yml)
