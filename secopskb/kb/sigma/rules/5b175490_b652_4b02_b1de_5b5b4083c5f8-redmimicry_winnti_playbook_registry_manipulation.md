---
sigma_id: "5b175490-b652-4b02-b1de-5b5b4083c5f8"
title: "RedMimicry Winnti Playbook Registry Manipulation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_redmimicry_winnti_reg.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_redmimicry_winnti_reg.yml"
build_date: "2026-04-26 15:01:50"
status: "test"
level: "high"
logsource: "windows / registry_event"
aliases:
  - "5b175490-b652-4b02-b1de-5b5b4083c5f8"
  - "RedMimicry Winnti Playbook Registry Manipulation"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# RedMimicry Winnti Playbook Registry Manipulation

Detects actions caused by the RedMimicry Winnti playbook

## Metadata

- Rule ID: 5b175490-b652-4b02-b1de-5b5b4083c5f8
- Status: test
- Level: high
- Author: Alexander Rausch
- Date: 2020-06-24
- Modified: 2021-11-27
- Source Path: rules/windows/registry/registry_event/registry_event_redmimicry_winnti_reg.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|contains: HKLM\SOFTWARE\Microsoft\HTMLHelp\data
condition: selection
```

## False Positives

- Unknown

## References

- https://redmimicry.com

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_redmimicry_winnti_reg.yml)
