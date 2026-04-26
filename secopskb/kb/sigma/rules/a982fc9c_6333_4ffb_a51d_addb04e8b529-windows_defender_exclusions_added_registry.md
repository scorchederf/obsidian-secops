---
sigma_id: "a982fc9c-6333-4ffb-a51d-addb04e8b529"
title: "Windows Defender Exclusions Added - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_defender_exclusions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_defender_exclusions.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "a982fc9c-6333-4ffb-a51d-addb04e8b529"
  - "Windows Defender Exclusions Added - Registry"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Defender Exclusions Added - Registry

Detects the Setting of Windows Defender Exclusions

## Metadata

- Rule ID: a982fc9c-6333-4ffb-a51d-addb04e8b529
- Status: test
- Level: medium
- Author: Christian Burkard (Nextron Systems)
- Date: 2021-07-06
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_defender_exclusions.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection2:
  TargetObject|contains: \Microsoft\Windows Defender\Exclusions
condition: selection2
```

## False Positives

- Administrator actions

## References

- https://twitter.com/_nullbind/status/1204923340810543109

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_defender_exclusions.yml)
