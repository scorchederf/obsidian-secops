---
sigma_id: "22e58743-4ac8-4a9f-bf19-00a0428d8c5f"
title: "Base64 MZ Header In CommandLine"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_inline_base64_mz_header.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_inline_base64_mz_header.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "22e58743-4ac8-4a9f-bf19-00a0428d8c5f"
  - "Base64 MZ Header In CommandLine"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects encoded base64 MZ header in the commandline

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  CommandLine|contains:
  - TVqQAAMAAAAEAAAA
  - TVpQAAIAAAAEAA8A
  - TVqAAAEAAAAEABAA
  - TVoAAAAAAAAAAAAA
  - TVpTAQEAAAAEAAAA
condition: selection
```

## False Positives

- Unlikely

## References

- https://thedfirreport.com/2022/07/11/select-xmrig-from-sqlserver/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_inline_base64_mz_header.yml)
