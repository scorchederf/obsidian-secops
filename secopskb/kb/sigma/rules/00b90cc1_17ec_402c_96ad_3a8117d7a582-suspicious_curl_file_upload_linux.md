---
sigma_id: "00b90cc1-17ec-402c-96ad-3a8117d7a582"
title: "Suspicious Curl File Upload - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_curl_fileupload.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_curl_fileupload.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "00b90cc1-17ec-402c-96ad-3a8117d7a582"
  - "Suspicious Curl File Upload - Linux"
attack_technique_ids:
  - "T1567"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Curl File Upload - Linux

Detects a suspicious curl process start the adds a file to a web request

## Metadata

- Rule ID: 00b90cc1-17ec-402c-96ad-3a8117d7a582
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Cedric MAURUGEON (Update)
- Date: 2022-09-15
- Modified: 2023-05-02
- Source Path: rules/linux/process_creation/proc_creation_lnx_susp_curl_fileupload.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection_img:
  Image|endswith: /curl
selection_cli:
- CommandLine|contains:
  - ' --form'
  - ' --upload-file '
  - ' --data '
  - ' --data-'
- CommandLine|re: \s-[FTd]\s
filter_optional_localhost:
  CommandLine|contains:
  - ://localhost
  - ://127.0.0.1
condition: all of selection_* and not 1 of filter_optional_*
```

## False Positives

- Scripts created by developers and admins

## References

- https://twitter.com/d1r4c/status/1279042657508081664
- https://medium.com/@petehouston/upload-files-with-curl-93064dcccc76
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1105/T1105.md#atomic-test-19---curl-upload-file
- https://curl.se/docs/manpage.html
- https://www.trendmicro.com/en_us/research/22/i/how-malicious-actors-abuse-native-linux-tools-in-their-attacks.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_curl_fileupload.yml)
