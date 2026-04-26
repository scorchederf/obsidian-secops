---
sigma_id: "894a8613-cf12-48b3-8e57-9085f54aa0c3"
title: "Potential Base64 Encoded User-Agent"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_ua_susp_base64.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_susp_base64.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "proxy"
aliases:
  - "894a8613-cf12-48b3-8e57-9085f54aa0c3"
  - "Potential Base64 Encoded User-Agent"
attack_technique_ids:
  - "T1071.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Base64 Encoded User-Agent

Detects User Agent strings that end with an equal sign, which can be a sign of base64 encoding.

## Metadata

- Rule ID: 894a8613-cf12-48b3-8e57-9085f54aa0c3
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Brian Ingram (update)
- Date: 2022-07-08
- Modified: 2023-05-04
- Source Path: rules/web/proxy_generic/proxy_ua_susp_base64.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]

## Detection

```yaml
selection:
  c-useragent|endswith: '='
condition: selection
```

## False Positives

- Unknown

## References

- https://blogs.jpcert.or.jp/en/2022/07/yamabot.html
- https://deviceatlas.com/blog/list-of-user-agent-strings#desktop

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_susp_base64.yml)
