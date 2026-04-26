---
atomic_guid: "5e09bed0-7d33-453b-9bf3-caea32bff719"
title: "Azure - Eventhub Deletion"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.008"
attack_technique_name: "Impair Defenses: Disable Cloud Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.008/T1562.008.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "5e09bed0-7d33-453b-9bf3-caea32bff719"
  - "Azure - Eventhub Deletion"
platforms:
  - "iaas:azure"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Azure - Eventhub Deletion

Identifies an Event Hub deletion in Azure.
An Event Hub is an event processing service that ingests and processes large volumes of events and data.
An adversary may delete an Event Hub in an attempt to evade detection.
https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-about.

## Metadata

- Atomic GUID: 5e09bed0-7d33-453b-9bf3-caea32bff719
- Technique: T1562.008: Impair Defenses: Disable Cloud Logs
- Platforms: iaas:azure
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1562.008/T1562.008.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.008]]

## Input Arguments

### event_hub_name

- description: Name of the eventhub
- type: string
- default: test_eventhub

### name_space_name

- description: Name of the NameSpace
- type: string

### password

- description: Azure password
- type: string

### resource_group

- description: Name of the resource group
- type: string

### username

- description: Azure username
- type: string

## Dependencies

Install-Module -Name Az

### Prerequisite Check

```text
try {if (Get-InstalledModule -Name AzureAD -ErrorAction SilentlyContinue) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```text
Install-Module -Name AzureAD -Force
```

Check if terraform is installed.

### Prerequisite Check

```text
terraform version
```

### Get Prerequisite

```text
echo Please install the terraform.
```

Check if the user is logged into Azure.

### Prerequisite Check

```text
az account show
```

### Get Prerequisite

```text
echo Configure your Azure account using: az login.
```

Create dependency resources using terraform

### Prerequisite Check

```text
try {if (Test-Path "$PathToAtomicsFolder/T1562.008/src/T1562.008-2/terraform.tfstate" ){ exit 0 } else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```text
cd "$PathToAtomicsFolder/T1562.008/src/T1562.008-2/"
terraform init
terraform apply -auto-approve
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$secure_pwd = "#{password}" | ConvertTo-SecureString -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential -ArgumentList "#{username}", $secure_pwd
Connect-AzureAD -Credential $creds
Remove-AzEventHub -ResourceGroupName #{resource_group} -Namespace #{name_space_name} -Name #{event_hub_name}
```

### Cleanup

```powershell
cd "$PathToAtomicsFolder/T1562.008/src/T1562.008-2/"
terraform destroy -auto-approve
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.008/T1562.008.yaml)
