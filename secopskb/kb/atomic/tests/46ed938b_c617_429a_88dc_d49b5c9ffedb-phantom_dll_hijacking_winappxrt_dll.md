---
atomic_guid: "46ed938b-c617-429a-88dc-d49b5c9ffedb"
title: "Phantom Dll Hijacking - WinAppXRT.dll"
framework: "atomic"
generated: "true"
attack_technique_id: "T1574.001"
attack_technique_name: "Hijack Execution Flow: DLL"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.001/T1574.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "46ed938b-c617-429a-88dc-d49b5c9ffedb"
  - "Phantom Dll Hijacking - WinAppXRT.dll"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Phantom Dll Hijacking - WinAppXRT.dll

.NET components (a couple of DLLs loaded anytime .NET apps are executed) when they are loaded they look for an environment variable called APPX_PROCESS
Setting the environmental variable and dropping the phantom WinAppXRT.dll in e.g. c:\windows\system32 (or any other location accessible via PATH) will ensure the 
WinAppXRT.dll is loaded everytime user launches an application using .NET.

Upon successful execution, amsi.dll will be copied and renamed to WinAppXRT.dll and then WinAppXRT.dll will be copied to system32 folder for loading during execution of any .NET application.

## Metadata

- Atomic GUID: 46ed938b-c617-429a-88dc-d49b5c9ffedb
- Technique: T1574.001: Hijack Execution Flow: DLL
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1574.001/T1574.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
copy %windir%\System32\amsi.dll %APPDATA%\amsi.dll
ren %APPDATA%\amsi.dll WinAppXRT.dll
copy %APPDATA%\WinAppXRT.dll %windir%\System32\WinAppXRT.dll
reg add "HKEY_CURRENT_USER\Environment" /v APPX_PROCESS /t REG_EXPAND_SZ /d "1" /f
```

### Cleanup

```cmd
reg delete "HKEY_CURRENT_USER\Environment" /v APPX_PROCESS /f
del %windir%\System32\WinAppXRT.dll
del %APPDATA%\WinAppXRT.dll
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.001/T1574.001.yaml)
