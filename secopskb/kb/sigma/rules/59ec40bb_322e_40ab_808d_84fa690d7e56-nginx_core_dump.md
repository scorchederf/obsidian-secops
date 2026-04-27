---
sigma_id: "59ec40bb-322e-40ab-808d-84fa690d7e56"
title: "Nginx Core Dump"
framework: "sigma"
generated: "true"
source_path: "rules/web/product/nginx/web_nginx_core_dump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/product/nginx/web_nginx_core_dump.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "nginx"
aliases:
  - "59ec40bb-322e-40ab-808d-84fa690d7e56"
  - "Nginx Core Dump"
attack_technique_ids:
  - "T1499.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a core dump of a crashing Nginx worker process, which could be a signal of a serious problem or exploitation attempts.

## Logsource

- service: nginx

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1499-endpoint_denial_of_service#^t1499004-application-or-system-exploitation|T1499.004: Application or System Exploitation]]

## Detection

```yaml
keywords:
- exited on signal 6 (core dumped)
condition: keywords
```

## False Positives

- Serious issues with a configuration or plugin

## References

- https://docs.nginx.com/nginx/admin-guide/monitoring/debugging/#enabling-core-dumps
- https://www.x41-dsec.de/lab/advisories/x41-2021-002-nginx-resolver-copy/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/product/nginx/web_nginx_core_dump.yml)
