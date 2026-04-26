---
sigma_id: "295a59c1-7b79-4b47-a930-df12c15fc9c2"
title: "Windows Registry Trust Record Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_office_trust_record_modification.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_office_trust_record_modification.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / registry_event"
aliases:
  - "295a59c1-7b79-4b47-a930-df12c15fc9c2"
  - "Windows Registry Trust Record Modification"
attack_technique_ids:
  - "T1566.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Registry Trust Record Modification

Alerts on trust record modification within the registry, indicating usage of macros

## Metadata

- Rule ID: 295a59c1-7b79-4b47-a930-df12c15fc9c2
- Status: test
- Level: medium
- Author: Antonlovesdnb, Trent Liffick (@tliffick)
- Date: 2020-02-19
- Modified: 2023-06-21
- Source Path: rules/windows/registry/registry_event/registry_event_office_trust_record_modification.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing|T1566.001]]

## Detection

```yaml
selection:
  TargetObject|contains: \Security\Trusted Documents\TrustRecords
condition: selection
```

## False Positives

- This will alert on legitimate macro usage as well, additional tuning is required

## References

- https://outflank.nl/blog/2018/01/16/hunting-for-evil-detect-macros-being-executed/
- http://az4n6.blogspot.com/2016/02/more-on-trust-records-macros-and.html
- https://twitter.com/inversecos/status/1494174785621819397

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_office_trust_record_modification.yml)
