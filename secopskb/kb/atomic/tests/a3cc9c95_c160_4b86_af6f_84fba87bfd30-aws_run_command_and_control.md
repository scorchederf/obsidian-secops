---
atomic_guid: "a3cc9c95-c160-4b86-af6f-84fba87bfd30"
title: "AWS Run Command (and Control)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1651"
attack_technique_name: "Cloud Administration Command"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1651/T1651.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "a3cc9c95-c160-4b86-af6f-84fba87bfd30"
  - "AWS Run Command (and Control)"
platforms:
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# AWS Run Command (and Control)

This test simulates an adversary using the AWS Run Command service to execute commands on EC2 instances.

## Metadata

- Atomic GUID: a3cc9c95-c160-4b86-af6f-84fba87bfd30
- Technique: T1651: Cloud Administration Command
- Platforms: iaas:aws
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1651/T1651.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1651-cloud_administration_command|T1651]]

## Input Arguments

### access_key

- description: AWS Access Key
- type: string

### profile

- description: AWS profile
- type: string

### region

- description: AWS region to deploy the EC2 instance
- type: string
- default: us-east-2

### secret_key

- description: AWS Secret Key
- type: string

### session_token

- description: AWS Session Token
- type: string

## Dependencies

The AWS PowerShell module must be installed.

### Prerequisite Check

```text
try {if (Get-InstalledModule -Name AWSPowerShell -ErrorAction SilentlyContinue) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```text
Install-Module -Name AWSPowerShell -Force
```

Terraform must be installed.

### Prerequisite Check

```text
terraform --version
```

### Get Prerequisite

```text
Write-Host "Terraform is required. Download it from https://www.terraform.io/downloads.html"
```

## Executor

- name: powershell

### Command

```powershell
Import-Module "PathToAtomicsFolder/T1651/src/T1651-1/AWSSSMAttack.ps1" -Force
$access_key = "#{access_key}"
$secret_key = "#{secret_key}"
$session_token = "#{session_token}"
$aws_profile = "#{profile}"
$region = "#{region}"
Set-AWSAuthentication -AccessKey $access_key -SecretKey $secret_key -SessionToken $session_token -AWSProfile $aws_profile -AWSRegion $region
Invoke-Terraform -TerraformCommand init -TerraformDirectory "PathToAtomicsFolder/T1651/src/T1651-1"
Invoke-Terraform -TerraformCommand apply -TerraformDirectory "PathToAtomicsFolder/T1651/src/T1651-1" -TerraformVariables @("profile=T1651-1", "region=$region")
Invoke-SSMAttack -AWSProfile "T1651-1" -TerraformDirectory "PathToAtomicsFolder/T1651/src/T1651-1"
Invoke-Terraform -TerraformCommand destroy -TerraformDirectory "PathToAtomicsFolder/T1651/src/T1651-1" -TerraformVariables @("profile=T1651-1", "region=$region")
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1651/T1651.yaml)
