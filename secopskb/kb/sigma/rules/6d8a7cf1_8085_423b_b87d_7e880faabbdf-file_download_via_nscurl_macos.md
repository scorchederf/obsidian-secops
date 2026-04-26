---
sigma_id: "6d8a7cf1-8085-423b-b87d-7e880faabbdf"
title: "File Download Via Nscurl - MacOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_nscurl_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_nscurl_usage.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "6d8a7cf1-8085-423b-b87d-7e880faabbdf"
  - "File Download Via Nscurl - MacOS"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File Download Via Nscurl - MacOS

Detects the execution of the nscurl utility in order to download files.

## Metadata

- Rule ID: 6d8a7cf1-8085-423b-b87d-7e880faabbdf
- Status: test
- Level: medium
- Author: Daniel Cortez
- Date: 2024-06-04
- Source Path: rules/macos/process_creation/proc_creation_macos_nscurl_usage.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection:
  Image|endswith: /nscurl
  CommandLine|contains:
  - '--download '
  - '--download-directory '
  - '--output '
  - '-dir '
  - '-dl '
  - -ld
  - '-o '
condition: selection
```

## False Positives

- Legitimate usage of nscurl by administrators and users.

## References

- https://www.loobins.io/binaries/nscurl/
- https://www.agnosticdev.com/content/how-diagnose-app-transport-security-issues-using-nscurl-and-openssl
- https://gist.github.com/nasbench/ca6ef95db04ae04ffd1e0b1ce709cadd

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_nscurl_usage.yml)
