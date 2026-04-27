---
atomic_guid: "8549ad4b-b5df-4a2d-a3d7-2aee9e7052a3"
title: "DLL Search Order Hijacking - amsi.dll"
framework: "atomic"
generated: "true"
attack_technique_id: "T1574.001"
attack_technique_name: "Hijack Execution Flow: DLL"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.001/T1574.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "8549ad4b-b5df-4a2d-a3d7-2aee9e7052a3"
  - "DLL Search Order Hijacking - amsi.dll"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Adversaries can take advantage of insecure library loading by PowerShell to load a vulnerable version of amsi.dll in order to bypass AMSI (Anti-Malware Scanning Interface)
https://enigma0x3.net/2017/07/19/bypassing-amsi-via-com-server-hijacking/

Upon successful execution, powershell.exe will be copied and renamed to updater.exe and load amsi.dll from a non-standard path.

## ATT&CK Mapping

- [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
copy %windir%\System32\windowspowershell\v1.0\powershell.exe %APPDATA%\updater.exe
copy %windir%\System32\amsi.dll %APPDATA%\amsi.dll
%APPDATA%\updater.exe -Command exit
```

### Cleanup

```cmd
del %APPDATA%\updater.exe >nul 2>&1
del %APPDATA%\amsi.dll >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.001/T1574.001.yaml)
