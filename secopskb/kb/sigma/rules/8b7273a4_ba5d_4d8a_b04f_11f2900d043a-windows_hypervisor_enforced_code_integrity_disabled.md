---
sigma_id: "8b7273a4-ba5d-4d8a-b04f-11f2900d043a"
title: "Windows Hypervisor Enforced Code Integrity Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_deviceguard_hypervisorenforcedcodeintegrity_disabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_deviceguard_hypervisorenforcedcodeintegrity_disabled.yml"
build_date: "2026-04-26 15:01:55"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "8b7273a4-ba5d-4d8a-b04f-11f2900d043a"
  - "Windows Hypervisor Enforced Code Integrity Disabled"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Hypervisor Enforced Code Integrity Disabled

Detects changes to the HypervisorEnforcedCodeIntegrity registry key and the "Enabled" value being set to 0 in order to disable the Hypervisor Enforced Code Integrity feature. This allows an attacker to load unsigned and untrusted code to be run in the kernel

## Metadata

- Rule ID: 8b7273a4-ba5d-4d8a-b04f-11f2900d043a
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), Anish Bogati
- Date: 2023-03-14
- Modified: 2024-07-05
- Source Path: rules/windows/registry/registry_set/registry_set_deviceguard_hypervisorenforcedcodeintegrity_disabled.yml

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
  - \Control\DeviceGuard\HypervisorEnforcedCodeIntegrity
  - \Control\DeviceGuard\Scenarios\HypervisorEnforcedCodeIntegrity\Enabled
  - \Microsoft\Windows\DeviceGuard\HypervisorEnforcedCodeIntegrity
  Details: DWORD (0x00000000)
condition: selection
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

- https://www.welivesecurity.com/2023/03/01/blacklotus-uefi-bootkit-myth-confirmed/
- https://github.com/redcanaryco/atomic-red-team/blob/04e487c1828d76df3e834621f4f893ea756d5232/atomics/T1562.001/T1562.001.md#atomic-test-43---disable-hypervisor-enforced-code-integrity-hvci

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_deviceguard_hypervisorenforcedcodeintegrity_disabled.yml)
