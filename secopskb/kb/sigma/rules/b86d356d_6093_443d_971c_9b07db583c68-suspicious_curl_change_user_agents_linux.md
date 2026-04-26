---
sigma_id: "b86d356d-6093-443d-971c-9b07db583c68"
title: "Suspicious Curl Change User Agents - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_curl_useragent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_curl_useragent.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "b86d356d-6093-443d-971c-9b07db583c68"
  - "Suspicious Curl Change User Agents - Linux"
attack_technique_ids:
  - "T1071.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Curl Change User Agents - Linux

Detects a suspicious curl process start on linux with set useragent options

## Metadata

- Rule ID: b86d356d-6093-443d-971c-9b07db583c68
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-15
- Source Path: rules/linux/process_creation/proc_creation_lnx_susp_curl_useragent.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]

## Detection

```yaml
selection:
  Image|endswith: /curl
  CommandLine|contains:
  - ' -A '
  - ' --user-agent '
condition: selection
```

## False Positives

- Scripts created by developers and admins
- Administrative activity

## References

- https://curl.se/docs/manpage.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_curl_useragent.yml)
