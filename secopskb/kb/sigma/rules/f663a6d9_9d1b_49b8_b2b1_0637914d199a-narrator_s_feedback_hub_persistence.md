---
sigma_id: "f663a6d9-9d1b-49b8-b2b1-0637914d199a"
title: "Narrator's Feedback-Hub Persistence"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_narrator_feedback_persistance.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_narrator_feedback_persistance.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "high"
logsource: "windows / registry_event"
aliases:
  - "f663a6d9-9d1b-49b8-b2b1-0637914d199a"
  - "Narrator's Feedback-Hub Persistence"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Narrator's Feedback-Hub Persistence

Detects abusing Windows 10 Narrator's Feedback-Hub

## Metadata

- Rule ID: f663a6d9-9d1b-49b8-b2b1-0637914d199a
- Status: test
- Level: high
- Author: Dmitriy Lifanov, oscd.community
- Date: 2019-10-25
- Modified: 2022-03-26
- Source Path: rules/windows/registry/registry_event/registry_event_narrator_feedback_persistance.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Detection

```yaml
selection1:
  EventType: DeleteValue
  TargetObject|endswith: \AppXypsaf9f1qserqevf0sws76dx4k9a5206\Shell\open\command\DelegateExecute
selection2:
  TargetObject|endswith: \AppXypsaf9f1qserqevf0sws76dx4k9a5206\Shell\open\command\(Default)
condition: 1 of selection*
```

## False Positives

- Unknown

## References

- https://giuliocomi.blogspot.com/2019/10/abusing-windows-10-narrators-feedback.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_narrator_feedback_persistance.yml)
