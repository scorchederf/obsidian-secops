---
atomic_guid: "26a18d3d-f8bc-486b-9a33-d6df5d78a594"
title: "Azure Security Scan with SkyArk"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "26a18d3d-f8bc-486b-9a33-d6df5d78a594"
  - "Azure Security Scan with SkyArk"
platforms:
  - "azure-ad"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Azure Security Scan with SkyArk

Upon successful execution, this test will utilize a valid read-only Azure AD user's credentials to conduct a security scan and determine what users exist in a given tenant, as well as identify any admin users. 
Once the test is complete, a folder will be output to the temp directory that contains 3 csv files which provide info on the discovered users. 
See https://github.com/cyberark/SkyArk

## Metadata

- Atomic GUID: 26a18d3d-f8bc-486b-9a33-d6df5d78a594
- Technique: T1082: System Information Discovery
- Platforms: azure-ad
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1082/T1082.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Input Arguments

### password

- description: Azure AD password
- type: string
- default: T1082Az

### username

- description: Azure AD username
- type: string

## Dependencies

The SkyArk AzureStealth module must exist in PathToAtomicsFolder\..\ExternalPayloads.

### Prerequisite Check

```text
if (test-path "PathToAtomicsFolder\..\ExternalPayloads\AzureStealth.ps1"){exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
invoke-webrequest "https://raw.githubusercontent.com/cyberark/SkyArk/3293ee145e95061a8980dd7b5da0030edc4da5c0/AzureStealth/AzureStealth.ps1" -outfile "PathToAtomicsFolder\..\ExternalPayloads\AzureStealth.ps1"
```

The AzureAD module must be installed.

### Prerequisite Check

```text
try {if (Get-InstalledModule -Name AzureAD -ErrorAction SilentlyContinue) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```text
Install-Module -Name AzureAD -Force
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

- elevation_required: True
- name: powershell

### Command

```powershell
Import-Module "PathToAtomicsFolder\..\ExternalPayloads\AzureStealth.ps1" -force      
$Password = ConvertTo-SecureString -String "#{password}" -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{username}", $Password
Connect-AzAccount -Credential $Credential
Connect-AzureAD -Credential $Credential
Scan-AzureAdmins -UseCurrentCred
```

### Cleanup

```powershell
$resultstime = Get-Date -Format "yyyyMMdd"
$resultsfolder = ("Results-" + $resultstime)
remove-item $env:temp\$resultsfolder -recurse -force -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
