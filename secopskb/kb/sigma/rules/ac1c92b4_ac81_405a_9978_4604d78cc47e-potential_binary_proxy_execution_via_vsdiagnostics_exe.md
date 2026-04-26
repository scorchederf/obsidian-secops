---
sigma_id: "ac1c92b4-ac81-405a-9978-4604d78cc47e"
title: "Potential Binary Proxy Execution Via VSDiagnostics.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_vsdiagnostics_execution_proxy.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vsdiagnostics_execution_proxy.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ac1c92b4-ac81-405a-9978-4604d78cc47e"
  - "Potential Binary Proxy Execution Via VSDiagnostics.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Binary Proxy Execution Via VSDiagnostics.EXE

Detects execution of "VSDiagnostics.exe" with the "start" command in order to launch and proxy arbitrary binaries.

## Metadata

- Rule ID: ac1c92b4-ac81-405a-9978-4604d78cc47e
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-03
- Source Path: rules/windows/process_creation/proc_creation_win_vsdiagnostics_execution_proxy.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \VSDiagnostics.exe
- OriginalFileName: VSDiagnostics.exe
selection_cli_start:
  CommandLine|contains: start
selection_cli_launch:
  CommandLine|contains:
  - ' /launch:'
  - ' -launch:'
condition: all of selection_*
```

## False Positives

- Legitimate usage for tracing and diagnostics purposes

## References

- https://twitter.com/0xBoku/status/1679200664013135872

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vsdiagnostics_execution_proxy.yml)
