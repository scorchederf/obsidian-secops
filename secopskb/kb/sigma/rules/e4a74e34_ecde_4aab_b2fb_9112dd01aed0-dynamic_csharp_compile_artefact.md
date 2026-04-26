---
sigma_id: "e4a74e34-ecde-4aab-b2fb-9112dd01aed0"
title: "Dynamic CSharp Compile Artefact"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_csharp_compile_artefact.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_csharp_compile_artefact.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "low"
logsource: "windows / file_event"
aliases:
  - "e4a74e34-ecde-4aab-b2fb-9112dd01aed0"
  - "Dynamic CSharp Compile Artefact"
attack_technique_ids:
  - "T1027.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Dynamic CSharp Compile Artefact

When C# is compiled dynamically, a .cmdline file will be created as a part of the process.
Certain processes are not typically observed compiling C# code, but can do so without touching disk.
This can be used to unpack a payload for execution

## Metadata

- Rule ID: e4a74e34-ecde-4aab-b2fb-9112dd01aed0
- Status: test
- Level: low
- Author: frack113
- Date: 2022-01-09
- Modified: 2023-02-17
- Source Path: rules/windows/file/file_event/file_event_win_csharp_compile_artefact.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.004]]

## Detection

```yaml
selection:
  TargetFilename|endswith: .cmdline
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1027.004/T1027.004.md#atomic-test-2---dynamic-c-compile

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_csharp_compile_artefact.yml)
