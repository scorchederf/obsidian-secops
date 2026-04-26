---
sigma_id: "41d1058a-aea7-4952-9293-29eaaf516465"
title: "Removal Of AMSI Provider Registry Keys"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_delete/registry_delete_removal_amsi_registry_key.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_delete/registry_delete_removal_amsi_registry_key.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / registry_delete"
aliases:
  - "41d1058a-aea7-4952-9293-29eaaf516465"
  - "Removal Of AMSI Provider Registry Keys"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Removal Of AMSI Provider Registry Keys

Detects the deletion of AMSI provider registry key entries in HKLM\Software\Microsoft\AMSI. This technique could be used by an attacker in order to disable AMSI inspection.

## Metadata

- Rule ID: 41d1058a-aea7-4952-9293-29eaaf516465
- Status: test
- Level: high
- Author: frack113
- Date: 2021-06-07
- Modified: 2025-10-07
- Source Path: rules/windows/registry/registry_delete/registry_delete_removal_amsi_registry_key.yml

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
  - '{2781761E-28E0-4109-99FE-B9D127C57AFE}'
  - '{A7C452EF-8E9F-42EB-9F2B-245613CA0DC9}'
filter_main_defender:
  Image|startswith:
  - C:\ProgramData\Microsoft\Windows Defender\Platform\
  - C:\Program Files\Windows Defender\
  - C:\Program Files (x86)\Windows Defender\
  Image|endswith: \MsMpEng.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unlikely

## Simulation

### AMSI Bypass - Remove AMSI Provider Reg Key

- Atomic Test: [[kb/atomic/tests/13f09b91_c953_438e_845b_b585e51cac9b-amsi_bypass_remove_amsi_provider_reg_key|13f09b91-c953-438e-845b-b585e51cac9b]]
- atomic_guid: 13f09b91-c953-438e-845b-b585e51cac9b
- name: AMSI Bypass - Remove AMSI Provider Reg Key
- technique: T1562.001
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md
- https://seclists.org/fulldisclosure/2020/Mar/45

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_delete/registry_delete_removal_amsi_registry_key.yml)
