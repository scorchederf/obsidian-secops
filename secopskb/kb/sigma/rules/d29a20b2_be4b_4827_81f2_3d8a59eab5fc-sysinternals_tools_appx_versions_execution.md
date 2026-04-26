---
sigma_id: "d29a20b2-be4b-4827-81f2-3d8a59eab5fc"
title: "Sysinternals Tools AppX Versions Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/appmodel_runtime/win_appmodel_runtime_sysinternals_tools_appx_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appmodel_runtime/win_appmodel_runtime_sysinternals_tools_appx_execution.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "low"
logsource: "windows / appmodel-runtime"
aliases:
  - "d29a20b2-be4b-4827-81f2-3d8a59eab5fc"
  - "Sysinternals Tools AppX Versions Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Sysinternals Tools AppX Versions Execution

Detects execution of Sysinternals tools via an AppX package.
Attackers could install the Sysinternals Suite to get access to tools such as psexec and procdump to avoid detection based on System paths.

## Metadata

- Rule ID: d29a20b2-be4b-4827-81f2-3d8a59eab5fc
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-16
- Modified: 2023-09-12
- Source Path: rules/windows/builtin/appmodel_runtime/win_appmodel_runtime_sysinternals_tools_appx_execution.yml

## Logsource

- product: windows
- service: appmodel-runtime

## Detection

```yaml
selection:
  EventID: 201
  ImageName:
  - procdump.exe
  - psloglist.exe
  - psexec.exe
  - livekd.exe
  - ADExplorer.exe
condition: selection
```

## False Positives

- Legitimate usage of sysinternals applications from the Windows Store will trigger this. Apply exclusions as needed.

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/microsoft-store

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appmodel_runtime/win_appmodel_runtime_sysinternals_tools_appx_execution.yml)
