---
atomic_guid: "87a4a141-c2bb-49d1-a604-8679082d8b91"
title: "Lambda Function Hijack"
framework: "atomic"
generated: "true"
attack_technique_id: "T1648"
attack_technique_name: "Serverless Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1648/T1648.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "87a4a141-c2bb-49d1-a604-8679082d8b91"
  - "Lambda Function Hijack"
platforms:
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Lambda Function Hijack

Modify an existing Lambda function to execute arbitrary code.

## Metadata

- Atomic GUID: 87a4a141-c2bb-49d1-a604-8679082d8b91
- Technique: T1648: Serverless Execution
- Platforms: iaas:aws
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1648/T1648.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1648-serverless_execution|T1648]]

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

```powershell
try {if (Get-InstalledModule -Name AWSPowerShell -ErrorAction SilentlyContinue) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```powershell
Install-Module -Name AWSPowerShell -Force
```

Terraform must be installed.

### Prerequisite Check

```powershell
terraform --version
```

### Get Prerequisite

```powershell
Write-Host "Terraform is required. Download it from https://www.terraform.io/downloads.html"
```

## Executor

- name: powershell

### Command

```powershell
Import-Module "PathToAtomicsFolder/T1648/src/T1648-1/LambdaAttack.ps1" -Force
$access_key = "#{access_key}"
$secret_key = "#{secret_key}"
$session_token = "#{session_token}"
$aws_profile = "#{profile}"
$region = "#{region}"
Set-AWSAuthentication -AccessKey $access_key -SecretKey $secret_key -SessionToken $session_token -AWSProfile $aws_profile -AWSRegion $region
Invoke-Terraform -TerraformCommand init -TerraformDirectory "PathToAtomicsFolder/T1648/src/T1648-1"
Invoke-Terraform -TerraformCommand apply -TerraformDirectory "PathToAtomicsFolder/T1648/src/T1648-1" -TerraformVariables @("profile=T1648-1", "region=$region")
Invoke-LambdaAttack -AWSProfile "T1648-1" -AWSRegion $region
```

### Cleanup

```powershell
Import-Module "PathToAtomicsFolder/T1648/src/T1648-1/LambdaAttack.ps1" -Force
$access_key = "#{access_key}"
$secret_key = "#{secret_key}"
$session_token = "#{session_token}"
$aws_profile = "#{profile}"
$region = "#{region}"
Set-AWSAuthentication -AccessKey $access_key -SecretKey $secret_key -SessionToken $session_token -AWSProfile $aws_profile -AWSRegion $region
Invoke-Terraform -TerraformCommand destroy -TerraformDirectory "PathToAtomicsFolder/T1648/src/T1648-1" -TerraformVariables @("profile=T1648-1", "region=$region")
Remove-MaliciousUser -AWSProfile "T1648-1"
Remove-TFFiles -Path "PathToAtomicsFolder/T1648/src/T1648-1/"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1648/T1648.yaml)
