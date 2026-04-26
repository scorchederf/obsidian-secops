---
atomic_guid: "d3d9af44-b8ad-4375-8b0a-4bff4b7e419c"
title: "Search files of interest and save them to a single zip file (Windows)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1005"
attack_technique_name: "Data from Local System"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1005/T1005.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "d3d9af44-b8ad-4375-8b0a-4bff4b7e419c"
  - "Search files of interest and save them to a single zip file (Windows)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Search files of interest and save them to a single zip file (Windows)

This test searches for files of certain extensions and saves them to a single zip file prior to extraction.

## Metadata

- Atomic GUID: d3d9af44-b8ad-4375-8b0a-4bff4b7e419c
- Technique: T1005: Data from Local System
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1005/T1005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1005-data_from_local_system|T1005]]

## Input Arguments

### file_extensions

- description: List of file extensions to be searched and zipped, separated by comma and space
- type: string
- default: .doc, .docx, .txt

### output_zip_folder_path

- description: Path to directory for saving the generated zip file
- type: Path
- default: PathToAtomicsFolder\..\ExternalPayloads\T1005

### starting_directory

- description: Path to starting directory for the search
- type: Path
- default: C:\Users

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$startingDirectory = "#{starting_directory}"
$outputZip = "#{output_zip_folder_path}"
$fileExtensionsString = "#{file_extensions}" 
$fileExtensions = $fileExtensionsString -split ", "

New-Item -Type Directory $outputZip -ErrorAction Ignore -Force | Out-Null

Function Search-Files {
  param (
    [string]$directory
  )
  $files = Get-ChildItem -Path $directory -File -Recurse | Where-Object {
    $fileExtensions -contains $_.Extension.ToLower()
  }
  return $files
}

$foundFiles = Search-Files -directory $startingDirectory
if ($foundFiles.Count -gt 0) {
  $foundFilePaths = $foundFiles.FullName
  Compress-Archive -Path $foundFilePaths -DestinationPath "$outputZip\data.zip"

  Write-Host "Zip file created: $outputZip\data.zip"
  } else {
      Write-Host "No files found with the specified extensions."
  }
```

### Cleanup

```powershell
Remove-Item -Path  $outputZip\data.zip -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1005/T1005.yaml)
