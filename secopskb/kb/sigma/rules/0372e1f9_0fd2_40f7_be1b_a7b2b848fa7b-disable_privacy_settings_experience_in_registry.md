---
sigma_id: "0372e1f9-0fd2-40f7-be1b-a7b2b848fa7b"
title: "Disable Privacy Settings Experience in Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_disable_privacy_settings_experience.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_privacy_settings_experience.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "0372e1f9-0fd2-40f7-be1b-a7b2b848fa7b"
  - "Disable Privacy Settings Experience in Registry"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Disable Privacy Settings Experience in Registry

Detects registry modifications that disable Privacy Settings Experience

## Metadata

- Rule ID: 0372e1f9-0fd2-40f7-be1b-a7b2b848fa7b
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-10-02
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_disable_privacy_settings_experience.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  TargetObject|endswith: \SOFTWARE\Policies\Microsoft\Windows\OOBE\DisablePrivacyExperience
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Legitimate admin script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/9e5b12c4912c07562aec7500447b11fa3e17e254/atomics/T1562.001/T1562.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_disable_privacy_settings_experience.yml)
