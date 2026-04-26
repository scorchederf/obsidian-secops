---
atomic_guid: "b8a49f03-e3c4-40f2-b7bb-9e8f8fdddbf1"
title: "UEFI Persistence via Wpbbin.exe File Creation"
framework: "atomic"
generated: "true"
attack_technique_id: "T1542.001"
attack_technique_name: "Pre-OS Boot: System Firmware"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1542.001/T1542.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "b8a49f03-e3c4-40f2-b7bb-9e8f8fdddbf1"
  - "UEFI Persistence via Wpbbin.exe File Creation"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# UEFI Persistence via Wpbbin.exe File Creation

Creates Wpbbin.exe in %systemroot%. This technique can be used for UEFI-based pre-OS boot persistence mechanisms.
- https://grzegorztworek.medium.com/using-uefi-to-inject-executable-files-into-bitlocker-protected-drives-8ff4ca59c94c
- http://download.microsoft.com/download/8/a/2/8a2fb72d-9b96-4e2d-a559-4a27cf905a80/windows-platform-binary-table.docx
- https://github.com/tandasat/WPBT-Builder

## Metadata

- Atomic GUID: b8a49f03-e3c4-40f2-b7bb-9e8f8fdddbf1
- Technique: T1542.001: Pre-OS Boot: System Firmware
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1542.001/T1542.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1542-pre-os_boot|T1542.001]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
echo "Creating %systemroot%\wpbbin.exe"      
New-Item -ItemType File -Path "$env:SystemRoot\System32\wpbbin.exe"
```

### Cleanup

```powershell
echo "Removing %systemroot%\wpbbin.exe" 
Remove-Item -Path "$env:SystemRoot\System32\wpbbin.exe"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1542.001/T1542.001.yaml)
