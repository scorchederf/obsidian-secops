---
atomic_guid: "3dab4bcc-667f-4459-aea7-4162dd2d6590"
title: "Azure - Enumerate Azure Blobs with MicroBurst"
framework: "atomic"
generated: "true"
attack_technique_id: "T1619"
attack_technique_name: "Cloud Storage Object Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1619/T1619.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "3dab4bcc-667f-4459-aea7-4162dd2d6590"
  - "Azure - Enumerate Azure Blobs with MicroBurst"
platforms:
  - "iaas:azure"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Azure - Enumerate Azure Blobs with MicroBurst

Upon successful execution, this test will utilize a wordlist to enumerate the public facing containers and blobs of a specified Azure storage account. 
See https://www.netspi.com/blog/technical/cloud-penetration-testing/anonymously-enumerating-azure-file-resources/ .

## Metadata

- Atomic GUID: 3dab4bcc-667f-4459-aea7-4162dd2d6590
- Technique: T1619: Cloud Storage Object Discovery
- Platforms: iaas:azure
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1619/T1619.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1619-cloud_storage_object_discovery|T1619]]

## Input Arguments

### base

- description: Azure blob keyword to enumerate (Example, storage account name)
- type: string
- default: secure

### output_file

- description: File to output results to
- type: string
- default: $env:temp\T1619Test1.txt

### wordlist

- description: File path to keywords for search permutations
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\permutations.txt

## Dependencies

The Invoke-EnumerateAzureBlobs module must exist in PathToAtomicsFolder\..\ExternalPayloads.

### Prerequisite Check

```powershell
if (test-path "PathToAtomicsFolder\..\ExternalPayloads\Invoke-EnumerateAzureBlobs.ps1"){exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
invoke-webrequest "https://raw.githubusercontent.com/NetSPI/MicroBurst/156c4e9f4253b482b2b68eda4651116b9f0f2e17/Misc/Invoke-EnumerateAzureBlobs.ps1" -outfile "PathToAtomicsFolder\..\ExternalPayloads\Invoke-EnumerateAzureBlobs.ps1"
```

The wordlist file for search permutations must exist in PathToAtomicsFolder\..\ExternalPayloads.

### Prerequisite Check

```powershell
if (test-path "#{wordlist}"){exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
invoke-webrequest "https://raw.githubusercontent.com/NetSPI/MicroBurst/156c4e9f4253b482b2b68eda4651116b9f0f2e17/Misc/permutations.txt" -outfile "#{wordlist}"
```

## Executor

- name: powershell

### Command

```powershell
import-module "PathToAtomicsFolder\..\ExternalPayloads\Invoke-EnumerateAzureBlobs.ps1"
Invoke-EnumerateAzureBlobs -base #{base} -permutations "#{wordlist}" -outputfile "#{output_file}"
```

### Cleanup

```powershell
remove-item #{output_file} -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1619/T1619.yaml)
