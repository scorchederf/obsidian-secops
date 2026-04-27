---
sigma_id: "7195a772-4b3f-43a4-a210-6a003d65caa1"
title: "Suspicious User Agent"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_ua_susp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_susp.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "proxy"
aliases:
  - "7195a772-4b3f-43a4-a210-6a003d65caa1"
  - "Suspicious User Agent"
attack_technique_ids:
  - "T1071.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious malformed user agent strings in proxy logs

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]

## Detection

```yaml
selection1:
  c-useragent|startswith:
  - user-agent
  - 'Mozilla/3.0 '
  - 'Mozilla/2.0 '
  - 'Mozilla/1.0 '
  - 'Mozilla '
  - ' Mozilla/'
  - Mozila/
  - Mozilla/4.0 (compatible; MSIE 6.0; MS Web Services Client Protocol
selection2:
  c-useragent|contains:
  - ' (compatible;MSIE '
  - '.0;Windows NT '
  - loader
selection3:
  c-useragent:
  - _
  - CertUtil URL Agent
  - Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0)
  - Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0
  - HTTPS
  - Erbium-UA-4ce7c27cb4be9d32e333bf032c88235a
  - x
  - xxx
falsepositives:
- c-useragent: Mozilla/3.0 * Acrobat *
- cs-host|endswith:
  - .acrobat.com
  - .adobe.com
  - .adobe.io
condition: 1 of selection* and not falsepositives
```

## False Positives

- Unknown

## References

- https://github.com/fastly/waf_testbed/blob/8bfc406551f3045e418cbaad7596cff8da331dfc/templates/default/scanners-user-agents.data.erb

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_susp.yml)
