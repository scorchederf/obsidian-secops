---
sigma_id: "93d298a1-d28f-47f1-a468-d971e7796679"
title: "Disable Tamper Protection on Windows Defender"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_disabled_tamper_protection_on_microsoft_defender.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disabled_tamper_protection_on_microsoft_defender.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "93d298a1-d28f-47f1-a468-d971e7796679"
  - "Disable Tamper Protection on Windows Defender"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Disable Tamper Protection on Windows Defender

Detects disabling Windows Defender Tamper Protection

## Metadata

- Rule ID: 93d298a1-d28f-47f1-a468-d971e7796679
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-08-04
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_disabled_tamper_protection_on_microsoft_defender.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  TargetObject|contains: \Microsoft\Windows Defender\Features\TamperProtection
  Details: DWORD (0x00000000)
filter_msmpeng_client:
  Image|startswith: C:\ProgramData\Microsoft\Windows Defender\Platform\
  Image|endswith: \MsMpEng.exe
filter_msmpeng_domain_controller:
  Image: C:\Program Files\Windows Defender\MsMpEng.exe
condition: selection and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://www.tenforums.com/tutorials/123792-turn-off-tamper-protection-microsoft-defender-antivirus.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disabled_tamper_protection_on_microsoft_defender.yml)
