---
atomic_guid: "b4ca838d-d013-4461-bf2c-f7132617b409"
title: "Process Discovery - PC Hunter"
framework: "atomic"
generated: "true"
attack_technique_id: "T1057"
attack_technique_name: "Process Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "b4ca838d-d013-4461-bf2c-f7132617b409"
  - "Process Discovery - PC Hunter"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Process Discovery - PC Hunter

PC Hunter is a toolkit with access to hundreds of settings including kernels, kernel modules, processes, network, startup, and more. When abused, this tool can allow threat actors to effectively access sensitive processes, collect system information, and terminate security software.

## Metadata

- Atomic GUID: b4ca838d-d013-4461-bf2c-f7132617b409
- Technique: T1057: Process Discovery
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1057/T1057.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1057-process_discovery|T1057]]

## Input Arguments

### pchunter64_exe

- description: Process hacker installation executables.
- type: string
- default: PChunter64.exe

## Dependencies

PCHunter must be present in device

### Prerequisite Check

```text
if (Get-ChildItem -Path C:\ -Include *PCHunter64* -File -Recurse -ErrorAction SilentlyContinue) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
Write-Host Downloading PC Hunter
New-Item -Type Directory "C:\Temp\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://www.snapfiles.com/directdl/PCHunter_free.zip" -OutFile "C:\Temp\ExternalPayloads\PCHunter_free.zip"
Expand-Archive -LiteralPath 'C:\Temp\ExternalPayloads\PCHunter_free.zip' -DestinationPath C:\Temp\ExternalPayloads
Write-Host Unzipping Installing Process Hunter
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Start-Process -FilePath "C:\Temp\ExternalPayloads\PCHunter_free\#{pchunter64_exe}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.yaml)
