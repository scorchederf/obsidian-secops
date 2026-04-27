---
atomic_guid: "7b5d350e-f758-43cc-a761-8e3f6b052a03"
title: "AutoHotKey script execution"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.010"
attack_technique_name: "Command and Scripting Interpreter: AutoHotKey & AutoIT"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.010/T1059.010.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "7b5d350e-f758-43cc-a761-8e3f6b052a03"
  - "AutoHotKey script execution"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# AutoHotKey script execution

An adversary may attempt to execute malicious script using AutoHotKey software instead of regular terminal like powershell or cmd. A messagebox will be displayed and calculator will popup when the script is executed successfully

## Metadata

- Atomic GUID: 7b5d350e-f758-43cc-a761-8e3f6b052a03
- Technique: T1059.010: Command and Scripting Interpreter: AutoHotKey & AutoIT
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1059.010/T1059.010.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.010]]

## Input Arguments

### autohotkey_path

- description: AutoHotKey Executable File Path
- type: path
- default: $PathToAtomicsFolder\..\ExternalPayloads\ahk\AutoHotKeyU64.exe

### script_path

- description: AutoHotKey Script Path
- type: path
- default: PathToAtomicsFolder\T1059.010\src\calc.ahk

## Dependencies

AutoHotKey executable file must exist on disk at the specified location (#{autohotkey_path})

### Prerequisite Check

```powershell
if(Test-Path "#{autohotkey_path}") {
    exit 0
} else {
    exit 1
}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
$AutoHotKeyURL = "https://www.autohotkey.com/download/ahk.zip"
$InstallerPath = "$PathToAtomicsFolder\..\ExternalPayloads"
Invoke-WebRequest -Uri $AutoHotKeyURL -OutFile $InstallerPath\ahk.zip
Expand-Archive -Path $InstallerPath -Force;
```

## Executor

- name: powershell

### Command

```powershell
Start-Process -FilePath "#{autohotkey_path}" -ArgumentList "#{script_path}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.010/T1059.010.yaml)
