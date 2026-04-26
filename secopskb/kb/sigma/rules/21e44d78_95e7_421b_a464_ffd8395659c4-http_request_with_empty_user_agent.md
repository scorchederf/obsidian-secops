---
sigma_id: "21e44d78-95e7-421b-a464-ffd8395659c4"
title: "HTTP Request With Empty User Agent"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_ua_empty.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_empty.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "proxy"
aliases:
  - "21e44d78-95e7-421b-a464-ffd8395659c4"
  - "HTTP Request With Empty User Agent"
attack_technique_ids:
  - "T1071.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HTTP Request With Empty User Agent

Detects a potentially suspicious empty user agent strings in proxy log.
Could potentially indicate an uncommon request method.

## Metadata

- Rule ID: 21e44d78-95e7-421b-a464-ffd8395659c4
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2017-07-08
- Modified: 2021-11-27
- Source Path: rules/web/proxy_generic/proxy_ua_empty.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]

## Detection

```yaml
selection:
  c-useragent: ''
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/Carlos_Perez/status/883455096645931008

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_empty.yml)
