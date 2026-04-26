---
atomic_guid: "adae83d3-0df6-45e7-b2c3-575f91584577"
title: "WMI Invoke-CimMethod Start Process"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546"
attack_technique_name: "Event Triggered Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546/T1546.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "adae83d3-0df6-45e7-b2c3-575f91584577"
  - "WMI Invoke-CimMethod Start Process"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WMI Invoke-CimMethod Start Process

The following Atomic will create a New-CimSession on a remote endpoint and start a process usnig Invoke-CimMethod.
This is a novel way to perform lateral movement or to start a remote process.
This does require WinRM to be enabled. The account performing the run will also need to be elevated.
A successful execution will stdout that the process started. On the remote endpoint, wmiprvse.exe will spawn the given process.

## Metadata

- Atomic GUID: adae83d3-0df6-45e7-b2c3-575f91584577
- Technique: T1546: Event Triggered Execution
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1546/T1546.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546]]

## Input Arguments

### dest

- description: destination computer name
- type: string
- default: localhost

### password

- description: password for account
- type: string
- default: P@ssword1

### process

- description: process to spawn
- type: string
- default: calc.exe

### username

- description: account to use
- type: string
- default: Administrator

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
# Set the remote computer name and credentials
 $RemoteComputer = "#{dest}"
 $PWord = ConvertTo-SecureString -String "#{password}" -AsPlainText -Force
 $Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{username}", $Pword

 # Create a CIM session
 $CimSession = New-CimSession -ComputerName $RemoteComputer -Credential $Credential

 # Define the process you want to start
 $ProcessToStart = "#{process}"

 # Invoke the Create method on the Win32_Process class to start the process
 $Result = Invoke-CimMethod -CimSession $CimSession -ClassName Win32_Process -MethodName Create -Arguments @{CommandLine = $ProcessToStart}

 # Check the result
 if ($Result.ReturnValue -eq 0) {
     Write-Host "Process started successfully with Process ID: $($Result.ProcessId)"
 } else {
     Write-Host "Failed to start the process. Error code: $($Result.ReturnValue)"
 }

 # Clean up the CIM session
 Remove-CimSession -CimSession $CimSession
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546/T1546.yaml)
