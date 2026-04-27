---
atomic_guid: "d07e4cc1-98ae-447e-9d31-36cb430d28c4"
title: "PowerView ShareFinder"
framework: "atomic"
generated: "true"
attack_technique_id: "T1135"
attack_technique_name: "Network Share Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "d07e4cc1-98ae-447e-9d31-36cb430d28c4"
  - "PowerView ShareFinder"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# PowerView ShareFinder

PowerView is a PowerShell tool to gain network situational awareness on Windows domains. ShareFinder finds (non-standard) shares on machines in the domain.

## Metadata

- Atomic GUID: d07e4cc1-98ae-447e-9d31-36cb430d28c4
- Technique: T1135: Network Share Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1135/T1135.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1135-network_share_discovery|T1135]]

## Input Arguments

### parameters

- description: ShareFinder parameter
- type: string
- default: -CheckShareAccess

## Dependencies

Invoke-ShareFinder module must exist in %TEMP% directory

### Prerequisite Check

```untitled
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\PowerView.ps1") {exit 0} else {exit 1}
```

### Get Prerequisite

```untitled
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://raw.githubusercontent.com/darkoperator/Veil-PowerView/8784e33f17ee7543ba2f45e27dc5f08ea3a1b856/PowerView/powerview.ps1" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\PowerView.ps1"
```

## Executor

- name: powershell

### Command

```powershell
Import-Module "PathToAtomicsFolder\..\ExternalPayloads\PowerView.ps1"
Invoke-ShareFinder #{parameters}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1135/T1135.yaml)
