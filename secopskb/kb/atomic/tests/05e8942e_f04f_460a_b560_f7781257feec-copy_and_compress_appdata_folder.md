---
atomic_guid: "05e8942e-f04f-460a-b560-f7781257feec"
title: "Copy and Compress AppData Folder"
framework: "atomic"
generated: "true"
attack_technique_id: "T1560.001"
attack_technique_name: "Archive Collected Data: Archive via Utility"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "05e8942e-f04f-460a-b560-f7781257feec"
  - "Copy and Compress AppData Folder"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Copy and Compress AppData Folder

Copies the AppData folder, compresses it, and cleans up temporary files.

## Metadata

- Atomic GUID: 05e8942e-f04f-460a-b560-f7781257feec
- Technique: T1560.001: Archive Collected Data: Archive via Utility
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1560.001/T1560.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1560-archive_collected_data|T1560.001]]

## Input Arguments

### destination_folder

- description: Temporary copy location
- type: Path
- default: $env:USERPROFILE\Desktop\AppDataCopy

### zip_file_path

- description: ZIP archive path
- type: Path
- default: $env:USERPROFILE\Desktop\AppDataBackup.zip

## Dependencies

Requires admin and .NET compression libraries

### Prerequisite Check

```text
if (-not ([Security.Principal.WindowsPrincipal] `
    [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole(`
    [Security.Principal.WindowsBuiltInRole]::Administrator)) { exit 1 }
if (-not (Test-Path "$env:USERPROFILE\AppData")) { exit 1 }
```

### Get Prerequisite

```text
Run PowerShell as Administrator and ensure .NET compression assemblies are available.
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$AppData="$env:USERPROFILE\AppData"
$Copy="#{destination_folder}"
$Zip="#{zip_file_path}"

if (Test-Path $Copy) { Remove-Item $Copy -Recurse -Force }
New-Item -ItemType Directory -Path $Copy | Out-Null

Get-ChildItem $AppData -Recurse -Force | ForEach-Object {
  $rel = $_.FullName.Substring($AppData.Length + 1)
  $dest = Join-Path $Copy $rel
  if ($_.PSIsContainer) { New-Item -ItemType Directory -Path $dest -Force | Out-Null }
  else { Copy-Item $_.FullName -Destination $dest -Force -ErrorAction SilentlyContinue }
}

Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::CreateFromDirectory($Copy, $Zip, [System.IO.Compression.CompressionLevel]::Optimal, $false)
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1560.001/T1560.001.yaml)
