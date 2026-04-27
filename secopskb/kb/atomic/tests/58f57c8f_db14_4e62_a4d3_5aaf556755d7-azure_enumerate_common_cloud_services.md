---
atomic_guid: "58f57c8f-db14-4e62-a4d3-5aaf556755d7"
title: "Azure - Enumerate common cloud services"
framework: "atomic"
generated: "true"
attack_technique_id: "T1526"
attack_technique_name: "Cloud Service Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1526/T1526.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "58f57c8f-db14-4e62-a4d3-5aaf556755d7"
  - "Azure - Enumerate common cloud services"
platforms:
  - "iaas:azure"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Azure - Enumerate common cloud services

Upon successful execution, this test will enumerate common resources that are contained within a valid Azure subscription.

## Metadata

- Atomic GUID: 58f57c8f-db14-4e62-a4d3-5aaf556755d7
- Technique: T1526: Cloud Service Discovery
- Platforms: iaas:azure
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1526/T1526.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1526-cloud_service_discovery|T1526]]

## Input Arguments

### client_id

- description: Azure AD client ID
- type: string

### client_secret

- description: Azure AD client secret
- type: string

### cloud

- description: Azure cloud environment
- type: string
- default: AzureCloud

### output_directory

- description: Directory to output results to
- type: string
- default: $env:TMPDIR/azure_discovery

### tenant_id

- description: Azure AD tenant ID
- type: string

## Dependencies

The Az module must be installed.

### Prerequisite Check

```powershell
try {if (Get-InstalledModule -Name Az -ErrorAction SilentlyContinue) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```powershell
Install-Module -Name Az -Force
```

## Executor

- name: powershell

### Command

```powershell
Import-Module "PathToAtomicsFolder\T1526\src\AzureDiscovery.ps1"
$client_id = "#{client_id}"
$client_secret = "#{client_secret}"
$tenant_id = "#{tenant_id}"
$environment = "#{cloud}"
Set-AzureAuthentication -ClientID $client_id -ClientSecret $client_secret -TenantID $tenant_id -Environment $environment
Get-AzureDiscoveryData -OutputDirectory "#{output_directory}" -Environment $environment
Remove-BlankFiles -OutputDirectory "#{output_directory}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1526/T1526.yaml)
