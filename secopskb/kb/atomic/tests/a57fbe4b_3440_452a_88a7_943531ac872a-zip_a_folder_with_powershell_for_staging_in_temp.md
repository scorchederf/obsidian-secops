---
atomic_guid: "a57fbe4b-3440-452a-88a7-943531ac872a"
title: "Zip a Folder with PowerShell for Staging in Temp"
framework: "atomic"
generated: "true"
attack_technique_id: "T1074.001"
attack_technique_name: "Data Staged: Local Data Staging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1074.001/T1074.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "a57fbe4b-3440-452a-88a7-943531ac872a"
  - "Zip a Folder with PowerShell for Staging in Temp"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Zip a Folder with PowerShell for Staging in Temp

Use living off the land tools to zip a file and stage it in the Windows temporary folder for later exfiltration. Upon execution, Verify that a zipped folder named Folder_to_zip.zip
was placed in the temp directory.

## Metadata

- Atomic GUID: a57fbe4b-3440-452a-88a7-943531ac872a
- Technique: T1074.001: Data Staged: Local Data Staging
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1074.001/T1074.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1074-data_staged|T1074.001]]

## Input Arguments

### input_file

- description: Location of file or folder to zip
- type: path
- default: PathToAtomicsFolder\T1074.001\bin\Folder_to_zip

### output_file

- description: Location to save zipped file or folder
- type: path
- default: $env:TEMP\Folder_to_zip.zip

## Executor

- name: powershell

### Command

```powershell
Compress-Archive -Path "#{input_file}" -DestinationPath #{output_file} -Force
```

### Cleanup

```powershell
Remove-Item -Path #{output_file} -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1074.001/T1074.001.yaml)
