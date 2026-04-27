---
atomic_guid: "5295bd61-bd7e-4744-9d52-85962a4cf2d6"
title: "Remote Code Execution with PS Credentials Using Invoke-Command"
framework: "atomic"
generated: "true"
attack_technique_id: "T1021.006"
attack_technique_name: "Remote Services: Windows Remote Management"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.006/T1021.006.yaml"
build_date: "2026-04-26 17:02:12"
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

# Remote Code Execution with PS Credentials Using Invoke-Command

Simulate lateral movement with PowerShell Remoting on the local host. 
Upon successful execution, PowerShell will execute `whoami` using `Invoke-Command`, targeting the 
local machine as remote target.

## Metadata

- Atomic GUID: 5295bd61-bd7e-4744-9d52-85962a4cf2d6
- Technique: T1021.006: Remote Services: Windows Remote Management
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1021.006/T1021.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1021-remote_services|T1021.006]]

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
