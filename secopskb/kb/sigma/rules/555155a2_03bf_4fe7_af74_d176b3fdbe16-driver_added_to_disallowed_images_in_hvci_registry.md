---
sigma_id: "555155a2-03bf-4fe7-af74-d176b3fdbe16"
title: "Driver Added To Disallowed Images In HVCI - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_hvci_disallowed_images.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_hvci_disallowed_images.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "555155a2-03bf-4fe7-af74-d176b3fdbe16"
  - "Driver Added To Disallowed Images In HVCI - Registry"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Driver Added To Disallowed Images In HVCI - Registry

Detects changes to the "HVCIDisallowedImages" registry value to potentially add a driver to the list, in order to prevent it from loading.

## Metadata

- Rule ID: 555155a2-03bf-4fe7-af74-d176b3fdbe16
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), Omar Khaled (@beacon_exe)
- Date: 2023-12-05
- Modified: 2024-08-21
- Source Path: rules/windows/registry/registry_set/registry_set_hvci_disallowed_images.yml

## Logsource

- category: registry_set
- product: windows

## Detection

```yaml
selection:
  TargetObject|contains|all:
  - \Control\CI\
  - \HVCIDisallowedImages
condition: selection
```

## False Positives

- Legitimate usage of this key would also trigger this. Investigate the driver being added and make sure its intended

## References

- https://github.com/yardenshafir/conference_talks/blob/3de1f5d7c02656c35117f067fbff0a219c304b09/OffensiveCon_2023_Your_Mitigations_are_My_Opportunities.pdf
- https://x.com/yarden_shafir/status/1822667605175324787

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_hvci_disallowed_images.yml)
