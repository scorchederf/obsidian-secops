---
sigma_id: "df68f791-ad95-447f-a271-640a0dab9cf8"
title: "DNS Query Request To OneLaunch Update Service"
framework: "sigma"
generated: "true"
source_path: "rules/windows/dns_query/dns_query_win_onelaunch_update_service.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_onelaunch_update_service.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "low"
logsource: "windows / dns_query"
aliases:
  - "df68f791-ad95-447f-a271-640a0dab9cf8"
  - "DNS Query Request To OneLaunch Update Service"
attack_technique_ids:
  - "T1056"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DNS Query Request To OneLaunch Update Service

Detects DNS query requests to "update.onelaunch.com". This domain is associated with the OneLaunch adware application.
When the OneLaunch application is installed it will attempt to get updates from this domain.

## Metadata

- Rule ID: df68f791-ad95-447f-a271-640a0dab9cf8
- Status: test
- Level: low
- Author: Josh Nickels
- Date: 2024-02-26
- Source Path: rules/windows/dns_query/dns_query_win_onelaunch_update_service.yml

## Logsource

- category: dns_query
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1056-input_capture|T1056]]

## Detection

```yaml
selection:
  QueryName: update.onelaunch.com
  Image|endswith: \OneLaunch.exe
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.malwarebytes.com/blog/detections/pup-optional-onelaunch-silentcf
- https://www.myantispyware.com/2020/12/14/how-to-uninstall-onelaunch-browser-removal-guide/
- https://malware.guide/browser-hijacker/remove-onelaunch-virus/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_onelaunch_update_service.yml)
