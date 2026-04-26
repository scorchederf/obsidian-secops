---
sigma_id: "ea34fb97-e2c4-4afb-810f-785e4459b194"
title: "Curl Usage on Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_curl_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_curl_usage.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "ea34fb97-e2c4-4afb-810f-785e4459b194"
  - "Curl Usage on Linux"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Curl Usage on Linux

Detects a curl process start on linux, which indicates a file download from a remote location or a simple web request to a remote server

## Metadata

- Rule ID: ea34fb97-e2c4-4afb-810f-785e4459b194
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-15
- Source Path: rules/linux/process_creation/proc_creation_lnx_curl_usage.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection:
  Image|endswith: /curl
condition: selection
```

## False Positives

- Scripts created by developers and admins
- Administrative activity

## References

- https://www.trendmicro.com/en_us/research/22/i/how-malicious-actors-abuse-native-linux-tools-in-their-attacks.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_curl_usage.yml)
