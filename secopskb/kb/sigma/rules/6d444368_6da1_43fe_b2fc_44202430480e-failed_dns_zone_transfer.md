---
sigma_id: "6d444368-6da1-43fe-b2fc-44202430480e"
title: "Failed DNS Zone Transfer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/dns_server/win_dns_server_failed_dns_zone_transfer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/dns_server/win_dns_server_failed_dns_zone_transfer.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / dns-server"
aliases:
  - "6d444368-6da1-43fe-b2fc-44202430480e"
  - "Failed DNS Zone Transfer"
attack_technique_ids:
  - "T1590.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Failed DNS Zone Transfer

Detects when a DNS zone transfer failed.

## Metadata

- Rule ID: 6d444368-6da1-43fe-b2fc-44202430480e
- Status: test
- Level: medium
- Author: Zach Mathis
- Date: 2023-05-24
- Source Path: rules/windows/builtin/dns_server/win_dns_server_failed_dns_zone_transfer.yml

## Logsource

- product: windows
- service: dns-server

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1590-gather_victim_network_information|T1590.002]]

## Detection

```yaml
selection:
  EventID: 6004
condition: selection
```

## False Positives

- Unlikely

## References

- https://kb.eventtracker.com/evtpass/evtpages/EventId_6004_Microsoft-Windows-DNS-Server-Service_65410.asp

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/dns_server/win_dns_server_failed_dns_zone_transfer.yml)
