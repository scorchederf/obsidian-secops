---
sigma_id: "719c22d7-c11a-4f2c-93a6-2cfdd5412f68"
title: "Decode Base64 Encoded Text -MacOs"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_base64_decode.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_base64_decode.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "low"
logsource: "macos / process_creation"
aliases:
  - "719c22d7-c11a-4f2c-93a6-2cfdd5412f68"
  - "Decode Base64 Encoded Text -MacOs"
attack_technique_ids:
  - "T1027"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Decode Base64 Encoded Text -MacOs

Detects usage of base64 utility to decode arbitrary base64-encoded text

## Metadata

- Rule ID: 719c22d7-c11a-4f2c-93a6-2cfdd5412f68
- Status: test
- Level: low
- Author: Daniil Yugoslavskiy, oscd.community
- Date: 2020-10-19
- Modified: 2022-11-26
- Source Path: rules/macos/process_creation/proc_creation_macos_base64_decode.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

## Detection

```yaml
selection:
  Image: /usr/bin/base64
  CommandLine|contains: -d
condition: selection
```

## False Positives

- Legitimate activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1027/T1027.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_base64_decode.yml)
