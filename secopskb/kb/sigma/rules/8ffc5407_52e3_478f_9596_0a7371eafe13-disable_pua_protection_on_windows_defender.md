---
sigma_id: "8ffc5407-52e3-478f-9596-0a7371eafe13"
title: "Disable PUA Protection on Windows Defender"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_disabled_pua_protection_on_microsoft_defender.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disabled_pua_protection_on_microsoft_defender.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "8ffc5407-52e3-478f-9596-0a7371eafe13"
  - "Disable PUA Protection on Windows Defender"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Disable PUA Protection on Windows Defender

Detects disabling Windows Defender PUA protection

## Metadata

- Rule ID: 8ffc5407-52e3-478f-9596-0a7371eafe13
- Status: test
- Level: high
- Author: Austin Songer @austinsonger
- Date: 2021-08-04
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_disabled_pua_protection_on_microsoft_defender.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  TargetObject|contains: \Policies\Microsoft\Windows Defender\PUAProtection
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Unknown

## References

- https://www.tenforums.com/tutorials/32236-enable-disable-microsoft-defender-pua-protection-windows-10-a.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disabled_pua_protection_on_microsoft_defender.yml)
