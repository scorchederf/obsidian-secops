---
sigma_id: "5468045b-4fcc-4d1a-973c-c9c9578edacb"
title: "Raw Paste Service Access"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_raw_paste_service_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_raw_paste_service_access.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "proxy"
aliases:
  - "5468045b-4fcc-4d1a-973c-c9c9578edacb"
  - "Raw Paste Service Access"
attack_technique_ids:
  - "T1071.001"
  - "T1102.001"
  - "T1102.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Raw Paste Service Access

Detects direct access to raw pastes in different paste services often used by malware in their second stages to download malicious code in encrypted or encoded form

## Metadata

- Rule ID: 5468045b-4fcc-4d1a-973c-c9c9578edacb
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2019-12-05
- Modified: 2023-01-19
- Source Path: rules/web/proxy_generic/proxy_raw_paste_service_access.yml

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
  c-uri|contains:
  - .paste.ee/r/
  - .pastebin.com/raw/
  - .hastebin.com/raw/
  - .ghostbin.co/paste/*/raw/
  - pastetext.net/
  - pastebin.pl/
  - paste.ee/
condition: selection
```

## False Positives

- User activity (e.g. developer that shared and copied code snippets and used the raw link instead of just copy & paste)

## References

- https://www.virustotal.com/gui/domain/paste.ee/relations

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_raw_paste_service_access.yml)
