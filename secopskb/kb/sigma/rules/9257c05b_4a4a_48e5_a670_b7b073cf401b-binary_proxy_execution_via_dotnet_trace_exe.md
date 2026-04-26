---
sigma_id: "9257c05b-4a4a-48e5-a670-b7b073cf401b"
title: "Binary Proxy Execution Via Dotnet-Trace.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dotnet_trace_lolbin_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dotnet_trace_lolbin_execution.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9257c05b-4a4a-48e5-a670-b7b073cf401b"
  - "Binary Proxy Execution Via Dotnet-Trace.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Binary Proxy Execution Via Dotnet-Trace.EXE

Detects commandline arguments for executing a child process via dotnet-trace.exe

## Metadata

- Rule ID: 9257c05b-4a4a-48e5-a670-b7b073cf401b
- Status: test
- Level: medium
- Author: Jimmy Bayne (@bohops)
- Date: 2024-01-02
- Source Path: rules/windows/process_creation/proc_creation_win_dotnet_trace_lolbin_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \dotnet-trace.exe
- OriginalFileName: dotnet-trace.dll
selection_cli:
  CommandLine|contains|all:
  - '-- '
  - collect
condition: all of selection_*
```

## False Positives

- Legitimate usage of the utility in order to debug and trace a program.

## References

- https://twitter.com/bohops/status/1740022869198037480

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dotnet_trace_lolbin_execution.yml)
