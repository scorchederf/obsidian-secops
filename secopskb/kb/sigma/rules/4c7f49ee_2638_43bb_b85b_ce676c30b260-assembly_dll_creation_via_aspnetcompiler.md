---
sigma_id: "4c7f49ee-2638-43bb-b85b-ce676c30b260"
title: "Assembly DLL Creation Via AspNetCompiler"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_aspnet_temp_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_aspnet_temp_files.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "4c7f49ee-2638-43bb-b85b-ce676c30b260"
  - "Assembly DLL Creation Via AspNetCompiler"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Assembly DLL Creation Via AspNetCompiler

Detects the creation of new DLL assembly files by "aspnet_compiler.exe", which could be a sign of "aspnet_compiler" abuse to proxy execution through a build provider.

## Metadata

- Rule ID: 4c7f49ee-2638-43bb-b85b-ce676c30b260
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-14
- Source Path: rules/windows/file/file_event/file_event_win_aspnet_temp_files.yml

## Logsource

- category: file_event
- product: windows

## Detection

```yaml
selection:
  Image|endswith: \aspnet_compiler.exe
  TargetFilename|contains|all:
  - \Temporary ASP.NET Files\
  - \assembly\tmp\
  - .dll
condition: selection
```

## False Positives

- Legitimate assembly compilation using a build provider

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_aspnet_temp_files.yml)
