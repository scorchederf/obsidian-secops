---
sigma_id: "b923f7d6-ac89-4a50-a71a-89fb846b4aa8"
title: "HackTool - Empire UserAgent URI Combo"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_hktl_empire_ua_uri_patterns.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_hktl_empire_ua_uri_patterns.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "proxy"
aliases:
  - "b923f7d6-ac89-4a50-a71a-89fb846b4aa8"
  - "HackTool - Empire UserAgent URI Combo"
attack_technique_ids:
  - "T1071.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# HackTool - Empire UserAgent URI Combo

Detects user agent and URI paths used by empire agents

## Metadata

- Rule ID: b923f7d6-ac89-4a50-a71a-89fb846b4aa8
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2020-07-13
- Modified: 2024-02-26
- Source Path: rules/web/proxy_generic/proxy_hktl_empire_ua_uri_patterns.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]

## Detection

```yaml
selection:
  c-useragent: Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
  cs-uri:
  - /admin/get.php
  - /news.php
  - /login/process.php
  cs-method: POST
condition: selection
```

## False Positives

- Valid requests with this exact user agent to server scripts of the defined names

## References

- https://github.com/BC-SECURITY/Empire

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_hktl_empire_ua_uri_patterns.yml)
