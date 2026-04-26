---
sigma_id: "66474410-b883-415f-9f8d-75345a0a66a6"
title: "DNS Query To MEGA Hosting Website - DNS Client"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/dns_client/win_dns_client_mega_nz.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/dns_client/win_dns_client_mega_nz.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / dns-client"
aliases:
  - "66474410-b883-415f-9f8d-75345a0a66a6"
  - "DNS Query To MEGA Hosting Website - DNS Client"
attack_technique_ids:
  - "T1567.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DNS Query To MEGA Hosting Website - DNS Client

Detects DNS queries for subdomains related to MEGA sharing website

## Metadata

- Rule ID: 66474410-b883-415f-9f8d-75345a0a66a6
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-16
- Source Path: rules/windows/builtin/dns_client/win_dns_client_mega_nz.yml

## Logsource

- definition: Requirements: Microsoft-Windows-DNS Client Events/Operational Event Log must be enabled/collected in order to receive the events.
- product: windows
- service: dns-client

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567.002]]

## Detection

```yaml
selection:
  EventID: 3008
  QueryName|contains: userstorage.mega.co.nz
condition: selection
```

## False Positives

- Legitimate DNS queries and usage of Mega

## References

- https://research.nccgroup.com/2021/05/27/detecting-rclone-an-effective-tool-for-exfiltration/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/dns_client/win_dns_client_mega_nz.yml)
