---
atomic_guid: "348f4d14-4bd3-4f6b-bd8a-61237f78b3ac"
title: "Azure Persistence Automation Runbook Created or Modified"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.004"
attack_technique_name: "Valid Accounts: Cloud Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.004/T1078.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "348f4d14-4bd3-4f6b-bd8a-61237f78b3ac"
  - "Azure Persistence Automation Runbook Created or Modified"
platforms:
  - "iaas:azure"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Azure Persistence Automation Runbook Created or Modified

Identifies when an Azure Automation runbook is created or modified. An adversary may create or modify an Azure
Automation runbook to execute malicious code and maintain persistence in their target's environment.

## Metadata

- Atomic GUID: 348f4d14-4bd3-4f6b-bd8a-61237f78b3ac
- Technique: T1078.004: Valid Accounts: Cloud Accounts
- Platforms: iaas:azure
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1078.004/T1078.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

## Input Arguments

### automation_account_name

- description: Name of the automation account name
- type: string
- default: ART-AutomationAccountName-T1078-004

### resource_group

- description: Name of the resource group
- type: string
- default: ART-ResourceGroupName-T1078-004

### runbook_name

- description: Name of the runbook name
- type: string
- default: ART-RunbookName-T1078-004

## Dependencies

Check if terraform is installed.

### Prerequisite Check

```powershell
terraform version
```

### Get Prerequisite

```powershell
echo "Please install terraform via https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli (URL accurate as of Nov. 15, 2024)."
```

Check if Azure CLI and Azure Powershell are installed.

* Login to Azure CLI with "az login", and login to Azure Powershell with "Connect-AzAccount". Sessions are not shared.
* Azure Powershell used in this test as they have better automation performance and error logging than Azure CLI.

### Prerequisite Check

```powershell
try {if (Get-InstalledModule -Name Az -ErrorAction SilentlyContinue) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```powershell
$ProgressPreference = 'SilentlyContinue'; Invoke-WebRequest -Uri https://aka.ms/installazurecliwindowsx64 -OutFile .\AzureCLI.msi; Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi /quiet'; Remove-Item .\AzureCLI.msi
```

Check if the user is logged into Azure.

### Prerequisite Check

```powershell
try {if (-not (Get-AzContext)) { exit 1 } else { exit 0 }} catch {exit 1}
```

### Get Prerequisite

```powershell
echo "* Configure your Azure account using: Connect-AzAccount"
```

Create dependency resources using terraform

* If fail to meet prereq, navigate to T1078.004-2 using "cd $PathToAtomicsFolder/T1078.004/src/T1078.004-2/"
* Open the "terraform.tfvars" file and fill in the variables with your desired values.
* Re-run -GetPrereqs

### Prerequisite Check

```powershell
try {if (Test-Path "$PathToAtomicsFolder/T1078.004/src/T1078.004-2/terraform.tfstate" ){ exit 0 } else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```powershell
echo "Navigating to: $PathToAtomicsFolder/T1078.004/src/T1078.004-2/"
cd "$PathToAtomicsFolder/T1078.004/src/T1078.004-2/"
terraform init
terraform apply -auto-approve
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
New-AzAutomationRunbook -Name #{runbook_name} -Type PowerShell -ResourceGroupName #{resource_group} -Description 'my-test-runbook' -AutomationAccountName #{automation_account_name}
```

### Cleanup

```powershell
Remove-AzAutomationRunbook -AutomationAccountName #{automation_account_name} -Name #{runbook_name} -ResourceGroupName #{resource_group} -Force
Remove-AzAutomationAccount -ResourceGroupName #{resource_group} -Name #{automation_account_name} -Force
Remove-AzResourceGroup -Name #{resource_group} -Force
echo "Cleanup should be completed. Run 'terraform destroy` to ensure remaining resources are also deleted."
cd "$PathToAtomicsFolder/T1078.004/src/T1078.004-2/"
terraform destroy -auto-approve
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.004/T1078.004.yaml)
