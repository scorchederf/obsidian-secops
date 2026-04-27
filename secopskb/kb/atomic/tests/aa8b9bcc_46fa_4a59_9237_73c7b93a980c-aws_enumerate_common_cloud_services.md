---
atomic_guid: "aa8b9bcc-46fa-4a59-9237-73c7b93a980c"
title: "AWS - Enumerate common cloud services"
framework: "atomic"
generated: "true"
attack_technique_id: "T1526"
attack_technique_name: "Cloud Service Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1526/T1526.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "aa8b9bcc-46fa-4a59-9237-73c7b93a980c"
  - "AWS - Enumerate common cloud services"
platforms:
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# AWS - Enumerate common cloud services

Upon successful execution, this test will enumerate common resources that are contained within a valid AWS account.

## Metadata

- Atomic GUID: aa8b9bcc-46fa-4a59-9237-73c7b93a980c
- Technique: T1526: Cloud Service Discovery
- Platforms: iaas:aws
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1526/T1526.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1526-cloud_service_discovery|T1526]]

## Input Arguments

### access_key

- description: AWS Access Key
- type: string

### output_directory

- description: Directory to output results to
- type: string
- default: $env:TMPDIR/aws_discovery

### profile

- description: AWS profile
- type: string

### regions

- description: AWS regions
- type: string
- default: us-east-1,us-east-2,us-west-1,us-west-2

### secret_key

- description: AWS Secret Key
- type: string

### session_token

- description: AWS Session Token
- type: string

## Dependencies

The AWS PowerShell module must be installed.

### Prerequisite Check

```powershell
try {if (Get-InstalledModule -Name AWSPowerShell -ErrorAction SilentlyContinue) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```powershell
Install-Module -Name AWSPowerShell -Force
```

## Executor

- name: powershell

### Command

```powershell
Import-Module "PathToAtomicsFolder\T1526\src\AWSDiscovery.ps1"
$access_key = "#{access_key}"
$secret_key = "#{secret_key}"
$session_token = "#{session_token}"
$aws_profile = "#{profile}"
$regions = "#{regions}"
Set-AWSAuthentication -AccessKey $access_key -SecretKey $secret_key -SessionToken $session_token -AWSProfile $aws_profile
Get-AWSDiscoveryData -Regions $regions -OutputDirectory "#{output_directory}"
Remove-BlankFiles -OutputDirectory "#{output_directory}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1526/T1526.yaml)
