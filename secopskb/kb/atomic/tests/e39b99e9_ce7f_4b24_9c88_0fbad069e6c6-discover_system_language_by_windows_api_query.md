---
atomic_guid: "e39b99e9-ce7f-4b24-9c88-0fbad069e6c6"
title: "Discover System Language by Windows API Query"
framework: "atomic"
generated: "true"
attack_technique_id: "T1614.001"
attack_technique_name: "System Location Discovery: System Language Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "e39b99e9-ce7f-4b24-9c88-0fbad069e6c6"
  - "Discover System Language by Windows API Query"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test executes a custom script called LanguageKeyboardLayout.exe which outputs the values of the following Windows API functions to the user terminal: 

`GetKeyboardLayout`, `GetKeyboardLayoutList`, `GetUserDefaultUILanguage`, `GetSystemDefaultUILanguage`, `GetUserDefaultLangID`.

Documentation for these functions is located [here](https://learn.microsoft.com/en-us/windows/win32/api/winuser/).

## ATT&CK Mapping

- [[kb/attack/techniques/T1614-system_location_discovery#^t1614001-system-language-discovery|T1614.001: System Language Discovery]]

## Dependencies

LanguageKeyboardLayout.exe must exist on disk (default location: PathToAtomicsFolder\..\ExternalPayloads\LanguageKeyboardLayout.exe)

### Prerequisite Check

```powershell
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\LanguageKeyboardLayout.exe") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "PathToAtomicsFolder\..\ExternalPayloads\LanguageKeyboardLayout.exe") -ErrorAction Ignore | Out-Null
Invoke-WebRequest -Uri "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1614.001/bin/LanguageKeyboardLayout.exe" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\LanguageKeyboardLayout.exe"
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
PathToAtomicsFolder\..\ExternalPayloads\LanguageKeyboardLayout.exe
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml)
