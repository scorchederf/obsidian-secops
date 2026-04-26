---
sigma_id: "13db8d2e-7723-4c2c-93c1-a4d36994f7ef"
title: "Potential In-Memory Download And Compile Of Payloads"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_susp_in_memory_download_and_compile.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_susp_in_memory_download_and_compile.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "13db8d2e-7723-4c2c-93c1-a4d36994f7ef"
  - "Potential In-Memory Download And Compile Of Payloads"
attack_technique_ids:
  - "T1059.007"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential In-Memory Download And Compile Of Payloads

Detects potential in-memory downloading and compiling of applets using curl and osacompile as seen used by XCSSET malware

## Metadata

- Rule ID: 13db8d2e-7723-4c2c-93c1-a4d36994f7ef
- Status: test
- Level: medium
- Author: Sohan G (D4rkCiph3r), Red Canary (idea)
- Date: 2023-08-22
- Source Path: rules/macos/process_creation/proc_creation_macos_susp_in_memory_download_and_compile.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.007]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - osacompile
  - curl
condition: selection
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/mac-application-bundles/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_susp_in_memory_download_and_compile.yml)
