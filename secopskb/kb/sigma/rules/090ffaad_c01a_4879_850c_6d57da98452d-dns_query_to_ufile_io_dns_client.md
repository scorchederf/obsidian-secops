---
sigma_id: "090ffaad-c01a-4879-850c-6d57da98452d"
title: "DNS Query To Ufile.io - DNS Client"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/dns_client/win_dns_client_ufile_io.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/dns_client/win_dns_client_ufile_io.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "low"
logsource: "windows / dns-client"
aliases:
  - "090ffaad-c01a-4879-850c-6d57da98452d"
  - "DNS Query To Ufile.io - DNS Client"
attack_technique_ids:
  - "T1567.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DNS Query To Ufile.io - DNS Client

Detects DNS queries to "ufile.io", which was seen abused by malware and threat actors as a method for data exfiltration

## Metadata

- Rule ID: 090ffaad-c01a-4879-850c-6d57da98452d
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-16
- Modified: 2023-09-18
- Source Path: rules/windows/builtin/dns_client/win_dns_client_ufile_io.yml

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
  QueryName|contains: ufile.io
condition: selection
```

## False Positives

- DNS queries for "ufile" are not malicious by nature necessarily. Investigate the source to determine the necessary actions to take

## References

- https://thedfirreport.com/2021/12/13/diavol-ransomware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/dns_client/win_dns_client_ufile_io.yml)
