---
sigma_id: "53d8d3e1-ca33-4012-adf3-e05a4d652e34"
title: "Process Memory Dump Via Dotnet-Dump"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dotnetdump_memory_dump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dotnetdump_memory_dump.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "53d8d3e1-ca33-4012-adf3-e05a4d652e34"
  - "Process Memory Dump Via Dotnet-Dump"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Process Memory Dump Via Dotnet-Dump

Detects the execution of "dotnet-dump" with the "collect" flag. The execution could indicate potential process dumping of critical processes such as LSASS.

## Metadata

- Rule ID: 53d8d3e1-ca33-4012-adf3-e05a4d652e34
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-03-14
- Source Path: rules/windows/process_creation/proc_creation_win_dotnetdump_memory_dump.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \dotnet-dump.exe
- OriginalFileName: dotnet-dump.dll
selection_cli:
  CommandLine|contains: collect
condition: all of selection_*
```

## False Positives

- Process dumping is the expected behavior of the tool. So false positives are expected in legitimate usage. The PID/Process Name of the process being dumped needs to be investigated

## References

- https://learn.microsoft.com/en-us/dotnet/core/diagnostics/dotnet-dump#dotnet-dump-collect
- https://twitter.com/bohops/status/1635288066909966338

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dotnetdump_memory_dump.yml)
