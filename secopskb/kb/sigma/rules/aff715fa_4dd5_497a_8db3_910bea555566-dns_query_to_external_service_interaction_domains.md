---
sigma_id: "aff715fa-4dd5-497a-8db3-910bea555566"
title: "DNS Query to External Service Interaction Domains"
framework: "sigma"
generated: "true"
source_path: "rules/network/dns/net_dns_external_service_interaction_domains.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/dns/net_dns_external_service_interaction_domains.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "dns"
aliases:
  - "aff715fa-4dd5-497a-8db3-910bea555566"
  - "DNS Query to External Service Interaction Domains"
attack_technique_ids:
  - "T1190"
  - "T1595.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious DNS queries to external service interaction domains often used for out-of-band interactions after successful RCE

## Logsource

- category: dns

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]]
- [[kb/attack/techniques/T1595-active_scanning#^t1595002-vulnerability-scanning|T1595.002: Vulnerability Scanning]]

## Detection

```yaml
selection:
  query|endswith:
  - .burpcollaborator.net
  - .canarytokens.com
  - .ceye.io
  - .ddns.1443.eu.org
  - .ddns.bypass.eu.org
  - .ddns.xn--gg8h.eu.org
  - .digimg.store
  - .dns.su18.org
  - .dnshook.site
  - .dnslog.cn
  - .dnslog.ink
  - .instances.httpworkbench.com
  - .interact.sh
  - .log.dnslog.pp.ua
  - .log.dnslog.qzz.io
  - .log.dnslogs.dpdns.org
  - .log.javaweb.org
  - .log.nat.cloudns.ph
  - .oast.fun
  - .oast.live
  - .oast.me
  - .oast.online
  - .oast.pro
  - .oast.site
  - .oastify.com
  - .p8.lol
  - .requestbin.net
filter_main_polling:
  query|contains: polling.oastify.com
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legitimate security scanning.

## References

- https://twitter.com/breakersall/status/1533493587828260866
- https://www.bitdefender.com/en-us/blog/businessinsights/bitdefender-advisory-critical-unauthenticated-rce-windows-server-update-services-cve-2025-59287
- https://github.com/SigmaHQ/sigma/pull/5724#issuecomment-3466382234

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/dns/net_dns_external_service_interaction_domains.yml)
