---
atomic_guid: "fe94a1c3-3e22-4dc9-9fdf-3a8bdbc10dc4"
title: "List Process Main Windows - C# .NET"
framework: "atomic"
generated: "true"
attack_technique_id: "T1010"
attack_technique_name: "Application Window Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1010/T1010.yaml"
build_date: "2026-04-27 19:12:25"
executor: "command_prompt"
aliases:
  - "fe94a1c3-3e22-4dc9-9fdf-3a8bdbc10dc4"
  - "List Process Main Windows - C# .NET"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Compiles and executes C# code to list main window titles associated with each process.

Upon successful execution, powershell will download the .cs from the Atomic Red Team repo, and cmd.exe will compile and execute T1010.exe. Upon T1010.exe execution, expected output will be via stdout.

## ATT&CK Mapping

- [[kb/attack/techniques/T1010-application_window_discovery|T1010: Application Window Discovery]]

## Input Arguments

### input_source_code

- description: Path to source of C# code
- type: path
- default: PathToAtomicsFolder\T1010\src\T1010.cs

### output_file_name

- description: Name of output binary
- type: string
- default: %TEMP%\T1010.exe

## Dependencies

T1010.cs must exist on disk at specified location (#{input_source_code})

### Prerequisite Check

```powershell
if (Test-Path "#{input_source_code}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{input_source_code}") -ErrorAction ignore | Out-Null
Invoke-WebRequest https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1010/src/T1010.cs -OutFile "#{input_source_code}"
```

## Executor

- name: command_prompt

### Command

```cmd
C:\Windows\Microsoft.NET\Framework\v4.0.30319\csc.exe -out:#{output_file_name} "#{input_source_code}"
#{output_file_name}
```

### Cleanup

```cmd
del /f /q /s #{output_file_name} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1010/T1010.yaml)
