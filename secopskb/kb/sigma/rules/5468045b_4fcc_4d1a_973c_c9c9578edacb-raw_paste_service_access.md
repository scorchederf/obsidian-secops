---
sigma_id: "5468045b-4fcc-4d1a-973c-c9c9578edacb"
title: "Raw Paste Service Access"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_raw_paste_service_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_raw_paste_service_access.yml"
build_date: "2026-04-27 19:13:55"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects direct access to raw pastes in different paste services often used by malware in their second stages to download malicious code in encrypted or encoded form

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]
- [[kb/attack/techniques/T1102-web_service#^t1102001-dead-drop-resolver|T1102.001: Dead Drop Resolver]]
- [[kb/attack/techniques/T1102-web_service#^t1102003-one-way-communication|T1102.003: One-Way Communication]]

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
