---
sigma_id: "c3a99af4-35a9-4668-879e-c09aeb4f2bdf"
title: "Rundll32 Execution With Uncommon DLL Extension"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_uncommon_dll_extension.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_uncommon_dll_extension.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c3a99af4-35a9-4668-879e-c09aeb4f2bdf"
  - "Rundll32 Execution With Uncommon DLL Extension"
attack_technique_ids:
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Rundll32 Execution With Uncommon DLL Extension

Detects the execution of rundll32 with a command line that doesn't contain a common extension

## Metadata

- Rule ID: c3a99af4-35a9-4668-879e-c09aeb4f2bdf
- Status: test
- Level: medium
- Author: Tim Shelton, Florian Roth (Nextron Systems), Yassine Oukessou
- Date: 2022-01-13
- Modified: 2024-04-04
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_uncommon_dll_extension.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detection

```yaml
selection:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
filter_main_null:
  CommandLine: null
filter_main_empty:
  CommandLine: ''
filter_main_known_extension:
- CommandLine|contains:
  - '.cpl '
  - .cpl,
  - .cpl"
  - .cpl'
  - '.dll '
  - .dll,
  - .dll"
  - .dll'
  - '.inf '
  - .inf,
  - .inf"
  - .inf'
- CommandLine|endswith:
  - .cpl
  - .dll
  - '.inf'
filter_main_localserver:
  CommandLine|contains: ' -localserver '
filter_main_zzzzInvokeManagedCustomActionOutOfProc:
  ParentImage|endswith: \msiexec.exe
  CommandLine|contains|all:
  - :\Windows\Installer\
  - .tmp
  - zzzzInvokeManagedCustomActionOutOfProc
filter_optional_EdgeUpdate:
  ParentCommandLine|contains|all:
  - :\Users\
  - \AppData\Local\Microsoft\EdgeUpdate\Install\{
  - \EDGEMITMP_
  - .tmp\setup.exe
  - --install-archive=
  - --previous-version=
  - --msedgewebview --verbose-logging --do-not-launch-msedge --user-level
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://twitter.com/mrd0x/status/1481630810495139841?s=12

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_uncommon_dll_extension.yml)
