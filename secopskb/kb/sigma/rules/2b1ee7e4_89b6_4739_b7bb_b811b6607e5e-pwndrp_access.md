---
sigma_id: "2b1ee7e4-89b6-4739-b7bb-b811b6607e5e"
title: "PwnDrp Access"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_pwndrop.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_pwndrop.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "critical"
logsource: "proxy"
aliases:
  - "2b1ee7e4-89b6-4739-b7bb-b811b6607e5e"
  - "PwnDrp Access"
attack_technique_ids:
  - "T1071.001"
  - "T1102.001"
  - "T1102.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# PwnDrp Access

Detects downloads from PwnDrp web servers developed for red team testing and most likely also used for criminal activity

## Metadata

- Rule ID: 2b1ee7e4-89b6-4739-b7bb-b811b6607e5e
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems)
- Date: 2020-04-15
- Modified: 2021-11-27
- Source Path: rules/web/proxy_generic/proxy_pwndrop.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]
- [[kb/attack/techniques/T1102-web_service|T1102.001]]
- [[kb/attack/techniques/T1102-web_service|T1102.003]]

## Detection

```yaml
selection:
  c-uri|contains: /pwndrop/
condition: selection
```

## False Positives

- Unknown

## References

- https://breakdev.org/pwndrop/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_pwndrop.yml)
