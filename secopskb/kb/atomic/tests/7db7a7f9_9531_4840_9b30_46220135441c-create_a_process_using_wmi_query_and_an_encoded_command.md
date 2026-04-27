---
atomic_guid: "7db7a7f9-9531-4840-9b30-46220135441c"
title: "Create a Process using WMI Query and an Encoded Command"
framework: "atomic"
generated: "true"
attack_technique_id: "T1047"
attack_technique_name: "Windows Management Instrumentation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "7db7a7f9-9531-4840-9b30-46220135441c"
  - "Create a Process using WMI Query and an Encoded Command"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Create a Process using WMI Query and an Encoded Command

Solarigate persistence is achieved via backdoors deployed via various techniques including using PowerShell with an EncodedCommand
 Powershell -nop -exec bypass -EncodedCommand <encoded command>
Where the –EncodedCommand, once decoded, would resemble:
  Invoke-WMIMethod win32_process -name create -argumentlist ‘rundll32 c:\windows\idmu\common\ypprop.dll _XInitImageFuncPtrs’ -ComputerName WORKSTATION
The EncodedCommand in this atomic is the following: Invoke-WmiMethod -Path win32_process -Name create -ArgumentList notepad.exe
You should expect to see notepad.exe running after execution of this test.
[Solarigate Analysis from Microsoft](https://www.microsoft.com/security/blog/2020/12/18/analyzing-solorigate-the-compromised-dll-file-that-started-a-sophisticated-cyberattack-and-how-microsoft-defender-helps-protect/)

## Metadata

- Atomic GUID: 7db7a7f9-9531-4840-9b30-46220135441c
- Technique: T1047: Windows Management Instrumentation
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1047/T1047.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Executor

- name: command_prompt

### Command

```cmd
powershell -exec bypass -e SQBuAHYAbwBrAGUALQBXAG0AaQBNAGUAdABoAG8AZAAgAC0AUABhAHQAaAAgAHcAaQBuADMAMgBfAHAAcgBvAGMAZQBzAHMAIAAtAE4AYQBtAGUAIABjAHIAZQBhAHQAZQAgAC0AQQByAGcAdQBtAGUAbgB0AEwAaQBzAHQAIABuAG8AdABlAHAAYQBkAC4AZQB4AGUA
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1047/T1047.yaml)
