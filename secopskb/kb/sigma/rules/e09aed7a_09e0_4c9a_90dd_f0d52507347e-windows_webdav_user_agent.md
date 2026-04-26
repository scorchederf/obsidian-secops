---
sigma_id: "e09aed7a-09e0-4c9a-90dd-f0d52507347e"
title: "Windows WebDAV User Agent"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_downloadcradle_webdav.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_downloadcradle_webdav.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "high"
logsource: "proxy"
aliases:
  - "e09aed7a-09e0-4c9a-90dd-f0d52507347e"
  - "Windows WebDAV User Agent"
attack_technique_ids:
  - "T1071.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows WebDAV User Agent

Detects WebDav DownloadCradle

## Metadata

- Rule ID: e09aed7a-09e0-4c9a-90dd-f0d52507347e
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2018-04-06
- Modified: 2021-11-27
- Source Path: rules/web/proxy_generic/proxy_downloadcradle_webdav.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]

## Detection

```yaml
selection:
  c-useragent|startswith: Microsoft-WebDAV-MiniRedir/
  cs-method: GET
condition: selection
```

## False Positives

- Administrative scripts that download files from the Internet
- Administrative scripts that retrieve certain website contents
- Legitimate WebDAV administration

## References

- https://mgreen27.github.io/posts/2018/04/02/DownloadCradle.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_downloadcradle_webdav.yml)
