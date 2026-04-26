---
sigma_id: "72f4ab3f-787d-495d-a55d-68c2ff46cf4c"
title: "Connection Proxy"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_proxy_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_proxy_connection.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "72f4ab3f-787d-495d-a55d-68c2ff46cf4c"
  - "Connection Proxy"
attack_technique_ids:
  - "T1090"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Connection Proxy

Detects setting proxy configuration

## Metadata

- Rule ID: 72f4ab3f-787d-495d-a55d-68c2ff46cf4c
- Status: test
- Level: low
- Author: Ömer Günal
- Date: 2020-06-17
- Modified: 2022-10-05
- Source Path: rules/linux/process_creation/proc_creation_lnx_proxy_connection.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - http_proxy=
  - https_proxy=
condition: selection
```

## False Positives

- Legitimate administration activities

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_proxy_connection.yml)
