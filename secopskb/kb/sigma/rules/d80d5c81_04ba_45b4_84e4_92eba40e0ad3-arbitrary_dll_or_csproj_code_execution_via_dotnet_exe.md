---
sigma_id: "d80d5c81-04ba-45b4-84e4-92eba40e0ad3"
title: "Arbitrary DLL or Csproj Code Execution Via Dotnet.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dotnet_arbitrary_dll_csproj_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dotnet_arbitrary_dll_csproj_execution.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d80d5c81-04ba-45b4-84e4-92eba40e0ad3"
  - "Arbitrary DLL or Csproj Code Execution Via Dotnet.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Arbitrary DLL or Csproj Code Execution Via Dotnet.EXE

Detects execution of arbitrary DLLs or unsigned code via a ".csproj" files via Dotnet.EXE.

## Metadata

- Rule ID: d80d5c81-04ba-45b4-84e4-92eba40e0ad3
- Status: test
- Level: medium
- Author: Beyu Denis, oscd.community
- Date: 2020-10-18
- Modified: 2025-10-08
- Source Path: rules/windows/process_creation/proc_creation_win_dotnet_arbitrary_dll_csproj_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \dotnet.exe
- OriginalFileName: .NET Host
selection_cli:
  CommandLine|endswith:
  - .csproj
  - .csproj"
  - .dll
  - .dll"
  - .csproj'
  - .dll'
filter_optional_notepadplus_plus:
  ParentImage:
  - C:\Program Files (x86)\Notepad++\notepad++.exe
  - C:\Program Files\Notepad++\notepad++.exe
  CommandLine|contains|all:
  - C:\ProgramData\CSScriptNpp\
  - '-cscs_path:'
  - \cs-script\cscs.dll
condition: all of selection_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate administrator usage

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Dotnet/
- https://twitter.com/_felamos/status/1204705548668555264
- https://bohops.com/2019/08/19/dotnet-core-a-vector-for-awl-bypass-defense-evasion/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dotnet_arbitrary_dll_csproj_execution.yml)
