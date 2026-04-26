---
atomic_guid: "a6a5ec26-a2d1-4109-9d35-58b867689329"
title: "Simulating access to Windows Edge Login Data"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.003"
attack_technique_name: "Credentials from Password Stores: Credentials from Web Browsers"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "a6a5ec26-a2d1-4109-9d35-58b867689329"
  - "Simulating access to Windows Edge Login Data"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Simulating access to Windows Edge Login Data

Simulates an adversary accessing encrypted credentials from Edge web browser's login database.
more info in https://www.forensicfocus.com/articles/chromium-based-microsoft-edge-from-a-forensic-point-of-view/

## Metadata

- Atomic GUID: a6a5ec26-a2d1-4109-9d35-58b867689329
- Technique: T1555.003: Credentials from Password Stores: Credentials from Web Browsers
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1555.003/T1555.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.003]]

## Dependencies

Edge must be installed

### Prerequisite Check

```powershell
if (Test-Path "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
"Installation is not implemented as Edge is a part of windows"
```

Edge login data file must exist

### Prerequisite Check

```powershell
if (Test-Path "$env:LOCALAPPDATA\Microsoft\Edge\User Data\Default") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
$edge="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
Start-Process $edge 
Start-Sleep -s 20
Stop-Process -Name msedge
```

## Executor

- name: powershell

### Command

```powershell
Copy-Item "$env:LOCALAPPDATA\Microsoft\Edge\User Data\Default" -Destination "PathToAtomicsFolder\..\ExternalPayloads\Edge" -Force -Recurse
```

### Cleanup

```powershell
Remove-Item -Path "PathToAtomicsFolder\..\ExternalPayloads\Edge" -Force -ErrorAction Ignore -Recurse
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml)
