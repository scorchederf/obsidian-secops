---
atomic_guid: "52778a8f-a10b-41a4-9eae-52ddb74072bf"
title: "MSFT Get-GPO Cmdlet"
framework: "atomic"
generated: "true"
attack_technique_id: "T1615"
attack_technique_name: "Group Policy Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1615/T1615.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "52778a8f-a10b-41a4-9eae-52ddb74072bf"
  - "MSFT Get-GPO Cmdlet"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# MSFT Get-GPO Cmdlet

The Get-GPO cmdlet gets one Group Policy Object (GPO) or all the GPOs in a domain. Tested on Windows Server 2019 as a domain user with computer joined to domain. Reference: https://docs.microsoft.com/en-us/powershell/module/grouppolicy/get-gpo?view=windowsserver2022-ps

## Metadata

- Atomic GUID: 52778a8f-a10b-41a4-9eae-52ddb74072bf
- Technique: T1615: Group Policy Discovery
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1615/T1615.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1615-group_policy_discovery|T1615]]

## Input Arguments

### gpo_output

- description: The output of the Get-GPO cmdlet
- type: string
- default: $env:temp\GPO_Output.txt

### gpo_param

- description: You can specify a GPO by its display name or by its globally unique identifier (GUID) to get a single GPO, or you can get all the GPOs in the domain through the All parameter
- type: string
- default: -All

## Dependencies

Add Rsat.ActiveDirectory.DS

### Prerequisite Check

```powershell
if(Get-WindowsCapability -Online -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0 | Where-Object { $_.State -eq 'Installed' }){ exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
Add-WindowsCapability -online -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0
```

Add Rsat.GroupPolicy.Management.Tools ###Two RSAT Modules needed for this to work on Win10, WinServer 2019 works by default. This will take a long time (almost 2 minutes) to install RSAT Manually###.

### Prerequisite Check

```powershell
if(Get-WindowsCapability -Online -Name Rsat.GroupPolicy.Management.Tools~~~~0.0.1.0 | Where-Object { $_.State -eq 'Installed' }){ exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
Add-WindowsCapability -online -Name Rsat.GroupPolicy.Management.Tools~~~~0.0.1.0
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Get-GPO -Domain $ENV:userdnsdomain #{gpo_param} >> #{gpo_output}
```

### Cleanup

```powershell
del $env:temp\GPO_Output.txt -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1615/T1615.yaml)
