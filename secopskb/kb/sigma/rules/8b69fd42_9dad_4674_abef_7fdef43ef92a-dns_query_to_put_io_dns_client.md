---
sigma_id: "8b69fd42-9dad-4674-abef-7fdef43ef92a"
title: "DNS Query To Put.io - DNS Client"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/dns_client/win_dns_client_put_io.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/dns_client/win_dns_client_put_io.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / dns-client"
aliases:
  - "8b69fd42-9dad-4674-abef-7fdef43ef92a"
  - "DNS Query To Put.io - DNS Client"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DNS Query To Put.io - DNS Client

Detects DNS queries for subdomains related to "Put.io" sharing website.

## Metadata

- Rule ID: 8b69fd42-9dad-4674-abef-7fdef43ef92a
- Status: test
- Level: medium
- Author: Omar Khaled (@beacon_exe)
- Date: 2024-08-23
- Source Path: rules/windows/builtin/dns_client/win_dns_client_put_io.yml

## Logsource

- definition: Requirements: Microsoft-Windows-DNS Client Events/Operational Event Log must be enabled/collected in order to receive the events.
- product: windows
- service: dns-client

## Detection

```yaml
selection:
  EventID: 3008
  QueryName|contains:
  - api.put.io
  - upload.put.io
condition: selection
```

## False Positives

- Legitimate DNS queries and usage of Put.io

## References

- https://darkatlas.io/blog/medusa-ransomware-group-opsec-failure

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/dns_client/win_dns_client_put_io.yml)
