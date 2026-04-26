---
sigma_id: "aa37cbb0-da36-42cb-a90f-fdf216fc7467"
title: "AMSI Disabled via Registry Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_amsi_disable.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_amsi_disable.yml"
build_date: "2026-04-26 14:14:19"
status: "experimental"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "aa37cbb0-da36-42cb-a90f-fdf216fc7467"
  - "AMSI Disabled via Registry Modification"
attack_technique_ids:
  - "T1562.001"
  - "T1562.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AMSI Disabled via Registry Modification

Detects attempts to disable AMSI (Anti-Malware Scan Interface) by modifying the AmsiEnable registry value.
Anti-Malware Scan Interface (AMSI) is a security feature in Windows that allows applications and services to integrate with anti-malware products for enhanced protection against malicious content.
Adversaries may attempt to disable AMSI to evade detection by security software, allowing them to execute malicious scripts or code without being scanned.

## Metadata

- Rule ID: aa37cbb0-da36-42cb-a90f-fdf216fc7467
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-12-25
- Source Path: rules/windows/registry/registry_set/registry_set_amsi_disable.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562.006]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Software\Microsoft\Windows Script\Settings\AmsiEnable
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Unlikely

## Simulation

### AMSI Bypass - Create AMSIEnable Reg Key

- atomic_guid: 728eca7b-0444-4f6f-ac36-437e3d751dc0
- name: AMSI Bypass - Create AMSIEnable Reg Key
- technique: T1562.001
- type: atomic-red-team

## References

- https://mostafayahiax.medium.com/hunting-for-amsi-bypassing-methods-9886dda0bf9d
- https://docs.microsoft.com/en-us/windows/win32/amsi/antimalware-scan-interface-portal
- https://www.mdsec.co.uk/2019/02/macros-and-more-with-sharpshooter-v2-0/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_amsi_disable.yml)
