---
sigma_id: "d526c60a-e236-4011-b165-831ffa52ab70"
title: "Windows Vulnerable Driver Blocklist Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_vulnerable_driver_blocklist_disable.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_vulnerable_driver_blocklist_disable.yml"
build_date: "2026-04-26 17:03:24"
status: "experimental"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "d526c60a-e236-4011-b165-831ffa52ab70"
  - "Windows Vulnerable Driver Blocklist Disabled"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Windows Vulnerable Driver Blocklist Disabled

Detects when the Windows Vulnerable Driver Blocklist is set to disabled. This setting is crucial for preventing the loading of known vulnerable drivers,
and its modification may indicate an attempt to bypass security controls. It is often targeted by threat actors to facilitate the installation of malicious or vulnerable drivers,
particularly in scenarios involving Endpoint Detection and Response (EDR) bypass techniques.
This rule applies to systems that support the Vulnerable Driver Blocklist feature, including Windows 10 version 1903 and later, and Windows Server 2022 and later.
Note that this change will require a reboot to take effect, and this rule only detects the registry modification action.

## Metadata

- Rule ID: d526c60a-e236-4011-b165-831ffa52ab70
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2026-01-26
- Source Path: rules/windows/registry/registry_set/registry_set_vulnerable_driver_blocklist_disable.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Control\CI\Config\VulnerableDriverBlocklistEnable
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Unlikely and should be investigated immediately.

## References

- https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules
- https://www.sophos.com/en-us/blog/sharpening-the-knife-gold-blades-strategic-evolution
- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/design/microsoft-recommended-driver-block-rules

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_vulnerable_driver_blocklist_disable.yml)
