---
atomic_guid: "24136435-c91a-4ede-9da1-8b284a1c1a23"
title: "Masquerading - wscript.exe running as svchost.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1036.003"
attack_technique_name: "Masquerading: Rename System Utilities"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.003/T1036.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "24136435-c91a-4ede-9da1-8b284a1c1a23"
  - "Masquerading - wscript.exe running as svchost.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Masquerading - wscript.exe running as svchost.exe

Copies wscript.exe, renames it, and launches it to masquerade as an instance of svchost.exe.

Upon execution, no windows will remain open but wscript will have been renamed to svchost and ran out of the temp folder

## Metadata

- Atomic GUID: 24136435-c91a-4ede-9da1-8b284a1c1a23
- Technique: T1036.003: Masquerading: Rename System Utilities
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1036.003/T1036.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

## Dependencies

Wscript file to execute must exist on disk

### Prerequisite Check

```text
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\T1036.003\src\T1036.003_masquerading.vbs") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory (split-path "PathToAtomicsFolder\..\ExternalPayloads\T1036.003\src\T1036.003_masquerading.vbs") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1036.003/src/T1036.003_masquerading.vbs" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\T1036.003\src\T1036.003_masquerading.vbs"
```

## Executor

- name: command_prompt

### Command

```commandprompt
copy %SystemRoot%\System32\wscript.exe %APPDATA%\svchost.exe /Y
cmd.exe /c %APPDATA%\svchost.exe "PathToAtomicsFolder\..\ExternalPayloads\T1036.003\src\T1036.003_masquerading.vbs"
```

### Cleanup

```commandprompt
del /Q /F %APPDATA%\svchost.exe >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.003/T1036.003.yaml)
