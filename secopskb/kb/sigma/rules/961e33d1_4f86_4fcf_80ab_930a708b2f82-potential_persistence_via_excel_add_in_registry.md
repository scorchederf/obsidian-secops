---
sigma_id: "961e33d1-4f86-4fcf-80ab-930a708b2f82"
title: "Potential Persistence Via Excel Add-in - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_xll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_xll.yml"
build_date: "2026-04-26 15:01:48"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "961e33d1-4f86-4fcf-80ab-930a708b2f82"
  - "Potential Persistence Via Excel Add-in - Registry"
attack_technique_ids:
  - "T1137.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Persistence Via Excel Add-in - Registry

Detect potential persistence via the creation of an excel add-in (XLL) file to make it run automatically when Excel is started.

## Metadata

- Rule ID: 961e33d1-4f86-4fcf-80ab-930a708b2f82
- Status: test
- Level: high
- Author: frack113
- Date: 2023-01-15
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_xll.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1137-office_application_startup|T1137.006]]

## Detection

```yaml
selection:
  TargetObject|contains: Software\Microsoft\Office\
  TargetObject|endswith: \Excel\Options
  Details|startswith: '/R '
  Details|endswith: .xll
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/4ae9580a1a8772db87a1b6cdb0d03e5af231e966/atomics/T1137.006/T1137.006.md
- https://labs.withsecure.com/publications/add-in-opportunities-for-office-persistence

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_xll.yml)
