---
sigma_id: "2c03648b-e081-41a5-b9fb-7d854a915091"
title: "Rclone Activity via Proxy"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_ua_rclone.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_rclone.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "proxy"
aliases:
  - "2c03648b-e081-41a5-b9fb-7d854a915091"
  - "Rclone Activity via Proxy"
attack_technique_ids:
  - "T1567.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Rclone Activity via Proxy

Detects the use of rclone, a command-line program to manage files on cloud storage, via its default user-agent string

## Metadata

- Rule ID: 2c03648b-e081-41a5-b9fb-7d854a915091
- Status: test
- Level: medium
- Author: Janantha Marasinghe
- Date: 2022-10-18
- Source Path: rules/web/proxy_generic/proxy_ua_rclone.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567.002]]

## Detection

```yaml
selection:
  c-useragent|startswith: rclone/v
condition: selection
```

## False Positives

- Valid requests with this exact user agent to that is used by legitimate scripts or sysadmin operations

## References

- https://rclone.org/
- https://www.kroll.com/en/insights/publications/cyber/new-m365-business-email-compromise-attacks-with-rclone

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_rclone.yml)
