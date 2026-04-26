---
sigma_id: "a166f74e-bf44-409d-b9ba-ea4b2dd8b3cd"
title: "Macro Enabled In A Potentially Suspicious Document"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_office_trust_record_susp_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_trust_record_susp_location.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "a166f74e-bf44-409d-b9ba-ea4b2dd8b3cd"
  - "Macro Enabled In A Potentially Suspicious Document"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Macro Enabled In A Potentially Suspicious Document

Detects registry changes to Office trust records where the path is located in a potentially suspicious location

## Metadata

- Rule ID: a166f74e-bf44-409d-b9ba-ea4b2dd8b3cd
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-21
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_office_trust_record_susp_location.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection_value:
  TargetObject|contains: \Security\Trusted Documents\TrustRecords
selection_paths:
  TargetObject|contains:
  - /AppData/Local/Microsoft/Windows/INetCache/
  - /AppData/Local/Temp/
  - /PerfLogs/
  - C:/Users/Public/
  - file:///D:/
  - file:///E:/
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://twitter.com/inversecos/status/1494174785621819397
- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_office_trust_record_susp_location.yml)
