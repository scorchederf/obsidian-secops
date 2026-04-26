---
sigma_id: "1712bafe-be05-4a0e-89d4-17a3ed151bf5"
title: "Potential Hello-World Scraper Botnet Activity"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_hello_world_user_agent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_hello_world_user_agent.yml"
build_date: "2026-04-26 14:14:32"
status: "experimental"
level: "medium"
logsource: "proxy"
aliases:
  - "1712bafe-be05-4a0e-89d4-17a3ed151bf5"
  - "Potential Hello-World Scraper Botnet Activity"
attack_technique_ids:
  - "T1595"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Hello-World Scraper Botnet Activity

Detects network traffic potentially associated with a scraper botnet variant that uses the "Hello-World/1.0" user-agent string.

## Metadata

- Rule ID: 1712bafe-be05-4a0e-89d4-17a3ed151bf5
- Status: experimental
- Level: medium
- Author: Joseph A. M.
- Date: 2025-08-02
- Source Path: rules/web/proxy_generic/proxy_hello_world_user_agent.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1595-active_scanning|T1595]]

## Detection

```yaml
selection:
  c-useragent: Hello-World/1.0
  cs-method: GET
condition: selection
```

## False Positives

- Legitimate network monitoring or vulnerability scanning tools that may use this generic user agent.
- Internal development or testing scripts. Consider filtering by source IP if this is expected from certain systems.

## References

- https://www.greynoise.io/blog/new-scraper-botnet-concentrated-in-taiwan
- https://viz.greynoise.io/tags/hello-world-scraper-botnet?days=30

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_hello_world_user_agent.yml)
