---
atomic_guid: "1e40bb1d-195e-401e-a86b-c192f55e005c"
title: "Azure - Dump Subscription Data with MicroBurst"
framework: "atomic"
generated: "true"
attack_technique_id: "T1526"
attack_technique_name: "Cloud Service Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1526/T1526.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "1e40bb1d-195e-401e-a86b-c192f55e005c"
  - "Azure - Dump Subscription Data with MicroBurst"
platforms:
  - "iaas:azure"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Azure - Dump Subscription Data with MicroBurst

Upon successful execution, this test will enumerate all resources that are contained within a valid Azure subscription. 
The resources enumerated will display on screen, as well as several csv files and folders will be output to a specified directory, listing what resources were discovered by the script. 
See https://dev.to/cheahengsoon/enumerating-subscription-information-with-microburst-35a1

## Metadata

- Atomic GUID: 1e40bb1d-195e-401e-a86b-c192f55e005c
- Technique: T1526: Cloud Service Discovery
- Platforms: iaas:azure
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1526/T1526.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1526-cloud_service_discovery|T1526]]

## Input Arguments

### output_directory

- description: Directory to output results to
- type: string
- default: $env:temp\T1526Test1

### password

- description: Azure AD password
- type: string
- default: T1082Az

### subscription_name

- description: Azure subscription name to scan
- type: string

### username

- description: Azure AD username
- type: string

## Dependencies

The Get-AzDomainInfo script must exist in PathToAtomicsFolder\..\ExternalPayloads.

### Prerequisite Check

```text
if (test-path "PathToAtomicsFolder\..\ExternalPayloads\Get-AzDomainInfo.ps1"){exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
invoke-webrequest "https://raw.githubusercontent.com/NetSPI/MicroBurst/c771c665a2c71f9c5ba474869cd1c211ebee68fd/Az/Get-AzDomainInfo.ps1" -outfile "PathToAtomicsFolder\..\ExternalPayloads\Get-AzDomainInfo.ps1"
```

The Az module must be installed.

### Prerequisite Check

```text
try {if (Get-InstalledModule -Name Az -ErrorAction SilentlyContinue) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```text
Install-Module -Name Az -Force
```

## Executor

- name: powershell

### Command

```powershell
import-module "PathToAtomicsFolder\..\ExternalPayloads\Get-AzDomainInfo.ps1"
$Password = ConvertTo-SecureString -String "#{password}" -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{username}", $Password
Connect-AzAccount -Credential $Credential | out-null
Get-AzDomainInfo -folder #{output_directory} -subscription "#{subscription_name}" -verbose
```

### Cleanup

```powershell
remove-item #{output_directory} -recurse -force -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1526/T1526.yaml)
