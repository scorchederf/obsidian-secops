---
sigma_id: "5b175490-b652-4b02-b1de-5b5b4083c5f8"
title: "RedMimicry Winnti Playbook Registry Manipulation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_redmimicry_winnti_reg.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_redmimicry_winnti_reg.yml"
build_date: "2026-04-27 19:13:55"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects actions caused by the RedMimicry Winnti playbook

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

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
