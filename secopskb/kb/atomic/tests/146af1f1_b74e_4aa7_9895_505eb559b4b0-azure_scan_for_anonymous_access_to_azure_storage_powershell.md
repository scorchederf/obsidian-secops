---
atomic_guid: "146af1f1-b74e-4aa7-9895-505eb559b4b0"
title: "Azure - Scan for Anonymous Access to Azure Storage (Powershell)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1619"
attack_technique_name: "Cloud Storage Object Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1619/T1619.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "146af1f1-b74e-4aa7-9895-505eb559b4b0"
  - "Azure - Scan for Anonymous Access to Azure Storage (Powershell)"
platforms:
  - "iaas:azure"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Azure - Scan for Anonymous Access to Azure Storage (Powershell)

Upon successful execution, this test will test for anonymous access to Azure storage containers by invoking a web request and outputting the results to a file. 
The corresponding response could then be interpreted to determine whether or not the resource/container exists, as well as other information. 
See https://ninocrudele.com/the-three-most-effective-and-dangerous-cyberattacks-to-azure-and-countermeasures-part-2-attack-the-azure-storage-service

## Metadata

- Atomic GUID: 146af1f1-b74e-4aa7-9895-505eb559b4b0
- Technique: T1619: Cloud Storage Object Discovery
- Platforms: iaas:azure
- Executor: powershell
- Source Path: atomics/T1619/T1619.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1619-cloud_storage_object_discovery|T1619]]

## Input Arguments

### base_name

- description: Azure storage account name to test
- type: string
- default: T1619Test2

### blob_name

- description: Blob name to search for (optional)
- type: string

### container_name

- description: Container name to search for (optional)
- type: string

### output_file

- description: File to output results to
- type: string
- default: $env:temp\T1619Test2.txt

## Executor

- name: powershell

### Command

```powershell
try{$response = invoke-webrequest "https://#{base_name}.blob.core.windows.net/#{container_name}/#{blob_name}" -method "GET"}
catch [system.net.webexception]
{if($_.Exception.Response -ne $null)
{$Response = $_.Exception.Response.GetResponseStream()
$ReadResponse = New-Object System.IO.StreamReader($Response)
$ReadResponse.BaseStream.Position = 0
$responseBody = $ReadResponse.ReadToEnd()}
else {$responseBody = "The storage account could not be anonymously accessed."}}
"Response received for #{base_name}.blob.core.windows.net/#{container_name}/#{blob_name}: $responsebody" | out-file -filepath #{output_file} -append
```

### Cleanup

```powershell
remove-item #{output_file} -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1619/T1619.yaml)
