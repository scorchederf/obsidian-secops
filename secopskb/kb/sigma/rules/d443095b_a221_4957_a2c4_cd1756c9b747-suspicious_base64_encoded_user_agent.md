---
sigma_id: "d443095b-a221-4957-a2c4-cd1756c9b747"
title: "Suspicious Base64 Encoded User-Agent"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_ua_base64_encoded.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_base64_encoded.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "proxy"
aliases:
  - "d443095b-a221-4957-a2c4-cd1756c9b747"
  - "Suspicious Base64 Encoded User-Agent"
attack_technique_ids:
  - "T1071.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Base64 Encoded User-Agent

Detects suspicious encoded User-Agent strings, as seen used by some malware.

## Metadata

- Rule ID: d443095b-a221-4957-a2c4-cd1756c9b747
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-04
- Source Path: rules/web/proxy_generic/proxy_ua_base64_encoded.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]

## Detection

```yaml
selection:
  c-useragent|startswith:
  - Q2hyb21l
  - QXBwbGVXZWJLaX
  - RGFsdmlr
  - TW96aWxsY
condition: selection
```

## False Positives

- Unknown

## References

- https://deviceatlas.com/blog/list-of-user-agent-strings#desktop

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_base64_encoded.yml)
