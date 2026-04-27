---
atomic_guid: "5295bd61-bd7e-4744-9d52-85962a4cf2d6"
title: "Remote Code Execution with PS Credentials Using Invoke-Command"
framework: "atomic"
generated: "true"
attack_technique_id: "T1021.006"
attack_technique_name: "Remote Services: Windows Remote Management"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.006/T1021.006.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "5295bd61-bd7e-4744-9d52-85962a4cf2d6"
  - "Remote Code Execution with PS Credentials Using Invoke-Command"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Simulate lateral movement with PowerShell Remoting on the local host. 
Upon successful execution, PowerShell will execute `whoami` using `Invoke-Command`, targeting the 
local machine as remote target.

## ATT&CK Mapping

- [[kb/attack/techniques/T1021-remote_services#^t1021006-windows-remote-management|T1021.006: Windows Remote Management]]

## Executor

- name: powershell

### Command

```powershell
Enable-PSRemoting -Force
Invoke-Command -ComputerName $env:COMPUTERNAME -ScriptBlock {whoami}
```

### Cleanup

```powershell
Disable-PSRemoting -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.006/T1021.006.yaml)
