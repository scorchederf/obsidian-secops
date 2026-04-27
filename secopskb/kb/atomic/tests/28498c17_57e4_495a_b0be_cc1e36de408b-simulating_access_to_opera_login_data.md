---
atomic_guid: "28498c17-57e4-495a-b0be-cc1e36de408b"
title: "Simulating access to Opera Login Data"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.003"
attack_technique_name: "Credentials from Password Stores: Credentials from Web Browsers"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "28498c17-57e4-495a-b0be-cc1e36de408b"
  - "Simulating access to Opera Login Data"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Simulating access to Opera Login Data

Simulates an adversary accessing encrypted credentials from Opera web browser's login database.

## Metadata

- Atomic GUID: 28498c17-57e4-495a-b0be-cc1e36de408b
- Technique: T1555.003: Credentials from Password Stores: Credentials from Web Browsers
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1555.003/T1555.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.003]]

## Dependencies

Opera must be installed

### Prerequisite Check

```powershell
if (((Test-Path "$env:LOCALAPPDATA\Programs\Opera\launcher.exe") -Or (Test-Path "C:\Program Files\Opera\launcher.exe") -Or (Test-Path "C:\Program Files (x86)\Opera\launcher.exe"))) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
$installer = "PathToAtomicsFolder\..\ExternalPayloads\OperaStandaloneInstaller.exe"
Invoke-WebRequest -OutFile "PathToAtomicsFolder\..\ExternalPayloads\OperaStandaloneInstaller.exe" https://get.geo.opera.com/pub/opera/desktop/82.0.4227.43/win/Opera_82.0.4227.43_Setup.exe
Start-Process $installer -ArgumentList '/install /silent /launchopera=1 /setdefaultbrowser=0'
Start-Sleep -s 180
Stop-Process -Name "opera"
```

Opera login data file must exist

### Prerequisite Check

```powershell
if (Test-Path "$env:APPDATA\Opera Software\Opera Stable\Login Data") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Path "$env:APPDATA\Opera Software\Opera Stable\Login Data" -ItemType File
```

## Executor

- name: powershell

### Command

```powershell
Copy-Item "$env:APPDATA\Opera Software\Opera Stable\Login Data" -Destination "PathToAtomicsFolder\..\ExternalPayloads"
```

### Cleanup

```powershell
Remove-Item -Path "PathToAtomicsFolder\..\ExternalPayloads\Login Data" -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml)
