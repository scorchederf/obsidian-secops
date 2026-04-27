---
atomic_guid: "69435dcf-c66f-4ec0-a8b1-82beb76b34db"
title: "Disable Windows IIS HTTP Logging"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.002"
attack_technique_name: "Impair Defenses: Disable Windows Event Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "69435dcf-c66f-4ec0-a8b1-82beb76b34db"
  - "Disable Windows IIS HTTP Logging"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Disables HTTP logging on a Windows IIS web server as seen by Threat Group 3390 (Bronze Union).
This action requires HTTP logging configurations in IIS to be unlocked.

Use the cleanup commands to restore some default auditpol settings (your original settings will be lost)

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]

## Input Arguments

### website_name

- description: The name of the website on a server
- type: string
- default: Default Web Site

## Executor

- name: powershell

### Command

```powershell
C:\Windows\System32\inetsrv\appcmd.exe set config "#{website_name}" /section:httplogging /dontLog:true
```

### Cleanup

```powershell
if(Test-Path "C:\Windows\System32\inetsrv\appcmd.exe"){
  C:\Windows\System32\inetsrv\appcmd.exe set config "#{website_name}" /section:httplogging /dontLog:false *>$null
}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.yaml)
