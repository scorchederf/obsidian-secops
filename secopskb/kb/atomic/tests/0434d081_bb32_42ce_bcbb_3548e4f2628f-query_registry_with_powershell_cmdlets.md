---
atomic_guid: "0434d081-bb32-42ce-bcbb-3548e4f2628f"
title: "Query Registry with Powershell cmdlets"
framework: "atomic"
generated: "true"
attack_technique_id: "T1012"
attack_technique_name: "Query Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1012/T1012.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "0434d081-bb32-42ce-bcbb-3548e4f2628f"
  - "Query Registry with Powershell cmdlets"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Query Windows Registry with Powershell cmdlets, i.e., Get-Item and Get-ChildItem. The results from above can also be achieved with Get-Item and Get-ChildItem.
Unlike using "reg query" which then executes reg.exe, using cmdlets won't generate new processes, which may evade detection systems monitoring process generation.

## ATT&CK Mapping

- [[kb/attack/techniques/T1012-query_registry|T1012: Query Registry]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Get-Item -Path "HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows"
Get-ChildItem -Path "HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\" | findstr Windows
Get-Item -Path "HKLM:Software\Microsoft\Windows\CurrentVersion\RunServicesOnce"
Get-Item -Path "HKCU:Software\Microsoft\Windows\CurrentVersion\RunServicesOnce"
Get-Item -Path "HKLM:Software\Microsoft\Windows\CurrentVersion\RunServices"
Get-Item -Path "HKCU:Software\Microsoft\Windows\CurrentVersion\RunServices"
Get-Item -Path "HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\Notify"
Get-Item -Path "HKLM:Software\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit"
Get-Item -Path "HKCU:Software\Microsoft\Windows NT\CurrentVersion\Winlogon\\Shell"
Get-Item -Path "HKLM:Software\Microsoft\Windows NT\CurrentVersion\Winlogon\\Shell"
Get-Item -Path "HKLM:SOFTWARE\Microsoft\Windows\CurrentVersion\ShellServiceObjectDelayLoad"
Get-Item -Path "HKLM:Software\Microsoft\Windows\CurrentVersion\RunOnce"
Get-Item -Path "HKLM:Software\Microsoft\Windows\CurrentVersion\RunOnceEx"
Get-Item -Path "HKLM:Software\Microsoft\Windows\CurrentVersion\Run"
Get-Item -Path "HKCU:Software\Microsoft\Windows\CurrentVersion\Run"
Get-Item -Path "HKCU:Software\Microsoft\Windows\CurrentVersion\RunOnce"
Get-Item -Path "HKLM:Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run"
Get-Item -Path "HKCU:Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run"
Get-ChildItem -Path "HKLM:system\currentcontrolset\services" 
Get-Item -Path "HKLM:Software\Microsoft\Windows\CurrentVersion\Run"
Get-Item -Path "HKLM:SYSTEM\CurrentControlSet\Control\SafeBoot"
Get-ChildItem -Path "HKLM:SOFTWARE\Microsoft\Active Setup\Installed Components"
Get-ChildItem -Path "HKLM:SOFTWARE\Microsoft\Windows\CurrentVersion\Group Policy\Scripts\Startup"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1012/T1012.yaml)
