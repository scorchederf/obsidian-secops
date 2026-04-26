---
sigma_id: "304810ed-8853-437f-9e36-c4975c3dfd7e"
title: "HackTool - BabyShark Agent Default URL Pattern"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_hktl_baby_shark_default_agent_url.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_hktl_baby_shark_default_agent_url.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "critical"
logsource: "proxy"
aliases:
  - "304810ed-8853-437f-9e36-c4975c3dfd7e"
  - "HackTool - BabyShark Agent Default URL Pattern"
attack_technique_ids:
  - "T1071.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - BabyShark Agent Default URL Pattern

Detects Baby Shark C2 Framework default communication patterns

## Metadata

- Rule ID: 304810ed-8853-437f-9e36-c4975c3dfd7e
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems)
- Date: 2021-06-09
- Modified: 2024-02-15
- Source Path: rules/web/proxy_generic/proxy_hktl_baby_shark_default_agent_url.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]

## Detection

```yaml
selection:
  c-uri|contains: momyshark\?key=
condition: selection
```

## False Positives

- Unlikely

## References

- https://nasbench.medium.com/understanding-detecting-c2-frameworks-babyshark-641be4595845

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_hktl_baby_shark_default_agent_url.yml)
