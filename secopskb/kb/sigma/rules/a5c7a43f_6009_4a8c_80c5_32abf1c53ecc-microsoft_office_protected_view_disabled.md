---
sigma_id: "a5c7a43f-6009-4a8c-80c5-32abf1c53ecc"
title: "Microsoft Office Protected View Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_office_disable_protected_view_features.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_disable_protected_view_features.yml"
build_date: "2026-04-26 15:01:46"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "a5c7a43f-6009-4a8c-80c5-32abf1c53ecc"
  - "Microsoft Office Protected View Disabled"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Microsoft Office Protected View Disabled

Detects changes to Microsoft Office protected view registry keys with which the attacker disables this feature.

## Metadata

- Rule ID: a5c7a43f-6009-4a8c-80c5-32abf1c53ecc
- Status: test
- Level: high
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-06-08
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_office_disable_protected_view_features.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_path:
  TargetObject|contains|all:
  - \SOFTWARE\Microsoft\Office\
  - \Security\ProtectedView\
selection_values_1:
  Details: DWORD (0x00000001)
  TargetObject|endswith:
  - \DisableAttachementsInPV
  - \DisableInternetFilesInPV
  - \DisableIntranetCheck
  - \DisableUnsafeLocationsInPV
selection_values_0:
  Details: DWORD (0x00000000)
  TargetObject|endswith:
  - \enabledatabasefileprotectedview
  - \enableforeigntextfileprotectedview
condition: selection_path and 1 of selection_values_*
```

## False Positives

- Unlikely

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md
- https://unit42.paloaltonetworks.com/unit42-gorgon-group-slithering-nation-state-cybercrime/
- https://yoroi.company/research/cyber-criminal-espionage-operation-insists-on-italian-manufacturing/
- https://admx.help/HKCU/software/policies/microsoft/office/16.0/excel/security/protectedview

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_disable_protected_view_features.yml)
