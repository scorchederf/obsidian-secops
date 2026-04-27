---
atomic_guid: "bfe6ac15-c50b-4c4f-a186-0fc6b8ba936c"
title: "Office Application Startup - Outlook as a C2"
framework: "atomic"
generated: "true"
attack_technique_id: "T1137"
attack_technique_name: "Office Application Startup"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137/T1137.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "bfe6ac15-c50b-4c4f-a186-0fc6b8ba936c"
  - "Office Application Startup - Outlook as a C2"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Office Application Startup - Outlook as a C2

As outlined in MDSEC's Blog post https://www.mdsec.co.uk/2020/11/a-fresh-outlook-on-mail-based-persistence/ 
it is possible to use Outlook Macro as a way to achieve persistance and execute arbitrary commands. This transform Outlook into a C2.
Too achieve this two things must happened on the syste
- The macro security registry value must be set to '1'
- A file called VbaProject.OTM must be created in the Outlook Folder.

## Metadata

- Atomic GUID: bfe6ac15-c50b-4c4f-a186-0fc6b8ba936c
- Technique: T1137: Office Application Startup
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1137/T1137.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1137-office_application_startup|T1137]]

## Executor

- name: command_prompt

### Command

```cmd
reg add "HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Outlook\Security" /v Level /t REG_DWORD /d 1 /f
mkdir  %APPDATA%\Microsoft\Outlook\ >nul 2>&1
echo "Atomic Red Team TEST" > %APPDATA%\Microsoft\Outlook\VbaProject.OTM
```

### Cleanup

```cmd
reg delete "HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Outlook\Security" /v Level /f >nul 2>&1
del %APPDATA%\Microsoft\Outlook\VbaProject.OTM >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137/T1137.yaml)
